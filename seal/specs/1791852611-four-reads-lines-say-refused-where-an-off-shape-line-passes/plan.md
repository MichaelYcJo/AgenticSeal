# Implementation Plan: four `Reads:` lines say refused where an off-shape `## Removes` line passes (#905)

<!-- seal/specs/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved <date> by <who>, when `smith` was spawned.

## Summary

Make the four `refused` words true instead of changing them: a line under
`## Removes` that is neither a table row nor a `nothing — <why>` line is
`REFUSED` naming it, pinned by a case seen red. Reword the two sentences
#834's round 6 found stale (limit 5's reader, the recorder's *strict side*)
and tell the warden what limit 5 now says it does. Write the records last, so
the frame's own `## Removes` rows read as gone the moment the work item
becomes live.

## Technical context

- `skills/evidence-check/scripts/evidence_check.py#removes_section` (:6032 at
  39a315a5) walks `claim_lines` of a frame, keeps the section's table body
  rows and its `nothing` lines, and adds every line number to `cut`. A line
  that `cell_rule()` does not split and that `REMOVES_NOTHING_RE` does not
  match is dropped: no list, no finding. `#removal_findings` (:6066) refuses
  the section only under `required and not (rows or nothing)`; `#file_claims`
  (:6230) calls it for a `spec.md` with `removes` not None and skips the cut
  lines in the name half; `#check_records` (:6323) computes `removes` from
  `Removes from` and the item's epoch.
- `claim_lines` (:5580) hands back `(number, text)` with fences and HTML
  comments taken out, blank lines included as empty text. So the refusal's
  rule is on the stripped text: empty passes; a row passes to the row rules;
  a line beginning `nothing` passes to the reason rule; anything else is
  refused. A `NAME NOT IN TREE` marker exempts a name, not a shape, so a
  prose line carrying it is still refused — it should be a row.
- The quoted-line anchor (`text_regions`, :599) matches a whole line with
  whitespace collapsed, so this frame's three `## Removes` rows quote whole
  lines as they stand at 39a315a5 and read as gone once each clause is
  reworded, however it is reworded.
- `tests/test_a_record_states_what_the_tree_has.py` from line 1548 holds the
  section's cases: `REMOVES_HEAD`, `REMOVES_TAIL`, `frame(tmp_path, rows)`,
  `removes_config`, `refusals`, `work_item`. `test_presence_is_required_at_or_above_the_cutoff`
  pins today's empty-section words, which stay.
- `tests/test_a_folded_statement_names_what_enforces_it.py` and
  `skills/settle/scripts/fold_check.py` read every `Enforced by:` target in
  `docs/`, so the new node id goes in after the case exists.
- `seal/config.md`: `Ledger frozen from 1790993141`, `Removes from
  1791780031`. This item (1791852611) is bound: its `spec.md` carries the
  section. Its work item is live for the records arm only once
  `seal/ledger/1791852611-….md` exists (`unshipped`, :5334;
  `test_a_work_item_with_no_fragment_is_counted_as_unread`), which is why the
  fragment is the last phase's write.
- The warden is told nothing about `Reads:` lines today (`grep -n 'Reads:'
  agents/warden.md skills/code-review/*.md` is empty, 2026-10-13); the
  registry's limit 1 and the test module's item 1 both say it reads them.

**What breaks in six months.** A framer writes a wrapped `nothing — <why>`
across two lines and meets a `REFUSED` naming the second line; the remedy in
the text says to keep the reason on one line or move the rest into a comment.
That is the same one-line rule the `Reads:` line already has (*a wrapped line
has no last word to read*), and the refusal says so. The other direction —
nobody writes prose there any more and the refusal fires never — costs one
unit's worth of code that reads a shape the template forbids, which is what
an owned-format reader is for.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Refuse the off-shape line; the four words stay `refused`, held by a test** | a frame that wants prose under the heading meets a refusal and moves one line; a wrapped `nothing` reason is refused at its second line | **chosen** — the converged shape of #834's table (owned format, unknown refused), #836's form for a claim (the test holds it), block-more as the cheaper direction, zero prompts; cost measured at two shipped, unread frames and no live one |
| Change the four words to `mixed` and add a paragraph under `removes_section` (round 6's first paste-ready) | records a tolerant owned-format reader as a fact; a removal written as a bullet stays a claim nobody reads; the paragraph is prose a reviewer re-reads, limit 5 again — round 5 fixed a direction word by prose and round 6 found the fix false | rejected |
| State in the registry that prose under the section is read as prose and keep `refused` | deciding from a person's line whether it is prose or a claim is a guess-class reader; a bullet naming a unit is both | rejected |
| Refuse only lines that look like claims (a bullet, a backticked name) and pass plain prose | the same guess-class reader, one shape narrower; the next shape is the next issue | rejected |
| Remove the direction word from the `Reads:` grammar, or add a checker that reads direction words | a change to #835's shipped rule in `docs/`, a `feat:` in a patch release; a checker cannot read a semantic claim (limit 1); without the word a bounded guess (allow-list, unknown refused) and an unbounded one read alike in `grep -rn "Reads: guess"` | out of scope; `questions.md` P1 carries it to the owner, non-blocking |
| ⬜ 4 by rewording the document alone, limit 5 stated as *read by nobody until the helper changes* | honest, but the lead then says the reviewer reads each limit and limit 5 says nobody does; and a reviewer did read helpers' lines at their callers in round 6, as the registry's own definition asks | rejected in favour of naming the warden and telling it, one sentence in `agents/warden.md`; P2 lets the owner take this one instead |
| ⬜ 5 by deleting the clause | leaves the module saying nothing about what a missing record means to the gate, which is what a reader opening it wants to know | rejected; the clause is replaced on its line by what #836 made true (round 6's option B wording) |
| Write the ledger fragment at phase 1 | the item becomes live while the three `## Removes` rows still stand, and `evidence-check` exits 2 on the frame's own rows until phases 2 and 3 land | rejected; records are the last phase |
| Edit `file_claims` and `check_records` docstrings too, for symmetry | moves ten released anchors and owes ten `Re-read ·` rows for words that are already true read through | rejected; the two helpers that change are the two whose text was false |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The two stale sentences and the warden's sentence (⬜ 4, ⬜ 5).** `docs/the-reader-registry.md` §*What neither check can read*: the lead, limit 5 and the `Enforced by:` line name the warden, and limit 5 says the warden reading a caller's change opens the lines of the helpers whose value it changes; `tests/test_a_reader_declares_its_input_class.py`'s docstring item 5 says the same; `agents/warden.md` §*Role* gains one sentence telling the warden to; `specseal_pytest_record.py:108` says a missing record is not measured where the suite failed and existence alone on the ledger arm. The three quoted lines of `spec.md` §*Removes* are gone from the tree. | `git grep -n "the strict side" -- skills` and `git grep -n "does not show its line" -- docs tests agents` print nothing; `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_the_recorder_writes_what_its_process_ran.py tests/test_one_word_one_meaning.py tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` exit 0; `bin/fold-check --root .` exit 0; `bin/evidence-check .` names #835's D1 row on `docs/the-reader-registry.md` as the one DRIFTED anchor and nothing BROKEN | |
| 2 | **The refusal (S1–S4).** `removes_section` hands back the off-shape lines; `removal_findings` refuses each at its line, naming the line, the two shapes and where prose goes; both docstrings say so, their `Reads:` lines unchanged; the new cases in `tests/test_a_record_states_what_the_tree_has.py`, each shown red against phase 1's commit before it is committed; `docs/the-reader-registry.md` §*A frame names what its work removes* gains the sentence and its `Enforced by:` line the node id; `templates/sdd-spec.md`'s comment says nothing else sits under the heading and where prose goes. | the new cases red at phase 1's head and green at this one, the method in `phases/phase-2.md`; `bin/test -q -p no:cacheprovider tests/test_a_record_states_what_the_tree_has.py tests/test_a_reader_declares_its_input_class.py tests/test_a_folded_statement_names_what_enforces_it.py tests/test_a_phase_hands_the_next_one_a_record.py` exit 0; `bin/evidence-check .` names no `file_claims` or `check_records` anchor; `git diff --stat origin/release/v0.21.1 -- skills/evidence-check/scripts/evidence_check.py` shows hunks only inside `removes_section` and `removal_findings` | |
| 3 | **The records (S7).** `seal/ledger/1791852611-….md`: `evidence-check --reverify --into seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md --checked <date>` writes D1's `Re-read ·` row; test-held rows for S1–S3; hashed rows for S5 and S6 (quoted-line anchors on the three rewritten clauses, and on the warden's sentence); `changelog.md` under `### Fixed`; `overview.md`; `phases/phase-3.md`. | `bin/evidence-check --strict .` exit 0 with the fragment present — the frame's three `## Removes` rows silent, D1 cleared, every test row resolving; `bin/correction-check --range origin/release/v0.21.1...HEAD` exit 0; `bin/unverified-check --baseline origin/release/v0.21.1` exit 0 | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. What a phase discovers while
it is being built, and needs the next phase to know, goes to
`seal/specs/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes/phases/phase-N.md`,
from `templates/sdd-phase.md`, when the phase closes. Re-read the Status
column after any rebase: a squashed or rebased commit still answers
`git cat-file` in the worktree that wrote it and nowhere else.

### Notes for the builder, by phase

- **Phase 1.** The three clauses are quoted whole in `spec.md` §*Removes*;
  any rewording clears them. Limit 5's new last sentence should keep the two
  facts (the hash does not move, the diff does not show the line) and add the
  act (the warden opens the helpers a changed caller feeds); round 6's
  paste-ready for ⬜ 4 is one wording. The warden's sentence belongs where
  §*Role* tells the warden what to open for a changed unit, one sentence, no
  new heading; the `seal` word rule (`tests/test_one_word_one_meaning.py`)
  and the role-marker test run on `agents/*.md`. Round 6's option B is one
  wording for the recorder's clause. Phase 1 edits no code outside
  docstrings, so the only anchor that moves is D1; leave its re-read to
  phase 3, where the fragment is written once.
- **Phase 2.** Red first: run the new cases against phase 1's head (a
  `git stash` of the code edit, or `git -C <wt> show <phase-1 sha>:…` into a
  scratch copy under the scratchpad) and record the failing assertion in
  `phases/phase-2.md`. The refusal's detail is new text (§14): name the
  line in backticks, say *a line under `## Removes` is a table row or
  `nothing — <why>`*, and say where prose goes — a row's last cell, the
  `nothing` line's reason, or an HTML comment. Keep the existing
  empty-section refusal's words byte for byte; S3 asserts both findings.
  Blank lines and the header and rule rows pass (S2). The `## Removes` rows
  of this frame are read by nothing until phase 3, so the registry document
  can change in this phase without a STANDING finding.
- **Phase 3.** Write the fragment from `templates/ledger.md`'s row shapes:
  a test-held row is `tests/test_x.py::test_y` in backticks in the Code
  grounds cell with how it was seen red in Verified behavior
  (`docs/the-evidence-ledger.md` §*A claim held by a test*); a hashed row is
  `path#"<whole line>"@<hash>` or `path#unit@hash`. Run `--reverify --into`
  after the new rows are in the file, so one run dates everything. The
  changelog fragment is one `### Fixed` entry in the shape of
  `changelog/0.21.0.md`'s: what a reader meets (a refusal naming the line),
  why (a removal written as a bullet was read by nobody), and the two
  sentences corrected, each with its issue number.

## Operational impact

- **A new refusal in `evidence-check`'s records arm**, exit 2, in every
  repository that runs it: a live frame with a line under `## Removes` that is
  neither a row nor a `nothing — <why>` line. At 39a315a5 no live frame in
  this repository has one; the two shipped frames that do are not read. A
  sibling 0.21.1 frame that writes prose there meets the refusal at its own
  `evidence-check` run and moves the line (`questions.md` M1 names who
  re-measures at the gather).
- No migration, no new dependency, no environment variable. The direction is
  block more; the prompt budget is zero.
- One released ledger row drifts (#835's D1) and is re-read in this item's
  fragment; `seal/releases/0.21.0.md` is not edited.
