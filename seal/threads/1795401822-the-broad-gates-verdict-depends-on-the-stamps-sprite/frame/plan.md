# Implementation Plan: 1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite

## Technical context

The tree as read at `ee8a72583`.

`skills/verify/scripts/broad_gate.py` loads `skills/verify/scripts/seal_stamp.py` for the panel's text rules and the head line's composer (`design.md` G5). It never draws, yet the load executes `seal_stamp.py:291`, which reads the disc's mark sprite and raises on a malformed one (G4). `broad_gate.py#sibling_module` (`:207-223`) exists to turn that raise into exit 2 (G6). `seal_stamp.py` also holds two rules for whether two spellings name one commit, which disagree on short, uppercase and non-hex spellings (G11).

The work moves the sprite's read into `build()`, removes the wrapper and the arms it alone fed, and makes `ref_is_commit` answer through `_same_commit`. The constraints are three. `seal_stamp.py` runs under the `Stop` hook on whatever `python3` the harness finds, so it stays Python 3.9 syntax (`lib/sibling.py`'s docstring). The stamp's `--stop` must still exit 0 whatever it meets (`docs/checks/the-stamp.md` *The stamp*). The gate and the stamp keep one set of text rules (`broad_gate.py:190-194`, `seal_stamp.py:469-473`).

Failure scenarios of the chosen approach, six months on:

- A later edit to `seal_stamp.py` adds another read at import, a palette file say, and the gate's verdict depends on a decorative file again. S1's case reads the sprite alone and does not catch it. The reviewer of that edit is who catches it, from the module docstring's statement that the broad gate imports the text rules from here.
- A person edits the sprite and leaves it malformed. `seal stamp --guarantee` queues the stamp, `--stop` draws nothing and says nothing, and only `seal stamp --from` names the fault. `## Rule changes` states that limit in `docs/checks/the-stamp.md`.
- A module the gate loads raises while it executes. With the wrapper gone, the gate ends in a traceback at exit 1, which the gate's exit codes read as failed. Any other exception in the gate's code does the same today, and the traceback names the module. The exception is `chain_check.py`, which `#rounds_rows` loads inside its own `except (Exception, SystemExit)`: its raise leaves the rounds count alone and the run goes on, the rule `Test_rounds_rows.test_refuses_to_stop_a_run_where_the_check_will_not_load[raises]` pins.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. `build()` reads the sprite when it draws, and nothing reads it at import | A later read at import couples the gate again, and S1 does not see it (*Technical context*). A malformed sprite queues at `--guarantee` and draws nothing at `--stop` | Chosen. It removes the cause the issue names, the import executes definitions alone afterwards (`design.md` G3), and the stamp's own commands then refuse in one line (G10) where they ended in a traceback |
| B. The text-panel helpers move to a module both scripts import, and the disc drawing stays in `seal_stamp.py`. This replaces the structure in which the gate loads the stamp's module | The panel's text rules, `text_lines` with its title constants, `TWIN_ASCII`, `sealed_names`, `ref_is_commit` and `is_utf8` leave `seal_stamp.py`, their cases leave `tests/skills/test_seal_stamp.py` for the new module's test file, and the docstrings of both scripts that cite them move. `seal_stamp.py` still reads the sprite at import, so the sealer's `seal stamp --guarantee` still ends in a traceback on a malformed sprite. The diff meets #1573's edits of both scripts in more places | Rejected. The premise that keeps the structure is checked: the gate and the stamp share these rules on purpose, so that both write a row by one set of rules (`broad_gate.py:190-194`, `seal_stamp.py:469-473`), and after A importing the shared module runs nothing but definitions (G3). Nothing is left that a second module would separate |
| C. The read stays at import and is caught there: `SPRITE` is `None` on a malformed file, and `build` raises | A module constant that may be `None`, and a second place that says what a malformed sprite means, beside `read_sprite` | Rejected. A reads the file where it is used and needs neither |
| D. `sibling_module` keeps its `except Exception` with a general reason: any module that raises while it loads ends the gate at exit 2 in one line | The wrapper's record is the sprite alone (G6). It is the plugin's only such wrapper (G7), so it stays as text every reader of the gate's loader reads, for a case no designed module produces | Rejected under `skills/core/SKILL.md` *The rule a mechanism is kept against*. Removing it costs the exit 1 of *Technical context*'s third scenario |
| E. One rule at git's floor of four characters | A refusal record then matches a SHA on four characters, and a false match skips a `sealed` that drew, so the work item's stamp is drawn twice. `seal_stamp.py#record_refusal`'s docstring ranks that failure worse than a stamp missed. It also contradicts `docs/checks/the-stamp.md:75-77`, which would need a rule change | Rejected. The floor of seven costs one thing: a `--base` typed as 4 to 6 hex characters prints `<ref> @ <commit>`, the commit said twice at two lengths |
| F. One rule compared case-sensitively | `--base EE8A725` keeps printing `EE8A725 @ ee8a7258` (G12), and `refused_here` would refuse the `DEADBEE` its case accepts (`tests/skills/test_seal_stamp.py:1257`) | Rejected. git resolves an uppercase spelling as the same commit (G12), so the rule folds case |
| G. One phase for the whole work | A crafter's spawn and one verifying read are saved, and a regression in the same-commit rule then reaches the review mixed with the wrapper's removal | Rejected. The two *Done when* lines touch different units, and each phase below is one of them |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `design.md` *Scope* items 1, 2, 3 and 4 | `bin/test -q tests/skills/test_broad_gate.py tests/skills/test_seal_stamp.py` passes. The cases of S1 and S2 are each seen red against `ee8a72583`. `git grep -n -w SPRITE -- skills tests` prints nothing; at `ee8a72583` it prints the lines `design.md` G16 lists, which *Scope* item 1 changes. The two searches of S4 print nothing. `git grep -n seal-mark -- skills/verify/scripts/broad_gate.py` prints nothing; at `ee8a72583` it prints `:113`, which *Scope* item 4 rewrites | `385ee7e2f` |
| 2 | `design.md` *Scope* item 5 | `bin/test -q tests/skills/test_seal_stamp.py tests/skills/test_broad_gate.py` passes. The case of S3 is seen red against `ee8a72583` at the pair `bbb2` and `bbb2222`. S3's search prints one line, in `_same_commit`. `git grep -n -F '{4,40}' -- skills/verify/scripts/seal_stamp.py` prints nothing; at `ee8a72583` it prints `:712`, which *Scope* item 5 removes | |

## Overlap with the release

The spawn names #1573 and #1579. Both frames were read at their checkouts' HEADs with `git show`, with each branch's diff against `origin/release/v0.38.6` (`design.md` G19). The merge order they give is #1579, then this work, then #1573.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1573, every git and `gh` call runs through `lib/gitcmd.py` | `skills/verify/scripts/broad_gate.py`. #1573's *Scope* item 7 rewrites `git` (`:240-250`), drops `repo_root` (`:253-255`) and has `main` catch `gitcmd.Failed`; its phase 5, which builds that item, has an empty Status cell at `019751544`. This work's *Scope* item 4 rewrites `git`'s and `gitcmd_module`'s docstrings and removes `main`'s `except Refused` around `repo_root` (`:2259-2264`), so the two meet on those lines. `skills/verify/scripts/seal_stamp.py`: #1573 changes `_git` and `:1328`, and this work changes `read_sprite`, `build`, `HEX_REF`, `ref_is_commit` and `_same_commit`, no unit of #1573's. `tests/skills/test_broad_gate.py#Test_main`: #1573 adds cases for `Failed`, and this work removes two | this work (#1582) | This work is two phases and the smaller diff, so it is likelier to be sealed first. Four of #1573's six phases have empty Status cells at `019751544`. Where #1573 merges the base before its phase 5, that phase's crafter writes `main` and `git` over the shape this work leaves, and the integration falls inside rounds #1573 spends anyway. Where #1573's phase 5 lands on its branch first, the same lines are resolved in the merge of the base inside the later item's rounds, which `routing.md` already assigns |
| #1579, per-spawn files carry text their reader never acts on | `skills/verify/scripts/broad_gate.py`. #1579 re-points two citations to `skills/code-review/gate-to-pull-request.md`: `moved_line`'s docstring (`:477`) and `gate`'s comment (`:2058`). This work edits neither line. #1579 also moves the paragraph of `skills/code-review/orchestration.md:533` that `design.md` *Scope* leaves out | #1579 | #1579 has two of its three phases closed (`236d3c5e6`), so it is likelier to be sealed first. The two changes share no line, so either order costs one clean merge of the base |

## Operational impact

No migration, environment variable or dependency. What a person sees changes in three places, each listed in `design.md` *Data & interfaces*: two spellings of `--base` print differently on the gate's head line and `base` row, `seal stamp` and `seal stamp --from` beside a malformed sprite exit 2 in one line where they exited 1 in a traceback, and a module that raises while the gate loads it, other than `chain_check.py`, ends the gate at exit 1 where it ended at exit 2. The version does not move in this pull request: `.claude-plugin/plugin.json` reads `0.38.6` on the base already (executed: `git show f2a664eb8:.claude-plugin/plugin.json`, the base this branch was cut from).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
