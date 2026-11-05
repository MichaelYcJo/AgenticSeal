# Implementation Plan: mutate-restore-is-held-by-no-case

## Technical context

Coordinates are at `fe793f03`, as `frame/design.md` states. Phase 1 starts after #1393 is squash-merged into `release/v0.32.5` and the orchestrator merges `release/v0.32.5` into this branch, never by a rebase. By then `restore`, `clear_bytecode_cache` and `command_words` are `mutation_check.py`'s own, and the phase locates every line below by its text.

- `skills/verify/scripts/mutation_check.py:403-417`, `mutation_run`: the baseline and the mutated run sit inside one `try`, and its `finally` at `:416-417` calls `_put_back`. A `no baseline` or timed-out baseline returns from inside the `try`, so the `finally` restores what the cases wrote.
- `:452-455`, `batch_run`: the baseline alone sits inside a `try` whose `finally` calls `_put_back`, before any mutant is written. Each mutant then has its own `try` and `finally` at `:465-472`.
- `:539-566`, `_put_back`: it writes the held bytes back only where the file's sha256 differs, and raises `NotRestored` where the write raises or lands other bytes. It has no platform branch.
- `:641-672`, `main`'s exception arms: `NotRestored` prints `not restored`, and `KeyboardInterrupt` prints `interrupted` with "holds the bytes it held before the command started". The comment D2 rewrites is `:652-656`.
- `tests/skills/test_mutation_check.py`: `Test_batch_run` drives `batch_run` directly with the `STAND_IN` world, and `Test_main` drives `main` in process through `run(argv, capsys)`, `probe` and `cases_command` (`:177-192`). The existing interrupt case `:1571-1652` monkeypatches `_wait` and is POSIX-only. The existing timed-out case `:1463-1527` is POSIX-only too, because it asserts the process group ended.

The chosen approach adds cases that drive `main` with stand-ins that write the target, one parameter per unheld path, and rewrites five sentences. Its failure scenario in six months: a stand-in's write and the 1-second bound race on a slow runner, the bound wins, and a timed-out parameter passes without the restore ever having had bytes to put back. D1's first assertion, that the stand-in's write happened, turns that race into a red that names it, rather than a green that holds nothing. A second scenario: a later change moves `restore` again or merges the two `finally`s. The cases call `main` and the module's own names, so they keep holding the behaviour wherever the restore lives.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Apply round 4's paste-ready case as given: two parameters, one pair only, at the old module path | It holds Mb and Mc and leaves Mbb, Mcb and Mib green, three paths the probe shows leave the cases' bytes on disk, one of them under a printed line that says the file holds its first bytes. The module it names no longer exists | Rejected. The text is read against the code, as `1793718241-a-fix-pass-applied-paste-ready-text-as-given` states, and contract rule 12 asks for the class, which `batch_run` joined with #942 |
| D1's cases across both shapes and every no-verdict baseline exit | The race in *Technical context*, which D1's first assertion turns red | Chosen |
| Replace the structure: take the baseline back out of the restore's reach, as before #698's round 3, and say the baseline writes nothing | Cases that write the target during the baseline leave it changed, while `interrupted` says the file holds its first bytes and `no baseline` says the break was never written over a rewritten file. The interrupt case's own `[baseline]` fixture is such cases | Rejected. The premise that keeps the restore's reach is that cases can write the file they test, and it is checked: the module's `REWRITES` and the interrupt case's `rewrites.py` fixtures do it, and the probe shows the restore putting their bytes back on every exit |
| Replace the structure: one helper both shapes call for the baseline and its restore, so one case per exit holds both shapes | `mutation_run` restores once after both runs and `batch_run` restores after the baseline and again after each mutant (`:416-417`, `:454-455`, `:472`), so one helper changes the one-pair path's restore count and is a code change a patch has to prove equal. The issue asks for cases and text | Rejected. The premise that keeps two call sites is that the two shapes restore at different moments, read at the three coordinates |
| One case per shape, for one exit each, rather than one per exit | An exit-specific skip, Mb or Mc, which round 4 measured surviving the module, survives again on the exit not chosen. The issue asks for each mutation seen red | Rejected. Two more parameters cost two runs, one of them a 1-second bound |
| Run the timed-out and interrupt parameters on Windows too | The Windows leg would run code paths no machine here can probe, and the interrupt fixture's signal handling is the process-group bound's, which only POSIX has | Rejected. `_put_back` and both `finally`s have no platform branch, so the platform part is how the run ends, which the existing timed-out and interrupt cases already hold on POSIX alone. The `no baseline` parameters run on every platform. `frame/questions.md` Q1 is the Windows legs' answer |
| Leave the message `restore` raises to #1393, which moves the function | #1393's frame moves `restore` with its behaviour unchanged and edits no message, and its subject is a removal. The false clause would ship in `seal mutate`, its only caller, with no work item owning it | Rejected, on the orchestrator's reading (P1, agreed). D4 takes it, and the build starts after #1393's merge so the two branches do not both edit `restore` |
| Correct the message in `arm_check.py` on this branch, before #1393 lands | Both branches edit `restore`'s block, one moving it and one rewording it, and the second to merge meets a conflict or carries the old sentence into `mutation_check.py` | Rejected (P2, agreed). The build starts on the merge |
| A text case pinning D3's new descriptions | It holds a sentence no printed line carries, and it would be read on every run to catch a drift a review round caught here | Rejected. D3's descriptions are not printed lines, so contract rule 14 does not reach them, and `skills/core/SKILL.md` *The rule a mechanism is kept against* keeps a mechanism only for what it catches |
| Leave the descriptions and fix only the case | The crafter reads `seal-mutate.md` at each unit it mutates, and it would read that `not restored` means a break left on disk where the break was never written | Rejected. The issue asks for both, and D3 is the top rung's reason |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* 1 to 7, starting from the merge of `release/v0.32.5` after #1393 lands | S1 to S9; each new parameter's red under its own mutant and green under the other four, and D4's case red with the old sentence back, written in `trail/phases/phase-1.md` with the command that showed it | 4aa0aa4c |

Assumptions the phase builds on, where any answer gives the same work: the batch interrupt may extend the existing interrupt case's parametrization or sit in the new case, whichever reads more plainly beside its neighbours. A `no baseline` stand-in may exit 1 or 5, since `no baseline` reads both the same way. Each mutant may be applied with `seal mutate` on `mutation_check.py` selecting the new cases, or by hand in a scratch clone, as long as the phase record names the replacement and the run.

## Operational impact

None for a deployer. No interface, dependency or environment variable changes. One printed sentence changes, inside the `not restored` line (`frame/design.md` D4). The build waits on #1393's merge into `release/v0.32.5`.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-05 | Folded phase 1's one contradicted statement: design *Grounding*'s #1393 row now cites #1393's frame at `4a3ed47c`, the squash on `release/v0.32.5`, instead of the branch commit `868dc7bf` | #1394's squash left `868dc7bf` on no main or release ref, so `test_every_cited_commit_outlives_the_squash` refused the row; I read the frame at `4a3ed47c` and its *Scope* items 1 and 2 and its out-of-scope line on #706 still say what the row quotes | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
