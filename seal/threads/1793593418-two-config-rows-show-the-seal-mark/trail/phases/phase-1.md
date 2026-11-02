# Phase 1: 1793593418-two-config-rows-show-the-seal-mark

## What this phase found

### The frame, checked before the build

The frame holds for phase 1, with one exception below. Every coordinate
`frame/design.md` and `frame/plan.md` give for this phase was opened at
`04bb49c1d` and stood as stated (read). `pr_body.py#read_item` is at
`:248-267` and reads no `guarantee.md`. `#_composed` is at `:436-483`, and
its `below` list opens at `:454`. `CHAIN` and `ROUTING` load at `:102-104`.
`chain_check.py#CLOSING_RECORDS` is at `:163`, `#follows` at `:955-986` and
`#guarantee` at `:1646-1692`. The verdict block's `target:` groups `commit`
and `base` are at `hooks/lib/fields.py:207`. `.claude-plugin/plugin.json`
carries `repository`, `version` and `icon`.

The exception is in what *sealed at HEAD* rests on. `follows` lists the
later commits with `git rev-list ... ^<base>`. Where git cannot resolve the
base, that command exits non-zero, `chain_check.py#git` answers None, the
loop reads no commit, and `follows` answers None, which reads as HEAD. A
guarantee naming such a base would then carry the mark over a repair
nobody sealed, which is the case S3 exists to refuse. In the pull
request's check this does not arise, because CI hands `follows` a base it
has fetched. `pr-body` takes the base from the guarantee's own `target:`
line instead, and a local clone may not hold it.

### Decision: a base that does not resolve writes no mark, and is named

`pr_body.py#_seal_at_head` asks `git rev-parse --verify --quiet
<base>^{commit}` before `follows`. Where it fails, no mark is written, and
`seal pr-body` prints one line naming the base. This departs from
`frame/design.md` *Scope* item 2, which defines sealed at HEAD as `follows`
answering None and says a guarantee that is not sealed at HEAD prints
nothing. The grounds are the design's own *Grounding* row on *The stamp*:
the mark means what the stamp means, so it must not stand over a stale
seal. The line is printed because neither the sealer nor the pull request's
check names a base this clone lacks. Judged against `frame/design.md`
*Scope* item 2 and `docs/the-review-record.md` *The stamp*.

### Decisions settled while writing the code

- **Where the row and the root are read.** The repository is the one
  `seal pr-body` runs in, `optin.py#repo_root` of the working directory,
  and its `seal/` root is `optin.py#home_at` of that root, as
  `frame/plan.md` *Technical context* states for `follows`. The row is read
  through `hooks/lib/config.py#declared_value`, which is `config_text` and
  then `config_value`, the one reader the design names. The guarantee is
  read from the directory the command is given, beside the other records.
  Judged against `frame/plan.md` *Technical context*.
- **When the line about the mark is printed.** It is printed on the line
  before `wrote:` or `matches:`, and only on those exit-0 paths. On exit 1
  the `refused:` lines stand first as they did, and
  `tests/skills/test_pr_body.py#Test_main` reads them so. Judged against
  `frame/design.md` *Data & interfaces*, "printed beside `wrote:` or
  `matches:`".
- **The mark is not one of `FIXED`.** Every line of `FIXED` is a template
  filled with a work item's name or a record's path, and the module's own
  test fills each that way. The mark is filled from the manifest, so it
  stands as `MARK` beside them, and the comment over `FIXED` says so.
  Judged against `frame/design.md` *Data & interfaces*, the mark line.
- **`seal_mark` takes the manifest's path, defaulting to the plugin's
  own.** The default is read when the function runs, so a case can point
  the command at a copy that lacks a field (S5). The plugin's own
  `plugin.json` is read by one case and edited by none.
- **The template's section holds one row in this phase.**
  `templates/setup/config.md` gains `## The seal mark`, written for a row
  per surface, with `Pull request seal mark` alone. Phase 2 adds
  `Release note seal mark` to the same section, with the sentence that the
  plugin's release workflow is this repository's alone. The row is not in
  the template's opening table, the same as the fold's values, because an
  absent row is the default. Judged against `docs/one-root-by-lifetime.md`
  *What the repository decides for itself, and how it is read*.

### The cases, and how each was shown red

`tests/skills/test_pr_body.py` gains `Test_seal_mark` and two cases in
`Test_main`. Twenty new cases ran red against the code at `04bb49c1d`, with
the cases in the working tree and `pr_body.py` not yet edited (executed,
exit 1). Nineteen failed on `seal_mark` or `MANIFEST` being absent. The
`Test_main` case for S4 failed on its first line, which read `wrote:` where
the case asks for the line naming the row. The module then ran green, 51
passed (executed, exit 0).

`tests/text/test_the_settings_have_a_front_door.py#ROWS` gained
`Pull request seal mark` before the documentation landed and failed with
"the skill does not name `Pull request seal mark`" (executed, exit 1). It
passed in the phase-boundary run below.

### Mutations

`seal mutate` ran after the build commit `72f39f9b3`, over
`skills/code-review/scripts/pr_body.py`, with `bin/test
tests/skills/test_pr_body.py -q -p no:xdist -k <cases>`. Each run restored
the file from its held bytes, and `git status` showed it unchanged after
(executed). A `red` run is one where the cases exited 1 and `seal mutate`
exited 0.

| Mutant | Cases run | Result |
|---|---|---|
| S3: `return behind is None, None` read as `return True, None`, the `follows` condition alone removed | `-k later_commit_follows` | red: the case read the mark where it asks for `(None, None)` |
| S4: `value != MARK_ON` read as `value.casefold() != MARK_ON` | `-k 'row_other_than_yes and Yes'` | red: the `Yes` case read the mark, and the `Test_main` case read `wrote:` where it asks for the line naming the row |
| the unresolved base's return replaced by `pass` | the batch below | red |
| the `sealed` comparison read as `if False:` | the batch | red |
| the refusal check dropped, `if not found.blocks:` alone | the batch | survived |
| the manifest's field loop over no field | the batch | red |
| `_composed`'s `if mark:` read as `if False:` | the batch | red |
| a refused row returning `(None, None)` | the batch | red |
| `if not value:` read as `if value is None:` | the batch | red |
| the `./` strip skipped | the batch | red |
| `html.escape(src)` read as `src.upper()` | the batch | red |

The batch ran in one command over `-k 'seal_mark or mark_under or
mark_on'`, its baseline green, and `seal mutate` exited 1 for the
survivor (executed). The
survivor showed that the S2 case for a refused block was caught by
`not found.blocks` alone, since `hooks/lib/fields.py` keeps a refused block
out of `blocks`. A guarantee with a sealed block and a refused block after
it would have carried the mark. S2 gained that case, committed as
`a566ad6b2`, and the mutant ran red against it with `-k not_sealed`
(executed, exit 0 from `seal mutate`).

### The phase-boundary run

One command, under `bash` (executed, exit 0):
`bin/test <54 modules> -q && bin/seal layout --check tests`. The 54 modules
are every test module under `tests/` whose text names `pr_body`,
`orchestration.md`, the config template, the config skill or
`seal/config.md`, with `tests/test_censuses.py`, `tests/hooks/test_launch.py`
and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` added. The
suite part read 3701 passed and 10 skipped. The layout check read 149
files and refused none. `bin/seal layout --pairs tests/skills/test_pr_body.py`
named 0 pairs (executed, exit 0). `uvx ruff check` and
`uvx ruff format --check` over the three changed Python files exited 0
(executed).

The design's `## Rule changes` was read by the tree's
`skills/settle/scripts/rule_changes.py#parse` with `docs` as the policy
root: three operations, no error and no unread line (executed). Placing
them with `apply_op` is left to `seal chain-check` at the pull request.

### For phase 2

- The template's `## The seal mark` section and its value table are
  written for both rows. Its third value row says the command that writes
  the surface names a value other than `yes`, which for the release note
  is the `seal` job's `::warning::` line.
- `tests/skills/test_pr_body.py#sealed_item` builds a sealed work item in a
  git repository. The release half reads no guarantee, so it needs none of
  it.
