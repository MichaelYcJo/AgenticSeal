# Review round 4: 1793188384-the-release-notes-are-kept-twice

target: 5aa3f0d4, fixes 572105e5..5aa3f0d4

This is the verifying round after round 3. It read the fix diff
`572105e5..5aa3f0d4` in a `git clone --no-local` of the branch at
`5aa3f0d4`, held in the round's scratch directory. The diff is three
commits. The orchestrator's `c7a3fa4d` changes the frame and the plan. The
fix pass's `5eebfaf1` changes the script's docstring, the workflow's
checkout comment and one test docstring. `5aa3f0d4` commits round 3's
record with the fix pass's two lines. The repository declares no
`seal/parity.md`, so this round has no `original:` line. Phase 5's S11 is
the orchestrator's, and this round did not judge it.

Round 3's coordinates were carried, not searched for again: the ten
sentences of its finding 1, the hits it kept with a reason, and the 0.15.3
shape, a directory restored inside the range, as the case the skip exists
for. Its probe was not written again. The fix range changes no line of code
that runs: `5eebfaf1` touches only a module docstring, a YAML comment and a
test docstring (read: the diff). So the reader's behaviour that the probe
measured at `4eb31bb8` is the reader's behaviour at `5aa3f0d4`. Every
verdict below was reached again. The two searches the fix pass's answer
records were re-run, with its search of `docs/`, and this round added its
own over the work item's `frame/`, `changelog.md` and `gaps.md` and a wider
phrasing over the tree.

## Findings

No finding this round.

## Confirmations

confirms: round-3#1
The close holds for the ten coordinates and for the class.

At the ten coordinates (read: `git diff 572105e5..5aa3f0d4`): `c7a3fa4d`
applies round 3's seven frame and plan blocks word for word, at
`frame/design.md:184-186`, `:211-217`, `:250-253`, `:431-432`, `:439-440`
and `:491`, and at `frame/plan.md:9-11`. It changes no `from:` text, so
every `from:` the settle matches against `docs/` is as it was. `5eebfaf1`
applies the other three blocks as given, at
`.github/scripts/publish_release_note.py:64-67`,
`.github/workflows/publish-release.yml:57-61` and
`tests/github/test_publish_release_note.py:238-240`. Each of the ten now
states that a fragment the previous tag already holds is left out.

For the class, the fix pass's two recorded searches were re-run in the
clone (executed). Search (A), the `added` sweep, printed 22 lines. Search
(B), the phrasing sweep, printed 51 lines. Every hit that states which
fragments the note reads, or when the job fails for an empty range, carries
the skip: `publish_release_note.py:19-21`, `:64`, `:97`, `:200` and the
message at `:665-666`, whose clause `held` adds where there is a previous
tag; `publish-release.yml:16-18` and `:57-59`;
`tests/github/test_gather_changelog.py:5-6`;
`tests/text/test_the_changelog_is_gathered_at_release.py:5-6`;
`test_publish_release_note.py:7-9`, `:11` and `:238-239`. The hits the
answer kept were each opened again, and each states no selection rule.
`publish_release_note.py:16` is a heading whose rule `:19-21` states.
`CONTRIBUTING.md:397` says only that the tag's workflow builds the notes
from the fragments, and points at `docs/branch-and-release.md`; `:453` names
the topic. `skills/verify/scripts/session_cost.py:2856` speaks of one work
item's fragment. `test_publish_release_note.py:65` and `:150` describe the
values handed to a stub. The case names at `:252` and `:384` and S1's
docstring at `:255-261` describe each case's own history, and S1's
docstring says the older fragment stays out. `publish_release_note.py:70`,
`.github/PULL_REQUEST_TEMPLATE.md:16` and `README.md:692` say an outside
contribution or a pull request carries no fragment. The rest of both
outputs are other uses of "added", "goes red on", "fails for a" or "built
from", each opened in its output line. Among them are
`evals/scripts/seed_defects.py:143`, `seal/follow-up.md:47`,
`.github/scripts/issue_claims_check.py:27`,
`skills/code-review/orchestration.md:60` and `:288`, `skills/verify/SKILL.md:206`
and `:377-378`, `skills/implement/scripts/seal.py:470`, the workflow
comments at `close-issues-on-release.yml:55`, `hygiene.yml:51` and
`templates/setup/hygiene.yml:84`, the theme cases at
`test_publish_release_note.py:313`, `:328` and `:709-710`, and lines of
the hygiene, routing, worktree-guard, arm-check, mutation-check,
seal-stamp, broad-gate and gate-range tests.

The answer's search of `docs/` was re-run: it printed nothing, git grep
exit 0 and grep exit 1 (executed). The policy root keeps the gather until
the settle writes the frame's `## Rule changes`, and the four `to:` texts
that settle writes now carry the skip.

The two recorded searches exclude `seal/threads/`, so this round searched
the work item's own `frame/`, `changelog.md` and `gaps.md` (executed:
`git grep -n -i -E "fragment"` over those paths, piped to a `grep -i -E`
for "added", "range", "commits", "no fragment", "goes red", "fail",
"refus", "empty", "every fragment", "by construction", "reads", "built",
"builds", "from the history", "after the previous" and "previous"). Each
hit that states the selection carries the skip:
`changelog.md:3` ("reads every fragment the commits after the previous
version tag added and that tag does not already hold"), *Scope* item 1 at
`design.md:29-34`, *Data & interfaces* at `:158-164`, the ten coordinates
above, the `to:` text for `docs/the-record-layout.md` at `:317-322`,
`frame/questions.md:8-10` and `gaps.md:14`. These hits state no selection
rule, re-derived this round. `design.md:13`, `:203` and `:494` and
`gaps.md:5` say only that the note is built from the fragments.
`design.md:330-333` speaks of one fragment as it stands at the tag.
*Verification* rows S1 at `design.md:137` and S5 at `:141` each state one
history, and each is still true of the code, as round 3 found.
`plan.md:37-40` says how each fragment is read, not which are read.
`plan.md:46-48` gives a widened range, where the lower tag is an older one
that holds none of the skipped release's fragments, so the note carrying
both releases' fragments is still true. `plan.md:57` labels the chosen
alternative, and `:58` names a rejected one; round 3 kept `:57` for the same
reason. The remaining hits name the removed gather, the Removes and
reworded-sentence tables, the theme and the section function.

A third search, written this round, looked for phrasings neither recorded
search reaches: "release's fragments", "range's fragments", "fragments of
the range", "since the previous" and "previous tag" over the tree, round
records and the released files excluded (executed). Beyond the lines the
searches above reached, it found six. `publish_release_note.py:185` is the
range function's docstring naming the case with no previous tag.
`design.md:142` and `:154` define the previous tag. `phase-1.md:42` is the
phase record's account of a measured miss.
`test_publish_release_note.py:304` is S1's assertion message that the older
fragment stayed out, and `:390` is A3's docstring, which states the skip.
None of the six states the selection without the skip. No sentence stating
the selection without the skip is left in the tree outside the round
records.

confirms: none
The fix range's record edit is the fix pass's two lines.
`git diff 572105e5..5aa3f0d4` on `round-3.md` changes the `verdict:` line
to `fixed 5eebfaf1` and fills the `answer:` line, and nothing else
(executed). `5eebfaf1` touches three paths that finding 1's `location:`
names (executed: `git show --stat`). All three commits are authored by the
repository owner's commit identity (executed: `git show --format`).

confirms: none
The narrow verification for this round passed. Executed in the clone: the 7
modules under `tests/` that `git grep -l` finds naming
`publish_release_note`, `publish-release.yml` or this work item's id ran with
`bin/test -q`: 103 passed, exit 0. `bin/seal layout --check` exited 0, with
160 files read and 0 refused. `bin/seal rules --check` exited 0, with all
266 check lines in 55 rule files holding. This is not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| S11: every released version's note holds its file after the republish of the 26 | `frame/plan.md` phase 5 row | the orchestrator, in phase 5 |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| The full suite, the repository-wide lint and the typecheck: unverified. The fix pass's answer reports `ruff check` and `ruff format --check` at exit 0; this round did not run either | the branch at `5aa3f0d4` | the orchestrator, at `seal gate`, before the sealer is spawned |
| Step 3 of the update skill run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

## Probes

| Command | Result |
|---|---|
| (A) `git grep -n -i -E 'added' -- ':!seal/threads/' ':!docs/' ':!.test_durations' \| grep -i -E 'fragment\|range\|commits? (after\|in)\|release.s commits'`, the fix pass's search | 22 lines; both exits 0; each hit judged in the confirmation of round-3#1 |
| (B) `git grep -n -E "release's commits\|commits (after\|in) (the\|that)\|range('s)? (added\|commits)\|no fragment\|no changelog fragment\|fragments? the (range\|release)\|built from the\|builds it from\|from the fragments\|fails for a\|goes red on" -- ':!seal/threads/' ':!docs/' ':!.test_durations'`, the fix pass's search | 51 lines, exit 0; each hit judged in the same confirmation |
| `git grep -n -i -E "fragment" -- docs \| grep -i -E "added\|range\|release's commits\|no fragment\|goes red\|fails"`, the fix pass's search of the policy root | nothing printed; exits 0 and 1 |
| `git grep -n -i -E "fragment"` over the work item's `frame`, `changelog.md` and `gaps.md`, piped to the `grep -i -E` the confirmation names | 89 lines; each hit that states the selection carries the skip |
| `git grep -n -i -E "release.s (changelog )?fragments\|range.s fragments\|fragments? (of\|in) the (range\|release)\|since the previous\|previous (version \|vX\.Y\.Z )?tag"`, round records, `.test_durations`, `changelog/` and `CHANGELOG.md` excluded | 29 lines, exit 0; six coordinates beyond the searches above, none stating the selection without the skip |
| `bin/test -q` over the 7 modules the last confirmation names | 103 passed, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

No probe file was written. `git status --short` in the clone printed
nothing after the runs.
