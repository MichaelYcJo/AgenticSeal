# Guarantee: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Target SHA | 3943873d against 53f21b54 |
| Broad gate | 36f61077 against 53f21b54 |

The base `release/v0.25.0` resolved through `release/v0.25.0@{upstream}` to
`53f21b54` (executed). `trail/gate.md` names `36f61077`, an ancestor of HEAD;
`git log --no-merges --name-only 36f61077..HEAD ^53f21b54` names one commit,
`3943873d`, touching only `trail/gate.md` (executed). `seal pr-body --check`
on the body file exits 0, with the installed command and with the tree's
`bin/seal` (executed).

## Claims re-run

Each `seen red` was re-run in a scratch clone at `3943873d` with every
changed non-test file restored from `53f21b54` and `skills/core/SKILL.md`
removed, by `.venv/bin/python -m pytest -q -p no:xdist -p no:cacheprovider
<ids>`; the same ids were first run in that clone at `3943873d` unchanged,
18 passed, exit 0. The clone was removed afterwards.

| Claim | Source | Command | Result |
|---|---|---|---|
| `test_the_sentence_names_the_core` seen red before the code | `trail/phases/phase-1.md:88-92` | the at-base run, `tests/text/test_every_agent_reads_the_contract.py::test_the_sentence_names_the_core` | holds: red at base (`FileNotFoundError` on `skills/core/SKILL.md`), green at HEAD |
| `test_a_dropped_or_reordered_core_is_caught` seen red before the code | `trail/phases/phase-1.md:88-92` | the case's checker is `shape_problems` in its own module, so restoring code from base leaves it green (1 passed); re-run with `shape_problems`'s list check set back to base's `skills != ["agent-contract"]` | holds: red (`assert False` on the dropped list), green at HEAD |
| `test_this_repository_imports_no_core_and_names_the_tree_copy` seen red (S3) | `trail/phases/phase-1.md:92-94` | the at-base run | holds: red, "CLAUDE.md does not name the core" |
| `test_the_core_names_where_the_routing_question_is` seen red | `trail/phases/phase-1.md:95-96` | the at-base run, `tests/text/test_review_axes.py::test_the_core_names_where_the_routing_question_is` | holds: red at base, green at HEAD |
| The phase-2 installer cases (`test_the_block_is_one_import_of_the_core_and_no_rule`, `test_install_sh_warns_when_the_core_it_imports_is_not_there`, `test_install_sh_says_nothing_when_the_core_is_there`, `test_both_scripts_default_to_the_config_directorys_file`, `test_install_sh_has_no_project_scope`, `test_install_sh_replaces_an_older_block_from_the_template`) seen red, each on its own assertion | `trail/phases/phase-2.md:210-224` | the at-base run, the six ids of `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py` | holds: all six red, each on its own assertion (the old eight-bullet block; no warning; the old overlap loop's five `[warn]` lines; no file under `CLAUDE_CONFIG_DIR`; `--project` exits 0; the old block's text) |
| The "the core arrived" assertion seen red against the old update step | `trail/phases/phase-2.md:218-220` | the at-base run, `tests/behaviour/test_release_hygiene.py::test_update_tells_the_user_when_the_preset_block_changed` | holds: red, "the update command does not say the core arrived" |
| The seven meter cases seen red against the committed meter; four of them were renamed after round 3 (`ab614222`) | `trail/phases/phase-3.md:319-334`; `trail/rounds/round-4.md` | the at-base run, `tests/skills/test_payload_meter.py::Test_imports_of` (four cases, current names) and the three `Test_measure` import cases | holds: all seven red at base (`imports_of` absent; the pair as two flat rows), all green at HEAD |
| `bash install.sh` by hand writes the three-line block, warns on a missing core, and `--project` exits 1 | `trail/phases/phase-2.md:239-246` | `bash install.sh <scratch>/inst/CLAUDE.md`; `bash install.sh --project`; `bash install.sh <scratch>/inst2/CLAUDE.md` with the core planted beside it | holds: exit 0, the markers and the `@` line, the `[warn]` naming the path; `[error] Unknown option --project`, exit 1; no `warn` line with the core present |
| The payload figures in the orchestrator's part of the body, measured at the gate's HEAD | the pull request body, `## Not from the records` *The core's cost* | `HOME=<scratch>/home-before bin/seal payload --root <git archive 53f21b54>`; `HOME=<scratch>/home-after bin/seal payload` with `36f61077`'s block and `git archive 36f61077` at `plugins/marketplaces/agenticseal` | holds: before 29,711 / 32,373 / 29,304 / 29,070 / 22,790 B, after 36,583 / 39,245 / 36,176 / 35,942 / 29,662 B, the core 6,749 B (2,109 tokens), the pair 7,618 B to 7,704 B, the user share 1,786 B to 6,848 B ("about 6,800") |
| Every `## Removes` row of `frame/design.md` stands nowhere in the tree | `frame/design.md:239-253` | `cat templates/setup/claude-md-block.md`; `grep` over `install.sh`, `README.md`, `README.ko.md`, `skills/preset-setup/SKILL.md`, `skills/update/SKILL.md`, the orchestration row and the two docstrings; `git grep` on the nine removed case names outside `seal/threads` | holds: the block is the markers and one `@` line; `CLAUDE.md` holds only *The core*; no `--project`, scope prompt or overlap loop in `install.sh`; no "pick ONE", `--project` or "loaded every turn" in either README; no scope or classification step in `preset-setup`; no `--project` or overlap paragraph in update step 4; no `claude-md-block` in the three reworded places; none of the nine case names. The installer update case replaces the `@` line to make its stale block (`:175`), as the row says |
| The removal the changelog names, `bash install.sh --project`, is gone | `changelog.md:3` | the by-hand run above | holds |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | the core moves whole to `skills/core/SKILL.md` with one added routing sentence; every agent preloads `core` then `agent-contract`; the block is one relative `@` line; `CLAUDE.md` here imports nothing and says which copy governs; `install.sh --project` goes; the meter follows `@` lines; Q1 answered A1 by the owner, Q2 open | the issue's Done-when and both constraints; the tree at every *Scope* item and *Removes* row (read, and the rows above) | none. Its `## Rule changes` rewrite `docs/`, which the diff does not touch, as the policy root is the settle's |
| the build | four phases at `5a283bd8`, `d58605ee`, `a7329570`, `0c1144ef`; three divergences from the frame (`uninstall.sh`'s default, the option refusal, two cases keeping their home half), each in `gaps.md` | the diff (read); the sampled `seen red` and `executed` claims (rows above); `gaps.md` *Where spec and implementation diverged* | none. Phase records give the measurements and case names of their own commits, and round 4 judged the renamed names no finding |
| the last round | round 5 at `a63a9b4a`: no finding; the `.test_durations` commit is the CI artifact byte for byte and prices every case | rounds 3 and 4, which also opened nothing; `trail/gate.md` at `36f61077` | none |
| the changelog | the core arrives in every agent and session; the block is one line; the old block's rules stand in their homes; `install.sh --project` is gone; the user share grows by about 1,570 tokens; an agent reads the core twice, about 2,100 tokens per spawn, and both paths stay | the tree (read); `gaps.md` *Not done*; the measured 5,062 B (1,582 tokens) and 6,749 B (2,109 tokens), each within 1% of its approximate figure | none |
| the orchestrator's part of the pull request body | `Closes #1177`; the before and after payload table at the gate's HEAD; the leftovers in #1183, #1184, #1185 and a comment on #1148; how the run went | the re-measured figures (row above); #1183, #1184 and #1185 open with titles matching their lines, and the #1148 comment of 2026-10-29T14:44:08Z (executed `gh issue view`); rounds 4 and 5 on the two post-round commits | none |

Verdict: sealed
