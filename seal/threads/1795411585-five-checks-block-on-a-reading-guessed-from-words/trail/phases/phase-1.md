# Phase 1: 1795411585-five-checks-block-on-a-reading-guessed-from-words

## What this phase found

**The frame holds against the tree at `71ff19ea2`.** `release_exists`
stood at `.github/scripts/publish_release_note.py:432-446`, `_issue_api`
at `.github/scripts/close_issues_on_release.py:129-143`, `Test__issue_api`
at `tests/github/test_close_issues_on_release.py:462-475`, and the timeout
pin at `tests/github/test_publish_release_note.py:975-980`, as
`frame/design.md` G8 gives them (read). The merge of #1574 changed none of
this phase's files: `git diff --stat 22803718e 71ff19ea2` over `lib/gitcmd.py`,
the two scripts, `tests/lib/test_gitcmd.py` and `tests/github/` printed
nothing (executed). So each red run below, made at `71ff19ea2` before the
fix, ran the bytes `22803718e` holds.

**`tests/github/test_publish_release_note.py` gains `Test_release_exists`,
where *Scope* item 1 asks the file to feed `-i` answers.** Before this
phase no case in the file fed `release_exists` an answer: `wire` replaces
the function, and the one case that reaches it raises a timeout. So the
four scenarios S1 to S4 are new cases in a class of their own, as the
file's docstring asks, one class per function (judged against
`frame/design.md` *Scope* item 1 and the scenarios S1 to S4). The two
cases call `release_exists` with equal arguments, which
`seal layout --pairs` names (executed). The answer `gh api -i` gives is
what differs, and the class docstring says so, as `Test_comments_on`'s
does.

**The 2xx test is written in each caller, and `http_answer` only reads.**
`frame/design.md` *Data & interfaces* has `http_answer` return the status
and the body, and has each caller answer differently on 404 and on 2xx:
`False` and `True` for `release_exists`, `(None, False)` and the body's
JSON for `_issue_api`. A shared verdict helper would hold one comparison,
`200 <= status < 300`, and would add a second unit for the two callers to
read (judged against the design's *Data & interfaces*).

**`http_answer`'s docstring states the fact it stands on, and cites no
frame.** A `gh` that reached no server prints nothing to stdout
(`frame/design.md` G10, executed by the framer). The docstring says that
in its own words, because the frame leaves the tree at the settle after
the release, and a citation of it would then name nothing (judged against
`skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes*). The test module's comment over `MISSING` and `PRESENT` names
#1572 for the measurement.

**The new cases need no `import json`.** Each `-i` answer they feed is a
string literal, so `tests/github/test_close_issues_on_release.py` keeps
`import json` for the `Tracker` double alone, as before this phase. #1576
removes that import with the double's label arms, and neither change
reaches the other's lines (`frame/plan.md` *Overlap with the release*).

**Seen red (executed, at `71ff19ea2` before the fix, one command over the
new and changed cases, 17 failed and 3 passed).**

- S2, the 403 whose stderr says `Not Found`: both
  `test_refuses_any_other_status_and_no_status_by_exiting[a-403-whose-stderr-says-not-found]`
  cases, in `Test_release_exists` and in `Test__issue_api`, failed on
  `DID NOT RAISE SystemExit`. The old code read the stderr's words and
  answered not-found.
- S1 and S4: three of the four `test_accepts_...` cases failed on their
  argv assertion, `['api', 'repos/...']` against `['api', '-i', ...]`. The
  `a-200` case of `Test__issue_api` failed earlier, on `JSONDecodeError`,
  because the old code parsed the whole stdout as JSON.
- `Test_http_answer`: all ten cases failed on `AttributeError`, since the
  function did not exist.
- The timeout pin in
  `test_a_gh_that_gave_no_answer_is_read_as_each_read_reads_a_failure`
  failed on the command it names, which now carries `-i`.
- S3, no HTTP answer: both `no-http-answer` cases passed at the old code,
  which also exited on a stderr without either word. After the fix they
  hold the no-status exit, and the mutant that removes `status is None or`
  turns them red (below).

**Mutation (executed, `bin/seal mutate`, 14 mutants, 14 red, 0
SURVIVED).** The tree was clean after each call.

- `lib/gitcmd.py`, with `-k http_answer`: the status pattern without the
  space after the code, `search` in place of `fullmatch`, a partition at
  one newline, the first line not split from the headers, and 0 in place
  of None for no status.
- `.github/scripts/publish_release_note.py`, with `-k release_exists`:
  `403` in place of `404`, the `status is None or` guard removed, the 2xx
  bound widened to 600, and `-i` removed.
- `.github/scripts/close_issues_on_release.py`, with `-k issue_api`: the
  same four, and `json.loads(out.stdout)` in place of `json.loads(body)`.

**Search 4 of `frame/design.md` prints nothing** (executed after the fix).

**The phase boundary set (executed, one `bin/test -q` command).** It held
the 26 test files under `tests/` outside `tests/text/` and
`tests/behaviour/` that name `gitcmd`, `publish_release_note` or
`close_issues_on_release`, the plan row's five among them, and the two
tree-wide directories. The first run failed one case,
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
on this work item's missing `gaps.md`, which the phase's close writes. The
run after it passed: 3632 passed, 10 skipped. Its five warnings are
citations that pending rule changes of other work items excuse, none in a
file this phase changed. Many more test files reach `lib/gitcmd.py`
through the script they load; the set names only those that name a
changed path, so the rest stand with the broad gate in `gaps.md`.
