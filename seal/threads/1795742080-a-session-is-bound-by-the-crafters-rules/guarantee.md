# Guarantee: 1795742080-a-session-is-bound-by-the-crafters-rules

This run audits HEAD `0bef5cbd9`. The earlier run sealed `f49ed5b31`, and its verdict block stands first below. By `agents/sealer.md` *The guarantee covers HEAD, and a re-run audits what came after*, this run re-runs the claims whose coordinates a commit after `f49ed5b31` touched, and reads the parties again. The earlier run's rows on the moved rules, the submodule and `-W` cases, the G18 searches and round 4's records-only fix rest on lines no later commit changed (executed, `git diff --stat f49ed5b31..HEAD`, which names `range_read.py`, `test_range_read.py`, `gaps.md`, `guarantee.md`, `trail/gate.md` and `trail/rounds/round-5.md`). Round 5 confirms round 4's finding, so a round has now read that fix too.

The base `release/v0.39.2` resolves through `release/v0.39.2@{upstream}` to `6bd4f4426` (executed). The newest `seal` block of `trail/gate.md` reads `run: 0e0ae8de8 against 6bd4f4426`. `git log --no-merges --name-only 0e0ae8de8..HEAD ^6bd4f4426` prints `0bef5cbd9` alone, which touches `trail/gate.md` alone (executed). `seal pr-body <item> --body pr-body-2.md --check` exited 0 (executed, the tree's `skills/implement/scripts/seal.py`).

Every run below was made in a scratch clone of the repository moved to `0bef5cbd9`. Each clone's `git status --short` was clean after its runs. The commit language and the record language are both English, and `seal/parity.json` is not declared, so no `pr.<lang>.md` and no comparison with an original are owed (read, carried from the earlier run: neither file changed).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run at `0e0ae8de8` is the `Broad gate` key's command, though it ran with `UV_OFFLINE=1` | the orchestrator's account in the spawn message; `trail/gate.md`'s second block; `seal/config.json` `Broad gate` | `UV_OFFLINE=1 uvx ruff --version`; `gh run view 45940625424 --job <lint> --log`, read for the ruff it installed; `gh run view 45940625424 --json jobs` | holds. The variable changes where `uv` takes its packages and no step of the command. The cached ruff is `ruff 0.17.6`, and CI's `lint` job at `367210ada` installed `ruff-0.17.6` and passed `ruff check .` and `ruff format --check .`. CI's `ubuntu-latest` and four `windows-latest` pytest jobs passed at the same commit. `367210ada..0e0ae8de8` touches the work item's records alone (executed). The pass count is the record's, and this run ran nothing broad |
| Seen red: the local-root case fails against `_records` before the repair | `367210ada`; `trail/rounds/round-5.md` *What matched*, the fix against the defect | `_records` restored from `9a113e2bd` in the clone, HEAD's case otherwise, then `bin/test tests/skills/test_range_read.py -q -p no:xdist -k test_accepts_a_local_root_reading_the_records_on_disk` | holds: exit 1. The assertion that fails is the `ON_DISK` line followed by `\n# Routing, local\nSecond line.\n`, the record's lines with LF alone, which is the guard the case names (executed). This shows the CRLF read on macOS, where the case writes the CRLF bytes itself |
| The changed slice passes at HEAD | `trail/rounds/round-5.md` *What matched*, the narrow set | `bin/test tests/skills/test_range_read.py tests/lib/test_gitcmd.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | holds: exit 0, 195 passed (executed) |
| `lib/gitcmd.py#decoded` turns CRLF and a lone CR into LF and replaces each undecodable byte | `skills/implement/scripts/range_read.py:66-68` | `grep -n "def decoded" -A4 lib/gitcmd.py` | holds: `data.decode("utf-8", "replace").replace("\r\n", "\n").replace("\r", "\n")` (read) |
| CI's run `45940625424` at `367210ada` passed all four `windows-latest` groups, and the run at `9a113e2bd` failed the local-root case | `gaps.md:8`; `trail/rounds/round-5.md` | `gh run view 45940625424 --json headSha,conclusion,jobs`; `gh run view 45939771497 --json headSha,conclusion,jobs` and `--log-failed` | holds: `45940625424` has head `367210ada`, conclusion `success`, and each of the four `windows-latest` groups `success`. `45939771497` has head `9a113e2bd`, conclusion `failure`, and its one failed job, `windows-latest` group 3, fails `Test_main.test_accepts_a_local_root_reading_the_records_on_disk` (executed) |
| The chain holds at the working tree but for this file | `skills/core/SKILL.md` *Judgment is not licence to skip a party* | `python3 skills/code-review/scripts/chain_check.py --baseline 6bd4f4426 --root <the repository> --worktree`, before this file was rewritten | holds for what this run owes: exit 1 on one line, that `guarantee.md` is behind HEAD because `6c128351b` touches `tests/skills/test_range_read.py`. That line is the reason for this run. It printed no other refusal (executed) |
| The crafter's account of its read of `9a113e2bd..367210ada` | `trail/rounds/round-5.md` *Not judged*, the first row | none | unverified: no record holds it, and round 5 was not given the hand-back. The orchestrator, which received the hand-back, answers it. The repair's two commits and every sentence they wrote were read by round 5 and by this run, so no statement of the range is left unread |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The design | `seal range` prints the records whole, at HEAD, or on disk where the root is local (*Data & interfaces*, S5) | The repair. The HEAD path has printed a committed CRLF record with LF since phase 1, through `subprocess`'s decode in `lib/gitcmd.py#git`. The on-disk path now does the same, so "as it stands on disk" still names where the record is read, as round 5 reads it (read) | none |
| The build | Phases 1 and 2, the fix passes of rounds 1 to 3, the fold for round 4, and the repair `6c128351b` and `367210ada` after the seal | The repair's diff changes `_records`, its docstring line at `:66-68` and the local-root case alone (executed, `git diff f49ed5b31..HEAD -- skills lib tests`). The seen red above. `frame/plan.md`'s two Status commits and both phase records stand (read) | none |
| The last round | Round 5 at `367210ada`, a verifying round of the repair, has no finding. It confirms round 4's finding | The tree. Only `0e0ae8de8`, which touches `gaps.md`, and `0bef5cbd9`, which touches `trail/gate.md`, follow `367210ada`. This run read both diffs whole (executed, `git diff 367210ada..HEAD`) | none |
| The changelog | It is unchanged since the earlier run. Its `seal range` item says the records follow "at HEAD, or on disk where the root is local" | The repair, which changes the line ends of the on-disk read and not its source (read) | none |
| The orchestrator's part of the pull request body | `pr.md` is unchanged: one quote of `frame/plan.md` *Operational impact* and the three `Closes` lines | `seal pr-body --check` on `pr-body-2.md` exited 0 (executed) | none |
| The orchestrator's own records | `0e0ae8de8` marks `gaps.md`'s Windows row `closed` and names run `45940625424` at `367210ada` and the failure at `9a113e2bd`. The spawn message says the gate's first attempt failed on a reset connection to PyPI and the second ran with `UV_OFFLINE=1` | The runs above confirm each fact of the row. The Item cell opens with `closed`, as `skills/implement/SKILL.md` *4.* asks. Its second cell still names CI's Windows leg, which is the party that answered, and the run that closed the row stands in the Item cell (read). The gate account agrees with the ruff version and CI's jobs above | none |

Not judged here: the broad gate's pass count, which `trail/gate.md` records and the sealer does not run. The spawn message asked that `guarantee.md` be rewritten. This run rewrote the tables for this run and appended its verdict block below the earlier one, which stays as it was, as `agents/sealer.md` step 5 asks.

```seal
target: f49ed5b31 against 6bd4f4426
Verdict: sealed
```

```seal
target: 0bef5cbd9 against 6bd4f4426
Verdict: sealed
```
