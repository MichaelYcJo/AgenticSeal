# Review round 6: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

target: 71c717bf, fixes 850c6c40..71c717bf

This round reads the commits after round 5's target, `850c6c40..71c717bf`, and nothing else of the branch. One of them changes a path outside this thread's records: 71c717bf changes `write_gate_file` and the comment above `GATE_FILE` in `skills/verify/scripts/broad_gate.py`. The other three change only this thread's records: 1d41c848 (`trail/rounds/round-5.md`), 8e71764d and 90d1d702 (`guarantee.md`). Round 5 left no finding open and closed none `fixed` or `rejected`, so this round names no earlier finding by a `confirms:` line. Carried from round 5 and not re-established: where the gate, the check and the hooks keep a thread's paths, and the list of multi-segment `os.path.join` constants in `hooks/`, `skills/*/scripts/` and `.github/scripts/`. Re-established this round: every verdict below, run 40500883542's failure, and the Windows join, by an `ntpath` run. No `original:` line is written, because the repository declares no `seal/parity.md`. `frame/plan.md` *Verification this work item owes* binds the round: no finding asks for red-first evidence or a mutation run.

## Findings

### 1. Round 5 confirms that 22598c73 fixes the Windows failure, though its own probe printed the mixed-separator path that `write_gate_file` returns

severity: should
location: `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/rounds/round-5.md:14`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/rounds/round-5.md:17`
evidence: read `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/rounds/round-5.md:14`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/rounds/round-5.md:17`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/rounds/round-5.md:43`, `tests/test_broad_gate.py:1978-1986`, `skills/verify/scripts/broad_gate.py:2473-2506`
verdict: fixed ed49b7a4

The sealer and every later round read round 5's confirmations as settled facts, so a wrong one is a sentence an agent acts on. The sealer did act on it: it sealed at 8e71764d, and the pull request's next Windows run failed.

Round 5's first confirmation, at `:14`, says that `write_gate_file` joins `GATE_FILE` under the thread "for `open` and `os.makedirs`". It quotes its own `ntpath` probe, which printed `<item>\trail/gate.md`. It then says that the normalised form is `<item>\trail\gate.md`, "so the disk path still works there". The sentence about the normalised form is true of `ntpath.normpath`. Nothing in `write_gate_file` calls it, though. The function also returns the joined path unchanged, at `skills/verify/scripts/broad_gate.py:2505` in the tree at 22598c73. Round 5 did not follow that return to its readers. `tests/test_broad_gate.py:1983` compares it as text with `os.path.join(str(tmp_path), "trail", "gate.md")`. That is the case run 40500883542 failed on the windows `--splits 4 --group 1` job, with `assert 'C:\\Users\\r...trail/gate.md' == 'C:\\Users\\r...rail\\gate.md'`. The two `Refused` messages at `:2487` and `:2504` of that tree also printed the mixed path. Only `uncommitted_line` normalised it, through `os.path.realpath`, and that is the one reader round 5 named. So 22598c73 moved the Windows failure from `tests/test_broad_gate.py:229` to `:1983` and did not end it, and the confirmation claimed more than the probe showed.

The second confirmation, at `:17`, rests on a premise that excludes this case: "Only a constant that another module compares as text can have it." The defect was not in a constant that another module compares. It was in a path joined from a `/`-spelt constant and then returned to a caller that compared it. The search that followed, for multi-segment `os.path.join` constants, could not find `GATE_FILE`, because 22598c73 had just made it a plain string. Its conclusion that no other path has the defect therefore had no grounds. This round re-did that search at 71c717bf (see the second confirmation below).

The fix pass rewrites the two sentences in place. In `:14`, replace the sentences from "`GATE_FILE` has one reader in the gate" through "The new comment at `:160-161` says this." with:

```markdown
`GATE_FILE` has one reader in the gate, `write_gate_file` at `:2475`, which joins it under the thread, opens the joined path, makes its directory and returns it. On Windows that join gives `<item>\trail/gate.md`. An `ntpath` run printed that path, and nothing in `write_gate_file` normalises it before it returns it. `tests/test_broad_gate.py:1983` compares the returned path as text with `os.path.join(str(tmp_path), "trail", "gate.md")`, so on Windows this fix moves the failure from `:229` to `:1983`. The `Refused` messages at `:2487` and `:2504` print the mixed path too. Only `uncommitted_line` at `:3089` normalises it, by `os.path.realpath`, before it hands it to `git status`. The new comment at `:160-161` says the join is accepted as a disk path, which holds for `open` and not for a caller that compares the path.
```

In `:17`, replace the sentence "Only a constant that another module compares as text can have it, so I listed every multi-segment `os.path.join` constant in `hooks/`, `skills/*/scripts/` and `.github/scripts/`." with:

```markdown
A path has it wherever a `/`-spelt constant is joined by `os.path.join` and the joined path is returned, printed or compared as text, and this round traced only the constants, not the joined paths. I listed every multi-segment `os.path.join` constant in `hooks/`, `skills/*/scripts/` and `.github/scripts/`, a search that cannot find `GATE_FILE` itself.
```

answer: fixed in the commit that adds this answer: both sentences of round-5.md are rewritten in place with the text this finding gives. The code defect itself was fixed in 71c717bf. The orchestrator made this record fix, as a correction too small for a crafter spawn.

## Confirmations

confirms: none
71c717bf ends the separator defect in the path `write_gate_file` returns. The orchestrator claimed that the function now joins `*GATE_FILE.split("/")` and that the comment above `GATE_FILE` says so. `skills/verify/scripts/broad_gate.py:2476` reads `path = os.path.join(item, *GATE_FILE.split("/"))`, and `:160-162` say that `write_gate_file` splits the constant on `/` so that the path it returns takes the platform's separator throughout. An `ntpath` run joined `trail/gate.md` both ways onto `C:\r\seal\threads\x`. The old join gave `C:\r\seal\threads\x\trail/gate.md`, which is not equal to `ntpath.join(item, "trail", "gate.md")`. The new join gives `C:\r\seal\threads\x\trail\gate.md`, which is equal to it, and its directory is `C:\r\seal\threads\x\trail`, so `os.makedirs` at `:2501` makes the same directory as before. The comment's "throughout" depends on `item` holding one separator. `main` at `:2941` passes `os.path.abspath(args.record)`, and the `ntpath` run shows `abspath` turning a typed `C:/r/seal/threads/x` into `C:\r\seal\threads\x`. The cases at `tests/test_broad_gate.py:235`, `:1980-1994` and `:2309-2316` pass `str(tmp_path)` or `str(repo / ITEM)`, which `pathlib` spells with the platform's separator. `GATE_FILE` is still `"trail/gate.md"`, so the case at `tests/test_broad_gate.py:228-232` still holds it equal to `chain_check.py#BROAD_GATE_FILE`. The pull request's `tests` run 40501484402 tested 71c717bf, and all four windows-latest shards passed. Group 1 reported `1285 passed, 16 skipped`. This round's one `bin/test` command over `tests/test_broad_gate.py` and `tests/test_chain_check.py` exited 0 on macOS. 71c717bf changes no case. The case that pins the new behaviour is `tests/test_broad_gate.py:1983`, and run 40500883542 saw it red on Windows against 22598c73. Executed and read.

confirms: none
`GATE_FILE` is the only `/`-spelt constant in `broad_gate.py` that the gate joins into a path, and every path built from it now takes one separator wherever it is returned, printed or compared. A search for string literals holding `/` found three constants: `GATE_FILE` at `:163`, and `REMOTE_BASE` and `REMOTE_LABEL` at `:416-417`, which are git ref names and never disk paths. A search for `os.path.join` calls that take a literal holding `/`, and for f-strings or `+` that put `/` after a value, found only `:2476`. `ROUNDS_DIR`, `GATE_REL`, `PLUGIN_JSON` and `WORKFLOW` at `:164`, `:282`, `:283` and `:2107` are built by `os.path.join` from single segments, so they take the platform's separator. The path `write_gate_file` returns reaches three readers: the `Refused` message at `:2488`, the `Refused` message at `:2505`, and `uncommitted_line` at `:3036` and `:3089`. The first two now print one separator. The third prints a `relpath` of `realpath`s, and an `ntpath` run gave `seal\threads\x\trail\gate.md` for it. That matches `tests/test_broad_gate.py:52`, which builds the expected path with `os.sep`. `:1691` converts a path the other way, from `os.sep` to `/`, for a value git reads. Outside the gate, `skills/verify/scripts/seal_stamp.py:1303` joins `chain.BROAD_GATE_FILE` onto `item` by `os.path.join`, so on Windows it builds a mixed path as well. It hands that path only to `_read` at `:1170-1176`, which opens it and returns the text or None, so the path is never returned, printed or compared. `skills/code-review/scripts/chain_check.py:1842` builds `f"{item}/{BROAD_GATE_FILE}"` for `read_record`, which reads it at a git commit, where `/` is the separator. Read and executed.

confirms: none
The three other commits change only this thread's records. `git show --name-only` lists `trail/rounds/round-5.md` alone for 1d41c848, and `guarantee.md` alone for 8e71764d and for 90d1d702. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| the full suite, the repository-wide lint and the typecheck at 71c717bf; the gate's newest run, recorded in `trail/gate.md`, is behind this commit | the branch | the orchestrator's broad run after the rounds settle |
| the hygiene workflow's `release` job on 71c717bf, run 40501484379, failed with three refusals: the last round's `target:`, the newest gate run and the guarantee are all behind 71c717bf. This record answers the first once it is committed. | `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/gate.md`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/guarantee.md` | the orchestrator, who commits this record and runs the broad gate, then the sealer |
| whether a case should hold `seal_stamp.py`'s join of `BROAD_GATE_FILE` to one separator; this round found no reader that compares or prints that path, and the code is outside the fix diff | `skills/verify/scripts/seal_stamp.py:1303` | the orchestrator, or a later work item |

## Probes

| Command | Result |
|---|---|
| `git log --oneline 850c6c40..71c717bf`; `git show --name-only --format=` of 1d41c848, 8e71764d, 90d1d702 and 71c717bf | four commits; 71c717bf touches `skills/verify/scripts/broad_gate.py` alone, and the other three touch `round-5.md` or `guarantee.md` alone |
| `grep -nE` over `broad_gate.py` for string literals holding `/`, for `os.path.join` with such a literal, and for `/` after an f-string value or a `+` | literals at `:163`, `:416` and `:417`; a join with such a literal only at `:2476` |
| `python3 -I -c` with `ntpath`: `abspath("C:\r\seal\threads\x")`; joins of `trail/gate.md` as one argument and split on `/`; their equality with `join(item, "trail", "gate.md")`; `dirname`; `abspath("C:/r/seal/threads/x")`; `relpath` of `realpath`s against `C:\r` | old `C:\r\seal\threads\x\trail/gate.md`, not equal; new `C:\r\seal\threads\x\trail\gate.md`, equal; directory `C:\r\seal\threads\x\trail`; the typed `/` path becomes `C:\r\seal\threads\x`; relative `seal\threads\x\trail\gate.md`; exit 0 |
| `gh run view 40500883542 --json headSha,conclusion` and `--log-failed`, filtered to `FAILED` and assertion lines | head 90d1d702, failure; windows `--splits 4 --group 1` failed `tests/test_broad_gate.py::Test_write_gate_file::test_accepts_a_second_run_in_front_of_the_first` with `assert 'C:\\Users\\r...trail/gate.md' == 'C:\\Users\\r...rail\\gate.md'` |
| `gh pr checks 1092 -R MichaelYcJo/AgenticSeal`, run twice; `gh pr view 1092 --json headRefOid` | head 71c717bf; every pytest job passed, the four windows-latest shards among them, and `lint` and both `arms-grammar` jobs passed; `release` failed |
| `gh run view 40501484379 --log-failed` and `gh run view 40501484402 --job 122179984213 --log` | `release` refused the last round's `target:`, the newest gate run and the guarantee as behind 71c717bf; windows group 1 reported `1285 passed, 16 skipped` |
| `bin/test tests/test_broad_gate.py tests/test_chain_check.py -q -p no:xdist` | exit 0, 569 passed, 1 skipped |
| `ls -d ~/.claude/agentic` and a count of `~/.claude/specseal/` before and after the run | `~/.claude/agentic` did not exist before or after, so nothing was removed; `~/.claude/specseal/` held seven entries both times |
