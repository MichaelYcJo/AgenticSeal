# Guarantee: 1793582903-each-entry-links-its-pull-request

| Field | Value |
|---|---|
| Broad gate | 852178961 against 30ba21373 |

## Claims re-run

The base `release/v0.28.0` resolved to `30ba21373` through
`release/v0.28.0@{upstream}`. Every run below took place in a
`git clone --no-local` of the worktree at `41f766529` under the sealer's
scratch directory, which is gone. The worktree itself was only read. The
seen-red cases ran with the changed source restored from the commit named
in the Command cell, and the tests at HEAD.

| Claim | Source | Command | Result |
|---|---|---|---|
| The gate's newest run is at HEAD, or followed only by this work item's records | `trail/gate.md:4` | `git merge-base --is-ancestor 852178961 HEAD`; `git log --no-merges --name-only 852178961..HEAD ^30ba21373` | holds (executed): ancestor, exit 0; one commit follows, `41f766529`, touching `trail/gate.md` alone |
| The body below `## From the records` is the records' own text | the spawn prompt; `pr-1139.md:16` | `seal pr-body seal/threads/1793582903-each-entry-links-its-pull-request --body pr-1139.md --check`, with the installed `seal` and with the tree's `bin/seal` | holds (executed): `matches`, exit 0 from both |
| #1216's copy notice on the design's `add` is gone after `852178961` | `pr-1139.md:10`; the spawn prompt | `python3 skills/code-review/scripts/chain_check.py --baseline 30ba21373 --worktree --sealing` | holds (executed): exit 0, no copy notice; its one line names `guarantee.md` as not yet written |
| S4, seen red: `test_apply_keeps_a_directory_its_published_note_does_not_carry` fails at `assert code == 1` with `0 == 1` | `trail/phases/phase-2.md:123-125` | source restored from `30ba21373`; `bin/test tests/skills/test_settle.py -p no:xdist -q -k "..."` | holds (executed): `assert 0 == 1` |
| S6, seen red, all three states: `test_apply_stops_where_the_release_list_cannot_be_read` fails at `assert code == 2` with `0 == 2` | `trail/phases/phase-2.md:126-127` | the same run | holds (executed): `[fails]`, `[garbled]`, `[entry]` each `assert 0 == 2` |
| S7b's kept case, seen red, both states, at `0 == 1` | `trail/phases/phase-2.md:128-129` | the same run | holds (executed): `[another]` and `[a draft]` each `assert 0 == 1` |
| The git case, seen red: `test_a_git_that_cannot_read_the_adding_commit_stops_apply` at `0 == 2` | `trail/phases/phase-2.md:130-131` | the same run | holds (executed): `assert 0 == 2`; the run ended 7 failed, exit 1 |
| S1 to S3, seen red: `Test_main::test_each_entry_links_the_pull_request_that_added_it` fails at its first assertion, the link line of `1700000001-linked`, with the note holding the marker | `trail/phases/phase-1.md:93-96` | source restored from `30ba21373`; `bin/test tests/github/test_publish_release_note.py -p no:xdist -q -k test_each_entry_links_the_pull_request_that_added_it` | holds (executed): failed on `[#42](https://github.com/o/r/pull/42)` with the note holding `<!-- specs/1700000001-linked -->`, exit 1 |
| `adding_commit` without `--no-follow` fails `[log.follow]` alone at `1 == 2` | `trail/phases/phase-1.md:103-106`, `:116` | `bin/seal mutate skills/settle/scripts/settle.py --replace '            "--no-follow",\n' '' --tests "bin/test tests/skills/test_settle.py -q -p no:xdist -k adding_commit"` | holds (executed): red, exit 0; `[log.follow]` failed at `assert 1 == 2`, the other three passed; the file was restored |
| The fix pass's `NOT_BUILT` case is red against the source before the fix, at `assert code == 0` with the `kept ... does not carry its entry` line | `trail/rounds/round-1.md:112` | source restored from `bbd15ec5e`, then from `30ba21373`; `bin/test tests/skills/test_settle.py -p no:xdist -q -k "test_apply_removes_where_no_published_note_is_built_from_the_fragments or test_apply_removes_a_directory_whose_fragment_is_empty"` | holds (executed): at `bbd15ec5e`, `assert 1 == 0` with that `kept` line; at the base, red on the missing `no note read:` line |
| The fix pass's `NO_TEXT` case is red against the source before the fix, the same way | `trail/rounds/round-1.md:172` | the same two runs | holds (executed): at `bbd15ec5e`, `assert 1 == 0` with the `kept` line; at the base, red on the missing `no note read:` line |
| The four narrow modules pass at HEAD, 216 cases | `trail/rounds/round-2.md:174-177` | `bin/test tests/skills/test_settle.py tests/github/test_publish_release_note.py tests/text/test_settle_reads_before_it_removes.py tests/behaviour/test_no_document_names_the_old_roots.py -q` | holds (executed): 216 passed, exit 0 |
| Every `## Removes` row: the marker, the docstring sentence, the marker in `skills/implement/SKILL.md`, `templates/setup/config.md` and `skills/implement/multi-repository.md`, the `KEEP` entry, the cases' pins, and "Shared mode never asks `gh`." stand nowhere in the tree; `docs/` is untouched | `frame/design.md:227-235` | `git grep -n -e '<!-- specs/' -e 'specs/{item}' -e 'specs/<work-item-id>' -e 'HTML comment naming' -- ':!seal/threads' ':!.test_durations'`; `git grep -n -i 'never asks'`; `git grep -n 'Each goes under an HTML comment'`; `git diff --stat 30ba21373...HEAD -- docs` | holds (executed): no writer of the marker is left. The hits are the policy text the rule changes rewrite (`docs/branch-and-release.md:78`), the settle's reader of the old marker (`settle.py:101`, `:411`, `SKILL.md:460`), the old-roots case's offenders, the absence assertion at `test_publish_release_note.py:366`, and fixtures the design puts out of scope. `docs/` has no change |
| The changelog's removal: no entry carries the hidden comment | `changelog.md:3` | the same `git grep`; `.github/scripts/publish_release_note.py#section` read at HEAD | holds (executed and read): `section` writes the link line or nothing |
| `921a020b7` changes two lines of `round-1.md` and no meaning | the spawn prompt; `pr-1139.md:10` | `git show 921a020b7` | holds (executed): the name of a host other than GitHub's, spelt as a domain, became `other-host` in the fix pass's answer and `a host other than GitHub's` in the probe row, nothing else |
| The broad run passed at `852178961`, 6235 passed and 12 skipped | `pr-1139.md:12`; the spawn prompt | read the gate's output file | holds (read): `BROAD GATE PASSED ... @ 852178961 against origin/release/v0.28.0 @ 30ba21373`, `6235 passed · 12 skipped`, chain exit 0. Not re-run (contract rule 2) |
| Round 1's `must`: before its fix, "in a user's repository every tagged directory would have been kept for ever" | `pr-1139.md:9`, the orchestrator's part; the same overstatement in `frame/plan.md:100`, the orchestrator's grounds | settle source restored from `a8d9015fa`; a probe `tests/skills/test_tmp_sealer_probe.py` over `test_settle.py`'s fixtures: `feat: a (#42)` tagged `v1.2.3`, and one published release whose body is GitHub's generated line `* feat: a by @x in https://github.com/o/r/pull/42`; run once, then deleted | does not hold (executed): exit 0 and `removed seal/threads/1700000001-a/`. `settle.py#carries` accepts that link anywhere in a body, and `round-1.md:47` says the same: "GitHub's own generated notes link `.../pull/N` and pass". Only a repository whose notes do not link each pull request at `github.com/<o>/<n>/pull/<N>` kept its tagged directories |
| "a SHA appears only in the terminal's `kept` line, as `git show <commit>:<path>`" | `pr-1139.md:7`, the orchestrator's part; `round-1.md:244-245` says the same | read `skills/settle/scripts/settle.py:525-532` and `tests/skills/test_settle.py:1741-1761` | does not hold (read): `NO_NUMBER` and `NO_TAG` print the adding commit's full SHA in the `no note read:` line under `removed`, and the S7 case pins both lines with `rev-parse` output. The note itself names no SHA, which holds |
| `log.showSignature=true` changes nothing `adding_commit` returns | `trail/phases/phase-1.md:58-63`, `gaps.md:8` | not re-run: it needs an ssh-signed commit | unverified; it rests on phase 1's probe. Nothing in the issue asks it, so no one owes an answer before the merge |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Each entry links the pull request its adding commit names, and the marker goes; one reader of that number; `--apply` keeps a directory its published note does not carry, reads notes only where some published release holds a renderer-shaped line, and names why no note was read; the policy changes through four rule changes | the issue's three *Done when* items; the build, with the departures the phase records name (`--no-follow --root` for `--no-renames`, `RELEASES_UNASKED` for `UNASKED`, `TAG_RE` taken from `settle.py#VERSION_RE`); the changelog | none |
| the build | `settle.py#adding_commit`, `notes`, `published_releases`, `carries` and `BUILT_RE`; the renderer's `section(entries, repo)` writing `PULL_LINK`; every note read before the first removal; exit 2 for an unreadable list or `git` | the design, the phase records' seen-red claims (sampled above), round 2's confirmations, the changelog | none |
| the last round | Round 2: round 1's `must` and `should` are fixed; three things weighed and not raised; nothing open | the build (its four narrow modules re-run above); the fix pass's reds (re-run above) | none |
| the changelog | Two `### Changed` entries: the link line and the gone marker; the note check, its cases of no note read, exit codes, and local mode | the build, line by line; the design's rule changes for where the settle writes the policy | none |
| the orchestrator's part of the pull request body | `pr-1139.md:1-14`: the change, the facts the check reads exactly, the earlier decisions, the questions, the rounds, the work after the rounds, and the gate | the issue, the design, the build, the records' copy and the gate on every sentence but two | Two sentences, contradicted by the tree. `:9` says that before round 1's fix every tagged directory in a user's repository would have been kept for ever: round 1's own record (`round-1.md:47`) and `settle.py#carries` at `a8d9015fa` remove a directory whose note GitHub generated (executed). `:7` says a SHA appears only in the terminal's `kept` line: `settle.py:525-532` prints one in each `no note read:` line for a commit that names no pull request or no version tag. The first overstatement also stands in `frame/plan.md:100`, the orchestrator's grounds for its first judgment. The second stands in round 1's confirmation `round-1.md:244-245`, the proofer's reading at `a8d9015fa`, which this verdict names and does not ask to rewrite |

Seen outside this audit, and no ground of its verdict: `cae15ac23` took one
space from the `settle --from DIR` line of `settle.py`'s usage block
(`skills/settle/scripts/settle.py:13`), so its text column stands one
column left of the other lines'. No record claims the block, and its
layout is the proofer's to judge.

```seal
target: 41f766529 against 30ba21373
Verdict: withheld reason: two sentences of the orchestrator's part of the pull request body do not hold against the tree. pr-1139.md:9 says that before round 1's fix "in a user's repository every tagged directory would have been kept for ever"; round-1.md:47 says GitHub's generated notes link .../pull/N and pass, and with settle.py at a8d9015fa a directory whose note GitHub generated was removed, exit 0 (executed), so only a repository whose notes do not link each pull request at github.com/<o>/<n>/pull/<N> kept them; the same words stand in frame/plan.md:100's grounds. pr-1139.md:7 says "a SHA appears only in the terminal's kept line"; settle.py NO_NUMBER and NO_TAG (skills/settle/scripts/settle.py:525-532) print the adding commit's full SHA in the no note read: lines, as tests/skills/test_settle.py:1755-1761 pins. Reword those two body sentences and the plan.md:100 clause; the code, the records' copy and every other claim sampled hold.
```

## Re-audit at 4a3596320

One commit follows the block above's target: `4a3596320`, which touches
`frame/plan.md` alone. The pull request body file was rewritten outside
the tree. The claims whose coordinates these touch are re-read below, and
the claims above that nothing touched stand as they were run.

| Claim | Source | Command | Result |
|---|---|---|---|
| The gate's newest run is at HEAD, or followed only by this work item's records | `trail/gate.md:4` | `git merge-base --is-ancestor 852178961 HEAD`; `git log --no-merges --name-only 852178961..HEAD ^30ba21373` | holds (executed): ancestor, exit 0. `41f766529` touches `trail/gate.md` and `4a3596320` touches `frame/plan.md`, both under `seal/threads/1793582903-each-entry-links-its-pull-request/` |
| The body below `## From the records` is the records' own text | `pr-1139.md:16` | `seal pr-body seal/threads/1793582903-each-entry-links-its-pull-request --body pr-1139.md --check`, with the installed `seal` and with the tree's `bin/seal` | holds (executed): `matches`, exit 0 from both |
| `4a3596320` changes only the grounds of the first judgment row | the coordinator's message | `git show 4a3596320` | holds (executed): one row of `frame/plan.md:100`, its Grounds cell alone |
| Round 1's `must` reached a user's repository whose notes link no pull request as `github.com/<owner>/<name>/pull/<N>`, hand-written notes or ones linking issues among them, and every tagged directory there would have been kept for ever; GitHub's generated notes were never affected | `pr-1139.md:9`; `frame/plan.md:100` | the probe of the block above, at `a8d9015fa`; `settle.py#carries` and `#notes` at `a8d9015fa` read | holds (executed and read). A GitHub-generated note carrying the link went, exit 0. `carries` keeps only a note holding no such link to that pull request. "Tagged" reads as the changelog's "gets as far as a version tag": a directory whose adding commit names no pull request never reaches the tag lookup, and it goes |
| A SHA appears only in `seal settle --apply`'s terminal output: the `kept` line's `git show <commit>:<path>`, and the adding commit on a `no note read:` line | `pr-1139.md:7` | `git grep -n 'git show {at}\|{commit}' -- skills/settle/scripts/settle.py` | holds (executed): `NO_NUMBER` and `NO_TAG` (`:526`, `:530`) print the adding commit, `NOT_CARRIED` and `NO_RELEASE` (`:544`, `:550`) print `git show {at}:{path}`, and `section` writes no SHA into the note. The other hit, `:1424`, is local mode's dry-run line naming a merge commit, which predates this work and names no entry |
| The orchestrator's commits include `4a3596320` | `pr-1139.md:11` | `git log --oneline 30ba21373..HEAD` | holds (executed) |

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | unchanged since the block above | as the block above states | none |
| the build | unchanged since the block above: `4a3596320` touches no code | as the block above states | none |
| the last round | round 2, unchanged | as the block above states | none |
| the changelog | unchanged | as the block above states | none |
| the orchestrator's part of the pull request body | `pr-1139.md:1-14`, with `:7`, `:9` and `:11` rewritten | the issue, the design, the build, round 1's record at `round-1.md:47`, the records' copy, the gate, and `frame/plan.md:100` as `4a3596320` left it | none. Round 1's confirmation at `round-1.md:244-245` still says the SHA appears only in the `kept` line. It is the proofer's reading at `a8d9015fa`, copied into the body as the record's own text, and `pr-1139.md:7` now states the fact. That gap stays named here; it grounds no verdict |

```seal
target: 4a3596320 against 30ba21373
Verdict: sealed
```
