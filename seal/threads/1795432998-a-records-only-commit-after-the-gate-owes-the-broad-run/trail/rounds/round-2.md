# Review round 2: 1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run

```seal
target: b34bb9e6b, fixes eb03b235f..b34bb9e6b
```

This is a verifying round. Its code bound is the diff from round 1's target
to HEAD, `eb03b235f..b34bb9e6b`: the round-1 record (`af42807dc`), the
framer's fold of both findings (`07a38f1ce`), the fix pass (`8baf1cb43`,
which changes `skills/code-review/orchestration.md`, `skills/core/SKILL.md`
and `changelog.md`) and the close blocks (`b34bb9e6b`). It was read in a
`git clone --no-local` of the branch at `b34bb9e6b`. `seal/parity.json` is
not declared, so no parity comparison was owed. `seal/config.json` names
English for both language keys, so no `pr.<lang>.md` is owed and none
stands.

The work item's records were each read whole at `b34bb9e6b`:
`routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`,
`gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and
`trail/rounds/round-1.md`. No sentence in them is contradicted by the
target. Each quote of `pr.md` still stands word for word at its
coordinate: `frame/design.md:34`, the G3 row at `frame/design.md:11` and
`frame/plan.md:47` (read).

Carried from round 1, not re-established: `chain_check.py#broad_gate`
calls `follows` with no `only`, and `#guarantee` passes
`only=CLOSING_RECORDS`. The fix diff leaves `skills/code-review/scripts/`
and `agents/` untouched (executed: `git diff --stat eb03b235f..b34bb9e6b`).
`CLOSING_RECORDS` still stands at `chain_check.py:303` (executed: `grep`).
Round 1's mutation probes were not re-run, since the case and the arms
they pinned are outside the fix diff and unchanged.

The fix pass's account claims that a `git grep` for "closing records"
over the files this branch changed finds the term only in
`tests/skills/test_chain_check.py`. The same search at `8baf1cb43` also
prints `templates/setup/config.md:485`, `frame/design.md:12` and `:18`,
`frame/plan.md:48` and `round-1.md` (executed). Each of those either
spells out the two files beside the term, quotes the code's refusal
string, or quotes round 1, and the account names `config.md:485` in its
next sentence. So the claim is loose in its wording and is no finding.

The new acceptance scenario *The commits of the gate's record and the
verdict* (`frame/design.md:63`) cites `test_accepts_a_sealed_verdict_at_head`
for its *Then*. That case pins the guarantee arm only. The half that says
neither commit owes another broad run is held by *Test_broad_gate*'s
`test_accepts_a_run_at_head` on the same fixture
(`tests/skills/test_chain_check.py:3076`), which the scenario does not
cite. The scenario's main check is the paragraph read in review, so this
gap in the citation changes nothing the release ships.

## Findings

### 1. The branch's core no longer fits the harness cap in its own worktree, so the broad run there fails `tests/lib/test_core.py`

```seal
severity: should
location: `skills/core/SKILL.md:114-115`, `tests/lib/test_core.py:233-247`
evidence: executed `bin/test tests/lib/test_core.py` among sixteen modules in the clone, which fails `Test_module::test_the_trees_core_stays_under_the_harness_cap` with `AssertionError: 10322`; executed `python3 -I <scratch>/round-2/test_tmp_core_cap.py <clone>`; read `lib/core.py:42-46`, `lib/core.py:106-123`, `skills/verify/scripts/broad_gate.py:937`, `skills/verify/scripts/broad_gate.py:1441-1442`
```

Why it matters: `test_the_trees_core_stays_under_the_harness_cap` renders
the tree's core as the hook prints it and asserts the output is shorter
than `CAP`, 10,000 characters (`tests/lib/test_core.py:233-243`,
`lib/core.py:46`). The output spells the checkout's root three times: once
in the header and twice in the closing line (`lib/core.py:106-123`). The
probe measured the rest of the output, which does not depend on the path,
at three commits. It is 9,462 characters at the base `2025561ae`, 9,719 at
round 1's target and 9,734 at HEAD. So the case passes at HEAD only where
the checkout's root is at most 88 characters long. At the base the limit
was 179.

The branch's worktree has a 124-character root. There the case gives
9,734 + 3 x 124 = 10,106 at HEAD and fails, while at the base it gives
9,834 and passes. `seal gate` runs the head suite in the checkout it is
called from (`broad_gate.py:937`, `cwd=root`), and runs the base in a
`mkdtemp` worktree with a short path (`broad_gate.py:1441-1442`). So the
orchestrator's broad run from this worktree will fail on this file, and
the base will pass it. A failure the base does not have costs a broad run
and a repair after it. In CI the root is about 41 characters, which gives
9,857, so a pull request run passes. The clone this round used has a
196-character root and failed at 10,322. That matches
9,734 + 3 x 196, which checks the arithmetic.

The defect is not the fix pass's. Phase 1's commit `3e1d1ec77` grew the
core by 257 characters, and `8baf1cb43` added 15 more when it spelled out
the two files in row 4. Neither the phase record's narrow runs nor round
1's included `tests/lib/test_core.py`. A build phase made the unit, so
this finding takes neither a `regression:` nor a `reopens:` line.

No text fix within rows 3 and 4 is enough on its own. Tightening both
rows while keeping every fact `frame/design.md` *Scope* items 1 and 2 name
saves about 35 characters, and 107 are needed for a 124-character root.
So the fix needs a choice, and the choice is the orchestrator's:

```text
Either (a) cut at least 107 characters from what skills/core/SKILL.md
renders below its frontmatter, so the rendered output stays under
10,000 at a 124-character root. Rows 3 and 4 give about 35 of them
without dropping a fact Scope items 1 and 2 name, so the rest comes
from text this branch did not write, and frame/design.md Scope has to
name that change. Or (b) change tests/lib/test_core.py so the case
measures the closing line against a plugin root of fixed length, not
the checkout's own root. The hook prints the installed plugin's root
there, whose length does not depend on where a worktree stands. That
change has to state the length it assumes, and frame/design.md Scope
and Removes have to name it. Taking the broad run from a checkout with
a shorter path is no fix: the next worktree of this repository meets
the same limit.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the paragraph at `skills/code-review/orchestration.md:268-278`
now says that a records-only commit owes `seal pr-body` and the sealer
again only where it changes a record other than `trail/gate.md` and
`guarantee.md` after the sealer has written its verdict. It also says the
commits of those two files owe neither another broad run nor another
sealer, which agrees with `CLOSING_RECORDS` at `chain_check.py:303`
(read). It does not say that the commit of `guarantee.md` owes no
`seal pr-body`, so it leaves `skills/code-review/gate-to-pull-request.md:12-13`
standing: one more `seal pr-body` run before the pull request opens
(read). `gate-to-pull-request.md:141-150` speaks of a repair to another
record and cites the paragraph (read). The same condition stands in
`frame/design.md:40` (*Scope* item 3), `frame/design.md:51` (*Out*),
`frame/plan.md:21`, `frame/questions.md:6` and `changelog.md:3` (read).
The rest of the paragraph keeps round 1's wording, rewrapped (executed:
`git diff --word-diff eb03b235f..b34bb9e6b -- skills/`).

```seal
confirms: round-1#2
```
What holds: row 4 at `skills/core/SKILL.md:115` reads "at HEAD or at a
commit that only `trail/gate.md` and `guarantee.md` follow", the
paste-ready row of round 1 (read). `frame/design.md:39` (*Scope* item 2),
the G4, G7 and G13 rows at `frame/design.md:12`, `:15` and `:21`, and the
first *Process changes* row at `changelog.md:11` name the two files
(read). A `git grep -F 'closing records'` outside `seal/threads/` prints
no line of `skills/core/SKILL.md` (executed).

What matched: the narrow modules that read the two files the fix pass
changed pass at the target, except finding 1's case. Those are
`tests/text/test_the_rules_have_one_owner.py`,
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/text/test_broad_gate_rule.py`,
`tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`,
`tests/behaviour/test_the_sealer_guarantees.py`,
`tests/behaviour/test_docs_line_wrap.py`, `tests/skills/test_passages.py`
and nine more: 474 passed and 1 failed (executed). `seal rules --check`
holds all 175 check lines in 68 rule files (executed).

What matched: `frame/plan.md:48`, the orchestrator's row in *Judgments of
the run*, cites `skills/implement/orchestration.md` *Orchestrator: the
order inside a ticket*, the paragraph opening **A decision made after the
frame is committed is folded**. Both stand at `:21` and `:58` (executed:
`grep`). Round 1 located both findings in `frame/design.md`, as the row
says (read).

What matched: *Data & interfaces* still holds after the fix pass. Seven
text files outside `seal/threads/` and one test module change against the
base (executed: `git diff --name-only 2025561ae..b34bb9e6b`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check over the target. The suite is `unverified` by this round, and contract rule 2 leaves it out of this round. Finding 1 says one case it will fail from the branch's worktree | `gaps.md:7` | the orchestrator, at the broad run after the rounds settle |
| Which of finding 1's two fixes to take: cutting core text the branch did not write, or changing what the cap case measures | `skills/core/SKILL.md:114-115`, `tests/lib/test_core.py:233-247` | the orchestrator, before the fix pass |

## Probes

| Command | Result |
|---|---|
| `bin/test` over sixteen modules that read `skills/core/SKILL.md` or `skills/code-review/orchestration.md`, `-q`, in the clone | exit 1: 474 passed, 1 failed, `tests/lib/test_core.py::Test_module::test_the_trees_core_stays_under_the_harness_cap`, `AssertionError: 10322` at a 196-character root |
| `python3 -I <scratch>/round-2/test_tmp_core_cap.py <clone>`, which writes each commit's `skills/core/SKILL.md` into the clone, renders it through `lib/core.py#rendered` and restores the file | the output apart from the root, which it spells 3 times: 9,462 at `2025561ae`, 9,719 at `eb03b235f`, 9,734 at `b34bb9e6b`; `git status` clean afterwards |
| `bin/seal rules --check`, in the clone | exit 0: all 175 check lines in 68 rule files hold |
