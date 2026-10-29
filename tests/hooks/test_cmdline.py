"""`hooks/lib/cmdline.py`, the reading of a command's text, one class per
function the cases call by name.

Every case reads a command with no git and no shell, through the reader
itself. Its one reader is `hooks/implementer-notice.py`. The commit gate's
text reading, which this module was written for, went with #1027's phase 5,
and the cases that read a command through it, or through the directory walk
only it reached, went with it.
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


test_census = census_case(TARGET)
