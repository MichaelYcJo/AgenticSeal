# Review round 1: 1794187229-the-body-carries-the-seal-mark

```seal
target: 89de04fa against 1af09327
```

The whole-diff round: the branch at `89de04fa` against `origin/release/v0.36.0`
at `1af09327`, read against issue #1452 (no comments, read with `gh issue
view`), the three frame files, `gaps.md`, `changelog.md`, `pr.md` and the
four phase records, each read whole at the target. This is round 1, so no
fact is carried from an earlier round; every fact below was established in
this round. The record language is English, since `seal/config.md` holds no
`Record language` row.

## Findings

### 1. The body arm drops the seal mark from its composition once the base moves past the guarantee's base, so a correct body is refused and `seal pr-body` cannot clear it

```seal
severity: must
location: `skills/code-review/scripts/pr_body.py:414`, `skills/code-review/scripts/pr_body.py:480`, `skills/code-review/scripts/pr_body.py:846`, `skills/code-review/scripts/chain_check.py:1797`, `skills/code-review/scripts/chain_check.py:2147`, `tests/skills/test_chain_check.py:3178`
evidence: executed `bin/test tests/skills/test_tmp_body_probe.py -p no:xdist -q` in `<scratchpad>/1452-r1/clone` (the probe in `## Probes`); read `skills/code-review/scripts/pr_body.py:390-427`, `skills/code-review/scripts/chain_check.py:1001-1036`, `skills/code-review/scripts/chain_check.py:2138-2144`
```

Why it matters: the frame says the arm composes "the body `seal pr-body`
would write at HEAD", with the mark "where the row and the guarantee give
one" (`frame/design.md:38-43`). It also says the CI checkout is the merge
commit, "the tree the guarantee arm already reads HEAD as"
(`frame/design.md:190-192`). The two readers of "sealed at HEAD" do not ask
the same question in CI.

- The guarantee arm calls `follows(root, sha, args.baseline, ...)`, so the
  base it excludes is `origin/<base>`, the base's tip at the run
  (`chain_check.py:2140`).
- The body arm calls `compared(item, text, root)` with no base
  (`chain_check.py:1797`). That calls `seal_mark`, then `_seal_at_head`,
  which takes the base from the guarantee's own `target:` line
  (`pr_body.py:414`). The sealer writes that base as a SHA: this repository's
  guarantees read `95f5efaa against c7bb14ca` and `bdcd5626b against
  9e758b0b0` (`git show` of two merged items' `guarantee.md`).
- In CI, HEAD is the pull request's merge ref, the head merged into the
  base's current tip. A pull request another squash landed before on the
  base, after the seal, then reaches HEAD and not the recorded base.
  `follows` lists that commit as `after`, `_seal_at_head` answers not
  sealed, and it returns no note (`pr_body.py:420-427`).

The probe built exactly this case: `bodied`'s repository with the
guarantee's base written as the fork point's SHA, one more commit on `main`
after the seal, and HEAD detached at `main` merged with `feature/g`. With
the body `seal pr-body` composes at the branch head as the payload, the
check exited 1 with one line and no notice:

```text
seal/threads/1791999999-a-work-item:0  the pull request's body, line 3: reads ``, then `<img src="https://github.com/MichaelYcJo/AgenticSeal/raw/HEAD/.claude-plugin/icon.png" alt="Sealed" width="128">`, which the records do not give
```

The guarantee arm refused nothing in the same run. The repair that
`skills/code-review/orchestration.md:265-270` asks for, `seal pr-body` once
more and a `gh api -X PATCH`, writes the same body on the branch, so the red
stays. This happens on the release branches this repository runs: parallel
items merge one after another, and each later pull request's `edited` run
or opening run sees a base that moved after its seal. The `edited` event
this item adds is exactly the run that meets it, since the mark repair is a
body edit. It contradicts the design's failure direction, "item 6 is what
makes that run clear the refusal whatever copy of the plugin composes"
(`frame/design.md:144-146`), and S2's "the arm prints nothing and the check
exits 0" (`frame/design.md:155`). The case set cannot see it, because the
fixtures' guarantee names its base as `main`, a branch that moves with the
base (`tests/skills/test_chain_check.py:185`).

The fix gives the composition the base the check runs against, so both
arms read one fact. A local `seal pr-body` keeps reading the guarantee's
base, which is right on the branch head, where no later base commit is
reachable.

```python
# skills/code-review/scripts/pr_body.py
def _seal_at_head(item, root, base=None):
    """... `chain_check.py#follows` finds the commit its `target:` names to be
    HEAD or followed only by the closing records, against BASE where it is
    given, the base the pull request's check runs against, and otherwise the
    base the same line names. ..."""
    ...
    target = newest.fields[CHAIN.FIELDS.TARGET].match
    base = base or target["base"]
    ...


def seal_mark(item, root, manifest=None, base=None):
    ...
    sealed, note = _seal_at_head(item, root, base)
    ...


def compared(item, body, root, manifest=None, base=None):
    """... the seal mark `seal_mark` gives from MANIFEST or the plugin's own,
    read against BASE where it is given ..."""
    mark, note = seal_mark(item, root, manifest, base)
    ...


# skills/code-review/scripts/chain_check.py
def body(root, items, text, why, base=None):
    """... compared through `pr_body.py#compared`, the mark read against
    BASE, the base the guarantee arm reads, ..."""
    ...
    note, causes = pr_body_reader().compared(
        os.path.join(root, *item.split("/")), text, root, base=base
    )
    ...

# in main
        found, unread_body = body(root, bodied, text, said, args.baseline)
```

The fix also owes a case in `Test_body` that the check above refuses
before the fix and passes after it. The case writes the guarantee's base
as a SHA, adds a base commit after the seal, and checks out the merge, as
the probe did. The docstrings of `_seal_at_head`, `seal_mark`, `compared`
and `body` that name the base change with the code. `frame/design.md`
*Data & interfaces* already says what the fix makes true, and
`changelog.md` holds no sentence on the base, so neither needs an edit.

```seal
verdict: fixed 1012b256
answer: Applied as the finding reads, after reading it against the tree: `chain_check.py#guarantee` calls `follows` with `args.baseline`, and `_seal_at_head` took the base from the guarantee's `target:` line. `_seal_at_head`, `seal_mark` and `compared` take `base=None`, `body` takes it and passes it on, and `main` passes `args.baseline`; with no base given, the guarantee's own base is read, so `seal pr-body` and `--check` at the branch head are unchanged. `Test_body::test_accepts_the_body_at_a_merge_past_a_later_base_commit` writes the guarantee's base as the fork point's SHA, lands one commit on `main` after the seal, and checks the merge with `GITHUB_HEAD_REF` set. It was seen red before the fix, with the line this finding quotes, and red again under three mutations after the commit: the base dropped from `body`'s call to `compared`, from `main`'s call to `body`, and from `_seal_at_head`. The docstrings of the four functions and the module docstring's `body` row say the mark is read against the check's base; `722f0727` rewraps them and changes no word.
```

### 2. `pr.md` carries none of what `CONTRIBUTING.md` asks a gate change's pull request to say, which the frame says the pull request copies

```seal
severity: must
location: `seal/threads/1794187229-the-body-carries-the-seal-mark/pr.md:1-12`
evidence: read `CONTRIBUTING.md` *What a change to a gate must carry*, `seal/threads/1794187229-the-body-carries-the-seal-mark/frame/design.md:11`, `seal/threads/1794187229-the-body-carries-the-seal-mark/frame/design.md:142-148`, `seal/threads/1794187229-the-body-carries-the-seal-mark/frame/design.md:304-310`, `skills/code-review/scripts/pr_body.py#_composed`
```

Why it matters: `routing.md` names this a change to a check on the pull
request, governed by `CONTRIBUTING.md` *What a change to a gate must carry*.
That section asks the pull request to state the failure direction, the
prompt budget, the platforms not tested and what the change removes. The
frame's G3 says these "are stated in this design under *Scope*, *Removes*
and *Data & interfaces*, and the pull request copies them from here"
(`frame/design.md:11`). The body is `pr.md` plus the records' copy, and the
copy holds the changelog, the plan's phases, the rounds, the gate record,
`gaps.md` and the questions table, never `frame/design.md`
(`pr_body.py#_composed`). `pr.md` quotes the changelog, the plan's prefix
row and one `gaps.md` row, and none of the four items. The changelog
fragment states what the arm reads and names as not read, so the fifth item
reaches the body through the copy. Earlier gate changes quoted the design
for these, for example `seal/threads/1794128303-the-plugin-ships-two-hooks-again/pr.md`
at `1af09327`. `pr.md` is the orchestrator's to repair.

```markdown
- "The failure direction, for `CONTRIBUTING.md` *What a change to a gate must carry*: the arm blocks more." (`frame/design.md` *Scope*, the failure-direction paragraph)
- "A wrong deny, a correct body refused, costs one `seal pr-body` run and one `gh api -X PATCH`, or one push, and no person; item 6 is what makes that run clear the refusal whatever copy of the plugin composes (G21)." (`frame/design.md` *Scope*, the failure-direction paragraph)
- "The arm puts no question in front of a person." (`frame/design.md` *Scope*, the failure-direction paragraph)
- "Platform: `hygiene` runs on `ubuntu-latest`, and the suite's new cases run on every leg of `tests`." (`frame/design.md` *Scope*, the failure-direction paragraph)
- "No mechanism goes." (`frame/design.md` *Removes*, the paragraph under the table)
- "What it would have caught is G10's: every pull request of 0.36.0." (`frame/design.md` *Removes*, the paragraph under the table)
```

These go above `Closes #1452.`. Each was checked word for word at its
coordinate with whitespace collapsed. The second quote is true only once
finding 1 is fixed, so it is added after that fix.

```seal
verdict: fixed a61f0fb0
answer: The orchestrator repaired `pr.md` at `a61f0fb0`: the six quotes stand above `Closes #1452.`, read at HEAD. The second quote holds since finding 1's fix at `1012b256`, where `seal pr-body` run again clears a refusal at the merge commit too.
```

### 3. Several judged work items with no `pr.md` are named with the sentence for two holders of `pr.md`, and neither that shape nor a refusal placed at a record has a case

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1749-1752`, `skills/code-review/scripts/chain_check.py:1790-1796`, `skills/code-review/scripts/chain_check.py:1810-1811`, `tests/skills/test_chain_check.py:3184`
evidence: read `skills/code-review/scripts/chain_check.py:1775-1812`; executed `git grep -n "pr.md:\|NO_OWN_PART\|several judged\|none of which" -- tests/skills/test_chain_check.py` (exit 1, no match)
```

Why it matters: `body` names the body as not read for each item where
several judged items hold no `pr.md` (`chain_check.py:1790-1796`). It does
so with `BODY_SPLIT`, which reads "the pull request carries more than one
judged work item holding `pr.md`" (`chain_check.py:1749-1752`). In that
shape no item holds one, so the line tells the reader something false. The
design's rule change separates the two shapes: "more than one judged work
item holding a `pr.md`, or several judged work items none of which holds
one" (`frame/design.md:237-239`). Neither branch has a case in `Test_body`.
Nor does the branch that places a cause `compared` gives at a record, such
as a missing `pr.md`, at that record's path (`chain_check.py:1810-1811`).
*Scope* item 1 and the rule change both state that behaviour. Phase 2's
mutation list breaks neither branch.

```python
# skills/code-review/scripts/chain_check.py, beside BODY_SPLIT
BODY_NONE_HOLDS = (
    f"the pull request carries more than one judged work item and none holds "
    f"`{PR_FILE}`, and one body is one work item's"
)

# in body()
    else:
        why = BODY_SPLIT if holders else BODY_NONE_HOLDS
        return [], [(i, 0, BODY_UNREAD.format(why=why)) for i in holders or items]
```

```python
# tests/skills/test_chain_check.py, in Test_body
    def test_names_the_body_as_not_read_for_two_work_items_without_pr_md(
        self, bodied, tmp_path, monkeypatch, capsys
    ):
        """*Scope* item 1: several judged work items none of which holds a
        `pr.md` are named as not read for each, in a sentence that says none
        holds one."""
        root, early, _late = bodied
        git(root, "rm", "-q", f"{ITEM}/pr.md")
        write(root, f"{SECOND_ITEM}/routing.md", SEALED_ROUTING)
        commit(root, "a second work item, and no pr.md")
        payload(tmp_path, monkeypatch, early)
        _code, out = check(root, capsys)
        said = (
            "not read: the pull request's body, since the pull request carries "
            "more than one judged work item and none holds `pr.md`, and one "
            "body is one work item's"
        )
        assert body_lines(out) == [f"{SECOND_ITEM}:0  {said}", f"{ITEM}:0  {said}"], out

    def test_refuses_a_missing_pr_md_at_its_path(
        self, bodied, tmp_path, monkeypatch, capsys
    ):
        """*Scope* item 1: a cause `compared` places at a record is refused
        at that record's path under the work item, as every other arm
        refuses a record."""
        root, _early, late = bodied
        git(root, "rm", "-q", f"{ITEM}/pr.md")
        commit(root, "pr.md taken out")
        payload(tmp_path, monkeypatch, late)
        code, out = check(root, capsys)
        assert code == 1, out
        assert f"{ITEM}/pr.md:0  {PR_BODY.NO_OWN_PART}" in out.splitlines(), out
```

The module docstring's `body` row (`chain_check.py:75-86`) names only the
two-holder shape among the not-read cases, so it gains "or several none of
which holds one". `changelog.md` *Fixed*, the first item, is a summary that
names the two-holder shape alone. It is not false, and the fix pass may leave
it. Each new case is seen red against the code as it stands before its fix.

```seal
verdict: fixed 1012b256
answer: `BODY_NONE_HOLDS` stands beside `BODY_SPLIT`, and `body` names the shape with no holder of `pr.md` in it; the module docstring's `body` row and `body`'s docstring name both shapes. The two cases are the finding's, as written. `test_names_the_body_as_not_read_for_two_work_items_without_pr_md` was seen red before the fix on the two-holder sentence, and red again with `BODY_SPLIT` put back for both shapes. `test_refuses_a_missing_pr_md_at_its_path` pins behaviour the code already had, so it was seen red with the record's cause placed on the work item's directory, where the line read `seal/threads/1791999999-a-work-item:0` and not `.../pr.md:0`. The `changelog.md` *Fixed* first item now names both shapes too, so the closed set of this item's records says one thing.
```

### 4. The two-manifest case covers nothing its group does not already cover, and `version` leaving `MARK_FIELDS` has no case

```seal
severity: should
location: `tests/skills/test_pr_body.py:628-647`, `tests/skills/test_pr_body.py:768`
evidence: read `tests/skills/test_pr_body.py:275-287`, `tests/skills/test_pr_body.py:620-660`, `tests/skills/test_pr_body.py:768-775`, `skills/code-review/scripts/pr_body.py:239`, `skills/code-review/scripts/pr_body.py:430-455`
```

Why it matters: `test_accepts_a_seal_only_its_guarantee_follows` already
asserts the line for a manifest whose `version` is `1.2.3` equals the
`raw/HEAD` line (`test_pr_body.py:620-626`, with `MARK_LINE` at
`test_pr_body.py:283-286`). `test_accepts_the_plugins_own_manifest` asserts
the same for the plugin's own manifest. Any `_mark_line` that puts the
version into the address turns both red, so the new case's second manifest,
`9.9.9`, separates no implementation the group lets through. Phase 4 claims
the case "ran red against `_mark_line` as it stood before this phase". That
claim holds, and the two older cases go red on the same break. The diff
also takes `version` out of `MARK_FIELDS` and out of the parametrized
`test_refuses_a_manifest_lacking_a_field` (`test_pr_body.py:768`). No case
then holds that a manifest with no `version` still gives the mark. A
`MARK_FIELDS` that kept `version` would pass every case. The design lists
that removal in *Removes*, so the case is owed. One edit to the new case
covers both: make its second manifest lack `version`.

```python
    def test_accepts_one_mark_line_from_two_releases_of_the_plugin(
        self, repo, tmp_path
    ):
        """#1452, *Scope* item 6 and S10. The installed plugin writes the
        body and the check's copy composes it again, and the two can be
        different releases. A manifest with a `version` and one with none
        give one mark line, the icon at the repository's default branch, so
        the address reads no version and the manifest need not hold one."""
        item = sealed_item(repo)
        (tmp_path / "older").mkdir()
        (tmp_path / "newer").mkdir()
        older = manifest_of(tmp_path / "older", MANIFEST)
        newer = manifest_of(
            tmp_path / "newer",
            {k: v for k, v in MANIFEST.items() if k != "version"},
        )
        lines = {PR.seal_mark(str(item), str(repo), m)[0] for m in (older, newer)}
        assert lines == {MARK_LINE}
```

It is seen red with `"version"` put back into `MARK_FIELDS`, where the
second manifest gives no line and the set holds `None`. The comment above
the `MANIFEST` fixture (`test_pr_body.py:275-277`) still says the fixture
keeps `version` "which the address does not read", and that stays true.

```seal
verdict: fixed 1012b256
answer: The two-manifest case's second manifest now lacks `version`, and the case compares the set with `MARK_LINE`; its docstring says how it was seen red. With `"version"` put back into `MARK_FIELDS` the case went red with the set holding None beside the line, which no other case of the group does.
```

## Confirmations

What matched: every quote in `pr.md` stands word for word at the coordinate
it names, with runs of whitespace collapsed (executed: a `python3 -c`
comparison of each list line's quote against `changelog.md`,
`frame/plan.md` and `gaps.md`, all ten `True`). Each quote's item position,
first, third and fourth in *Fixed*, the *Updating* paragraph, the prefix
row and the second *Not verified* row, matched on reading.

What matched: *Scope* item 2. `compared` returns `(note, causes)` and raises
nothing. `main --check` calls it (`pr_body.py:836-853`, `pr_body.py:894-908`),
and `_first_part` and `_check` name every line of an inserted or deleted run
through `_run` (`pr_body.py:776-830`) (read). Phase 1 claimed the `_body`
read moved ahead of the composition. `pr_body.py:896` confirms it, and the
departure it names, a double fault naming the body file first, stands as
claimed (read).

What matched: *Scope* item 1's other shapes. A payload with no body field,
a `body` of another type, `null` read as `""`, `--worktree`, `--sealing`
turning the arm's findings into notices, and a draft printing and exiting 0
are all in `chain_check.py:577-599` and `chain_check.py:2145-2155` (read).
Each has its case in `Test_body`, and the three touched modules passed
(executed: `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/text/test_ci_gives_the_checks_what_they_need.py -q`
in the clone, exit 0, 300 passed). The run reaches the body arm only where
a declaration is judged. A pull request with none, a settle or a release
pull request whose items another squash carried among them, returns before
the arm (`chain_check.py:2072-2078`) (read).

What matched: `frame/questions.md` Q1, answered (b). A cause with no record
is annotated on the work item's directory at line 0, and its message
carries the body's line (`chain_check.py:1802-1809`) (read).

What matched: *Scope* items 3 and 4. `templates/setup/hygiene.yml` and
`.github/workflows/hygiene.yml` list `edited` with the comments the design
asks for. `test_the_edited_event_runs_wherever_the_body_is_read` requires
it wherever `chain_check.py` runs and refuses it nowhere. The core's row,
`skills/code-review/orchestration.md`'s two paragraphs, `pr_body.py`'s
*Limits* line and `chain_check.py`'s docstring say what *Scope* item 4
names (read, in the diff against `1af09327`).

What matched: *Scope* item 6 and `## Removes`. `_mark_line` builds
`<repository>/raw/HEAD/<icon>`, and `MARK_FIELDS` reads
`("repository", "icon")` (`pr_body.py:239`, `pr_body.py:453`). The
`version` row of the parametrization is gone, the `templates/setup/config.md`
sentence and the `hygiene.yml` comment are rewritten in place, and no
`raw/v` stands outside the work item's records (executed: `git grep -n
"raw/v" HEAD` outside the work item's directory, exit 1). The one sentence
still on the tag address is `docs/forms/the-guarantee.md:40`, which the
design's second `change` on that file rewrites at the settle, as a
code-subject work item leaves the policy root (read). Phases 3 and 4 called
their lists of old-fact sentences samples, as rule 12 asks. A `git grep` on
`seal pr-body`, `pr-body --check`, `tag of the` and `read by nobody` found no
sentence outside the policy root that the change makes false (executed).

What matched: the suite's label. `gaps.md` *Not verified* names the full
suite, the lint and the format check as unrun, with the orchestrator's broad
run as their answerer, and no phase record calls the suite green. The label
is honest (read).

What matched: the security axis. The body is untrusted text from a fork's
pull request. It reaches `difflib` and the annotation message only. The
workflow keeps `contents: read`, and the arm writes nothing. `annotate`
does not escape the message (`skills/verify/scripts/unverified_check.py:1329-1339`).
The body is split by `gfm_lines` before any line is quoted, so no quoted
line carries a line end that could start a workflow command (read).

`python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.36.0 --worktree`
over the worktree printed no notice on a test pin or a copy at a line of
`frame/design.md` (executed). So no finding here comes from such a notice.

## Not judged

| What | Location | Who answers |
|---|---|---|
| how GitHub shows an annotation on a directory at line 0, which no case can run | `gaps.md` *Not verified*, the second row | the first `hygiene` run that refuses a body, read on the pull request's checks |
| the full suite, the repository-wide lint and the format check at `89de04fa`; this round ran three modules only | the branch | the orchestrator's broad run |
| a bot or an integration that rewrites a pull request body after it opens, which the arm then refuses on every run; the design names neither the shape nor a limit sentence for it | `frame/design.md` *Rule changes*, the `add` on *What the check reads at the pull request* | the framer, if the orchestrator judges the shape worth a limit sentence |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_body_probe.py -p no:xdist -q` in `<scratchpad>/1452-r1/clone` at `89de04fa`: the `bodied` repository with the guarantee's base written as the fork point's SHA, one commit on `main` after the seal, HEAD detached at `main` merged with `feature/g`, the payload holding the body composed at the branch head | exit 1 from the check, one line refusing the mark run as "which the records do not give", no notice, and no refusal from the guarantee arm. The probe ran twice: the first run printed through `capsys` and showed nothing, so its assertion message was changed to carry the output. The file was then deleted, and the clone's `git status --short` was empty |
| `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/text/test_ci_gives_the_checks_what_they_need.py -q` in the clone | exit 0, 300 passed |
