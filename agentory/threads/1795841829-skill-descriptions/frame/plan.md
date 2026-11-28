# Implementation Plan: 1795841829-skill-descriptions

## Technical context

The tree as read at `24c5276f`.

**What the work edits.** The work edits the YAML frontmatter of `skills/agent-contract/SKILL.md`, `skills/code-review/SKILL.md`, `skills/commit-pr-convention/SKILL.md`, `skills/core/SKILL.md`, `skills/implement/SKILL.md`, `skills/legacy-parity/SKILL.md`, `skills/settle/SKILL.md`, `skills/verify/SKILL.md` and `skills/writing-style/SKILL.md`. It also edits the test modules `tests/behaviour/test_chain_hooks_hardening.py` (`#skill_groups` at line 360 and `#test_auto_firing_skills_declare_when_not_to_fire` at lines 554 to 572) `tests/text/test_the_agent_contract_holds_the_universal_rules.py` (the module docstring at lines 39 to 42 and the case at lines 120 to 137) and `tests/behaviour/test_docs_line_wrap.py` (its `COVERED` list). It adds one record under `docs/experiments/` where the measurement step's run is made. No body of a `SKILL.md` changes.

**M1, the measure of the descriptions.** This is the command `frame/design.md` G5 ran. It is run from the worktree's root:

```
uv run --no-project --with pyyaml python -c 'import glob,os,yaml
t=0
for p in sorted(glob.glob("skills/*/SKILL.md")):
    fm=yaml.safe_load(open(p,encoding="utf-8").read().split("\n---\n",1)[0].lstrip("-\n"))
    if fm.get("disable-model-invocation"): continue
    d=fm["description"].strip(); t+=len(d); print(os.path.basename(os.path.dirname(p)),len(d))
print("total",t)'
```

The worktree's `python3` resolves through pyenv to an interpreter without PyYAML (executed: `ModuleNotFoundError`), so M1 runs under `uv` with `--with pyyaml`.

**What the measurement step's run cannot reuse, and why the orchestrator takes it.** The 2026-09-03 method edited the version cache and needed `/reload-plugins` in the main session, because a preloaded body is read at session start and at a reload (`frame/design.md` G8). A new headless session reads its plugins at its start, so `claude -p --plugin-dir <copy>` gives the same reading without a reload (G12). That session is a paid model session on the person's Claude Code credentials. `--bare` cannot stand in for it without `ANTHROPIC_API_KEY` (G12). The session the run starts spawns an agent, `probe:sentinel`, and contract rule 6 withholds spawning an agent from every agent. So the orchestrator takes the run, before it spawns the crafter for phase 1, and no crafter builds it.

**The failure scenario of the chosen approach.** In six months, a session meets a request that a removed `NOT for:` clause would have turned away. Two cases stand: a request to explain how the review chain works, which implement then claims, or a request to review a diff, which verify then claims. The cost is one skill body loaded into context that the request did not need. Nothing records it unless a person notices. *Alternatives considered* row A7 weighs a run that would show it, and `frame/design.md` S7 names the one trigger the issue asks to keep.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 `core` and `agent-contract` take `disable-model-invocation: true`, the issue's first branch, where the measurement step's run shows the preload surviving the flag | Claude Code's documentation says the flag "prevents the skill from being preloaded into subagents" (`frame/design.md` G7). A Claude Code release that holds to its documentation then strips the core and the contract from every agent, with no error and no symptom, which breaks `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* (G1). The saving over A2 is the characters of two short descriptions | Rejected, whatever the run shows. Where the run shows the preload surviving, its record states that the measured behaviour contradicts the documentation, and the new case of `frame/design.md` *Scope* item 4 refuses the flag on a preloaded skill. Where the run shows the preload blocked, A1 cannot be built, as the issue states |
| A2 Both keep `user-invocable: false`, take no new flag, and carry a description of at most two sentences | A model that reads the short description still invokes the skill and loads its body a second time. The description says the file arrives preloaded, which is the signal against that | Chosen |
| A3 Both drop `description`, so the listing falls back to the body's first non-empty line (G7) | The core's first line is `# The core`, which tells a model nothing about what the file holds or that it arrives preloaded. The fallback's rendering in the listing is not measured | Rejected |
| A4 The structure is replaced: the core and the contract leave `skills/` and reach the agents another way, such as text copied into each `agents/*.md` or a hook | A copy in each definition under `agents/` needs a generator or a check to keep the copies in step, which is a thing kept beside the tree. A `SessionStart` hook reaches no subagent (`skills/verify/scripts/payload_meter.py` module docstring, read). The structure is kept on its premise, checked: an agent's `skills:` list is the one mechanism that delivers one file whole to every agent before its first tool call (G1, and G8 run 6) | Rejected |
| A5 Every `NOT for:` clause stays | 1,320 characters (G5) stay in every session's listing, and the issue's third *Done when* line is unmet | Rejected |
| A6 Every `NOT for:` clause goes, the two with a recorded confusion among them | The writing-style clause answers a pull request that shipped with no prefix (G10), and code-review's clause separates it from Claude Code's built-in `code-review`, which stands in the same listing (G6). Two cases go red, `#test_the_writing_style_handoff_names_a_skill_that_ships` and `#test_the_review_skill_names_the_built_in_command_a_person_types` | Rejected |
| A7 A run of the model's choice of a skill decides each removed clause | One headless session per prompt and per clause, at about the 61k tokens a spawn cost on 2026-09-03 (G8). #1076 was closed for the same weighing, with no failure on record asking for the run | Rejected. A clause comes back when a run or a report shows the confusion it names |
| A8 A case or a meter holds each description's length, or the listing's total | A ceiling stored in a test is a count kept beside the tree, and it has caught nothing on the day it is added (`skills/core/SKILL.md` *The rule a mechanism is kept against*). The issue asks for the totals in the records, which M1 gives | Rejected |
| A9 The case that requires a `NOT for` is narrowed to require that each remaining clause names another skill in backticks | The script then encodes the judgment of `frame/design.md` G4. A clause that names a skill with no recorded confusion passes, and code-review's clause, which names the built-in command in words, fails | Rejected |
| A10 The contract-only assertion stays, and a copy of it is added for the core | A skill that a later definition preloads is held only after someone edits the case. The new case of *Scope* item 4 derives the set from `agents/*.md` through `#skill_groups`, so it needs no edit | Rejected |
| A11 The orchestrator writes the `docs/experiments/` record with its run, as part of the measurement step, the second half of the orchestrator's proposal P1 of 2026-11-28 | The record is a file of the tree, and `routing.md` answers `Implementation` with `crafter`, so a record the orchestrator commits is a build the routing gives the crafter. The crafter's phase 1 reads the transcripts at the paths the orchestrator names and writes the record from its own `grep -c`, as contract rule 5 asks of a fact that reaches it in prose | Rejected. The orchestrator takes the run and writes Q1's `Status`, and the crafter writes the record in phase 1 |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 2, 3, 4 and 5, with `changelog.md` and the version move (*Operational impact*). Where the measurement step's run was made, also *Scope* item 1's record under `docs/experiments/`, written from the commands and the transcript paths the orchestrator's spawn names | The record's sentinel counts are the crafter's own `grep -c` of those transcript paths, and the control run shows both sentinels or the record calls the run void. M1 prints a total below 4,860 (S1). The searches of S2 and S3 print what those rows state. The new case is seen red with `disable-model-invocation: true` added to the core and green without it (S4). `uv run --no-project tests/run_tests.py -q tests/behaviour/test_chain_hooks_hardening.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/lib/test_core.py tests/text/test_no_passage_is_pasted_into_a_second_file.py` passes (S5). The last module counts passages that two files share, and the core's and the contract's descriptions each hold a sentence opening `Not a command to run`, which goes | ee1c63a3 |

**The measurement step, before phase 1.** The orchestrator takes `frame/design.md` *Scope* item 1's run before it spawns the crafter for phase 1, because contract rule 6 withholds the run's agent spawn from every agent (*Technical context*). It works under its own scratch directory, `<scratchpad>/1795841829-skill-descriptions/orchestrator/`, and edits nothing in the worktree. It writes Q1's `Status` where the run answers Q1, and it names in phase 1's spawn prompt each command it ran and each transcript path the result stands in. The step is no row of *Phases*, because it closes with no commit of the build.

1. It makes two clones of the worktree at the branch's tip with `git clone --no-local`: `flag-off/` and `flag-on/`.
2. In each clone it makes four edits:
   - `.claude-plugin/plugin.json`'s `name` becomes `probe`, so the clone's skills and agents stand apart from the installed `agentic`.
   - A definition `agents/sentinel.md` is added, whose `skills:` list holds `core` and `agent-contract`, whose `tools:` holds `Read`, and whose body asks the agent to answer from the text it received at startup and to use no tool.
   - One line `SENTINEL-CORE-<random>` is appended to the body of `skills/core/SKILL.md`.
   - One line `SENTINEL-CONTRACT-<random>` is appended to the body of `skills/agent-contract/SKILL.md`.
3. In `flag-on/` alone, `disable-model-invocation: true` is added to both frontmatters.
4. It makes an empty repository with `git init` under the scratch directory as the session's working directory. That repository holds no `agentory/` root, so no core hook prints the core into the session.
5. For each clone it runs `claude -p '<prompt>' --plugin-dir <clone> --settings '{"enabledPlugins":{"agentic@agenticseal":false}}' --max-budget-usd 2 --output-format json` from that directory. It records each run's PID. The prompt asks the session to spawn `probe:sentinel` with one question: quote every line of its startup text that begins with `SENTINEL-`, or answer `NONE`. The prompt also asks the session whether `probe:core` and `probe:agent-contract` stand in its own skill listing. The `enabledPlugins` key and its plugin identifier are unverified, and the control run tests them.
6. It reads the result exactly. For each run, the `session_id` in the JSON output locates the transcripts, `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/projects/<working directory with slashes as dashes>/<session_id>/subagents/*.jsonl` (`skills/verify/scripts/session_cost.py` module docstring, read). `grep -c` of each sentinel in those files is the result, and the agent's answer is a second reading.

The verdict:

- The `flag-off/` run shows both sentinels: the setup delivers the clone's preload, and the `flag-on/` run decides.
- The `flag-off/` run shows a sentinel missing: the run is void. The orchestrator changes the step the void run points at and makes one more pair of runs at most.
- The `flag-on/` run shows both sentinels: the preload survives the flag.
- The `flag-on/` run shows neither: the flag blocks the preload.

Two edges stay open. A run in which one sentinel shows and the other does not is recorded as it fell. A listing answer that disagrees with the transcript is recorded as the agent's reading and decides nothing.

**Where the run cannot be made.** A missing credential, a refusal of `claude -p` by the permission system, or a void second pair each stops the measurement step. In that case the orchestrator writes a row of *Judgments of the run* that names the step that stopped and its output, Q1 stays open with its default, and phase 1 builds the same tree with no `docs/experiments/` record, because A2 is chosen whatever the run shows. The issue's first *Done when* line then stays unmet, and the owner answers Q1.

## Overlap with the release

The spawn names #1655 (`fix/1655-settle-only-release-note`, work item `1795841828-settle-only-release-note`) and #1659 (`feat/1659-find-leftovers-before-a-round`, work item `1795841830-find-leftovers-before-a-round`). On 2026-11-28 #1655's branch held its frame at `c0cabec2`, whose *Overlap with the release* orders #1650 first over `skills/settle/SKILL.md` (read). On the same date #1659's branch held its routing commit `bbb66b38` alone, and its worktree held an uncommitted skeleton of `frame/design.md` that names no `SKILL.md` frontmatter (read, `grep`). The rows read their issues, #1655 and #1659, as `gh issue view` printed them on 2026-11-28.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1655 | `skills/settle/SKILL.md`. This work removes the frontmatter clause "NOT for: the release notes, which the tag's workflow builds from the fragments". #1655 states the settle-only release in that file's body, and its subject, where a release note comes from, makes that clause stale for a release made of a settle alone | #1650 | Merged first, this work removes the clause that contract rule 19 would otherwise oblige #1655 to correct. The two edits stand in different hunks, so either order merges without a conflict where #1655 leaves the frontmatter alone. This work's diff is the smaller |
| #1659 | `skills/verify/SKILL.md`. This work removes the frontmatter's `NOT for:` clause, and #1659 changes the body's *Scope* row *Phase boundary*. Neither change reads the other's: #1659's keep file and suite commands read no skill description, and this work reads nothing #1659 adds | #1650 | The hunks are disjoint, so the order costs no conflict either way. This work's diff is the smaller, so it is likelier to be cleared first, and it carries the version move, which merges before every other item of the release (`skills/implement/merge-order.md`) |

## Operational impact

- No migration, environment variable or dependency. M1 needs `uv`, which the broad gate already runs.
- A session's skill listing becomes shorter, and the descriptions `frame/design.md` *Scope* item 3 names lose `NOT for:` items. A session may choose a skill differently for a request a removed item named (*Technical context*, failure scenario).
- The removed case allows more: a skill a model may invoke can now ship with no `NOT for:` clause. That is the cheaper mistake here, because the cost of a missing clause is one unneeded skill body, and the proofer reads each clause the case would have required (`frame/design.md` G4).
- The new case denies more: a skill that an agent's `skills:` list names can no longer take `disable-model-invocation: true`.
- The measurement step spends a paid model session on the person's credentials, bounded by `--max-budget-usd` on each run.
- The version move. The orchestrator chose this work item to carry the release's version move under `skills/implement/merge-order.md`, because no plan it had read when it chose orders this item after another. #1655's plan at `c0cabec2` orders #1650 first. The phase 1 crafter moves `.claude-plugin/plugin.json`'s `version` in the commit that adds `changelog.md`, to the version that the release branch's name holds. The crafter reads that name with `git rev-parse --abbrev-ref @{upstream}` in the worktree. At `24c5276f`, `.claude-plugin/plugin.json` was the one file outside `agentory/threads/` that held the current version (executed: `git grep -n '0\.40\.1'`).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-28 | This work item carries the release's version move and merges first. | No plan of the release orders it after another: #1655's plan at `c0cabec2` and #1659's plan at `61ea6bcc` each order #1650 before themselves, and this plan orders it before both. | `skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in* |
| 2026-11-28 | The measurement step's run is the orchestrator's, and phase 1 alone is the crafter's; the framer agreed with a change, keeping the `docs/experiments/` record with the crafter (A11). | The run starts a session that spawns an agent, which contract rule 6 withholds from every agent, and `routing.md` answers `Implementation` with `crafter`. | `skills/agent-contract/SKILL.md` rule 6; `skills/implement/orchestration.md` *The frame is read against the issue at the spawn* |
| 2026-11-28 | The pull request's title takes `perf:`. | Every session pays fewer characters of skill descriptions on every turn, and no script, hook, case or skill body changes what a party does; whether a session now picks a skill differently is unverified and handed to the repository owner in `gaps.md`. | `skills/commit-pr-convention/SKILL.md`, its prefix table, row `perf:` |
