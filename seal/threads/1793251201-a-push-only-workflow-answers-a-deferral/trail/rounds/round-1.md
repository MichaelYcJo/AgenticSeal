# Review round 1: 1793251201-a-push-only-workflow-answers-a-deferral

target: cbbbe744 against origin/release/v0.24.2

This is round 1, so no earlier round handed over a coordinate and nothing
here is carried. Every fact below was opened or run this round in a
`git clone --no-local` of the branch at `cbbbe744`.

## Findings

### 1. Two valid trigger spellings the base read as answering now read as unread and refuse

severity: should
location: `skills/verify/scripts/deferral_check.py:166-167`, `skills/verify/scripts/deferral_check.py:139-140`, `tests/skills/test_deferral_check.py:153-173`
evidence: executed `python3 -I test_tmp_shapes.py`, `uv run --no-project --with pyyaml python3 -c 'import yaml; yaml.safe_load(...)'`

The change adds a new failure path, and it refuses workflows that do run on
pull requests. Two such spellings are a flow list with a trailing comma and
an event name on the line below `on:`. A YAML parser reads
`on: [push, pull_request, ]` as `['push', 'pull_request']`,
`on: [pull_request,]` as `['pull_request']`, and `on:` followed by
`  pull_request` as the scalar `pull_request`. The base script printed
`answers ... (on pull_request, push)`, `answers ... (on pull_request)` and
`answers ... (on pull_request)` for them, each at exit 0. The branch prints
`unread ... (trigger unread, not counted)` for all three, at exit 1.

The trailing comma regressed because the rewrite dropped the base's
`if e.strip()` filter (base `deferral_check.py:105`). Now
`value[1:-1].split(",")` at `:167` yields an empty last name, which fails
`EVENT_NAME`. The scalar on the next line regressed because the base's key
pattern took the colon as optional (base `:117`). The `else: return []` arm
of `block_entries` at `:139-140` now refuses any line at the block's indent
that has no colon.

`plan.md` accepts a false refusal for a spelling nobody foresaw, provided
the cause is printed. These two spellings were not unforeseen: the base read
both of them, and the frame's Scope item 1 does not say to drop them. The
person is told the trigger could not be read when it could, and the deferral
is refused where it held before. `KNOWN_LIMITS` names a flow mapping and a
flow list across lines as unread, and names neither of these.

The trailing comma takes one line to read. The scalar on the next line can
be read or named as a limit. Either way, the S4 case gains a parameter, or
S8 gains an assertion, that is seen red first.

```python
        elif value.startswith("[") and value.endswith("]"):
            names = value[1:-1].split(",")
            # YAML allows one trailing comma in a flow list: `[push, pull_request, ]`.
            if len(names) > 1 and not names[-1].strip():
                names.pop()
```

```python
KNOWN_LIMITS = (
    "reads command text, not a YAML graph: a runner reached through a "
    "composite action, a reusable workflow, or a script this cannot see "
    "reads as absent; a trigger written as a flow mapping, as a flow list "
    "across lines, or as one event name on the line below `on:`, reads as "
    "unread and is not counted"
)
```

```python
# tests/skills/test_deferral_check.py, test_a_pull_request_trigger_in_the_wider_spellings_answers
            "on: [pull_request, ]\n",
        ...
            "flow-list-trailing-comma",
```

verdict: open
answer:

### 2. A pull_request trigger narrowed to after the merge now counts as answering in the inline spelling the base refused

severity: should
location: `skills/verify/scripts/deferral_check.py:137-138`, `skills/verify/scripts/deferral_check.py:83-88`, `tests/skills/test_deferral_check.py:234-238`
evidence: executed `python3 -I test_tmp_shapes.py`, `uv run --no-project --with pyyaml python3 -c 'import yaml; yaml.safe_load(...)'`

The trigger `on:` / `  push:` / `  pull_request: {types: [closed]}` runs the
suite when a pull request closes, which is after the point a deferral is
made. That is the same too-late failure as #1123's push-only run. The base
printed `too late ... (on push, not pull_request)` at exit 1. The branch
prints `answers ... (on pull_request, push)` at exit 0, because
`block_entries` now takes the key out of a line that carries a value
(`:137-138`), as Scope item 1 asks.

The class is older than this branch. Its block spelling, `pull_request:`
with `types: [closed]` on a deeper line, was counted at the base too,
because deeper lines are skipped (`:131-134` here, the `indent <= 2` key
match at base `:117-119`). The same holds for `branches:` and `paths:`
filters that keep a pull_request workflow from running on the pull request
being deferred. `SECURITY.md` *What is in scope* calls a check that fails
open a security defect. Nothing the command prints says that filters go
unread: `KNOWN_LIMITS` at `:83-88` names composite actions, reusable
workflows, unseen scripts and the two unread shapes, and no filters. This
diff moves one more spelling into the class, and it rewrites the limit
string, which is where the class can be named.

Filters are an open set of keys and values, so naming them closes nothing
by enumeration. The limit sentence is what states it, and S8 pins it.

```python
KNOWN_LIMITS = (
    "reads command text, not a YAML graph: a runner reached through a "
    "composite action, a reusable workflow, or a script this cannot see "
    "reads as absent; an event's filters (types, branches, paths) are not "
    "read, so a pull_request trigger limited to closed pull requests counts "
    "as answering; a trigger written as a flow mapping, or as a flow list "
    "across lines, reads as unread and is not counted"
)
```

```python
    def test_the_printed_limit_names_a_trigger_it_cannot_read(self, tmp_path):
        r = run(["--kind", "tests", str(tmp_path)])
        [limit] = [line for line in r.stdout.split("\n") if line.startswith("limit: ")]
        assert "flow mapping" in limit, limit
        assert "unread and is not counted" in limit, limit
        assert "filters" in limit, limit
```

verdict: open
answer:

## Confirmations

confirms: none
The S-row cases were red at the base. The crafter claimed S1 to S8 failed
against the base script. The probe ran the base script, from
`git show 8d8d6390:skills/verify/scripts/deferral_check.py` on stdin, and
the branch script over each of the 21 trigger parameters (executed). Every
push-only spelling exited 0 at the base with `answers ... (trigger unread)`
and exits 1 on the branch with `too late ... (on push, not pull_request)`.
The wider pull-request spellings printed `(trigger unread)`, or
`too late ... (on "pull_request", ...)` for the quoted name, and now print
`answers ... (on pull_request)`. The seven unread shapes printed `answers`
or `too late` with no `unread` line, and now print the `unread` line. S7
printed `on push] # trigger` at the base. So each new parameter pins a
behaviour the base did not have.

confirms: none
The crafter's departure from Scope item 1 holds. It claimed that a block
line shallower than the block, but not at indent zero, makes the whole
trigger unread (61e2e6be), following Scope item 2. `block_entries` returns
an empty list at `skills/verify/scripts/deferral_check.py:131-132`. The
probe showed `on:` / `    pull_request:` / `  push:` printed `too late` at
the base and `unread` on the branch. A YAML parser refuses that text with a
`ParserError` (executed), so ending the block there would read a trigger
GitHub does not run as `{pull_request}`, which answers. The departure fails
closed. It is the reading Scope item 2's sentence on partly read triggers
gives, and `gaps.md` records it. `frame/design.md` Scope item 1 still reads
"A shallower line ... ends the block"; `gaps.md` *Where spec and
implementation diverged* is where the work item keeps that difference.

confirms: none
Each row of `frame/design.md` *Removes* is gone. The `not events` arm in
`inspect` became the `unread` list at
`skills/verify/scripts/deferral_check.py:249-251` (read). `git grep -i
'trigger unread'` outside `seal/threads` finds only the new
`(trigger unread, not counted)` at `:279` and `README.md:257` (executed).
The `indent <= 2` bound and the "reported as unknown" sentence are gone from
`read_events` (read `:144-173`). The module docstring says five outcomes
and lists five at `:14-21` (read).

confirms: none
The unread line has the shape and position the design states. At
`skills/verify/scripts/deferral_check.py:277-280` it prints after the
`too late` lines and before the `local` lines, with `unread` padded to the
same ten-character column (read). The verdict at `:287` is `True` only when
`resolving` is non-empty, so an unread workflow alone exits 1, and one
beside an answering workflow exits 0 (read; S6 and the probe's no-on-key
row, executed).

confirms: none
The fifth outcome is in the three documents the frame names:
`skills/verify/SKILL.md:357-363`, `README.md:257` and `README.ko.md:252`
(read). `tests/behaviour/test_both_editions_carry_the_same_folds.py` and
`tests/behaviour/test_docs_line_wrap.py` pass over them (executed, in the
narrow run below).

confirms: none
The fail-open the crafter flagged outside scope is not made worse. A
pull-request workflow with `run: echo skip pytest` printed
`answers ... — echo skip pytest` at exit 0 at both the base and the branch
(executed). `runners_in` is not in the diff (read).

confirms: none
The new tests do not duplicate their group. `seal layout --pairs` names no
pair in `tests/skills/test_deferral_check.py` (executed). Read against the
existing `Test_main` cases, only `test_inline_event_list_is_read`
(`on: [push, pull_request]`) is near a new parameter, and S7's
`on: [push] # trigger` covers the trailing comment it does not cover (read
`tests/skills/test_deferral_check.py:74-121`).

confirms: none
The replay eval's line pins do not move with this edit. Both
`evals/behaviour/proofer/replay-1791382684-r2/graders/truth-inspect-reads.md`
and `evals/scripts/recurred_truths.json` cite `deferral_check.py` lines
read in `scaffold.sh`'s checkout of `7ef6abbf` (read
`evals/behaviour/proofer/replay-1791382684-r2/scaffold.sh:4-6`).

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* names the full
suite, the repository-wide ruff check and format and the typecheck, with
the orchestrator through `seal gate` as the answerer (read). This round ran
none of the three.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's `seal mutate` result: 14 mutants over `read_events`, `inspect`, `block_entries` and `unquoted`, with the survivors answered by 5cc5c80d and 61e2e6be. Not re-run this round. A mutation score licenses tested, never safe | `trail/phases/phase-1.md` | the sealer, in its sample of the crafter's claims |
| Whether a block that mixes a `- ` item and a key at one indent should read as unread like the shallower line. `on:` / `  - push` / `  pull_request:` is refused by a YAML parser (executed), and it reads as `answers ... (on pull_request, push)` at the base and on the branch alike (executed). The scan validates no YAML elsewhere in the file either | `skills/verify/scripts/deferral_check.py:135-138` | the orchestrator, whether it belongs to this work item, a limit sentence or #1038 |
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the branch at `cbbbe744` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_shapes.py`, in the clone at `cbbbe744`: one temporary project per trigger shape with a `pytest` step, run through the base script (`git show 8d8d6390:skills/verify/scripts/deferral_check.py` on stdin) and the branch script with `--kind tests` | 28 shapes, exit 0. The 21 S-row parameters were red at the base as the first confirmation states. `on: [push, pull_request, ]` and `on: [pull_request,]`: base exit 0 `answers`, branch exit 1 `unread`. `on:` / `  pull_request`: base exit 0 `answers`, branch exit 1 `unread`. `on:` / `  push:` / `  pull_request: {types: [closed]}`: base exit 1 `too late`, branch exit 0 `answers (on pull_request, push)`. `on:` / `  - push` / `  pull_request:`: exit 0 `answers` at both. `run: echo skip pytest` on `pull_request`: exit 0 `answers` at both. CRLF line endings, `on: # the trigger` above a four-space block, and `on : pull_request`: branch exit 0 `answers (on pull_request)`. The file was deleted after its one run |
| `uv run --no-project --with pyyaml python3 -c 'import yaml; yaml.safe_load(...)'` over the shapes above | `on: [push, pull_request, ]` loads as `{True: ['push', 'pull_request']}`, `on: [pull_request,]` as `{True: ['pull_request']}`, `on:` / `  pull_request` as `{True: 'pull_request'}`, and the closed-only trigger as `{True: {'push': None, 'pull_request': {'types': ['closed']}}}`. `on:` / `    pull_request:` / `  push:` and the mixed item and key block raise `ParserError` |
| `bin/test tests/skills/test_deferral_check.py tests/test_censuses.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_both_editions_carry_the_same_folds.py -q -p no:xdist` | 279 passed, exit 0 |
| `bin/seal layout --pairs` | exit 0, 128 pairs, none in `tests/skills/test_deferral_check.py` |
