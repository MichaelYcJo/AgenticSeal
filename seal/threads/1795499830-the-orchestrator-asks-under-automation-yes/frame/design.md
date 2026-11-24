# Design: 1795499830-the-orchestrator-asks-under-automation-yes (#1608)

## Grounding

The tree as read at `bf5369cee`, whose code is that of `7c8f67103`, the v0.38.7 merge (the one commit between them adds `routing.md`).

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *The rule a mechanism is kept against*, the sentence "A script holds a gate only on a fact it reads exactly" | The hook refuses only on three exact readings: the `Automation` row as `lib/routing.py#parse` reads it, a branch as `git worktree list --porcelain` prints it, and the marker `hooks/ask-under-automation.py#MARKER` in its one spelling. It carries no list of other spellings. A question that holds the marker with its case changed is named in the refusal as a line the hook did not read, and the hook decides nothing on it. Whether the stated reason is true is not the hook's to judge. |
| G2. `skills/core/SKILL.md` *The first value: efficient development through the AgenticSeal process*, the paragraph **Asking a person is the most expensive step** | The hook adds no question. It refuses a call, and the refusal names what lets the next call through, so a question the owner must answer costs one more call and no wait. |
| G3. `docs/running/the-run.md` *The run*, the paragraph opening **On a run whose `routing.md` reads `Automation` `yes`** (read, lines 33 to 55) | This is the rule the hook puts in front of the orchestrator at the act. The hook reads the paragraph from the plugin root it runs from, so the paragraph keeps one home. The paragraph has no `check:` line today. The one change the paragraph takes is a `## Rule changes` item below. |
| G4. `docs/running/what-a-script-gates.md` *Which gate a script holds* and *The checks* (read) | A gate names the form it reads, what it names as not read, and the agent and step that judge the meaning of the same text. The hook is a new gate, so *The checks* takes a row for it, as a `## Rule changes` item. |
| G5. `CONTRIBUTING.md` *What a change to a gate must carry* (read) | Each new case is seen red first. The failure direction is toward letting the call through: every error, an unreadable payload, a git that does not answer and a tree with no root all print nothing. The hook adds no prompt and removes stops. Windows is not run, and the pull request says so. |
| G6. `CONTRIBUTING.md` *House rules*, the item **The plugin ships two hooks, and neither writes outside the repository** (read) | Each hook's command is `python3 <script> \|\| py -3 <script> \|\| exit 0` with the script under `${CLAUDE_PLUGIN_ROOT}`. The plugin directory refuses a plugin that registers a command hook (#1376), and the owner chose on 2026-11-08 to ship such hooks (#1430). #1608, which asks for this hook, was filed by the repository's owner (executed: `gh issue view 1608 --json author` reads `MichaelYcJo`; `gh repo view` reads `MichaelYcJo/AgenticSeal`). |
| G7. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | This work item's subject is the code: a hook, its reader and the orchestrator's skill. It states its changes to the policy root (`docs/`, `seal/config.json` names no `Policy root`) in `## Rule changes` for the settle. `skills/`, `lib/`, `hooks/`, `tests/`, `README.md`, `README.ko.md`, `SECURITY.md` and `CONTRIBUTING.md` lie outside the policy root, so the build edits them directly. |
| G8. `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* (read, lines 51 to 59) | The diff changes `skills/implement/orchestration.md`, so `changelog.md` ends with `### Process changes` in the shape `templates/records/process.md` gives. |
| G9. `docs/releasing/branch-and-release.md`, the list opening at line 15, and `routing.md` *Why this way* | This is the first pull request into `release/v0.38.8`. `.claude-plugin/plugin.json` reads `0.38.7` and is the one file outside the records that holds the version (executed: `git grep -n '0\.38\.7' -- ':!seal/threads'` prints `.claude-plugin/plugin.json:4` alone). |
| G10. `lib/routing.py#item_dir` and `#declarations` (read, lines 302 to 352) | The declaration that applies to a branch is the one whose `Branch` row names it; the directory's name and position decide nothing. A work item is open in this design where its declared branch is checked out in a worktree of the repository. |
| G11. The cases that hold the hooks (read): `tests/behaviour/test_chain_hooks_hardening.py#HOOK_ENTRIES` and `#HOOK_FILES` (lines 28 and 29), `#test_the_places_that_reach_the_network_are_named` (line 428), `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#README_FACTS` (line 196), `tests/hooks/test_core_start.py#command` and `#start` | A third entry in `hooks/hooks.json` turns the first module red until `HOOK_ENTRIES` and `HOOK_FILES` name it. The command-shape cases are parametrized over `HOOK_ENTRIES`, so they then hold the new command too. The new module runs the hook's command as `hooks/hooks.json` spells it, as `tests/hooks/test_core_start.py` does. |
| G12. `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser` (read) | A citation of a section that this pull request renames passes where a pending `## Rule changes` item's `from` holds it and its `to` does not. The `docs/running/measuring-a-run.md` citation of `CONTRIBUTING.md`'s renamed item is corrected that way. |

**What Claude Code passes the hook and what it accepts back** (executed). The installed Claude Code is 2.1.331 (`claude --version`). Its binary's strings hold the `PreToolUse` branch that reads `hookSpecificOutput.permissionDecision`, takes `"deny"` as a decision and carries `permissionDecisionReason` with it. An `AskUserQuestion` call's input, read from one transcript's `tool_use` block, has the one key `questions`. Each question has the keys `header`, `multiSelect`, `options` and `question`, and each option has `description` and `label`. Whether the main session shows the reason and asks nothing is a behaviour no subagent can trigger, and it is `frame/questions.md` Q1.

**Nothing in the tree reads a question today** (executed: `git grep -n -E 'AskUserQuestion|tool_input|permissionDecision' bf5369cee -- '*.py' '*.json'` prints lines of `tests/behaviour/test_first_setup_asks_once.py` and `tests/behaviour/test_waiver_decided_at_start.py` alone, and each reads the word in prose; `git grep -n PreToolUse` prints this work item's `routing.md` alone; `git grep -l 'No default'` prints nothing). `hooks/hooks.json` registers `Stop` and `SessionStart` (read).

**A work item's directory outlives its run** (executed). `seal/threads/` holds 50 directories, and all 50 `routing.md` files read `| Automation | yes |` (`grep -l`). Released items keep their directories until the settle after their release (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*), so a reader that took every directory present as open would refuse every `AskUserQuestion` call in this repository until the next settle.

**The reading this design takes, run over this repository** (executed: `test_tmp_open_items.py` in the framer's scratch, loading `lib/` from a `git clone --no-local` at `bf5369cee` and run against this checkout). `git worktree list --porcelain` lists 1 worktree with 1 branch. Its root holds the declarations the paragraph above counts, and one of them reads `yes` on a checked-out branch: this work item's, on `fix/1608-the-orchestrator-asks-under-automation-yes`. The reading took 0.025 s.

**How the tree lists worktrees today** (read). `skills/implement/scripts/seal.py#other_worktrees` (line 1584) reads the `worktree` lines of the same listing, leaves out the clone's own and the common git directory, and feeds a note. This work needs each worktree's `branch` line as well, and a worktree whose branch is the session's own. A `bare` or `detached` entry has no `branch` line. `lib/optin.py#home_at` finds a worktree's root: its own `seal/` in shared mode, the common directory's in local mode, so in local mode every worktree answers the same root.

**The installed plugin ships `docs/`** (executed: listing the 0.38.7 copy in the plugin cache shows `docs/running/the-run.md`). The hook can read the paragraph from the root it runs from.

**Every statement that no script decides on `Automation`** (executed: `git grep -n -i -E 'decides anything on it' bf5369cee -- . ':!seal/threads'`). The search prints three lines: `lib/routing.py:103`, `lib/routing.py:205` and `skills/implement/orchestration.md:289`. `lib/routing.py:28` to `:30` says nothing decides a commit on the three optional rows, and that stays true, since the hook decides no commit. The search is on one wording, so the list is a sample (contract rule 12). The other statements of the hook's subject found by reading are `README.md:150` to `:157` and `docs/running/the-review-and-parity-arms.md:107`, and both stay true.

**Every statement of how many hooks the plugin ships** (executed: `git grep -n -E 'two (command )?hooks|neither hook|Neither hook|both hooks|registers both|훅 두|두 훅|어느 훅도' bf5369cee -- . ':!seal/threads' ':!skills/verify/scripts/pytest_record'`). The pathspec leaves out this work item's directory and the pytest plugin, whose "two hooks" are pytest's. The search prints 36 lines (executed: the same search piped to `wc -l`):

- `CONTRIBUTING.md:485` and `:498`.
- `README.ko.md:60`, `:64`, `:337`, `:339`, `:352`, `:354`, `:370`, `:379`, `:392` and `:441`.
- `README.md:56`, `:59`, `:338`, `:340`, `:353`, `:355`, `:371`, `:381`, `:394` and `:444`.
- `SECURITY.md:23` and `:26`.
- `docs/running/measuring-a-run.md:140` and `:143`, which the settle rewrites (`## Rule changes`).
- `lib/launch.py:35` and `skills/update/SKILL.md:161`.
- `tests/behaviour/test_chain_hooks_hardening.py:34`, `:429`, `:439` and `:440`.
- `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:198`, `:206`, `:219` and `:222`.

The search is on wordings, so the list is a sample.

**The `## Rule changes` items below parse and place** (executed: `test_tmp_rule_changes_2.py` in the framer's scratch calls `parse` and `apply_op` of `skills/settle/scripts/rule_changes.py` from the clone at `bf5369cee` on this file). `parse` gives no error and no unread line, and each item places in its document with no refusal.

## Scope

1. **`lib/routing.py#open_declarations(cwd)`.** It asks `git worktree list --porcelain` from `cwd` through `lib/gitcmd.py#git`, reads every `worktree <path>` line and every `branch refs/heads/<name>` line, and returns `[(path, parsed)]` for each declaration that `#declarations` finds under any listed worktree whose `branch` names a branch one of those worktrees has checked out. Each `routing.md` counts once, by its real path. It returns `[]` where git does not start or does not finish (`lib/gitcmd.py#Failed`), exits non-zero, or lists no worktree. Its docstring says that "open" means a declared branch checked out in a worktree, and why a directory's presence is not enough.
2. **`hooks/ask-under-automation.py`.** It reads the payload's `cwd` and `tool_input`. It keeps the declarations of `open_declarations(cwd)` whose `automation` is `yes`. Where none is kept, it prints nothing. Otherwise it reads `tool_input["questions"]`, and where that is not a non-empty list of objects each holding a string `question`, it prints nothing. A question states why its default cannot be taken where its `question` text holds `MARKER`, `No default:`, followed on the same line by a non-blank character. Where every question of the call states it, the hook prints nothing. Otherwise it prints the `PreToolUse` deny object of *Data & interfaces*, whose reason holds, in this order:
   - the paragraph of `docs/running/the-run.md` whose first line opens with `LEAD`, read from `CLAUDE_PLUGIN_ROOT`, or from the root two directories above the script where that is unset, as `hooks/core-start.py#OWN_ROOT` does, or, where the paragraph cannot be read, that document's path and section and the paragraph's lead;
   - each open work item's directory name and branch whose `routing.md` reads `yes`;
   - the `header` of each question that does not state it, and a sentence naming the form;
   - for a question whose text holds `MARKER` with its case changed, a sentence saying the hook did not read it, because it reads `MARKER` in that one spelling.

   It exits 0 on every path and prints nothing where anything raises, `lib/gitcmd.py#Failed` among them. Its `__main__` block reconfigures the three streams as `hooks/core-start.py`'s does. Its docstring holds its edge cases and its failure direction.
3. **`hooks/hooks.json`** registers a `PreToolUse` entry with the matcher `AskUserQuestion` and one command hook, `python3 "${CLAUDE_PLUGIN_ROOT}/hooks/ask-under-automation.py" || py -3 "${CLAUDE_PLUGIN_ROOT}/hooks/ask-under-automation.py" || exit 0`.
4. **The statements that no script decides on `Automation`** are rewritten in place: the comment at `lib/routing.py:101` to `:104` and the sentence at `:204` to `:206` say that the pull request's check decides nothing on the row, and that the plugin's `PreToolUse` hook reads a `yes` alone. `skills/implement/orchestration.md` line 289 is item 7's.
5. **The cases.** `tests/hooks/test_ask_under_automation.py`, whose `TARGET` is the hook, holds the cases of S1 to S5, S7 and S9 that run the command as `hooks/hooks.json` spells it. `tests/lib/test_routing.py` holds the cases of S5 to S7 that call `open_declarations`. `tests/behaviour/test_chain_hooks_hardening.py` adds `"PreToolUse": "AskUserQuestion"` to `HOOK_ENTRIES` and `hooks/ask-under-automation.py` to `HOOK_FILES`. That module's docstrings at lines 33 to 58 and 428 to 433 name the third hook, the removal list names the hook and its test module, and the `git grep` in that docstring adds `PreToolUse\\|ask-under-automation`. Its network case locates each README passage by item 6's new sentences. `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#README_FACTS` adds `` `PreToolUse` `` and `` `hooks/ask-under-automation.py` ``, and its comments and docstring at lines 198, 206, 219 and 222 say "the hooks" without a count.
6. **The count of the plugin's hooks stands once, in each README edition, in the sentence that opens the list under *What runs on your machine* and *내 컴퓨터에서 도는 것*.** That list gains a `PreToolUse` item saying what the hook reads, that it refuses one `AskUserQuestion` call and never ends a turn, and what lets the call through. Every other line the count search of *Grounding* prints says "the plugin's hooks", or "every hook" or "no hook", without a number, in `README.md`, `README.ko.md`, `SECURITY.md` (with the hook in its list), `CONTRIBUTING.md` *House rules* (with the third command named, and the item's lead reading **The plugin's hooks write nothing outside the repository.**, which the last `## Rule changes` item cites), `lib/launch.py` and `skills/update/SKILL.md`. `README.md:355` and `README.ko.md:354` say that no hook ends a turn and that the `PreToolUse` hook refuses one call, after which the session goes on.
7. **`skills/implement/orchestration.md`**, three passages:
   - Line 289's paragraph opens with what the hook does in place of "`Automation` is a record, and no script decides anything on it": while the row reads `yes`, the orchestrator follows the paragraph of `docs/running/the-run.md` *The run*, and the plugin's `PreToolUse` hook puts it in front of the orchestrator at each `AskUserQuestion` call. The paragraph says what the hook refuses, what lets a call through, with the marker cited as `hooks/ask-under-automation.py#MARKER`, and that the hook does not judge whether the question is the owner's.
   - *Orchestrator: what needs a person is asked in one batch, before the first edit*, its first paragraph: the orchestrator reads the *Done when* of every issue the request names before it puts the batch, and puts in the batch each line that needs a real session, a credential, an outside service or a permission.
   - The same section gains one paragraph: a rule that restricts what agents may do in a run comes only from the person's answer in this run's batch or from a policy document. The orchestrator writes it under `## Why this way` in the work item's `routing.md` with its source, the batch question and its answer or the document's path and section. A spawn prompt carries such a rule only as `routing.md` states it, and an orchestrator does not carry a rule a person gave for an earlier run into this one.
8. **`changelog.md`** with a `### Process changes` table holding one row for each passage of item 7, and `.claude-plugin/plugin.json` at `0.38.8`, in one commit.

Out of scope:

- MichaelYcJo/owlery#181, the fork's copy of the hook, is that repository's work.
- `docs/running/the-run.md`, `docs/running/what-a-script-gates.md` and `docs/running/measuring-a-run.md`, which the settle writes from `## Rule changes`.
- A hook for an agent. A subagent has no `AskUserQuestion` (`skills/implement/routing-question.md`, the paragraph **The routing question is the orchestrator's, whether or not a framer runs**).
- A marker written into the batch's own questions by default. The routing question is refused only where another open work item reads `yes`, and a habit of writing the marker would make the hook a ritual. The refusal says what lets the call through.
- `README.md:150` to `:157` and `docs/running/the-review-and-parity-arms.md:107`, which stay true.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A question under `Automation` `yes` is refused | Given a repository with a marked root whose one work item's `routing.md` reads `Automation` `yes` on the checked-out branch. When the hook's command receives an `AskUserQuestion` payload whose one question does not hold `MARKER`. Then it exits 0 and prints the deny object, whose reason holds the paragraph's first line as `docs/running/the-run.md` holds it, the work item's directory name and its branch. | A case in `tests/hooks/test_ask_under_automation.py`, seen red against `bf5369cee`, where no script stands and the command prints nothing. |
| S2. A question that states why goes through | Given S1's repository. When every question of the call holds `No default: ` and a reason. Then the command prints nothing and exits 0. | A case in the same module, seen red with the marker test made to fail every question. |
| S3. One question of two without the form refuses the call | Given S1's repository. When one of two questions holds the form. Then the deny object's reason names the other question's `header`. | A case in the same module, seen red with the check reading the first question alone. |
| S4. A marker in another case is named and not read | Given S1's repository. When the one question holds `no default: x`. Then the call is refused, and the reason says the hook did not read that spelling. | A case in the same module, seen red with the near-spelling sentence removed, and the failing line read for that sentence. |
| S5. No open work item reads `yes` | Given each of: a root whose one `routing.md` reads `Automation` `no` on the checked-out branch; one that reads `yes` for a branch no worktree has checked out; a repository with no root; a directory outside any repository. When `open_declarations` runs there, and the hook's command runs there. Then `open_declarations` answers the one declaration, reading `no`, in the first, and `[]` in the other three, and the command prints nothing in all four. | Cases in `tests/lib/test_routing.py` and in the hook's module. The released-branch case is seen red with the branch test removed from `open_declarations`. |
| S6. A worktree's open work item counts | Given a main checkout on one branch and a linked worktree on a second whose `routing.md` reads `yes`, once in shared mode and once in local mode. When `open_declarations` runs from the main checkout. Then it answers the linked worktree's declaration, once. | Cases in `tests/lib/test_routing.py`, seen red with the reading narrowed to `cwd`'s own branch, and the local-mode case red with the real-path dedupe removed. |
| S7. The hook lets the call through on what it cannot read | Given S1's repository. When the payload is not JSON, or holds no `questions` list, or `git` is not on `PATH`. Then the command prints nothing, writes nothing to stderr and exits 0, and `open_declarations` answers `[]` where `git` is not on `PATH`. | Two cases in the hook's module, for the payload that is not JSON and the one with no list, each seen red with the `__main__` block's catch removed. The no-list case is held by the shape test of *Scope* item 2 as well, so it is shown red with both removed and pins the behaviour, not either guard. One case in `tests/lib/test_routing.py` for `git` off `PATH`, seen red with `open_declarations`' catch of `lib/gitcmd.py#Failed` removed, since `Failed` is a `SystemExit`. |
| S8. The hook is registered in the plugin's shape | Given `hooks/hooks.json`. When it is read. Then it holds a `PreToolUse` entry whose matcher is `AskUserQuestion` and whose one command has the three-part shape, and the command exits 0 where its script cannot be opened. | `tests/behaviour/test_chain_hooks_hardening.py`, with `HOOK_ENTRIES` and `HOOK_FILES` naming the hook, red before the entry is added. |
| S9. The paragraph comes from the plugin root | Given a plugin root whose `docs/running/the-run.md` lacks the paragraph. When S1's call runs with `CLAUDE_PLUGIN_ROOT` at that root. Then the reason names `docs/running/the-run.md` *The run* and the paragraph's lead in place of the paragraph. | A case in the hook's module. S1's case reads the paragraph's first and last lines from the tree's own document, so a rewrite of the paragraph that keeps its lead keeps S1 green. |
| S10. The orchestrator's skill states the three rules | Given `skills/implement/orchestration.md` after the build. When the proofer reads *Scope* item 7's three passages against the issue's *Done when* items 1, 2 and 3. Then each is stated once, with its source cited. | Read at review. The search `git grep -n -i -E 'decides anything on it' -- . ':!seal/threads'` prints nothing after phase 2 (executed at `bf5369cee`: it prints the three lines *Grounding* names, each of which *Scope* items 4 and 7 rewrite). |
| S11. The count of hooks stands once | Given the tree after phase 1. When the count search of *Grounding* runs. Then it prints `docs/running/measuring-a-run.md:140` and `:143` alone, which a `## Rule changes` item corrects at the settle. | The search, run at `bf5369cee` with every printed line accounted for in *Grounding*. The two README sentences that state the count read "three" and "세 개", which the search's patterns do not match. |

## Data & interfaces

**What the hook reads on stdin** (executed for the question's keys; read for `cwd`, which `hooks/core-start.py#main` reads from the same harness):

```json
{"cwd": "<the session's directory>", "tool_name": "AskUserQuestion",
 "tool_input": {"questions": [{"question": "...", "header": "...",
   "multiSelect": false, "options": [{"label": "...", "description": "..."}]}]}}
```

**What it prints to refuse**, on stdout, exit 0, and nothing otherwise:

```json
{"hookSpecificOutput": {"hookEventName": "PreToolUse",
  "permissionDecision": "deny", "permissionDecisionReason": "<the reason>"}}
```

**Names the build adds.** `hooks/ask-under-automation.py#MARKER` is `"No default:"`, the form's one home, which `skills/implement/orchestration.md` and the `## Rule changes` items cite. `hooks/ask-under-automation.py#LEAD` is the first line's opening of the paragraph G3 names, which locates the paragraph and is no copy of its text. `lib/routing.py#open_declarations(cwd)` returns a list of `(path, parsed)` pairs as `#declarations` does.

**The new entry in `hooks/hooks.json`**, beside `Stop` and `SessionStart`:

```json
"PreToolUse": [{"matcher": "AskUserQuestion", "hooks": [{"type": "command",
  "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/ask-under-automation.py\" || py -3 \"${CLAUDE_PLUGIN_ROOT}/hooks/ask-under-automation.py\" || exit 0"}]}]
```

## Rule changes

- change
  file: docs/running/the-run.md
  section: The run
  from: The orchestrator keeps a blocking question for what only the
    owner can decide, and only where proceeding on a default would be costly to undo or
    would reach outside the repository. A question or a remark the owner raises
    during the run is taken up when it arrives: the framer folds it into the
    frame, or it goes into the code, and it is never deferred to the pull
    request body.
  to: The orchestrator keeps a blocking question for what only the
    owner can decide, and only where proceeding on a default would be costly to undo or
    would reach outside the repository. Each question of such a call states why
    its default cannot be taken, in its text, after the marker
    `hooks/ask-under-automation.py#MARKER` holds, followed on the same line by
    the reason. The plugin's `PreToolUse` hook refuses an `AskUserQuestion`
    call whose questions do not, as `docs/running/what-a-script-gates.md`
    *The checks* states. A question or a remark the owner raises
    during the run is taken up when it arrives: the framer folds it into the
    frame, or it goes into the code, and it is never deferred to the pull
    request body.
    check: tests/hooks/test_ask_under_automation.py
- add
  file: docs/running/what-a-script-gates.md
  section: The checks
  to: | the `PreToolUse` hook (`hooks/ask-under-automation.py`) | each `AskUserQuestion` call of a session | the `Automation` row of each `routing.md` through `lib/routing.py`, under the root of each worktree `git worktree list --porcelain` lists, where the row's `Branch` is checked out in one of them; and, where one of those rows reads `yes`, the text of each question of the call, for `hooks/ask-under-automation.py#MARKER` followed on the same line by a reason, refusing the call where a question lacks it | lets the call through, printing nothing, where the payload, the question list, git or a root cannot be read; names a question holding the marker with its case changed as not read and refuses the call; reads no other spelling | whether a question is one only the owner can decide: the orchestrator writing the reason, and the person reading it |
- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: The
    plugin's two hooks, the stamp's `Stop` hook and the `SessionStart` hook that
    prints the core, reach no network.
  to: The
    plugin's hooks, which `README.md` *What runs on your machine* lists,
    reach no network.
- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: What
    `CONTRIBUTING.md` *The plugin ships two hooks, and neither writes outside
    the repository* forbids still binds it
  to: What
    `CONTRIBUTING.md` *The plugin's hooks write nothing outside the
    repository* forbids still binds it

## Removes

The removals are the rows of this table. The work adds a mechanism, a hook with a line form, and no mechanism can go in return. The paragraph of G3 is what the hook prints, so it stays. The batch is what the hook relieves, and #1608 records that it missed a *Done when* line, so it stays and grows. The hook's record of what it caught is #1608's run: two `AskUserQuestion` stops under `Automation` `yes`, the cost the issue reports.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sentence that no script decides anything on `Automation` | `skills/implement/orchestration.md` *Orchestrator: how the work is routed*, its bold lead **`Automation` is a record, and no script decides anything on it** | *Scope* item 7's first passage, which states what the hook decides |
| The same statement in code | `lib/routing.py:101` to `:104`, the comment above `AUTOMATION`, and `lib/routing.py#parse`, its docstring at lines 204 to 206 | *Scope* item 4 |
| Each count of the plugin's hooks outside the list it counts | the lines the count search of *Grounding* prints, outside `docs/` | the sentence opening the list in `README.md` *What runs on your machine* and `README.ko.md` *내 컴퓨터에서 도는 것*, the one place the count stands (*Scope* item 6) |
| The count in `docs/running/measuring-a-run.md` and its citation of the renamed `CONTRIBUTING.md` item | `docs/running/measuring-a-run.md` *Where a reading goes* | `## Rule changes`, for the settle |

Framed 2026-11-24 by framer, before the build.
