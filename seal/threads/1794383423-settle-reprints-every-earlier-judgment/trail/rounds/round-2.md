# Review round 2: 1794383423-settle-reprints-every-earlier-judgment

```seal
target: 94d4bbae7, fixes 4fab90b87..94d4bbae7
```

This is a verifying round. It reviewed as code the fix diff
`4fab90b87..94d4bbae7`:

- `0a354b5a7` and `c719f1de8`: the code and the cases.
- `87387b856`: `changelog.md` and `gaps.md`.
- `51b5d5ab4`: reflows.
- `508d093ad` and `94d4bbae7`: the close blocks.
- `8c1eb676f`: the framer's fold.

The round read the work item's records at `94d4bbae7`. Round 1 read each
of them whole at `452d08a3d`. This round read whole the diff of each since
then, and searched every record and `skills/settle/` for the statements the
fixes made stale (executed: `grep -n -i` for "two calls", "24 git",
"two git calls" and "holds no newline"). It found none standing outside a
dated section or a phase record.

Round 1's probes were re-run from its `## Probes` rows, unchanged, against
a `git clone --no-local` at `94d4bbae7`. Git 2.39.3 was reached through a
scratch directory holding only a link to
`/Library/Developer/CommandLineTools/usr/bin/git`, so the interpreter on
PATH stayed the same.

## Findings

### 1. Round 1's close of finding 2 names `fixed c719f1de8`, a commit that touches none of the finding's locations, so the chain check refuses it

```seal
severity: must
location: `seal/threads/1794383423-settle-reprints-every-earlier-judgment/trail/rounds/round-1.md:192`
evidence: executed `skills/code-review/scripts/chain_check.py --baseline origin/release/v0.37.4 --root <worktree> --worktree`, the installed copy and the tree's
regression: round-1#2
```

Why it matters: the close block that fix pass 1 appended at `508d093ad`
reads `verdict: fixed c719f1de8`. Finding 2's `location:` names
`skills/settle/scripts/settle.py` and `frame/plan.md`.
`git show --stat c719f1de8` shows that commit changed
`tests/skills/test_settle.py` alone; it added the `[alone]` parameter. The
code fix is `0a354b5a7`, which changed `settle.py`, `skills/settle/SKILL.md`
and the test module. Both copies of the chain check refuse the line
(executed):

> round-1.md:192 ... reads `verdict: fixed c719f1de8`, and `c719f1de8`
> touches no path its `location:` names (...): it changed
> `tests/skills/test_settle.py`. A fix that went elsewhere names that path
> on a `location:` line of its close block

The invariant *No fix that no round reads* holds through this line. A ready
pull request fails on it, and the sealer withholds on it. The code fix
itself holds; `confirms: round-1#2` below says so. The defect is in the
close block alone.

This defect is in the close block, a unit the fix pass's own commit added.
The frame gives no row for close blocks. The fix pass named the commit that
added the last case, not the commit that made the fix the finding asks
for.

The fix names the commit that changed the finding's location. The answer
line stays as written, since it already names both commits:

```markdown
verdict: fixed 0a354b5a7
```

The fix touches the work item's records alone. So the sealer can read it,
as the invariant's second row allows, or a round after it can.

```seal
verdict: fixed 05394cbca
answer: The finding holds: `c719f1de8` changed `tests/skills/test_settle.py` alone, and the code fix of round 1's finding 2 is `0a354b5a7`. `05394cbca` changes round 1's close of finding 2 to `verdict: fixed 0a354b5a7` and leaves its answer line as it was. The fix touches the work item's records alone, for a finding located in them alone.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `versions` now lists the version tags by name and peels each
`refs/tags/<name>^{}` in one `git cat-file --batch-check`
(`skills/settle/scripts/settle.py:543-602`). `^{}` peels a tag of a tag
whole on every git. The fix does not take the round 1 record's branch for a
git before 2.44; it puts every git on one path. The close block gives that
as its grounds, and the frame now states it at design *Scope* item 4. Two
probes re-ran (executed):

- Round 1's nested-tag probe: on git 2.39.3, `for-each-ref` still prints
  `tag` for the nested `v0.1.0`, and `versions()` now labels the commit
  `v0.1.0`, as `git tag --contains` does. On git 2.50.1 it labels it
  `v0.1.0` too.
- `Test_versions::test_accepts_a_version_tag_of_a_tag_at_the_commit_it_peels_to`
  passed with git 2.39.3 first on PATH. With the code at `452d08a3d`, round
  1's probe gave that commit `v0.2.0` on 2.39.3, which is the value the
  case refuses. Its red is carried from that run and from the close block,
  and was not shown again.

Only names `VERSION_RE` accepts reach `cat-file`, so no tag name can break
a line. An answer that is not `commit`, such as a tree, or a `missing`
line, labels nothing. The 2.39.3 run of S7 printed the same 108,893 B and
308,350 B as the 2.50.1 run.

```seal
confirms: round-1#2
```
What holds: `earlier_judgments` names each plan whose path holds a newline
with `NO_ONE_LINE` before `blobs` is called, and asks git for the other
plans alone (`settle.py:1348-1366`). Round 1's newline probe re-ran
(executed). The plain plan's row is now printed, released in v0.1.0. The
odd plan is named as not read with "its path holds a newline, which
`git cat-file --batch` reads as two names, so none of its rows were read".
The new case
`test_a_removed_plan_whose_path_holds_a_newline_is_named_and_the_rest_read`
holds both branches. `[beside]` holds the plain plan read beside the odd
one, and `[alone]` holds the early return where no other plan is left.
Each passed on both gits (executed). The case covers a fact its group does
not. The S6 case holds a plan git answers `missing` for, and this one holds
a plan that is never asked for. The skill's bullet, the two docstrings,
design *Scope* item 6 and `frame/plan.md:39-43` say the same.

```seal
confirms: round-1#3
```
What holds: S5 (`frame/design.md:128`) and phase row 1 (`frame/plan.md:81`)
now carry `:1423-1651`, `:1615` and `:1663` "after phase 2" beside the base
coordinates, in the form `design.md:74` and `:97` use. The close block says
the range ends at `:1651`, the case's last line at `c89db956f`. That
matches round 1's reading, where `:1652` was blank (read). These are
coordinates dated to phase 2. The fix diff since moved the git-failure
case's `def` to `:1667`, and the dating covers that. The #1482 row
(`frame/plan.md:100`) now names `NO_PLAN_TEXT` and `NO_ONE_LINE`. Round 1's
`ast` listing, together with the one unit `0a354b5a7` adds, leaves no unit
out (read).

What matched: the new failure path of the peel is named like the others.
The git-failure case gained a `the tags' peel` parameter that fails the
`cat-file --batch-check` (`tests/skills/test_settle.py:1660-1663`), and the
docstring counts six calls. The narrow modules
`tests/skills/test_settle.py` and `tests/github/test_publish_release_note.py`
passed at the target, 233 cases (executed). So did
`tests/behaviour/test_docs_line_wrap.py`, 51 cases, and `uvx ruff check` and
`uvx ruff format --check` on the two changed Python files (executed).

What matched: `changelog.md` and the A1 row of `frame/plan.md:66` say the
dry run makes 25 git calls with or without `--all-earlier`. S7 re-ran at the
target (executed). Both runs made 25 calls. The dry run printed 108,893 B
with a 47,844 B section and the line of 8 older commits. `--all-earlier`
printed 308,350 B with a 247,301 B section. The dry run took 0.53 s on
2.50.1 and 0.34 s on 2.39.3, under the 2 s of design S7. The changelog's
0.56 s and 0.53 s are the fix pass's own runs. This round did not reproduce
those two figures, and its own times stand beside them. The `gaps.md` row
of phase 1 is closed in place, with the word `closed` and the answer.
`pr.md` is unchanged, and its first quote still stands word for word in the
A1 row, whose new sentences follow it.

One thing the fix leaves in an edge, with no finding opened for it. Where a
batched read fails after the split (`settle.py:1364`), the section returns
only the failure line, so a plan whose path holds a newline is not named.
Design *Scope* item 6 says such a plan is named "before the batch". The
settling session still reads that nothing past the deletions was read,
from the one `not read:` line, so what it does next does not change. The
intersection needs a path with a newline and a failing git in one run.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the target, labelled `unverified` by both phase records and the fix pass | `seal/config.json` `Broad gate` | the orchestrator, by the broad run, once finding 1 is closed; the sealer is spawned after it |
| Whether the settling session reads the bounded section and runs `--all-earlier` where a kind may predate the window (design S8) | `skills/settle/SKILL.md` step 5 | the owner, at the next settle |
| The cost of `versions` on a history much larger than this repository's, carried from round 1 | `skills/settle/scripts/settle.py:543-602` | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py tests/github/test_publish_release_note.py -q`, in the clone at `94d4bbae7`, git 2.50.1 | 233 passed, exit 0 |
| `bin/test tests/skills/test_settle.py -q -k "Test_versions or newline or cannot_read_an_earlier or Test_blobs or Test_adding_commit or git_calls"`, git 2.39.3 first on PATH | 16 passed, exit 0 |
| `bin/test tests/behaviour/test_docs_line_wrap.py -q` | 51 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` on `settle.py` and `test_settle.py` | exit 0 and exit 0 |
| round 1's `test_tmp_nested_tag.py <clone> <dir>`, git 2.39.3 | `%(*objecttype)` of the nested `v0.1.0` is `tag`; `versions()` labels the first commit `v0.1.0` |
| the same, git 2.50.1 | `versions()` labels the first commit `v0.1.0` |
| round 1's `test_tmp_newline_id.py <clone> <dir>` | the plain plan's row printed, released in v0.1.0; the odd plan named with `NO_ONE_LINE` |
| round 1's `test_tmp_s7.py <clone>`, git 2.50.1 | 25 and 25 git calls; 0.53 s and 0.70 s; output 108,893 B and 308,350 B; section 47,844 B and 247,301 B |
| the same, git 2.39.3 | 25 and 25 git calls; 0.34 s and 0.53 s; the same bytes |
| `chain_check.py --baseline origin/release/v0.37.4 --root <worktree> --worktree`, the installed copy and the tree's | each refused `round-1.md:192` (finding 1) and named the gate and guarantee records not yet written |
