# Review round 1: 1795841830-find-leftovers-before-a-round

```iadd
target: 4c46218b against origin/release/v0.41.0
```

Round 1 is a finding round over the whole range from the merge base `991a51c7`, which is the base's tip, to `4c46218b`. No earlier round exists, so no fact was carried: every coordinate below was opened at the target in a `git clone --no-local` under the round's scratch directory. The range holds no merge of the base.

Stage 1 read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md` whole at the target, then the diff of every path the range changes. `Record language` and `Commit and pull request language` are both English (`agentory/config.json`, `read`), so no `pr.<lang>.md` is owed and none stands. The policy root is `docs/`, which the range does not change; the design's `## Rule changes` carries its five operations.

## Findings

### 1. The keep file's rule gives one keep file per phase, but a phase can run two searches that keep lines, and the rule's cross-phase sentences assume every phase runs the same search

```iadd
severity: should
location: `skills/verify/SKILL.md:63-80`, `skills/verify/SKILL.md:105-117`, `agents/framer.md:176-186`
evidence: read `skills/verify/SKILL.md:63-80`, `skills/verify/SKILL.md:92`, `skills/verify/SKILL.md:105-117`, `agents/framer.md:176-186`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/plan.md:41`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:96-110`; executed `git grep -n -e "keep-<N>" -e "keep-N" -e "keep file" -- agents skills templates agentory/README.md docs lib` and `git grep -n -i -e "search of phase" -e "phase's search" -e "phase N's search" -e "a phase's search" -- .`
```

Why it matters: `skills/verify/SKILL.md:63-67` gives the keep file to "a content search" that a phase's *Verified by* cell "or a *Verifiable how* cell in `frame/design.md`" names "for phase `<N>`", and names it `frame/keep-<N>.txt`. The name carries the phase and no search. A phase that runs two searches which each keep lines therefore has two searches with one keep file. The content command at `skills/verify/SKILL.md:92` runs one pattern and compares its output with the whole file, so each search's `diff` prints the other search's kept lines as `>` lines, which `:99-100` reads as "a kept line the phase changed or removed". Neither command can then print nothing, and the rule gives the framer no reading for the case. Two searches in one phase is not rare: this work item's own phase 1 is verified by `S1` and `S2` (`frame/plan.md:41`), two patterns over one pathspec.

The same assumption sits in the cross-phase sentences. `skills/verify/SKILL.md:71-72` defines "a phase's own lines" as those "its keep file lacks and the earlier phase's keep file holds", and `:108-110` has the builder write a rewritten kept line "into every later phase's keep file". Both hold only where every phase runs the same search. Where phase 1 renames one name and phase 2 another, phase 2's search does not print phase 1's kept lines, so a line written into phase 2's keep file by `:110` is a `>` line of phase 2's `diff`. A *Verifiable how* cell of `frame/design.md` (`:65`) belongs to no phase, since the acceptance table has no phase column, so `<N>` has no value for it, and `agents/framer.md:183-184` sends such a cell's kept lines to "the phase's keep file" the same way.

The search listed every statement of the keep file's subject (the two commands on the `evidence:` line). Each other statement names "the search of phase N" in the singular: `skills/implement/SKILL.md:353`, `templates/setup/agentory-README.md:94-95`, `agentory/README.md:94-95`, `agents/framer.md:41-42` and the design's two `add` operations at `frame/design.md:117` and `:121`. The fix below makes one search per phase the rule, so those statements stay true and the snippet touches `skills/verify/SKILL.md` and `agents/framer.md` alone. A search on these words is a sample under contract rules 12 and 19, since a statement in other words escapes it. Should the fix pass choose a keep file per search instead, it owes `lib/optin.py#KEEP`, the case of `tests/skills/test_range_read.py` and every statement the search printed.

In `skills/verify/SKILL.md`, replace the sentence at lines 63-67 that opens the rule's first paragraph, and the two sentences at lines 71-72:

```markdown
**A search that is to print lines the design keeps compares them with a
keep file.** A phase has at most one content search that is to print lines
the design keeps at its close, and its *Verified by* cell in
`frame/plan.md` names it: where the design keeps lines of several
patterns, the cell joins them into one pattern over one pathspec, as
`-P 'first|second'`. That search has the keep file `frame/keep-<N>.txt`. A
*Verifiable how* cell in `frame/design.md` that rests on such a search
names the phase whose search it is, and runs no search of its own. The
keep file holds each line the search is to print at that close, written as
`git grep` prints it with no line number, `path:content`, and sorted under
`LC_ALL=C sort`. Those lines are the lines the design keeps and the lines
a later phase changes. Where an earlier phase runs the same search, a
phase's own lines are the lines its keep file lacks and the earlier
phase's keep file holds.
```

and in the same file, at lines 108-111:

```markdown
names. Where a phase rewrites a kept line, as a rewrap does, or writes a
line that holds a kept kind, the builder writes the line into that phase's
keep file and into the keep file of each later phase whose search prints
it, in the same commit. A kept line the tree no longer holds leaves those
keep files the same way.
```

In `agents/framer.md`, at lines 183-184:

```markdown
*Scope* item or a `## Removes` row. A line the design keeps is a line of
the keep file of the phase whose search prints it, as `skills/verify/SKILL.md` *An absence claim is only
```

### 2. The framer's rule accounts for a line that a later phase removes only by a Scope item, so the framer leaves it out of the earlier phase's keep file and that phase's crafter reads it as a leftover

```iadd
severity: should
location: `agents/framer.md:180-186`
evidence: read `agents/framer.md:180-186`, `skills/verify/SKILL.md:67-71`, `skills/verify/SKILL.md:96-100`
```

Why it matters: `agents/framer.md:180-183` has the framer "account for each line it prints in one of two ways": a line the build removes is named by a *Scope* item or a `## Removes` row, and a line the design keeps is a line of the phase's keep file. `skills/verify/SKILL.md:67-71` says the keep file of phase `<N>` holds each line its search is to print at that phase's close, "the lines the design keeps and the lines a later phase changes". A line that phase 2 renames is printed by phase 1's search at phase 1's close, so it belongs in `frame/keep-1.txt`. The framer's own rule, which its definition preloads, files that line under the first way alone, a line "the build removes", and gives no second way for it. A framer that follows `agents/framer.md` writes `frame/keep-1.txt` without the lines phase 2 renames. Phase 1's keep command then prints each of them as a `<` line, which `skills/verify/SKILL.md:97-99` calls "a leftover". The crafter of phase 1 renames them, and builds phase 2's scope inside phase 1. The "one of two ways" wording is the defect: the two ways are written as exclusive, and the line a later phase removes needs both.

In `agents/framer.md`, replace lines 180-183, from "account for each line" to "`## Removes` row.":

```markdown
account for each line it prints. A line the build removes, or changes so
that the search no longer matches it, is named by a *Scope* item or a
`## Removes` row, and it is also a line of the keep file of each phase that
closes before the phase that removes it.
```

### 3. A fix pass runs its set under "the commands the phase's *Verified by* cell names", but a fix pass has no phase, and the crafter's rule for a suite no cell names does not reach it

```iadd
severity: should
location: `skills/implement/fix-pass.md:95-97`, `skills/implement/SKILL.md:203-205`, `skills/verify/SKILL.md:200`, `skills/verify/SKILL.md:202`
evidence: read `skills/implement/fix-pass.md:95-97`, `skills/implement/SKILL.md:203-205`, `skills/verify/SKILL.md:200-202`, `skills/verify/SKILL.md:223-229`, `agents/crafter.md:61-65`, `agents/crafter.md:71-73`; executed `git grep -n -i "phase boundary" -- agents skills docs templates CONTRIBUTING.md`
```

Why it matters: `skills/implement/fix-pass.md:95-97` runs the *Review rounds 1..n* set "under the commands that table's *Phase boundary* row states". That row, at `skills/verify/SKILL.md:200`, states them as "the commands the phase's *Verified by* cell names". A fix pass is no phase, and the paths its fixes change can fall in several phases, each with its own *Verified by* cell. `skills/implement/SKILL.md:203-205` sends the builder to the same row for both sets. So "the phase" has no referent in a fix pass. A fix pass that takes the last phase's cell runs a file of an earlier phase's built-app or end-to-end suite under the last phase's runner. That is the green run over a file it did not run that `skills/verify/SKILL.md:225-227` describes and Scope item 6 exists to prevent.

The fallback does not reach the fix pass either. The rule for a file whose suite no cell names stands in `agents/crafter.md:63-65`, step 7, and step 9 at `:71-73` has a fix pass follow `skills/implement/fix-pass.md` "in place of step 7's run". `fix-pass.md` carries no such rule. The search on the `evidence:` line listed the statements of the *Phase boundary* set: `agents/crafter.md:61`, `skills/implement/SKILL.md:203`, `skills/implement/fix-pass.md:97`, `skills/implement/orchestration.md:503`, `skills/code-review/orchestration.md:27` and `CONTRIBUTING.md:300`. Only the first three say which commands run the set, and the snippets cover the two a fix pass reads. The search is a sample under contract rules 12 and 19.

In `skills/implement/fix-pass.md`, replace lines 95-97:

```markdown
Once the fixes are committed, the fix pass runs the set the *Review rounds
1..n* row of `skills/verify/SKILL.md` *Scope: cheap and often, broad and
once* names, with one command for each suite that owns a file of it: the
commands the *Verified by* cells of the phases whose paths the fixes
changed name. Where a file of the set belongs to a suite none of those
cells names, the fix pass runs the file under that suite and names the
missing command in the `answer:` of the close block of the finding whose
fix changed it.
```

In `skills/implement/SKILL.md`, replace lines 203-205:

```markdown
The builder types the commands the *Phase boundary* row of
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once* states
for a phase, and the commands `skills/implement/fix-pass.md` *The narrow
set, then the read of the range* states for a fix pass, over the set that
row or the *Review rounds 1..n* row names, never the
```

## Confirmations

What matched: `frame/questions.md` Q2, which the frame left to this round or to `chain-check`. `## Rule changes` parses whole as `skills/settle/scripts/rule_changes.py#parse` reads it, with five operations, no error and no unread line. `rule_changes.py#apply_op` places each operation in `docs/layout/the-record-layout.md` at the target (`executed`, the probe in `## Probes`). The two `add` rows land as the last rows of the table under *agentory/threads/<work-item-id>/*, after `pr.<lang>.md`. The `change` of the *leave together* sentence matches across its wrapped lines and writes the new text on one line, which the settle's draft rewraps or leaves as it is. Q2's Status cell still reads `open`. Marking it answered is for the party that answers the row, so this round does not mark it.

What matched: Scope item 12. `skills/implement/scripts/range_read.py#_read` sends a work item's keep file to `_own_lines` after the deleted, submodule and binary branches and before the `.md` branch (`range_read.py:463-476`, `read`). `_keep` refuses a local root (`rel is None`), a path outside the item's directory and a name `lib/optin.py#KEEP` does not match whole (`range_read.py:386-392`, `read`). `_own_lines` prints `git diff -U0 --inter-hunk-context=0` with each hunk header cut to `HUNK`'s match, so git's function line is gone (`range_read.py:395-402`, `read`). `tests/skills/test_range_read.py` and `tests/lib/test_optin.py` pass at the target, and the keep file case fails against `range_read.py` and `lib/optin.py` as `d216647a` holds them, on `assert line + "\n" not in own` (`executed`). That reproduces the claim of `trail/phases/phase-2.md:22`. The module docstring (`range_read.py:22-29`), `skills/implement/SKILL.md:276-283`, `frame/design.md` *The range file and a keep file* and `changelog.md:4` say what the code does (`read`).

What matched: Scope items 2 to 5, 8, 9 and 13, each sentence the design names read at its coordinate (`read`). `S1`, `S2` and `S3` run over `.` with the work item's directory excluded print nothing in `agents/`, `skills/`, `docs/` or `templates/` (`executed`). `S2`'s hits are the test docstrings and comments the design names, the two of `frame/design.md:107` and five that use "three files" of other things. `templates/setup/agentory-README.md` and `agentory/README.md` are byte-identical (`executed`, `diff`). The new paragraph of `skills/implement/orchestration.md` *Under agentic* cites `skills/code-review/orchestration.md:146` for the verifying round's cost, which says it "runs close to a finding round", and `docs/releasing/branch-and-release.md:435` for `Part of #N` (`read`).

What matched: the coordinates that `trail/phases/phase-2.md:38-40` names for the test files that open a changed file, `tests/conftest.py:459` and `:1206`, `tests/skills/test_agentic.py:3211` and `:3729`, `tests/lib/test_gaps.py:357`, `tests/github/test_release_mark.py:586`, `tests/skills/test_chain_check.py:4535` and `tests/skills/test_session_cost.py:768`, each say what the record says (`read`).

What matched: `pr.md`. `agentic pr-body` composes the body at the target with exit 0 (`executed`), so both quote lines hold in the records they name. The `feat:` row of `frame/plan.md` *Judgments of the run* cites `skills/commit-pr-convention/SKILL.md`'s prefix table, and the work adds a form and a command's output (`read`).

What matched: *Out* excludes `agents/framer.md`'s frontmatter `description`, which still lists the three frame records as its writes. It does so with grounds in the SDD set (`frame/design.md:55`), so the round does not count it as an omission. `chain_check.py --worktree` printed no notice at a line of `frame/design.md` naming a test pin or a copy (`executed`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check. The suite stays `unverified` here, as phase 2 handed it over | `agentory/config.json` `Broad gate` | the orchestrator |
| Whether a framer, a crafter and an orchestrator follow the rules this work wrote in a later run. A round reads each rule for one reading, as findings 1 to 3 do, and runs no agent | `gaps.md` `## Not verified`, its second and third rows | the repository owner, through the row this work adds to `agentory/follow-up.md` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_range_read.py tests/lib/test_optin.py -q`, in the scratch clone at `4c46218b` | 97 passed |
| `git checkout d216647a -- skills/implement/scripts/range_read.py lib/optin.py`, then `bin/test tests/skills/test_range_read.py -q -p no:xdist -k "keep_file or local_root"`, then `git checkout HEAD --` of both files, in the scratch clone | exit 1: the keep file case failed on `assert line + "\n" not in own`, and the local-root case passed; `git status --short` printed nothing after the restore |
| `test_tmp_rule_changes.py` under the round's scratch directory, run once with the clone's `.venv` Python: `rule_changes.parse` over `frame/design.md` with policy root `docs`, then `apply_op` of each operation over `docs/layout/the-record-layout.md` | `ops 5 errors [] unread []`, and each of the five operations printed `placed` |
| `bin/agentic pr-body agentory/threads/1795841830-find-leftovers-before-a-round --body <scratch file>`, in the scratch clone | exit 0, a body of 9900 bytes |
| `S1`, `S2` and `S3` of `frame/design.md` *The searches* with the pathspec `. ':!agentory/threads/1795841830-find-leftovers-before-a-round'` | `S1` and `S3` printed nothing; `S2` printed seven lines, all under `tests/` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.41.0 --root <the branch worktree> --worktree`, before this record was written | exit 0; it named the missing round record, gate record and inspection, and printed no notice at `frame/design.md` |
