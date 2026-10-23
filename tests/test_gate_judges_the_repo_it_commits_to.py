"""The commit gate judged the shell's cwd, not the repository being committed to.

`git -C <repo> commit` names its own repository. The gate resolved everything
from the payload's `cwd` and never read the command, so a commit landing in a
repository that never opted in was gated against whichever repository the shell
happened to be sitting in — and a session testing hooks, which builds a scratch
repository and drives it with `-C` from inside the repository under
development, answered a prompt on every command.

The worktree guard was fixed for this same defect, recorded in the changelog, and its
`-C` parsing is what this gate now reads the target out of.

Reading `-C` opened a second hole (issue #56). The gate sees the command
before the shell expands it, so `git -C "$WT" commit` hands it the literal
characters `$WT` — a directory that does not exist. The gate resolved no
repository there and said nothing, which is indistinguishable from having
checked one and found it clean. Every agent in that release session was
instructed to write exactly that form, and their commits went through
unreviewed. An unresolvable target now stops the commit instead.

The cases here are `hooks/cmdline.py`'s walk: which directory each segment of a
command runs in, read with no git, for the phase of #942 that rebuilds that
module. The gate's own cases, `commit_invocations`, `commit_targets` and every
case that runs the hook, are in `tests/test_commit_review_gate.py` (#942's
phase 6).
"""

from conftest import load_hook_module, sh

reader = load_hook_module("cmdline.py", "cmdline_cd")


# --- the shell walk: which directory each segment runs in -----------------


def joined(command):
    """The operator that joined each segment to the one before it."""
    items, clean = reader.split_segments_with_separators(command)
    assert clean, command
    return [sep for sep, _ in items]


def judgment_text(command):
    """`command` as the gate's JUDGMENT read sees it.

    Resolved at call time and tolerant of a `cmdline` that predates the
    function, because these cases are run against older revisions to show
    they were red there. A helper that raises `AttributeError` is not a case
    catching a defect — it is a case that never ran, and counting it as red
    inflates the accounting exactly the way a test that cannot fail inflates
    the green.
    """
    drop = getattr(reader, "drop_heredoc_bodies", None)
    return drop(command) if drop else command


def commit_dirs(command, cwd):
    """Every directory the `git commit` in `command` may run in.

    Through the judgment read, because that is what the gate performs — a
    helper that skipped it would be asking a question no gate asks, and would
    have reported a heredoc body as commands.
    """
    items, clean = reader.split_segments_with_separators(judgment_text(command))
    assert clean, command
    out = []
    for tokens, wheres in reader.walk_directories(items, str(cwd)):
        parsed = reader.parse_git(tokens)
        if parsed and parsed[0] == "commit":
            out.extend(wheres)
    return out


def unreadable(wheres):
    return [isinstance(w, reader.Unresolved) for w in wheres]


def test_the_reader_keeps_the_operator_that_joined_two_segments():
    """`&&` and `||` are opposites in a shell and were indistinguishable here.

    Measured on the unfixed module: all three forms returned
    `[['cd','/tmp/x'], ['git','commit']]`, so a design judging only the `cd`
    destination would judge the wrong repository with confidence on `||`, and
    one judging every reachable directory would keep asking about the
    session's own on `&&`.
    """
    for sep in ("&&", ";", "||", "|"):
        assert joined(f"cd /tmp/x {sep} git commit") == ["", sep], sep


def test_the_old_splitter_answers_exactly_what_it_always_did():
    """Three call sites read the two-element tuple; the separator arrives
    beside it rather than inside it."""
    assert reader.split_segments("cd /tmp/x && git commit") == (
        [["cd", "/tmp/x"], ["git", "commit"]],
        True,
    )


def test_a_cd_carries_the_commit_that_follows_it(tmp_path):
    """`&&` runs the commit only where the `cd` arrived, so B is the answer."""
    assert commit_dirs(f"cd {sh(tmp_path / 'b')} && git commit -m x", tmp_path) == [
        str(tmp_path / "b")
    ]


def test_a_semicolon_carries_the_commit_to_both(tmp_path):
    """`;` is not `&&`, and this loop used to run both through one assertion.

    `;` runs what follows whether the `cd` succeeded or not, so a failed `cd`
    leaves the commit in the directory the shell was already in -- executed:
    `bash -c 'cd /no/such/dir ; pwd'` prints the directory it started in. The
    row was added beside the `&&` one with no grounds and pinned the defect as
    the expected answer; issue #72 names it, and this is the assertion that
    replaces it.
    """
    assert commit_dirs(f"cd {sh(tmp_path / 'b')} ; git commit -m x", tmp_path) == [
        str(tmp_path / "b"),
        str(tmp_path),
    ]


def test_a_relative_cd_composes_against_the_directory_the_shell_is_in(tmp_path):
    assert commit_dirs("cd sub && git commit -m x", tmp_path) == [str(tmp_path / "sub")]


def test_a_command_with_no_cd_still_answers_the_shells_own_directory(tmp_path):
    assert commit_dirs("git commit -m x", tmp_path) == [str(tmp_path)]


def test_or_reaches_the_directory_the_cd_did_not_leave(tmp_path):
    """`cd X || git commit` commits where the shell already was, and the
    session's own directory is what a reader dropping the operator loses."""
    assert commit_dirs(f"cd {sh(tmp_path / 'b')} || git commit -m x", tmp_path) == [
        str(tmp_path),
        str(tmp_path / "b"),
    ]


def test_a_pipeline_does_not_move_the_shell_that_commits(tmp_path):
    """Both sides of a pipeline run in subshells, so a `cd` in one does not
    move the shell the next command runs in.

    Executed: `bash -c 'cd <B> | pwd'` from `<A>` prints `<A>`. The reader
    treated `|` as ordinary sequencing and answered `<B>` alone, so a commit
    landing in the session's own repository was judged against a repository it
    never touches — and where that other repository carried a routing
    declaration, the arm went silent. `&` was already branching for exactly
    this reason; `|` and `|&` have the same property and did not get the same
    answer.
    """
    b = tmp_path / "b"
    for sep in ("|", "|&"):
        got = [
            str(w) for w in commit_dirs(f"cd {sh(b)} {sep} git commit -m x", tmp_path)
        ]
        assert str(tmp_path) in got, f"{sep}: the shell never left {tmp_path}"
        assert str(b) in got, f"{sep}: a shell with `lastpipe` set does land there"


def test_an_operator_at_the_end_of_a_line_is_still_that_operator(tmp_path):
    """A newline behind an operator glued itself onto it.

    The newline is converted to `;` character by character, and shlex groups a
    RUN of punctuation into ONE token — so `cd <B> ||` followed by a newline
    arrived as the single token `||;`, which is in neither `BRANCHING` nor the
    plain-`;` path. Measured tokens: `||;`, `|;`, `&;`.

    Writing the operator at the end of the line is the ordinary way to write a
    long command, so this is the common form rather than a constructed one,
    and it was silent where the commit before this work item stopped it.
    """
    b = tmp_path / "b"
    for sep in ("||", "|", "|&", "&"):
        items, clean = reader.split_segments_with_separators(
            f"cd {sh(b)} {sep}\ngit commit -m x"
        )
        assert clean
        assert [s for s, _ in items] == ["", sep], (
            f"{sep} followed by a newline arrived as one glued token"
        )
        got = [
            str(w) for w in commit_dirs(f"cd {sh(b)} {sep}\ngit commit -m x", tmp_path)
        ]
        assert str(tmp_path) in got, f"{sep}: the session's own directory dropped out"


def test_the_first_operator_after_a_segment_is_the_one_that_binds(tmp_path):
    """`&&` at the end of a line is `&&`, not the newline that follows it."""
    b = tmp_path / "b"
    items, _ = reader.split_segments_with_separators(f"cd {sh(b)} &&\ngit commit -m x")
    assert [s for s, _ in items] == ["", "&&"]


def test_a_branch_that_skips_a_cd_keeps_the_directory_it_skipped_from(tmp_path):
    """`cd N || cd B && git commit` reaches N and B, and the reader kept
    neither of them for the right reason.

    If the first `cd` works the second is skipped and the commit lands in N;
    if it fails the commit lands in B. The union was formed by looking only at
    the operator that FOLLOWS a segment, so the second `cd` overwrote it and N
    stopped being a candidate. A segment joined by a branching operator may
    never run, so the states in front of it have to survive past it.
    """
    n, b = tmp_path / "n", tmp_path / "b"
    got = [
        str(w)
        for w in commit_dirs(f"cd {sh(n)} || cd {sh(b)} && git commit -m x", tmp_path)
    ]
    assert str(n) in got, "the branch where the second cd is skipped"
    assert str(b) in got, "the branch where the first cd failed"


def test_a_heredoc_body_is_data_and_not_commands(tmp_path):
    """Writing a script and then committing it is ordinary, and the script is
    not a command the shell runs.

    A newline was unconditionally a segment separator, so a `cd` written INSIDE
    a heredoc body moved the reader's shell and the commit two lines later was
    judged against a repository the shell never entered. The session's own
    directory was not in the candidate list at all — this is not over-collecting
    and missing, it is being confidently wrong.

    `drop_comments` in the same module exists for the same reason: a JUDGMENT
    read has to drop what the shell will not execute.
    """
    b = tmp_path / "b"
    for opener in ("<<'EOF'", '<<"EOF"', "<<EOF", "<<-EOF"):
        command = (
            f"cat > run.sh {opener}\n"
            f"cd {sh(b)}\n"
            "make\n"
            "EOF\n"
            "git add -A && git commit -m x"
        )
        got = [str(w) for w in commit_dirs(command, tmp_path)]
        assert got == [str(tmp_path)], f"{opener}: {got}"


def test_a_herestring_is_not_a_heredoc(tmp_path):
    """`<<<` feeds one word to stdin and opens no body, so nothing after it
    may be swallowed."""
    got = [str(w) for w in commit_dirs("cat <<<hello\ngit commit -m x", tmp_path)]
    assert got == [str(tmp_path)], got


def test_a_failure_branch_survives_an_intervening_segment(tmp_path):
    """`cd <B> && make || git commit` commits where the shell is when the `cd`
    fails, and that is the session's own directory.

    Only the IMMEDIATELY next operator was consulted, so one segment between
    the `cd` and the `||` dropped the failure branch entirely. It is the
    mirror of what round 2's tagging closed, one operator further along.
    """
    b = tmp_path / "b"
    for middle in ("make", "test -f x", "git add -A", "npm run build && lint"):
        got = [
            str(w)
            for w in commit_dirs(f"cd {sh(b)} && {middle} || git commit -m x", tmp_path)
        ]
        assert str(tmp_path) in got, f"{middle}: {got}"


def test_the_common_cross_repository_form_gains_nothing(tmp_path):
    """The cost the other option would have charged, pinned so it cannot be
    paid by accident.

    `cd <repo> && git commit` is the shape this work item exists to make
    silent when the target is declared, and it is the prompt-flood direction
    issue #45 named. Carrying the failure branch must not put the session's
    own directory back into this answer.
    """
    b = tmp_path / "b"
    assert [
        str(w) for w in commit_dirs(f"cd {sh(b)} && git commit -m x", tmp_path)
    ] == [str(b)]
    # The `;` form belongs to `test_a_semicolon_carries_the_commit_to_both`
    # above and not here. `;` runs what follows whether the `cd` worked or
    # not, so a failed `cd` leaves the commit in the session's own directory,
    # and issue #72 closed that — it is a second candidate the reader offers
    # on purpose, not the cost this case exists to keep at zero.


def test_a_line_continuation_leaves_the_destination_readable(tmp_path):
    """A long command wrapped across lines is the same command.

    An escaped newline survived as a character inside the token, so `cd` read
    as a two-argument `cd` and the destination fell to unreadable. It errs
    toward stopping, but a command that passes on one line was blocked for
    being wrapped.
    """
    b = tmp_path / "b"
    got = commit_dirs(f"cd {sh(b)} \\\n&& git commit -m x", tmp_path)
    assert [str(w) for w in got] == [str(b)], got
    assert not any(isinstance(w, reader.Unresolved) for w in got)


def test_two_exclusive_branches_are_not_walked_as_one(tmp_path):
    """`cd build || cd dist` reaches build OR dist, never `build/dist`.

    The second `cd` was applied to the state the FIRST one produced, so the
    reader offered a directory no run of the command can reach. It is
    fail-closed — an extra candidate is judged rather than missed — but the
    cost is not zero: a composed path exists nowhere, so it enters the
    unreadable partition, and that partition returns before the real verdict
    is used. The phantom then replaces the answer in the prompt.
    """
    got = [
        str(w) for w in commit_dirs("cd build || cd dist && git commit -m x", tmp_path)
    ]
    assert str(tmp_path / "build" / "dist") not in got, (
        "a directory no shell run can reach was offered as a candidate"
    )
    assert str(tmp_path / "build") in got and str(tmp_path / "dist") in got


def test_a_skipped_branch_does_not_execute_the_next_one(tmp_path):
    """The tag that makes the case above work, asserted on its own.

    A state that arrived by a branch that SUCCEEDED must not run a segment
    joined by `||`, and one that arrived by a branch that FAILED must not run
    a segment joined by `&&`.
    """
    got = [
        str(w) for w in commit_dirs("cd a || cd b || cd c && git commit -m x", tmp_path)
    ]
    for name in ("a", "b", "c"):
        assert str(tmp_path / name) in got, name
    assert str(tmp_path) not in got, (
        "with every cd failing the `&&` never runs, so the session's own "
        "directory is not a landing place"
    )
    assert len(got) == 3, got


def test_the_candidate_count_stays_linear_in_the_branches(tmp_path):
    """Measured before the fix: 16 segments produced 65536 candidates and a
    non-git command took 5.8 seconds. Each `||` adds one landing place, so the
    count is the number of branches rather than two to its power."""
    command = " || ".join(f"cd d{i}" for i in range(16)) + " && git commit -m x"
    got = commit_dirs(command, tmp_path)
    assert len(got) <= 20, f"{len(got)} candidates from 16 branches"


def test_a_command_the_reader_cannot_bound_is_unreadable_rather_than_slow(
    tmp_path,
):
    """The cap, which is containment and not a fix.

    Three shapes still multiply, and the candidates in all of them are REAL
    rather than phantom: a chain of pipe stages, where the reader keeps the
    moved directory beside the unmoved one, and chains of `;` or of `&&` and
    `||`, where each one parks a further failure branch. Counting the `cd`
    segments in front of the commit, they reach the cap at seven, seven and
    nine-or-ten — and the pipe chain at six when the commit is joined by `;`,
    which parks a branch at every stage on top of the pipe keeping both. Past
    the cap the whole command reads as a directory the reader could not
    compute, which is the failure direction this module already has — a stop,
    never a guess.
    """
    # Fourteen stages, not forty: without the cap this is 16384 candidates,
    # which the reader still computes in well under a second, so the case
    # FAILS rather than hanging. A red nobody can wait for is not a red.
    command = " | ".join(f"cd d{i}" for i in range(14)) + " ; git commit -m x"
    got = commit_dirs(command, tmp_path)
    assert len(got) <= reader.STATE_CAP
    assert any(isinstance(w, reader.Unresolved) for w in got), (
        "past the cap the answer has to say it is not an answer"
    )


def test_a_pipeline_in_front_of_a_cd_does_not_hide_the_session(tmp_path):
    """The mirror of the case above: the branching operator is BEFORE the
    `cd`, so the `cd` segment itself may never run."""
    b = tmp_path / "b"
    got = [
        str(w)
        for w in commit_dirs(f"echo hi | cd {sh(b)} && git commit -m x", tmp_path)
    ]
    assert str(tmp_path) in got


def test_one_directory_is_named_once(tmp_path):
    """Two ways of reaching the same directory are one candidate, not two.
    `cd N || cd B` reached B from both branches and reported it twice."""
    n, b = tmp_path / "n", tmp_path / "b"
    got = [
        str(w)
        for w in commit_dirs(f"cd {sh(n)} || cd {sh(b)} && git commit -m x", tmp_path)
    ]
    assert len(got) == len(set(got)), got


def test_a_subshell_with_no_subcommand_is_not_a_git_invocation():
    """`parse_git` documents "None when no subcommand", and stripping the
    closing parenthesis could leave the empty string instead — a value that
    reads as a subcommand to anything testing it for identity."""
    assert reader.parse_git(["(", "git", ")"]) is None
    assert reader.parse_git(["(git", ")"]) is None
    assert reader.parse_git(["git"]) is None


def test_a_destination_the_reader_cannot_expand_is_not_a_directory(tmp_path):
    """The gate reads the command BEFORE the shell expands it, which is the
    same fact that made `git -C "$WT"` unresolvable (issue #56)."""
    for dest in ('"$WT"', "'$WT'", "/tmp/x*", "{a,b}"):
        wheres = commit_dirs(f"cd {dest} && git commit -m x", tmp_path)
        assert unreadable(wheres) == [True], dest


def test_a_subshell_does_not_hide_the_cd_by_hiding_the_word(tmp_path):
    """`(cd X && git commit)` tokenizes its first word as `(cd`, so the cd was
    invisible while the commit was not — the fail-open reproduced with one
    parenthesis. Where the commit runs cannot be read, so it is not read."""
    wheres = commit_dirs(f"(cd {sh(tmp_path / 'b')} && git commit -m x)", tmp_path)
    assert wheres and all(unreadable(wheres)), wheres


def test_cd_dash_goes_back_to_the_directory_before_it(tmp_path):
    command = f"cd {sh(tmp_path / 'b')} && cd - && git commit -m x"
    assert commit_dirs(command, tmp_path) == [str(tmp_path)]


def test_cd_dash_with_nothing_behind_it_is_unreadable(tmp_path):
    wheres = commit_dirs("cd - && git commit -m x", tmp_path)
    assert unreadable(wheres) == [True]


def test_an_unreadable_directory_still_says_what_it_could_not_read(tmp_path):
    """The prompt for an unresolved target prints the directories it could
    not identify, so the text has to survive being marked unreadable."""
    (where,) = commit_dirs('cd "$WT" && git commit -m x', tmp_path)
    assert "$WT" in str(where)
