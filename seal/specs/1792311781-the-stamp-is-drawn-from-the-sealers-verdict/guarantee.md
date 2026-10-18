# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | f2c07086 against f6ae6db6; earlier run: f2f7b6d5 withheld |
| Broad gate | 7be0f715 against f6ae6db6 |

## Claims re-run

<!-- One row per act of `agents/sealer.md` step 3, whatever the act, and one
per thing the act checks. `Result` reads `holds`, or `does not hold — <what
came back>`, and a `does not hold` is what the verdict names. -->

`<base>` is `release/v0.22.1` resolved as `broad_gate.py#resolve_base` does:
`release/v0.22.1@{upstream}` and the local branch do not resolve here, and
`origin/release/v0.22.1` answers f6ae6db6, an ancestor of HEAD. This is a
re-run over the earlier guarantee at f2f7b6d5. Outside this item's records,
the commits since then (d6e9d285, fa551683, 9e8c1532) change two paths,
`assets/seals/README.md` and `tests/test_one_word_one_meaning.py`, so the
claims re-run below are the earlier run's two `does not hold` rows, the
earlier `seen red` whose case lives in the touched test module, the two new
`seen red` claims rounds 9 and 10 rest on, and the `## Removes` rows again.
Each `seen red` was re-run in a clone of the branch at f2c07086 under the
session scratch directory (`<item>/at-base/`), with the named file restored
from the commit the claim names, and the clone was removed afterwards; the
tree under audit was not changed.

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at HEAD or followed only by this item's records | `broad-gate.md:5` (`7be0f715 against f6ae6db6`) | `git log --no-merges --name-only 7be0f715..HEAD ^f6ae6db6`; `git merge-base --is-ancestor 7be0f715 HEAD` | holds — one commit, f2c07086, touching only `seal/specs/1792311781-…/broad-gate.md`; 7be0f715 is an ancestor of HEAD (executed) |
| The earlier run's other claims stand, since nothing they read changed | the earlier `guarantee.md` at 527afede, rows 2–11 and 13–29 | `git diff --stat f2f7b6d5 HEAD -- ':(exclude,glob)seal/specs/**'` | holds — two paths: `assets/seals/README.md` and `tests/test_one_word_one_meaning.py`; no code path any of those rows re-ran (`broad_gate.py`, `seal_stamp.py`, the hooks, the docs other than the emblems page) changed (executed) |
| The sweep found and reworded every sentence calling the broad gate's run a stamp (the earlier `does not hold`) | `phases/phase-3.md:43-46` | `git grep -n -i -e "gate's stamp" -e "gate draws a stamp" -e "gate's run draws" -e "Where the stamp is drawn" -e "stamp drawn by the"` outside `seal/specs/**`, `CHANGELOG.md`, `changelog/`; then `git grep -n -i -P` of gate then up to five words then `stamp`, and the passive `stamp(s) is/was/are/were drawn by/from the/a (broad) gate`, outside the same and `tests/` | holds now — the fixed-string grep hits only `tests/`: the sweep's own pattern, comment and pinned sentences (`test_one_word_one_meaning.py:479-527`), its history comment (`:180`), a docstring `overview.md` §*Not done* leaves as history (`test_the_stamp_reaches_the_person_it_is_drawn_for.py:1`) and the absence assertion (`:1321`); the wider pattern finds nothing outside `tests/`. `assets/seals/README.md:1-11` says the stamp is the sealer's (executed, read) |
| Removes: `docs/the-broad-gate.md` §*Where the stamp is drawn* (the earlier `does not hold`) | `spec.md:181` | the same `git grep` of `Where the stamp is drawn`; `grep -n '^## ' docs/the-broad-gate.md` | holds — no citation stands outside `tests/`; the section is absent (executed) |
| `test_no_instructing_document_gives_the_stamp_to_the_broad_gate` is red on the emblems page as f2f7b6d5 carries it | its docstring, `tests/test_one_word_one_meaning.py:496-500`; `rounds/round-9.md` probe row 2 | clone at f2c07086; `git checkout f2f7b6d5 -- assets/seals/README.md`; `bin/test tests/test_one_word_one_meaning.py -q -p no:xdist -k test_no_instructing_document_gives_the_stamp_to_the_broad_gate`; the file restored | holds — 1 failed, exit 1, three hits on the page: the heading's `broad gate's stamp`, `The broad gate draws a stamp`, and `Where the stamp is drawn`; `git status --short` clean of tracked changes after the restore (executed) |
| `test_the_stamp_sweep_reads_the_gates_run_and_the_passive` is red with the two-word pattern d6e9d285 wrote | its docstring, `tests/test_one_word_one_meaning.py:513-518`; `rounds/round-9.md:270` | in the clone, `STAMP_GIVEN_TO_THE_GATE` replaced with d6e9d285's `r"\bgate(?:'s)?(?:\s+\w+){0,2}\s+stamps?\b\|Where the stamp is drawn"` by a script asserting the old block matched once; `bin/test … -k "test_the_stamp_sweep_reads_the_gates_run_and_the_passive or test_no_instructing_document_gives_the_stamp_to_the_broad_gate"`; the file restored | holds — 1 failed (`AssertionError: the broad gate's run draws the stamp`, line 528), 1 passed, exit 1 (executed) |
| The four cases of the touched module this item rests on pass at HEAD | `phases/phase-1.md:75-79` (`test_the_gate_never_says_sealed`), `rounds/round-10.md` (the two new cases and the fold case) | `bin/test tests/test_one_word_one_meaning.py -q -p no:xdist -k "test_no_instructing_document_gives_the_stamp_to_the_broad_gate or test_the_stamp_sweep_reads_the_gates_run_and_the_passive or test_the_gate_never_says_sealed or test_folding_the_seam_cannot_hide"` at f2c07086 | holds — 4 passed, exit 0 (executed); the earlier run's red for `test_the_gate_never_says_sealed` stands, its case unchanged by `git diff f2f7b6d5 HEAD` (read) |
| The emblems page's history: the S was carried by 0.20.0 through 0.22.0, and the red lily ended at 0.19.0 | `assets/seals/README.md:6-9`, `:70-71`; `rounds/round-9.md` finding 2 | per tag v0.19.0, v0.20.0, v0.21.0, v0.21.1, v0.22.0: `git ls-tree --name-only <tag> skills/verify/scripts/seal-mark.txt`, `git show <tag>:skills/verify/scripts/seal_stamp.py \| grep -c seal-mark.txt`, `git diff --quiet v0.20.0 <tag> -- …/seal-mark.txt` | holds — absent at v0.19.0 and not read there; present, read and unchanged from v0.20.0 through v0.22.0 (executed) |
| The S's missing entry is filed as #978 | `overview.md` §*Not done*; the pull request body's *Not in this pull request* | `gh issue view 978` | holds — open, titled for the S's missing entry, milestone `release: 0.22.2` (executed) |
| Every `Enforced by:` target resolves | `phases/phase-3.md:76` | `bin/rules --check` at f2c07086 | holds — exit 0, "all 497 `Enforced by:` targets in 60 rule files resolve" (executed) |
| Removes: the gate's values-file write and its outcome names | `spec.md:177` | `grep -cE 'SESSION_VAR\|NOTHING_RECORDED\|VALUES_UNWRITTEN\|NO_SESSION_FOUND\|DRAWN_AT_TURN_END\|SCALE_FOR_OLDER_HOOKS\|def common_dir\|def signal' skills/verify/scripts/broad_gate.py` | holds — 0 (executed) |
| Removes: the gate's terminal drawing and the terminal/pipe fork | `spec.md:178` | `grep -cE 'if terminal and item is not None\|console_is_terminal\|is_terminal' skills/verify/scripts/broad_gate.py` | holds — 0 (executed) |
| Removes: `SEALED` / `NOT SEALED` as the gate's heads | `spec.md:179` | `grep -c SEALED` of `broad_gate.py`, `bin/broad-gate`, `bin/broad-gate.cmd`, `docs/the-broad-gate.md`; `grep -cE 'NOT SEALED\|def not_sealed'` of `seal_stamp.py` | holds — 0 in each (executed) |
| Removes: the panel's `SEALED` title row | `spec.md:180` | `grep -c '("SEALED", "")' skills/verify/scripts/broad_gate.py` | holds — 0 (executed) |
| Removes: the sealer's clause *from its own run* | `spec.md:183` | `grep -c 'from its own run' agents/sealer.md` | holds — 0 (executed) |
| Removes: the bin header, module docstring, READMEs and bin inventory saying the gate stamps | `spec.md:186-188` | `grep -c "broad gate's stamp\|gate's stamp"` of `bin/seal-stamp`, `bin/seal-stamp.cmd`, `seal_stamp.py`, `README.md`, `README.ko.md`, `tests/test_a_reference_root_is_read_and_never_taken.py` | holds — 0 in each (executed) |
| Removes: the fragment's clause that a repaired row draws the stamp | `spec.md:191` | `git grep -n 'corrects that row in place'` excluding the rounds, `plan.md` and `spec.md` | holds — the hits are `phases/phase-6.md:55` quoting the frame's check and the earlier guarantee's row quoting the same (executed) |
| Removes: rows 182, 184, 185, 189, 190 | `spec.md:182-190` | carried from the earlier run: their files (`skills/code-review/orchestration.md`, `skills/verify/SKILL.md`, the hooks, the stamp tests, `seal_stamp.py`) are outside `git diff --stat f2f7b6d5 HEAD` | holds — unchanged since the earlier run read them (executed, read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The issue body (#975) | The stamp is drawn once per work item from `guarantee.md` reading `sealed`, never from the gate's run; the gate's line never says `SEALED` and draws nothing; a re-seal after `withheld` draws it then; item 4: the hook, `bin/seal-stamp`, the values file and the docs say what draws the stamp | the spec, the build, the changelog, the pull request body, and now `assets/seals/README.md:1-11`, which says the stamp is the sealer's and that the broad gate's run drew it only before #975 | none |
| The spec | S1–S14 as the issue asks; `## Removes` takes out §*Where the stamp is drawn* and every sentence on the old fact; the amend in a second clone a stated limit | the issue; the build's code and tests; the changelog; the pull request body; the tree, now including the emblems page (no citation of the removed section stands outside `tests/`). Its amend-only limit against the class the docs state is recorded in `overview.md:27` and decided by `questions.md` Q9 (a) | none unrecorded |
| The build (the diff, phases 1–7, the fix commits d6e9d285, fa551683, 9e8c1532) | The gate prints `BROAD GATE PASSED`/`FAILED` and draws nothing; `post-commit` queues the stamp from a `sealed` guarantee once per work item; the words follow, and the emblems page now sits under `SEAL_SWEPT` with a case that refuses a sentence giving the stamp to the gate | the issue and the spec in code and tests (every sampled `seen red` and `executed` claim held); rounds 9 and 10; the changelog; the pull request body | none standing. Phase 3's sweep claim (`phases/phase-3.md:43-46`) was false when written, and `overview.md:30` records the miss, its repair and the case that now reads the page |
| The last round (round 10) | No finding; round 9's two closes hold; the residual reach of the pattern (`are`/`were` passive, four or more words) is outside round 9's sentences and no swept file says it | the build at e8a8ac06, `overview.md`, #978, the page's facts at every tag; my wider `git grep -P` over the tree outside `tests/` finds none of the residual forms either | none |
| The changelog fragment | The stamp is the sealer's, queued at a `sealed` guarantee's commit, once per work item with the stated limits; the gate says `BROAD GATE PASSED`/`FAILED` and draws nothing; `seal-stamp --from`, the hook and `specseal-stamp/` unchanged; the sealer measured `pass` | the code, the pull request body, the issue, the emblems page's new wording ("drawn once per work item, at the commit of a `guarantee.md` reading `sealed`") | none |
| The pull request body | The same story as the fragment; ten rounds, the sealer's `withheld` at f2f7b6d5 on `assets/seals/README.md` and rounds 9–10 on its repair, round 10 finding nothing; the S's entry left to #978 | the changelog, `questions.md`, the ten round files under `rounds/`, #978 (open), the earlier guarantee at 527afede, the issue | none |

Verdict: sealed
