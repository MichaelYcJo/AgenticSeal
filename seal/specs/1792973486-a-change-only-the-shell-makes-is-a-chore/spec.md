# Feature Specification: a change only the shell makes is a chore

Issue #1031. Reviewing #1027 on 2026-10-26, the owner set a principle no file
of the repository states: a change only the shell makes, with no `Write`,
`Edit` or `NotebookEdit` before it, is a chore that would have been routed
`no work item` anyway, so a gate that catches only such changes adds a cost
and a question with nothing to catch. This work writes that principle into
`CLAUDE.md` *The rule a mechanism is kept against*, the section the owner
named, and leaves every other file as it stands, because no other file states
the opposite (*Scope*, item 3).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | The home of the sentence. Its first sentence weighs a mechanism by what it caught against what it costs, and the new sentences say which catches count. The same section says a fact has one source, so no other file restates the principle |
| `CLAUDE.md` *The goal a design is chosen against* | The ground the owner gave: a gate that catches only chores puts a question in front of a person with nothing to catch, which is the expensive design this goal argues against |
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*, and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | The wording: no symbol used as syntax, no value stated twice, and a defined term in its one meaning. `routed` keeps its routing meaning, so the sentence says `gap` where a path past a gate is meant |
| `docs/the-record-layout.md` *The root records* | `CLAUDE.md` holds the rules a session in this repository must hold. A principle every session weighs a gate against belongs there |
| `skills/settle/SKILL.md` *Rule changes* | A `file:` is a top-level `.md` file of the policy root, which is `docs` here (`seal/config.md` has no `Policy root` row). `CLAUDE.md` is outside it, so the build edits `CLAUDE.md` directly and `## Rule changes` holds the no-change block |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | A pull request does not edit the policy root. `CLAUDE.md` is not the policy root, and the pull requests that last changed this section edited it in place (`5aed51cb` for #940, `b451e503` for #941; executed: `git log -- CLAUDE.md`) |
| `skills/agent-contract/SKILL.md` rule 9 | The premise the principle rests on, checked: every agent writes through the `Edit` tool, so work a work item owns reaches the routing check, and the shell route is left to changes no work item owns. Its `check:` line names `tests/test_edits_go_through_the_edit_tool.py` |
| `CONTRIBUTING.md` *What a change to a gate must carry* | Where a pull request that adds a gate answers this section. It already cites `CLAUDE.md` *The rule a mechanism is kept against* as the reason, so it needs no edit to reach the new sentences |

## Scope

In:

1. **Two sentences in `CLAUDE.md` *The rule a mechanism is kept against*,
   placed directly after its first sentence**, which ends `existing is no
   reason to keep it.` (`CLAUDE.md:17`), and before `A rule's proof is the
   test or behaviour eval its`. The text, exactly:

   > A gate that stops a session, the routing check among them, guards the
   > work a work item owns. A change that would be routed `no work item`, such
   > as a formatter run, a dependency bump or an identifier renamed across
   > files by `sed`, is outside that work, so a gap in that kind of gate which
   > only such a change passes through is not a weakness to close.

   The checks that run on every pull request are not that kind of gate: they
   run on a change no work item owns as on any other, and the principle does
   not exempt them (round 1, finding 2). A file renamed with `git mv` inside
   a work item is work the work item owns, which is why the example is an
   identifier renamed by `sed` (round 1, finding 1).

   The build reflows the paragraph's line breaks around the insertion and
   changes no other word of the section.

2. **No `check:` line for the sentences.** None of the section's existing
   sentences carries one (executed: `grep -n 'check:' CLAUDE.md` finds only
   the mid-line mention at `CLAUDE.md:18`), and the sentences decide between
   designs at review rather than state a fact a test can read. A test that
   looked for the words would prove the words exist and nothing about any
   gate (`.github/scripts/rules.py` docstring, *How it errs*, read). The
   reader is the warden at review and the reviewer of a pull request that
   adds a gate, through `CONTRIBUTING.md` *What a change to a gate must
   carry*.

3. **The places that touch the shell route, each read and each left as it
   stands.** Found by `git grep` over `docs/`, `skills/`, `agents/`,
   `templates/`, `README.md`, `README.ko.md`, `CONTRIBUTING.md`, `CLAUDE.md`
   and every `seal/specs/*/spec.md`, for `through the shell`, `shell write`,
   `sed -i`, `edit tool`, `routing-edit-gate`, `edit gate`, `edit check`,
   `slip`, `bypass`, `weakness`, `hole`, `invisible to`, `left to catch`,
   `loophole`, `unguarded`, `not a security control` and the Korean `셸`
   (executed). None of them calls the shell route a weakness to close or
   proposes a mechanism to catch it:

   | Coordinate | What it says | Verdict |
   |---|---|---|
   | `skills/agent-contract/SKILL.md` *9 Edits go through the `Edit` tool*, second paragraph (lines 118 to 123) | The routing check sees only the edit tools, an edit through the shell is invisible to it, and only the pull request's trailer arm is left to catch the change | Kept. It speaks of an agent's edit inside a work item, which is work a work item owns, so the principle does not exempt it. It is the premise the principle rests on, not its opposite |
   | `README.md` *Limits*, first bullet (lines 585 to 592), and `README.ko.md` *한계*, first bullet (lines 579 to 585) | The edit hook is a record for a session about to edit unrouted work, not a security control, and an edit made through the shell never reaches it | Kept. It states what the hook does not reach, which is what the principle says need not be reached. Restating the principle there would be a second source |
   | `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md` *Rule changes*, the `add` of `docs/the-routing-check.md`, section *The edit check* (lines 186 to 193) | An edit made through the shell reaches neither the main session's check nor a subagent's, which is why every agent edits through the `Edit` tool, and the trailer arm is what remains for such a change | Kept, so this spec adds no `change` against it. It states a fact and cites rule 9 for agents. A later operation on text another unsettled spec adds is a place where two specs meet, and #1025 is the open defect of that shape, so none is added where nothing is wrong |
   | `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/plan.md` *Technical context*, the failure scenario, and *Alternatives considered*, the row *No pull-request arm; the edit check alone* | A session that learns to write files through Bash lands edits with no routing; an edit through the shell lands commits on an undeclared branch | Kept. The records of a merged work item are history and are not rewritten. Both speak of a session writing a work item's own files through the shell, which is work a work item owns |
   | `docs/the-review-record.md` *The stamp* (line 449) | No stamp is drawn for a local-mode `guarantee.md` that arrived by a shell write | Kept. It states a limit of the stamp, and #1027's spec already rewrites that sentence |
   | `skills/implement/SKILL.md` *2. Implement test-first* (lines 260 to 275) and `agents/smith.md:70` | An edit must be able to fail, so edits go through the `Edit` tool, and a shell substitution asserts that it matched | Kept. It is about an edit failing silently, not about the routing check |

4. **What stays out, each with its reason.**
   - The session memory file that held the principle,
     `chores-need-no-gate.md` in the memory directory of this repository's
     Claude Code project under `~/.claude/projects/`, with its line in that
     directory's `MEMORY.md`. It lies outside the
     repository, so no build commit can remove it. The issue's *Done when*
     names its removal, and the orchestrator removes it after the sentence
     merges.
   - `templates/claude-md-block.md`, the block the plugin writes into a
     consuming repository's `CLAUDE.md`. Its rules govern a session's own
     conduct, and the principle governs how this repository designs a gate.
     The owner named `CLAUDE.md` *The rule a mechanism is kept against* as
     the home.
   - The neighbouring principle that a shape the single-issue automation
     flow cannot produce is stated as a limit and not guarded. It is a
     second session memory, and nobody asked for it in #1031.
   - Any change to `hooks/routing-edit-gate.py` or to the pull request's
     trailer arm. The principle keeps both as they are.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The sentence stands where it was framed | Given the branch after phase 1, when `CLAUDE.md` *The rule a mechanism is kept against* is read, then the two sentences of *Scope* item 1 stand directly after `existing is no reason to keep it.`, word for word, and every other sentence of the section is unchanged | `git diff 61a8455a -- CLAUDE.md` shows the insertion and line reflow only, with no word of the old text changed (`git diff --word-diff`) |
| S2 It has one source | Given the tree after phase 1, when `git grep -n 'only such a change passes through'` runs, then it finds `CLAUDE.md` alone outside `seal/specs/` | the grep, executed by the smith and re-run by the warden |
| S3 A gate proposed for chores has its answer | Given a review or a design that lists a shell-only change slipping past a gate as a weakness, or proposes a gate that catches only such changes, when the reviewer reads `CLAUDE.md`, then the section names that gap as not a weakness to close | read by the warden at review |
| S4 Nothing in the tree states the opposite | Given the tree after phase 1, when the searches of *Scope* item 3 run again, then every hit is one of the coordinates that table lists as kept | the searches, re-run by the warden |
| S5 The checks that read `CLAUDE.md` stay green | Given the tree after phase 1, when the cases that read `CLAUDE.md` run, then each passes | `bin/test tests/test_rules.py tests/test_the_rules_claude_md_names_have_one_home.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_one_word_one_meaning.py tests/test_a_release_is_sized_by_a_criterion.py -q`, run by the smith |

## Data & interfaces

None. The change is two sentences of prose at `CLAUDE.md:17`, inside
*The rule a mechanism is kept against*. No code, hook, test or record format
changes.

## Rule changes

- nothing
  why: the one rule this work adds is two sentences of CLAUDE.md, which is
    outside the policy root docs, so the build writes it in place and settle
    has nothing to apply.

## Removes

- nothing
  why: the work adds two sentences and takes nothing out of the tree. The
    session memory that held the principle lies outside the repository, and
    the orchestrator removes it after the merge.

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-26 by framer, before the build.
