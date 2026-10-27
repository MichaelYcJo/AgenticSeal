#!/usr/bin/env python3
"""Reading a shell command line: where one invocation ends, and what git it is.

Three readers ask questions of the string the harness hands a hook.
`hooks/worktree-guard.py`'s wider reading asks for the strings a shell is
handed and the git a redirection or a runner hides; `hooks/implementer-notice.py`
asks whether a command commits; `hooks/tokens.py#without_bodies` asks where a
here-document body is. None of them owns the answer, so it lives here.

`hooks/optin.py` states the rule this module follows: "the answer moved once
already, and four divergent copies is how half of them keep the old answer."
Copying was not what went wrong here — two gates once imported each other
instead, and that is worse. One loaded the other for `parse_git` and
`apply_chdir`, and the other loaded the first for `split_segments`;
`importlib.util.module_from_spec` does not consult `sys.modules`, so neither
load was deduplicated and the pair recursed. Measured on a merge tree built
with `git merge-file` from the two branches that each held one half: 496
executions of the two module bodies per hook event instead of two, and one
`dispatch.py pre-bash` call going from 25.7ms to 100.8ms (median of fifteen).
The verdicts were still right. The cost was the defect.

A plain filename with no hyphen is the whole fix: `import cmdline` goes
through `sys.modules` and runs once, the way `import optin` already does in
four gates.

There is no load fallback here and none is wanted. A gate that cannot read a
command line has no verdict to give, so a soft failure and a hard one are the
same silence — the difference would only be which line it happens on.
`hooks/dispatch.py:72` (`except Exception: return ""`) is what turns either
into silence, and that is the place to fix it; a `try` around the import here
would only make the silence look deliberate.
"""

import os
import re
import shlex

WRAPPERS = {"command", "env", "nohup", "time", "sudo"}

# A redirection's operator, at the start of a word (#674). The shell takes a
# redirection off the command line wherever it stands, so the word it is written
# in is neither a program nor a string a host runs -- and a reader that stopped
# at it read `2>/dev/null git commit` as no commit at all. An optional file
# descriptor comes first, a number or bash 4.1's `{name}`; longer operators are
# listed before the ones they begin with. `&>`, `&>>`, `>&`, `<&` and `>|` hold
# a character the splitter cuts at, so as single words they arrive only in
# `merged_view`; zsh's `>!` and `>>!` are read without having been run here.
_REDIRECTION = re.compile(
    r"(?:[0-9]+|\{[A-Za-z_][A-Za-z0-9_]*\})?"
    r"(?:<<<|<<-|<<|<>|<&|>&|&>>|&>|>>!|>>|>\||>!|>|<)"
)


def redirection_width(tokens, i):
    """How many of TOKENS, from I, one redirection takes -- 0 when TOKENS[I] is none.

    A target glued to its operator (`2>/dev/null`, `<<EOF`) is one word, and a
    spaced one (`2> /dev/null`, `<< EOF`) is the operator and the word after it.
    A process substitution as the target (`2> >(tee log)`) arrives from the
    splitter as several words, `>(tee` and `log)`, and runs to the one that
    closes it.

    Asked only where a program word may stand, or where a host's string is
    picked, and every reader that asks it keeps the answer it gave without it
    (`frame/design.md` decision 1 of work item 1790660768): a word that merely looks
    like a redirection there can only add a reading.
    """
    if i >= len(tokens):
        return 0
    m = _REDIRECTION.match(tokens[i])
    if not m:
        return 0
    target, j = tokens[i][m.end() :], i + 1
    if not target:
        if j >= len(tokens):
            return 1
        target, j = tokens[j], j + 1
    if target.startswith(("(", ">(", "<(")):
        depth = target.count("(") - target.count(")")
        while depth > 0 and j < len(tokens):
            depth += tokens[j].count("(") - tokens[j].count(")")
            j += 1
    return j - i


def unglued(tokens):
    """TOKENS with a redirection glued to the END of a word cut into its own
    word, or None where no word carries one (round 1 of 1790660768, yellow 4).

    `_REDIRECTION` matches at the start of a word, and a shell ends a word at
    `<` and `>` wherever they stand: `git>/dev/null commit` runs `git commit`,
    and `commit>/dev/null` is the subcommand `commit`. A descriptor in front
    (`2>f`) and bash 4.1's `{fd}>f` are the operator's own and stay whole. A
    word holding whitespace was quoted, and is an argument's, so it is not
    cut. It is read as a view BESIDE the segment, the way `merged_view` is,
    so every answer the segment gave stands and the view only adds.
    """
    out, cut = [], False
    for t in tokens:
        k = min((t.find(c) for c in "<>" if c in t), default=-1)
        if (
            k > 0
            and not t[:k].isdigit()
            and not (t[0] == "{" and t[k - 1] == "}")
            and not any(c.isspace() for c in t)
        ):
            out += [t[:k], t[k:]]
            cut = True
        else:
            out.append(t)
    return out if cut else None


# Characters after which a `#` starts a comment. A shell ends a word at these,
# and `#` opens a comment only at the start of a word: `git switch feat#1`
# names a branch, and dropping from that `#` would leave `git switch feat`.
#
# `(` and `)` are NOT here, and the reason is that neither answer is right for
# both of them. A `)` that closes `$(…)` leaves the word running — executed,
# `bash -c 'echo $(echo a)#foo && echo X'` prints `a#foo` and then `X`, so
# that `#` opens nothing — while a `)` that closes a SUBSHELL ends the word
# and the `#` after it IS a comment: `bash -c '(echo a)#x' $'\n' echo REACHED`
# prints `a` and reaches the next line.
#
# Treating every `)` as a word end deleted a command; treating none as one
# left a real comment in place, and an apostrophe inside it then opened a
# quote that never closes, which took every LATER line out of the segment
# list — the failure this function's own docstring exists to describe, and a
# commit two lines down went unseen. Both directions were measured against the
# gate, one round apart. So the loop below tracks which kind each `)` closes
# and this constant holds only the characters where there is nothing to tell
# apart.
#
# WHICH KIND, precisely. NINE openers make the `(` part of a word: `$(` (and
# `$((`), the `<(` and `>(` of a process substitution, the `(` of an array
# assignment `name=(`, and extglob's five — `@(`, `!(`, `*(`, `+(`, `?(`. Two
# close a COMMAND: a subshell's `(` and an arithmetic command's `((`.
#
# Round 4 enumerated four and declared the list closed; round 5 generated 1,815
# inputs and found the other five. The extglob half is a fail-OPEN and it hides
# from the obvious check: `bash -n` calls `ls -d @(a|b)#x ; git commit` a syntax
# error, and running it really commits, because `extglob` is a RUNTIME shopt the
# parse check cannot see. Measure this family with `bash -O extglob`, never with
# `bash -n`. Read as a command paren, the `)` ended the word, the `#` after it
# opened a comment bash does not, and the commit behind it was deleted — both
# gates silent. `release/v0.22.0` is silent too, by a different route, so it is
# not a regression; the line below is this branch's, so it is this branch's to
# get right. Reading a process
# substitution's or an array assignment's `)` as a subshell's put a comment
# where bash opens none and deleted the commit behind it — six forms, each of
# which really commits, measured under bash 3.2.57 against a scratch
# repository, silent at the revision before this one and denied after it.
# `f()` is a function definition rather than an assignment, which is why the
# preceding CHARACTER decides and not the preceding word.
WORD_BREAK = " \t\r\n;|&<>"


def drop_comments(command: str) -> str:
    """`command` with its shell comments removed, quotes respected.

    A JUDGMENT read has to do this and a CONSENT read must not; the two
    callers are `split_segments` for the first and the gates' own bare-word
    scans for the second.

    Why judgment needs it: `#` opens a comment and `\\n` closes it, so bash
    runs the next line. `shlex` with `commenters=""` — which is what keeps a
    `[worktree-ok]` written inside a comment readable — sees no comment at
    all, and an apostrophe in one is an opening quote to it. Everything after
    that point is swallowed into a string that never closes, the lexer raises,
    and every LATER line is gone from the segment list. Measured: `git status
    # don't forget` followed by `git worktree add ../wt f` runs both lines in
    bash and produced no verdict at all in the guard, while the same two lines
    without the apostrophe denied.

    Why consent must not: a retry token is written in a comment on purpose
    (`git worktree add ../wt f  # [worktree-ok]`). Dropping comments before
    looking for it would throw away the only place users put it.

    A comment ends at the newline and the newline stays, because
    `split_segments` needs it to end the segment. Escaping and quoting follow
    the same rules as the splitter below, so the two agree about which `#`
    characters are inside a string.
    """
    out, quote, esc, comment, word_start = [], None, False, False, True
    # One entry per open `(`, True when the `(` is part of a WORD rather than
    # the start of a command. See `WORD_BREAK` above for the four openers that
    # make it a word, the two that make it a command, and what each answer
    # costs.
    #
    # `braces` is how deep inside a `${…}` parameter expansion this is, and
    # `dollar` is what opens one -- the `$` immediately before the `{`, asked
    # for on its own because `word_part` is also true after `<>=!@*+?` and
    # `A={a,b}` is a brace expansion rather than an expansion of a name.
    #
    # A measured finding says this function is ignorant of `${…}` and pays nothing for
    # it, measured on six `${x:-((}#zzz` shapes. The `#` after a BLANK inside
    # one was never measured and is a fail-OPEN: bash prints `a #b` for
    # `echo ${x:-a #b} ; echo REACHED` and reaches the next command, while
    # this function returned `echo ${x:-a ` and DELETED the `git commit`
    # behind it -- both gates silent. So the state goes in for a reason of its
    # own here, and not only to keep the two paren models saying one thing.
    parens, word_part, braces, dollar = [], False, 0, False
    for ch in command:
        if comment:
            if ch == "\n":
                comment, word_start = False, True
                out.append(ch)
            continue
        if esc:
            out.append(ch)
            esc, word_start, word_part, dollar = False, False, False, False
            continue
        if quote != "'" and ch == "\\":
            out.append(ch)
            esc, word_start, word_part, dollar = True, False, False, False
            continue
        if quote:
            if ch == quote:
                quote = None
            out.append(ch)
            word_start, word_part, dollar = False, False, False
            continue
        if ch in "'\"":
            quote = ch
            out.append(ch)
            word_start, word_part, dollar = False, False, False
            continue
        if ch == "#" and word_start and not braces:
            comment = True
            continue
        out.append(ch)
        if ch == "{" and dollar:
            braces += 1
        elif ch == "}" and braces:
            braces -= 1
        if ch == "(":
            # Inside a `${…}` the parenthesis is text the expansion carries,
            # so the word runs on through the `)` that closes it. An
            # unbalanced `{` leaves this true to the end of the input, which
            # leaves a real comment standing -- the fail-CLOSED direction, and
            # the one this function's own docstring already takes.
            parens.append(word_part or bool(braces))
            word_start = True
        elif ch == ")":
            # An unbalanced `)` is not something this reader can place, and
            # ending the word is the answer that keeps a comment readable.
            # `else False` is what ENDS it. Round 4 found this fallback written
            # the other way round, against its own comment: a `case` pattern's
            # `)` — the place an unbalanced one actually occurs — left the word
            # running, the `#` after it read as no comment, and an apostrophe
            # inside that comment opened a quote that never closes. Measured:
            # bash DOES open a comment there, and the segment list came back
            # `clean=False`, which is the exact failure this function's
            # docstring exists to describe.
            word_start = not (parens.pop() if parens else False)
        else:
            word_start = ch in WORD_BREAK
        word_part = ch in "$<>=!@*+?"
        dollar = ch == "$"
    return "".join(out)


def _closes(command, i):
    """True when the `${` at `i` has a `}` that closes it.

    Round 2 asked for `not braces` on the two heredoc openers and the answer
    could not simply be added: an unbalanced `${` would then hold the count
    open to the end of the input, hide every heredoc opener after it, and
    read a heredoc BODY as commands -- the fail-OPEN direction, and the
    opposite of what the count was added for.
    `tests/test_cmdline.py` pins `echo ${x <<EOF`, which
    is exactly that shape.

    So an expansion counts only if the shell would accept it. Quotes are
    tracked because a `}` inside one closes nothing.
    """
    depth, j, n, quote = 0, i, len(command), None
    while j < n:
        ch = command[j]
        if quote:
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote = ch
        elif command.startswith("${", j):
            depth += 1
            j += 2
            continue
        elif ch == "}":
            depth -= 1
            if not depth:
                return True
        j += 1
    return False


def _heredoc_word(command, i):
    """(delimiter, index after it) for the word a `<<` redirect names.

    The delimiter may be quoted (`<<'EOF'`, `<<"EOF"`) or bare, and quoting is
    what decides whether the SHELL expands the body — which this reader does
    not care about, because it drops the body either way. What it does decide
    here is where the word ends.
    """
    out, quote, n = [], None, len(command)
    while i < n:
        ch = command[i]
        if quote:
            if ch == quote:
                quote = None
            else:
                out.append(ch)
            i += 1
            continue
        if ch in "'\"":
            quote = ch
            i += 1
            continue
        if ch == "\\" and i + 1 < n:
            out.append(command[i + 1])
            i += 2
            continue
        if ch in " \t\n;|&<>()":
            break
        out.append(ch)
        i += 1
    return "".join(out), i


def drop_heredoc_bodies(command: str) -> str:
    """`command` with heredoc BODIES removed, quotes and comments respected.

    A heredoc body is data. The shell feeds it to a command on stdin and never
    executes it, so a JUDGMENT read has to drop it — the same rule, and the
    same reason, as `drop_comments` above. Writing a script and then committing
    it is ordinary:

        cat > run.sh <<'EOF'
        cd /somewhere/else
        make
        EOF
        git add -A && git commit -m x

    Every newline was a segment separator, so the `cd` on the second line moved
    the reader's shell and the commit two lines later was judged against a
    repository the shell never entered. The session's own directory was not
    among the candidates at all: not over-collecting and missing, but
    confidently wrong. `hooks/worktree-guard.py` recorded the same residual for
    its own splitter.

    What it does NOT do, deliberately: it does not track which command owns
    which redirect, so two heredocs opened on one line have their bodies read
    off in the order the delimiters appeared, which is what a shell does. A
    `<<` inside a comment opens nothing, because a comment is not a redirect —
    without that, `echo hi # cat <<EOF` would swallow every command after it,
    which is the fail-open direction. `<<<` is a herestring and opens no body.

    Neither does `$((…))`, and that one was a defect rather than a decision.
    The `<<` in `n=$((1<<2))` is an arithmetic left shift; reading it as a
    redirect took `2))` for a delimiter and dropped every line after it until
    one matched — which no line does, so a `git commit` on the next line was
    not merely misjudged, it was gone from the segment list entirely and
    neither gate had anything to say. Arithmetic is copied through to its
    matching `))`, which is also why a `<<` inside one opens nothing.

    An unterminated body runs to the end of the input, which is what the shell
    does with one.
    """
    stripped, _bodies = _heredoc_split(command)
    return stripped


def _heredoc_split(command: str):
    """(stripped, bodies) -- the one pass `drop_heredoc_bodies` reads."""
    out, i, n = [], 0, len(command)
    bodies = []
    quote, esc, comment, word_start, pending = None, False, False, True, []
    # How deep inside a `${…}` parameter expansion this is. The `((` below is
    # arithmetic everywhere except in here, where it is text the expansion
    # carries -- see the branch for what that costs and what it buys.
    braces = 0
    while i < n:
        ch = command[i]
        if esc:
            out.append(ch)
            esc, word_start = False, False
            i += 1
            continue
        if not comment and quote != "'" and ch == "\\":
            out.append(ch)
            esc, word_start = True, False
            i += 1
            continue
        if quote:
            if ch == quote:
                quote = None
            out.append(ch)
            word_start = False
            i += 1
            continue
        if not comment and ch in "'\"":
            quote = ch
            out.append(ch)
            word_start = False
            i += 1
            continue
        if not comment and ch == "#" and word_start and not braces:
            # `and not braces` is the same guard `drop_comments` carries, and
            # it was added there and not here. Round 1 measured what that
            # cost: `${x:-a #b}` opened a comment that swallowed the closing
            # `}`, so `braces` stayed 1 to the end of the input, every `((`
            # after it stopped being an arithmetic region, and a `<<` inside
            # one opened a heredoc that ate the rest of the command. The
            # `git worktree add` below such a line left the segment list
            # entirely and the worktree guard went silent on a command bash
            # really runs. Two models of one question have to answer it the
            # same way, which is the whole subject of that finding.
            comment = True
            out.append(ch)
            i += 1
            continue
        if not comment and command.startswith("${", i) and _closes(command, i):
            # A parameter expansion. Counted rather than matched, so
            # `${x:-${y}}` closes where the shell closes it, and only `${`
            # opens one: a bare `{` is a brace expansion or a group, and
            # counting it would hold this open past the `}` that ends it.
            #
            # An unbalanced `${` leaves this open to the end of the input,
            # which is the direction that can HIDE a real `((` region and let
            # a `<<` inside it open a body. That is the fail-open direction,
            # and what bounds it is that only `${` reaches here at all --
            # quotes, escapes and comments are handled by the branches above.
            braces += 1
            out.append(command[i : i + 2])
            word_start = False
            i += 2
            continue
        if not comment and ch == "}" and braces:
            braces -= 1
            out.append(ch)
            word_start = False
            i += 1
            continue
        if not comment and (
            command.startswith("$((", i)
            or command.startswith("$[", i)
            or (not braces and command.startswith("((", i))
        ):
            # `((` needs no preceding blank, and requiring one was a
            # fail-open. `(` is a bash metacharacter, so a reserved word ENDS
            # at it: `do((`, `then((`, `else((`, `!((` and `{((` are arithmetic
            # commands to bash and were heredoc redirects to this reader, which
            # took the `<<`'s delimiter out of the expression and swallowed
            # every line after it — the `git commit` included. Measured under
            # bash 3.2.57: all five really create a commit and both gates
            # stayed silent, while the same command with ONE space was read
            # correctly. bash DOES re-parse `((` as nested subshells when
            # the arithmetic parse fails — `bash -c '((echo a) )'` prints `a`,
            # measured. Those forms are paren-balanced so stepping over them
            # changes no answer, but the sentence that stood here said no such
            # form exists and that was simply false.
            #
            # WHAT DROPPING THE BLANK COST, AND WHY `braces` IS HERE. Round 4
            # measured eight shapes by hand and reported two, both supposedly
            # rejected by `bash -n`. Round 5 generated 1,815 inputs: the real
            # number was 51, every one a `((` written inside a `${…}`
            # parameter expansion, reproduced by all seventeen operators that
            # take a WORD, and bash accepts them all. `${x:-((}` has no
            # closing paren, so the region ran to the end of the input, the
            # `<<` below was never seen as a redirect, and the heredoc body
            # stayed in as commands. (`!((<<E … ))` passes `bash -n` too, so
            # "both are rejected" was wrong twice over.)
            #
            # That family was accepted as rare and pinned by test, and a later
            # finding is what reopened it: `echo ${x:-((} <<EOF / cd <path> / EOF
            # / git commit` makes one commit in bash and never leaves its
            # directory — executed, 1 -> 2 in a scratch repository, `pwd`
            # unmoved — while the gate answered for a path that exists only in
            # the heredoc body and DENIED a commit that had already been
            # reviewed. `braces` above is that fix: a bare `((` inside `${…}`
            # is the text bash treats it as, and `$((` and `$[` stay
            # arithmetic in there because they are unambiguous.
            #
            # Skipping the region is still fail-CLOSED, for the reason below —
            # it is copied through verbatim, so widening it can only skip a
            # heredoc DELETION. NARROWING it, which `braces` does, is the
            # direction that can delete one, so `${` alone opens the count and
            # every `}` closes it: an unbalanced `{` therefore leaves this
            # reader where it already was rather than one step further.
            #
            # Quotes and comments are handled by the branches above this one,
            # so `echo '((' <<EOF` is untouched. Trading a fail-open on five
            # valid forms for a fail-closed on this family is the direction
            # this repository takes everywhere else.
            #
            # Arithmetic, not a subshell and not a redirect. Copied through to
            # the bracket that closes it: this reader has no use for the
            # value, and stepping over the region is what keeps a `<<` inside
            # it from opening a body. Nesting is counted rather than matched
            # on the first close, so `$(( (1<<2) + 3 ))` ends where the shell
            # ends it. One that never closes runs to the end of the input,
            # which is the same thing the shell's own parser does with it.
            #
            # `$[1<<2]` is the same construct in bash's older spelling, and it
            # closes on ONE bracket. Left out, it swallowed the commit below
            # it exactly as `$((1<<2))` did — executed, with the commit really
            # created and the reader's segment list holding no commit at all.
            #
            # Quotes are tracked inside the region, because the depth count is
            # otherwise fooled by a parenthesis in a string: one `(` inside
            # `'…'` stretched the region to the end of the input and raised a
            # following heredoc body as commands.
            bracket = "[" if command.startswith("$[", i) else "("
            closer = "]" if bracket == "[" else ")"
            j = i + (2 if bracket == "[" else (3 if command[i] == "$" else 2))
            depth = 1 if bracket == "[" else 2
            inner = None
            while j < n and depth:
                c = command[j]
                if inner:
                    if c == inner:
                        inner = None
                elif c in "'\"":
                    inner = c
                elif c == bracket:
                    depth += 1
                elif c == closer:
                    depth -= 1
                j += 1
            out.append(command[i:j])
            word_start = False
            i = j
            continue
        if not comment and not braces and command.startswith("<<<", i):
            # A herestring feeds one word and opens no body. Stepping over all
            # THREE characters is what keeps the `<<` inside it from being read
            # as a redirect on the next pass — which swallowed every command
            # after `cat <<<hello`.
            out.append(command[i : i + 3])
            word_start = False
            i += 3
            continue
        if not comment and not braces and ch == "<" and command.startswith("<<", i):
            j = i + 2
            dashed = j < n and command[j] == "-"
            if dashed:
                j += 1
            while j < n and command[j] in " \t":
                j += 1
            delim, j = _heredoc_word(command, j)
            if delim:
                pending.append((delim, dashed))
                out.append(command[i:j])
                word_start = False
                i = j
                continue
        if ch == "\n":
            out.append(ch)
            i += 1
            comment, word_start = False, True
            for delim, dashed in pending:
                body_lines = []
                while i < n:
                    end = command.find("\n", i)
                    line = command[i:] if end == -1 else command[i:end]
                    i = n if end == -1 else end + 1
                    if (line.lstrip("\t") if dashed else line).rstrip("\r") == delim:
                        break
                    body_lines.append(line.rstrip("\r"))
                bodies.append("\n".join(body_lines))
            pending = []
            continue
        out.append(ch)
        comment = comment and ch != "\n"
        word_start = ch in WORD_BREAK
        i += 1
    return "".join(out), bodies


def split_segments(command):
    """Split into pipeline/list segments while respecting quotes.

    A regex split on `;`/`&&`/newline breaks inside quoted strings, so the
    heredoc commit form Claude Code itself uses (`git commit -m "$(cat
    <<'EOF' ...)"`) fell apart mid-quote and slipped past the reader.
    shlex with punctuation_chars keeps quoted arguments whole and emits
    the separators as their own tokens.

    Unquoted newlines separate commands just like `;`; newlines inside
    quotes belong to an argument and must not split it. shlex alone treats
    every newline as plain whitespace, so a small quote-aware scan converts
    only the unquoted ones first.

    `commenters` is cleared: a `#` has to survive as an ordinary character so
    that a retry token written in a comment can still be matched as a bare
    word. Callers judging what a command DOES run it through `drop_comments`
    first — see that docstring for what clearing this costs otherwise.

    Returns (segments, parsed_cleanly)."""
    items, clean = split_segments_with_separators(command)
    return [tokens for _, tokens in items], clean


def split_segments_with_separators(command):
    """The same split, keeping the operator that joined each segment.

    Returns ([(separator, tokens), ...], parsed_cleanly). `separator` is the
    operator that joined this segment to the one before it, "" for the first.

    The separator used to be emitted as a token and dropped, so `&&`, `;` and
    `||` were indistinguishable downstream — measured on all three forms of
    `cd /tmp/x <sep> git commit`, which returned the same two segments. In a
    shell the last of those is the opposite of the first: `&&` runs the commit
    where the `cd` arrived, `||` runs it only if the `cd` failed, which is
    where the shell already was. Without the operator, a reader following the
    `cd` judges the wrong repository with confidence on `||`, and a reader
    judging every reachable directory keeps asking about the session's own on
    `&&` — the prompt volume this exists to reduce.

    It arrives beside the tuple rather than inside it because the callers of
    `split_segments` read its two elements, and a third element in the middle
    of a fix for silent misjudgment would have been a change to every one of
    them.
    """
    out, quote, esc = [], None, False
    for ch in command:
        if esc:
            # A backslash-newline is a line continuation: the shell removes
            # BOTH characters and the command is one line. Keeping them turned
            # `cd /B \<newline> && git commit` into a two-argument `cd`, which
            # reads as a destination that cannot be computed — so a command
            # that passes on one line was stopped for being wrapped.
            if ch == "\n":
                out.pop()
            else:
                out.append(ch)
            esc = False
            continue
        if quote != "'" and ch == "\\":
            out.append(ch)
            esc = True
            continue
        if quote:
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote = ch
        # Spaced, because shlex groups a RUN of punctuation into ONE token:
        # `cd /B ||` followed by a newline became the single token `||;`,
        # which is neither a branching operator nor a plain `;`. Writing the
        # operator at the end of the line is how a long command is normally
        # written, so this was the common form and not a constructed one, and
        # it went silent where the release before this work stopped it.
        # Measured tokens before the spaces: `||;`, `|;`, `&;`.
        out.append(" ; " if ch == "\n" and quote is None else ch)
    command = "".join(out)

    lex = shlex.shlex(command, posix=True, punctuation_chars=";|&")
    lex.whitespace_split = True
    lex.commenters = ""
    items, current, sep = [], [], ""
    try:
        for tok in lex:
            if tok and set(tok) <= set(";|&"):
                if current:
                    items.append((sep, current))
                    current, sep = [], tok
                # Two operators with nothing between them — `cd x ||` and then
                # a newline, which arrives here as its own `;`. The FIRST one
                # is the one that binds the segments; the second is the line
                # ending, and letting it win turned a multi-line `||` into a
                # `;` and dropped the session's own directory from the answer.
                elif not sep:
                    sep = tok
            else:
                current.append(tok)
    except ValueError:
        if current:
            items.append((sep, current))
        return items, False
    if current:
        items.append((sep, current))
    return items, True


def merged_view(items):
    """The segments the splitter cut inside a redirection, glued back (#674).

    `split_segments_with_separators` cuts at every `&` and `|`, so `2>&1`,
    `>&2`, `<&0`, `>&-`, `>|f`, and `&>f` after a word each arrive as a
    separator between two segments, and a program or a string behind one lands
    in a segment of its own. The splitter is not changed: teaching it these
    operators moves every segment in both gates and in the walk, and `cd W
    2>&1 && git commit` would then be judged in W alone where `86256492` also
    judged the session's directory (`plan.md` Alternatives B).

    A segment is glued to the next where it ends in a bare redirection
    operator (`2>`, `>`, `<`, `{fd}>`) and the separator is `&` or `|`, or where
    the separator is `&` and the next segment begins with `>` (`&>`, `&>>`). A
    chain folds into one. Returns `(parts, tokens)` for each group of two or
    more parts: the item indices and the glued tokens. Callers read a group
    BESIDE its parts and add only what no part found on its own.
    """
    groups = []
    for index, (sep, tokens) in enumerate(items):
        if groups and sep in ("&", "|") and tokens:
            parts, toks = groups[-1]
            # The operator may be glued to the end of a word (`git>&2`, round
            # 1 of 1790660768, yellow 4), so the last piece `unglued` cuts is
            # the one asked.
            last = (unglued(toks[-1:]) or toks[-1:])[-1]
            m = _REDIRECTION.match(last)
            if m and m.end() == len(last):
                toks[-1] += sep + tokens[0]
                toks += tokens[1:]
                parts.append(index)
                continue
            if sep == "&" and tokens[0].startswith(">"):
                toks += ["&" + tokens[0], *tokens[1:]]
                parts.append(index)
                continue
        groups.append(([index], list(tokens)))
    return [g for g in groups if len(g[0]) > 1]


# Reserved words that BEGIN A COMMAND LIST, so the word after one is a command
# word (#669). The shell splits `for d in a; do git commit; done` at `;`, and
# the commit arrives as a segment whose first word is `do`; reading only that
# position found no commit in a command a shell runs. `{` is here for the same
# reason after one of the others -- `do { git commit; }` -- and `(` is taken off
# by `strip_subshell` wherever it opens the remainder.
LIST_OPENERS = frozenset({"do", "then", "else", "elif", "if", "while", "until", "{"})

# Constructs whose command word is not found by position: a `case` arm's
# pattern, a function definition's name, a coprocess's optional name. Rather
# than read their grammar, the first `git` word in the segment is read as the
# command word -- a false one is a stop, never a silence.
UNPLACED = frozenset({"case", "coproc", "function"})

# Programs that RUN THEIR OPERANDS AS A COMMAND (#670). The reader used to know
# `WRAPPERS` alone and stopped at the first word it did not know, so `exec`,
# `nice`, `timeout` and `xargs` in front of `git commit` read as no commit. The
# enumeration and how it was found are in work item 1790644505's
# `trail/phases/phase-5.md`: POSIX's utilities that execute an operand, GNU
# coreutils' "Modified command invocation" chapter and its `g`-prefixed names
# on macOS, util-linux's scheduling and namespace tools, the privilege tools,
# the tracers, and `find`, `parallel`, `watch` and `script`. Directly followed
# by `git`, the commit runs where the shell is; behind the program's own
# options or operands, which this reader does not parse, the first `git` word
# stands in for the command word and the directory is unplaced -- `env -C`,
# `sudo -D` and `chroot` move it, and knowing which flags do is a parser.
RUNNERS = frozenset(
    WRAPPERS
    | {
        "exec",
        "nice",
        "timeout",
        "xargs",
        "stdbuf",
        "chroot",
        "runcon",
        "setsid",
        "ionice",
        "taskset",
        "chrt",
        "flock",
        "unshare",
        "nsenter",
        "prlimit",
        "setpriv",
        "runuser",
        "doas",
        "pkexec",
        "caffeinate",
        "arch",
        "strace",
        "ltrace",
        "valgrind",
        "gtimeout",
        "gnice",
        "gnohup",
        "gstdbuf",
        "genv",
        "gchroot",
        "find",
        "parallel",
        "watch",
        "script",
        # zsh (round 1 of 1790660768, yellow 5): its precommand modifiers,
        # and `repeat N`, whose count is an operand the stand-in reads past.
        "noglob",
        "nocorrect",
        "repeat",
    }
)

# Programs that hand a STRING to a shell to parse, once given the flag that
# says so: `sh -c 'git commit'`. The string is read as a command the way
# `eval`'s argument already was (`reparsed_texts`).
SHELLS = frozenset({"sh", "bash", "zsh", "dash", "ksh", "mksh", "yash", "ash"})
# `flock` joined with #674: util-linux's flock(1) says `-c`/`--command` passes
# "a single command, without arguments, to the shell with -c". `sudo -s` and
# `sudo -i` did not, although they reach a shell's `-c` too: `man sudo`
# (1.9.17p2) escapes every character of the command but alphanumerics,
# underscores, hyphens and dollar signs, so a quoted string arrives as one
# word and not as a command line. Its argv form is `sudo` the runner's.
STRING_HOSTS = frozenset(SHELLS | {"su", "runuser", "script", "flock"})


def _string_at(words, j):
    """The words a host's string is picked from, starting at J (#674).

    WORDS[J] as it always was, and, where that word is a redirection, the words
    past it up to the first that is not one. The shell takes a redirection off
    before the host runs, so `bash -c 2>/dev/null "$CMD"` runs `$CMD`; the base
    asked `2>/dev/null` and nothing after it. A spaced target goes with its
    operator and is not asked.
    """
    out = []
    while j < len(words):
        out.append(words[j])
        width = redirection_width(words, j)
        if not width:
            break
        j += width
    return out


def command_word(tokens, stand_in="git", redirections=False):
    """(the segment from its command word on, whether its directory is unplaced).

    STAND_IN is the word looked for where no position names the command word;
    the worktree guard passes `eval` to find an `eval`'s argument.

    Assignments, wrappers and the `!`/`time` prefixes are read past as they
    always were, and so are the words in `LIST_OPENERS`. What sits behind one of
    those, or inside an `UNPLACED` construct, runs somewhere a reader of the
    command cannot place: a loop or conditional body, a loop condition that runs
    again after its body, a function body that runs where it is called. The
    second value says so.

    Every segment the base read a command word in keeps it: the tokens read
    past before are read past now, and the new ones are words at which the old
    reading stopped with no command at all.

    REDIRECTIONS reads past a redirection as well (#674), and it is a second
    reading rather than a change to this one: `2>/x/git commit` reads as `git`
    without it, because the word's last component is `git`, and as `commit`
    with it. So every consumer asks this reading only where the first found
    nothing, and adds what it finds (`parse_git` and the worktree guard's
    reading of an `eval`).
    """
    toks, _opened = strip_subshell(tokens)
    unplaced = False
    after_runner = False
    i = 0
    while i < len(toks):
        tok = toks[i]
        width = redirection_width(toks, i) if redirections else 0
        if width:
            i += width
            continue
        if "=" in tok and not tok.startswith("-"):
            i += 1
            continue
        if os.path.basename(tok) in RUNNERS:
            after_runner = True
            i += 1
            continue
        if tok == "!":
            i += 1
            continue
        if tok in LIST_OPENERS:
            unplaced = True
            rest, _opened = strip_subshell(toks[i + 1 :])
            toks, i = rest, 0
            continue
        break
    if i < len(toks) and (
        toks[i] in UNPLACED
        # zsh's short loop, `for i (1 2) git commit` (round 1 of 1790660768,
        # yellow 5): the word list in parentheses, and the command straight
        # after it. `for d in git commit` has no parenthesis there and stays
        # a word list.
        or (
            toks[i] in ("for", "foreach")
            and i + 2 < len(toks)
            and toks[i + 2].startswith("(")
        )
        or toks[i].endswith(")")
        or (i + 1 < len(toks) and toks[i + 1] == "()")
        or (after_runner and os.path.basename(toks[i]) != "git")
    ):
        # A pattern (`a)`), a definition (`f()`, `f ()`), a word in
        # `UNPLACED`, or a runner's own option or operand: no position names
        # the command word, so the first STAND_IN word stands in for it, and
        # none means no such command is in the segment.
        later = [
            j for j in range(i + 1, len(toks)) if os.path.basename(toks[j]) == stand_in
        ]
        if later:
            i, unplaced = later[0], True
    return toks[i:], unplaced


def host_word(tok):
    """The program TOK names, read with a glued subshell opener taken off.

    `(sh -c 'git commit')` arrives from the splitter as `(sh`, and the last
    component of that is `(sh`, which is no host (#674, P10). Taking the `(`
    off first only ever adds a host: a word whose last component was already
    a host keeps it, because a `(` in front of a `/` is not in that component.
    """
    return os.path.basename(tok.lstrip("("))


def _hands_a_string(word, tok):
    """True when `tok`, an argument of `word`, tells it to run a string."""
    if tok == "--command" or tok.startswith("--command="):
        return word in ("su", "runuser", "script", "flock")
    # A short-option cluster holding `c`: `-c`, `-ec`, `-lc`.
    return tok.startswith("-") and not tok.startswith("--") and "c" in tok[1:]


def reparsed_texts(tokens, env_words=True):
    """Every string in this segment that a program hands to a shell to parse.

    `sh -c`, `bash -c` and the other `SHELLS`, `su -c`, `runuser -c` and
    `script -c` run their string; `env -S` splits one into a command; `watch`
    runs its arguments through `sh -c`. Where the flag is present every
    non-option word after the program is returned, because which of them is
    the string depends on options this reader does not parse (`bash -o errexit
    -c '…'`) -- reading an extra word as a command costs a stop, and missing
    the string costs a silence. A program found anywhere in the segment
    counts, not only as its command word: `sudo sh -c` and `xargs -I{} sh -c`
    put it behind a runner.

    ENV_WORDS adds `env -S`'s string read as `env`'s own words (#716). A
    caller asking which command word expands passes False: env's other words
    are its arguments, never a command word.
    """
    texts = []
    for k, tok in enumerate(tokens):
        word = host_word(tok)
        rest = tokens[k + 1 :]
        if word in STRING_HOSTS and any(_hands_a_string(word, t) for t in rest):
            texts += [t for t in rest if not t.startswith("-")]
            texts += [t.split("=", 1)[1] for t in rest if t.startswith("--command=")]
        elif word in ("watch", "parallel"):
            # `parallel` runs each of its arguments through a shell (#674). It
            # is read for a commit written out, which costs nothing where none
            # is; placing its command word is a parser (`frame/design.md` *Scope*).
            texts += [t for t in rest if not t.startswith("-")]
        elif word in ("env", "genv"):
            # env's words are walked once under GNU's grammar and, for `env`
            # alone, once under BSD's, and every string either walk finds is
            # kept (#737): where the two read a word differently, one of them
            # is the env that runs. `genv` is GNU's by name.
            found = _env_walk(word, rest, "gnu", env_words)
            if word == "env":
                found += [
                    t for t in _env_walk(word, rest, "bsd", env_words) if t not in found
                ]
            texts += found
    return texts


def _env_walk(word, rest, grammar, env_words):
    """The strings `env`'s words REST hand a shell, read under GRAMMAR.

    OWN: still among env's own options, read through `ENV_OPTIONS`, where a
    cluster or an abbreviation can spell the split string. A redirection
    anywhere among them is the shell's and is read past; `--` ends them
    (rounds 1 and 2 of 1790993140). The split string's unabbreviated
    spellings are read anywhere, as the base read them.
    """
    texts = []
    own, value, skip = True, False, 0
    for j, t in enumerate(rest):
        if skip:
            skip -= 1
            continue
        width = redirection_width(rest, j) if own else 0
        if width:
            skip = width - 1
            continue
        at, takes_next = _env_option(t, own and not value, grammar=grammar)
        if value:
            value = False
        elif own and (t == "--" or not t.startswith("-")):
            own = False
        elif own:
            value = takes_next or (at is not None and at[0] == "next")
        if at is None:
            continue
        kind, string = at
        if kind == "next" and j + 1 < len(rest):
            texts += _string_at(rest, j + 1)
            after = rest[j + 1 :]
        elif kind == "here":
            texts.append(string)
            after = [string, *rest[j + 1 :]]
        else:
            continue
        if env_words:
            texts += _env_words(word, rest[:j], after)
    return texts


# Every option of `env`, and the one table the env arm of `reparsed_texts`
# reads them from (round 2 of 1790993140). Sources, read from the code and not
# from a synopsis, which is what missed two rows (#737): GNU coreutils
# `src/env.c` at `f799b2f48a61` (`shortopts` and `longopts`; `--quoting-style`
# is there before any release has it) and FreeBSD `usr.bin/env/env.c` at
# `c2d93a803ace` (its `getopt` letters; Apple's `shell_cmds` `env/env.c` has
# the same less `L` and `U`). Re-derive from those files, never from `--help`.
# (short, long, value): VALUE is `ENV_STRING` for the split string,
# "required" for a value attached or in the next word, "optional" for one
# attached with `=` only, None for no value. A short option with no long name
# has None there.
#
# What the table does not need a row for: a lone `-`, which GNU takes as `-i`
# and the end of the options and BSD as `-i` among them; the walk reads it as
# one of env's own options, which costs a stop only where GNU's program is
# named like an option. And `--`, which ends them. BSD's `-` inside a word is
# `_ENV_SHORT`'s, below the table, and BSD's getopt reads a word starting `--`
# with more after it as a cluster led by that letter, which `_env_option`
# reads under the "bsd" grammar. GNU's getopt takes an unambiguous prefix of a
# long name (`--un`, `--spl`); an ambiguous one (`--i`, `--d`) is an error,
# after which env runs nothing, so it is read as a flag.
ENV_STRING = "string"
ENV_OPTIONS = (
    ("i", "--ignore-environment", None),
    ("0", "--null", None),
    ("v", "--debug", None),
    ("u", "--unset", "required"),
    ("C", "--chdir", "required"),
    ("S", "--split-string", ENV_STRING),
    ("a", "--argv0", "required"),
    ("P", None, "required"),
    ("L", None, "required"),
    ("U", None, "required"),
    (None, "--block-signal", "optional"),
    (None, "--default-signal", "optional"),
    (None, "--ignore-signal", "optional"),
    (None, "--list-signal-handling", None),
    (None, "--env0-from", "required"),
    (None, "--quoting-style", "required"),
    (None, "--help", None),
    (None, "--version", None),
)
_ENV_SHORT = {short: value for short, _long, value in ENV_OPTIONS if short}
# BSD's getopt has `-` among its letters, as `-i`: `env -i-S '…'` runs the
# string on macOS (executed, #737). A row would be spelt `--`, the end of the
# options, so the letter lives here.
_ENV_SHORT["-"] = None
_ENV_LONG = {long: value for _short, long, value in ENV_OPTIONS if long}


def _env_long(name, abbreviated):
    """The long option NAME spells in `ENV_OPTIONS`, or None.

    Exactly, or, where ABBREVIATED, as the one long name it is a prefix of,
    which is GNU getopt's rule; `--` alone is no prefix.
    """
    if name in _ENV_LONG:
        return name
    if not abbreviated or len(name) < 3:
        return None
    found = [long for long in _ENV_LONG if long.startswith(name)]
    return found[0] if len(found) == 1 else None


def _env_option(t, own, grammar="gnu"):
    """What T is to `env`: (where it spells the split string, takes_next).

    The first is ("next", None) where the split string is the next word,
    ("here", s) where T carries it, and None otherwise. TAKES_NEXT is True
    where T is an option whose value is the next word. Among env's own
    options (OWN) a short cluster is read letter by letter, up to the letter
    whose value is the rest of the word or the next one (`-iS`, `-vu FOO`),
    and a long name in any prefix getopt takes. Elsewhere only the split
    string's unabbreviated spellings at a word's head count, as the base read
    them (#716).

    GRAMMAR is "gnu" or "bsd" (#737). Under "bsd" there is no long name: a
    word that starts `--` is a cluster whose first letter is `-`, as FreeBSD's
    getopt reads it, so `--S` is `-i -S` and `--unset` is `-i -u nset`. `--`
    alone spells nothing either way, and the walk ends env's options there.
    The split string's spellings read anywhere are GNU's, and the walk under
    "gnu" keeps them.
    """
    if t.startswith("--") and grammar != "bsd":
        name, eq, attached = t.partition("=")
        value = _ENV_LONG.get(_env_long(name, own))
        if value == ENV_STRING:
            return (("here", attached) if eq else ("next", None)), False
        return None, own and value == "required" and not eq
    if not t.startswith("-") or len(t) < 2:
        return None, False
    letters = t[1:] if own else t[1]
    for i, ch in enumerate(letters, 1):
        value = _ENV_SHORT.get(ch, "unknown")
        if value == ENV_STRING:
            string = t[i + 1 :]
            return (("here", string) if string else ("next", None)), False
        if value == "required":
            return None, i == len(t) - 1
        if value is not None:
            # A letter no synopsis has: getopt fails, and env runs nothing.
            return None, False
    return None, False


def _env_words(word, before, after):
    """`env -S`'s string read as the command `env` runs, as a one-item list (#716).

    `env` splits the string into its OWN arguments, so `env -S '-i git
    commit'` runs `env -i git commit`, and the string alone reads as a command
    whose word is `-i`. BEFORE is what stood between `env` and the option,
    AFTER the string and what follows it. The shell takes the redirections off
    before `env` runs, so they are left out, and the string is the first word
    past them. Returned beside the string, never instead of it; empty where a
    redirection is the last word and no string follows.
    """
    after = _without_redirections(after)
    if not after:
        return []
    # Only the string is split again; every other word reached `env` as ONE
    # argument, so it is quoted back into one: `env -S echo 'a && b'` runs
    # `echo` with one operand, not a list (round 1 of 1790993140, yellow 1).
    head = [shlex.quote(w) for w in _without_redirections(before)]
    tail = [shlex.quote(w) for w in after[1:]]
    return [" ".join([word, *head, after[0], *tail])]


def _without_redirections(toks):
    """TOKS with every redirection taken out, a spaced target with its operator."""
    out, i = [], 0
    while i < len(toks):
        width = redirection_width(toks, i)
        if width:
            i += width
            continue
        out.append(toks[i])
        i += 1
    return out


def _heredoc_end(command, k, n):
    """Where the heredoc opened by the `<<` at `k` ends, or None if none opens."""
    dashed = command.startswith("<<-", k)
    j = k + (3 if dashed else 2)
    while j < n and command[j] in " \t":
        j += 1
    delim, after = _heredoc_word(command, j)
    if not delim:
        return None
    line_end = command.find("\n", after)
    while line_end != -1:
        start = line_end + 1
        line_end = command.find("\n", start)
        line = command[start:] if line_end == -1 else command[start:line_end]
        if (line.lstrip("\t") if dashed else line).rstrip("\r") == delim:
            return n if line_end == -1 else line_end
    return n


def _paren_end(command, j):
    """The index of the `)` that closes a substitution whose body starts at `j`.

    Quotes, escapes and heredocs are stepped over, because a `)` in any of them
    closes nothing. A `case` inside is where counting parentheses stops being
    right -- its patterns end in an unmatched `)` -- so from there the rest of
    the input is the body: a longer body can only hold more commits.
    """
    depth, k, n, quote = 1, j, len(command), None
    while k < n:
        ch = command[k]
        if quote == "'":
            quote = None if ch == "'" else quote
        elif ch == "\\":
            k += 2
            continue
        elif ch == '"':
            quote = None if quote == '"' else '"'
        elif quote is None:
            if command.startswith("<<<", k):
                # A herestring opens no body. Stepped over whole, because the
                # last two of its three `<` would otherwise read as a `<<`.
                k += 3
                continue
            if command.startswith("<<", k):
                end = _heredoc_end(command, k, n)
                if end is not None:
                    k = end
                    continue
            if ch == "'":
                quote = "'"
            elif ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if not depth:
                    return k
            elif (
                command.startswith("case", k)
                and (k == 0 or command[k - 1] in " \t\n;|&(")
                and command[k + 4 : k + 5] in (" ", "\t", "\n")
            ):
                return n
        k += 1
    return n


def substitution_bodies(command):
    """The body of every `$( … )`, `` ` … ` ``, `<( … )` and `>( … )` (#670).

    The shell runs each body as a command, in a subshell, and substitutes its
    output -- so a commit in one is a commit, and the reader never looked. The
    outermost bodies come back; a caller reading a body as a command calls
    this again on it for the ones nested inside. A single-quoted `$(` is text
    and opens nothing; a double-quoted one runs. An unterminated body runs to
    the end of the input. `$((…))` comes back too, as a body holding its
    expression, which reads as no command.
    """
    bodies, i, n, quote = [], 0, len(command), None
    while i < n:
        ch = command[i]
        if quote == "'":
            quote = None if ch == "'" else quote
            i += 1
            continue
        if ch == "\\":
            i += 2
            continue
        if ch == "'" and quote is None:
            quote = "'"
        elif ch == '"':
            quote = None if quote == '"' else '"'
        elif ch == "`":
            end = i + 1
            while end < n and command[end] != "`":
                end += 2 if command[end] == "\\" else 1
            bodies.append(command[i + 1 : min(end, n)])
            i = end + 1
            continue
        elif command.startswith("$(", i) or (
            quote is None and ch in "<>" and command.startswith("(", i + 1)
        ):
            end = _paren_end(command, i + 2)
            bodies.append(command[i + 2 : end])
            i = end + 1
            continue
        i += 1
    return bodies


def strip_subshell(tokens):
    """(tokens, opened) with a leading subshell opener taken off the word.

    A shell ends a word at `(` and `)`; shlex here is told only about `;`, `|`
    and `&`, so `(cd /tmp/x && git commit)` arrives as `(cd` … `commit)` and
    BOTH readers missed it — the `cd` was not a `cd` and the `git` was not a
    `git`. One parenthesis reproduced the whole fail-open this work item
    exists to close.

    Whether the parenthesis is worth reading is a separate question from
    whether the shell moves. It is not added to the splitter's punctuation
    because that changes how every quoted argument in every command tokenizes,
    which is a wider change than the two words it would fix.
    """
    out, opened = list(tokens), False
    while out and out[0] in ("(", "((", "{"):
        out.pop(0)
        opened = True
    if out and out[0].startswith("("):
        out[0] = out[0].lstrip("(")
        opened = True
    return out, opened


def _git_options(rest, redirections=False):
    """(index of the subcommand, indices of the `-C` VALUES) within `rest`.

    `rest` is what follows the `git` word, and `parse_git` takes the values.

    REDIRECTIONS reads past a redirection before the subcommand as well
    (#674): `git 2>/dev/null commit` read `2>/dev/null` as the subcommand.
    `parse_git` asks it only where the first scan landed on a redirection.
    """
    # RIDER: `--git-dir` and `--work-tree` are in this set so the SUBCOMMAND
    # is still found, and their values are then thrown away -- so
    # `git --git-dir=/elsewhere/.git --work-tree=/elsewhere commit` is judged
    # against the shell's cwd. It is narrower than `-C`, which is what a
    # session driving another repository actually types, and that is why it
    # was left: closing it means `chdirs` stops being one list of composing
    # paths and becomes a resolved (git-dir, work-tree) pair, which the
    # worktree guard's `apply_chdir` cannot express. The rider is here rather
    # than on the guard because this is the file the fix is in.
    #
    # The options git 2.54.0 ran `status` after with the value as a separate
    # word (#716, M1). `--config-env`, `--attr-source` and `--shallow-file`
    # were missing, so their value read as the subcommand. `--exec-path` takes
    # no separate value -- git prints its path and exits -- and stays: the
    # word it skips was never run.
    takes_value = {
        "-C",
        "-c",
        "--git-dir",
        "--work-tree",
        "--namespace",
        "--exec-path",
        "--config-env",
        "--attr-source",
        "--shallow-file",
    }
    i, chdirs = 0, []
    while i < len(rest):
        t = rest[i]
        width = redirection_width(rest, i) if redirections else 0
        if width:
            i += width
            continue
        if t in takes_value:
            if t == "-C" and i + 1 < len(rest):
                chdirs.append(i + 1)
            i += 2
            continue
        if t.startswith("-") and t != "-":
            i += 1
            continue
        break
    return i, chdirs


def parse_git(tokens):
    """Return (subcommand, args, chdirs) if this segment IS a git invocation.

    `git` must be the segment's command word -- leading VAR=val assignments and
    common wrappers are skipped, anything else (echo, cat, prose) disqualifies
    the segment. Then git's own global options (-C <path>, -c k=v, ...) are
    skipped to find the subcommand.

    `chdirs` are the `-C <path>` values in order. Skipping them was enough to
    FIND the subcommand and not enough to know which repository it acts on,
    which is the whole question the worktree guard answers.
    """
    # A reserved word in front of `git` used to stop this reading, so a commit
    # that was the first command of a loop or conditional body was invisible
    # (#669). `command_word` reads past it, and says such a segment's
    # directory is unplaced.
    #
    # A redirection in front of `git` or before its subcommand stopped both
    # scans (#674). Each is asked again past redirections only where it found
    # no `git`, or landed on a redirection for the subcommand, so every answer
    # the first reading gave is kept -- `2>/x/git commit` among them.
    word, _unplaced = command_word(tokens)
    if not word or os.path.basename(word[0]) != "git":
        word, _unplaced = command_word(tokens, redirections=True)
        if not word or os.path.basename(word[0]) != "git":
            return None
    rest = word[1:]
    at, chdir_at = _git_options(rest)
    if redirection_width(rest, at):
        again = _git_options(rest, redirections=True)
        if again[0] < len(rest):
            at, chdir_at = again
    chdirs = [rest[k] for k in chdir_at]
    if at >= len(rest):
        return None
    # A closing parenthesis rides on the last word of the segment, which for
    # `(git commit)` is the SUBCOMMAND: it read as `commit)`, matched nothing,
    # and the gate returned before any of this module's walking was used. The
    # `-m x` form hides it, because the paren attaches to the argument
    # instead. No git subcommand ends in `)`, so taking it off costs nothing;
    # arguments are left alone, where a `)` can be part of a commit message.
    subcommand = rest[at].rstrip(")")
    # `( git )` leaves nothing behind, and the empty string is not a
    # subcommand — this function documents None for that, and a caller
    # testing the result for identity would read `''` as one.
    return (subcommand, rest[at + 1 :], chdirs) if subcommand else None
