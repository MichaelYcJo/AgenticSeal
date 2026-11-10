# Review round 1: 1794271935-the-releasing-documents-describe-the-note-twice

```seal
target: b6845b32c against origin/release/v0.37.1
```

This is the first round, so no earlier record carries a coordinate and every
fact below was established here. The diff was read from the merge base
`8657297d5` to `b6845b32c`. `routing.md`, the three frame files, `gaps.md`,
`changelog.md` and `pr.md` were each read whole at `b6845b32c`. No
`pr.<lang>.md` stands, and none is owed: `seal/config.json` names English
for both language keys. No `seal/parity.json` is declared.

## Findings

### 1. The census claims a whole list of path citations, and misses a second docstring that cites the checklist's "step 3"

```seal
severity: should
location: `seal/threads/1794271935-the-releasing-documents-describe-the-note-twice/gaps.md:24-33`, `seal/threads/1794271935-the-releasing-documents-describe-the-note-twice/trail/phases/phase-2.md:90-106`, `tests/conftest.py:213-215`, `tests/behaviour/test_release_hygiene.py:1372-1376`
evidence: executed `git grep -n 'release-checklist' -- . ':!seal/threads'`, `git grep -n -i -P "\bsteps? (0|1|2|2b|3|4|5|6)\b" -- . ':!seal/threads' ':!skills/update'`, `git show 53f21b542^:docs/release-checklist.md | grep -n '^## '` and the same at `53f21b542`; read `tests/conftest.py:208-216`, `tests/behaviour/test_release_hygiene.py:1371-1380`, `docs/releasing/release-checklist.md:109-111`, `skills/settle/scripts/settle.py:1854`
```

Why it matters: the phase record and the closing memo tell the sealer and
the settle that one stale step number is left in the tree, and there are
two. Contract rule 12 makes a sample handed back as a whole list a finding
on the method, even where every listed instance was handled.

The claims and what the tree holds:

- **Claimed** in `trail/phases/phase-2.md:90-95`: the census "builds the
  list from what produces the defect, a citation that writes the path or
  the heading's words, so it is whole for those two spellings." **Found**:
  `tests/conftest.py:213-215`, the docstring of `build_tracked_tree`, says
  "the state the documented release sequence produces at step 3 of
  `docs/releasing/release-checklist.md`". That sentence writes the path, and
  `git grep -n 'release-checklist'`, the first pattern of `frame/plan.md`
  *Technical context*, lists it at line 215. Neither phase record nor
  `gaps.md` names it.
- **Claimed** in `gaps.md:24-33`: the docstring of
  `tests/behaviour/test_release_hygiene.py#test_the_timer_sweep_survives_a_tracked_file_the_tree_deleted`
  is the one step number left, and rewriting it "needs a fact this work
  item did not establish: which act of a release meets that sweep first, if
  any." **Found**: both sentences were written in `fc3e1175c`, when the
  checklist's step 3 was *3. Verify before committing*. `53f21b542` removed
  that step: its parent holds the heading at line 119 and `53f21b542` holds
  no step 3. The fact both sentences need already stands in the
  checklist. `docs/releasing/release-checklist.md:109-111` says
  "`--apply` deletes each directory from the working tree and stages
  nothing", and `skills/settle/scripts/settle.py:1854` removes each
  directory with `shutil.rmtree`. That is the state `build_tracked_tree`
  builds: a tracked file deleted from disk and still in the index.
- **Claimed** in `gaps.md:27-29`: no box of the checklist runs
  `test_release_hygiene.py`, which names it only in the opening paragraph
  and on two `check:` lines. **Found**: true, at lines 8, 241 and 344.

Neither docstring is one of the four headings `frame/design.md` *Scope*
item 5 renames, so the two sentences are outside that item. The finding is
the account's method and the memo's count. Of the fix below, the memo and
the phase record's sentence are owed. The two docstring rewrites are the
cheaper way to owe them, since the memo's paragraph then has nothing left
to hold. The checklist cannot have a numbered step after this work, so each
sentence can only name the act.

In `tests/conftest.py`, lines 213 to 215 of `build_tracked_tree`'s
docstring:

```python
    it stays in the index and leaves the working tree. That is the state
    `seal settle --apply` leaves, since it deletes each directory and stages
    nothing (`docs/releasing/release-checklist.md` *Settle what earlier
    releases left behind*), and the state `on_disk` below is about.
```

In `tests/behaviour/test_release_hygiene.py`, the docstring's first two
sentences. The second sentence's claim that "the whole gate runs before
anything is staged" stood on the removed step 3, and nothing this round read
says a gate runs between `--apply` and its commit, so the rewrite drops it:

```python
    """#432's class in the module `docs/releasing/release-checklist.md` names
    on its `check:` lines.

    `seal settle --apply` deletes each directory and stages nothing
    (`docs/releasing/release-checklist.md` *Settle what earlier releases left
    behind*), so the index can list paths the disk does not have. The running
    version and the timer are both fixture values, for the
```

With both rewritten, `gaps.md` *Not done* loses its second paragraph,
lines 24 to 33. `trail/phases/phase-2.md:93-95` stated `c44121bff`, where
`tests/conftest.py:215` already stood. So its "whole for those two
spellings" was untrue at that commit, and the fix pass names that in its
close or corrects the sentence in place. Where the docstrings stay, the
memo's paragraph names `tests/conftest.py:213-215` beside the hygiene
docstring, and drops the claim that the fact was not established.

## Confirmations

What matched: `frame/design.md` *Scope* item 1. The box **A GitHub Release
exists at `vX.Y.Z`** at `docs/releasing/release-checklist.md:273-315` was
read against the item's three lists. It keeps `gh release view`,
`gh run list --workflow publish-release.yml` and the workflow file. It keeps
each state: no release, the `no tag:` line, the job's red causes, a bare
tag-name title with the log line `publish_release_note.py:421-430` prints,
the line saying the pull requests could not be listed, and the `seal` job's
`::warning::` causes with the key named as a key. It keeps both repairs.
It cites `branch-and-release.md` *Cutting a release* twice for the make-up.
The scenario S1 grep lists `branch-and-release.md:85` alone (executed).
The box's unconditional "attaches `seal.png`" is qualified by the key
sentence two lines later and by the citation, and
`.github/scripts/release_seal.py:11-12` agrees that a value other than
`yes` is named on a `::warning::` line (read).

What matched: *Scope* item 2 and scenario S5. The diff of
`.github/workflows/publish-release.yml` changes `#` lines alone (executed,
the diff filtered to lines that do not open with `#`, empty). The seal
paragraph cites *Cutting a release*, and the `dist` red's reason no longer
names the directory (read, lines 22-46). Phase 1's departure, the `dist`
sentence, is the copy *Scope* item 3 removes, and it stays a comment.

What matched: *Scope* item 3, scenario S2. The S2 grep finds nothing in
`docs/releasing/` (executed). Every sentence of `docs/releasing/` on the
directory was read: `branch-and-release.md:116-127, 144-182, 228-244` and
`release-checklist.md:258-334`. The orchestrator asked for two sentences to
be read against item 3. The `dist` paragraph says the workflow "pushes
without force, because the directory serves a scanned commit of the branch
it tracks" (`branch-and-release.md:173-174`). The third-reader paragraph
says a submitted plugin "is served from a scanned commit of the branch or
tag the submission tracks", and that "this plugin's submission tracks
`dist`" (`branch-and-release.md:233-238`). Each states how the directory
treats a submission and which branch this plugin's submission names. #1420's
body records that the directory still holds the `dist` submission
`v0.33.0 · 4871b80` under review (executed, `gh issue view 1420`), so "holds
a commit" stays true while the listing is on hold. Neither says the
directory lists or serves this plugin's version, so I agree with the
crafter's judgment in `gaps.md:10-22`. The checklist's "Two acts come
after the tag: publishing the release note, and telling the plugin
directory" (`release-checklist.md:262-263`) was weighed on the same grounds.
The `dist` job still adds the commit the tracked submission names, and the
box below says the listing is on hold and that it runs all the same. So
this round opens no finding on it. Whether the directory reviews a new
`dist` commit while held is a row of `## Not judged`.

What matched: *Scope* item 4. The case
`tests/text/test_the_release_tail_does_not_end_at_the_tag.py#test_the_listing_s_hold_carries_its_date_and_whose_decision_it_is`
passes at `b6845b32c`, and went red on its `` `dist` `` line with `dist`
taken out of the hold's sentence (executed, see `## Probes`). That agrees
with phase 1's mutation record. Read against its group in the same file,
the case holds a fact no other case there holds, and it replaces the case
that pinned the removed sentence. The paragraph's `check:` line names the
file (`branch-and-release.md:182`).

What matched: *Scope* item 5, scenario S4. Both S4 greps find nothing
(executed). The census and every module the plan's two rows name pass
(executed, see `## Probes`). `python3 .github/scripts/finding_counts.py
--help` prints the citation of *Settle what earlier releases left behind*
(executed). The three prose mentions inside the checklist now name the
heading or drop the number (`release-checklist.md:30, 139-140, 172-173`,
read). The prose sweep this round added for step mentions that write
neither the path nor a heading's words found the two docstrings of
finding 1 and nothing else about this checklist. That sweep was
`git grep -P` on numbered steps and on `2b` across the tree, and
`git grep -i checklist` filtered to step, box, section and heading.
The other hits name steps of `agents/`, `skills/` and
`skills/update/SKILL.md`, which are other documents' steps. Over prose the
class is open, so this sweep is a sample too.

What matched: *Scope* items 6 and 7, scenario S3. `git grep -n '#51' --
docs` finds nothing (executed). The five sites name "the open
`flow-baseline` issue", and the `log:` paragraph and Ends cell say why the
milestone never closes (`issues-and-milestones.md:16, 61-67`, read). #1464's
body says "This body is the current state" in its second paragraph
(executed, `gh issue view 1464`), so "at the top" holds. Phase 2's departure
at `issues-and-milestones.md:192` follows the same fact. The #1148 sentence
names #1148 once (`release-checklist.md:89-92`, read).

What matched: `pr.md`. Each of its seven quotes stands word for word, with
whitespace collapsed, at the coordinate it names: `changelog.md` *Changed*
items 1 to 4, and `frame/plan.md` *Alternatives considered*, *Operational
impact* and *Judgments of the run* (read). `changelog.md`'s items each match
the diff (read). The closing memo's `## Not verified` reads "nothing", and
every phase claim this round re-ran held.

The `.test_durations` key of the removed case at line 5973, which phase 1
names, is left for the release's refresh (#1468). Neither phase writes it,
and the narrow run does not refuse it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at `b6845b32c`: the suite stands `unverified` here, and the narrow run of `## Probes` is not it | `seal/config.json` `Broad gate` | the orchestrator, by its broad run before the sealer's spawn |
| Whether the plugin directory still reviews a new `dist` commit while the listing is on hold, which decides whether "telling the plugin directory" stays true | `docs/releasing/release-checklist.md:262-263` | the owner, who reads the developer portal |
| #1464's body still cites `docs/releasing/release-checklist.md` *2b* | outside the tree; `frame/plan.md` *Operational impact* | the orchestrator or the owner, with `gh issue edit 1464` |

## Probes

| Command | Result |
|---|---|
| `bin/test` on the ten modules `frame/plan.md` *Phases* names, `-q`, in a clone at `b6845b32c` | 207 passed, 1 skipped, exit 0 |
| The hold's sentence edited with `` `dist` `` replaced by "publish" in the clone, then `bin/test tests/text/test_the_release_tail_does_not_end_at_the_tag.py -q -k test_the_listing_s_hold -p no:xdist` | exit 1, failed on the case's `` `dist` `` assertion with its own message, "the hold's sentence does not name the branch that keeps running"; the file was restored with `git checkout`, and `git status --short` printed nothing |
| `python3 .github/scripts/finding_counts.py --help` in the clone | prints "Print the four numbers of `docs/releasing/release-checklist.md` *Settle what earlier releases left behind* per released work item." |
| The greps of scenarios S1 to S5, as `frame/design.md` writes them | S1 lists `docs/releasing/branch-and-release.md:85` alone; S2, S3 and both S4 greps find nothing; S5's filtered diff is empty |
