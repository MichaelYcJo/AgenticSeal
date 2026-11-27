# Guarantee: 1795759278-the-cores-margin-depends-on-the-path

Audited on 2026-11-27 by the sealer, at `b72c94c9b` against the base
`release/v0.39.3`, whose upstream, `origin/release/v0.39.3` and local branch
all resolve to `86f98018c` (`executed`: `git rev-parse --verify --quiet` on
the three refs). The gate record `trail/gate.md`'s last block names
`run: 72b34e712 against 86f98018c`. `72b34e712` is an ancestor of HEAD, and
the one commit after it, `b72c94c9b`, touches only
`seal/threads/1795759278-the-cores-margin-depends-on-the-path/trail/gate.md`
(`executed`: `git log --no-merges --name-only 72b34e712..HEAD ^86f98018c`).
`bin/seal pr-body seal/threads/1795759278-the-cores-margin-depends-on-the-path --body <scratchpad>/1795759278-the-cores-margin-depends-on-the-path/body.md --check`
exited 0, printing that the body is `pr.md` above `## From the records` and
the records' text below it (`executed`). Git carries no `seal/parity.json`,
so no comparison with an original is owed. `seal/config.json` names English
for both language keys, and no `pr.<lang>.md` stands.

The broad gate's pass is the orchestrator's account: the sealer read
`trail/gate.md` at HEAD and ran nothing broad (`read`, contract rule 2).

This is the sealer's second audit of the work item. The first, at
`ed2a7c48a`, was never committed and stands in no `guarantee.md` of the
tree, so this file holds one block. Since `ed2a7c48a` the commits
`7a5e970c1`, `ca3d5c301`, `848397bc7`, `72b34e712` and `b72c94c9b` change
`hooks/core-start.py`'s docstring, `frame/design.md` *Data & interfaces*,
three rows of `frame/plan.md` *Judgments of the run*, `trail/rounds/round-4.md`
and `trail/gate.md`, and nothing under `lib/`, `tests/`, `skills/`,
`.claude-plugin/`, `README.md`, `README.ko.md` or `CONTRIBUTING.md`
(`executed`: `git diff --stat ed2a7c48a..HEAD`, and
`git diff --name-only ed2a7c48a..HEAD` over those paths printing nothing).
The claims the first audit re-ran rest on files no later commit touched.
They are carried below with the date and commit of their run. The narrow
modules, the one claim the hook's file bears on, were re-run at HEAD.

## Claims re-run

Each claim ran in a `git clone --no-local` of this worktree under
`<scratchpad>/1795759278-the-cores-margin-depends-on-the-path/seal/at-base/`,
whose root is 176 characters long. After each run every file was restored by
`git checkout <commit> -- <path>`, and the tree under audit was not changed.

| Claim | Source | Command | Result |
|---|---|---|---|
| The plan's three narrow modules pass at HEAD in a clone deeper than 70 characters | `frame/plan.md` *Phases*, row 1; `frame/design.md` S1 | the clone checked out at `b72c94c9b`, then `bin/test tests/lib/test_core.py tests/hooks/test_core_start.py tests/skills/test_payload_meter.py -q -p no:xdist` | Holds. 76 passed, exit 0 (`executed` at `b72c94c9b`) |
| `hooks/core-start.py`'s rewritten docstring says what the hook prints in each branch | `hooks/core-start.py:2-15`, `7a5e970c1`; `frame/design.md` *Data & interfaces*, its last bullet | read against `lib/core.py#rendered` and `#output` and `hooks/core-start.py:46-48` | Holds. `output` returns "" with no root, otherwise `rendered`. `rendered` returns the whole output under `CAP`, `TOO_LONG`, a newline and the closing line from `CAP` on, and `MISSING` where the file cannot be opened. The hook writes the text and a newline. The docstring names all three and the empty case (`read`) |
| S1: the cap's case of the old code fails in a deep clone, and the new case passes there | `trail/phases/phase-1.md`, the bullet **Seen red**, S1 | `lib/core.py` and `tests/lib/test_core.py` restored from `86f98018c`, then `bin/test "tests/lib/test_core.py::Test_module::test_the_trees_core_stays_under_the_harness_cap" -q -p no:xdist`; then both restored and the same command | Holds. Old: exit 1, `AssertionError: 10318` at `tests/lib/test_core.py:243`, which is 3 × 176 + 9,790. New: 1 passed (`executed` at `ed2a7c48a`, files untouched since) |
| S2: a core 65 characters longer passes the case, and 66 fails it with the length, `CAP` and `ROOT_ROOM` in the message | `trail/phases/phase-1.md`, the bullet **Seen red**, S2 | `skills/core/SKILL.md` appended with 65, then 66, `y` characters, the same case run after each | Holds. 65: 1 passed. 66: exit 1, `the hook's whole output is 10,000 characters at a plugin root of 100 characters (lib/core.py#ROOT_ROOM), against a cap of 10,000 (lib/core.py#CAP)` (`executed` at `ed2a7c48a`, files untouched since) |
| Every new and rewritten case fails against `lib/core.py` unchanged | `trail/phases/phase-1.md`, the bullet **Seen red**, its first sentence | `lib/core.py` restored from `86f98018c`, then `bin/test tests/lib/test_core.py tests/hooks/test_core_start.py -q -p no:xdist` | Holds. 10 failed and 20 passed. The failures are the eight new or rewritten cases of `Test_closing`, `Test_whole` and `Test_rendered`, the cap's case and the hook's clone case, each on `AttributeError` for `closing`, `whole` or `ROOT_ROOM` (`executed` at `ed2a7c48a`; `tests/hooks/test_core_start.py` and `lib/core.py` untouched since) |
| Mutation (2): treating the comparison's `OSError` as the plugin's own core is red over the case for a core at another path | `trail/phases/phase-1.md`, the bullet **`seal mutate`**, row (2) | `own = False` at `lib/core.py:171` replaced by `own = True`, the replacement asserted to match once, then `bin/test tests/lib/test_core.py -q -p no:xdist` | Holds. 1 failed, `Test_rendered::test_accepts_a_core_at_another_path_with_the_running_plugins_root_once`; 22 passed (`executed` at `ed2a7c48a`, files untouched since) |
| At the base, the installed plugin's own output at a 63-character root is 9,979 characters, and 9,980 with the hook's newline | `changelog.md`, the first `### Fixed` entry; `trail/phases/phase-1.md`, the bullet **Measurements** | `<scratchpad>/…/seal/probe/test_tmp_measure.py`, run with the clone's `.venv/bin/python -I`. With `lib/core.py` and `.claude-plugin/plugin.json` of `86f98018c`, it renders the clone's own core at its 176-character root and replaces the three roots with three of 63 characters | Holds. 10,318 at 176, the root counted 3 times. 9,979 at 63, and 9,980 with the newline `hooks/core-start.py:48` writes (`executed` at `ed2a7c48a`; the newline `read` at HEAD) |
| At HEAD the same output is 9,897 at 63 and 9,934 at 100, and it prints whole up to a root of 165 | `changelog.md`, the first `### Fixed` entry; `frame/plan.md` *Judgments of the run*, the row on the seven summary sentences | the same probe, `core.whole` on the tree's core at roots of 63, 100, 165 and 166 | Holds. 9,897, 9,934, 9,999 and 10,000 (`executed` at `ed2a7c48a`; `lib/core.py` and `skills/core/SKILL.md` untouched since) |
| S7: the commit that added `changelog.md` moved `.claude-plugin/plugin.json` to the milestone's version | `frame/design.md` S7; `routing.md` *Why this way*, **The version move** | `git log --diff-filter=A --format=%h -- <item>/changelog.md`, `git show --stat bb7168b57`, `gh issue view 1641 --json milestone` | Holds. `bb7168b57` changes `.claude-plugin/plugin.json` and `changelog.md`, the version reads `0.39.3`, and the milestone is `release: 0.39.3` (`executed` at `ed2a7c48a`) |
| Nothing of `## Removes` rows 1 to 4, or of the changelog's removal of the measure at the checkout's path, stands in the tree | `frame/design.md` `## Removes`; `changelog.md`, the third `### Fixed` entry | `git grep -n -e 'START.format' -e 'os.path.join(plugin_root, \*ORCHESTRATION' -e 'os.path.join(plugin_root, \*REVIEW' -- lib`; `git grep -n -e 'start_line' -e 'core.origin(ROOT, ROOT)' -e 'core.rendered(path, ROOT)' -- tests`; `git grep -n -e 'spelled absolute' -- . ':!seal/threads'` | Holds. The first and third print nothing. The second prints only `tests/lib/test_lines.py:643-651`, a parameter named `start_line` of an unrelated helper (`executed` at `ed2a7c48a`; `lib/`, `tests/` untouched since, and `hooks/core-start.py`'s new docstring holds none of the words) |
| `## Removes`, row 5: an output of `CAP` characters or more is no longer returned | `frame/design.md` `## Removes`, its last row | read `lib/core.py#rendered` at HEAD | Holds. `rendered` returns `out` only where `len(out) < CAP`, and `TOO_LONG` with `closing(plugin_root)` otherwise (`read`) |

Not re-run: the mutation rows of `trail/phases/phase-1.md` other than (2);
the `payload_meter.py` seen red and its note's mutant, which rounds 2 and 3
re-ran; round 4's `ruff` runs on `hooks/core-start.py`; the phase's boundary
set. The full suite, lint and format are `unverified` here and answered by
the orchestrator's broad run that `trail/gate.md` records at `72b34e712`.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `frame/design.md` *Scope* items 1 to 9. The closing line names its two files relative to the plugin's root, and the root stands once where the core is printed. An output that would reach `CAP` becomes `TOO_LONG` above the closing line naming the running root. `ROOT_ROOM` is 100, and the cap's case measures at a root of that length. `seal payload` marks a `named` hook row. The two READMEs and `CONTRIBUTING.md` gain their sentences, and the version moves. *Data & interfaces*, folded at `ca3d5c301`, says `hooks/core-start.py` is unchanged in code and interface and its docstring says what `rendered` returns past the cap | The issue's two *Done when* lines: the case measures at a root of fixed length, and `CONTRIBUTING.md` states the weighing. An installed plugin's root now stands once, the installed margin is measured, and a root past 165 characters is told to open the core. The diff: each item stands where it says, and `git diff 86f98018c...HEAD -- hooks/` changes only the docstring (`read`) | none |
| the build | The diff and `trail/phases/phase-1.md`. `lib/core.py` gains `closing`, `whole`, `ROOT_ROOM`, `TOO_LONG`, `OWN_ROOT` and `RUNNING_ROOT`. The cases of *Scope* items 5, 6 and 9 are added, and `7a5e970c1` rewrites the hook's docstring | The design, the claims re-run above, and `frame/plan.md` *Judgments of the run* on the phase's two departures. `routing.md` reads `crafter`, and the one phase whose Status holds a commit, phase 1 at `bb7168b57`, has `trail/phases/phase-1.md` (`read`) | none |
| the last round | `trail/rounds/round-4.md`, target `848397bc7`, reading `9389704ec..848397bc7`. It opens no finding and confirms the docstring, the fold and the repair row's citation. It takes the judgment that the summary sentences stand, extends its grounds to `docs/layout/the-record-layout.md:181` and `docs/running/measuring-a-run.md:141`, and carries Q1, the Windows join and the trailing newline as not judged | The tree. After `848397bc7` only `trail/rounds/round-4.md` and `trail/gate.md` change (`executed`: `git diff --name-only 848397bc7..HEAD`). No finding of it reads `fixed`, so no fix falls to the sealer as its reader. The paragraphs its rows cite stand at `skills/code-review/orchestration.md:318` and `skills/implement/orchestration.md:83` (`executed`: `grep -n`) | none |
| the changelog | `changelog.md`: three `### Fixed` entries, the measured lengths dated 2026-11-27 with the issue's installed figures corrected, and the version move to 0.39.3 | The measurements re-run above, the design's *Scope* items 1, 2, 5, 7, 8 and 9, and the version at `bb7168b57`. The docstring repair changes no behaviour a release note states | none |
| the orchestrator's part of the pull request body | `pr.md`: three quotes of `frame/plan.md` *Operational impact*, the prefix row's judgment and its grounds, and `Closes #1641.`. Its three new rows of *Judgments of the run* order the repair, fold the frame line, and keep the seven summary sentences | Each quote stands word for word at its coordinate in `frame/plan.md`, and `pr.md` is unchanged since `ed2a7c48a` (`read`). The repair row orders a round, the broad run and the sealer again, which is what `trail/rounds/round-4.md` and the gate record's second block show done. The summary-sentences row's grounds, "a session receives the core whole at every plugin root up to 165 characters", hold by the measurement above. `routing.md` *Why this way* describes a change to how the core's size is measured and to what every session receives, which is what the diff changes | none |

Three questions stay unmeasured, and the guarantee does not cover them.
- **Q1:** whether a fresh session resolves the closing line's relative paths under the plugin's root. It is a question about how a session behaves (`gaps.md`, its first row), and the owner or the orchestrator answers it.
- **The Windows join:** whether the `/` join holds on Windows. CI's Windows legs answer it at the pull request (`gaps.md`, its second row).
- **The trailing newline:** whether the harness counts the newline the hook writes after an output of 9,990 to 9,999 characters. It stands in `trail/rounds/round-4.md` *Not judged*, with the repository owner as its answerer, and not in `gaps.md` (`read`). It bears only on a plugin root of 157 to 165 characters.

```seal
target: b72c94c9b9331a4b70e08a123c36b5df9036ec59 against 86f98018c960314eaa9c9e7121d007eb8ef42c12
Verdict: sealed
```
