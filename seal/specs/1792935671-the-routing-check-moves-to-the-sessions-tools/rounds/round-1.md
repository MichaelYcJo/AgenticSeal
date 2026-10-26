# Review round 1: 1792935671-the-routing-check-moves-to-the-sessions-tools

target: 6bfead52 against release/v0.22.4

## Findings

### 1. In local mode, every session commit's trailer fails a ready pull request that can never declare its work item

severity: should
location: `skills/code-review/scripts/chain_check.py:2174-2190`, `skills/commit-pr-convention/SKILL.md:138-158`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:181-187`
evidence: executed `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-1/test_tmp_round1.py`
verdict: fixed 43abdbea

The convention tells every session in an opted-in repository to end each
commit with `SpecSeal-Routing: <work-item-id>`
(`skills/commit-pr-convention/SKILL.md:138-141`). A repository whose root is
under the common git directory (local mode) is opted in, and in local mode no
`routing.md` is ever committed. So `declarations` in `chain_check.py#main` is
always empty there, and `trailer_findings` refuses every work-item trailer.

The probe built a local-mode repository with a `.git/seal/specs/W1/` root and
one commit on `feat` carrying `SpecSeal-Routing: W1`, then ran the branch's
`chain_check.py --baseline main` with an event payload for a ready pull
request. It exited 1. Its output first printed the local-mode notice, which
says "the review-chain check examined nothing", and then refused commit
`ae49a9e8` for naming a work item no declaration names. The refusal's way on,
"commit its `routing.md`, naming this branch", is the one thing local mode
never does.

This reaches a real run. `broad-gate` runs `chain_check.py --sealing` in
every mode (`skills/verify/scripts/broad_gate.py:2999-3008`), and it is strict
wherever `gh pr view` reports a ready pull request. So a local-mode work item
whose broad gate runs again after its pull request opened fails on its own
trailers. Local mode is also the mode for a repository whose team does not run
SpecSeal, so the trailer puts a work-item id that no tree holds into that
team's shared history. The frame did not weigh local mode for the trailer:
`spec.md` *Scope* item 2 and the rule text at lines 181-187 say "in an
opted-in repository" with no mode.

The fix has two parts. The convention and the rule text restrict the trailer
to the shared root, and the check prints a work-item trailer instead of
refusing it where the root it runs against is local.

```python
    judged_ids = {os.path.basename(os.path.dirname(rel)) for rel in declarations}
    problems, notices = trailer_findings(trailers, judged_ids)
    # In local mode no declaration is ever committed, so a trailer naming a
    # work item can match none: it is printed, never refused.
    if local_root(root, routing):
        notices.extend(problems)
        problems = []
```

```markdown
**A session's commit in a repository whose root is shared (`<repo>/seal/`)
ends with one `SpecSeal-Routing:` trailer, naming its work item or reading
`no work item`.** In local mode a commit carries none: no declaration it
could name is ever committed, and the history belongs to a team that does
not run SpecSeal.
```

The same restriction goes into the `spec.md` rule text at lines 181-187 and
into the `no work item` sentence of `templates/claude-md-block.md:16`.

answer: The finding holds, and 43abdbea takes the record's direction: `trailer_findings` takes `local`, `main` passes `local_root(root, routing)`, and a work item's trailer at a local root is the notice `LOCAL_TRAILER` ("printed, not judged"), never `UNDECLARED_TRAILER`, whose way on local mode never takes. `tests/test_chain_check.py::Test_routing_trailers::test_a_work_item_trailer_at_a_local_root_is_printed_not_refused` was red at the tree before the fix (exit 1 with the refusal) and goes red again under `mutation-check` with `elif local:` made false (executed). The convention in `skills/commit-pr-convention/SKILL.md` and the `no work item` sentence of `templates/claude-md-block.md` now restrict the trailer to a shared root, and every other sentence stating the trailer for `no work item` says "where the root is shared": both READMEs (the switch row, the root-move paragraph, the first limit), `skills/implement/orchestration.md` (question 1's exit row, the exit paragraph, the declaration paragraph, the standing-waiver paragraph), `skills/settle/SKILL.md` and `changelog.md` (executed: `git grep -n trailer` over the READMEs, agents, skills, templates and hooks). The `spec.md` rule text at 181-187 is the framer's file and not a write my definition names, so `overview.md` carries the divergence row "Where a commit carries the trailer" saying the settle would apply the unrestricted text; the orchestrator answers whether `spec.md` is amended before the settle.

### 2. A person's cherry-pick of a session commit is judged, and fails a pull request that declares nothing

severity: should
location: `skills/code-review/scripts/chain_check.py:2053-2086`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:189-197`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/overview.md:11`
evidence: executed `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-1/test_tmp_round1.py`
verdict: fixed 43abdbea

The owner's decision 4 (`spec.md:9`) is that the pull-request rule judges
only commits a session made, never a teammate's own. The trailer is the
only thing `routing_trailers` reads, and a trailer travels with a commit
message. A person who cherry-picks a session's commit makes a new commit of
their own that carries the session's trailer.

The probe committed `seal/specs/A/routing.md` naming `feat-a` on `main`, made
a commit on `feat-a` carrying `SpecSeal-Routing: A`, and then, as a person
would, ran `git cherry-pick -x` of it onto a new branch `fix-b`. With
`GITHUB_HEAD_REF=fix-b` and a ready payload, `chain_check.py` exited 1 and
told the person to "commit its `routing.md`, naming this branch, or correct
the trailer". So a teammate's backport pull request, in a repository that
runs the hygiene workflow, fails until they rewrite a commit message SpecSeal
asked for. That is SpecSeal reaching a person who does not use it.

The same probe settled one case the other way: a local `git merge --squash`
indents the squashed messages, and git's trailer parser read no
`SpecSeal-Routing` value from the squash commit.

The smith's squash exclusion (`overview.md:11`) is one instance of this
class: a commit someone other than its author committed. GitHub's squash and
rebase-merge, a teammate's cherry-pick and a teammate's rebase all share that
shape, and git records it on every commit. A session's own commit is
committed by the identity that authored it. Reading that one fact replaces
the squash test and covers the whole class.

```python
        f"--format=%H%x1f%ae%x1f%ce%x1f%s%x1f%(trailers:key={TRAILER},valueonly,separator=%x1e)",
        f"{base}..HEAD",
    )
    if out is None:
        return None
    found = []
    for entry in out.split("\0"):
        parts = entry.strip("\n").split("\x1f")
        if len(parts) != 5:
            continue
        sha, author, committer, _subject, values = parts
        # A commit someone other than its author committed (a teammate's
        # cherry-pick or rebase, GitHub's squash or rebase-merge) carries a
        # trailer its committer did not write, so it is not judged.
        # Precondition: emails as git records them, compared case-folded; a
        # session whose committer email differs from its author email is
        # not judged either.
        if author.strip().lower() != committer.strip().lower():
            continue
        for value in values.split("\x1e"):
            if value.strip():
                found.append((sha.strip(), value.strip()))
    return found
```

The rule text at `spec.md:194-196` then reads: "The commits are the pull
request's own, merges left out, and one its author did not commit is not
judged: it carries a trailer somebody else wrote." The docstring of
`routing_trailers` and `overview.md:11` change with it. A case in
`tests/test_chain_check.py` pins a cherry-pick whose committer differs from
its author as not judged.

answer: The finding holds, and 43abdbea takes the record's reading of "made by a session": a commit whose committer email is not its author email is not judged, compared case-folded as git records them, and GitHub's squash is one case of it, so the `SQUASH_COMMITTER` test left `routing_trailers` (`carried_by` keeps it for declarations). No other reading holds better: the harness's co-author trailer survives a person's cherry-pick, and dates move with any rebase, while git records the committer on every commit; the cost is that a person's own cherry-pick of their own session's commit, same identity, is still judged, which the docstring states. `tests/test_chain_check.py::Test_routing_trailers::test_a_commit_its_author_did_not_commit_is_not_judged` was red at the tree before the fix (exit 1, the cherry-picked trailer refused), the GitHub-squash case passes unchanged with its docstring naming the wider rule, and `mutation-check` removing the author test turned two cases of `Test_routing_trailers` red (executed). The `routing_trailers` docstring states the rule and its precondition; `overview.md`'s row "Which commits the trailer arm reads" now names the author-and-committer test and says the `spec.md` rule text at 194-196 still reads "merges left out" alone, which is the framer's file and not a write my definition names; the orchestrator answers whether it is amended before the settle.

### 3. A detached checkout of a declared branch's own commit is refused, which stops a warden's or smith's probe mid-run

severity: should
location: `hooks/routing-edit-gate.py:192-218`, `hooks/routing-edit-gate.py:21-24`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:137-139`, `tests/test_routing_edit_gate.py:128`
evidence: executed `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-1/test_tmp_detached.py`
verdict: fixed 43abdbea

The gate reads a detached HEAD as no branch outside a paused rebase, as
`spec.md:137-139` says. But the plugin's own agents edit in detached
checkouts of declared commits as a matter of course:

- `agents/warden.md:29-30` sends a warden to "a `git clone --no-local` of the
  repository at the target SHA", and its probes run in that clone (contract
  rule 7).
- Contract rule 15 has a new case shown red against older code. Phase 7 did
  this by copying test files into a `git clone --no-local` of `863fd292`
  (`phases/phase-7.md:61`), an ancestor of the declared branch.

The probe made a repository whose `feat` branch declares itself. An `Edit`
on `feat` went ahead. The same `Edit` in a `--no-local` clone checked out
detached at `feat`'s head, and in a `git worktree add --detach` of the same
commit, were both denied with the `DETACHED` text.

Under the `automation` press the deny offers `seal no-work-item`. A warden's
definition names no such write, so the probe cannot run. Attended, the deny
tells the subagent to put the routing question to the person with
`AskUserQuestion`. Either way the run stops or asks mid-run, the most
expensive outcome under `CLAUDE.md` *The goal a design is chosen against*.
Allowing such an edit opens nothing new. Commits made there carry the work
item's trailer, and they reach a pull request only through a branch, which
the gate and the trailer arm judge.

The fix lets a detached HEAD through where a branch some declaration names
already holds it, under its local or a remote-tracking name. That covers a
clone at the reviewed commit and a red-first clone of an earlier commit of
that branch. A detached HEAD at any other commit is still refused. This is
the refusal path only, so an allowed edit's cost does not change.

```python
def detached_on_declared(top):
    """Whether TOP's detached HEAD is a commit that a branch some declaration
    names already holds, under `refs/heads/<branch>` or any
    `refs/remotes/<remote>/<branch>`: a clone at a reviewed commit, or a
    red-first check of an earlier commit of that branch."""
    names = {d["branch"] for _, d in routing.declarations(top) if d.get("branch")}
    for name in sorted(names):
        code, out = git(
            top,
            "for-each-ref",
            "--format=%(refname)",
            f"refs/heads/{name}",
            f"refs/remotes/*/{name}",
        )
        for ref in out.split() if code == 0 else []:
            if git(top, "merge-base", "--is-ancestor", "HEAD", ref)[0] == 0:
                return True
    return False
```

```python
    branch = routing.current_branch(top) or rebase_branch(top)
    if routing.for_branch(top, branch):
        return None
    if not branch and detached_on_declared(top):
        return None
```

The rule text at `spec.md:137-139` and the module docstring become: "A
detached HEAD names no branch, except during a paused rebase, where the
branch the rebase names stands for it, and at a commit that a declared
branch already holds." `tests/test_routing_edit_gate.py:128` splits into
two cases: a detached HEAD on a declared branch's commit goes ahead, and one
on a commit no declared branch holds is refused.

answer: The finding holds, and 43abdbea takes the record's direction: `detached_on_declared` lets a detached HEAD through where a branch some declaration names holds it under `refs/heads/<branch>` or `refs/remotes/*/<branch>`, reached only on the refusal path after `for_branch` finds nothing, and the module docstring states the exception. `tests/test_routing_edit_gate.py:128` stays for a tree with no declaration, and two cases join it: `test_accepts_a_detached_head_at_a_commit_a_declared_branch_holds` (the branch's head and its parent by the local name, and a `--no-local` clone detached at `origin/feature/x`, a name holding a `/`, with no local branch of it) was red at the tree before the fix (`deny` at the head), and `test_refuses_a_detached_head_no_declared_branch_holds` (a commit only an undeclared branch holds, the declaration in its tree) went red under `mutation-check` with the ancestor test forced true; removing the exception and removing the remote-tracking pattern each turned the accept case red (executed). No README or skill sentence states the detached-HEAD rule (executed: `git grep -n -i detached` over the READMEs, agents and skills); `changelog.md` names the exception, and `overview.md`'s row "A detached HEAD" says the `spec.md` rule text at 137-139 does not carry it yet, the framer's file and not a write my definition names; the orchestrator answers whether it is amended before the settle.

### 4. The placeholder test file says the settle removes it, and nothing in the settle removes a test file

severity: should
location: `tests/test_the_retired_rules_await_their_settle.py:11-12`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/overview.md:13-14`
evidence: read `skills/settle/scripts/settle.py:590-605`, `tests/test_the_retired_rules_await_their_settle.py:11-12`
verdict: fixed 43abdbea

The account was: "The settle that applies the work item removes this file
with the documents" (`tests/test_the_retired_rules_await_their_settle.py:11-12`),
and "The settle removes them with the documents" for the five caseless files
(`overview.md:13-14`). `settle.py#apply` writes or deletes policy documents
and removes `seal/specs/<id>/` directories (`settle.py:590-605`). It touches
no file under `tests/`, and `skills/settle/SKILL.md` gives the session
running a settle no step that does.

After this work item settles, the four caseless classes and the five caseless
files outlive every rule that named them, and the one sentence that says they
go points at a mechanism that does not exist. A settle session that reads it
does nothing, because it believes the tool already did it. That is what
`CLAUDE.md` *The rule a mechanism is kept against* forbids: something kept
beside the tree, and nothing removing what stood on the old fact.

The fix states who removes them and makes that party's commitment
schedulable. The orchestrator files the removal as an issue the settle of
this work item closes, and both sentences name it.

```python
"""...
a class with no case: nothing of the retired rule is left to test. Nothing
removes this file on its own: the pull request that settles this work item
deletes it, with the five caseless files `docs/` names for it, as issue
#<N> asks.   # NAME NOT IN TREE: the issue the orchestrator files
"""
```

The two `overview.md` rows end the same way: "Nothing removes them on its
own; issue #<N> asks the settle's pull request to delete them."

answer: The finding holds, and 43abdbea writes issue #1028, which the orchestrator filed, where the record held its placeholder: the docstring of `tests/test_the_retired_rules_await_their_settle.py` now says nothing removes the file on its own because `settle` touches no file under `tests/`, and that the pull request settling this work item deletes it with the five caseless files, as #1028 asks; the two `overview.md` rows end "issue #1028 asks the settle's pull request to delete them" and "to delete it". The other places that could state the old claim were swept (executed: `git grep -n -i` for "settle removes" and "removes this file with" outside `docs/` and released history): the five caseless files say only that `docs/` names them until the rule change is settled, which stands; `phases/phase-5.md` line 17 keeps the old sentence because a phase record is what was true when it was written. No case changes: the fix is a docstring and two record cells, and `rules --check` holds all 249 lines (executed).

## Confirmations

confirms: none
No remaining path writes into a person's or a teammate's git hooks
(executed: `git grep` over the tree outside `tests/`, `docs/`, `CHANGELOG.md`,
`changelog/` and `seal/` for `hooksPath`, `hooks_dir`, a `git config`
write, the marker, `pre-commit`, `reference-transaction` and `post-commit`).
The only hits are `hooks/stub-remove.py`, its README rows, and
`skills/verify/scripts/deferral_check.py`, which reads a
`.pre-commit-config.yaml` and writes nothing. `install.sh` writes no hook.
`hooks/stub-remove.py:47-81` deletes only a file whose second line starts
with `# specseal-git-hook`, in the common git directory's `hooks/` of the
clone the session starts in, which is not shared with any teammate. That
marker has stood on the second line of every stub since `9da8cd1a`
(executed: `git log -S`), so no earlier release's stub escapes it. What the
session writes beside git (`specseal-no-work-item/`, `specseal-stamp/`, the
implementer marks) sits in the session user's own git directory and runs
nothing. The judging that stays outside the session is the trailer arm in
CI, and findings 1 and 2 are where it reaches past the session.

confirms: none
The smith's divergence "the trailer arm leaves out a squash GitHub
committed" (`overview.md:11`) holds as far as it goes. It uses
`carried_by`'s own rule (`chain_check.py:276-277`), and without it every
release pull request into `main` would fail on its squashes. Finding 2 is
the wider class it belongs to.

confirms: none
The divergence "`hooks/gate.py#git` and `#lines` went" (`overview.md:16`)
holds. `hooks/gate.py` is now `DOC_ROOTS` and `touches_code` (read
`hooks/gate.py:1-25`). `git grep` outside `tests/` for `gate.git(`,
`gate.lines(`, `declaration_hint` and `arms_missing` found no caller
(executed).

confirms: none
The divergence "the whole of `hooks/hook-install.py` went" (`overview.md:17`)
holds. `spec.md:72` replaces it in `session-start` with `stub-remove.py`, and
`hooks/dispatch.py` `GROUPS` names it nowhere (read).

confirms: none
The divergence "the moved `declaration_hint` lost its no-root branch"
(`overview.md:19`) holds. `decide` returns at `hooks/routing-edit-gate.py:203`
where `home_at` finds no root, so `declaration_hint` is reached only with a
root (read).

confirms: none
The divergences on the caseless files and markers (`overview.md:13-14`)
hold as reasons to keep the files until the settle: `bin/rules --check`
exits 0 at the working tree (executed). Finding 4 is about the claim of who
removes them, not about keeping them.

confirms: none
The divergence "the prose phase changed files the plan did not list"
(`overview.md:18`) holds under contract rule 12. Each named file stated the
removed marks or waiver (read: the phase-7 diff of `agents/smith.md`,
`agents/scribe.md`, `agents/warden.md`, `skills/settle/SKILL.md` and
`templates/claude-md-block.md`).

confirms: none
Q3 is stated wherever a reader needs it. `questions.md` Q3 reads
`unverified` with the owner as answerer. `overview.md` *Not verified* row 1
names it. The rule text on subagents carries
`check: none reader: the orchestrator on the first live run after a change here`
(`spec.md:171-177`). `phases/phase-2.md` records why it was not measured.

confirms: none
The new gate's and the trailer arm's cases pass at the working tree
(executed: `bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_stub_remove.py tests/test_chain_check.py -k "routing_trailers or originals_of or Test_main or Test_module"`,
58 passed). The matcher is pinned to the gate's `TOOLS` and to the
`post-edit` matcher (`tests/test_routing_edit_gate.py:305-326`), which
answers the plan's failure scenario of an unmatched tool.

confirms: none
The settle change holds for its callers. `apply_op` returns `(None, None)`
for an emptied document, `replay` stores the None, `settle.py#apply` deletes
it, and `unverified_check.py#settled` drops it before counting (read
`skills/settle/scripts/rule_changes.py:217-248`,
`skills/settle/scripts/settle.py:590-596`,
`skills/verify/scripts/unverified_check.py:1312-1320`). `git grep` found no
other consumer of `replay`'s documents (executed).

Round 1 carries no coordinates from an earlier round, so every fact above
was established in this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a subagent's edit meets the `PreToolUse` gate at all (Q3), and with it two readings the gate takes from a subagent's call: whether its `transcript_path` holds the main session's `automation` press, so a subagent in an automation run gets the `PRESSED` text and not `AskUserQuestion`, and whether its Bash environment carries the main session's `CLAUDE_CODE_SESSION_ID`, so `seal no-work-item` run there matches the hook payload's `session_id` | `hooks/routing-edit-gate.py:213-217`, `skills/implement/scripts/seal.py#no_work_item` | the owner, in a live session after an installed release carries the hook |
| Q1 and Q2, both open; the build took default (a) of each | `questions.md` Q1, Q2 | the owner |
| Whether the harness has an edit tool `Write\|Edit\|NotebookEdit` does not name in the Claude Code version a consumer runs | `hooks/hooks.json` `pre-edit` matcher | the owner, in a live session |
| Whether citing `docs/the-routing-check.md`, which only the settle creates, from contract rule 9 and the gate's docstrings is accepted until then | `skills/agent-contract/SKILL.md` rule 9, `hooks/routing-edit-gate.py:4` | the orchestrator |
| The full suite, the repository-wide lint and format check, and the typecheck at `6bfead52` | the branch | the orchestrator's broad run |
| `.test_durations` naming 1,378 removed cases, red under `test_the_durations_file_prices_the_suite` | `.test_durations` | the orchestrator, from CI run 40209166795, then the verifying round |

## Probes

| Command | Result |
|---|---|
| `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-1/test_tmp_round1.py` | Three scratch repositories under the round's scratch directory, driven from Python, then deleted. Local mode with a work-item trailer and a ready payload: `chain_check.py` exit 1. A person's `cherry-pick -x` of a session commit onto an undeclared branch: exit 1. `git merge --squash` of a commit carrying the trailer: git's trailer parser read no value from the squash commit. |
| `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-1/test_tmp_detached.py` | One scratch repository whose `feat` branch declares itself, then deleted. An `Edit` on `feat`: no output, so it goes ahead. The same `Edit` in a `--no-local` clone detached at `feat`'s head, and in a `worktree add --detach` of that commit: `deny`, with the `DETACHED` text. |
| `bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_stub_remove.py tests/test_chain_check.py -k "routing_trailers or originals_of or Test_main or Test_module"` | 58 passed |
| `bin/rules --check` | exit 0 |
