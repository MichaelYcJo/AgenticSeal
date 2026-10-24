# Guarantee: 1792619407-the-replay-scaffold-and-reader-misread-rounds

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md is written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` *The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | 24482f01 against eae7f0ad |
| Broad gate | 1219ffdd against eae7f0ad |

The base `release/v0.22.3` resolves to eae7f0ad through `@{upstream}`, the
first of the three refs `broad_gate.py#resolve_base` tries, and
`git ls-remote origin` gives 24482f01 for the branch (executed). This audit
follows `agents/sealer.md` and `templates/sdd-guarantee.md` as they stand at
HEAD, as the spawn prompt directs, because the loaded plugin copy (0.22.2)
writes the older verdict shape.

`broad-gate.md` names 1219ffdd. It is an ancestor of HEAD, and
`git log --no-merges --name-only 1219ffdd..HEAD ^eae7f0ad` lists one commit,
24482f01, which touches only this item's `broad-gate.md` and `overview.md`
(executed). The run's log beside the body reads `BROAD GATE PASSED`, the
suite 7420 passed and 13 skipped, chain exit 0, under the command
`uvx ruff check . && uvx ruff format --check . && bin/test -q` (read). No
broad check was run here.

Every re-run below ran in a scratch clone of the branch at 24482f01. A
`seen red` was re-run by restoring the one changed file from the commit the
claim names and running the named cases, then restoring HEAD's file. The
clone and the scaffold directories were removed after the audit.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Phase 3's reader cases fail against the reader before the redesign: 7 failed (S5a, S5b, S5c, round 3's record) | `phases/phase-3.md:32-45` | `noninferiority.py` restored from 9f8fe13b, then `pytest tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k "never_closes or cannot_read or closed_fence or opener_inside"` | holds: exit 1, 7 failed, the seven cases the record names; at HEAD the same cases pass (executed) |
| Round 4's fix case gives no rows for both shapes against ad78bfb6 | `rounds/round-4.md:51` | `noninferiority.py` restored from ad78bfb6, then `pytest … -k cannot_split` | holds: exit 1, 2 failed, each `assert [] == ['', '', '']`, for a second `## Findings` section and a misspelt heading (executed) |
| The CRLF line check's two cases were red against 729cea97 with the Windows message | `overview.md:18` | `seed_defects.py` restored from 729cea97, then `pytest … -k ends_with_crlf` | holds: exit 1, 2 failed, each `AssertionError: a.py:40 is not '    return b != 2'`, the message `tests` run 39691387210 printed (executed) |
| S1: the base's `FINDING_ROW` gives two rows over the fenced-fix record, the new reader one | `spec.md:211`, `phases/phase-1.md:68-74` | a probe loading the base's `FINDING_ROW` line from `git show eae7f0ad:evals/scripts/noninferiority.py` and HEAD's `finding_rows`, over the S1 case's `printed(FENCED_FIX)`; probe deleted | holds: base gives `src/a.py:11` and the fenced `src/a.py:40`, HEAD gives `src/a.py:11` alone (executed) |
| S7: `compare` and `regrade` refuse a committed side with exit 2 and the side's file named | `phases/phase-1.md:87-94` | `noninferiority.py compare --agent warden --phase 3 --old …/1792368015-…/evals/baseline-warden.json --new …/warden-phase-3.json --out <scratch>`, and `regrade --side` over the same file | holds: exit 2 each, the line naming the file and `replay-1791382684-r2, run 0, keeps no report_text` (executed) |
| Every side committed before #986 keeps no `report_text` | `changelog.md:17-19`, pr-body.md line 9 | a scan of every tracked JSON file holding `cases` with runs | holds: 18 sides, no run of any keeps `report_text` (executed) |
| S10: each regenerated seeded scaffold exits 0, holds no rounds path, resolves every `plan.md` Status commit, and keeps no copy or name of the original target | `phases/phase-2.md:89-97` | `sh scaffold.sh` for the four seeded cases, each in an empty scratch directory over the GitHub remote, then `git grep`, `cat-file -e` of each Status commit and of the original target, `grep -r <target> .git --exclude-dir=objects`, `fsck --unreachable --no-reflogs` | holds: exit 0 each; rounds path grep exit 1 and no directory; every Status commit resolves; the original target `cat-file -e` exit 1 (full hash; the record's 128 is a short hash's, both non-zero); its grep exit 1; no unreachable object (executed) |
| The amend keeps the original committer and date, and the clone keeps no remote | `changelog.md:25-30`, `rounds/round-1.md:148` | in the same four clones, `git log -1 --format='%cn %ce %cI'` against the original target's, `git remote`, `git for-each-ref` | holds: committer and date equal in all four; no remote; refs are the branch and round 1's one base ref (executed) |
| Q5's residue: `HEAD^..HEAD` changes the seeded file inside a records commit | `phases/phase-2.md:34-39` | `git diff --stat HEAD^ HEAD` in the four clones | holds: 7, 5, 3 and 3 files changed, as the table's rows list (executed) |
| S11: the seeded cases are generated, so regenerating them changes no file | `phases/phase-2.md:102-104` | a probe calling `seed_defects.main(["--case", …])` for the four cases, with `rt.origin_url` handed the GitHub URL the committed scaffolds carry, since the scratch clone's origin is a local path; then `git status --porcelain evals/behaviour/`; probe deleted | holds: generator exit 0, four cases written, porcelain empty (executed) |
| S12: only the seeded cases move | `phases/phase-2.md:106-108` | `git rev-parse eae7f0ad:<dir>` against `HEAD:<dir>` for the four `replay-*` cases, `rule-warden-one-finding` and the `smith`, `framer` and `sealer` suites | holds: equal for all eight (executed) |
| S13: `report_rows` and `FINDING_ROW` stand outside `seal/` only on the two test lines | `spec.md:226`, `phases/phase-1.md:96-101` | `git grep -n -e report_rows -e FINDING_ROW -- ':!seal'` | holds: `tests/test_a_rewritten_definition_proved_non_inferior.py:960` and `:1704` alone (executed) |
| Removes: `FINDING_ROW`, `report_rows`, `unhidden` | `spec.md:283-284`, `spec.md:289` | the S13 grep; `git grep -n unhidden -- ':!seal'` | holds: only S13's two lines; `unhidden` exit 1 (executed) |
| Removes: the seeded scaffold's `git rm` of the rounds, and the squash commit as the case's tree | `spec.md:286-287` | `git grep -n "git rm" -- evals/behaviour/warden evals/scripts` at HEAD and at eae7f0ad; the fetch and checkout lines of the four scaffolds against `round-1.md` read at each squash commit | holds: none at HEAD, four scaffolds and the generator at base; each scaffold checks out round 1's target, 7795f390, 7e68ed00, 4279671d and 56172bbe, as each round 1 names (executed) |
| Removes: the six seeded entries of `recurred_truths.json` | `spec.md:288` | count of entries and of `seeded-` entries at eae7f0ad and HEAD | holds: 17 with 6 seeded at base, 11 with none at HEAD (executed) |
| Removes: the old S6 case name, and the four seeded case directories as generated before | `spec.md:290-291`, `changelog.md:33-37` | `git grep` of the old test name; `ls evals/behaviour/warden/` | holds: the old name stands only in `spec.md`'s own rows; `seeded-4d316179` and `seeded-9b644676` are gone, `seeded-279a580b` and `seeded-ad447367` rewritten, `seeded-8a100e13` and `seeded-f1c9932d` added (executed) |
| The `tests` runs: 8ef3a12c and 4875eb7b each failed one Windows split, first a remote path that lost its backslashes, then the CRLF line check; 8c7ba12d, ad78bfb6 and c64c8845 passed every leg | pr-body.md lines 32-33 | `gh run view <id> --json headSha,conclusion,jobs` and `--log-failed` for 39688600936, 39691387210, 39692693904, 39693779473, 39694379127 | holds: the first two `failure` at those commits, one job each, `windows-latest … --group 1`, with `fatal: 'C:UsersrunneradminAppData…' does not appear to be a git repository` and `a.py:40 is not '    return b != 2'`; the last three `success`, every pytest leg, lint and grammar jobs `success`, `release-report` skipped (executed). No file outside the item's records changed after c64c8845 (executed: `git diff --name-only c64c8845 HEAD`) |

The sample left out the smith's `mutation-check` runs and the phase
boundary module runs; the seen-red re-runs above revert the same units for
phase 3, round 4 and the CRLF fix, and the broad run covers the modules.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | A side keeps the record whole and is read by the check's split; a record the check cannot read or split gives one empty false row per raw finding heading and no find; a side without `report_text` is refused; a seeded case is built at round 1's target, keeps no copy of the original commit, and carries round 1's confirmed fixes as truths; the paid baseline is out by default, Q1, and the `HEAD^` residue is Q5, both the owner's | the build: every scope item and `Removes` row re-run above holds in the tree; the issue: both defects fixed with cases, and the spec's reading that defect 1 sits in the seeded scaffolds, not the replay ones, holds (executed: at eae7f0ad `git rm` stands only in the four seeded scaffolds and `seed_defects.py`) | none. Scope item 6 and *Data & interfaces* do not name the removed remote or the committer kept; `overview.md:17` records both as divergences, and the changelog and body state them |
| the build | The diff against eae7f0ad and the three phase records: the reader, the kept and masked text, the refusal, the seeded generator at round 1's target, four regenerated cases, two of them replacements under Q3 | the spec and every claim re-run above; the overview's divergence rows, each a rule the code states (`noninferiority.py#reads_record`, `#apart`, `seed_defects.py#MUTATE`, `replay_targets.py#ref_base`, `#round_target`) | none |
| the last round | Round 6 at a1be6ae1: round 5's one finding is confirmed, no code changed since c64c8845, nothing opened; the full suite left to the broad run | the build (no file outside the item's records changed after c64c8845, executed) and the broad run at 1219ffdd, which follows a1be6ae1 by round 6's record alone | none |
| the changelog | Fixed: the reader by the check's split, the kept masked record, the floor for a refused record, the refusal of a side without text; the seeded case at round 1's target, committer kept, remote removed, reflog, `FETCH_HEAD` and unreachable objects gone, the CRLF line check, the two replacements. Changed: the warden's suite from the squash commit that lands #986 | the build, every sentence against the claims re-run above, and the spec's scope items 1 to 11 | none |
| the pull request body | The changelog's facts; Q1 and Q5 on their stated defaults and open for the owner; round 2's two remaining routes to the shipped code; the verification table; six rounds; no gate changes; the misnested fence left open | Each verification row against its record: the scaffolds row against `phases/phase-2.md:89-97` and `rounds/round-2.md:114-123`, and my four runs; the reader row against `phases/phase-1.md:68-74`, `rounds/round-1.md:81`, `rounds/round-2.md:57`, `phases/phase-3.md:32-45` and `rounds/round-4.md:51`, its five shapes each pinned by a case; the two CI rows against `gh`; the broad-run row against the log; the review row against each round: round 1 five findings, all `fixed`; round 2 four `confirms:` of round 1 and two findings each with a `regression:` line; round 3 one regression, `deferred the frame`; round 4 one finding `fixed d4e134cd`; round 5 one `fixed 14349634`; round 6 `confirms: round-5#1` and no finding. The Q1 row names the paid side the issue's *Done when* asks for as not run and open for the owner, as `questions.md:48`'s default says it must. "No gate changes" holds by `CONTRIBUTING.md`'s meaning of a gate, a check on a commit or branch switch, which no file of the diff is. The "every shape the rounds found" of the reader row is read as the rounds' findings: the misnested fence the rounds named under `## Not judged` has no fix and no case, and the body names it under *Left open* | none |

Verdict: sealed
