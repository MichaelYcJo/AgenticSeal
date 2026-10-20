# Feature Specification: under automation, a mid-run question is refused

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

Issue #1002. In 0.22.3 the orchestrating session put four framer questions to
the owner through `AskUserQuestion` on runs routed `automation`, with
`skills/implement/SKILL.md` §1 loaded. That section says the session runs to
the pull request once the batch is answered. The rule was prose, and it did
not hold. The repair is a hook that reads the branch's declaration and
refuses the question tool.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | A design that stops to ask a person is the more expensive one. This hook removes a stop and adds none. |
| `docs/the-review-record.md` §*The run*, "No person is asked mid-run." | The run-level rule this work holds with a check. The new rule lands in this section, beside that sentence (`## Rule changes`). |
| `docs/commit-review-gate-spec.md` §*Registration* | A gate is a standalone script named in `GROUPS` in `hooks/dispatch.py`, and `hooks/hooks.json` registers the group. The strictest decision wins. A gate that raises is skipped, the call goes ahead, and the failure is said once at the end of the turn. |
| `docs/commit-review-gate-spec.md` §*The PreToolUse reading of a commit*, "Where the person pressed `automation`, every stop is a deny." | Two things are inherited. A stop under automation is a deny on every call, because nobody is there to answer a prompt. And every way of not reading the promise counts as attended. |
| `docs/worktree-guard-spec.md` §*Creation consent* | The guard never reads `routing.md` as consent, because the model writes that file. This hook reads the file only to refuse. A row the model forged can only bind the model more, and a row edited to `no` shows up in the diff the review reads. |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The change has to state five things: the failure direction, the prompt budget, what it removes, platform honesty and a test seen red. Each is answered below and in `plan.md`. |
| `skills/implement/orchestration.md` §*Question 1 — single-select*, "A run resumed in a new session puts question 1 through `AskUserQuestion` again" | A resumed run has to put the routing question again, because the worktree guard and the commit gate read the person's press from the transcript (#894). So when question 1 is put alone, the hook lets it through. |
| `skills/implement/SKILL.md` §*1. Read the spec before the code*, "Once the batch is answered, the session runs to the pull request." | The prose rule. The hook holds it, and the paragraph points to the hook. |
| `hooks/routing.py#declared`, `#parse` | There is one reader of the declaration. It fails toward "no declaration", and `Automation` reads `yes`, `no`, or `None` for absent or outside its vocabulary. |

## Scope

**In:**

- A `PreToolUse` gate on `AskUserQuestion`, `hooks/question-gate.py`, in a
  dispatch group of its own, registered in `hooks/hooks.json`. The name is
  this frame's choice. A different name builds the same thing.
- The gate denies the call only when all three hold:
  1. the tool name is exactly `AskUserQuestion`;
  2. `routing.declared(cwd, optin.repo_root(cwd))` returns a declaration
     whose `automation` is `routing.AUTOMATION_YES`;
  3. the call is not the routing question put alone while this session has
     not yet answered it from this clone. Put alone means one question,
     single-select, with its text, whose labels the press reader recognises.
     Not yet answered means `worktree_consent.last_routing_answer` is None.
- Every other case passes, with no output:
  - no `seal/`;
  - no declaration naming the branch, which covers the routing question at
    the start, asked before `routing.md` exists;
  - a detached HEAD;
  - `Automation` reading `no`, absent, or outside its vocabulary;
  - a declaration that does not parse;
  - two declarations naming one branch.
- The deny fires on every call, with no once-per-session marker. Its reason
  names the work item's directory once, and says three things: build on the
  default the question states, write that default as a row of `questions.md`
  in that directory, and name it in the pull request body. It also says that
  a question stating no default is not the session's to answer, that asking
  again meets the same refusal, and that the routing question put alone goes
  through only until this session has answered it here. The row label and value it prints come
  from `routing.AUTOMATION` and `routing.AUTOMATION_YES`, never retyped. A
  test pins the text (contract §14).
- `hooks/worktree_consent.py` has one predicate for "these are question 1's
  labels", `is_routing_question`, in place of the two inline copies of the
  label comparison. The press reader and the gate's `routing_question_alone`
  both call it.
- The prose points to the hook instead of carrying the rule alone:
  - `skills/implement/SKILL.md` §1 gains one sentence naming the hook and the
    rule's home.
  - `skills/implement/orchestration.md` §*What the answer writes* rewrites its
    "`Automation` is an audit trail, not a gate" paragraph in place.
  - The resume sentence in §*Question 1 — single-select* says that question 1
    goes alone on a branch whose declaration reads `Automation` `yes`.
  - `hooks/routing.py` (the `AUTOMATION` comment and `parse`'s docstring) and
    `templates/sdd-routing.md` (the `Automation` comment) stop saying that
    nothing can hold a run to the row.
  - `README.md` gains a row for the gate in its gate table.
- The rule is stated once, in `docs/the-review-record.md` §*The run*
  (`## Rule changes`).

**Out, each for a reason:**

- **Removing the machine-local memory note**
  `automation-means-no-mid-run-questions.md`. The note is not in the tree,
  and hooks run from the installed plugin cache, not from this tree. So the
  note keeps doing its job until the release carrying this hook is installed.
  Removing it is the orchestrator's act, after that install.
- **Questions put as plain text in conversation.** A question the owner
  raises is answered in text, and the hook neither sees it nor needs to (the
  issue's stated limit).
- **Gates that read the press rather than the row.** The commit gate and the
  worktree guard decide between deny and `ask` on the harness-written press.
  Under `per axis` with box 1 checked there is no press, so their `ask` can
  still reach a person. This is by design: consent cannot rest on a file the
  model writes (`docs/worktree-guard-spec.md` §*Creation consent*). It is
  not changed here.
- **Gates whose reason tells the model to use `AskUserQuestion`**:
  `review-skill-gate.py`, `mode-gate.py`, the commit gate's first deny
  without the press, and the worktree guard's choice sites. Under
  `Automation` `yes` that instruction meets this refusal. Such a question
  states no default, so the session takes none of its ways on and hands the
  stop back at the end of the run. This is a stated limit, not a change to
  those gates.
- **An orchestrator sitting in a checkout whose branch is not the declared
  one**, for example the main checkout on a release branch while the work
  item lives in a linked worktree. Its question passes. The normal flow is one
  issue under automation on its own branch, switched to in place, and there
  the session is on the declared branch. This is a limit sentence in the rule,
  not a mechanism (the owner's 2026-10-19 direction, recorded in the machine
  memory note `edge-cases-outside-the-normal-flow-are-limits.md`; `read`).
- **Other work items' `routing.md` copies** of the template comment. They are
  records, and they are not rewritten. This item's own `routing.md` is not
  rewritten either (spawn prompt).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 automation refuses | Given a repository with `seal/` and a declaration naming the checked-out branch with `Automation` `yes`, when an `AskUserQuestion` call carrying a framer-style question reaches the gate, then the decision is `deny`, and the reason names the work item's directory once, `questions.md` in it, the pull request body, and the label and value from `routing.py` | a case in the new test module, driving the gate through `run_hook` |
| S2 every call | Given S1, when the same session calls a second time, then it is `deny` again, and nothing is written under the git directory | the same module |
| S3 attended | Given the declaration reads `Automation` `no`, or has no `Automation` row, or a value outside its vocabulary, then the gate prints nothing | the same module, one case per spelling |
| S4 not a declaration | Given no `seal/`; or `seal/` with no declaration for the branch; or a declaration whose `Review` row is outside its vocabulary; or two declarations naming the branch, then the gate prints nothing | the same module |
| S5 detached HEAD | Given S1's declaration and a detached HEAD, then the gate prints nothing | the same module |
| S6 linked worktree | Given a linked worktree checked out on the declared branch, with the main checkout on an undeclared branch, then a call whose `cwd` is the worktree is `deny`, and a call whose `cwd` is the main checkout prints nothing | the same module |
| S7 local mode | Given the root under the common git directory holding S1's declaration, then the call is `deny` | the same module |
| S8 the routing question alone | Given S1 and a session holding no answer to the routing question from this clone, when the call carries one single-select question with its text and question 1's three labels, decorated as the press reader accepts (`automation (Recommended)`), then the gate prints nothing. Once the transcript holds an answer from this clone, the same call is `deny`. A call with the labels but multi-select, or with no question text, is `deny` | the same module |
| S9 the routing question with company | Given S1, when the call carries question 1 and a second question, then it is `deny` | the same module |
| S10 an unreadable call | Given S1, when `tool_input` has no `questions` list, or a question that is not an object, then it is `deny` | the same module |
| S11 a near miss of the tool | Given S1, when `tool_name` is anything other than exactly `AskUserQuestion`, then the gate prints nothing | the same module |
| S12 registered | `hooks/hooks.json` carries a `PreToolUse` entry for `AskUserQuestion` that runs `dispatch.py` on the new group, with the `py -3` fallback, and `GROUPS` holds the gate. Through `dispatch.py`, S1's payload is a `deny` | the new module, plus the existing `tests/test_chain_hooks_hardening.py` and `tests/test_a_script_says_which_interpreter_it_needs.py`, which read every `hooks.json` entry |
| S13 one predicate | `_routing_preset` and `_routing_answer` call `is_routing_question`, and their existing cases pass unedited | `tests/test_the_guard_asks_once_per_session.py`, `tests/test_an_automation_run_meets_no_commit_prompt.py` |
| S14 the prose points to the hook | `skills/implement/SKILL.md` §1 and `skills/implement/orchestration.md` each name `hooks/question-gate.py`, and none of the four sentences `## Removes` lists still stands | one case in the new module, plus `tests/test_waiver_decided_at_start.py`, whose pin of "the session runs to the pull request" still passes |

Each new case is seen red before it is committed (contract §15): against the
tree with the gate absent, or with the pinned sentence deleted.

## Data & interfaces

- **Payload read**: `tool_name`, `tool_input.questions` and `cwd`. An input
  shape of `{questions: [{question, header, options: [{label, description}],
  multiSelect}]}` was read from six `AskUserQuestion` calls in this machine's
  transcripts (`executed`, a `python3 -I` scan of the `tool_use` inputs,
  keys only). That the PreToolUse `tool_input` carries the same object is
  `unverified`, and `questions.md` Q1 asks it.
- **Branch and root**: the same call the commit gate's PreToolUse reading
  makes, `hooks/gate.py#arms_missing` → `routing.declared(cwd, top)`
  (`read`):
  - `top` is `optin.repo_root(cwd)`, which is `git rev-parse --show-toplevel`.
  - `routing.current_branch` is `git -C cwd rev-parse --abbrev-ref HEAD`,
    and `HEAD` reads as "", so a detached HEAD matches no declaration.
  - In a linked worktree, `top` is that worktree's toplevel and the branch is
    its own. `optin.home_at(top)` reads `<worktree>/seal/` in shared mode and
    `<common-dir>/seal/` in local mode.
- **The work item's directory** for the reason is `routing.item_dir(top,
  branch)`, named once. `routing.md` and `questions.md` are named as files in
  it. It is printed relative to `top`. Where no relative spelling exists
  (Windows, another drive) the absolute path is printed, the way
  `hooks/gate.py#declaration_hint` does it.
- **Output**: the `hookSpecificOutput` deny object every gate prints
  (`hooks/review-skill-gate.py#decide` is the shape), or nothing.
- **The exemption**: `routing_question_alone(tool_input)` in the gate. It is
  True for exactly one question that `worktree_consent.is_routing_question`
  recognises, with `multiSelect` False and a string `question`. These are the
  press reader's conditions. The exemption also needs
  `worktree_consent.last_routing_answer(top, session, transcript_path)` to be
  None, meaning this session holds no answer from this clone. Once that
  answer is recorded, a question in question 1's labels is refused like any
  other.
- **New function**: `worktree_consent.is_routing_question(question) -> bool`.
  It returns True when `question` is an object whose `options` labels, cut by
  `leading_phrase`, are exactly `ROUTING_LABELS`. It replaces the comparison
  `_routing_preset` and `_routing_answer` each made inline.
- **Registration**: `GROUPS["pre-question"] = ("question-gate.py",)`, and a
  `hooks.json` `PreToolUse` entry with matcher `AskUserQuestion`. The gate
  compares `tool_name` exactly, so the decision does not rest on how the
  harness reads a matcher.
- **Failure direction**: it blocks more.
  - A wrong deny costs the session one default it would have asked about,
    and the pull request body names that default for the owner to overturn.
  - A wrong allow is the stopped run this item exists to end.
  - Every way of not reading the declaration is the attended answer, as
    `docs/commit-review-gate-spec.md` states for the press: no `seal/`, no
    branch, an unparseable file, the gate raising (`dispatch.py` skips it and
    says so). The deny rests on a promise the person made, and a promise
    nobody can read was not made. An unparseable declaration is already
    stopped at the next commit by the review arm, so nothing is lost by
    passing here.
  - An unreadable *question* is refused, because the exemption rests on
    reading the routing question, and a question that cannot be read is not
    it.
- **Prompt budget**: none added. The hook removes every mid-run
  `AskUserQuestion` on a branch declared `Automation` `yes`; 0.22.3 measured
  four in one run (the issue).
- **Platform**: no process inspection. It makes two `git rev-parse` calls,
  on the path every gate already takes. It is registered with the
  `python3 … || py -3 …` pair every entry carries.
- **This item's own first case**: once a release carrying the hook is
  installed, this branch's declaration (`Automation` `yes`) denies
  `AskUserQuestion` on this branch. During this run the installed 0.22.2
  hooks run, and the tree's hook does not fire.

## Rule changes

- add
  file: docs/the-review-record.md
  section: The run
  to: **On a branch whose `routing.md` reads `Automation` `yes`, the
    question tool is refused on every call.** The person who answered the
    routing question was promised that nothing stops to ask, and a
    question put at minute thirty waits for somebody who is not there.
    The session builds on the default the question states, writes that
    default as a row of the work item's `questions.md`, and names it in
    the pull request body, where the owner can overturn it. The routing
    question put alone, single-select and with its text, goes through
    until this session has answered it from this clone, because a run
    resumed in a new session has to put question 1 again for the gates
    that read the press; once it is answered, it is refused like any
    other question. The declaration is read through `hooks/routing.py` for the
    branch checked out where the session sits, and every way of not
    reading it is the attended answer. The file is written by the model,
    which is why the worktree guard never reads it as consent. It is read
    here only to refuse, so a row the model forged binds only the model,
    and a row edited to `no` is in the diff the review reads. A session
    sitting in a checkout whose branch is not the declared one is not
    held, and neither is a question asked as plain text. A gate whose own
    reason says to ask with the question tool meets this refusal too, and
    its question states no default: the session takes none of the ways on
    that question offers, and hands the stop back at the end of the run,
    as the commit gate's reason under `automation` says.
    check: tests/test_an_automation_run_puts_no_question.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the sentence that nothing can hold a run to `Automation` | skills/implement/orchestration.md#"What the answer writes">"Automation is an audit trail, not a gate." (the bold opening of that paragraph, its backticks left out here) | rewritten in place: the row is held by `hooks/question-gate.py`, and the rule is `docs/the-review-record.md` §*The run* |
| the comment "Nothing gates on it and nothing can" | `hooks/routing.py#AUTOMATION` | rewritten in place to name the one gate that reads the row |
| the docstring clause "nothing CAN decide one on `Automation`" | `hooks/routing.py#parse` | rewritten in place: nothing decides a *commit* on the row, and the question gate reads it |
| the template comment "WHAT IT DOES NOT BUY — nothing at the pull request can hold a run to it." | `templates/sdd-routing.md#"WHAT IT DOES NOT BUY — nothing at the pull request can hold a run to it."` | rewritten in place to say what holds it |
| the two inline copies of "these options are question 1's" | `hooks/worktree_consent.py#_routing_preset`, `hooks/worktree_consent.py#_routing_answer` | `hooks/worktree_consent.py#is_routing_question`, which the new gate calls too |
| the resume clause "in the same call as whatever else the resume has to ask" | `skills/implement/orchestration.md#"Question 1 — single-select">"in the same call as whatever else the resume has to ask"` | rewritten in place: question 1 goes alone where the declaration reads `Automation` `yes`, because anything beside it is refused |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

Framed 2026-10-21 by framer, before the build.
