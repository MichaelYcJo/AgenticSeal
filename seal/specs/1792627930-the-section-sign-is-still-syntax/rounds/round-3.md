# Review round 3: 1792627930-the-section-sign-is-still-syntax

target: 14e4b411, fixes ea3141ed..14e4b411

This verifying round read the fix diff ea3141ed..14e4b411, in a
`git clone --no-local` of the branch at 14e4b411. The diff holds 7eb63541,
the smith's fix pass, and 14e4b411, the framer's `## Rule changes` item. As
the coordinator asked, the round also sampled phase 4 rows that neither
earlier round read. From round 2 it carried coordinates only: the three
locations of its finding, and the base templates at 0d62145a. Every verdict
below was reached again in this round. This round opens no finding.

## Findings

## Confirmations

confirms: round-2#1
The finding's close holds in each of its five locations, for these reasons.
`agents/framer.md:129-130` now names the three values of
`skills/implement/SKILL.md` *3. The SDD file set*, in the record's words.
`skills/writing-style/SKILL.md:169-170` now opens
`skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot
show*.
The citation reader reads both new citations. Renaming the cited heading in
either file turned
`tests/test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists`
red, exit 0 (executed, `bin/mutation-check`).
The `docs/the-review-and-parity-arms.md` sentence is changed by the
framer's new `change` item in `spec.md` `## Rule changes`.
`rule_changes.parse` on the spec at 14e4b411 returns no error and six
operations, four `change` and two `add`. `apply_op` places all six against
the docs at 14e4b411. The changed sentence names `no work item` in
`skills/implement/orchestration.md` *Question 1* (executed).
The two `seal/follow-up.md` rows the smith's sweep added hold. The Status
rule they cite stands in `skills/implement/SKILL.md` *3. The SDD file set*.
`offered` reads the third axis's placeholder: `offered` of the routing
template's `Implementation` row returns `smith` and `the session`
(executed).
The framer's preload is 25239 bytes, against 25255 at the base, and the
other four agents are unchanged below their bases (executed,
`noninferiority.preload_bytes`).

confirms: none
The fix pass introduced no defect in the lines it changed. The fifteen
modules that read `agents/framer.md`, `skills/writing-style/SKILL.md`,
`seal/follow-up.md` or the spec's `## Rule changes` passed: 1120 passed
(executed). These include the wrap, pasted-passage and section-sign
modules. `spec.md` S8 now counts four `change` and two `add`, which matches
the replay above. The new `## Removes` row names the sentence and where it
lands.

confirms: none
This round read nine more rows of the phase 4 table at
`seal/specs/1792627930-the-section-sign-is-still-syntax/phases/phase-4.md:33-81`.
Each was read against the base template at 0d62145a and the home the row
names, and each holds there (read).
1. spec, "the framer cites them and does not restate them": at
   `docs/the-record-layout.md:9`.
2. plan, "holds HOW in phases, the Design Gate's artifact": at
   `skills/implement/SKILL.md:359`.
3. plan, "the approval line, its writer, moment and shape": at
   `skills/implement/orchestration.md:33-50` *The plan is approved at the
   spawn*.
4. routing, "`Planning` is recorded, not asked": at
   `skills/implement/orchestration.md:401`.
5. overview, an open item worded to begin with `closed`: at
   `skills/implement/SKILL.md:464`.
6. phase, "what the record holds and who writes it": in the
   `phases/phase-N.md` row at `skills/implement/SKILL.md:362`. The
   template's `Commit` placeholder still names the hash that `plan.md`'s
   Status cell carries.
7. phase, "a removal is not recorded in a phase record": in the same row,
   "never what the work removes".
8. round, "the `target:` line and the extension line": at
   `docs/the-review-record.md:44` and `:487` *The run*.
9. round, "the `original:` line": at `agents/warden.md:38-42` and
   `skills/legacy-parity/SKILL.md:113`. The two together carry the
   condition (outside `docs/` and `seal/`), the baseline commit, and the
   unresolved case.

## Not judged

| What | Location | Who answers |
|---|---|---|
| CI run 39714074783 at 14e4b411, not yet read | the run's logs | the coordinator |
| The full suite, the repository-wide lint and the typecheck at 14e4b411 | the whole tree | the orchestrator, through `broad-gate` now that the rounds have settled |
| About a dozen rows of the phase 4 table that no round sampled; three rounds together read about 30 of 46 | `seal/specs/1792627930-the-section-sign-is-still-syntax/phases/phase-4.md:33-81` | the sealer, if its sample reaches them |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the fifteen modules that read the changed files | 1120 passed |
| `bin/mutation-check agents/framer.md`, renaming the cited heading, over the implement citation case | red, exit 0 |
| `bin/mutation-check skills/writing-style/SKILL.md`, renaming the cited heading, over the same case | red, exit 0 |
| `rule_changes.parse` and `apply_op` on `spec.md` at 14e4b411 | no error; four `change` and two `add`, all placed |
| `noninferiority.preload_bytes` for the five agents, at 0d62145a and at 14e4b411 | framer 25255 to 25239, smith 24746 to 24668, warden 25370 to 25300, sealer 23383 to 23302, scribe 18545 to 18486 |
| `offered` on the routing template's `Implementation` row | `smith`, `the session` |
