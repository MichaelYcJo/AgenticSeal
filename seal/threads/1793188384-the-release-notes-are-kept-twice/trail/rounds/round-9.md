# Review round 9: 1793188384-the-release-notes-are-kept-twice

target: afc53ac5, fixes aa81491f..afc53ac5

This is the verifying round after round 8. The fix range holds two
commits. `c6730b99` is the crafter's fix pass: it changes
`templates/setup/config.md`, `.github/scripts/publish_release_note.py` and
`tests/behaviour/test_release_hygiene.py`, ten lines in all. `afc53ac5` is
the orchestrator's: it writes round 8's finding 1 `verdict:` and `answer:`
lines and changes nothing else (executed: `git diff aa81491f afc53ac5 --
seal/`). The round ran read only in the branch worktree the spawn prompt
names, at `afc53ac5`. The repository declares no `seal/parity.md`, so this
round writes no `original:` line.

Carried from round 8 and not established again: that the merge
`9477538d` is clean, the readers of the removed files, and the three sweep
greps over `skills/`, `agents/`, `templates/` and `hooks/` its sixth
confirmation names. No commit in the fix range touches `skills/`,
`agents/` or `hooks/`. Re-established this round: the fix diff, the fix
pass's recorded search, the truth of the two extra rewrites, every other
citation of a test case this branch removed, and the narrow verification.

The account checked. The fix pass's `answer:` in `round-8.md:105` makes
five claims. First, it claims the bullet now reads exactly as round 8 gave
it and only those five lines changed. That holds, see the first
confirmation. Second, it claims its recorded search gives hits that are
each rewritten or judged. This round ran the same command at `afc53ac5`
and got 12 lines. Each one is a coordinate the answer names, and the two
rewritten ones are now at `publish_release_note.py:42` and
`test_release_hygiene.py:1146` and `:1152` (executed). The answer's
sentence on the `changelog/` and `CHANGELOG.md` hits describes phase 4's
table, which round 8 confirmed; that search has no pattern for either, so
the sentence is not about its output. Third, it claims the two extra
rewrites are true. They are, see the second and third confirmations.
Fourth, it claims 33 modules passed with 1482 passed and 9 skipped. This
round's `git grep -l` with the spawn prompt's three names finds 26
modules under `tests/`, plus `tests/conftest.py`. With
`tests/behaviour/test_release_hygiene.py` added, the 27 modules gave 1412
passed and 9 skipped, exit 0 (executed). Four patterns were tried, and
none gave 33 modules: they gave 26, 47, 26 and 47 (executed). The count
is an aggregate, so this round reports the gap and relies on its own run.
Fifth, it claims `ruff check` and `ruff format --check` exit 0 on the two
Python files. This round did not run the lint (rule 2). `ruff.toml:53`
selects no `E501`, so line length is not among what it checks (read).

## Findings

None. The close of round 8's finding 1 holds. The two extra rewrites are
true, and the sweep found no other text outside the work item's records
that cites a case this branch removed.

## Confirmations

confirms: round-8#1
The template no longer lists the gathered file's release heading among the
literals a checker reads. `git diff -w --word-diff aa81491f c6730b99 --
templates/setup/config.md` removes exactly "a release section's `## X.Y.Z
— <date>`," and changes no other word (executed). The bullet at
`templates/setup/config.md:143-147` now equals round 8's block word for
word (read). No other file holds a copy of the bullet: `git grep` for
"markers and anchors", "anchor table's header" and "release section's"
finds only this template, `skills/verify/scripts/pact_check.py:188`
(a comment on the pact table's own header) and round 8's record
(executed). The fix pass's recorded search, re-run at `afc53ac5` over
`tests/`, `skills/`, `hooks/`, `.github/`, `agents/`, `templates/`,
`bin/`, `evals/` and the four root documents, no longer matches the
template (executed). The verdict `fixed c6730b99` names a commit that
changes `templates/setup/config.md`, the finding's `location:`.

confirms: none
The rewrite of the title paragraph at
`.github/scripts/publish_release_note.py:42-44` is true. It now says the
`## X.Y.Z -- <date>` heading "the gathered changelog carried until #1053
held a date and no prose". At `v0.23.1`, `CHANGELOG.md:11` reads
`## 0.23.1 — 2026-10-28`, a version and a date and nothing else
(executed: `git show v0.23.1:CHANGELOG.md`). `268480ac`, a commit of this
branch, removed `CHANGELOG.md` (executed: `git show --stat`). So the past
tense and the date to #1053 both hold. The rewrap leaves `:44` at 112
columns. `:40` and `:46` were already longer than 88 before this branch
(executed: `git blame`, `awk`), and no rule this repository selects reads
a docstring's width, so the long line reads badly and misleads no reader.

confirms: none
The rewrite of the comment at
`tests/behaviour/test_release_hygiene.py:1150-1152` is true. It now says a
crafter that created `## Unreleased` reddened "the case that refused it in
`CHANGELOG.md`, which #1053 removed with the file". At `8a1173c8`,
`test_no_section_accumulates_entries_in_the_shared_file` read the `## `
headings of `CHANGELOG.md` and failed on any that started with
"unreleased" (read `8a1173c8:tests/behaviour/test_release_hygiene.py:1081-1103`).
`268480ac` removed that case and `CHANGELOG.md` together (executed: `git
log -S` and `git show --stat`). The comment's lines are at most 83
columns (executed: `awk`).

The class of the second rewrite was enumerated (contract rule 12). The
class is text that cites a test case this branch removed. The 58 test
names `git diff faf093f1 afc53ac5 -- tests/` removes and does not add
back were each searched with `git grep -w` over the tree at `afc53ac5`,
leaving out `seal/threads/`, `.test_durations` and the removed module
`tests/github/test_gather_changelog.py` (executed). One hit came back:
`tests/github/test_close_issues_on_release.py:948` defines its own live
`test_dry_run_writes_nothing`, a different case in another module that
only shares the name. `.test_durations:789` still names the removed case.
That file is timing data the test workflow reads, not text a person or an
agent acts on, and 174 of its 6774 entries name a case the tree no longer
defines (executed), so a stale entry there is the file's normal state.

confirms: none
The narrow verification for this round passed. `git grep -l -E
"setup/config\.md|publish_release_note|test_release_hygiene" -- tests/`
finds 27 files: 26 modules and `tests/conftest.py`, which is not a module.
`bin/test -q` over the 26 modules and
`tests/behaviour/test_release_hygiene.py`, which the fix edits and which
does not name itself, gave 1412 passed and 9 skipped, exit 0 (executed).
`bin/seal layout --check` exited 0 (160 files read, 0 refused), and
`bin/seal rules --check` exited 0 (all 266 check lines in 55 rule files
hold) (executed). This is not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at `afc53ac5` | the orchestrator, at `seal gate`, before the sealer is spawned |
| The fix pass's claim that `ruff check` and `ruff format --check` exit 0 on the two Python files `c6730b99` edits: unverified here, because the lint is not this round's to run | `.github/scripts/publish_release_note.py`, `tests/behaviour/test_release_hygiene.py` | the orchestrator, at `seal gate` |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| Step 3 of the update skill, run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

This round leaves nothing open. What comes due is the orchestrator's broad
run, `seal gate`, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git show --stat` of `c6730b99` and `afc53ac5`; `git diff aa81491f afc53ac5 -- seal/` | three files and ten lines in the fix; two lines of `round-8.md` in the record commit |
| `git diff -w --word-diff aa81491f c6730b99 -- templates/setup/config.md` | one clause removed, no other word changed |
| the fix pass's recorded `git grep -n -E` at `afc53ac5`, over the paths its `answer:` names | exit 0, 12 lines, each a coordinate the `answer:` names |
| `git grep -n -E` for "markers and anchors", "anchor table's header" and "release section's" | the template, `pact_check.py:188` and `round-8.md` only |
| `git show v0.23.1:CHANGELOG.md`, `git show --stat 268480ac`, `git log -S test_no_section_accumulates_entries_in_the_shared_file` | the heading is a version and a date; `268480ac` removed the case and the file |
| `git blame -L 38,46` and `awk` widths on `publish_release_note.py`; `awk` widths on `test_release_hygiene.py:1144-1156` | `:44` is 112 columns, `:40` and `:46` were already over 88; the comment is at most 83 |
| the 58 removed test names, each with `git grep -w` at `afc53ac5` outside the exclusions the third confirmation names | one hit, a same-named live case in another module |
| `python3 -I` over `.test_durations` against the `def test_` names in the tree | 6774 entries, 174 name no defined case |
| `git grep -l -E` with four module patterns over `tests/*test_*.py` | 26, 47, 26 and 47 modules; none gives 33 |
| `bin/test -q` over the 27 modules the last confirmation names | 1412 passed, 9 skipped, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

No probe file was written. The module lists, the diff and the command
outputs this round saved sat in the session's scratch directory and are
removed before hand-back.
