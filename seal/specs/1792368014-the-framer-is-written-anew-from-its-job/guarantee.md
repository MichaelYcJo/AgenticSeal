# 1792368014-the-framer-is-written-anew-from-its-job — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | 13945de4 against 2ff7b963 |
| Broad gate | 113ae699 against 2ff7b963 |

## Claims re-run

<!-- One row per act of `agents/sealer.md` step 3, whatever the act, and one
per thing the act checks. `Result` reads `holds`, or `does not hold — <what
came back>`, and a `does not hold` is what the verdict names. -->

This run audits 13945de4. The base `release/v0.22.2` resolves through
`release/v0.22.2@{upstream}` to 2ff7b963, which is also the merge base of
HEAD, so `git diff 2ff7b963...HEAD` is the branch's own change with both
merges (461f00c6, ae3f6ccf) folded out. "At base" means a
`git clone --no-local` of the branch at 13945de4 under the sealer's
scratchpad, with `agents/framer.md` (or the file a row names) checked out
from the named commit and every test at HEAD, run with the worktree's
`.venv` interpreter. The clone was removed after. The tree under audit was
only read. The rounds were judged with the tree's `chain_check.py`, as
#985's grammar requires.

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at HEAD, or only this item's records follow it | `broad-gate.md:5` | `git rev-parse --verify --quiet 113ae699`; `git merge-base --is-ancestor 113ae699 HEAD`; `git log --no-merges --name-only 113ae699..HEAD ^2ff7b963` | holds — 113ae699 resolves and is an ancestor; one commit follows, 13945de4, touching `broad-gate.md` and `overview.md` in this directory |
| The item's records pass the tree's check | `rounds/round-1.md` to `round-3.md` | `python3 skills/code-review/scripts/chain_check.py --baseline 2ff7b963 --root <worktree>` | holds — exit 0; its one line names the absent `guarantee.md`, this file |
| The shape case and the replace-or-keep case are red on the old file | `phases/phase-1.md:112-116` | at base: `test_every_definition_has_the_shape_and_preloads_the_contract_alone[agents/framer.md]`, `test_the_framer_weighs_replacing_a_structure_as_an_equal_of_keeping_it` | holds — both exit 1 with `agents/framer.md` at 2ff7b963; both pass at HEAD |
| Round 1's three pins are red on the definition before the fix | `rounds/round-1.md:78`, `:138`, `:186`; `phases/phase-4.md:83-84` | with `agents/framer.md` at 1bdbb586: `test_the_framer_inherits_what_the_tree_already_settled`, `test_a_reframe_keeps_every_closed_phase`, `test_the_hand_back_labels_what_the_framer_ran_as_executed` | holds — all three exit 1; all three pass at HEAD. At 2ff7b963 the reframe pin passes, because the old file carried *every closed phase keeping its commit* (`:303-305`): the rewrite dropped it, and 1bdbb586 is where it was missing |
| 6fe805e1's case refuses the wrapped 0.4.0 sentence, and the old case did not | `phases/phase-1.md:231-239` | in the clone at HEAD, *creates the root at `<repo>/seal/` and nowhere⏎else* appended to `skills/implement/orchestration.md`, then `test_the_sentence_that_said_nowhere_else_is_gone` with the case at HEAD and at 6fe805e1^ | holds — exit 1 at HEAD, exit 0 with the old case; green on the tree |
| The preload is 26,604 bytes at HEAD, and the measured definition is b434e145's | `phases/phase-4.md:86-89`, `changelog.md:39-41`, `overview.md:13` | `wc -c agents/framer.md skills/agent-contract/SKILL.md`; `bin/payload-meter --agent framer`; `git show <rev>:agents/framer.md \| shasum -a 256` at b434e145 and HEAD | holds — 10,001 + 16,603 = 26,604; b434e145 hashes `f70b2eb37f0e`, the side's `New preload` row and `meta.json`; HEAD hashes `7e8136336a6c`, the fix |
| Nothing else of the read set moved after the measured commit | `phases/phase-4.md:27-49`, `:92` | `git diff --stat b434e145 HEAD -- skills templates docs agents`; `git merge-base --is-ancestor ae3f6ccf b434e145` | holds — `agents/framer.md` alone (the fix); b434e145 descends from ae3f6ccf, so the side ran after #976 and #985 merged, as Q2's answer asks |
| The baseline stands under guard 1 and is #967's side byte for byte | `spec.md:76-81`, `changelog.md:30-32` | `git show 43cbc361:<path> \| shasum -a 256` for the four old preload files against `baseline-framer.json`'s `specseal.preload`; `cmp` with `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/framer-phase-4.json` | holds — four hashes equal; `cmp` exit 0 |
| `evals/framer-phase-2.md` reads `pass` and its figures check | `phases/phase-2.md:39-43` | `python3 evals/scripts/noninferiority.py check evals/framer-phase-2.md` | holds — exit 0 |
| Phase 2's per-run table and its skill opens | `phases/phase-2.md:81-122`, `changelog.md:16-18`, the pull request body line 21 | a scratch script (deleted) over `968-framer-raw/traces/*.jsonl`, read-only with `python3 -I`: distinct assistant `message.id` under a `parent_tool_use_id`, its input + cache tokens, `tool_use` ids, and every call naming either `SKILL.md` | holds — the eight rows' requests, tool calls and framer tokens equal the record's (57, 164, 2,129,160 in all); every open of either skill is a ranged `Read`, a `sed -n` range or a heading `grep`; no run read either file whole |
| `## Removes` rows 1 to 9 and the changelog's *incident histories and release readings are gone* | `spec.md:227-235`, `changelog.md:15` | `git grep -n -F` outside `seal/specs`, `changelog`, `.test_durations` for *Do not promise a saving*, *promises no saving*, *The middle act is the one*, *Every framer that read*, *its bar is the framing row*, *A row also says*, *You have no interactive phase*, *When you run*, *How a frame opens*, *not the builder*, *The frame is a drawing*, `sequenceDiagram`; `grep -n '^## \|```' agents/framer.md`; the frontmatter's `skills:` | holds — no hit; the file has `## Job`, `## Order of work`, `## Never`, `## Rules`, no code block, and `skills:` is `agent-contract` alone |
| `## Removes` rows 10 and 11: the exemption and the narration pins | `spec.md:236-237` | the same search for `NOT_YET_REWRITTEN`, *#968 to #970*, `points_at_its_bar`, *framers of 0.12.1*, *0.12.2 framers*, `framer_opening` | holds — no hit |
| `## Removes` row 12: the paste allowances | `spec.md:238` | `grep -n framer tests/test_no_passage_is_pasted_into_a_second_file.py`; `git diff 2ff7b963...HEAD` of the file | holds — the three debt entries are gone and the four kept read 4, 14, 24, 31 |
| `## Removes` row 13: the READMEs' framer preload | `spec.md:239` | `sed -n 30,50p README.md README.ko.md` | holds — `Follows` reads `agent-contract` in both; the skills row counts one, fifteen and six |
| The emoji and the proof block are gone (#968's body) | the issue body, *The change*, bullet 2 | a scan of `agents/framer.md` for characters at U+2190 and above outside Hangul, and for `applied` or `proof` | holds — none |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `agents/framer.md` rewritten to the four sections with `skills: [agent-contract]`, `implement` opened by three sections and `writing-style` by one; the pins sorted; one side against #967's; `implement`, `writing-style` and the contract left alone | the issue body; the diff, which leaves `skills/implement/SKILL.md`, `skills/writing-style/SKILL.md` and the contract untouched; the build | none. `skills/implement/orchestration.md` is edited, which the spec's *Out* does not name, and `overview.md`'s third divergence row records it (read) |
| the build | phases 1, 2 and 4 as above; phase 3 not run because phase 2 passed; round 1's fix not measured again, by the orchestrator's decision under the owner's word | the tree on every claim re-run above; Q1 and Q2 as answered | none that the verdict rests on. Two sentences of `overview.md` are loose: its fourth divergence row says the side ran *after the first merge*, where the tree shows b434e145 descends from the second (ae3f6ccf) as well; and its suite row cites `broad-gate.md` for *7604 passed, 12 skipped*, which that file does not hold (it names the run's commit only), so those counts are the orchestrator's (unverified here) |
| the last round | round 3 at a277188d confirms round 2's finding closed and opens nothing; round 1 recorded that *where a heading is not found, it reads the file whole* is true of `implement` and not of `writing-style`, and judged the difference harmless (`rounds/round-1.md:215-217`) | the tree's check, exit 0; the tree at each confirmed coordinate | none |
| the changelog | the framer's rewrite, the README row, and the row 86,353 → 26,027, 29,894.6 → 17,190.9, 16.1196 → 14.7490, 64 → 64 of 64, `pass`, with the shipped 26,604 bytes not measured again | `evals/framer-phase-2.md`, the side files, the traces, the tree's sizes | `changelog.md:12`: *Where a heading is not found, it reads the file whole*, stated after both skills' lines. `agents/framer.md:46-49` (step 3) gives `implement` that fallback; `:69-71` (step 6) gives `writing-style` none |
| the pull request body | the same change and figures, four new pins each seen failing against the definition before it, the nowhere-else check fixed, three rounds in the new grammar, no gate's decision changed | each claim re-run above; `hooks/`, `bin/`, `.github/` and the check scripts are untouched by the diff, so *No gate's decision changes* holds (`CONTRIBUTING.md` §*What a change to a gate must carry*); line 5's *the last agent still preloading whole skills* holds at 2ff7b963, where only the framer listed more than `agent-contract` | line 9, the same sentence as `changelog.md:12`, contradicted by `agents/framer.md:69-71`. Line 23 says the tree was not measured again *by the owner's word*; the records say the orchestrator decided it under that word (`phases/phase-4.md:89-90`, `overview.md:29`), a difference of whose act and not a contradiction of the tree |

<!-- One line: `sealed`, `withheld — <the claim, its party, its coordinate>`
or `undecided — <the question, for the owner>`. An owner's answer is a line
under it, `Answered <date> by <who>: <answer>`, which the next run keeps. -->

Verdict: withheld — the changelog (`changelog.md:12`) and the pull request body (line 9) say that where a heading is not found the framer reads the file whole, after naming both skills it opens; the tree gives that fallback to `implement` alone (`agents/framer.md:46-49`), and step 6 (`agents/framer.md:69-71`) gives `writing-style` none, so the sentence is untrue of `writing-style` and is owed the scope it has (for example *Where one of `implement`'s headings is not found, it reads that file whole*)
