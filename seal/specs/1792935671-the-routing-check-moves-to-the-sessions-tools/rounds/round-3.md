# Review round 3: 1792935671-the-routing-check-moves-to-the-sessions-tools

target: a168466e, fixes 888f9b66..a168466e

## Findings

This round opens no finding. The range holds four commits: `5ce40f25` (round
2's record), `59b86822` (the framer's `spec.md` amendment), `04dd6c6a` (the
smith's fixes) and `a168466e` (round 2's verdict and answer lines). Its code
units are the filter line in `hooks/routing-edit-gate.py#detached_on_declared`,
the restored `#declaration_hint` and `#reason`, and three changes to
`tests/test_routing_edit_gate.py`: the `HINT` constant, the rewritten Windows
case and one new case. Each is weighed under its finding below (executed:
`git diff --stat 888f9b66 a168466e`).

## Confirmations

confirms: round-2#2
The close holds. The smith's claim is that `detached_on_declared` now counts
only the declared branch's own name, and that the remote-tracking pattern
needs no filter because git matches its glob against the whole name.
`hooks/routing-edit-gate.py:178` skips any `refs/heads/` ref other than
`refs/heads/<name>`, and the check is still reached only where no branch is
named and `for_branch` found nothing (`:243`), read. The round-2 probe was
written again from its `## Probes` row (executed: the round-3 probe). With a
declared `feat`, no `feat` branch and an undeclared `feat/sub` holding HEAD,
`for-each-ref` still lists `refs/heads/feat/sub`, and the gate now denies.
It also denies in a `--no-local` clone detached at `origin/feat/sub`. This
round also probed the other side of the same cause, a pattern read as a
name it does not match. With an undeclared `team/feat` on the origin and the
clone detached at `origin/team/feat`, `for-each-ref` did not list
`refs/remotes/origin/team/feat`, and the gate denied. The control, detached
at `origin/feat`, stayed silent. So the code comment's claim that git
matches the remote glob whole holds on git 2.54.0, and no slash in a longer
remote name reaches the exception. The new case
`tests/test_routing_edit_gate.py:212` reaches the same scenario through the
gate. Against the code before `04dd6c6a`, `for-each-ref refs/heads/x` lists
`refs/heads/x/sub` and the ancestor test passes, so the case's `deny`
assertion fails, as the smith says it did (read). Read against its group, it
covers a case none of the other detached-HEAD cases covers, and
`bin/test-layout --pairs` names no pair for this module (executed).

confirms: round-2#3
The close holds. `04dd6c6a` returns `declaration_hint` and `reason` to the
text they had before `a314f3a7`: `os.path.join` at
`hooks/routing-edit-gate.py:213`, and a bare `os.path.relpath` at `:218`
(read: `git show a314f3a7` against the current lines). The docstring now
cites `hooks/implementer-notice.py` and the `normpath` reasoning of
`hooks/optin.py:86-93`, which is the rule the tree documents. The cases now
build their expected text the platform's way through `HINT` at
`tests/test_routing_edit_gate.py:81`, as `tests/test_implementer_notice.py:157`
and `:181` do. The Windows case at `:134-154` pins Windows' spelling for the
hint, for an absolute root on another drive, and for the edited file in
`` `src\new.py` is in `C:\r` `` whole. The smith's claim is that the case was
red against the `/` code. Under the monkeypatched `sep`, the old
`rel.replace(os.sep, "/")` gives `seal/specs/...`, which is not the asserted
text, so the claim holds (read). The module passes at the working tree
(executed: `bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_implementer_notice.py`,
42 passed). Cross-platform run 40212628767 ran at `a168466e`, and every leg
succeeded, all four Windows splits included (executed: `gh run view 40212628767`).
The Windows splits are where `a314f3a7`'s two cases failed.

confirms: round-2#4
The close holds. `59b86822` rewrites `spec.md` *Scope* item 2 (line 25) to
the shared-root rule with the author-and-committer test. It also rewrites
*The trailer* (line 70), the parity-arm and sequencer rows of the move table
(lines 81 and 86), and the edit-check paragraphs at lines 160-163 and 182.
It replaces the two restatements in `docs/the-review-and-parity-arms.md`'s
tables, at lines 401 and 445, with references to `docs/the-routing-check.md`
*At the pull request*, which the spec's own addition creates at lines 186-213
(read). Every other line of `spec.md` that states the trailer agrees with
that section: lines 17, 35, 53, 54 and 516 (executed: `grep -n -i trailer`
over `spec.md`). The read command at line 70 now matches
`skills/code-review/scripts/chain_check.py:2070-2078` field for field
(read).

confirms: round-2#5
The close holds. Each of the three `overview.md` rows at lines 11-13 now
ends with a true sentence. `spec.md` *At the pull request* states the
author-and-committer test and the shared-root rule since `f221c3db`, *Scope*
item 2 and the two table rows state it since `59b86822`, and *The edit
check* states the detached-HEAD exception since `f221c3db` (read against the
diff of `59b86822` and lines 137-143 of `spec.md`). The rows' first cells
still quote what the spec said when the build diverged, such as "in an
opted-in repository". Their last sentences say when the frame caught up, so
each row has one reading: a dated divergence, now closed.

confirms: none
`bin/rules --check` exits 0 at the working tree, so every `check:` target
the frame and the build name still resolves (executed).

Round 2's finding 1 stands `deferred #1028` and is not written up again. Its
home was read (executed: `gh issue view 1028`). The issue is open, and its
*Done when* names `tests/test_the_retired_rules_await_their_settle.py` and
six caseless files, `tests/test_the_hooks_are_installed_where_git_runs_them.py`
among them. A `check:` line under `docs/` names each of the six (executed:
`git grep -l` for each name over `docs/`). Of the caseless test files in the
tree, only those two changed on this branch. The other five were already
caseless at the base (executed: `git diff --stat 97bf7a9a a168466e` over
them). So the home covers the whole class this work item leaves. The
docstring at `tests/test_the_retired_rules_await_their_settle.py:14` still
says "the five caseless files". That is one short of what #1028 now asks,
but the pull request #1028 describes deletes that file too, and no reader
acts on the count.

Carried from round 2, not re-established: the local-root and
author-and-committer behaviour of `chain_check.py` (round 1's findings 1 and
2). `chain_check.py` is not in this range (executed: `git diff --stat`), so
round 2's probe of it was not run again. The `## Not judged` rows on the
GitHub rebase, Q3, Q1 and Q2 and the matcher are also round 2's. Every other
fact above was established in this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `a168466e` | the branch | the orchestrator's broad run |
| Whether GitHub's server-side rebase of a pull request's head records a committer other than the author, which under the author-and-committer test leaves every rebased session commit unjudged | `skills/code-review/scripts/chain_check.py:2087-2088` | the orchestrator, on a live pull request |
| Whether a subagent's edit meets the `PreToolUse` gate at all (Q3), with the two readings round 1 named | `hooks/routing-edit-gate.py:247-252` | the owner, in a live session after an installed release carries the hook |
| Q1 and Q2, both open; the build took default (a) of each | `questions.md` Q1, Q2 | the owner |
| Whether the harness has an edit tool that `Write\|Edit\|NotebookEdit` does not name | `hooks/hooks.json` `pre-edit` matcher | the owner, in a live session |

## Probes

| Command | Result |
|---|---|
| `.venv/bin/python <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-3/test_tmp_round3.py` | It made repositories under the round's scratch directory, drove them from Python, and deleted them. With an undeclared `team/feat` on the origin and the clone detached at `origin/team/feat`, `for-each-ref` listed `refs/heads/feat` and `refs/remotes/origin/feat`, and the gate denied. Detached at `origin/feat`, the gate stayed silent. At the origin detached at a local `team/feat`, it denied. With a declared `feat` and only `feat/sub` holding HEAD, `for-each-ref` listed `refs/heads/feat/sub`, and the gate denied, locally and in a `--no-local` clone detached at `origin/feat/sub`. The scratch directory was removed. |
| `bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_implementer_notice.py` | 42 passed |
| `bin/test-layout --pairs` | exit 0; no pair names `tests/test_routing_edit_gate.py` |
| `bin/rules --check` | exit 0 |
| `gh run view 40212628767` | head `a168466e`; completed, success; every pytest leg success, the four Windows splits included |
| `gh issue view 1028` | open; *Done when* names `tests/test_the_retired_rules_await_their_settle.py` and six caseless files |
