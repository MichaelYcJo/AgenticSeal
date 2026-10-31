# Review round 1: 1793432602-a-feat-moves-to-the-minor-of-its-goal

target: 9588bef7 against origin/release/v0.26.0

This round reads the branch against `origin/release/v0.26.0` (62aab17e):
the frame commits `d560db71`, `ab181e77`, `e380a2cb` and `545d5eb2`, the
build commits `44cf3cdc` and `27fc807a`, and the records commit `9588bef7`.
It is the first round, so no earlier round's coordinates were carried and
every fact below was established here. No `seal/parity.md` is declared, so
the record names no original commit.

The standard is issue #1205's *Done when* beside the frame. The frame
narrowed the first *Done when* item (`frame/plan.md` A3: the error names the
move as owed before the squash and the rename for a `feat:` already
squashed) and added the grounds requirement of A8. Both are recorded in
`frame/plan.md` *Judgments of the run* (`frame/plan.md:44`), so this round
judges the error against A3's reading and not against the issue's wording.

The axes named for this change, beyond the table: the words a person reads
in the refusal and in the minor line; the release note the two fragments
build together; the merge order of the two designs' `## Rule changes` at
the settle; and every other statement of the old rule in the tree.

## Findings

### 1. This work's changelog entry describes the refusal and the minor line as changed from #1199's text, which never shipped, and restates #1199's entry

severity: should
location: `seal/threads/1793432602-a-feat-moves-to-the-minor-of-its-goal/changelog.md:3`
evidence: executed `git grep -n -i -E 'every later planned|pushes the milestones|renamed one step|judge_feat' origin/main -- .`
verdict: open

The claim of absence rests on the grep above. The texts compared were read
at `seal/threads/1793432602-a-feat-moves-to-the-minor-of-its-goal/changelog.md:3`,
`seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:3`,
`trail/phases/phase-1.md:17` and `frame/design.md:32`.

The 0.26.0 release note is built from both fragments together. #1199's
`### Added` entry introduces the refusal in this release, and its rewritten
text already says it "states each repair at the moment it can be made",
with the move before the squash and the rename after it
(`seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:3`).
This work's `### Changed` entry then says, in the same note, "The release
pull request's refusal now names both repairs, each at the moment it can be
made", and "the release check's line for that case now says this is because
the branch was cut under that name". Its bold lead says "so one minor is no
longer made for each `feat:`", and its last sentence says a minor with no
`feat:` "still ships under its name".

Each of the four compares against #1199's text on `release/v0.26.0`, and
that text never reached a release. The grep over `origin/main` (v0.25.1)
found no `judge_feat`, no "every later planned" and no push rule. A reader
of the 0.26.0 note meets the refusal as new in `### Added` and then as
changed in `### Changed`, and "no longer" tells them that releases up to
0.25.1 made one minor per `feat:`. They did not: 14 of 37 patches carried a
`feat:`, which is the opposite. The release note is what a person acts on
after updating, so this is a sentence that tells a person something wrong.

The implementer's account claims the opposite. `trail/phases/phase-1.md:17`
says "The entry does not describe #1199's push as a past rule: the push
never shipped". The entry does not name the push, but "now names both
repairs" and "now says this is because" describe #1199's refusal and minor
line as the past state. *Scope* item 4 (`frame/design.md:32`) asked for four
points, none of them the refusal's text, which *Scope* item 2 puts in
#1199's fragment. The two "now" sentences restate that fragment's content a
second time in the same note.

The class, enumerated by reading the entry whole: "no longer", "now names",
"now says" and "still ships". No other comparative word stands in the
entry. #1199's rewritten entry and process row were read for the same
class and hold none: they state the rule as it ships.

The paste-ready fix replaces line 3 of
`seal/threads/1793432602-a-feat-moves-to-the-minor-of-its-goal/changelog.md`
whole. It keeps every point of *Scope* item 4 and the A8 exception the
phase record added, and drops the refusal's text, which #1199's entry
carries.

```markdown
- **A planned minor is a category with one goal, and a `feat:` that lands in a milestone numbered as a patch moves to the planned minor whose goal it shares (#1205).** A minor milestone's description states the one goal its `feat:`s share, and a patch's description says it builds no `feat:`. Whoever files a `feat:` issue into a patch-numbered milestone, or moves one there, moves it to the planned minor whose goal it shares. The milestones are renamed one step forward only in three cases: no planned minor shares the goal; the work that follows needs the `feat:` before that minor ships, and the renamed milestone's description names that work and says why the minor is too late; or the `feat:` is already squashed onto the patch's branch, where the release pull request's reading counts it even after a revert. Until a release branch is cut, a planned milestone's name follows its goal, and a regrouping renames milestones back as well as forward. Once a branch is cut, its name is never pulled back, so a minor with no `feat:` ships under the name its branch was cut with.
```

answer:

## Confirmations

confirms: none
The refusal's text matches *Data & interfaces*, *The release check's words*
(`frame/design.md:60`) part by part and in the order it gives, at
`.github/scripts/release_completeness_check.py:327-339`: the patch and each
subject; "A feat: makes a minor."; the move before the squash to the
planned minor whose goal it shares; a `feat:` squashed here staying in its
range because a revert still counts; the rename of the milestone and every
later planned `release:` milestone, the re-cut and `plugin.json`; the
citation; and "never lowered to fit the number". It names no force-push and
no ruleset. The claim that a revert still counts was read against
`judge_feat` (`release_completeness_check.py:317`), which counts every
subject opening `feat:` in the range, so a `Revert "feat: ..."` subject
leaves the original counted. The error does not say "where none shares it,
rename" for a `feat:` before its squash; that is the A3 narrowing, recorded
and accepted (read).

confirms: none
The minor line at `.github/scripts/release_completeness_check.py:348-349`
reads "ships as the minor it was named, since its branch is cut under that
name", as the frame gives it (`frame/design.md:61`). The step only runs on
a `release/vX.Y.Z` head, so the branch it names is cut whenever the line
prints, and the sentence is true where it is read (read).

confirms: none
The module docstring's second-question paragraph
(`.github/scripts/release_completeness_check.py:45-60`) names the move and
the rename and ends on the rename for a `feat:` squashed here, as *The
release check's words* asks. `judge_feat`'s own docstring names no repair,
so `gaps.md` *Not done* holds (read).

confirms: none
S1 and S7 pin the new words
(`tests/github/test_release_completeness_check.py:217-245`, `:293-304`).
The crafter's claim that each was red against the old text was settled by
reading the diff, not by a probe: the base's error held neither "before its
squash" nor "stays in its range", and the base's minor line ended "a
milestone is never pulled back", which S7's whole-line equality refuses.
The claimed surviving mutant on "A feat: makes a minor." is pinned at
`:236`. `seal mutate` was not re-run here; its 5 of 5 licenses *tested*,
not *safe*. The four narrow modules passed (`## Probes`). No test was
added, only rewritten, so no group comparison is owed.

confirms: none
S8. The grep run here outside `seal/threads/` returns the six hits the
phase record names. `release_completeness_check.py:52` and `:334` and
`test_release_completeness_check.py:240` state the rename for a `feat:`
already squashed, and `test_release_completeness_check.py:294` states the
bound at the cut. `tests/github/test_label_merged_on_release_branch.py:330`
and `tests/github/test_roll_flow_measurement_issue.py:641` use "the same
push" for a `git push` and state no rule. A wider grep for "one step
forward", "makes a minor" and "never pulled back" found only these lines
and the docstrings of `judge_feat` and the test module, which state that a
`feat:` makes a minor and no repair (executed).

confirms: none
S9. Neither fragment states that every `feat:` in a patch renames the
milestones forward. #1199's second process row
(`seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:14`)
equals *#1199's second process row* in `frame/design.md:68` character for
character (executed, a string comparison), with its source moved to the
owner's correction. The grouping rule, with its three rename cases, is
stated in one entry, this work's; #1199's `### Added` entry states only
the two repairs the refusal prints, as *Scope* item 2 asks. Finding 1 is
about the comparative words in this work's entry, not about S9.

confirms: none
S10, as far as a dry run before the tag can show it. `seal settle
--released-at HEAD` reads both designs as released and shows, in the group
for *Work accumulates on a release branch*, #1199's change before this one;
in *An issue is titled like a commit*, #1199's add and change before this
one; and *A milestone answers when, and takes three shapes* with this
design's operation alone. No pair is reported unordered (executed). Each
`from` was compared with its source: the first equals #1199's `to`, the
second is the last sentence of #1199's `add`, and the third stands in
`docs/issues-and-milestones.md` (executed). The settle after 0.26.0's tag
reads the order again; that run is not this round's.

confirms: none
*Done when*: item 1 as A3 reads it (the confirmations above); item 2, the
two sections #1199 changed, plus a third for item 4, in later merge order;
item 3, the process row; item 4, the third operation of `## Rule changes`
(`frame/design.md:97-101`), whose policy text the settle writes. The
owner's milestone descriptions already state the goals, which the frame
read with `gh` and this round did not re-read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at this branch's head, the full suite, the repository-wide lint and format; the crafter's `unverified` label on it is honest, since `gaps.md` names the orchestrator and no hand-back claims it passed | `seal/threads/1793432602-a-feat-moves-to-the-minor-of-its-goal/gaps.md:7` | the orchestrator, by `seal gate` |
| The rewritten `::error::` line and minor line on a real release pull request into `main` | `.github/scripts/release_completeness_check.py:327-349` | the orchestrator, at the release pull request |
| The order the settle shows after the 0.26.0 tag, read at `--released-at origin/main` | `seal/threads/1793432602-a-feat-moves-to-the-minor-of-its-goal/frame/design.md:83-101` | the settling session after the tag |
| The crafter's 39-module boundary run (3233 passed, 9 skipped) and `seal mutate` 5 of 5, not re-run here | `seal/threads/1793432602-a-feat-moves-to-the-minor-of-its-goal/trail/phases/phase-1.md:11`, `:21` | the sealer, which re-runs a sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_release_completeness_check.py tests/text/test_a_release_cannot_ship_an_untrue_milestone.py tests/behaviour/test_release_hygiene.py tests/github/test_publish_release_note.py -q` | 120 passed, exit 0 |
| `git grep -n -i -E 'every later planned\|pulled back\|the same push\|names what to do: the push' -- ':!seal/threads/'` | six hits, the ones listed under S8 |
| `git grep -n -i -E 'one step forward\|renamed one step\|pushes the milestones\|milestones forward\|makes a minor\|never pulled back' -- ':!seal/threads/'` | the S8 hits plus `release_completeness_check.py:46`, `:311`, `:328` and `test_release_completeness_check.py:18`, `:218`, `:236`, each stating that a `feat:` makes a minor |
| `git grep -n -i -E 'every later planned\|pushes the milestones\|renamed one step\|judge_feat' origin/main -- .` | no hit: the push rule and `judge_feat` never reached a release |
| `python3 skills/settle/scripts/settle.py --released-at HEAD` | exit 0; the three groups as stated under S10, no unordered pair |
| a Python string comparison of each `## Rule changes` `from` against #1199's `to`, #1199's `add` and `docs/issues-and-milestones.md`, and of #1199's process row against `frame/design.md:68` | all four equal or contained, as stated under S9 and S10 |
