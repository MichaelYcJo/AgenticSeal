# Review round 1: 1793593418-two-config-rows-show-the-seal-mark

```seal
target: be0548a17 against 4ab345cba
```

The target is the branch `feat/1204-the-seal-mark-is-drawn-only-in-the-terminal`
at `be0548a17` against its base `4ab345cba`. The release branch has since
moved on with #1281, and this round did not read that move. No earlier round
exists, so no fact was carried. Every coordinate below was opened at
`be0548a17`. No `seal/parity.md` is declared, so the round block carries no
`original:` line.

## Findings

### 1. `seal pr-body` run from another checkout of the repository writes no mark over a sealed work item and says nothing

```seal
severity: should
location: `skills/code-review/scripts/pr_body.py:743`, `skills/code-review/scripts/pr_body.py:323-356`, `tests/skills/test_pr_body.py`
evidence: executed `python3 test_tmp_cwd_probe.py`
```

Why it matters: the design and phase 1 claim that the repository is "the
one `seal pr-body` runs in" (`frame/plan.md` *Technical context*,
`trail/phases/phase-1.md` *Decisions settled while writing the code*).
`pr_body.py:743` builds that root from `os.getcwd()`. It reads the
guarantee from the item's own directory. The row and HEAD come from the
working directory's checkout. Before this change, `main` read nothing from
the working directory, and `seal pr-body <item>` gave the same body from any
directory.

The orchestrator in this repository runs from the main checkout and reaches
each work item in a linked worktree, as this round's own spawn did. In that
case `chain_check.py#follows` answers `("off", ...)`, because the main
checkout's HEAD does not descend from the sealed commit. `_seal_at_head`
returns `(False, None)` at `pr_body.py:356`, and no line is printed. The
docstring's grounds for the silence are that "every other way of not being
sealed is the sealer's and the pull request check's to name". That does not
cover this case. The work item is sealed at its own HEAD, so neither the
sealer nor the check names anything.

The probe built a repository with a `release` branch checked out and a
linked worktree on `feat`. The `feat` worktree held a work item whose
committed `guarantee.md` read `sealed` at the commit before it. Both
checkouts' `seal/config.md` read `Pull request seal mark | yes`. Run with
the worktree as the working directory, `main` wrote the mark. Run with the
main checkout as the working directory, it wrote no mark, printed only
`wrote: ...`, and exited 0.

Leaving this unfixed costs more than a missing picture. `frame/questions.md`
Q1 reads a body with no image as "the address or GitHub's handling of it
changed". A body written from the main checkout would trigger that
misreading, and nothing would point to the working directory. The class is
every read in `seal_mark` that depends on the working directory: the row
(`pr_body.py:398`, through `OPTIN.home_at(root)`), the base's resolution
(`:347-351`) and `follows` (`:353-355`). I listed it by following `root`
from `main` through `seal_mark` and `_seal_at_head` to every call that takes
it. The fix reads them all from the item's repository where git can find
one. Local mode keeps the working directory, because there the item sits
under the common git directory, and `git rev-parse --show-toplevel` exits
128 inside that directory, so `repo_root` answers "". A sealed commit that
the chosen HEAD cannot see is then named instead of passed over.

```python
# pr_body.py, main: the work item's own checkout where git finds one (shared
# mode); the working directory's where the item sits under the common git
# directory (local mode), where `repo_root` answers "".
root = OPTIN.repo_root(os.path.abspath(args.item)) or OPTIN.repo_root(os.getcwd())
mark, note = seal_mark(args.item, root)

# pr_body.py, beside BASE_UNSEEN:
NOT_IN_HISTORY = (  # NAME NOT IN TREE: new constant
    "the guarantee is sealed at `{sha}`, which HEAD of {root} does not hold, "
    f"so whether its seal is at HEAD is not read and {NO_MARK}"
)

# pr_body.py, _seal_at_head, replacing its last line:
if behind is not None and behind[0] in ("unseen", "off"):
    return False, NOT_IN_HISTORY.format(sha=target["commit"][:8], root=root)
return behind is None, None
```

Precondition: `repo_root` runs `git -C <dir> rev-parse --show-toplevel` and
answers "" where git exits non-zero, which it does inside a `.git`
directory. A case in `Test_main` runs `main` from a second worktree's
directory over the first worktree's sealed item and asks for the mark. The
design's *Technical context* sentence "`pr-body` asks `follows` with the
root of the repository it runs in" is rewritten to match.

### 2. After a repair on an open pull request, nothing runs `seal pr-body` once the repair is sealed, so the mark leaves the body for good

```seal
severity: should
location: `skills/code-review/orchestration.md:309-319`, `skills/code-review/orchestration.md:389-396`
evidence: read `skills/code-review/orchestration.md:220-230`, `skills/code-review/orchestration.md:284-319`, `skills/code-review/orchestration.md:389-405`, `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/plan.md:66`, `seal/threads/1793593418-two-config-rows-show-the-seal-mark/changelog.md:3`
```

Why it matters: the changelog fragment claims "A body rewritten after a
later repair carries no mark until the repair is sealed". `frame/plan.md`
row A1 is chosen on the same ground: "it drops the mark from a body
rewritten after a repair until the repair is sealed". Both promise that the
mark comes back.

The orchestration text for that path never brings it back. For a pull
request already open, `orchestration.md:315-319` runs `seal pr-body` once
the repair's broad run is committed. That is before the sealer runs again,
and it gives that file to the pull request with `gh api -X PATCH`.
`:393-396` does the same before the sealer's next spawn. At that point the
older `sealed` block is behind HEAD, so the run writes no mark, which is
correct. The sentence this work added at `:222-230` runs `seal pr-body`
after the seal only on the way to `gh pr create`, so it covers only the
first opening. After the new `sealed` is committed on an open pull request,
no step writes the body again. The merge from the base at `:290-294` takes
the same path whenever it falls after the pull request opens.

So every pull request repaired after it opened ends with no mark, and the
changelog line tells its reader otherwise. An orchestrator reads and acts on
this sentence, which makes it a `should`. The fix is one sentence in the
stated limit, and the paragraph at `:389` already points there.

```markdown
the file to the open pull request with
`gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>`, not
`gh pr edit`: that command's GraphQL query has stopped on an error about
Projects (classic), and the REST call sends the body alone. Once the
sealer's next `sealed` is committed, run `seal pr-body` on the body file
once more and give it to the pull request the same way: the body given
before that seal carries no mark, and only a run after it writes the one
the `Pull request seal mark` row asks for.
```

### 3. Two of the design's rule changes copy the row documentation `templates/setup/config.md` *The seal mark* keeps, so after the settle each fact stands twice

```seal
severity: should
location: `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/design.md:201-215`, `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/design.md:226-248`, `templates/setup/config.md:435-472`
evidence: read `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/design.md:186-248`, `templates/setup/config.md:435-472`, `docs/the-pact.md:73-99`
```

Why it matters: `skills/core/SKILL.md` *The rule a mechanism is kept
against* says "A fact has one source, and every other place links to it".
`docs/one-root-by-lifetime.md` names `templates/setup/config.md` as the
place where a row is documented. This branch writes *The seal mark* there.
That section states three facts:

- the meaning of each value: `yes` exactly, absent or empty, and any other
  value named;
- for the release row, "The plugin ships no release workflow, so in any
  other repository nothing reads this row" (`:467-468`);
- that the mark's address ties a body to the plugin's repository staying
  public and to the version's tag existing (`:459-460`).

I took the design's `## Rule changes` apart into its three operations and
read each `to` against that section.

- The `add` for `docs/the-review-record.md` *The guarantee* repeats the
  value meanings (`design.md:237-238`, "An absent or empty row puts no mark,
  and any other value puts none and is named as not read"). It also repeats
  the address tie (`:245-247`).
- The `change` for `docs/branch-and-release.md` *Cutting a release* repeats
  the value meanings (`:212-214`). It also repeats the sentence that the
  plugin ships no release workflow (`:214-215`).
- The `change` for `docs/release-checklist.md` *6. After the merge* states
  only what the person ticking the box acts on. It is not a copy in this
  sense, and it stays.

The settle writes each `to` into `docs/`, so a later change to a value's
meaning or to the address must edit two files. Rule 19's search finds the
second file only if the wording still matches. The cost is small, and
removing the copies costs only the sentences themselves.
`docs/the-pact.md` and the template's *Pact* section show the pattern: the
policy keeps its rule, and the template keeps the row's values. The fix
keeps in each `to` what the policy owns: the condition, the meaning beside
*The stamp*, the unresolved base, the sealer's check and the orchestrator's
second run. Everything else cites the template.

```text
  to: It runs the suite at the tag and replaces the note's header with a
    table whose last cell holds the results the stamp states, as text, one
    per line. They are the sealed version and commit, the pull requests
    merged, the issues closed, the outside contributors where there are
    any, the suite's counts, the work items and their review rounds, how
    many were capped, and the issues deferred. Where `seal/config.md`'s
    `Release note seal mark` row reads `yes` at the tag, the job first
    attaches the page form of the stamp's mark, the PNG that
    `.claude-plugin/plugin.json` names as its `icon`, as `seal.png`, and the
    table opens with a cell holding that image at its display width. Its
    alt text names the image alone, because the results' cell carries every
    number. Under any other value nothing is attached and the table is the
    results' cell alone; `templates/setup/config.md` *The seal mark* states
    the row's values and who reads it.
```

```text
  to: **A pull request body carries the seal mark only where the
    repository turns it on and the work item is sealed at HEAD.**
    `seal pr-body` writes the mark, the plugin's icon at the tag of the
    plugin's version, as the first line under the line
    `skills/code-review/scripts/pr_body.py#HEADING` holds. It writes it
    where `seal/config.md`'s `Pull request seal mark` row reads `yes` and
    the newest verdict block of `guarantee.md` reads `sealed` at a commit
    that only the closing records follow, so the mark means what the stamp
    means (*The stamp*). A base the verdict block names that git cannot
    resolve where the command runs puts no mark either, and is named, since
    whether the seal holds at HEAD cannot then be read. The row's other
    values, and what the mark's address ties a body to, are
    `templates/setup/config.md` *The seal mark*'s. The sealer's
    `seal pr-body --check` runs before its own verdict exists, so the copy
    it checks carries no mark from that run. The orchestrator runs
    `seal pr-body` once more after it commits a `sealed` guarantee, and that
    run changes no copied line, because the copy reads no `guarantee.md`.
    check: tests/skills/test_pr_body.py
```

## Confirmations

```seal
confirms: none
```
What matched: the mark follows the stamp's condition, as `frame/design.md`'s
*Grounding* row on *The stamp* claims. `pr_body.py:337-343` reads the
guarantee through `CHAIN.FIELDS.read(text, CHAIN.FIELDS.GUARANTEE)`. It
returns no mark on a refusal or no block, and asks the newest block's
`verdict_word` for `sealed`. This is the read
`skills/verify/scripts/seal_stamp.py:1145-1160` makes for the stamp, the
reader `docs/the-review-record.md` *The stamp* names. The mark adds one
condition the stamp lacks. `follows` must find the sealed commit at HEAD or
followed only by `CLOSING_RECORDS` (`pr_body.py:353-356`), which is what
`chain_check.py:1669-1680` asks of a ready pull request. The phase-1 claim
that a refused block after a sealed one puts no mark holds: that case
passed in this round's run. Read, and executed through the narrow run under
*Probes*.

```seal
confirms: none
```
What matched: each row reads only `yes` and names any other value.
`pr_body.py:398-404` and `.github/scripts/release_seal.py:414-436` take
`hooks/lib/config.py#declared_value`. Each says nothing on an absent or
empty row. Each names a refusal and any value that is not exactly `yes`.
Each changes no exit code. The cases for `Yes`, `on`, `true`, absent, empty
and a row written twice pin the full sentence in both modules
(`tests/skills/test_pr_body.py`, `tests/github/test_release_seal.py`).
`hooks/lib/config.py:450-470` returns the value stripped and never
case-folded, so `Yes` stays `Yes`. Executed through the narrow run, and
read.

```seal
confirms: none
```
What matched: the terminal stamp is untouched. `git diff --stat
4ab345cba..HEAD` over `skills/verify/scripts/seal_stamp.py`,
`skills/verify/scripts/seal-mark.txt`, `hooks/sealer-stamp-queue.py`,
`hooks/sealer-stamp.py` and `.claude-plugin/` printed nothing and exited 0
(executed). The `--stat` of the whole branch lists twenty files, none of
them under those paths.

```seal
confirms: none
```
What matched: the keep test the issue names. `frame/design.md` *Removes*,
its last row, weighs the mark by cost alone. The design adds no hook,
check, label or file. It adds two row reads in the two steps that already
write their surfaces, one `follows` call, and one more `seal pr-body` run
per sealed work item. The diff holds exactly that: `seal_mark` and
`mark_on`, and no new file outside the work item, the test modules and the
template section (read, `git diff --stat`, executed). Finding 2 adds one
more `seal pr-body` run and `PATCH` per repaired open pull request, which
the design already prices as "one more command".

```seal
confirms: none
```
What matched: the release half. `release_seal.py:546-554` reads the row
before `draw`, which phase 2 names as its departure from `frame/plan.md`,
with grounds. Read after the header guard, an off row would still run
`draw`, and a refused draw would lose the results. The upload stays after
the guard (`:586-597`), so the plan's purpose for the placement holds. The
off path makes one `gh release edit` and no upload. `sealed_header` with no
image returns `table(lines)`
(`.github/scripts/publish_release_note.py:663-664`). The S7 case pins that
the one-cell table equals the two-cell table with its image cell removed.
The re-run case runs under `yes` and absent. Read, and executed through the
narrow run.

```seal
confirms: none
```
What matched: local mode, the row `gaps.md` hands to the proofer. In local
mode no commit touches `seal/threads/<name>/`, so `follows` at
`chain_check.py:972-986` returns `("after", ...)` for any later commit.
`_seal_at_head` therefore writes a mark only where the sealed commit is
HEAD. `pr_body.py:352` builds the same `seal/threads/<name>` prefix in
either mode, which matches `gaps.md`'s claim. Finding 1's fix keeps the
working directory for this mode. Read.

```seal
confirms: none
```
What matched: the rule-change notices. The tree's `chain_check.py` run
over the worktree printed no notice on this design's `## Rule changes`
(executed, see *Probes*). I read each `from` against the tests that pin the
sentences it removes. `tests/behaviour/test_the_release_seal_is_drawn.py:54`
pins "the same workflow's `seal` job attaches `seal.png`". The checklist's
`to` keeps that wording, and it is a fact the person ticking the box acts
on, so no finding. `tests/github/test_publish_release_note.py:882`'s
docstring "the same table with two cells" describes the case it stands in,
which builds the header with an image, so it still holds. No `from` takes
out a pin of a rule's wording. The repeats found are finding 3.

```seal
confirms: none
```
What matched: the new tests against their groups. Phase 1 and phase 2 each
claim that `seal layout --pairs` named 0 pairs for the changed modules. I
did not re-run that, and rest on it as read. I read the new cases of
`Test_seal_mark`, `Test_main`, the S6 and S8 cases and the S7 case against
the other cases of their functions. S7, in `test_publish_release_note.py`,
and S6, in `test_release_seal.py`, both state the one-cell table. Only S7
holds its equality with the two-cell table, and only S6 holds the job's
upload and warning, so neither is covered by the other.
`test_accepts_the_plugins_own_manifest` is the only case that reaches the
default `MANIFEST` path. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the work item's head: the full suite, the repository-wide lint and the format check. This round ran five modules alone, and the suite stays `unverified` | the branch at `be0548a17` | the orchestrator, by `seal gate` after the rounds settle; the sealer's spawn follows it |
| Whether a pull request page draws the mark line as the icon at desktop and phone width | `frame/questions.md` Q1 | a measurement on the first body written after a seal by 0.28.0 or later. Finding 1 bears on reading it |
| Whether the mark at width 128 looks as the owner wants | `frame/questions.md` Q2 | the owner |
| The new cases on Linux and Windows | `tests/skills/test_pr_body.py`, `tests/github/test_release_seal.py` | the orchestrator, by the `tests` workflow or CI on the pull request |
| The `seal` job at the 0.28.0 tag, reading the row from the checkout | `.github/workflows/publish-release.yml` | the orchestrator, from the job's log and the published note of 0.28.0 |
| Where `apply_op` places the three rule changes after #1153's | `frame/design.md` *Rule changes* | the orchestrator, by `seal chain-check` at the pull request |
| Edges weighed and not raised. A guarantee edited on disk and not yet committed is read as it stands, which `plan.md` A1 states as outside the flow. `seal_mark` runs outside `main`'s `try`, so a `git` timeout in `follows` would print a traceback; `follows` already runs at every chain check, and its 60 s timeout has no recorded hit. No case runs `DRY_RUN=1` with the row off, which `gaps.md` *Not done* answers. Each would cost a reader less than a finding's fix pass | `skills/code-review/scripts/pr_body.py:743`, `.github/scripts/release_seal.py:546` | none owed; recorded so the next round does not search again |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py tests/github/test_release_seal.py tests/github/test_publish_release_note.py tests/text/test_the_settings_have_a_front_door.py tests/behaviour/test_the_release_seal_is_drawn.py -q`, in a `git clone --no-local` of the branch at `be0548a17` | 176 passed, exit 0 |
| `python3 test_tmp_cwd_probe.py`, one file in the round's scratch directory, run once and deleted with the repository it built. It loads the clone's `pr_body.py`, builds a repository with `release` checked out and a linked worktree on `feat` holding a work item sealed one commit back, sets the row to `yes` in both, and runs `main` once from each checkout | from the worktree: the body holds the mark, exit 0. From the main checkout: no mark, no `seal pr-body:` line, only `wrote: ...`, exit 0 |
| `git -C <the main checkout>/.git rev-parse --show-toplevel` | `fatal: this operation must be run in a work tree`, exit 128, so `repo_root` answers "" inside the common git directory |
| `python3 skills/code-review/scripts/chain_check.py --baseline 4ab345cba --root <the worktree> --worktree`, before the record was written | exit 0. It names the missing round record, `trail/gate.md` and `guarantee.md`, and prints no rule-change notice |
