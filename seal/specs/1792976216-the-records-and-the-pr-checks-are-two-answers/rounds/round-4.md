# Review round 4: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: d0ba9fba against release/v0.22.4

## Findings

This round opens no finding. It read the reframe and phase 3,
`64a13a36..d0ba9fba`, against the reframed `spec.md`, `plan.md` and
`questions.md`, and then the branch as a whole, `02ee12de..d0ba9fba`.

## Confirmations

confirms: round-3#1
The reframe closes the finding. `spec.md:482-485` wraps the `change` to
`docs/the-review-and-parity-arms.md` after "except where the tree" (read).
The round replayed the 17 items onto `docs/` at `02ee12de` in a scratch
clone. Line 110 of that document is then 81 columns, line 111 is 74 and
line 112 is 44 (executed). `tests/test_docs_line_wrap.py` passed over the
applied `docs/`, inside the S8 run below (executed). The finding was closed
`deferred the frame`, and the frame now carries the round's wrap as written.

confirms: round-3#2
Phase 3 closes the finding. `tests/test_chain_check.py:3417-3431` is round 3's
draft, unchanged but for its docstring (read). The round dropped each of the
five answers of the no-root test at `chain_check.py:2192-2195` with
`bin/mutation-check`, and each mutant went red (executed). The smith's
claimed table in `phases/phase-3.md` matches the runs case for case:

- HEAD without the entry: `gone = False` in the CI arm.
  `Test_retired::test_accepts_every_declaration_leaving_with_the_root` failed.
- HEAD with the entry: `gone = git(...) is not None`. 33 cases failed, among
  them the three parameters of
  `Test_retired::test_refuses_a_declaration_deleted_with_nothing_absorbing_it`
  and `Test_retired::test_accepts_a_declaration_a_settle_removed`.
- git not answering: `gone = not git(...)`. The same acceptance case failed,
  in its monkeypatched half (`tests/test_chain_check.py:3409-3415`, read).
- Under `--worktree`, the working tree without the entry: `gone = False` in
  the `if WORKTREE:` arm. Only the new case failed,
  `Test_retired::test_accepts_under_worktree_a_root_the_working_tree_no_longer_has`.
  So it is the one case that reaches that answer, and this run shows it red.
- Under `--worktree`, the working tree with the entry: `gone = True`. Three
  cases failed, as the phase record names.

The round also dropped the `declarations and` guard, so that a pull request
with no declaration and no root would print the no-root notice. Three cases
of `Test_declared_for_this_branch` failed (executed). The new case is the
only one in `Test_retired` that runs `--worktree` on a tree with no `seal`
entry. `bin/test-layout --pairs tests/test_chain_check.py` printed 0 pairs
(executed), so the case covers an answer its group did not, and no duplicate
check names it.

confirms: round-3#3
The reframe closes the finding. The `add` at `spec.md:463-471` now says a
deleted declaration "is otherwise judged" (read). That is the word of the
section's paragraph *The check reads the diff as declarations*. With the
items applied, `docs/the-review-record.md` states the deletion rule as
"judged" in both paragraphs (executed, the replay printed the new lines).
The reframe corrected one more instance of the same class. `spec.md:155-159`
had said the check "refuses each deleted declaration HEAD does not carry".
It now says the check judged each one, "accepting one a settle retired and
refusing the rest". The *Places* row at `spec.md:227` adds "unless a settle
retired it" (read). Contract rule 12 is met for this class.

confirms: none
S8's applied half holds, run again by this round rather than taken from
`phases/phase-3.md`. In a scratch clone at `d0ba9fba`, `docs/` is unchanged
from `02ee12de` (`git diff --stat 02ee12de d0ba9fba -- docs` is empty,
executed). `rule_changes.py#parse` read 17 items with no error, and
`rule_changes.py#replay` applied them as one spec with nothing refused. Six
documents changed. The round chose the modules the frame names, those whose
source names `docs/`, `README.md`, `README.ko.md` or a changed document's
base name: 112 modules, the smith's count. Over the applied `docs/` they
gave 4433 passed and 14 skipped, exit 0. With `docs/` restored they gave
the same (both executed). The smith saw 1 failed and 4432 passed both ways.
Its one failure was the overview case, from a clone taken before
`overview.md` existed, and `d0ba9fba` carries that file.

The round widened the class by contract rule 12. It added the 43 modules
whose source names `"docs"` as a string or any `.md` path, which round 3's
selection and phase 3's could each have missed. Over the applied `docs/`
those gave 1185 passed and 2 skipped (executed). `bin/rules --check` over the
applied `docs/` read 253 check lines in 62 rule files, and all held. With
`docs/` restored it read 249 (both executed). The four new lines are the two
`check: tests/test_seal.py` lines and the two
`check: nothing-declared-nothing-owed` lines the items add.

confirms: none
S8's parse half holds. Run on the branch,
`python3 skills/code-review/scripts/chain_check.py --baseline release/v0.22.4`
exited 0 and named no `## Rule changes` problem (executed). It printed the
notices owed at this point: the pull request's state unknown with none
open, round 3's `target:` behind HEAD (this record answers that), and no
`broad-gate.md` or `guarantee.md` yet.

confirms: none
The phase 3 commits do what `plan.md` row 3 says and nothing more.
`41d87aba` touches only `tests/test_chain_check.py`, and `d0ba9fba` touches
only `overview.md`, `phases/phase-3.md` and `plan.md`'s Status cell. No file
under `skills/`, `tests/` or `docs/` changed between `2f41bbf9` and
`e3b321ad`. The framer's commit `eeccf30a` touches only `spec.md`, `plan.md`
and `questions.md`, and `spec.md` ends with its `Reframed` line. Each of the
five commits after round 3 carries
`SpecSeal-Routing: 1792976216-the-records-and-the-pr-checks-are-two-answers`,
with author and committer both the repository's identity (all executed,
`git show --stat` and `git diff --stat`). No changelog line changed, as
`plan.md` *Operational impact* says.

confirms: none
The narrow set exits 0 at `d0ba9fba`. `bin/test` over
`tests/test_chain_check.py`, `tests/e2e/teammate`,
`tests/test_unverified_check.py`, `tests/test_seal.py`,
`tests/test_mode_gate.py`, `tests/test_first_setup_asks_once.py`,
`tests/test_the_mode_is_a_row_and_a_command.py` and
`tests/test_chain_hooks_hardening.py` gave 1080 passed (executed). That
includes the overview case round 3 carried under `## Not judged`. Phase 3's
own line, `bin/test tests/test_chain_check.py tests/e2e/teammate
tests/test_unverified_check.py -q`, gave 604 passed, as it claims
(executed). `uvx ruff check` and `uvx ruff format --check` over the 11 Python
files the branch changes passed (executed). `bin/test-layout --check` over
the flow case and `tests/test_chain_check.py` refused nothing (executed).

confirms: none
`overview.md` agrees with the records (read). Its three divergences are the
ones `phases/phase-1.md` and `phases/phase-2.md` record. Each holds in the
code: the `command -v python3` skip at
`tests/e2e/teammate/test_teammate_flow.py:207-213`, the switch to shared
printing only where `workflow_at` answers `absent`, and the one-path
refusal sentence. Its `## Not verified` rows are the ones the rounds carry:
the Windows legs, the broad gate and the merge-order settle. Its
`## Not done` matches `spec.md` *Out* and `questions.md` Q4's default. One
claim reads loosely. The second divergence quotes `spec.md` *In* item 4 and
then calls the spec silent on a file another party wrote. "Such file" there
can be read as the plugin's file, and then the spec would ask for the line.
The divergence is disclosed with its grounds, and naming
`seal pr-checks install` there would send a person to a refusal
(`seal.py#install_workflow`). So it is no finding.

confirms: none
The branch as a whole, `02ee12de..d0ba9fba`, was read again for what rounds
2 and 3, which read fix diffs, did not reach. That covers `seal.py`'s
`workflow_at`, `left_workflow_line`, `install_workflow`, `remove_workflow`,
`pr_checks`, `refusals`, `switch` and the parser, `unverified_check.py`'s
`absent_root` and `unwritten_root`, `templates/hygiene.yml`,
`hooks/mode-gate.py`, `skills/implement/orchestration.md`,
`skills/config/SKILL.md`, `CONTRIBUTING.md`, both READMEs and
`templates/seal-README.md` (read). A search outside `docs/`, `changelog/`,
`CHANGELOG.md` and `seal/specs/` for `workflows/hygiene`, `install_workflow`
and `red forever` finds only the coordinates `spec.md` *Places* keeps and
this repository's own workflow (executed, `git grep`). `.test_durations`
still names the retired cases. It is a timing file the runner writes, and
nothing reads a name from it as a case.

Two readings were weighed and are not findings. First,
`seal.py#left_workflow_line` says a workflow pinned to this release examines
nothing and passes after a switch to local. The chain step still judges a
`SpecSeal-Routing` trailer naming a work item (`chain_check.py#main`). A
commit made in shared mode on the same branch as the switch would then fail
it. `spec.md` *In* items 4 and 6 choose exactly this: the line's wording, and
the trailers judged as for any pull request that declares nothing. The
template's step comment says the same. In local mode a session's commit
carries no trailer (`skills/commit-pr-convention/SKILL.md:138-143`, read).
Second, `ce6b9afe` spliced a sentence into `templates/seal-README.md` and
`seal/README.md` without re-wrapping it, leaving line 32 of each at 107
columns. `tests/test_docs_line_wrap.py` `COVERED` lists neither file, and the
text reads correctly (read).

Facts carried from earlier rounds rather than re-established: where the
no-root test lives (`chain_check.py#main`), the replay method of round 3's
`## Probes`, `questions.md` Q2, and the merge-order hold behind other specs.
The hold was not replayed again. Every verdict above was reached this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the flow cases run or skip on the Windows legs of `.github/workflows/test.yml` (`questions.md` Q2). Carried from round 3 and not re-run | `tests/e2e/teammate/test_teammate_flow.py` | the pull request's CI run on `windows-latest`, read by the orchestrator |
| The settle holds this spec behind specs refused for reasons outside this branch. Carried from round 2; the merge-order replay was not run again. This round replayed this spec alone, as S8 asks | `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:292` | the orchestrator, at the settle that applies this release's specs |
| `questions.md` Q1 and Q4 stay open for the owner, built on their defaults (a) | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/questions.md` | the owner, relayed by the orchestrator in the pull request body |
| The full suite, the repository-wide lint and the typecheck: not run, as contract rule 2 gives them to the broad gate after the rounds settle; the smith's suite stays `unverified`. This round leaves nothing open, so the orchestrator's broad run comes due next, then the sealer's spawn | the branch | the orchestrator, by `broad-gate` |

## Probes

| Command | Result |
|---|---|
| `bin/mutation-check skills/code-review/scripts/chain_check.py --replace <line> <mutant> --tests "bin/test tests/test_chain_check.py -q -p no:randomly"`, once for each of the five answers, in a scratch clone at `d0ba9fba` | all five red; the failing cases are as `## Confirmations` names, and the tool restored the file after each |
| the same with `"    if declarations and gone:"` replaced by `"    if gone:"`, over `tests/test_chain_check.py` and `tests/e2e/teammate` | red: 3 cases of `Test_declared_for_this_branch` failed |
| `bin/test-layout --pairs tests/test_chain_check.py` | 0 pairs |
| `python3 -I test_tmp_round4_replay.py <clone> --write`, in a second scratch clone at `d0ba9fba`: parse the 17 items, replay them with `rule_changes.py#replay` onto `docs/`, print the new lines with their widths, and list the modules whose source names `docs/`, a README or a changed document's base name | 17 parsed, 1 spec applied, nothing refused; six documents changed; 112 modules |
| `bin/test` over the 112 modules with the items applied, then with `git checkout HEAD -- docs` | 4433 passed, 14 skipped, exit 0; then the same |
| `bin/test` over the 43 further modules naming `"docs"` or a `.md` path, with the items applied | 1185 passed, 2 skipped, exit 0 |
| `bin/rules --check` with the items applied, then restored | 253 check lines in 62 rule files hold; then 249 |
| `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.22.4` on the branch | exit 0, no `## Rule changes` problem |
| `bin/test` over the eight modules of the narrow set; phase 3's three-module line | 1080 passed; 604 passed |
| `uvx ruff check` and `uvx ruff format --check` over the 11 changed Python files | all checks passed; 11 files already formatted |

Each applied `docs/` was restored with `git checkout HEAD -- docs` after its
run, and `bin/mutation-check` restored `chain_check.py` and compared its hash
after each mutant. The probe file and both scratch clones were removed
before the hand-back.
