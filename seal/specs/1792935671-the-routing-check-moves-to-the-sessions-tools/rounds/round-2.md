# Review round 2: 1792935671-the-routing-check-moves-to-the-sessions-tools

target: 888f9b66, fixes 6bfead52..888f9b66

## Findings

### 1. Issue #1028 asks for one file, and the docstring and `overview.md` say it asks for the five caseless files too

severity: should
location: `tests/test_the_retired_rules_await_their_settle.py:11-14`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/overview.md:15`
evidence: executed `gh issue view 1028 --json title,state,body`
verdict: open
reopens: round-1#4

The close of round 1's finding 4 does not hold for five of the six files it
covered. The fix pointed both sentences at issue #1028. The docstring now
says the settle's pull request deletes this file "with the five caseless
files `docs/` names for it, as issue #1028 asks". The `overview.md` row for
the five caseless files ends "issue #1028 asks the settle's pull request to
delete them".

Issue #1028 (open) names only one file. Its title is about
`tests/test_the_retired_rules_await_their_settle.py`, and its *Done when* asks
for that file alone. It names none of the five files:
`tests/test_a_commit_behind_a_reserved_word_is_judged.py`,
`tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`,
`tests/test_an_automation_run_meets_no_commit_prompt.py`,
`tests/test_gate_judges_the_repo_it_commits_to.py` and
`tests/test_the_waiver_can_be_typed.py`. A person who runs that settle reads
#1028's *Done when*, deletes the one file and closes the issue. The five
files then outlive the documents that named them, and both sentences say
that someone was asked to remove them when nobody was. Round 1's finding
named exactly that defect. Closed against a body that leaves the five out,
the finding is still open for them.

The repair is outside the tree. Add the five files to #1028's *Done when*,
and both sentences then hold as written:

```markdown
## Done when

The pull request of the settle that applies 1792935671's spec deletes, in the
same commit as the applied documents, `tests/test_the_retired_rules_await_their_settle.py`
and the five caseless files the retired documents name on their `check:`
lines: `tests/test_a_commit_behind_a_reserved_word_is_judged.py`,
`tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`,
`tests/test_an_automation_run_meets_no_commit_prompt.py`,
`tests/test_gate_judges_the_repo_it_commits_to.py` and
`tests/test_the_waiver_can_be_typed.py`; `rules --check` holds after it.
```

answer:

### 2. A detached HEAD that only an undeclared `<declared>/<more>` branch holds is let through

severity: should
location: `hooks/routing-edit-gate.py:156-175`, `tests/test_routing_edit_gate.py`
evidence: executed `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-2/test_tmp_round2.py`
verdict: open
regression: round-1#3

The unit is `hooks/routing-edit-gate.py#detached_on_declared`, added by
`43abdbea`. Phase 2's `plan.md` row delivers the edit check. `spec.md`
*The edit check*, as `f221c3db` amended it, allows a detached HEAD whose
commit a declared branch holds "under `refs/heads/<branch>`". The fix passes
`refs/heads/<name>` to `git for-each-ref`, and git also matches a pattern
with no glob in it as a prefix ending at a slash. So the pattern matches
`refs/heads/<name>/<anything>`, and the defect came from reading that
pattern as an exact ref name.

The probe made a repository whose committed declaration names `feat`, with
no `feat` branch and an undeclared `feat/sub` one commit ahead. Then it
detached HEAD at `feat/sub`'s commit. The gate stayed silent, where the rule
says deny. `git for-each-ref --format=%(refname) refs/heads/feat
refs/remotes/*/feat` printed `refs/heads/feat/sub` (git 2.54.0). The same
happened in a `--no-local` clone detached at `origin/feat/sub`, through the
local branch the clone made. The remote-tracking pattern holds a glob, so git
matched it as a whole name and it did not match `refs/remotes/origin/feat/sub`.

The exposure is small, because commits made there reach a pull request only
through a branch. But the gate lets through what its rule refuses, and the
docstring and the amended rule text both say `refs/heads/<branch>`.

```python
        for ref in out.split() if code == 0 else []:
            # `for-each-ref` matches a pattern without a glob up to a slash
            # too, so `refs/heads/feat` names `refs/heads/feat/sub`; only the
            # declared name itself counts. The remote pattern holds a glob,
            # which git matches as a whole name. No OS precondition.
            if ref.startswith("refs/heads/") and ref != f"refs/heads/{name}":
                continue
            if git(top, "merge-base", "--is-ancestor", "HEAD", ref)[0] == 0:
                return True
```

```python
    def test_refuses_a_detached_head_only_a_longer_branch_name_holds(self, repo):
        """A declaration naming `x`, with no branch `x`, and an undeclared
        `x/sub` holding HEAD: still refused."""
        opt_in(repo)
        declare_routing(repo, branch="x")   # NAME NOT IN TREE: check declare_routing's parameter for the branch
        git(repo, "add", "seal")
        git(repo, "commit", "-qm", "declare x")
        git(repo, "switch", "-q", "-c", "x/sub")
        (repo / "f.txt").write_text("sub\n", encoding="utf-8")
        git(repo, "commit", "-qam", "sub")
        git(repo, "switch", "-q", "--detach")
        assert decision_of(run(repo / "f.txt")) == "deny"
```

answer:

### 3. The edit gate now spells the declaration path with `/`, against the platform spelling the implementer notice pins for the same file

severity: should
location: `hooks/routing-edit-gate.py:189-218`, `tests/test_routing_edit_gate.py:79-111`, `tests/test_routing_edit_gate.py:128-146`
evidence: read `hooks/routing-edit-gate.py:189-212`, `hooks/implementer-notice.py:160-168`, `tests/test_implementer_notice.py:157`, `tests/test_implementer_notice.py:181`, `hooks/optin.py:86-93`, `hooks/question-gate.py:57-62`
verdict: open
regression: round-1

The unit is `hooks/routing-edit-gate.py#declaration_hint` and `#reason`,
changed by `a314f3a7`, a commit of the fix pass that no finding named.
Phase 2's `plan.md` row delivers "the deny texts", and `spec.md` S1 asks
for "a reason naming the declaration path" without choosing a spelling. The
gate's own docstring said "spelled the way the platform spells it" until
`a314f3a7`. Two Windows cases that asserted `/` failed, and the commit
changed the code rather than the two cases. That is where the defect came
from.

The claim in the new docstring is "written with `/` on every platform, as a
repository path shown to a person is". No document in the tree states that
rule. The tree states and pins the opposite one for the same file.
`hooks/implementer-notice.py:160-162` spells the `routing.md` path "the way
their platform spells it", and `tests/test_implementer_notice.py:157` and
`:181` pin it with `os.path.join`. `hooks/optin.py:86-93` gives the reason:
a root in one dialect joined in the other prints half of one path each way.
So a Windows session now meets one declaration path in two spellings: the
edit gate's `/` and the implementer notice's `\`. The refusal itself also
mixes them, printing `` `src/new.py` is in `C:\r` ``.

The smith's hand-back offers `hooks/question-gate.py#shown` and
`hooks/implementer-notice.py` as same-class instances of the defect. Under
contract rule 12, neither is this work's to fix. Both follow the convention
the tree documents. The sentence that would send the next agent to "fix"
them is the new docstring's, and that is why it counts as a `should`. If
`/` everywhere is wanted, that is a change across the gates and their pinned
cases, and it goes to an issue of its own.

The fix puts the gate back on the tree's convention and makes the cases
platform-neutral (contract rule 18: the cases were what disagreed). The
precondition is the one `hooks/optin.py:86-93` states: the root arrives
`normpath`ed, so joining with `os.path.join` keeps one dialect.

```python
def declaration_hint(top):
    """The declaration path a refusal tells a session to write, relative to
    `top` and spelled the way the platform spells it, as
    `hooks/implementer-notice.py` spells the same file.
    ...
    """
    home = optin.home_at(top)
    try:
        rel = os.path.relpath(home, top)
    except ValueError:
        rel = home
    return os.path.join(rel, optin.WORK_ITEMS, "<work-item-id>", routing.FILENAME)


def reason(path, top, branch, pressed):
    """The whole text of the refusal."""
    shown = os.path.relpath(os.path.realpath(path), os.path.realpath(top))
```

```python
HINT = os.path.join("seal", "specs", "<work-item-id>", "routing.md")
# in attended() and pressed():
        f"declaration at `{HINT}` from "
# and test_the_declaration_path_is_written_with_slashes_on_windows becomes
# test_the_declaration_path_is_spelled_the_platforms_way_on_windows:
        assert gate.declaration_hint(r"C:\r") == r"seal\specs\<work-item-id>\routing.md"
        assert gate.declaration_hint(r"D:\w") == r"C:\r\seal\specs\<work-item-id>\routing.md"
        said = gate.reason(r"C:\r\src\new.py", r"C:\r", "feat", False)
        assert "`src\\new.py` is in" in said, said
```

answer:

### 4. `spec.md` still states the unrestricted trailer rule in three places its amendment did not reach

severity: should
location: `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:25`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:399`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:443`
evidence: read `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:25`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:399`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:443`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:186-211`
verdict: open

The framer's account is that `888f9b66` makes the spec "state the trailer
rule once". `f221c3db` rewrote the rule in *At the pull request*
(`spec.md:186-211`), and `888f9b66` removed one restatement from the
`docs/the-review-record.md` addition. Three statements of the old rule
remain, and each now contradicts the amended rule and the code at
`43abdbea`:

- `spec.md:25`, *Scope* item 2: "Every session commit in an opted-in
  repository carries the trailer". The amended rule says that at a local root
  a commit carries none.
- `spec.md:399`, the rule change to `docs/the-review-and-parity-arms.md`'s
  table, *nothing readable, or no file* row: "a commit whose
  `SpecSeal-Routing` trailer names a work item fails it". At a local root
  `trailer_findings(..., local=True)` turns it into a notice, and a commit
  its author did not commit is not read at all (probe: local root, exit 0).
- `spec.md:443`, the same document's parity table, `none` row: "a commit
  whose `SpecSeal-Routing` trailer names a work item fails the pull request
  first". The same two exceptions apply.

The last two are rule texts that the settle writes into
`docs/the-review-and-parity-arms.md`. That document would then contradict
`docs/the-routing-check.md` *At the pull request* about local mode, and an
agent reading it for a local-mode repository would expect a refusal that
never comes. Contract rule 19 asks the amendment to correct every sentence
that stated the old fact, and these three were left out. The units come from
the framing phase, so this finding names no earlier one.

```markdown
2. **The pull-request check.** Every session commit in a repository whose root is shared carries the trailer `SpecSeal-Routing: <work-item-id>` or `SpecSeal-Routing: no work item`; at a local root a commit carries none. `chain-check` fails a ready pull request where one of its own commits, committed by its author, names a work item that no declaration it judges names. A commit without the trailer is not judged.
```

```markdown
  to: | nothing readable, or no file | refused, unless the session recorded that its change belongs to no work item | its commits' `SpecSeal-Routing` trailers are judged as `docs/the-routing-check.md` *At the pull request* states; with none refused, pass, with a notice saying nothing was checked |
```

```markdown
    | none | nowhere: a work item's `SpecSeal-Routing` trailer is judged first, as `docs/the-routing-check.md` *At the pull request* states, and one reading `no work item` stands as the per-command waiver did, visible in history |
```

answer:

### 5. Three `overview.md` rows say `spec.md` does not yet state the rules it states since `f221c3db`

severity: should
location: `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/overview.md:11-13`
evidence: read `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/overview.md:11-13`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:137-143`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:186-211`
verdict: open
regression: round-1

The unit is the three divergence rows `43abdbea` wrote into `overview.md`,
each ending with the sentence that `spec.md` does not carry the change. The
frame is `spec.md` as `f221c3db` amended it, a commit of the fix pass that
no finding named. It added the detached-HEAD exception (`spec.md:137-143`),
the author-and-committer test and the local-root rule (`spec.md:186-211`).
Neither commit touched the other's file, which is where the defect came
from.

Each row now makes a false claim:

- Row "Which commits the trailer arm reads" ends: the rule text "still says
  'merges left out' alone".
- Row "Where a commit carries the trailer" ends: "the rule text in `spec.md`
  does not, and the settle applies that text".
- Row "A detached HEAD" ends: "The rule text in `spec.md` does not carry the
  exception yet".

The sealer reads `overview.md`'s divergences against the frame. Each row
sends it after a gap that `f221c3db` closed. The second row also tells it the
settle will apply an unrestricted rule. Once finding 4 is fixed, that is
untrue too.

```markdown
... The rule text in `spec.md` *At the pull request* states the author-and-committer test since `f221c3db` |
... `skills/commit-pr-convention/SKILL.md` and the CLAUDE.md block say so, and `spec.md` *At the pull request* and *Scope* item 2 state it since `f221c3db` and round 2's finding 4 |
... `spec.md` *The edit check* states the exception since `f221c3db` |
```

answer:

## Confirmations

confirms: round-1#1
The local-root fix holds (executed: the round-2 probe). A local-mode
repository with `.git/seal/specs/W1/`, a commit on `feat` carrying
`SpecSeal-Routing: W1` and a ready event payload made `chain_check.py` exit 0
and print the `LOCAL_TRAILER` notice. The same commit at a shared root with
no declaration exited 1, so the arm still refuses where it should.
`main` passes `local=bool(local_root(root, routing))`
(`skills/code-review/scripts/chain_check.py:2193-2195`), and
`trailer_findings` turns a work item's value into a notice only where that
flag is set (`:2095-2110`), read. The convention
(`skills/commit-pr-convention/SKILL.md:138-143`), the README rows, the
orchestration exit row, `skills/settle/SKILL.md:225-228` and
`templates/claude-md-block.md:16` each restrict the trailer to a shared root
(executed: `git grep -n -E 'SpecSeal-Routing|routing trailer|the trailer'`
outside `seal/`, `tests/`, `docs/` and the changelogs). The `spec.md` rule
text at 186-195 now carries the restriction. Finding 4 covers the three
restatements the amendment missed.

confirms: round-1#2
The author-and-committer fix holds (executed: the round-2 probe). A
teammate's `cherry-pick -x`, with committer email `t@example.com`, of a
session's commit onto an undeclared `fix-b` exited 0. The same cherry-pick
under the author's own identity exited 1, which is the cost the rule text
states. A commit whose committer email differed from its author email only
in case exited 1, which matches "compared case-folded". `routing_trailers`
reads `%ae` and `%ce` and skips a commit where they differ
(`skills/code-review/scripts/chain_check.py:2076-2088`), read. The rule text
at `spec.md:197-211` states what the code does.

confirms: round-1#3
The detached-HEAD fix holds for the cases the finding named (executed: the
round-2 probe). A `--no-local` clone detached at `origin/feat` was silent,
and so was a `worktree add --detach` at `feat`. A detached HEAD at a commit
only the undeclared `side` holds was denied. The new check runs only after
`for_branch` finds nothing and only where no branch is named
(`hooks/routing-edit-gate.py:234-238`), read, so an allowed edit's cost does
not change. Finding 2 is a defect the fix brought in with its pattern, not
the defect round 1 named. A red-first clone of the base commit is still
refused, because the base's tree holds no declaration for the branch. No
agent was found doing that: phase 7's red-first clone, `863fd292`, is a
branch commit after `36a78242` committed the declaration (executed:
`git merge-base --is-ancestor` and `git ls-tree`).

confirms: none
`d88696b7`'s `.test_durations` refresh prices the suite:
`bin/test tests -q -k test_the_durations_file_prices_the_suite` passed at
`888f9b66` (executed). This settles round 1's last `## Not judged` row.

confirms: none
The new and changed cases pass at `888f9b66`:
`bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_the_retired_rules_await_their_settle.py "tests/test_chain_check.py::Test_routing_trailers"`,
31 passed (executed). Under monkeypatched `ntpath`, the Windows case of
`a314f3a7` would fail against the old `os.path.join` code, so it was red
before its fix (read). Whether it should pin `/` at all is finding 3.

Carried from round 1, not re-established: settle touches no file under
`tests/` (`skills/settle/scripts/settle.py:590-605`). No path writes into a
person's or a teammate's git hooks: none of round 1's coordinates changed in
this range, and the owner's premise stands. The `## Not judged` rows below
on Q3, Q1 and Q2 and the matcher are also round 1's. Every other fact above
was established in this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `888f9b66`, and the Windows leg that found the `a314f3a7` defect | the branch | the orchestrator's broad run and the cross-platform CI run |
| Whether GitHub's server-side rebase of a pull request's head (the "Update branch" button with rebase) records a committer other than the author, which under the author-and-committer test leaves every rebased session commit unjudged; the rule text states the class ("a rebase under another identity"), not this case | `skills/code-review/scripts/chain_check.py:2086-2087` | the orchestrator, on a live pull request |
| Whether a subagent's edit meets the `PreToolUse` gate at all (Q3), with the two readings round 1 named | `hooks/routing-edit-gate.py:241-248` | the owner, in a live session after an installed release carries the hook |
| Q1 and Q2, both open; the build took default (a) of each | `questions.md` Q1, Q2 | the owner |
| Whether the harness has an edit tool that `Write\|Edit\|NotebookEdit` does not name | `hooks/hooks.json` `pre-edit` matcher | the owner, in a live session |

## Probes

| Command | Result |
|---|---|
| `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-2/test_tmp_round2.py` | Round 1's two probes written again, plus the prefix case. It made repositories under the round's scratch directory, drove them from Python, then deleted them. Local root with a work-item trailer: exit 0, `LOCAL_TRAILER` printed. Shared root, no declaration: exit 1. A teammate's cherry-pick: exit 0. A same-identity cherry-pick: exit 1. A case-only email difference: exit 1. Detached `--no-local` clone at `origin/feat`, and `worktree add --detach`: silent. Detached at a commit only `side` holds: deny. Declared `feat` with only `feat/sub` holding HEAD: silent where deny was expected, locally and in a clone. It ran a second time, unchanged except that it also printed `for-each-ref`'s matches, which were `refs/heads/feat/sub` in both. |
| `bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_the_retired_rules_await_their_settle.py "tests/test_chain_check.py::Test_routing_trailers"` | 31 passed |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` | 1 passed |
| `gh issue view 1028 --json title,state,body` | Open. Title and *Done when* name `tests/test_the_retired_rules_await_their_settle.py` alone |
