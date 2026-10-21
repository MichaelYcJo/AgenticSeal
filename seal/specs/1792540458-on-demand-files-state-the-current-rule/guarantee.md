# Guarantee: 1792540458-on-demand-files-state-the-current-rule

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md is written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` *The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | 8e4d1a6492ddf54cc2b65dfb7c04dc02f3d9f271 against b3154f436405182f5a1d486f55b9c879c8d383fd |
| Broad gate | f1c0e1a7 against b3154f43 |

The base `release/v0.22.3` resolves to b3154f43 through `@{upstream}`, and
`origin/release/v0.22.3` and the local name give the same commit (executed).
This audit follows `agents/sealer.md` and `templates/sdd-guarantee.md` as
they stand at HEAD, as the spawn prompt directs, because the loaded plugin
copy (0.22.2) writes the older verdict shape. The pull request body audited
is the file the prompt names, as it stood at this audit: its CI row already
names 0f7fb366.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Step 1: the broad run is at HEAD, or only the item's records follow it (`executed`) | `broad-gate.md:5` | `git rev-parse --verify --quiet f1c0e1a7`; `git merge-base --is-ancestor f1c0e1a7 HEAD` exit 0; `git log --no-merges --name-only f1c0e1a7..HEAD ^b3154f43` | holds: one commit, 8e4d1a64, touching only `seal/specs/<item>/broad-gate.md` and `seal/specs/<item>/overview.md` |
| The four `tests` runs at 4ce4daf0, ac92a9e6, 623c771e and 0f7fb366 passed on every leg (`executed`) | pull request body line 37; the prompt | `gh run view <id> --json headSha,conclusion,jobs` for 39531314997, 39533477920, 39534663738, 39535133679 | holds: each `completed success` at the SHA named, 13 jobs, every `pytest`, `lint`, `arm-check-grammar` and `durations` job `success`; `release-report` is skipped, and it runs only for a base of `main` (`.github/workflows/test.yml:253`) |
| The broad run: ruff clean, 7393 passed, 13 skipped, chain exit 0 (`read`) | pull request body line 38; `overview.md` *Not verified* | read the orchestrator's `broad-gate.log` beside the body | holds as read: `BROAD GATE PASSED … @ f1c0e1a7 against … @ b3154f43`, the row `uvx ruff check . && uvx ruff format --check . && bin/test -q`, `7393 passed · 13 skipped`, `chain ✓ exit 0`. Not re-run, by `agents/sealer.md` *Never* |
| S13 byte sums per agent at b3154f43 and 493d9816 (`executed`) | `phases/phase-9.md:419-427`; body lines 27 and 35 | `git cat-file -s <rev>:<path>` summed over each set `spec.md` *Data and interfaces* lists, by a scratch script, deleted | holds: framer 110,562 to 112,603; smith 146,526 to 117,039; warden 76,287 to 78,706; sealer 55,861 to 23,597; orchestrator 105,113 to 100,664, and with both `verify` files 159,334 to 151,600. At HEAD the framer's set is 112,835 and the orchestrator's with both files 151,947; the body dates its figures to phase 9's commit, so this is no disagreement |
| Block 1,669 bytes, `CLAUDE.md` 3,066 from 8,524, `skills/verify/SKILL.md` 21,960 from 54,221 (`executed`) | body lines 8 to 10 | `git cat-file -s` at b3154f43, 493d9816 and HEAD | holds at HEAD: 4,695 to 1,669; 8,524 to 3,066; 54,221 to 21,960. No record states 3,066; phases 3 and 9 state 3,049, the size before bd1aa449 rewrote `CLAUDE.md`'s writing rule. `phases/phase-5.md:323` says 54,220 at b3154f43; the tree says 54,221, which the body uses |
| `CLAUDE.md`'s sections are the goal, the tenet, merge method, identifiers and the writing rule (`executed`) | body line 9; `spec.md` Scope 3 | `grep -n '^#' CLAUDE.md` | holds: five `##` headings, those five |
| Phase 6's new pin `test_branch_names_state_the_issue_number_rule_once` was seen red (`executed`) | `phases/phase-6.md:422` | in an at-base `git clone --no-local` at HEAD, `skills/commit-pr-convention/SKILL.md` restored from b3154f43, then `bin/test -p no:xdist -q <case>` | holds: green at HEAD, exit 0; against the base file exit 1, "*Branch names* does not state 'A branch cut from an issue is `<prefix>/<issue number>-<slug>`.'" |
| Round 2's new pin `test_the_preset_writes_no_declaration_under_no_work_item` was seen red with its clause deleted (`executed`) | `rounds/round-2.md:74` | the same clone: the template restored from b3154f43 and the case run; then "Except under `no work item`, " removed from the HEAD template by a script that asserts one match, and the case run | holds: against the base file exit 1, but on the case's paragraph finder, since the base bullet opens differently; with the clause deleted exit 1, "the routing rule writes routing.md under every answer, `no work item` included" |
| Phase 3's new pin `test_this_repository_carries_no_copy_of_the_block` was seen red (`executed`) | `phases/phase-3.md:356` | the same clone, `CLAUDE.md` restored from b3154f43 | holds: exit 1, "CLAUDE.md carries the block's markers again" |
| Phase 5's pin on the flow log's close comment was seen red (`executed`) | `phases/phase-5.md:160-166` | the same clone, `.github/scripts/roll_flow_measurement_issue.py` restored from b3154f43 | holds: exit 1, "the comment sends its reader to a file the section left" |
| Phase 2's new pin `test_the_orchestrator_states_the_approval_line_where_it_spawns_the_build` was seen red (`executed`) | `phases/phase-2.md:201-206` | the same clone, `skills/implement/orchestration.md` restored from b3154f43 | holds: exit 1, "the spawn step no longer states the approval line" |
| Phase 9's lowered `BASELINE` holds, and a lowered entry is tight (`executed`) | `phases/phase-9.md:362-393` | the same clone at HEAD: `bin/test -q tests/test_no_passage_is_pasted_into_a_second_file.py`; then `("agents/scribe.md", "agents/sealer.md")` lowered from 5 to 4 by a script that asserts one match, and the module run | holds: 8 passed, exit 0; with the entry one below its count exit 1, "share 5 runs of 15 words where 4 were measured". The clone was removed after the runs |
| S16: `bin/rules --check` exits 0 (`executed`) | `spec.md` S16; `rounds/round-1.md:329` | `bin/rules --check` in the clone at HEAD | holds: exit 0, "all 244 check lines in 62 rule files hold" |
| S8: the section sign stands only in contract-number citations (`executed`) | `phases/phase-9.md:323-335` | `git grep -n '§' -- 'skills/*.md' 'templates/*.md' CLAUDE.md CONTRIBUTING.md ':!skills/agent-contract'` | holds: 13 lines, the ones phase 9 lists at shifted line numbers (`code-review/orchestration.md:308`, `implement/orchestration.md:428,498,502,575`); no `§*heading*` citation |
| Issue numbers left the rewritten files (`executed`) | `spec.md` Scope 7 | `grep -c '#[0-9]\{2,\}'` at b3154f43 and HEAD | holds: `verify/SKILL.md` 22 to 0, `implement/orchestration.md` 18 to 0, `CONTRIBUTING.md` 11 to 0, `code-review/orchestration.md` 8 to 0, `templates/config.md` 7 to 0; `verify/orchestration.md` keeps #300, #377 and #642, which `phases/phase-5.md:213-219` keeps on its grounds |
| `## Removes`: the generated block, its generator and its CI step (`executed`) | `spec.md` *Removes* rows 1 and 2 | `git grep -n 'specseal:start' -- CLAUDE.md`; `git grep -n claude_block -- ':!seal' ':!changelog' ':!CHANGELOG.md'`; `ls .github/scripts/claude_block.py`; `grep` over `hygiene.yml` | holds: no line, no file, no step |
| `## Removes`: the copy's cases and `GENERATED` (`executed`) | *Removes* row 3 | `ls tests/test_the_claude_md_block_has_one_source.py`; `grep -n GENERATED tests/test_no_passage_is_pasted_into_a_second_file.py` | holds: the module is gone, no `GENERATED` |
| `## Removes`: the three `CLAUDE.md` rows (`executed`) | *Removes* rows 5 and 6 | `grep -n '^#' CLAUDE.md`; `grep -n 'commit early\|writes fragments\|named with whose' CLAUDE.md` | holds: no row heading; "named with whose" stands once inside the writing rule, where Scope 1 folds it |
| `## Removes`: verify's two orchestrator sections (`executed`) | *Removes* row 7 | `grep -n '^## '` over both `skills/verify/` files | holds: `SKILL.md` holds neither; `orchestration.md` holds *The broad gate* and *Measure the segment, and feed the flow log* |
| `## Removes`: the restated branch shape and `perf/403` (`executed`) | *Removes* row 8; Scope 5 | `grep -n 'Branch names stay ASCII\|perf/403'` and `sed -n 60,100p skills/commit-pr-convention/SKILL.md` | holds: the bullet keeps its reason and links *Branch names*, with no shape; no `perf/403` |
| `## Removes`: the arrow heading (`executed`) | *Removes* row 9 | `grep -n '^## Open questions' templates/sdd-spec.md` | holds: `## Open questions` |
| `## Rule changes`: each `from:` line stands in its `docs/` file (`executed`) | `spec.md` *Rule changes* | `git grep -c -F` of each `from:` fragment over `docs/` | holds: one hit in each of the four files named |
| The owner decided to keep the framer's and warden's sets over S13, on 2026-10-21 (`unverified`) | body line 27, *By* column | none: no record holds the decision; `overview.md` says "shipped over, and reported" and names no one who chose | not contradicted; the owner answers it, and the spawn prompt's account that the orchestrator put it to the owner is a claim |
| The rewritten files leave each agent no worse at its cases (`unverified`) | `questions.md` Q1; `overview.md` *Not verified* | none: the paid non-inferiority run, not made under Q1's default | not claimed by any party; the repository owner answers it |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | Scopes 1 to 11, Scope 9 amended to drain before `broad-gate --preflight`, S1 at 1,669 bytes, four `## Rule changes` items, the `## Removes` table | the issue body's five owner decisions; the tree at HEAD on every `Removes` row re-run; the build, through the divergences `overview.md` records | none |
| the build | nine phases at the commits `plan.md` names; S13 holds for the smith, the sealer and the orchestrator and fails for the framer and the warden; nine divergences in `overview.md` | the tree on every figure and red re-run above; the spec through those divergences | none on the tree. Two record slips that mislead nobody: `phases/phase-5.md:323` gives 54,220 for 54,221, and `phases/phase-9.md:307-321` gives section 6's heading and moment as phase 9 built them, which round 1's fix replaced and `overview.md` records |
| the last round | round 4 confirms round 3's two fixes and opens nothing; rounds 1 to 3 hold nine, two and two findings, each `fixed` at a named commit | the tree: section 6, the seal README and the questions template read as the rounds confirm; `bin/rules --check` exit 0 | none |
| the changelog | three writing rules; the block at 1,669 bytes with its routing rule and scoped lint rule; one copy; both orchestration halves; the `verify` split at about two fifths of its size; the branch rule; the templates; `CONTRIBUTING.md`; the drain before the broad run | the tree, the spec and the build | none |
| the pull request body | the changes above, the decisions table, the verification table, the gate change and what is left open | the tree, the records and the CI runs on every claim re-run but three | three sentences, quoted with their coordinates below |

**1. The verification table's pins row says more than the records hold.**
The body says, line 36: "| New and rewritten pins | each phase record
lists its cases; each was shown red by `mutation-check` against the new
text |". Two records disagree:

- `phases/phase-9.md:391-393`, on the `BASELINE` entries phase 9 lowered:
  "Two of the entries, one of each kind, were seen red one below their count
  (`mutation-check`, executed); the others were not mutated one by one."
- `phases/phase-3.md:357`, on its new case
  `#test_the_runtime_readers_name_the_template_path`: "red against the tree
  before the two skills were edited", a red against the old text, not
  `mutation-check` against the new.

The cases round 2's fix pass added are listed in `rounds/round-2.md:74` and
`:135`, not in a phase record. A row the records bear out reads: "each phase
record, and round 2's fix-pass answers, list the cases; each new or
rewritten case was seen red, by `mutation-check` on the new text or against
the old, except phase 9's lowered `BASELINE` entries, of which two were
mutated one below their count (`phases/phase-9.md`)".

**2. The body says `CLAUDE.md` names the writing section in one line.**
The body says, line 7: "`CLAUDE.md` names the section in one line." The tree
contradicts it: `CLAUDE.md:44-54` is a section of its own, *Repo rule: text
an agent or a check reads has one reading*, nine lines that state the two
directions in compact form (no symbol as syntax, no value twice, no spelling
a near miss passes; an instruction names who acts, when, on which file and
what counts as done; one meaning per term; whose) and then name the section.
That is what `spec.md` Scope 1 asks ("one compact rule naming both
directions and linking the section"). A sentence the tree bears out: "`CLAUDE.md`
states the two directions in one short section and names that section."

**3. The failure direction says nothing else changes a gate.** The body
says, line 43: "Every other change is text an agent reads." The tree and
`phases/phase-9.md:389-391` contradict it: phase 9 lowered ten
`tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` entries to
their measured counts ("a lower entry only makes the ratchet stricter"),
for example `("agents/smith.md", "agents/warden.md")` from 153 to 18, so that
check now blocks more on the pull request. The body names the entries
removed at zero under *What it removes* and not this direction.
`CONTRIBUTING.md` *What a change to a gate must carry* asks the body to say
whether the change makes the gate block more or allow more. A sentence the
tree bears out: "The restatement check blocks more: its `BASELINE` entries
are lowered to their measured counts, so a restatement that grows back
fails the pull request. Every other change is text an agent reads, and the
pins that hold it."

None of the three is a defect in the code or a record. Each is a body
sentence, and the orchestrator's fix is to those three sentences of the body
file and nothing else. No commit to the tree follows from them.

Verdict: withheld reason: the pull request body states three things the records and the tree contradict: line 36 "each was shown red by `mutation-check` against the new text" against `phases/phase-9.md:391-393` and `phases/phase-3.md:357`; line 7 "`CLAUDE.md` names the section in one line" against `CLAUDE.md:44-54`; line 43 "Every other change is text an agent reads" against `phases/phase-9.md:389-391` and `tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE`
