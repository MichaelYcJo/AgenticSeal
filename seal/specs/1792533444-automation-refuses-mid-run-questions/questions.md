# under automation, a mid-run question is refused — questions for the planner

## Answered from the tree, not to be reopened

- **When the declaration cannot be read, the gate passes.** This is the
  issue's answer, and the house convention agrees. `hooks/routing.py` fails
  toward "no declaration". `docs/commit-review-gate-spec.md` says, of the
  automation press, "Every way of not reading the press is the attended
  answer". `CONTRIBUTING.md` §*What a change to a gate must carry* calls a
  deny that fires on every call in some environment an outage, and a broken
  file on an attended branch would be that. The review arm already stops the
  next commit on such a branch.
- **An unreadable question is refused.** The exemption rests on reading the
  routing question, so a call that cannot be read is not it.
- **The branch resolves the way the commit gate's PreToolUse reading
  resolves it.** Both call `routing.declared(cwd, optin.repo_root(cwd))`
  (`hooks/gate.py#arms_missing`). A linked worktree reads its own branch,
  and its own `seal/` in shared mode or the common one in local mode. A
  detached HEAD reads as no branch, so the call passes.
- **The routing question put alone passes while this session's transcript
  can be read and holds no answer to it from this clone.** Put alone means
  single-select and with its text. A run resumed in a new session has to put
  question 1 again, so that the worktree guard and the commit gate find the
  press (`skills/implement/orchestration.md` §*Question 1 — single-select*,
  #894). The issue did not cover this case.
  `worktree_consent.last_routing_answer` returns None when it read the
  transcript and found no answer, and only then does the question pass. It
  returns `worktree_consent.UNREAD` when nothing could be read, which is
  refused, since the gates that read the press would find none. Once it
  returns an answer, the routing question is refused like any other. Any
  answer from this clone spends the exemption, including one given for
  another work item. That case is outside the one-issue flow.
- **The deny repeats on every call.** It carries no once-per-session marker,
  because under automation every stop is a deny
  (`docs/commit-review-gate-spec.md` §*The PreToolUse reading of a commit*).
- **The orchestrator's prose points to the gate.** `skills/implement/SKILL.md`
  §1 gains one sentence. The `Automation` paragraph and the resume clause in
  `skills/implement/orchestration.md` are rewritten in place. The rule's one
  home is `docs/the-review-record.md` §*The run*, beside "No person is asked
  mid-run."
- **The reason is in English.** No `Record language` row exists, and every
  gate except the worktree guard prints English.
- **The memory note goes after the install, not at the merge.** Hooks run
  from the installed plugin cache, so until the release is installed the
  note is the only thing standing for the rule. Removing it is the
  orchestrator's act.
- **The hook's name and group** (`hooks/question-gate.py`, `pre-question`)
  are assumed. A different name builds the same thing.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the harness run a `PreToolUse` hook registered with matcher `AskUserQuestion`, hand it `tool_input.questions` in the shape the transcript's `tool_use` input shows, and honour its `deny`? The tree cannot say. The input shape was read from six transcript calls (`executed`), but no case drives the harness. A subagent has no `AskUserQuestion`, so neither the smith nor the warden can trigger the hook. And this run's hooks come from the installed 0.22.2 cache, so the tree's gate does not fire here. The orchestrator takes the measurement in the first session after a release carrying the gate is installed, by putting a non-routing question on a branch that declares `Automation` `yes`. | a measurement | It fires and denies: the gate works as framed. It does not fire, or the payload differs: the gate is inert, behaviour stays as it is today, and the registration or the payload read is fixed in a follow-up | It fires, with that shape, and honours the deny. `hooks/review-skill-gate.py` records a measured PreToolUse deny on `Skill` against Claude Code 2.1.241 | open |

**`Who can answer` takes one of three values and nothing else.**

- **a person**: what the product should be, or a value somebody has to be
  accountable for. This is the only kind of row that blocks the build.
- **a measurement**: a probe, a command or a count settles it.
- **the work**: unknowable at framing time. The phase that meets it decides
  it there and records a divergence row.

**The framer opens rows and does not own their answers.** The `Status`
column is written by whoever answered, as `answered <date> by <who>`.

Answered rows feed back into `spec.md`'s `## Rule changes` (a policy clause
or an open-questions section) before this directory's work merges.
