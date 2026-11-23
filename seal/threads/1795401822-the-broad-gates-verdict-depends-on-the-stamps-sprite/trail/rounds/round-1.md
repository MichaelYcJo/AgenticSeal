# Review round 1: 1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite

```seal
target: 6b6ef8ba906c6eb516eb5aec0c6f76e221ed1e0b against origin/release/v0.38.6
```

This is a finding round over `git diff f2a664eb8..6b6ef8ba9`, the branch against `origin/release/v0.38.6`. No earlier round exists, so no verdict was carried. The probes ran in a `git clone --no-local` of the branch at the target, under this round's scratch directory. No `seal/parity.json` is declared, so no parity comparison was owed. `seal/config.json` has no `Pact` key, so no pact anchor was read.

Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md`. `Commit and pull request language` is English, so no `pr.<lang>.md` is owed and none stands.

Facts carried from the frame and not established again: G3's walk of what importing `seal_stamp.py` executes, G11's answers of the two old rules at `ee8a72583`, G12's reading of how git resolves short and upper-case spellings, and G19's reading of #1573's and #1579's frames. The spawn forbids opening those two checkouts, so `## Not judged` holds the overlap rows. Everything else below was opened or run this round.

Axes walked. Inputs: the spellings `ref_is_commit` and `_same_commit` take (probe rows). Exclusions and boundaries: the floor of 7, the ceiling of 40, case, `None` and `""`. Error paths: each entry of `seal stamp` beside a malformed sprite, and an absent one. State transitions: a values file stays pending, or is claimed. Concurrency: the sprite is now read on every draw. Security: `SPRITE_PATH` is still fixed beside the script, so no new input crosses a boundary. This change also has two axes of its own. One is the gate's exit codes once the wrapper is gone. The other is the statements of the exit codes in docstrings.

## Findings

### 1. `seal stamp`'s exit-code list does not name the new exit 2 for a malformed sprite

```seal
severity: should
location: `skills/verify/scripts/seal_stamp.py:79-84`, `skills/verify/scripts/seal_stamp.py:1563-1567`
evidence: executed `bin/test tests/skills/test_tmp_round1_sprite.py -q -s -p no:xdist` in the clone (the `## Probes` row); read `skills/verify/scripts/seal_stamp.py:79-84`, `:1493-1559`, `:1562-1578`, `skills/verify/scripts/broad_gate.py:111-114`
```

Why it matters: before this change, a malformed sprite made `seal stamp` and `seal stamp --from` end in a traceback at import, with exit 1. They now exit 2 with `SPRITE_MALFORMED`'s sentence. `main` catches `ValueError` around `stamp` and `drawn_from` (`seal_stamp.py:1550-1557`). The probe ran the sample, `--shape` and `--from` as processes from a copy of the plugin whose `seal-mark.txt` was cut to one line. Each exited 2 with stdout empty and that sentence on stderr. `frame/design.md` *Data & interfaces* states this exit, and `changelog.md` states it to the release's readers.

The module docstring's `Exit codes` paragraph is the one place this file lists what exit 2 means. It says "2 refused — a values file that is unreadable or drawn already, or a guarantee that could not be read" (`:79-81`), and the diff left it unchanged. For the gate, *Scope* item 4 had the same kind of list rewritten (`broad_gate.py:111-114`). The stamp's list gained a cause and was not touched. `drawn_from`'s docstring has the same gap. It lists the refusals as "a file drawn already, unreadable, or out of shape" (`:1565`), and it now also raises the sprite's `ValueError` through `stamp`, before the claim. The last sentence of `:83-84` says a load that fails under the `Stop` hook draws nothing. That is now true of a malformed sprite as well, without any load failing. An agent that edits `main` or `drawn_from` reads these lists to learn which refusals exist, and with this gap it treats the sprite's refusal as an exit nobody designed.

No other document states `seal stamp`'s exit codes (executed: `git grep -n -i -e 'seal stamp.*exit' -e 'exits 2' -- docs skills/verify agents`). `docs/checks/the-stamp.md` gets its sentence through `frame/design.md` `## Rule changes`, at the settle. So the snippet below covers every statement of the fact.

```python
# skills/verify/scripts/seal_stamp.py:79-84
Exit codes: 0 printed, or `--stop` whatever happened · 2 refused — a values
file that is unreadable or drawn already, a guarantee that could not be
read, or, for the sample and `--from`, a disc's mark sprite that is
malformed (`SPRITE_MALFORMED`); nothing was written on 2. An interpreter
below the floor never reaches this file through `seal stamp`:
`lib/launch.py` refuses `seal` with 2 first. The `Stop` hook runs it with
whatever `python3` the harness finds, and a load that fails there, or a
malformed sprite, draws nothing.
"""

# skills/verify/scripts/seal_stamp.py:1563-1567
    """The lines for the values file at `path`, which is claimed before they
    are returned. Raises `ValueError`
    with a refusal for a file drawn already, unreadable, or out of shape, or
    for a disc's mark sprite that is malformed — and every refusal comes
    before the claim, so a file refused for its content or for the sprite is
    still there to be drawn once it is repaired."""
```

## Confirmations

What matched: *Scope* items 1 and 2. `SPRITE = read_sprite(SPRITE_PATH)` is gone, and `build` reads `read_sprite(SPRITE_PATH)` on each call (`seal_stamp.py:319`). Its docstring names the read (`:293-296`). `git grep -n -w SPRITE -- skills tests` prints nothing and exits 1 (executed). `Test_main.test_a_malformed_sprite_leaves_the_verdict_and_the_report_as_they_were` (`tests/skills/test_broad_gate.py:2118`) passes in the narrow run (executed). It runs the copy's gate as a process, once with the shipped sprite and once with a cut one, and compares the exit and stdout. Phase 1 says it saw the case red against `ee8a72583` and red under the mutant that puts the read back at import. This round did not run those, and read the case's assertions against that claim: the cut run's `returncode == 0` is the line the mutant breaks.

What matched: *Scope* item 3, and the `gaps.md` row this round was named for. `seal stamp` with no argument and `seal stamp --shape`, beside a cut sprite, each exit 2 with the sprite's one sentence and empty stdout. `seal stamp --guarantee` over the local-mode fixture's sealed `guarantee.md` exits 0, prints the queued line and writes one values file. `--from` over that file exits 2 and the file stays pending. `--stop` exits 0 with empty stdout, and the file stays pending (executed, the `## Probes` row). That is what `frame/design.md` G10 and *Data & interfaces* state. The in-process S2 cases at `tests/skills/test_seal_stamp.py:2375` and the `--stop` case below it pass (executed).

What matched: *Scope* item 4. `sibling_module` is gone, and every caller calls `sibling.load` (read: the diff of `broad_gate.py`). S4's two searches print nothing and exit 1, and so does `git grep -n seal-mark -- skills/verify/scripts/broad_gate.py` (executed). `rounds_rows` catches `(Exception, SystemExit)` around the check's load alone (`broad_gate.py:1601-1612`). Phase 1 departed from the first wording of *Scope* item 4 here, and `5d0a4758d` folded that into the frame. The departure stands on the comment's rule and on `test_refuses_to_stop_a_run_where_the_check_will_not_load[raises]`, which the narrow run passed (executed). `main` no longer loads `seal_stamp.py` before parsing. Its only in-process callers are cases (executed: `git grep -n -e 'gate\.main(' -- tests`), and `__main__` still loads the module first (`broad_gate.py:2265`), so a process beside an absent `seal_stamp.py` still exits 2 with `MISSING` before anything runs. `test_refuses_a_copy_without_the_git_helper_in_a_sentence` passes unchanged (executed).

What matched: *Scope* item 5. `HEX_REF` and its comment are gone. `_same_commit` holds each spelling to `SHA_SPELLING`, built from `SHORTEST_SHA` with a ceiling of 40, after lower-casing (`seal_stamp.py:1134-1152`). `ref_is_commit` answers True for `None` and `""` and otherwise answers through `_same_commit` (`:740-748`). S3's search prints one line, `:1152`, and `git grep -n -F '{4,40}'` prints nothing (executed). The probe rows show: `bbb2` is refused; `BBB2222` is accepted against `bbb2222` and the other way round; a 40-character spelling is accepted; a 64-character spelling is refused; a `base` of `None` matches no ref; `sealed_names` prints `ee8a @ ee8a7258` for a four-character ref and the commit alone for `EE8A725` (executed). The ceiling of 40 drops nothing a record can hold, because `lib/fields.py:97`'s `COMMIT` is also 7 to 40. Every spelling that reaches `refused_here` is a recorded target in that grammar, so `docs/checks/the-stamp.md:75-77` still holds for what reaches it (read: `seal_stamp.py:1090-1116`, `:1300-1347`).

What matched: the new cases, read against their groups. `seal layout --pairs` in the clone names three pairs in `tests/skills/test_seal_stamp.py` that this diff touches (executed): `Test_read_sprite`'s two cases, and the new `--stop` case with each of the two older `--stop` cases. Each pair asserts a different fact. The new `--stop` case's world is a pending stamp beside a malformed sprite, and it asserts that the file stays pending, which neither older case asserts. `test_answers_as_a_refusal_record_is_matched` (`:1013`) holds both rules to one answer over S3's pairs. That is a fact `frame/design.md` S3 states, and `Test_refused_here` does not assert it.

What matched: the records. `pr.md`'s one quote stands word for word in `frame/plan.md` *Judgments of the run* (read). Each sentence of `changelog.md` was read against the code and the probe, and each holds. The five removed cases it counts are `Test_sibling_module`'s three and the two of `Test_main` (read: the test diff). The `from:` of `## Rule changes` stands word for word, with whitespace collapsed, at `docs/checks/the-stamp.md:157-159` (read). The version is `0.38.6` on the base and at the target, as *Operational impact* says (executed: `git show f2a664eb8:.claude-plugin/plugin.json`). Each claim of `trail/phases/phase-1.md` and `phase-2.md` checked by search or run this round holds at the target. The searches, the line `:1152`, the pairs and the narrow passes were reproduced. The mutation runs and the seen-red runs were read and not re-run.

What matched: the suite's label. `gaps.md` names the full suite, the lint and the format check as unverified, with the orchestrator as their answerer. The phase records label their boundary runs as executed and name the modules. This round ran `bin/test -q tests/skills/test_seal_stamp.py tests/skills/test_broad_gate.py` in the clone: 406 passed, 1 skipped (executed).

One new failure path was counted and classified as accepted. Under `--stop`, `drawings` draws each block, then claims the files, and then `fitted` draws the claimed blocks again (`seal_stamp.py:1428-1443`, `:662-709`). Each draw now reads the sprite. If a person makes the sprite malformed between the first read and the last, the claimed files raise in `fitted`. `main`'s `except Exception` then prints nothing (`:1525-1531`), and those stamps are claimed but never drawn. Before this change the sprite was read once, at import, so this could not happen. The window is one hook run, and only an edit of the plugin's own file opens it. `docs/checks/the-stamp.md` *The stamp* already ranks a missed stamp as the accepted failure, so this round opens no finding for it.

An absent `seal-mark.txt` makes the sample exit 1 in a traceback, because `read_sprite`'s `open` raises `FileNotFoundError` and `main` catches only `ValueError` (executed, the probe). At the base the same absent file failed at import, also with exit 1. So the stamp's behaviour for an absent sprite is unchanged, and the gate no longer depends on that file at all. The frame covers a malformed sprite and does not name an absent one.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The S1 case on Windows | `tests/skills/test_broad_gate.py:2118`, the `windows-latest` legs of `.github/workflows/test.yml` | CI, on the pull request |
| The full suite, the repository-wide lint and the format check at the target | `seal/config.json` `Broad gate` | the orchestrator, at the broad gate |
| `frame/plan.md` *Overlap with the release*: what #1573 and #1579 change and the merge order. The spawn forbids opening their checkouts, so this round read neither frame | `frame/plan.md` *Overlap with the release* | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/skills/test_seal_stamp.py tests/skills/test_broad_gate.py`, in the clone at the target | exit 0: 406 passed, 1 skipped |
| `bin/test tests/skills/test_tmp_round1_sprite.py -q -s -p no:xdist`, in the clone. The probe copies `lib`, `skills` and `.claude-plugin` into a temporary plugin, cuts its `seal-mark.txt` to one line, and runs the copy's `seal_stamp.py` as a process | no argument: exit 2, stdout empty, stderr the `SPRITE_MALFORMED` sentence ending `(1 lines). Nothing was drawn.` `--shape`: the same. `--guarantee` over the local fixture's sealed `guarantee.md`: exit 0, the queued line, one values file. `--from` over it: exit 2, the same sentence, the file still pending. `--stop` with a `Stop` payload for the fixture's clone: exit 0, stdout and stderr empty, the file still pending. With the sprite removed, no argument: exit 1, a traceback ending in `FileNotFoundError`. `ref_is_commit`: `bbb2` False, `BBB2222` True against `bbb2222` and the reverse, the 40-character spelling True, the 64-character one False, `None` and `""` True, a base of `None` False, `origin/base` False. `sealed_names` prints `ee8a @ ee8a7258` and `ee8a7258` alone for `EE8A725` |
| `bin/seal layout --pairs`, in the clone | exit 0; the pairs in `tests/skills/test_seal_stamp.py` that this diff touches are the three named under `## Confirmations` |
| `git grep` over the plan's and S3's and S4's searches, in the worktree at the target | each prints what `frame/plan.md`'s rows ask: nothing, except S3's one line at `seal_stamp.py:1152` |
