# Review round 1: 1793251202-the-citation-case-misses-files-and-wrapped-comments

target: 9d3a3929 against origin/release/v0.24.2

This is round 1, so no earlier round exists and no fact was carried. Every
fact below was found again this round, in a `git clone --no-local` of the
branch at 9d3a3929. Each run went through the repository's `bin/test`.

## Findings

## Confirmations

confirms: none
Phase 1 is a move. `phase-1.md` claimed the seven cases moved unchanged
except for two helper renames, the banner, and one wrapped comprehension. I
took the lines phase 1 removed from the contract module and the lines it
added to `tests/behaviour/test_a_cited_section_stands_in_its_file.py`. With
`contract_dangling` renamed back to `dangling` and `read_at_root` back to
`read`, `diff -w` showed only the two imports, the renamed banner, and the
`found = [...]` comprehension split over three lines (executed). So the
claim holds.

confirms: none
The 15 timing keys were re-keyed and nothing else changed. A read-only
script compared `.test_durations` at 8d8d6390 with the file at the target.
It found 15 keys removed, all under the contract module's path, and 15
added, all under the module's path. The case ids and seconds match one for
one, and the keys are still sorted (executed). The same script found the
five new case ids unpriced, as `phase-2.md:106-108` says. Several of the
module's older cases have no key at the base either, among them
`test_a_record_is_not_read`.

confirms: none
The plan's phase command passes at the target. The plan's eight modules ran
with `-q`: 337 passed, exit 0 (executed). The crafter claimed 337.

confirms: none
The tree reads as the frame and `phase-2.md:24-30` say. I imported the
module's own functions and called them over the clone's tree.
`corpus(ROOT)` lists 913 tracked paths and returns 325 files. The
contract-rule reader recognises 232 citations, none dangling, and
`near_citations` finds nothing (executed). The crafter recorded 912 paths at
37434c86. The one extra path is `trail/phases/phase-2.md`, which the closing
commit 9d3a3929 added under `seal/threads/` and the corpus leaves out.

confirms: none
Each new case fails against the old reading. In the clone, I made three
edits to the module. `corpus` was cut to the old walk: the six trees and
`CONTRIBUTING.md`, with the five extensions only. `cited_sections` and
`near_citations` were changed to read the raw text instead of `flowing`.
The module then failed 15 cases (executed). Among them are all five new
case ids: S3, the three ids of S5 and S6, and S7. Both ids of
`test_a_record_is_not_read` also failed. The two contract tree cases passed,
which is expected, since the tree is green under either reading. The edits
were reverted with `git checkout` and the clone was clean afterwards. This
matches the crafter's copy A in `phase-2.md:57-67`. I did not repeat copy B
separately. The five `seal mutate` runs in `phase-2.md:77-91` were read and
not repeated.

confirms: none
Departure 1, weighed: `contract_dangling` takes `[(rel, text)]` and not a
root. `frame/design.md:155-161` says the reader takes a root, so that both
the tree case and a fixture case pass one. In the build, every caller that
reads a tree passes `corpus(root)[1]` (`:488`, `:651`, `:716`, `:738`,
`:755`). So fixture trees are read, which is what the frame needed. The
crafter's grounds hold: the tree case's two floors need the file list, and
a reader that took a root would have to list twice or return a second
value. One cost comes with the choice. No case pins that
`test_every_cited_section_exists` (`:645-656`) reads through `corpus`. If
that case went back to a narrower walk, its floors would still pass, since
the frame measured the old walk at 262 files and 230 citations. A
root-taking reader would close this only if the tree case still called it.
The composition is four lines and visible at `:650-656`, so I record it here
and raise no finding.

confirms: none
Departure 2, weighed: S4 went into `test_a_record_is_not_read` (`:472-490`)
instead of a case of its own. The crafter cited its own rule *A new test
starts from its group*, and the case already builds a file under each
`RECORDS` prefix beside `a.md`. The new assertion adds no failure that the
case's section-citation assertion does not already give. Both read the one
`corpus`, so a dropped `RECORDS` filter fails the earlier assertion first
(read). The assertion is there because the frame asked for S4, and keeping
it costs three lines.

confirms: none
Departure 3, weighed: S4 went red under copy A, while the plan's row said
"S4 passes on both sides". The cause is the one the crafter gives:
`citations()` reads the same `corpus`, and the old walk does not read a
top-level `a.md`. My old-reading run above reproduced the red at both ids
(executed). The plan assumed a separate case. Nothing in the plan required
S4 to be shown red, so the departure owes nothing.

confirms: none
The new reading behaves as the design states at edges no case names. A
probe file of six cases passed, exit 0 (executed), and was deleted. The
cases were: a trailing `#` comment on a code line followed by a comment
line in `.py`, named at line 1; a wrapped citation in a `.sh` file; a
wrapped citation inside a fenced block of a `.md` file, which is not read
(the stated `.md` limit, `frame/design.md:94-97`); a citation named at its
right line after a joined literal earlier in the file; an indented
near miss in `.yml`; and a bare `rule <N>` across `#` in an `agents/` file
that is not `.md`.

confirms: none
S8 holds. The module docstring (`:1-31`) names the corpus as the tracked
paths outside `tests/censuses.py#RECORDS`, on disk, decoding as UTF-8. It
names the three kinds left out, each with its reason: records, files that
are not UTF-8, and files the working tree deleted. It also says the
`flowing` reading keeps a `#` that opens a `.md` line (read).

confirms: none
Nothing still states the old fact (contract rule 19). `git grep` for
`tree_files`, `CITED_TREES`, `CITED_FILES`, `six trees`,
`test_every_cited_section_exists`, `near_citations`,
`test_no_file_cites_the_contract` and `#citations` outside `seal/threads/`
found only the module and its `.test_durations` keys, plus the unrelated
`worktree_files` in `chain_check.py` (executed). Every other file that names
the contract module does so for `HEADING` or for the contract's own shape.
`skills/writing-style/SKILL.md:268` names both modules. The registry row is
now `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#corpus`
(`:92`), and that module passed within the 337.

confirms: none
`frame/design.md:72` says the corpus "reads one `git ls-files` listing per
run". I read "per run" as one listing per call of the shared function,
which `corpus` (`:185-198`) does, returning both `tracked` and the files.
Three tree cases each call it once per module run. Before, the tree cases
made one listing and two `os.walk` passes; now they make three listings.
The frame measured a full read of the 325 files at 0.066 s.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether this work item owes a `gaps.md`. `skills/implement/SKILL.md:343` opens one at the first divergence or unverified item. `agents/crafter.md:16-20` lets the crafter write `gaps.md` only where the plan's row asks for it, and neither row did. The three divergences and the unpriced keys stand in `phase-2.md:32-48` and `:106-108`, and `seal pr-body` will print `gaps.md` as absent. | `seal/threads/1793251202-the-citation-case-misses-files-and-wrapped-comments/` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck. The crafter's label `unverified`, with the orchestrator named, is honest: no agent ran them, and this round did not either (contract rule 2). | the broad gate | the orchestrator, at `seal gate` |
| Whether the five unpriced case ids keep `test_the_durations_file_prices_the_suite` under `STALE_SHARE` (5 %). That case judges the whole collected suite, so only the broad run reads it. | `.test_durations` | the orchestrator, at `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the plan's eight modules with `-q`, at 9d3a3929 | 337 passed, exit 0 |
| `diff -w` of phase 1's removed lines against its added lines, two renames undone | three hunks: imports, banner, one wrapped comprehension; exit 1 |
| `python3 -I -c` comparing `.test_durations` at 8d8d6390 with the target | 15 removed, 15 added, same ids and seconds, sorted; five new ids unpriced; exit 0 |
| `.venv/bin/python -c` calling `corpus`, `cited_sections`, `contract_dangling` and `near_citations` over the tree | 913 tracked, 325 read, 232 citations, none dangling, no near miss; exit 0 |
| `bin/test tests/behaviour/test_tmp_contract_flowing_edges.py -q -p no:xdist -p no:cacheprovider` | 6 passed, exit 0; file deleted |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -p no:cacheprovider -rf`, with `corpus` cut to the old walk and both readers off `flowing` | 15 failed, 28 passed, exit 1; the five new ids and both `test_a_record_is_not_read` ids among the failures; reverted, clone clean |
