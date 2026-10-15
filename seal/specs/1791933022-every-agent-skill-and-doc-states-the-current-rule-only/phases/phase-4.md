# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | f1ccf61a, the last build commit; this record's commit follows it |

## What this phase was asked

`plan.md`'s row 4: the sealer as the final, independent guarantor, in the
owner's words on #923 item 2 — *I verified, independently of the smith and
the warden, that the work before me is sound, and I guarantee it* — with the
issue body and the tree as its reference, never an agent's word. It checks a
claim against the fact (a sample of the smith's `executed` and `seen red`
claims re-run; each `fixed <commit>` on the branch and touching its
`Location`; nothing removed in this release back) and the parties against
each other, and it re-judges neither the design nor the code's quality. The
broad run and its record stay a script's, run as its first act; it runs on
Opus, after the pull request body and the changelog exist.

To build: `agents/sealer.md` anew and small, the old text a reference only;
`templates/sdd-guarantee.md`; the `guarantee` arm in `chain_check.py`, a
ready pull request passing only where the file names HEAD and reads `sound`;
the three sealer eval cases (sound → `sound`; a pull request body claiming a
change the tree lacks → `not sound`; a phase record's false `seen red` →
`not sound`); the documents' sealer sections rewritten in place; the old
sealer cases replaced. And two leftovers of phase 3: the hygiene step that
fetched `refs/pull/*/head`, with everything that counted it, and a decision
on whether `chain_check.py#changed` should read without rename detection,
pinned by a case seen red. No agent eval against a model, and no full suite.

## What this phase found

**The guarantee may be followed only by the sealer's two files.** The file
cannot name the commit that adds it, so *names HEAD* reads as HEAD or
commits touching only `broad-gate.md` and `guarantee.md` after it. The
broad-gate arm's rule, any file of the work item, would let a phase record, a
round or the changelog change after the sealer read them. `follows` took an
`only` argument for it rather than a second walk.

**The check reads without rename detection, and keeps the #90 exemption by
bytes.** `git diff -M` paired a deleted declaration with a similar added one,
which the two `TestRetired` cases had padded against; the padding is gone and
those two cases were the red ones. An exact move of a declaration, which the
0.4.0 root move does to every one, is still neither judged nor missed: an
added file whose bytes a deleted file of the same name carried is a move, its
blob hashed where git names none (an untracked file under `--worktree`). The
old check read with `-M` since 95e32588, so the blind spot predates the
branch.

**A release pull request into `main` refuses every squashed item.** Run at
cba5e0cd against `origin/main`, the check named four 0.22.0 items' last
`Target SHA` as one *HEAD does not descend from*, and none of them carries a
`broad-gate.md`. The pull-head fetch this phase removed was what resolved
those commits before phase 3; phase 3 made the check ancestor-only. The
guarantee arm refuses the same items the same way. `questions.md` Q7 holds
the options; nothing here builds one.

**The new definition keeps the contract paragraph.** Every definition carries
it under `tests/test_every_agent_reads_the_contract.py`, and part B rewrites
the five together; a sealer without it would split a rule the set shares.
`agents/sealer.md` is 8,017 B (from 15,188), and `payload_meter --agent
sealer` reads the agent share at 28,385 B — the definition and the contract —
where it was 35,597, with the CLAUDE.md pair 14,775 B beside it (`executed`,
3.2 B/token estimated). Its `Enforced by:` lines fit the 88-column wrap, which
reads a definition's targets as prose, so each names one target.

**Pins on the old sealer text, one line each.**

| Case | What it pinned | Now |
|---|---|---|
| `test_the_seal_is_taken_once_by_the_sealer.py::test_the_sealer_is_told_the_gate_says_which_copy_ran` | the copy line, `tree` values, *Quote the gate line* | removed; `test_the_sealer_guarantees.py::TestDefinition::test_the_sealer_quotes_what_only_the_gate_can_tell` holds the quote |
| `…::test_the_documents_name_the_line_that_says_to_commit_the_cell` | the sealer's sentences on the `SEALED` line's second line | the sealer half removed; the orchestration half stays |
| `…::test_the_documents_say_where_the_panel_now_carries_each_name` | the sealer's `gate`, `rounds`, `base` and deferral rows | the sealer half removed; the documents' halves stay |
| `…::test_the_documents_name_the_ci_also_row` | the sealer's `CI also` sentence | narrowed to the stale name's absence |
| `…::test_the_sealer_names_the_one_write_its_definition_is_allowed` | `broad-gate.md` as the one write | re-pointed: `guarantee.md` is the whole write, and `broad-gate.md` the gate's, through `broad-gate --record` |
| `test_the_gate_names_every_step_ci_runs.py::test_the_documents_say_the_count_is_over_the_steps_ci_runs` | the sealer's `CI also` sentence | the sealer half removed |
| `test_the_gate_asks_the_range_ci_will_ask.py::test_the_documents_name_the_panel_row_the_gate_actually_prints` | the sealer naming the `base` row | narrowed to the stale names' absence; the panel half stays |
| `test_a_parallel_agent_names_its_scratch_after_the_work_item.py::test_the_sealers_capture_file_carries_the_work_item_id` | §*The command*'s capture file | re-pointed at §*Order of work* and §*Rules*, with the `at-base/` clone |

Every other case reading `agents/sealer.md` is green on the new text, its
pinned sentence carried where the guarantor still needs it (the row refusal,
the stamp, `new?`, the four conditions, §6's four acts, the base's
resolution, one assigning definition and the four silent).

**Two cases phase 3 left red, and one exposed here.** The reader census
listed three units whose docstrings phase 3 re-pointed, and the post-bash
dispatch case asserted the reminder that left with its hook; both fixed at
5bb3d4c2. `test_the_rules_command_reads_each_rule_off_its_test.py`'s tree
case renamed the first target it met even in a glob it had already planted,
which counted eight where it expected seven once a definition carried a
target; it now plants or renames once per glob.

**New tests, against their groups.** `TestChanged` is `changed`'s first
group: no case read it before. `tests/test_the_sealer_guarantees.py` is the
new arm's and the template's module, where `spec.md` names it.
`test_evals_layout.py::test_every_sealer_case_grades_the_guarantee` covers
what no layout case read, a case's graders against its agent's output.

**Red first, and the mutations.** Each new and changed case was run before
its code: the step counts (4 failed), `TestChanged` and the unpadded
`TestRetired` (4), the guarantee cases and `TestDefinition` (9), the settle
counts (18), T18 against the old cases copied from HEAD (6 gaps), the rules
tree case (8 for 7). Eleven units broken through `mutation-check`, four in
`changed` and seven in the arm, each `red` once a case was sharpened or added
for the three that first survived (the worktree hash, `sound` read by prefix,
two `Verdict:` lines).

**The fixtures behave as their cases claim.** Each scaffold built; its case
was green at HEAD, and against `main`'s `src/textutil.py` red in the sound
and untrue-body fixtures and green in the false-red one. The tree's
`broad-gate --base main --record` over the sound fixture exited 0 and wrote
`broad-gate.md` (`executed`). No session ran: Q2, the guarantor's cost, is
the sealer's first run on this branch.
