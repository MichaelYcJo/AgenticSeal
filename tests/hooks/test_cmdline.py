"""`hooks/lib/cmdline.py`, the wider reading of a command's text, one class per
function the cases call by name.

Every case reads a command with no git and no shell, through the reader
itself. Its readers are the worktree guard's wider reading
(`hooks/worktree-guard.py`, `wide`), `hooks/implementer-notice.py` and
`hooks/lib/tokens.py#without_bodies`. The commit gate's text reading, which this
module was written for, went with #1027's phase 5, and the cases that read a
command through it, or through the directory walk only it reached, went with
it.
"""

import os
import sys

import pytest
from conftest import HOOKS, census_case, load_hook_module, sh

TARGET = "hooks/lib/cmdline.py"

sys.path.insert(0, os.path.join(HOOKS, "lib"))
import cmdline  # noqa: E402  -- the plain name the hooks import

reader = load_hook_module("lib/cmdline.py", "cmdline_cd")


def joined(command):
    """The operator that joined each segment to the one before it."""
    items, clean = reader.split_segments_with_separators(command)
    assert clean, command
    return [sep for sep, _ in items]


# --- a commit behind a wrapper (#670) ----------------------------------------

C = "git commit -m x"
UNRESOLVED, HERE = "unresolved", "here"

# #670's four wrappers and the rest of the enumeration, each in the shape it
# is used in: directly in front of `git` it keeps the directory, behind its
# own operand or option it does not.
WRAPPED = {
    "exec": (f"exec {C}", HERE),
    "nice": (f"nice {C}", HERE),
    "nice -n": (f"nice -n 5 {C}", UNRESOLVED),
    "timeout": (f"timeout 5 {C}", UNRESOLVED),
    "xargs": (f"echo a | xargs {C}", HERE),
    "xargs -I": (f"echo a | xargs -I{{}} {C}", UNRESOLVED),
    "stdbuf": (f"stdbuf -oL {C}", UNRESOLVED),
    "setsid": (f"setsid {C}", HERE),
    "ionice": (f"ionice -c 3 {C}", UNRESOLVED),
    "taskset": (f"taskset 1 {C}", UNRESOLVED),
    "chrt": (f"chrt -i 0 {C}", UNRESOLVED),
    "flock": (f"flock /tmp/l {C}", UNRESOLVED),
    "chroot": (f"chroot / {C}", UNRESOLVED),
    "unshare": (f"unshare -r {C}", UNRESOLVED),
    "nsenter": (f"nsenter -t 1 {C}", UNRESOLVED),
    "prlimit": (f"prlimit --nofile=10 {C}", UNRESOLVED),
    "setpriv": (f"setpriv --reuid=1 {C}", UNRESOLVED),
    "runuser": (f"runuser -u u -- {C}", UNRESOLVED),
    "doas": (f"doas {C}", HERE),
    "pkexec": (f"pkexec {C}", HERE),
    "caffeinate": (f"caffeinate -i {C}", UNRESOLVED),
    "arch": (f"arch -arm64 {C}", UNRESOLVED),
    "strace": (f"strace -f {C}", UNRESOLVED),
    "ltrace": (f"ltrace {C}", HERE),
    "valgrind": (f"valgrind {C}", HERE),
    "gtimeout": (f"gtimeout 5 {C}", UNRESOLVED),
    "gnice": (f"gnice {C}", HERE),
    "gnohup": (f"gnohup {C}", HERE),
    "gstdbuf": (f"gstdbuf -oL {C}", UNRESOLVED),
    "genv": (f"genv -i {C}", UNRESOLVED),
    "gchroot": (f"gchroot / {C}", UNRESOLVED),
    "runcon": (f"runcon -t t {C}", UNRESOLVED),
    "find -exec": (f"find . -name f -exec {C} {{}} +", UNRESOLVED),
    "parallel": (f"parallel {C} ::: a", HERE),
    "watch -n": (f"watch -n 5 {C}", UNRESOLVED),
    "script, argv form": (f"script /dev/null {C}", UNRESOLVED),
    # The five the base already named, behind an option it stopped at.
    "env -i": (f"env -i {C}", UNRESOLVED),
    "sudo -u": (f"sudo -u a {C}", UNRESOLVED),
    "command -p": (f"command -p {C}", UNRESOLVED),
    # zsh's precommand modifiers and `repeat N` (round 1 of 1790660768,
    # yellow 5). zsh 5.9 committed for each.
    "noglob": (f"noglob {C}", HERE),
    "nocorrect": (f"nocorrect {C}", HERE),
    "repeat": (f"repeat 1 {C}", UNRESOLVED),
}


MERGED = {
    "2>&1": ("a 2>&1 b", ["a", "2>&1", "b"]),
    ">&2": (">&2 a", [">&2", "a"]),
    "<&0": ("<&0 a", ["<&0", "a"]),
    ">&-": ("a >&- b", ["a", ">&-", "b"]),
    ">|f": ("a >|f b", ["a", ">|f", "b"]),
    "&>f after a word": ("a &>f b", ["a", "&>f", "b"]),
    "&>>f after a word": ("a &>>f b", ["a", "&>>f", "b"]),
    "a chain": ("a >&2 2>&1 b", ["a", ">&2", "2>&1", "b"]),
    "{fd}>&1": ("a {fd}>&1 b", ["a", "{fd}>&1", "b"]),
}

SEPARATE = {
    "a background job": ("a & b", []),
    "a pipe": ("a | b", []),
    "a list": ("a && b", []),
    "a redirection with its target, then a job": ("a > f & b", []),
    "&& before a redirection": ("a && >f b", []),
    "|| before a redirection": ("a || >f b", []),
    "; before a redirection": ("a; >f b", []),
    # bash refuses a bare operator before a list operator, and the view does
    # not make one up either.
    "a bare operator before &&": ("a > && b", []),
    "a bare operator before ;": ("a 2> ; b", []),
    "2>&1, then a list": ("a 2>&1 && b", [["a", "2>&1"]]),
    # A redirection that already carries its target is whole, so the `|`
    # after it is a pipe; and `|` before a `>` is a pipe, where only `&`
    # before one spells `&>`.
    "a redirection carrying its target, then a pipe": ("a 2>f | b", []),
    "a pipe before a redirection": ("a | >f b", []),
}

# Each body `drop_heredoc_bodies` drops, beside the text it leaves.
DROPPED = {
    # A `#` inside `${…}` opens no comment, so the `}` closes the expansion
    # and the heredoc on the next line opens. Read as a comment, the `#`
    # would swallow the `}`, hold the brace count open, and leave the body
    # in as commands.
    "a heredoc after a hash inside an expansion": (
        "echo ${x:-a #b}\ncat <<EOF\ncd /elsewhere\nEOF\ngit commit -m x",
        "echo ${x:-a #b}\ncat <<EOF\ngit commit -m x",
    ),
    # `<<-` strips leading tabs from the body and from its closing line, so
    # a tabbed `EOF` ends the body.
    "a dashed heredoc closed by a tabbed delimiter": (
        "cat <<-EOF\n\tcd /elsewhere\n\tEOF\ngit commit -m x",
        "cat <<-EOF\ngit commit -m x",
    ),
}

# --- the readers, one rule each ---------------------------------------------
#
# A body the shell would close later than the reader does loses the commands
# after the early close, and a body it closes earlier reads text as commands,
# so each rule is pinned here on the body itself.

BODIES = {
    "a plain one": ("echo $(a b)", ["a b"]),
    "a `)` in double quotes": ('echo $(printf ")") x', ['printf ")"']),
    "a `)` in single quotes": ("echo $(printf ')') x", ["printf ')'"]),
    "an escaped `)`": ("echo $(printf \\)) x", ["printf \\)"]),
    "a `)` in a heredoc": (
        "echo \"$(cat <<'EOF'\n)\nEOF\nb)\" x",
        ["cat <<'EOF'\n)\nEOF\nb"],
    ),
    "a `)` in a dashed heredoc": (
        "echo \"$(cat <<-'EOF'\n)\n\tEOF\nb)\" x",
        ["cat <<-'EOF'\n)\n\tEOF\nb"],
    ),
    "a case runs to the end": (
        "echo $(case x in a) b;; esac) c",
        ["case x in a) b;; esac) c"],
    ),
    "nested, outermost only": ("echo $(a $(b)) c", ["a $(b)"]),
    "backticks": ("echo `a` `b`", ["a", "b"]),
    "an escaped backtick inside": ("echo `a \\` b` c", ["a \\` b"]),
    "unterminated": ("echo $(a b", ["a b"]),
    "process substitutions": ("cat <(a) >(b)", ["a", "b"]),
    "single quotes are text": ("echo '$(a)' '`b`'", []),
    "a quoted `<(` is text": ('echo "<(a)"', []),
    "a herestring opens no heredoc": ('echo $(cat <<< "a" ; b) c', ['cat <<< "a" ; b']),
    "an apostrophe in double quotes is not a quote": ('echo "it\'s $(a)"', ["a"]),
    "a double-quoted `$(` runs": ('echo "$(a)"', ["a"]),
    "an escaped `$(` is text": ("echo \\$(a) b", []),
}

TEXTS = {
    "bash -c": (["bash", "-c", "a b"], ["a b"]),
    "a cluster holding c": (["bash", "-ec", "a b"], ["a b"]),
    "every non-option word once -c is given": (
        ["bash", "-o", "errexit", "-c", "a b"],
        ["errexit", "a b"],
    ),
    "no -c: a script, not a string": (["bash", "run.sh", "a b"], []),
    "su --command=": (["su", "--command=a b", "u"], ["u", "a b"]),
    "su --command, separate": (["su", "--command", "a b"], ["a b"]),
    "--command is su's, not a shell's": (["bash", "--command", "a b"], []),
    "watch": (["watch", "-n", "5", "a b"], ["5", "a b"]),
    # #716: the string is also read as `env`'s own words, beside the string
    # alone. The base text stays first, so every answer it gave is kept.
    "env -S": (["env", "-S", "a b"], ["a b", "env a b"]),
    "env -S glued": (["env", "-Sa b"], ["a b", "env a b"]),
    "env --split-string=": (["env", "--split-string=a b"], ["a b", "env a b"]),
    "env -S, the words around it": (
        ["env", "-v", "-S", "-i a", "b"],
        ["-i a", "env -v -i a b"],
    ),
    "env -S past a redirection": (
        ["env", "-S", "2>/dev/null", "a b", "c"],
        ["2>/dev/null", "a b", "env a b c"],
    ),
    "env -S behind a redirection": (
        ["env", "2>", "/dev/null", "-S", "a b"],
        ["a b", "env a b"],
    ),
    "env -S with no string after its redirection": (
        ["env", "-S", "2>/dev/null"],
        ["2>/dev/null"],
    ),
    "behind a runner": (["sudo", "sh", "-c", "a b"], ["a b"]),
}


# Round 2 of 1790993140: `env`'s option grammar, one case per row of
# `cmdline.ENV_OPTIONS`. Written from GNU coreutils' `src/env.c` and FreeBSD's
# `usr.bin/env/env.c` (#737), not from the table.
# GNU env is not installed here, so its half is read, not run.
ENV_SPELLINGS = {
    "-i": "-i",
    "-0": "-0",
    "-v": "-v",
    "-u": "-u FOO",
    "-C": "-C /tmp",
    "-S": "-S '-i true'",
    "-a": "-a x",
    "-P": "-P /bin",
    "-L": "-L user",
    "-U": "-U user",
    "--ignore-environment": "--ignore-environment",
    "--null": "--null",
    "--debug": "--debug",
    "--unset": "--unset FOO",
    "--chdir": "--chdir /tmp",
    "--split-string": "--split-string '-i true'",
    "--argv0": "--argv0 x",
    "--block-signal": "--block-signal",
    "--default-signal": "--default-signal",
    "--ignore-signal": "--ignore-signal",
    "--list-signal-handling": "--list-signal-handling",
    "--env0-from": "--env0-from f",
    "--quoting-style": "--quoting-style shell",
    "--help": "--help",
    "--version": "--version",
}


class Test_module:
    def test_the_old_splitter_answers_exactly_what_it_always_did(self):
        """`split_segments`' callers read the two-element tuple; the separator
        arrives beside it rather than inside it."""
        assert reader.split_segments("cd /tmp/x && git commit") == (
            [["cd", "/tmp/x"], ["git", "commit"]],
            True,
        )

    def test_every_enumerated_wrapper_has_a_shape(self):
        """The enumeration is the set, and every member of it is exercised here.
        A wrapper added to `RUNNERS` with no shape is a reading nothing pins."""
        named = {name.split()[0].rstrip(",") for name in WRAPPED}
        missing = sorted(
            set(cmdline.RUNNERS) - named - set(cmdline.WRAPPERS) - {"time"}
        )
        assert not missing, missing

    @pytest.mark.parametrize("name", sorted(BODIES))
    def test_substitution_bodies(self, name):
        command, bodies = BODIES[name]
        assert cmdline.substitution_bodies(command) == bodies, name

    @pytest.mark.parametrize("name", sorted(TEXTS))
    def test_reparsed_texts(self, name):
        tokens, texts = TEXTS[name]
        assert cmdline.reparsed_texts(tokens) == texts, name

    def test_every_row_of_the_env_grammar_has_a_case(self):
        rows = set()
        for short, long, _value in cmdline.ENV_OPTIONS:
            rows |= {f"-{short}"} if short else set()
            rows |= {long} if long else set()
        assert rows == set(ENV_SPELLINGS), rows ^ set(ENV_SPELLINGS)

    def test_an_ambiguous_prefix_names_no_long_option(self):
        """GNU's getopt refuses a prefix of two long names (`--i`, `--d`), and env
        then runs nothing; one long name's prefix is that name."""
        assert cmdline._env_long("--i", True) is None
        assert cmdline._env_long("--d", True) is None
        assert cmdline._env_long("--un", True) == "--unset"
        assert cmdline._env_long("--un", False) is None


class Test__env_walk:
    @pytest.mark.parametrize("grammar", ["gnu", "bsd"])
    def test_accepts_the_word_after_a_cluster_ending_in_s_as_its_value(self, grammar):
        """The word after `-iS` is the split string, never one of env's words.
        An empty string splits into no word, so env's options run on to the
        `-vS` after it, and the string that one names is read. Read as a word
        of its own, the empty string would end env's options and leave
        `git commit` unread: the silence, where an extra reading costs a stop."""
        rest = ["-iS", "", "-vS", "git commit"]
        assert "git commit" in cmdline._env_walk("env", rest, grammar, False)

    def test_refuses_a_cluster_with_no_split_letter_as_a_string(self):
        """No letter of `-iv` takes the split string, so the word after it is
        the command env runs, and no string is read."""
        assert cmdline._env_walk("env", ["-iv", "git commit"], "gnu", False) == []


class Test_split_segments:
    def test_accepts_a_quoted_newline_as_part_of_one_argument(self):
        """An unquoted newline ends a segment; a quoted one is the argument's."""
        assert reader.split_segments('git commit -m "a\nb"') == (
            [["git", "commit", "-m", "a\nb"]],
            True,
        )

    def test_refuses_an_unclosed_quote_as_a_clean_split(self):
        """A quote that never closes ends the split, and the answer says so:
        the words before it are kept, and the split is not clean."""
        assert reader.split_segments('git commit -m "a b') == (
            [["git", "commit", "-m"]],
            False,
        )


class Test_split_segments_with_separators:
    def test_accepts_the_operator_that_joined_two_segments(self):
        """`&&` and `||` are opposites in a shell and were indistinguishable here.

        Measured on the unfixed module: all three forms returned
        `[['cd','/tmp/x'], ['git','commit']]`, so a design judging only the `cd`
        destination would judge the wrong repository with confidence on `||`, and
        one judging every reachable directory would keep asking about the
        session's own on `&&`.
        """
        for sep in ("&&", ";", "||", "|"):
            assert joined(f"cd /tmp/x {sep} git commit") == ["", sep], sep

    def test_refuses_the_newline_after_an_operator_as_the_one_that_binds(
        self, tmp_path
    ):
        """`&&` at the end of a line is `&&`, not the newline that follows it."""
        b = tmp_path / "b"
        items, _ = reader.split_segments_with_separators(
            f"cd {sh(b)} &&\ngit commit -m x"
        )
        assert [s for s, _ in items] == ["", "&&"]

    def test_an_operator_at_the_end_of_a_line_is_still_that_operator(self, tmp_path):
        """A newline behind an operator glued itself onto it.

        The newline is converted to `;` character by character, and shlex groups a
        RUN of punctuation into ONE token — so `cd <B> ||` followed by a newline
        arrived as the single token `||;`, which is neither a branching operator
        nor a plain `;`. Measured tokens: `||;`, `|;`, `&;`.

        Writing the operator at the end of the line is the ordinary way to write a
        long command, so this is the common form rather than a constructed one.
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

    def test_refuses_an_unclosed_quote_as_a_clean_split(self):
        """The segments read before the quote that never closes are kept, with
        their operator, and the split says it failed."""
        assert reader.split_segments_with_separators('cd /x && echo "a b') == (
            [("", ["cd", "/x"]), ("&&", ["echo"])],
            False,
        )


class Test_drop_comments:
    def test_accepts_a_paren_inside_an_expansion_as_a_word_part(self):
        """Both models, not one. This is the half issue #78's title is about.

        Asserted at `drop_comments` rather than through a shell: bash rejects
        `echo ${x:-((} zz)#c` outright — `syntax error near unexpected token ')'`,
        measured — so there is no behaviour to compare against. What is being
        pinned is that the two models answer the same question the same way, which
        is what makes their answers predictable when one of them is wrong.
        """
        text = "echo ${x:-((} zz)#c ; git commit -m x"
        assert reader.drop_comments(text) == text, (
            "the `)` ended the word, the `#` opened a comment, and the commit went"
        )

    def test_refuses_a_bare_brace_as_an_expansion_opener(self):
        """A bare `{` is a group or a brace expansion, not an expansion of a name.

        Measured under bash 3.2.57: `echo { #c ; echo REACHED` prints `{` and does
        NOT reach the next command, so bash opens a comment there. Counting a bare
        `{` would hold the expansion open past the `}` that never comes and leave
        the comment standing.
        """
        assert reader.drop_comments("echo { #c ; git commit -m x") == "echo { "

    def test_a_hash_inside_a_parameter_expansion_opens_no_comment(self):
        """The other paren model's own cost, which issue #78 reported as nothing.

        A `#` after a BLANK inside the expansion is a fail-OPEN if read as a
        comment: executed under bash 3.2.57, `echo ${x:-a #b} ; echo REACHED`
        prints `a #b` and then `REACHED`, so bash opens no comment and runs what
        follows.
        """
        assert "#b" in reader.drop_comments("echo ${x:-a #b} ; git commit -m x")

    def test_a_case_pattern_comment_does_not_take_the_segment_list(self):
        """An unbalanced `)` ends the word, which is what keeps a comment readable.

        A `case` pattern's `)` closes nothing this reader opened, and it is the
        place an unbalanced one actually occurs. Measured: bash opens a comment
        after it, and a comment left in place whose text holds an apostrophe opens
        a quote that never closes -- which took every later line, the commit
        included, out of the segment list.
        """
        command = (
            "case x in\nx)#don't\n  echo hit ;;\nesac\ncd /elsewhere && git commit -m x"
        )
        text = reader.drop_heredoc_bodies(reader.drop_comments(command))
        _, clean = reader.split_segments_with_separators(text)
        assert clean, "the apostrophe in a comment bash DOES open took the segment list"


class Test_drop_heredoc_bodies:
    def test_a_hash_inside_an_expansion_closes_no_brace_in_either_model(self):
        """Round 1: `drop_comments` got `and not braces` and the heredoc splitter
        did not, so the two models answered one question two ways.

        `${x:-a #b}` opened a comment in the splitter that swallowed the closing
        `}`, `braces` stayed 1 to the end of the input, every `((` after it
        stopped being an arithmetic region, and a `<<` inside one opened a
        heredoc that ate the rest of the command. Measured: the `git worktree
        add` below such a line left the segment list entirely and the worktree
        guard went silent on a command bash really runs, `rc=0`.
        """
        command = "echo ${x:-a #b}\n((1<<2))\ngit worktree add -b nb ../wt"
        text = reader.drop_heredoc_bodies(reader.drop_comments(command))
        items, clean = reader.split_segments_with_separators(text)
        assert clean, command
        words = [tokens for _, tokens in items]
        assert any(t[:2] == ["git", "worktree"] for t in words), (
            f"the `git worktree add` left the segment list: {words}. A `#` inside "
            "an expansion must not close the brace count in either model"
        )

    def test_refuses_a_heredoc_opener_inside_an_expansion(self):
        """Round 2: `braces` reached the `#` and `((` branches and not `<<`.

        `${x:-<<E}` opened a heredoc whose delimiter was `E}`, the closing line
        never came, and every line below it was swallowed as a body -- so a
        `git worktree add` bash really runs, `rc=0`, left the segment list
        entirely. 32 of 333 generated inputs failed open this way and every one
        was this family.
        """
        command = "echo ${x:-<<E}\ngit worktree add -b nb ../wt"
        items, clean = reader.split_segments_with_separators(
            reader.drop_heredoc_bodies(reader.drop_comments(command))
        )
        assert clean, command
        words = [tokens for _, tokens in items]
        assert any(t[:2] == ["git", "worktree"] for t in words), (
            f"the `git worktree add` left the segment list: {words}"
        )

    def test_accepts_a_heredoc_opened_after_an_unbalanced_expansion(self):
        """The guard the fix above needed, and the reason it is not one word.

        Adding `not braces` alone would let an UNBALANCED `${` hold the count to
        the end of the input, hiding every heredoc opener after it and reading a
        body as commands -- the fail-OPEN direction, and the opposite of what the
        count exists for. So an expansion counts only when a `}` closes it."""
        command = "echo ${x <<EOF\ncd /elsewhere\nEOF\ngit commit -m x"
        items, clean = reader.split_segments_with_separators(
            reader.drop_heredoc_bodies(reader.drop_comments(command))
        )
        assert clean, command
        words = [tokens for _, tokens in items]
        assert not any("cd" in t for t in words), (
            f"the heredoc body was read as commands: {words}. An unbalanced "
            "`${` must not hold the brace count open"
        )

    @pytest.mark.parametrize("name", sorted(DROPPED))
    def test_accepts_a_body_dropped_where_the_shell_ends_it(self, name):
        """This model alone, with no `drop_comments` before it: the body goes,
        and the commit after its closing line stays."""
        command, stripped = DROPPED[name]
        assert reader.drop_heredoc_bodies(command) == stripped, name


class Test_parse_git:
    def test_accepts_the_command_word_behind_a_list_opener(self, tmp_path):
        """`parse_git` is the reading the worktree guard and the implementer
        notice use, so a switch or a creation in a loop body is read as one
        too."""
        for tokens, sub in (
            (["do", "git", "switch", "main"], "switch"),
            (["then", "!", "git", "worktree", "add", "../wt"], "worktree"),
            (["else", "{", "git", "checkout", "main"], "checkout"),
        ):
            parsed = cmdline.parse_git(tokens)
            assert parsed and parsed[0] == sub, tokens

    def test_refuses_a_subshell_with_no_subcommand_as_a_git_invocation(self):
        """`parse_git` documents "None when no subcommand", and stripping the
        closing parenthesis could leave the empty string instead — a value that
        reads as a subcommand to anything testing it for identity."""
        assert reader.parse_git(["(", "git", ")"]) is None
        assert reader.parse_git(["(git", ")"]) is None
        assert reader.parse_git(["git"]) is None

    def test_a_redirection_with_nothing_after_it_keeps_the_base_subcommand(self):
        """The same rule one scan over: `git 2>/dev/null` names no subcommand past
        the redirection, so the answer `86256492` gave is the one returned."""
        assert cmdline.parse_git(["git", "2>/dev/null"]) == ("2>/dev/null", [], [])
        assert cmdline.parse_git(["git", "2>/dev/null", "commit"]) == (
            "commit",
            [],
            [],
        )

    def test_a_glued_config_env_reads_as_it_did(self):
        assert cmdline.parse_git(["git", "--config-env=k=v", "commit", "-m", "x"]) == (
            "commit",
            ["-m", "x"],
            [],
        )


class Test_merged_view:
    @pytest.mark.parametrize("name", sorted(MERGED))
    def test_accepts_the_cut_operators_glued_back(self, name):
        """#674, `frame/design.md` decision 3: the cut operators glued back, as a view."""
        command, tokens = MERGED[name]
        items, _clean = cmdline.split_segments_with_separators(command)
        groups = cmdline.merged_view(items)
        assert [g[1] for g in groups] == [tokens], name

    @pytest.mark.parametrize("name", sorted(SEPARATE))
    def test_refuses_to_glue_across_a_real_separator(self, name):
        """A background job, a pipe and a list are not redirections, and the
        view never glues across one."""
        command, groups = SEPARATE[name]
        items, _clean = cmdline.split_segments_with_separators(command)
        assert [g[1] for g in cmdline.merged_view(items)] == groups, name


test_census = census_case(TARGET)
