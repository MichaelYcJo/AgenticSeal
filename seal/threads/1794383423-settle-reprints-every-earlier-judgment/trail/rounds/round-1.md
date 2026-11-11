# Review round 1: 1794383423-settle-reprints-every-earlier-judgment

```seal
target: 452d08a3d against origin/release/v0.37.4
```

This round read the branch against `origin/release/v0.37.4` (`eec0bd040`),
which is also the merge base after `29b11964a`. The diff outside the work
item's records is `skills/settle/scripts/settle.py`,
`skills/settle/SKILL.md` and `tests/skills/test_settle.py`. The round read
`routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`,
`gaps.md`, `changelog.md`, `pr.md` and both phase records whole at
`452d08a3d`. No `pr.<lang>.md` stands, and none is owed, because
`Commit and pull request language` is English. No earlier round exists, so
nothing was carried from one. The phase records' red runs and mutation
tables are carried as claims and were not re-run. The round re-ran S7 and
the two narrow modules itself (`## Probes`).

The `## Not verified` row of phase 1 in `gaps.md` asked this round to run
`for-each-ref` over a nested tag on an older git. The round ran it, and the
answer is finding 1.

## Findings

### 1. On a git before 2.44, a commit that only a nested version tag holds is labelled with a higher tag, where `git tag --contains` named the nested one

```seal
severity: must
location: `skills/settle/scripts/settle.py:541-569`
evidence: executed `python3 -I test_tmp_nested_tag.py <clone> <dir>` once with git 2.50.1 and once with `/Library/Developer/CommandLineTools/usr/bin` (git 2.39.3) first on PATH
```

Why it matters: design *Scope* item 5 says that what `version` returned to
its callers does not change, and that "the lowest tag stays the lowest by
number". `frame/plan.md` *Technical context* says "The tag read stays
exact". `versions` takes a tag's commit from `%(*objecttype)` and
`%(*objectname)` (`settle.py:557`, `:566`). On git 2.50.1 those fields peel a
tag of a tag down to the commit. On git 2.39.3 they peel one level only. The
probe built one commit tagged by a nested annotated `v0.1.0` (a tag of the
tag `inner`) and a later commit tagged `v0.2.0`. It then printed
`for-each-ref` and `git tag --contains` for the first commit, and the label
`versions` gives it:

| git | `%(*objecttype)` of `v0.1.0` | `git tag --contains` | `versions()[first]` |
|---|---|---|---|
| 2.50.1 | `commit` | `v0.1.0`, `v0.2.0` | `v0.1.0` |
| 2.39.3 | `tag` | `v0.1.0`, `v0.2.0` | `v0.2.0` |

On 2.39.3, `tip` is None for the nested tag, so `v0.1.0` labels nothing and
the commit takes the next tag up. The reader this replaced asked
`git tag --contains`, which peels fully on both gits, and would have
returned `v0.1.0`. Two callers act on the wrong tag:

- The earlier section prints "released in v0.2.0" for a plan v0.1.0
  shipped.
- `notes` (`settle.py:736-741`) checks the published note of v0.2.0, not of
  v0.1.0, for the work item's entry. So `--apply` keeps a directory whose
  note carries it, or names "no tag holds" where no higher tag stands.

The repository names no git floor; a `git grep` over `README.md`, `docs`,
`lib`, `bin`, `hooks`, `.github` and `CONTRIBUTING.md` found none (executed).
macOS's Command Line Tools ship git 2.39.3 on this machine. A nested version
tag is rare, but the change makes the fact depend on the git version where
it did not before.

The fix peels a nested tag with `^{}`, which peels fully on every git. It
adds a third call only where a nested version tag stands, so the call count
still does not grow with the plans read:

```python
    tips, nested = [], []
    # exempt from splitlines: git output
    for line in listed.splitlines():
        kind, oid, peeled_kind, peeled, name = line.split(" ", 4)
        matched = VERSION_RE.match(name)
        if not matched:
            continue
        number = tuple(int(n) for n in matched.group(1).split("."))
        if kind == "commit":
            tips.append((number, name, oid))
        elif peeled_kind == "commit":
            tips.append((number, name, peeled))
        elif peeled_kind == "tag":
            # A git before 2.44 peels `%(*...)` one level only, so a tag of
            # a tag names the inner tag here; `^{}` peels it whole on every git.
            nested.append((number, name, peeled))
    if nested:
        answered = decoded(
            git_run(
                root,
                "cat-file",
                "--batch-check=%(objecttype) %(objectname)",
                given="".join(f"{oid}^{{}}\n" for *_held, oid in nested).encode(),
            )
        )
        # exempt from splitlines: git output
        for (number, name, _oid), line in zip(
            nested, answered.splitlines(), strict=True
        ):
            kind, _, tip = line.partition(" ")
            if kind == "commit":
                tips.append((number, name, tip))
```

The snippet does not reach every statement of the fact. The fix pass also
owes these:

- the docstring of `versions` (`settle.py:547-552`), which says "Two calls";
- design *Scope* item 4 (`frame/design.md:63-66`), which allows two calls
  for the tag read;
- the last sentence of the second item of `changelog.md:4`, which says
  "two git calls per run";
- the phase 1 row of `gaps.md` *Not verified*, which this answers;
- a case in `Test_versions` with a nested version tag. On git 2.44 or later
  that case passes without the fix, so it can be seen red only with a git
  before 2.44 first on PATH, such as the Command Line Tools git above.

```seal
verdict: fixed 0a354b5a7
answer: The finding holds: on the Command Line Tools git 2.39.3 the nested-tag case failed with `'v0.2.0' == 'v0.1.0'` before the fix. `versions` now peels every `refs/tags/<name>^{}` in one `cat-file --batch-check`, so every git runs the same path and the case is green on 2.39.3 and 2.50.1. This takes the place of the record's branch for a git before 2.44, which no case run on a current git could reach. The tag read is three calls, one fixed call more per run, and the count still does not grow with the plans read (S4). The docstring, `changelog.md` and the `gaps.md` row were rewritten at `0a354b5a7` and `87387b856`; the frame's two-call sentence goes to the framer.
```

### 2. A removed plan whose path holds a newline shifts the batch's answers, so a later plan's rows are dropped and it is named with another name's answer

```seal
severity: should
location: `skills/settle/scripts/settle.py:1321-1335`, `skills/settle/scripts/settle.py:591-597`, `seal/threads/1794383423-settle-reprints-every-earlier-judgment/frame/plan.md:39-41`
evidence: executed `python3 -I test_tmp_newline_id.py <clone> <dir>` against the target's and the base's `settle.py`
```

Why it matters: `blobs` sends each name to `git cat-file --batch` on its own
line (`settle.py:600`). Its docstring states "a name holds no newline" as a
precondition (`:596`). `frame/plan.md:39-41` claims "A work item id holds no
newline", and nothing on the path enforces that. The deletion log reads
paths with `-z`, so a path committed with a newline in its work item
directory reaches `blobs` whole. Git then reads it as two names, and every
answer after it shifts by one. The probe committed two plans in one commit,
`seal/threads/1700000001-odd<newline>name/frame/plan.md` and
`seal/threads/1700000002-plain/frame/plan.md`, and removed both in the next:

- At the base, `earlier_judgments` read both plans and printed both rows,
  each released in v0.1.0.
- At the target, it printed no row. It named the plain plan, which git
  holds, as not read with the answer "`name/frame/plan.md missing`". That
  answer belongs to the second half of the other path.

This is a new failure path that the change introduced. The plain plan's
judgments vanish from the section that exists to show them, and the line
naming it is wrong. A commit that reaches `--released-at` can plant such a
path.

The fix names such a plan as not read before the batch, in
`earlier_judgments` after the window:

```python
    # `git cat-file --batch` reads one name per line (`blobs`), so a path
    # holding a newline would shift the answer of every plan after it.
    split = [
        (f"{work_item_id}  {short}^:{path}", NO_ONE_LINE)
        for (_full, short, _subject), work_item_id, path in deleted
        if "\n" in path
    ]
    deleted = [d for d in deleted if "\n" not in d[2]]
    if not deleted:
        return [], split, older
    try:
        texts = blobs(root, [f"{full}^:{path}" for (full, _s, _t), _i, path in deleted])
        added = adding_commits(root, ref, specs)
        labels = versions(root)
    except RuntimeError as failed:
        return [], [("", str(failed))], older
    groups, unread = {}, split
```

```python
# A removed plan whose path holds a newline, which `blobs` cannot ask for.
NO_ONE_LINE = (
    "its path holds a newline, which `git cat-file --batch` reads as two "
    "names, so none of its rows were read"
)
```

The fix pass also owes a case in `tests/skills/test_settle.py` beside
`test_a_plan_git_holds_no_text_for_is_named_and_none_of_its_rows_printed`.
The case commits the two paths as the probe does, through
`git update-index --cacheinfo`, and asserts that the plain plan's row is
printed. It also owes the plan's sentence at `frame/plan.md:40`, and a
clause in the bullet *The judgments earlier settles removed* of
`skills/settle/SKILL.md`, which lists what is named as not read.

```seal
verdict: fixed 0a354b5a7
answer: The finding holds: the `[beside]` case named the plain plan with `name/frame/plan.md missing` before the fix. The record's fix was applied after reading it: `NO_ONE_LINE` names a plan whose path holds a newline before `blobs` is called, and that plan is never asked for (`0a354b5a7`). The `[alone]` parameter, added at `c719f1de8`, holds the branch where it is the only plan left. The docstrings and the skill bullet say the same; the frame's sentence that an id holds no newline goes to the framer.
```

### 3. Three frame statements left by the fold at `e72cbe025` are contradicted by the target

```seal
severity: should
location: `seal/threads/1794383423-settle-reprints-every-earlier-judgment/frame/design.md:124`, `seal/threads/1794383423-settle-reprints-every-earlier-judgment/frame/plan.md:79`, `seal/threads/1794383423-settle-reprints-every-earlier-judgment/frame/plan.md:98`
evidence: executed `grep -n -o ':[0-9]\{2,4\}\(-[0-9]\{2,4\}\)\?'` over `frame/*.md` and `grep -n` for each case at `452d08a3d`, and an `ast` listing of the top-level units `settle.py` adds, removes and changes between `eec0bd040` and `452d08a3d`
```

Why it matters: the claim in `frame/plan.md:112` is that the fold at
`e72cbe025` carried "the moved test coordinates". The grep listed every line
coordinate in the two frame files. Those in *Grounding* and *Technical
context* are dated to `18a7e18fb` and state that commit. Of the rest,
`design.md:72` and `:93` and `plan.md:80` carry their position after phase
2, and `plan.md:97` names another file and still holds. Two rows carry none:

- S5 (`design.md:124`) places the #1281 cases at
  `tests/skills/test_settle.py:1371-1578`, with `:1541` and `:1580`. At the
  target the cases stand at `:1423-1652`. The `adding_commits` patch is at
  `:1615`, and the git-failure case's `def` is at `:1663`. Line `:1580` is
  now inside `test_names_a_plan_no_tag_holds_and_a_removal_no_number_names`.
- Phase row 1 (`plan.md:79`) gives the same three coordinates.

The sealer and the settle open these coordinates to check S5. Phase row 2,
one line below, shows the form the fold chose.

The third statement is the #1482 row of *Overlap with the release*
(`plan.md:98`). It lists the units this work adds to `settle.py`, and the
`ast` listing finds one more it does not name: `NO_PLAN_TEXT`
(`settle.py:966`). The other adds, the eight changed units and the removed
`version` match the row.

```markdown
| S5 | Given the #1281 cases at `tests/skills/test_settle.py:1371-1578` (`:1423-1652` after phase 2), when they run against the batched reads, then each passes. Each history there removes plans in at most two removing commits, so each pins the batched output as it pinned today's. `:1580` (`:1663` after phase 2) fails each batched call in turn and asserts the one `not read:` line with what git said, and exit 0. | the cases as they stand, with `:1541` (`:1615` after phase 2) and `:1580` changed to replace the batched readers |
```

In phase row 1 of `plan.md:79`, the fix pass writes the same three
positions after phase 2 beside `:1371-1578`, `:1541` and `:1580`. In
`plan.md:98`, it writes `NO_PLAN_TEXT` among the adds, before
`EARLIER_WITH_APPLY`. Findings 1 and 2 each add a unit to `settle.py`. If
the fix pass adds one, it owes that unit's name in this row as well.

```seal
verdict: fixed 8c1eb676f
answer: The finding holds. The fold at `8c1eb676f` gives S5 (`frame/design.md`) and phase row 1 (`frame/plan.md`) their positions after phase 2 beside the base ones: `:1423-1651`, `:1663` and `:1615`. The range ends at `:1651`, the case's last line at `c89db956f`, where `:1652` is blank. The #1482 row of *Overlap with the release* now names `NO_PLAN_TEXT`, and also `NO_ONE_LINE`, which fix pass 1 added. An `ast` comparison of `settle.py` at `18a7e18fb` and `508d093ad` finds no other unit the row leaves out.
```

## Confirmations

What matched: S7 at the target. `test_tmp_s7.py` ran `settle.main` in a
`git clone --no-local` with `--released-at 18a7e18fb` (executed). The dry
run made 24 git calls in 0.53 s and printed 108,893 B, with a 47,844 B
section. The section's removing commits were `8657297d (#1495)` and
`e5370691 (#1466)`, and its last line read "8 older commits removed plans
this section did not read; `seal settle --all-earlier` reads them".
`--all-earlier` made 24 calls in 0.69 s and printed 308,350 B, with a
247,301 B section. That section named the seven removing commits #1214,
#1269, #1310, #1400, #1432, #1466 and #1495, and printed no count line.
These are the figures `trail/phases/phase-2.md:135-148` and `changelog.md`
state.

What matched: the window of design *Scope* item 1 and the count of item 2
(`settle.py:1321-1328`, read). Removing commits are listed once each in log
order from `deleted`, after both of its filters. The count is
`len(removing) - EARLIER_WINDOW`, and `report` prints the section where
`groups or unread or older` (`:1860`). The count is printed last after a
blank line (`:1872-1873`).

What matched: *Scope* item 3. `main` refuses `--all-earlier` beside `--apply`
and beside `--draft` with exit 2, each after the three refusals that stood
(`settle.py:2108-2113`, read). `--from` reaches `survey` with the flag
(`:2166`, read).

What matched: *Scope* items 4 and 5 (read). `blobs`, `adding_commits` and
`versions` are each one batched read. `adding_commit` is one call of
`adding_commits` (`settle.py:399-406`), and `version` has no caller left.
`adding_commits` keys by the path git prints, which is relative to the
top level. Both callers ask with such a path: `notes` builds
`{specs}/<id>/changelog.md` (`:728`), and `publish_release_note.py:261`
takes its paths from git's own output. `main` resolves the root to the top
level (`settle.py:2123`). `decoded` repeats the decoding that text-mode
`subprocess.run` applies: UTF-8 with replacement, then `\r\n` and `\r` read
as a newline.

What matched: the lowest-first walk in `versions` (`settle.py:579-587`,
read). A walk stops only at a commit a lower tag's walk labelled. That
walk ran whole before this one began, so it also labelled every ancestor of
that commit. So each commit gets the lowest tag whose history holds it.

What matched: *Scope* item 7 (read). The command table, the bullet, step 5,
the module docstring, `EARLIER_HEADING`, the argument's help and the exit-2
list each state the bound and the flag. The three `from` passages of
`## Rule changes` drew no line from `chain_check.py --worktree` (executed).
That run printed no notice at a line of `frame/design.md`.

What matched: `pr.md`. Each of its three quotes stands word for word at the
row it names, `frame/plan.md:64`, `:68` and `:113` (read). Each figure in
`changelog.md` stands in the record it comes from: 247,730 B and 308,261 B
in design G8, 8.40 s and 422 calls in `phase-1.md:19-22`, and 47,844 B, 8
older commits, 24 calls, 0.91 s and 1.04 s in `phase-2.md:135-142` (read).

What matched: each new case against its group (read). No `seal layout
--pairs` pair names these cases. Each covers a fact no case beside it
holds:

- `Test_versions` and `Test_blobs` are the unit cases of two new functions.
- The S6 case and the failing-batch case are end-to-end cases on paths the
  unit cases do not reach.
- `test_a_batched_read_that_fails_keeps_the_line_of_older_commits` holds the
  count. The parametrized git-failure case does not, because its history
  has one removing commit.

The two narrow modules passed at the target, 229 cases (executed).

`EARLIER_HEADING` reads more loosely than the bullet of `skills/settle/SKILL.md`
in one edge, and the round opens no finding for it. The heading says "one
of the two newest commits on `--released-at` that deleted a plan". The
bullet defines a removing commit after the rule that reads each plan once
and after the exclusion of a standing directory. In
`test_a_plan_is_read_once_at_its_newest_deletion`, the middle commit deleted
a plan and is not counted. The settling session's act does not change there,
because the count line still sends it to `--all-earlier`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the target, labelled `unverified` by both phase records | `seal/config.json` `Broad gate` | the orchestrator, by the broad run |
| Whether the settling session reads the bounded section and runs `--all-earlier` where a kind may predate the window (design S8) | `skills/settle/SKILL.md` step 5 | the owner, at the next settle |
| The cost of `versions` on a history much larger than this repository's. `rev-list --parents` of every version tag lists every commit those tags hold, and `notes` now pays it once per `--apply`. Only this repository was measured | `skills/settle/scripts/settle.py:572-587` | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py tests/github/test_publish_release_note.py -q`, in the clone at `452d08a3d` | 229 passed, exit 0 |
| `python3 -I test_tmp_s7.py <clone>`, `settle.main` with `--released-at 18a7e18fb`, without and with `--all-earlier` | 24 and 24 git calls; 0.53 s and 0.69 s; output 108,893 B and 308,350 B; section 47,844 B and 247,301 B; count line "8 older commits" only in the dry run |
| `python3 -I test_tmp_nested_tag.py <clone> <dir>`, git 2.50.1 | `%(*objecttype)` of the nested `v0.1.0` is `commit`; `versions()` labels the first commit `v0.1.0` |
| the same with git 2.39.3 first on PATH | `%(*objecttype)` is `tag`; `git tag --contains` lists `v0.1.0` and `v0.2.0`; `versions()` labels the first commit `v0.2.0` |
| `python3 -I test_tmp_newline_id.py <clone> <dir>`, against the target's `settle.py` | no row printed; the plain plan named not read with the answer `name/frame/plan.md missing` |
| the same against the base's `settle.py`, in a second clone at `eec0bd040` | both plans' rows printed, each released in v0.1.0 |
| `chain_check.py --baseline origin/release/v0.37.4 --root <worktree> --worktree`, before the record was written | no line at `frame/design.md`; the missing round, gate and guarantee records named |
