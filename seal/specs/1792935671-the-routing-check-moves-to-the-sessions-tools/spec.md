# Feature Specification: 1792935671-the-routing-check-moves-to-the-sessions-tools

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | Between two designs that catch the same defect, the one that stops to ask a person costs more. Every refusal this work adds is a deny addressed to the model, and nothing it adds asks mid-run |
| `CLAUDE.md` *The rule a mechanism is kept against* | A mechanism stays only while what it catches outweighs what it costs. Each job of the git hooks is weighed below against a home outside git, and one with no home and a reason to keep would stay. None is found that needs git |
| The owner's four decisions of 2026-10-25, given in conversation to the orchestrator, carried into this frame as nobody's finding (answerer: the owner) | (1) The routing check governs the session, so it belongs at the session's tools before the first edit and at the pull request, not at git. (2) A check at git's level reaches people who do not use SpecSeal: the person committing from a terminal in the clone, and teammates through any shared hook configuration. (3) A line in husky's, the pre-commit framework's or lefthook's committed configuration is set aside on that ground. (4) The pull-request rule judges only commits a session made, never a teammate's own |
| `skills/implement/SKILL.md` *1. Read the spec before the code* | The routing is decided before the first edit. Today the commit is the stand-in for that moment; this work checks the moment itself |
| `docs/the-review-and-parity-arms.md` *The declaration, and where the check went*, with the rule changes of `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/spec.md` applied | A declaration naming the branch routes the work item, for either answer. Every way the lookup fails is *no declaration*, and the fail direction is a stop. Under `through the review chain` both arms are already quiet at the commit and the parity check is at the pull request |
| `docs/the-commit-gate-inside-git.md` (whole) | The stubs, their session test, the review and parity arms inside git, the `sealed`-off-the-branch refusal, the `--no-verify` backstop, the sequencer exemption and the text reading's stand-aside. The table in *Data & interfaces* says where each goes |
| `docs/commit-review-gate-spec.md` *Registration* and *The implementer mark and notice* | A gate that raises is skipped and said once at the end of the turn. The implementer notice is a `post-bash` reminder that reads `git commit` from the command |
| `docs/the-review-record.md` *The stamp* | One stamp per work item, from the sealer's `sealed`, queued at the commit in shared mode and at the write in local mode, with the refusal record that keeps a refused `sealed`'s repair drawable |
| `docs/the-review-record.md` *What the check reads at the pull request* | `chain-check` passes a pull request that declares nothing, with a notice. Where `seal/parity.md` is declared, each chain round record carries an `original:` line (from 1792619408) |
| `docs/worktree-guard-spec.md` *Which tree* and *Choice sites* | The guard reads commands through the frozen reader, and its tokens are read by `hooks/tokens.py#given`, which stays |
| Issue #952 *The change*, step 4 (read, open) | A pull request that touches nothing under `seal/` owes nothing in any step `templates/hygiene.yml` runs. The trailer arm below judges no commit that lacks the session's own trailer, so a teammate's pull request stays unjudged |
| `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md` and `seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md` (unsettled) | They rewrite check lines and one sentence in the documents this work changes. Every `from` below is written against the text as it reads once they apply, in merge order |

## Scope

In:

1. **The edit check.** A new `PreToolUse` gate on `Write|Edit|NotebookEdit`, `hooks/routing-edit-gate.py`, refuses an edit of a file in an opted-in repository's worktree while no routing declaration names that worktree's branch and the session has not recorded that its change belongs to no work item. `seal no-work-item` writes that record.
2. **The pull-request check.** Every session commit in a repository whose root is shared carries the trailer `SpecSeal-Routing: <work-item-id>` or `SpecSeal-Routing: no work item`; at a local root none does. At a shared root, `chain-check` fails a ready pull request where one of its own commits, committed by its author, names a work item that no declaration it judges names; at a local root such a trailer is printed and never refused. A commit without the trailer is not judged, and neither is one whose committer email differs from its author email, compared case-folded.
3. **The parity arm's last commit-time case moves to the pull request.** Under `straight to the PR`, where `seal/parity.md` is declared and the change reaches outside the document roots, the sealer's `guarantee.md` carries one `original:` line naming the baseline, read as a round record's line is read.
4. **Git's other jobs move to session hooks.** In shared mode the stamp is queued at the write of `guarantee.md`, as local mode does already, and the refusal record is written there in both modes. The implementer notice keeps only its `post-bash` reading.
5. **Nothing is installed into git any more.** The three stubs, the installer's write path, `hooks/commitgate.py`, the arms inside git, the text reading `hooks/commit-review-gate.py`, the old waiver's carriers (`hooks/answers.py`, `hooks/answer-write.py`, `hooks/answer-clear.py`), the review mark and the parity mark are removed. `hooks/stub-remove.py` takes out, at session start, the stubs an earlier release wrote.
6. **Settle can remove a document.** A `remove` with no `from` whose `section` names two headings, one inside the other, removes the outer one, and a document a `remove` leaves empty is deleted. Without this, the two documents this work retires cannot leave `docs/` at settle: the title and the first section of `docs/the-commit-gate-inside-git.md` read the same text.
7. The agent contract, skills, agent definitions, templates and READMEs stop describing the commit gate (see *Removes*).

Out:

- **Integration with husky, the pre-commit framework or lefthook.** The owner set it aside (decision 3).
- **#952's mode question and its `hygiene.yml` steps.** That issue owns them. This work keeps to its step 4: no commit without the session's trailer is judged.
- **The worktree guard's reading.** It reads commands through the frozen reader, `hooks/cmdline_base.py`, which no git hook can replace (the convergence argument moves to `docs/worktree-guard-spec.md` *Which tree*). `hooks/cmdline.py` stays for the guard, `hooks/tokens.py#given` and `hooks/implementer-notice.py`, as #1014's frame enumerated. Only the units that the commit gate alone reaches go.
- **The session lease.** `hooks/session-lease.py` stays for the worktree guard. Only the commit gate's lease route in `hooks/hooksession.py` goes.
- **Retiring `hooks/stub-remove.py`.** A later release can retire it once its own history shows no clone still carries a stub. Plan *Operational impact* says so.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 undeclared edit refused | Given an opted-in repository on a branch no `routing.md` names and no no-work-item record for the session, when the session calls `Edit` on `src/a.py`, then the gate denies with a reason naming the declaration path and `seal no-work-item` | `tests/test_routing_edit_gate.py`, payload in process |
| S2 declared edit allowed | Given a `routing.md` naming the checked-out branch, for either `Review` answer, when the session edits any file, then the gate is silent | `tests/test_routing_edit_gate.py` |
| S3 the declaration can be written | Given no declaration, when the session writes `seal/specs/<id>/routing.md` under either root, then the gate is silent | `tests/test_routing_edit_gate.py`, shared and local mode |
| S4 no work item | Given no declaration, when `seal no-work-item` has run in this clone under this session's `CLAUDE_CODE_SESSION_ID`, then an edit is allowed; under another session id it is denied | `tests/test_routing_edit_gate.py`, `tests/test_seal.py` |
| S5 the edited file decides | Given the payload's `cwd` in a repository that has not opted in and `file_path` in a worktree of one that has, then the edited file's repository and branch are judged, and in the reverse case nothing is | `tests/test_routing_edit_gate.py` |
| S6 not judged | A file git ignores, a file outside every repository, a file in a repository that has not opted in, and `NotebookEdit`'s `notebook_path` under a declared branch are all silent | `tests/test_routing_edit_gate.py` |
| S7 paused rebase | Given a rebase paused on a conflict of a declared branch, with HEAD detached, when the session edits the conflicted file, then the branch the rebase names is read and the edit goes ahead | `tests/test_routing_edit_gate.py` |
| S8 press | Under the `automation` press the deny names no question tool; attended, it tells the model to put the routing question with `AskUserQuestion` | `tests/test_routing_edit_gate.py` |
| S9 subagent | A subagent's `Edit` in an undeclared opted-in scratch repository meets the same deny | executed once by the orchestrator in a live session (`questions.md` Q3); no case can run the harness |
| S10 trailer arm | Given a ready pull request with no declaration at a shared root, when one of its commits, committed by its author, carries `SpecSeal-Routing: <id>`, then `chain-check` exits 1 naming the commit and the id; one reading `no work item` is printed as a notice; a commit without the trailer is not named | `tests/test_chain_check.py` under marker `routing-trailer-at-the-pull-request` |
| S11 a teammate's pull request | Given commits with the harness's `Co-Authored-By` trailer and no `SpecSeal-Routing`, then `chain-check` judges nothing about them | `tests/test_chain_check.py` |
| S12 parity under the direct answer | Given `seal/parity.md` and a `straight to the PR` work item changing code, a ready pull request fails while `guarantee.md` holds no `original:` line naming the baseline, and passes with one | `tests/test_chain_check.py` under marker `parity-in-the-guarantee` |
| S13 shared-mode stamp | Given shared mode, when the sealer's `Write` leaves `seal/specs/<id>/guarantee.md` reading `sealed` over a commit the declared branch holds, then the stamp is queued once, and the `Stop` hook draws it; a second write of the same verdict queues nothing | `tests/test_sealer_stamp_queue.py`, `tests/test_seal_stamp.py` |
| S14 refused `sealed` | Given a `sealed` whose audited commit the declared branch does not hold, when it is written, then nothing is queued, the refusal record is written and one line names the commit and the branch; the new audit that keeps it as `; earlier run: <sha> sealed` draws the stamp even after the stale row was committed | `tests/test_seal_stamp.py` under marker `refused-sealed-leaves-a-record` |
| S15 old stubs go | Given a clone holding the three marker-carrying stubs and a foreign `pre-commit` without the marker, when a session starts there, then the three are removed and the foreign file is untouched | `tests/test_stub_remove.py` |
| S16 nothing writes into git | After the removal phase, no file of the plugin writes under a hooks directory, and `hooks/hooks.json` registers no `pre-bash` gate that reads a commit | `tests/test_dispatch.py`; `git grep` over `hooks/` for `hooks_dir` and `core.hooksPath` |
| S17 a person's commit | A commit typed in a terminal in an opted-in clone runs no SpecSeal code | `tests/test_stub_remove.py` (no stub left) |
| S18 settle retires a document | A spec whose `remove` names `The commit gate inside git` in a document titled and sectioned by that text removes the document from the policy root, and fold-check passes once the index row goes with it | `tests/test_rule_changes.py`, `tests/test_settle.py` |
| S19 the frame parses | This file's `## Rule changes` parses under `skills/settle/scripts/rule_changes.py#parse` | `chain-check` at the pull request |

## Data & interfaces

**The edit gate's payload.** `tool_name` among `Write`, `Edit`, `NotebookEdit`; `tool_input.file_path`, or `tool_input.notebook_path` for `NotebookEdit`; `session_id`; `transcript_path` for the press. The `cwd` is not read for the target.

**The no-work-item record.** `<git-common-dir>/specseal-no-work-item/<session-id>`, an empty file, the id reduced to its basename. `seal no-work-item` reads the session from `CLAUDE_CODE_SESSION_ID` and the clone from its working directory, or from `--root`, and writes nothing where either is missing. Records older than a day are pruned when one is written, as leases are.

**The trailer.** One line in the commit message's trailer block, `SpecSeal-Routing: <work-item-id>` or `SpecSeal-Routing: no work item`, written at a shared root only. It is read with git's own trailer parser, `git log --no-merges --reverse -z --format=%H%x1f%ae%x1f%ce%x1f%(trailers:key=SpecSeal-Routing,valueonly,separator=%x1e) <base>..HEAD`, so the key matches as git matches it, and a commit whose author and committer emails differ, case-folded, is skipped (`chain_check.py#routing_trailers`).

**Registration.** `hooks/hooks.json` gains `PreToolUse` with matcher `Write|Edit|NotebookEdit` running `dispatch.py pre-edit`. `hooks/dispatch.py#GROUPS` gains `"pre-edit": ("routing-edit-gate.py",)`, drops `hook-install.py`, `answer-write.py` and `commit-review-gate.py` from `pre-bash` and `answer-clear.py` from `post-bash`, and replaces `hook-install.py` in `session-start` with `stub-remove.py`.

**Where each job of git's hooks and of the text reading goes.** The jobs were enumerated from the code at `36a78242`, by construction: every branch of `hooks/commitgate.py#pre_commit`, `#reference_transaction` and `#post_commit`, every arm of `hooks/gate.py#arms_missing`, and the decisions of `hooks/commit-review-gate.py#main`.

| Job | Today | Goes to |
|---|---|---|
| Review arm on an undeclared branch | `pre-commit` and `reference-transaction` through `gate.py#arms_missing`; the text reading where git cannot | the edit check, before the first edit, and the trailer arm at the pull request |
| Review mark `specseal-reviewed` | read by the review arm only; written by the orchestrator (`skills/code-review/orchestration.md`) | nothing: no reader is left, so the write goes too |
| Parity arm under `straight to the PR` | `pre-commit` and the text reading, against `specseal-parity` | the sealer's `original:` line in `guarantee.md`, read by `chain-check` |
| Parity arm on an undeclared branch | `pre-commit` and the text reading | at a shared root the trailer arm refuses a session's own work-item commits first; `no work item` stands as `[no-parity]` did, visible in history |
| Parity mark `specseal-parity` | written by `legacy-parity`, read by the parity arm only | nothing: no reader is left |
| Waivers `[no-review]`, `[no-parity]`, `git -c specseal.waive=` | read by the arms; the bare word carried to git by `answers.py`, `answer-write.py`, `answer-clear.py` | `seal no-work-item` for edits, the trailer's `no work item` for the pull request |
| Session test (a person's commit is not judged) | `hooksession.py#session`, leases, the stub's short-cut | nothing to decide: no stub runs, so a person's commit runs no SpecSeal code |
| Automation press in a refusal | `gate.py#refusal`, `commit-review-gate.py` | the edit check's deny text |
| Sequencer commits not judged | `commitgate.py#_sequencer_commit` | the edit check reads a paused rebase's branch, and allows a detached HEAD whose commit a declared branch holds; commits are not judged locally at all |
| `sealed` over a commit the branch does not hold | `pre-commit` refuses the commit and writes the refusal record | the pull request's guarantee arm refuses the landed row as stale (it already does), and the write-time queue writes the refusal record in both modes |
| `--no-verify` backstop | `reference-transaction` | nothing to back up: there is no local refusal to skip |
| Implementer notice | `post-commit`, and `post-bash` where git does not decide | `post-bash` alone, always |
| Shared-mode stamp queue | `post-commit` through `seal_stamp.queue_for_guarantee` | `hooks/sealer-stamp-queue.py` at the write, under local mode's rule, in both modes |
| Installer | `hooks/hook-install.py` at session start and first in every Bash call's `pre-bash` group (a median 113 ms per Bash call, `docs/the-commit-gate-inside-git.md` *Known limits*) | `hooks/stub-remove.py`, at session start, removing marker-carrying stubs only |
| Text reading's which-repository resolution, unresolved-target stop, deny-then-ask record | `hooks/commit-review-gate.py` | nothing: no commit is read from a command |

## Rule changes

- add
  file: docs/the-routing-check.md
  to: # The routing check

    Authority for where a session's routing is checked: at its edit tools,
    before the first edit, and at the pull request. What each routing answer
    owes at the pull request is `docs/the-review-and-parity-arms.md`. How the
    hooks are registered is `docs/the-session-hooks.md`. Update spec and code
    together.

    ## Where the routing is checked

    **A session's routing is checked where the session acts, at its edit
    tools before the first edit, and again at the pull request; this plugin
    writes nothing into a clone's git hooks.** The routing governs a
    session, and git's hooks run for every commit made in the clone, a
    person's own from a terminal included. The hooks slot is also where
    husky, the pre-commit framework and lefthook live, and a line or an entry
    in their committed configuration reaches every teammate. A check at git's
    level reaches people who do not use this plugin, with an experience they
    did not ask for (the owner, 2026-10-25).
    check: tests/test_routing_edit_gate.py tests/test_stub_remove.py

    **A session takes out, at its start, the git hook stubs an earlier release
    of this plugin wrote into its clone.** A stub is a hook file carrying the
    marker line `# specseal-git-hook`, and a hook file without it is never
    touched. Each stub ran the plugin copy whose absolute path it names, so
    after an upgrade it goes on judging commits with the old copy for as long
    as that copy stays on disk. A clone no session of this release starts in
    keeps its stubs, and a person removes them by deleting the files that
    carry the marker.
    check: tests/test_stub_remove.py

    ## The edit check

    **`hooks/routing-edit-gate.py` refuses a `Write`, `Edit` or `NotebookEdit`
    of a file in an opted-in repository's worktree while no routing
    declaration names the branch checked out there and the session has not
    recorded that its change belongs to no work item.** The repository and
    the branch are the edited file's: its path is resolved to a worktree,
    never the payload's `cwd`, because a session can edit a tree its working
    directory is not in. A detached HEAD names no branch, with two
    exceptions. During a paused rebase the branch the rebase names stands for
    it. And a detached HEAD whose commit a branch some declaration names
    already holds, under `refs/heads/<branch>` or a remote-tracking
    `refs/remotes/<remote>/<branch>`, is allowed, because commits made there
    reach a pull request only through a branch, which this gate and the
    trailer arm judge. The tool
    input is a path, so no command is read. Every way the declaration cannot
    be read is no declaration, as `docs/the-review-and-parity-arms.md` states.
    check: tests/test_routing_edit_gate.py

    **Three kinds of file are not judged: one under the repository's `seal/`
    root, one git ignores, and one outside every opted-in repository.** The
    root holds the routing record and the records that follow it, so writing
    the declaration is never refused for the want of one. An ignored file
    never lands in a commit. Anything else belongs to nothing this plugin
    governs.
    check: tests/test_routing_edit_gate.py

    **A change that belongs to no work item is recorded per session by
    `seal no-work-item`, and the record lets that session edit in that
    clone.** It
    is `<git-common-dir>/specseal-no-work-item/<session-id>`, the session read
    from `CLAUDE_CODE_SESSION_ID`. Nothing verifies who ran it, the standing
    the per-command waiver had: an audit trail, in the transcript and, at a
    shared root, in each commit's trailer at the pull request, not an
    authorization. A record that
    cannot be read is no record.
    check: tests/test_routing_edit_gate.py tests/test_seal.py

    **A refusal is a deny addressed to the model, with the same text every
    time.** It names the declaration to write, at the path `routing.md` takes
    under the repository's root, and `seal no-work-item`. Where the person
    pressed `automation` on the routing question, read through
    `hooks/worktree_consent.py#automation_answered`, it names no question
    tool; otherwise it tells the model to put the routing question to the
    person with `AskUserQuestion`. Re-issuing the edit unchanged meets the same
    refusal.
    check: tests/test_routing_edit_gate.py

    **The check reaches a subagent's edits as it reaches the main session's,
    and an edit made through the shell reaches neither.** A subagent's tool
    call runs the same hooks and carries the main session's id. A `sed -i`, a
    redirection or a script writes a file with no edit tool, which is why every
    agent edits through the `Edit` tool (`skills/agent-contract/SKILL.md` rule
    9), and at a shared root the pull request's trailer arm, as *At the pull
    request* below states, is what remains for such a change.
    check: none reader: the orchestrator on the first live run after a change here

    ## At the pull request

    **A session's commit in a repository whose root is shared ends with one
    trailer, `SpecSeal-Routing:`, naming its work item or reading
    `no work item`; at a local root a commit carries none.** It tells a
    session's commit from a person's: the harness's co-author trailer is
    carried by any Claude Code session, a teammate's who does not use this
    plugin included, and a person's own commit carries neither. At a local
    root no declaration is ever committed for a trailer to name, and the
    history belongs to a team that does not run this plugin.
    `skills/commit-pr-convention/SKILL.md` is where a session reads it.
    check: skills/commit-pr-convention/SKILL.md

    **At a shared root, `chain-check` fails a ready pull request where one of
    its own commits, committed by its author, carries a `SpecSeal-Routing`
    trailer naming a work item that no declaration it judges names, and
    prints each commit whose trailer reads `no work item`.** A commit with no
    such trailer is not judged, so a teammate's never is, and neither is a
    session's that dropped the trailer: that is what judging no teammate
    costs. A commit whose committer email differs from its author email,
    compared case-folded, is not judged either, because its committer did not
    write the trailer: GitHub's squash is one such commit, and a person's
    cherry-pick or rebase under another identity is another. The cost is that
    a person's cherry-pick of their own session's commit under the same
    identity is still judged. At a local root a work item's trailer is printed
    as a notice and never refused. The commits are the pull request's own,
    merges left out, and the trailer is read by git's own trailer parser.
    check: routing-trailer-at-the-pull-request
- add
  file: docs/the-session-hooks.md
  to: # The session hooks

    Authority for how the hooks are registered and for the implementer mark.
    Where a session's routing is checked is `docs/the-routing-check.md`. The
    review run the hooks serve is `docs/the-review-record.md`. Update spec and
    code together.

    ## Registration

    `hooks/hooks.json` registers `hooks/dispatch.py <group>` per event, and the
    dispatcher runs every gate of the group in one interpreter. A gate stays a
    standalone script, and adding one means adding it to `GROUPS` in
    `dispatch.py`. Where several gates of a group decide, the strictest wins
    (deny, then ask, then silence) and every reason is kept in the merged text.
    A gate that raises is skipped, and the rest of the group decides without
    it.

    **A gate that fails is said once per session, at the end of the main
    session's turn, and the call it failed on still goes ahead.** A failure is
    an exception while loading the gate's file, a `SystemExit` included, or an
    `Exception` from its `main()`; a `SystemExit` from `main()` is a gate
    finishing. The dispatcher writes a record under
    `<git-common-dir>/specseal-gate-failure/`, keyed by session and gate, in an
    opted-in repository and wherever `optin.py` is itself the broken module.
    The `stop` group says each pending record once as a `systemMessage`, before
    the sealer's stamp where there is one, and the report carries no decision.
    A failure in a git directory the dispatcher cannot write to is not said. No
    case sees how the harness renders the report beside the stamp, on any
    platform, and two hook processes racing for one record are forced in
    process, never run.
    check: tests/test_dispatch.py tests/test_a_gate_that_fails_says_so.py

    ## The implementer mark and notice

    **A `framer` or `smith` spawn leaves a mark, and a commit on a branch whose
    declaration names that agent, with no mark standing, gets one line saying
    so.** The two axes of the routing declaration that name an agent,
    `Planning` and `Implementation`, each answer an agent's name or
    `the session`. Two hooks share one address module, `hooks/implementer.py`,
    for both axes.

    | Hook | Fires | Does |
    |---|---|---|
    | `implementer-mark` (`pre-agent`) | an Agent or Task spawn whose `subagent_type` is `framer` or `smith` | writes the checked-out branch name to `<git-dir>/specseal-planner` or `<git-dir>/specseal-implementer`, and prints nothing |
    | `implementer-notice` (`post-bash`) | a command that invokes `git commit` | where the branch's declaration names an agent on an axis and no mark of that axis stands for the branch, prints one line naming the file, one line for both axes where both are unfulfilled, once per session per repository; silent for an axis whose mark stands, whose row is absent or outside its vocabulary, or which answers `the session` |

    Neither hook can deny or ask. A mark is keyed on the branch, because a work
    item commits many times, and on the axis, because `smith` is spawned on
    nearly every work item. It lives in the git directory, so nothing at the
    pull request reads either axis. Everything fails toward no mark, which is
    toward the reminder.
    check: tests/test_implementer_mark.py tests/test_implementer_notice.py
- remove
  file: docs/the-commit-gate-inside-git.md
  section: The commit gate inside git
- remove
  file: docs/commit-review-gate-spec.md
  section: The commit gate's PreToolUse reading
- remove
  file: docs/README.md
  section: docs/
  from: | `docs/commit-review-gate-spec.md` | how the gates are registered, what the PreToolUse reading of a commit decides where git cannot, and what the implementer mark says |
- remove
  file: docs/README.md
  section: docs/
  from: | `docs/the-commit-gate-inside-git.md` | what git decides inside a commit, what its hooks cannot see, and which reading judges each state of a repository |
- change
  file: docs/README.md
  section: docs/
  from: | `docs/the-review-and-parity-arms.md` | what each opt-in arm of the commit gate wants, and the routing declaration that moves the review arm's check, and under `through the review chain` the parity arm's, to the pull request |
  to: | `docs/the-review-and-parity-arms.md` | what each routing answer owes at the pull request, and what the parity arm wants of a change in a migration |
- change
  file: docs/README.md
  section: docs/
  from: | `docs/the-review-record.md` | what a review round leaves in the tree, what the pull-request check reads of it, the run's bound and end, and how work is handed to an agent |
  to: | `docs/the-review-record.md` | what a review round leaves in the tree, what the pull-request check reads of it, the run's bound and end, and how work is handed to an agent |
    | `docs/the-routing-check.md` | where a session's routing is checked: at its edit tools before the first edit, and at the pull request |
    | `docs/the-session-hooks.md` | how the hooks are registered, and what the implementer mark says |
- change
  file: docs/the-review-and-parity-arms.md
  section: The review and parity arms
  from: Authority for the two opt-in arms of the commit gate, the review arm and the
    parity arm: what each wants before a commit, its mark, its waiver and where it
    stays silent, and the routing declaration that moves the review arm's check, and
    under `through the review chain` the parity arm's, to the pull request.
  to: Authority for what each routing answer owes at the pull request, and for
    the parity arm: what a change in a migration owes, and where that is checked.
- change
  file: docs/the-review-and-parity-arms.md
  section: The review and parity arms
  from: Where the arms are asked from is
    `docs/the-commit-gate-inside-git.md`, inside the commit where this plugin's
    git hooks run, and `docs/commit-review-gate-spec.md`, the PreToolUse reading
    where they do not.
  to: Where a session's routing is checked, at its edit tools and at the pull
    request, is `docs/the-routing-check.md`.
- change
  file: docs/the-review-and-parity-arms.md
  section: The two arms of the commit gate
  from: The two arms are evaluated independently: each has its own mark, waiver token
    and silence, and one arm's mark never quiets the other. A routing
    declaration answering `through the review chain` quiets both arms at the
    commit, and each arm's check then moves to the pull request. They are not declared
    independently: the migration config lives at `seal/parity.md`, so declaring it
    creates `seal/`, which opts into the review arm too. A repository that wants
    the parity arm alone waives the review arm per command.
  to: **No arm runs at the commit.** The review arm became the routing check,
    which runs at a session's edit tools and at the pull request
    (`docs/the-routing-check.md`), and the parity arm is checked at the pull
    request alone, as *Parity arm* below states. The migration config lives at
    `seal/parity.md`, so declaring it creates `seal/`, which opts the
    repository into the routing check too.
    check: tests/test_routing_edit_gate.py tests/test_chain_check.py
- change
  file: docs/the-review-and-parity-arms.md
  section: Review arm
  from: Opt-in: `seal/` at the repository root, or under the common git directory in
    local mode.
    | Condition | Decision |
    |---|---|
    | the waiver in the command | silent, and visible in history |
    | a `routing.md` declaration names this branch, for either answer | silent: the routing question was answered before the first edit, and CI checks the answer at the pull request |
    | `specseal-reviewed` equals current HEAD | satisfied |
    | the change confined to `docs/`, `seal/` | no different from any other change — this arm reads no paths. The paragraph below says why |
    | otherwise | contributes a stop |
    **The review arm reads no paths: a change confined to `docs/` and `seal/`
    meets it as any other change does, and a lighter tier is declared, never
    inferred.**
    **Why this arm has no document-root line.** The parity arm asks whether the
    original was consulted, and a `docs/` file has no original, so its silence
    there is right. This arm asks whether anybody reads the change before it
    lands, and `docs/` is the policy the code conforms to; review finds defects
    there as it does in code. A documentation pass that should reach nobody is
    routed that way before the first edit, by declaring `straight to the PR`; it
    is never inferred from the paths it touches.
    check: review-arm-asks
  to: **The review arm is the routing check, and it runs at a session's edit
    tools and at the pull request, never at the commit.** What it refuses, what
    it reads and what waives it are `docs/the-routing-check.md`. A change
    confined to `docs/` meets it as any other change does, because `docs/` is
    the policy the code conforms to and review finds defects there as it does
    in code. A documentation pass that should reach nobody is routed that way
    before the first edit, by declaring `straight to the PR`; it is never
    inferred from the paths it touches.
    check: tests/test_routing_edit_gate.py
- remove
  file: docs/the-review-and-parity-arms.md
  section: Review arm
  from: **The waiver goes in front of the command.** After `git commit` a bare word is
    a pathspec and git rejects the command, and a `#` comment is no comment in
    interactive zsh, so `: '[no-review]'; git commit …` puts the token inside a
    no-op `:`, where the shell discards it and the history keeps it.
    `git -c specseal.waive=review commit …` is the same waiver in git's own
    spelling, and the one a refusal names first.
    check: tests/test_commit_review_gate.py
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: **The gate reads `seal/specs/<work-item-id>/routing.md` before it reads
    anything else.** Where a declaration is in force the review arm stays silent
    for either answer, because asking for the waiver as well would ask for the
    same answer twice.
  to: **The routing check reads `seal/specs/<work-item-id>/routing.md` before it
    reads anything else.** Where a declaration names the branch, an edit goes
    ahead for either answer, because the routing question was answered before
    the first edit.
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: | The declaration says | At the commit | At the pull request |
  to: | The declaration says | At an edit | At the pull request |
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: | through the review chain | silent |
  to: | through the review chain | allowed |
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: | straight to the PR | silent |
  to: | straight to the PR | allowed |
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: | nothing readable, or no file | the review arm's table above | pass, with a notice saying nothing was checked |
  to: | nothing readable, or no file | refused, unless the session recorded that its change belongs to no work item | each commit's `SpecSeal-Routing` trailer is judged as `docs/the-routing-check.md` *At the pull request* states; nothing else is checked, and a notice says so |
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: **There is no standing waiver: a declaration moves the review arm's check to
    the pull request, and the waiver stays per command.**
  to: **There is no standing waiver: a declaration moves the review arm's check to
    the pull request, and a change no work item owns is recorded per session,
    never per branch.**
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: and therefore to
    **asking**:
  to: and therefore to
    **refusing the edit**:
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: Deleting the routing file restores the review arm's table exactly.
  to: Deleting the routing file brings the edit check's refusal back.
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: Ported behaviour follows the original where policy is silent, so a commit
    that changes code carries a record that the original was consulted. Mark:
    `<git-dir>/specseal-parity`, written by the `legacy-parity` skill after an
    actual comparison.
  to: Ported behaviour follows the original where policy is silent, so a change
    to code carries a record, in the tree, that the original was consulted.
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: | Condition | Decision |
    |---|---|
    | `[no-parity]` in the command, placed as the review arm's waiver is | silent, and visible in history |
    | a `routing.md` declaration names this branch and answers `through the review chain` | silent: every round record carries the comparison, and CI checks it at the pull request |
    | the change confined to `docs/`, `seal/` | silent: nothing there can be compared against an original |
    | `specseal-parity` equals current HEAD | satisfied |
    | otherwise | contributes a stop |
  to: | The declaration says | Where the comparison is recorded |
    |---|---|
    | through the review chain | each round record's `original:` line |
    | straight to the PR | one `original:` line in the sealer's `guarantee.md` |
    | none | nowhere: each commit's `SpecSeal-Routing` trailer is judged as `docs/the-routing-check.md` *At the pull request* states, and one reading `no work item` stands as the per-command waiver did, visible in history |
    | any, for a change confined to `docs/`, `seal/` | nothing is owed: nothing there can be compared against an original |
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: "The change" is every path the commit would carry: `changed_paths()` reads
    the staged diff and what `-a` and a trailing pathspec pick up.
  to: "The change" is every path the pull request changes against its base.
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: Where a `git diff` that lists the paths exits non-zero, cannot start or times
    out, the paths are unknown and the arm stops. The PreToolUse reading,
    `pre-commit` and the `reference-transaction` backstop read the paths through
    one runner, `hooks/gate.py#git`, which answers None for a failure, and
    `hooks/gate.py#touches_code` answers True for None, a branch with no commit
    yet included.
  to: Where the pull request's diff cannot be listed, the check ends with exit 2
    before any record is judged, and `hooks/gate.py#touches_code` answers True
    for a list it was not given.
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: check: tests/test_commit_review_gate.py tests/test_commitgate.py tests/test_gate.py
  to: check: tests/test_gate.py tests/test_chain_check.py
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: **A declaration answering `through the review chain` moves the parity
    arm's check to the pull request, and one answering `straight to the PR`
    leaves it at the commit.**
  to: **A declaration answering `through the review chain` moves the parity
    arm's check to the round records, and one answering `straight to the PR`
    to the sealer's guarantee.**
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: Under `straight to the PR`
    no review round records a comparison, so the arm stays at the commit as
    the table above states, and under the press a code commit there is
    refused and handed back at the end of the run.
  to: Under `straight to the PR`
    no review round records a comparison, so the sealer compares the audited
    commit with the original through `legacy-parity` and writes the line in
    `guarantee.md`, where the check reads it as it reads a round record's.
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: check: parity-quiet-under-the-chain
  to: check: parity-at-the-pull-request parity-in-the-guarantee
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: The mark says a comparison was recorded, not that it was a good one.
  to: An `original:` line says a comparison was recorded, not that it was a good one.
- add
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  to: **Where `seal/parity.md` is declared and the change reaches outside
    `docs/` and `seal/`, the `guarantee.md` of a work item declaring
    `straight to the PR` carries one `original:` line naming the migration
    config's baseline.** The sealer writes it after comparing the audited
    commit with the original through `legacy-parity`, and the check reads it by
    the rule a round record's line is read by: a ready pull request fails while
    the guarantee holds no such line, or one whose commit and the
    `Baseline commit` row's SHA are not one a prefix of the other. What the check cannot
    read is whether the comparison was a good one, which is the sealer's.
    check: parity-in-the-guarantee
- add
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  to: **On every pull request, the check reads the `SpecSeal-Routing` trailer of
    each of its own commits, as `docs/the-routing-check.md` *At the pull
    request* states.**
    check: routing-trailer-at-the-pull-request
- change
  file: docs/the-review-record.md
  section: The stamp
  from: at the end of the turn in which `guarantee.md` came to read it: at its commit in
    shared mode, and at its write in local mode.**
  to: at the end of the turn in which `guarantee.md` came to read it, at its
    write, in either mode.**
- change
  file: docs/the-review-record.md
  section: The stamp
  from: In shared mode git's
    `post-commit` runs after the commit, in the worktree it landed in. Where the
    commit carries a work item's `guarantee.md` whose one `Verdict:` reads
    `sealed`, it writes the stamp's values under
    `<git-common-dir>/specseal-stamp/<session>/` and prints one line naming the
    file and `seal-stamp --from <path>`. In local mode the `seal/` root sits under
    the git common dir and no commit carries `guarantee.md`. So a `post-edit`
    gate, `hooks/sealer-stamp-queue.py`, runs after each `Write` or `Edit` of
    `<git-common-dir>/seal/specs/<id>/guarantee.md`. It writes the same values for the
    payload's session, which a subagent's write carries as the main session's,
    and says the same line as its message.
  to: A `post-edit` gate, `hooks/sealer-stamp-queue.py`, runs after each `Write`
    or `Edit` of a `seal/specs/<id>/guarantee.md` under either root. Where its
    one `Verdict:` reads `sealed`, it writes the stamp's values under
    `<git-common-dir>/specseal-stamp/<session>/` for the payload's session,
    which a subagent's write carries as the main session's, and says one line
    naming the file and `seal-stamp --from <path>` as its message.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: a commit whose audited commit is not in its own history, a squash or a
    cherry-pick of the guarantee elsewhere, queues nothing; and a guarantee that
    read `sealed` at an earlier commit of that history,
  to: a `sealed` whose audited commit is not an ancestor of the branch the work
    item's `routing.md` names queues nothing; and in shared mode a guarantee
    that read `sealed` at an earlier commit of HEAD's history,
- change
  file: docs/the-review-record.md
  section: The stamp
  from: Two writers leave it, each for a row
    that stands in its own clone and nowhere else. In shared mode the commit gate
    writes it when it refuses the commit of that row
    (`docs/the-commit-gate-inside-git.md`), so the row never became history. In
    local mode the local writer writes it where the `Branch` row's branch stands,
    and says one line naming the commit and the branch, since no pull request's
    check reads a local guarantee.
  to: One writer leaves it, for a row that stands in its own clone and nowhere
    else: `hooks/sealer-stamp-queue.py`, in either mode, where the `Branch`
    row's branch stands and does not hold the audited commit. It says one line
    naming the commit and the branch. In shared mode the pull request's check
    refuses the same row as stale; in local mode no check reads it.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: `sealed_before`
    asks no record: a `sealed` in the history drew where it was made, or was
    committed where no gate judged it, and either way it counts. `post-commit`
    writes none.
  to: `sealed_before`
    skips a `sealed` this clone recorded refusing, as the earlier-run chain
    does, because no gate stops a refused row from becoming history before the
    pull request's check refuses it; any other `sealed` in the history drew
    where it was made, and counts.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: In
    local mode the line reaches the person as the edit hook's message, and nobody
    has watched that message on a screen yet.
  to: The line reaches the person as the edit hook's message, and nobody has
    watched that message on a screen yet.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: No stamp is queued, and
    nothing is said, where git's hooks slot is somebody else's (`core.hooksPath`,
    or a hook file the plugin did not write), since none of its stubs runs there;
    for a person's own commit with no Claude session behind it, which has no turn
    to draw at; for a local-mode `guarantee.md` that arrived by a shell write or
    `seal import` rather than by `Write` or `Edit`, which no edit hook sees;
  to: No stamp is queued, and
    nothing is said, for a `guarantee.md` that arrived by a shell write, a
    commit fetched from elsewhere or `seal import` rather than by `Write` or
    `Edit`, which no edit hook sees;
- change
  file: docs/the-review-record.md
  section: The stamp
  from: still counts as the work item's stamp, so its repair draws none, where it
    was committed past the commit gate: under `--no-verify`, in a foreign hooks
    slot, under a plugin older than the gate, as a person's own commit, or in a
    clone no session has reached (`docs/the-commit-gate-inside-git.md`); or
    where an amend folded the guarantee into the very commit it audited, which
    `pre-commit` sees as that commit's child and cannot tell from a plain one.
  to: still counts as the work item's stamp, so its repair draws none, where no
    edit hook saw it written: by a shell, by a person, or under a plugin older
    than the hook.
- remove
  file: docs/the-review-record.md
  section: The stamp
  from: Likewise
    a commit that concludes a conflicted merge bringing in a side's `sealed` is
    refused; `docs/the-commit-gate-inside-git.md` gives its way on and why this
    plugin's flow never meets it.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: The gate judges a commit's newest verdict
    alone, never the `; earlier run:` chain,
  to: The hook judges a write's newest verdict
    alone, never the `; earlier run:` chain,
- change
  file: docs/the-review-record.md
  section: The stamp
  from: the gate refuses and records it, and the
    new audit it asks for draws again.
  to: the hook refuses and records it, and the
    new audit it asks for draws again.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: draws a second
    time once the gate refuses and records it,
  to: draws a second
    time once the hook refuses and records it,
- change
  file: docs/the-review-record.md
  section: The stamp
  from: is refused at its
    commit and recorded,
  to: is refused at its
    write and recorded,
- change
  file: docs/the-review-record.md
  section: The stamp
  from: Where a file was written,
    the line `post-commit` printed, or in local mode the edit hook's message,
    names `seal-stamp --from <path>`,
  to: Where a file was written,
    the edit hook's message names `seal-stamp --from <path>`,
- change
  file: docs/worktree-guard-spec.md
  section: Choice sites
  from: the rule the commit gate's waiver read keeps (`hooks/tokens.py#without_bodies`).
  to: the rule `hooks/tokens.py#given` reads every token by
    (`hooks/tokens.py#without_bodies`).
- change
  file: docs/worktree-guard-spec.md
  section: Choice sites
  from: the standing `[worktree-ok]` and `[no-review]`
    have: an audit trail, not an authorization.
  to: the standing `[worktree-ok]`
    has: an audit trail, not an authorization.
- add
  file: docs/worktree-guard-spec.md
  section: Choice sites
  to: **A token counts only where it is typed outside every here-document body,
    and a command that does not split carries none from where its split
    fails.** `hooks/tokens.py#given` keeps comments, because a token may be
    written in one, and skips every heredoc body, a body a shell runs
    included. A token inside a quote that never closes, or after an apostrophe
    in a comment (`# don't [worktree-ok]`), is read as nothing.
    check: executed-text-is-read
- change
  file: docs/worktree-guard-spec.md
  section: Which tree
  from: The guard takes one answer where the commit gate takes all of them:
  to: The guard takes one answer where a reader of every target would take all
    of them:
- remove
  file: docs/worktree-guard-spec.md
  section: Which tree
  from: The commit gate stops on a target like this instead: a commit nobody
    judged is a commit nobody reviewed, while a guard that goes silent leaves a
    shared tree unguarded, and *Unknowns resolve conservatively* weighs a wrong
    deny at one prompt.
- add
  file: docs/worktree-guard-spec.md
  section: Which tree
  to: **No git hook can judge a branch switch or a worktree creation before it
    happens, so the guard's switch and creation arms read the command, and
    that reading does not converge.** No git refuses a branch switch before its
    tree has moved: on 2.34 to 2.43 a switch reaches `reference-transaction`
    with no line at all, and on 2.50.1 the line arrives after the tree and index
    already hold the new branch. A branch-naming rebase reaches
    `reference-transaction` the same way. A worktree creation can be judged
    after git made it, in `post-checkout`, but only taken back there, and a
    take-back cannot undo all of it: `worktree add -B` resets an existing
    branch first, `--no-checkout` and `--orphan` run no `post-checkout`, and a
    `--lock`ed tree survives one `--force`. This plugin writes nothing into a
    clone's git hooks in any case (`docs/the-routing-check.md`).
    check: tests/test_the_hook_surface_git_offers.py tests/test_the_frozen_reading_never_grows.py
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: its commit carries
    `: '[no-review]';` in front of the command.
  to: its commit carries
    the trailer `SpecSeal-Routing: no work item`.
- change
  file: docs/release-checklist.md
  section: 4. Commit, push, open the first pull request
  from: that answer's recorded form is the waiver in front of each command, in
    quotes:
  to: that answer's recorded form is `seal no-work-item`, run before the first
    edit, and the trailer `SpecSeal-Routing: no work item` on each commit:
- change
  file: docs/release-checklist.md
  section: 4. Commit, push, open the first pull request
  from: : '[no-review]'; git commit -m "chore: release X.Y.Z — <what the fragments say>"
  to: git commit -m "chore: release X.Y.Z — <what the fragments say>" -m "SpecSeal-Routing: no work item"

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The three git hooks | `hooks/git/pre-commit.py`, `hooks/git/reference-transaction.py`, `hooks/git/post-commit.py` | Each job: *Data & interfaces*, the table of jobs |
| The commit gate inside git | `hooks/commitgate.py` (whole) | Same table; the refusal record's writer is `hooks/sealer-stamp-queue.py` |
| The stub writer and its clone tests | `hooks/githooks.py` (whole); `hooks/hook-install.py#write_stubs`, `#install`, `INSTALLED`, `FOREIGN`, `say_once` | `hooks/stub-remove.py` keeps the marker test and the removal, at session start only |
| The arms and their texts | `hooks/gate.py#arms_missing`, `#refusal`, `#guarantee_refusal`, `#options`, `#waiver`, `#old_waiver`, `MARKS`, `TOKENS`, `HEADER`, `STATES`, `QUESTIONS`, `BACKSTOP`, `AUTOMATION`, `UNCHANGED`, `GUARANTEE_STATE`, `GUARANTEE_WAY_ON` | The edit gate's deny text; `#touches_code`, `#git`, `#lines` and `DOC_ROOTS` stay for `chain_check.py`; `#declaration_hint` moves to the edit gate |
| The commit gate's session route | `hooks/hooksession.py#session`, `#from_lease`, `#lease_dirs`, `#call_args` | No hook needs a session behind a commit; `#is_claude`, `#claude_pid`, `#claude_ancestor` and `SESSION_VARIABLE` stay for the lease writer and the guard |
| The text reading | `hooks/commit-review-gate.py` (whole), its `pre-bash` entry | No commit is read from a command |
| The old waiver's carriers | `hooks/answers.py`, `hooks/answer-write.py`, `hooks/answer-clear.py` (whole), their group entries | No reader of `[no-review]` or `[no-parity]` is left |
| Readers of the commit gate alone | `hooks/tokens.py#is_plain`, `#steps_around_hooks`; `[no-review]` and `[no-parity]` in `hooks/tokens.py#KNOWN`; every unit of `hooks/cmdline.py` that only the commit gate reaches, enumerated by the build from the call graph | `hooks/tokens.py#given`, `#without_bodies` and `hooks/one_heredoc.py` stay for the guard's tokens |
| The notice's stand-aside | `hooks/implementer-notice.py#main`'s `githooks.decides` test; `#notify`'s `post-commit` caller | `post-bash` alone says the line |
| The post-commit stamp queue | `skills/verify/scripts/seal_stamp.py#queue_for_guarantee` | `seal_stamp.queue_for_local_guarantee`'s rule, for both roots, under `hooks/sealer-stamp-queue.py` |
| The review mark | the `specseal-reviewed` write in `skills/code-review/orchestration.md`; `agents/warden.md`'s line on it; its sentences in `README.md` and `README.ko.md` | No reader is left |
| The parity mark | the `specseal-parity` write in `skills/legacy-parity/SKILL.md` and `skills/parity-setup/SKILL.md` | The comparison is recorded in the round records and the guarantee |
| The per-command waiver in prose | `skills/implement/SKILL.md` *1. Read the spec before the code*, the paragraph opening *A waiver is one command's*; `skills/implement/orchestration.md`'s `[no-review]` lines; `templates/claude-md-block.md`; `skills/agent-contract/SKILL.md` rule 8's waiver sentence | `seal no-work-item` and the trailer, stated in `skills/commit-pr-convention/SKILL.md` and `docs/the-routing-check.md` |
| The agent contract's reasons that rested on the commit gate | `skills/agent-contract/SKILL.md` rule 8 (whole: no gate reads a probe's commit, so it retires to one line under its number), rule 9's second reason and its heredoc-exception paragraph, rule 16's second reason | Rule 9's second reason becomes the edit check: an edit through the shell is invisible to it. Rule 16 keeps its first reason |
| Two policy documents | `docs/the-commit-gate-inside-git.md`, `docs/commit-review-gate-spec.md` (whole, by the rule changes above) | `docs/the-routing-check.md`, `docs/the-session-hooks.md`, `docs/worktree-guard-spec.md` *Which tree* |
| The rule a heredoc shape is data | `docs/commit-review-gate-spec.md` *Which repository*, the paragraphs *A file edit goes through the `Edit` tool* and the one shape, with the marker `one-heredoc-shape-is-data` in the tests that carry it | Its subject was whether a command commits, which nothing reads now |
| Tests of the removed units | `tests/test_commit_review_gate.py`, `tests/e2e/commit/test_commit_flow.py`, `tests/test_commitgate.py`, `tests/test_answers.py`, `tests/test_the_hooks_are_installed_where_git_runs_them.py`, `tests/test_the_commit_gate_decides_at_the_commit.py`, `tests/test_the_old_spellings_reach_the_hook.py`, `tests/test_the_waiver_can_be_typed.py`, `tests/test_gate_judges_the_repo_it_commits_to.py`, `tests/test_a_commit_behind_a_reserved_word_is_judged.py`, `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`, `tests/test_an_automation_run_meets_no_commit_prompt.py`, and the cases of `tests/test_gate.py`, `tests/test_hooksession.py`, `tests/test_cmdline.py`, `tests/test_tokens.py` and `tests/test_the_hook_surface_git_offers.py` whose unit is removed, enumerated by the build from the units removed | Each covered a removed unit; a marker a kept rule names stays carried by a kept test, which `rules --check` reads |
| Recorded durations | the `.test_durations` entries of the removed tests | Rewritten by the recorder at the next broad run |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-25 by framer, before the build.
