"""The bare words of a command, read for the worktree guard's consent tokens
and nothing else (#692, #868).

Its failure direction is why a text read may stay: a token it cannot read
costs one refusal, and a token it reads has exactly the standing tokens
always had -- `docs/worktree-guard-spec.md` *Choice sites* calls it an audit
trail, not an authorization. Nothing here names a directory or decides
where an action lands.

The rules are the two consent reads 0.16.0 had, joined:

  * **a bare word, never a substring** -- inside a quoted message it is prose
    (`echo "we agreed on [worktree-ok] yesterday"`), which the reads this one
    replaced both refused to read as consent;
  * **comments are read** -- the documented form writes the token in one;
  * **a here-document body reads nothing** (#773) -- a token is typed with
    a command, and a body is text the command only carries, so a token
    inside one consented to what nobody agreed to. `without_bodies` is the
    text a consent read reads, and a token counts only where the command as
    written carries it too, so leaving the bodies out can only refuse. A new
    consent read starts here, and since #780 the worktree guard's
    `has_token` does;
  * **a parenthesis riding on a word is not part of it** --
    `(git worktree add ../wt f [worktree-ok])` (the guard's `has_token`);
  * **a quote that never closes reads nothing from where it opens** -- the
    words read before the split fails are read, and none after it. A word
    inside an unclosed quote is prose a shell would refuse to run, so a
    substring fallback, which once read it, has no place here: reading
    loosely is the direction that waives without anybody asking. The words
    before it are kept because the documented comment form carries an
    English apostrophe after the token often enough to count
    (`# [shared-tree-ok] the release's own tree`): the comment is a comment
    to the shell, which runs the command, and this splitter, which reads
    comments on purpose, reads its apostrophe as a quote. Over the recorded
    runs that kept four of the guard's tokens and read none the base's reads
    did not (work item 1791384157, `trail/phases/phase-1.md`).
    A quote this splitter cannot close is not always one bash refuses, and
    ANSI-C quoting is the known disagreement, in both directions: `$'it\\'s'`
    is one closed word to bash, while shlex closes the quote at `\\'` and
    reads the rest as a quote that never closes. So a token typed after
    `echo $'it\\'s'` is refused although bash runs the command, and
    a token inside `echo $'it\\'s [shared-tree-ok] x'` is read although bash
    quotes it, as every base read did too (round 1 of work item 1791384157,
    white 6). The token typed in front is the way on in the first.

**This is the one reader of a consent token** (#868). The worktree guard's
`has_token` answers `token in given(command)`.
"""

import shlex

KNOWN = ("[worktree-ok]", "[shared-tree-ok]")


def without_bodies(command):
    """`command` with its here-document bodies taken out and its comments kept:
    the text a consent read reads beside the command as written (#773).

    The bodies are found by two readers. Where `hooks/lib/one_heredoc.py`
    matches the one shape byte for byte, its reduced text, which holds no
    `<<`; everywhere else `hooks/lib/cmdline.py#drop_heredoc_bodies`, which
    copies a comment through and opens no body inside one. No reader here
    decides where a body is.

    It is never read alone. Taking a body out can make a split succeed that
    failed on the raw text, and a token that split reads would be one the
    command as written never offered, so each caller ANDs this read with its
    read of the raw command.
    """
    import one_heredoc
    from cmdline import drop_heredoc_bodies

    command = command or ""
    reduced = one_heredoc.reduce(command)
    return drop_heredoc_bodies(command if reduced is None else reduced)


def _read_words(text):
    """The bare words of TEXT, comments included, up to where its split fails:
    a quote that never closes ends the read, and nothing from inside it is a
    word."""
    lexer = shlex.shlex(text or "", posix=True, punctuation_chars=";&|<>")
    lexer.commenters = ""
    lexer.whitespace_split = True
    read = []
    try:
        for word in lexer:
            read.append(word)
    except ValueError:
        pass
    return read


def _bare(text):
    return {w.strip("()") for w in _read_words(text)}


def given(command, fallback=None):
    """The known tokens `command` carries as bare words outside its
    here-document bodies, in `KNOWN`'s order -- read in the command as written
    AND in `without_bodies`, so a token in a body counts nowhere (#773).

    FALLBACK is the body reader to use where `without_bodies` raises,
    `hooks/lib/cmdline.py` failing to load among the causes. The worktree guard
    hands the frozen reader's `drop_heredoc_bodies`, so a broken wider reader
    still finds the bodies and the single-stream creation deny keeps its way
    past (released row T1 of 0.18.3). It is an argument rather than an import
    because the frozen reader is the guard's and the consent writer's alone
    (`tests/test_the_frozen_reading_never_grows.py`). Without one the error
    propagates: a gate that raises is reported by `hooks/dispatch.py`."""
    try:
        bodiless = without_bodies(command)
    except (Exception, SystemExit):
        if fallback is None:
            raise
        bodiless = fallback(command or "")
    found = _bare(command) & _bare(bodiless)
    return tuple(t for t in KNOWN if t in found)
