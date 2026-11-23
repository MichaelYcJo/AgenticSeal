# Review round 3: 1795406406-code-stands-on-facts-that-no-longer-hold

```seal
target: 61c1042ea, fixes 4dac381e1..61c1042ea
```

This is the verifying round after round 2's fix pass. It also reads one merge of the base. The range `4dac381e1..61c1042ea` holds four commits. `399174f03` commits round 2's record. `fc573606d` is the fix: it changes `skills/code-review/scripts/chain_check.py`, `tests/skills/test_chain_check.py` and this work item's `changelog.md`. `99144eecd` appends the close block to `trail/rounds/round-2.md`. `61c1042ea` merges `origin/release/v0.38.6` at `459116a4e`, which carries #1572 (executed: `git show --stat` on each). The round worked in a `git clone --no-local` of the branch worktree, checked out at `61c1042ea`, under `<scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-3/clone`. The work item's records were read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` to `phase-5.md`, and `trail/rounds/round-1.md` and `round-2.md`. Of these, only `changelog.md` and `round-2.md` changed in the range (executed: `git diff --stat 4dac381e1 61c1042ea -- seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold`). No `pr.<lang>.md` stands, and none is owed, because `Commit and pull request language` is English. No `seal/parity.json` is declared.

Carried from round 2 and not established again: the `## Rule changes` probe, which parsed every operation and placed each `from` once in its section. The merge leaves its input as it was. #1572 changed no file under `docs/` (executed: `git diff --stat 02369a0e9 459116a4e -- docs` prints nothing). Its own operations name `docs/layout/the-pact.md` and `docs/running/what-a-script-gates.md`, and this work's operations name neither (read: the `file:` lines of both designs). The acceptance searches were run again rather than carried, because the merge brought #1572's code into `lib/` and `skills/verify/`.

## Findings

### 1. At a local root the review-chain check now says it judged the commit trailers, and the same run prints each trailer as printed, not judged

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1909-1919`, `skills/code-review/scripts/chain_check.py:1936-1941`, `skills/code-review/scripts/chain_check.py:2175-2176`, `tests/skills/test_chain_check.py:3701-3709`, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/changelog.md:4`
evidence: executed `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-3/test_tmp_round3_local_notice.py <clone> <scratch>`, `git log -S'judged the commit' -- skills/code-review/scripts/chain_check.py`, `git grep -n 'ROOT_LEFT_SAYS'`; read `skills/code-review/scripts/chain_check.py:1831-1839`, `skills/code-review/scripts/chain_check.py:2002-2015`, `skills/code-review/scripts/chain_check.py:2165-2208`, `docs/checks/the-routing-check.md:42-56`, `tests/skills/test_chain_check.py:3926-3949`, `tests/skills/test_chain_check.py:4773-4795`
regression: round-2#1
```

The unit is the local-root return of `chain_check.py#declared_for_this_branch` (`:1910-1919`), which `fc573606d` changed. The frame does not cover this notice. `frame/design.md` G7 and *Scope* item 2, built in phase 3 of `frame/plan.md`, describe a workflow left in local mode, which runs in CI, where no clone holds a local root and the trailers are judged. Round 2's finding asked for the words "judged the commit trailers and nothing else" in both returns, although its own grounds said that at a local root each trailer is printed as a notice. `fc573606d` applied those words to the local-root return as well, and that is where the defect came from.

Why it matters: the local-root notice is printed only where `local_root(root, routing)` answers (`:1910`). `_checked` passes that same predicate to `trailer_findings` as `local` (`:2199-2201`). With `local` set, every trailer that names a work item becomes a `LOCAL_TRAILER` notice, which ends "printed, not judged" (`:1952-1956`, `:2014-2015`). A `no work item` trailer is a notice in every mode. So on this path no trailer is ever a problem, and the check exits 0 whatever the trailers say (`:2203-2208`). `docs/checks/the-routing-check.md` *At the pull request* states the same rule: "At a local root a work item's trailer is printed as a notice and never refused." The notice now says the opposite of the line printed under it. The probe built a repository with a marked root under `.git/seal` and a commit on `feature` carrying `Seal-Routing: some-item`, then ran the target's `chain_check.py --baseline main`. It printed, in one run:

- "So no routing declaration for `feature` can be read from what git carries, and the review-chain check judged the commit trailers and nothing else."
- "commit c0133de2 carries `Seal-Routing: some-item` in a repository whose root is local, where no routing declaration is committed for it to name: printed, not judged"

Before `fc573606d` this notice said the check "examined nothing", which was close to the truth at a local root. The fix turned it into a statement that is false in every run that prints it. A session reads this line when it runs `chain_check.py --worktree` in a local-mode clone: the proofer before it hands back, and the orchestrator. It then acts on a check that it believes judged its trailers, so the severity is `should`.

`ROOT_LEFT_SAYS` (`:1936-1941`) is a second statement of the same claim, and this work did not write it. It came in with #1034 (`2974871d`, executed: `git log -S`). The fix pass took its words from it. `_checked` prints it where the declarations left the tree with the root (`:2175-2176`). In CI no local root stands, so the claim holds there, and the case at `tests/skills/test_chain_check.py:4773-4795` holds it in that state. A session's `--worktree` run after `seal mode local` is a different state. There the root has moved under the common git directory, `gone` reads true, and `local_root` answers, so the trailers are printed, not judged (read: `:2170-2176`, `:2199-2201`). The class has these two statements. The snippet below reaches both, and the changelog's sentence that describes them. The two docstrings of `skills/implement/scripts/seal.py` that cite `ROOT_LEFT_SAYS` (`:1850-1853`, `:2420`) describe the workflow in CI, and they still hold.

The notice is a line a person reads, so the fix follows contract rule 14: a case pins each new text in the same commit, and the changelog says what changed.

```python
# skills/code-review/scripts/chain_check.py, after NO_WORK_ITEM_TRAILER (:1957-1961)
# What the review-chain check did with the commit trailers where nothing is
# declared: judged them, or, at a local root, printed them (`trailer_findings`).
JUDGED_TRAILERS = "judged the commit trailers and nothing else"
PRINTED_TRAILERS = (
    f"judged nothing: at a local root each commit's `{TRAILER}` trailer is "
    "printed, not judged"
)
```

```python
# skills/code-review/scripts/chain_check.py, ROOT_LEFT_SAYS (:1936-1941)
ROOT_LEFT_SAYS = (
    "the tree the check reads has no top-level `{home}` entry, so nothing is "
    "declared: the routing declarations this pull request deletes left the "
    "tree with the root, and the review-chain check {trailers}"
)
```

```python
# skills/code-review/scripts/chain_check.py, declared_for_this_branch, the two returns under `if not matching:`
    if not matching:
        home = local_root(root, routing)
        if home:
            return [], (
                f"this repository keeps its root at {home} — local mode, where "
                "nothing under the root is committed. So no routing declaration "
                f"for `{branch}` can be read from what git carries, and the "
                f"review-chain check {PRINTED_TRAILERS}. `seal mode shared` "
                "moves the root into the tree and gets the declarations judged."
            )
        return [], (
            "this pull request declared neither way, so the review-chain check "
            f"{JUDGED_TRAILERS}. Nothing git carries under `{work_items}/` "
            f"declares `{branch}`. Add {work_items}/<work-item>/"
            f"{routing.FILENAME} to declare."
        )
```

```python
# skills/code-review/scripts/chain_check.py, _checked (:2175-2176)
    if declarations and gone:
        said = PRINTED_TRAILERS if local_root(root, routing) else JUDGED_TRAILERS
        declarations, why = [], ROOT_LEFT_SAYS.format(home=home, trailers=said)
```

```python
# tests/skills/test_chain_check.py, the case at :3701-3709
    def test_local_mode_says_the_check_judged_nothing(self, repo):
        """Naming the root does not turn an untracked declaration into a checked
        one: CI reads what git carries, and local mode commits nothing. At a
        local root each trailer is printed, not judged, so the notice says the
        check judged nothing."""
        local_item(repo)
        _code, out = run_check(repo)
        assert (
            "the review-chain check judged nothing: at a local root each "
            "commit's `Seal-Routing` trailer is printed, not judged"
        ) in out, out
        assert "judged the commit trailers" not in out, out
        assert "examined nothing" not in out, out
        assert "through the review chain" not in out, out
```

```markdown
<!-- changelog.md:4, the last sentence of the entry on `seal mode local` and the workflow template -->
The review-chain check's own notice for a pull request that declares nothing now says the check judged the commit trailers and nothing else, where it said the check examined nothing. At a local root, where each trailer is printed and not judged, the notice and the one for a root that left the tree say the check judged nothing.
```

The snippets do not write one case: `ROOT_LEFT_SAYS` printed at a local root. Its fixture is the one of `test_accepts_every_declaration_leaving_with_the_root` (`:4773-4795`), with a marked root added under `.git/seal` after `git rm -rq seal`. The case asserts the `PRINTED_TRAILERS` words, and the fix pass owes it beside that case. The existing assert at `:4789-4794` keeps its full sentence, because that case runs with no local root. The snippets also leave the bold opening of `changelog.md:4` as it is, because "no longer say a run with nothing declared examines nothing" stays true.

## Confirmations

```seal
confirms: round-2#1
```
What holds: for the state round 2's finding was about, the close holds. That state is every pull request whose branch no committed declaration names, the workflow left in a local-mode repository among them. Run in CI, no local root stands there. The shared return at `chain_check.py:1920-1925` now says the check "judged the commit trailers and nothing else". `_checked` then judges the trailers: a trailer that names an undeclared work item is a problem, and an error on a ready pull request (`:2199-2208`, read). Round 2's probe printed that state's notice beside a judged trailer, and the line no longer contradicts what follows it. `test_the_shared_sentence_says_what_it_searched_and_for_what` pins the new words and the absence of "examined nothing" (read: `tests/skills/test_chain_check.py:3719-3728`). No other case of `Test_declared_for_this_branch` holds the shared return's words, so the new asserts cover something the group did not. The fix pass said its earlier search had run on `examine nothing`, which does not match `examined nothing`. A `git grep -n 'examined nothing'` outside `seal/threads/` and `evals/` now prints only `.github/scripts/issue_claims_check.py`, `skills/verify/SKILL.md:176` and their case, which concern other checks, `docs/layout/one-root-by-lifetime.md:150`, which a `## Rule changes` operation rewrites, and the two negative asserts of `fc573606d` (executed). Finding 1 above is the regression the same commit made in the local-root return.

What matched: the base merge leaves the two works standing together. The merge base is `02369a0e9` (executed: `git merge-base 99144eecd 459116a4e`). In `.github/scripts/close_issues_on_release.py`, #1572 rewrote `#_issue_api` and this work rewrote the comment over `SPENT_ON_CLOSE`, and the hunks are apart. In `tests/github/test_close_issues_on_release.py`, this work removed `import json`. #1572's new `_gh_answers` and `Test__issue_api` write each `gh api -i` answer as a string literal and use no `json` name. The only matches of `json` in the merged file are `--json` arguments inside strings (executed: `grep -n json`). In `tests/behaviour/test_chain_hooks_hardening.py`, this work removed the cases at `:215` and `:299`, and #1572 removed the batch sweep at `:569-935`. The module docstring that #1572 rewrote still names what the module holds, its packaging cases and its `seal/threads/` cases among them. `uvx ruff check` and `uvx ruff format --check` over `chain_check.py`, `tests/skills/test_chain_check.py`, the two merged test files and `close_issues_on_release.py` each exit 0, so the merge left no unused import and no undefined name (executed). #1572's plan predicted this meeting point, the `json` import, and the merged tree bears it out (read: `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/frame/plan.md:58`).

What matched: the orchestrator said `tests/github/test_close_issues_on_release.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/skills/test_chain_check.py` and `tests/lib/test_gitcmd.py` gave 362 passed after the merge. `bin/test -q` over the same four modules at `61c1042ea` gave 362 passed, exit 0 (executed).

What matched: the acceptance searches of `frame/design.md` S4, S5, S7, S9, S14 and S15 each print nothing and exit 1 over the merged tree, so #1572 brought back no unit this work removed (executed: each `git grep` as the design gives it, the first command of S14 among them).

What matched: the fix pass said each changed case was seen red against the old messages. That follows from the diff, because each case asserts words the old code did not print (read). The fix pass also said each `examined nothing` negative was seen red under `seal mutate`. A negative assert of words the new code never prints can only be shown red that way, and the round did not run it again.

What matched: the records read whole state nothing that the target contradicts, apart from `changelog.md:4`, which finding 1 locates. The quotes of `pr.md` stand word for word at `frame/plan.md` *Judgments of the run*: the title row's Judgment cell, and the gate row's Judgment cell whole (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite, the repository-wide lint and the format check (`Broad gate` of `seal/config.json`). The suite stays `unverified` (contract rule 2) | `seal/config.json` | the orchestrator's broad run, after finding 1 is closed |
| The close-issues workflow without the label step, on a push to `main` | `.github/workflows/close-issues-on-release.yml` | the close-issues run when this release reaches `main`, read by the repository owner (`gaps.md`) |
| The two `examined nothing` negatives that the fix pass saw red under `seal mutate`, not run again here | `tests/skills/test_chain_check.py:3708`, `tests/skills/test_chain_check.py:3728` | the sealer, from the fix pass's account |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-3/test_tmp_round3_local_notice.py <clone> <scratch>`: a repository with a marked root under `.git/seal`, branch `feature` with one commit carrying `Seal-Routing: some-item`, `chain_check.py --baseline main` run with no `GITHUB_` variable | exit 0, state unknown; prints the local-mode notice saying the check "judged the commit trailers and nothing else", then `commit c0133de2 carries ... printed, not judged` |
| `bin/test -q tests/skills/test_chain_check.py tests/github/test_close_issues_on_release.py tests/behaviour/test_chain_hooks_hardening.py tests/lib/test_gitcmd.py` at `61c1042ea` | 362 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the five files named under *Confirmations* | both exit 0 |
| the `git grep` commands of `frame/design.md` S4, S5, S7, S9, S14 and S15 over the merged tree | each prints nothing, exit 1 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 459116a4e --root <the branch worktree> --worktree`, run on this record before hand-back | exit 0 on an unknown pull request state; it names finding 1 as open, with no close block, and names the gate record and the guarantee as not yet written; no notice at a line of the design names a pin or a copy |
