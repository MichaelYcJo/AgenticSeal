# Design: 1793419350-a-prefix-states-what-a-change-is (#1199)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1199 as folded on 2026-10-31, comments none (executed, `gh issue view 1199 --json body,comments`) | The owner's decisions: milestones keep their numbers and order; the prefix states what the change is and is never lowered to fit a number; a `feat:` in a patch-numbered milestone pushes it and every later one forward; `chore:` is no default; the line between `feat:` and `refactor:` is drawn here, with #1167 and #1198 as its first cases. The milestones stand frozen at 74 = 0.26.0, 75 = 0.26.1, 76 = 0.26.2, 70 = 0.27.0 until this lands. |
| `docs/branch-and-release.md` *Work accumulates on a release branch*, the paragraph opening **The version is named at the cut** (read) | Today it lets a release move either way, "a minor become a patch or a patch become a minor". The owner's decision keeps one direction, forward. It is the push rule's home, changed through `## Rule changes`. |
| `skills/commit-pr-convention/SKILL.md` *Commit messages* (read) | Its table says `feat:` "behaviour that did not exist now does", `refactor:` "same behaviour, different structure", `docs:` "documentation or comments only", `chore:` "release preparation, configuration, dependencies". Nothing says a skill's or an agent's text is behaviour, and nothing says what `chore:` is not. Its next paragraph, "A repository's own log outranks the table", lets a log full of `chore:` teach `chore:`. *First, check the title against the history* says the same of titles. |
| `docs/issues-and-milestones.md` *An issue is titled like a commit* (read) | An issue takes the skill's vocabulary. Its one good example is `chore: the round cap is a ceiling and has been spent like a budget`, a change to a review-chain rule, which the new table never calls `chore:`. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*, at the base and as #1167's phase 1 rewrote it on its branch (read, `git show` of `chore/1167-judgment-where-meaning-is-the-question`) | A script holds a gate only on a fact it reads exactly, and names as not read a line that looks like its form and is not. A mechanism stays while what it caught outweighs what it costs. The refuse-or-report call below is judged against both sentences. |
| `CONTRIBUTING.md` *What a change to a gate must carry*, on #1167's branch (read) | This work adds a refusal, so its pull request answers the failure direction, the prompt budget, platforms, what it removes and what it reads. *Data & interfaces*, *What the release check owes `CONTRIBUTING.md`*, holds the answers for the orchestrator's part of the body. |
| `.github/scripts/release_completeness_check.py#main` and `#subjects_since` (read) | The release pull request's step already reads the release branch's own commit subjects since it left `main`, and the version from the head branch's name through `label_merged_on_release_branch.py#version_of`. It returns early, at exit 0, where the milestone does not exist, before it reads any subject. |
| `.github/workflows/hygiene.yml`, job `release`, step `the milestone this release claims is the work it carries` (read); the `main` ruleset requires `lint` and `release` (executed, `gh api repos/{owner}/{repo}/rulesets/<id>`) | The step runs only where the base is `main`. Its job is a required check, so a rule whose test drives it names a marker on its `check:` line (`skills/settle/SKILL.md` *A rule has one shape*). `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py#hygiene_step` finds the step by the name's opening words, `- name: the milestone this release claims`. |
| What the reading would have caught (executed, for each pair of consecutive `v*` tags: `git log --no-merges --format=%s <prev>..<tag>`, counting subjects that open `feat`) | 37 tags from v0.8.1 to v0.25.1 are patches, and 14 of them carried at least one `feat:` subject: v0.8.2, v0.9.2, v0.9.5, v0.11.1, v0.11.3, v0.13.1, v0.15.2, v0.15.3, v0.15.7, v0.18.1, v0.22.4, v0.23.1, v0.24.1, v0.24.2. #653's body says the owner approved "`feat:` makes a minor" on 2026-09-02 and that no workflow ever held it (read). |
| When a release pull request opens (executed, `gh pr list --base main --state all --limit 4 --json number,headRefName,createdAt,mergedAt`) | #1194, #1188, #1175 and #1161 each opened between 1 and 14 minutes before their merge. `docs/release-checklist.md` *5. The release pull request* says it opens with the release's first work item, so in practice a refusal there lands at the end of the release, not at the squash that caused it. The plan's failure scenario carries this. |
| Prefix spellings on `main` (executed, `git log origin/main --no-merges --format=%s`, counting subjects opening a lowercase word followed by `(` or `!`) | 0. Scoped forms such as `feat(agents):` exist only on unmerged branch commits. The reading counts the one spelling `feat:` and names any other spelling of the word as not read. |
| Release branches on `origin` (executed, `git ls-remote --heads origin 'release/*'`) | Only `release/v0.25.2` and `release/v0.26.0`. Pushing milestones 75, 76 and 70 forward renames milestones and recuts no branch. |
| `.claude-plugin/plugin.json` on the base reads `0.25.2` (executed, `grep`) | #1167's frame *Scope* item 14 moves it to `0.26.0` in its last phase, and #1167 merges first (`frame/plan.md` *Operational impact*). This work leaves `plugin.json` alone. |
| #653 (executed, `gh issue view 653 --json body,comments`) | Its two directions: bump on what an installing repository experiences, and take the number out of the milestone's name. Its comment of 2026-10-31 hands the answer to this work. |
| #1167's frame *Scope* items 11, 12 and 14 (read, `git show` of its branch) | Item 11 adds `## Judgments of the run` to `templates/records/sdd-plan.md`. Item 12 adds *The judgments* to `seal settle`'s dry run. Item 14 calls the work a feature. Items 1 to 10 move judgments from scripts to agents. |
| #1198 (executed, `gh issue view 1198`) | It adds a marked-block record format and a standard process that assembles, disassembles and stacks it, after a review that decides build or drop. It sits in milestone 75, `release: 0.26.1`, titled `feat:`. |
| #1167's `## Rule changes`, the `add` of `docs/what-a-script-gates.md`, row `hygiene's other steps` (read) | Table A lists what each gating check reads. Once this work's reading lands, the row's *Reads* and *Unread* cells are stale, so `## Rule changes` below changes that row. |
| `tests/behaviour/test_release_hygiene.py#ILLUSTRATIVE_VERSION` (read) | A loaded document may name `1.2.3` and versions already tagged, and no other. The policy text below names versions as `X.Y.Z`. |

## Scope

In. Each item is one decision of this frame; `frame/plan.md`'s Delivers cell cites them by number.

1. **A prefix is the writer's judgment of what the change does for whoever meets it, and the skill guides that judgment and asks for its grounds.** `skills/commit-pr-convention/SKILL.md` *Commit messages*: the table and the sentences under it are rewritten in place to *Data & interfaces*, *The classification* (reframed after round 3): each kind with its meaning and examples, the precedence, and the clarifications. A change's own tests and its work item's records never decide its prefix. Text a party reads and acts on, such as a skill, an agent definition, a template a party fills or a hook's message, is behaviour, so a change to it is never `docs:` and never `chore:`. An effect is counted once, by the change that decided it. *Pull request bodies* gains the grounds sentence the orchestrator writes. An issue's title takes the prefix the pull request that closes it will take, chosen by the same table, so no issue is filed `chore:` by default. The prefix states what the change is and is never chosen to fit a release number. The skill names no version and no file of this repository: it ships to repositories whose versioning is their own.
2. **A repository's log decides a prefix's spelling, never which row a change takes.** In the same skill, the paragraph "A repository's own log outranks the table" is rewritten in place. The log still outranks the table on how a prefix is spelt and on a prefix the table lacks. Which row a change takes is the table's, because a log written by default teaches the default. *First, check the title against the history* gains one sentence: the comparison is of a title's shape and language, and the prefix is the table's.
3. **The release pull request refuses a patch-numbered release whose own subjects carry a `feat:`.** `.github/scripts/release_completeness_check.py` gains the reading in *Data & interfaces*, *The release check*, in the existing step. The step's name keeps its opening words and adds the second question. The module docstring states the new direction beside the four it has. The cases go in `tests/github/test_release_completeness_check.py` and carry `@pytest.mark.rule("a-patch-carries-no-feat")`. Each is seen red (contract rule 15).
4. **The policy root's changes are `## Rule changes` below**, written at the settle: the push rule and the version each prefix gives, an issue's prefix and the moment a push happens, the example title, and #1167's Table A row.
5. **The changelog fragment.** `changelog.md` holds the table and the refusal under `### Changed` and `### Added`, and one `### Process changes` row each for "an issue and a pull request take their prefix by the table, never `chore:` by default" and "a `feat:` in a patch-numbered milestone pushes the milestones forward".

Out.

- **Retitling issues and pushing the milestones.** Agents post nothing (contract rule 6), and the owner applies the result once, after this lands. The orchestrator's acts after the merge are `frame/plan.md` *Operational impact*.
- **Closing #653.** The answer is *Data & interfaces*, *#653*. The pull request body carries `Closes #653` beside `Closes #1199`, and the release closes both.
- **Opening the release pull request earlier.** The checklist already says it opens with the first work item. The practice measured above differs, and changing it is not what this issue asks. The refusal is correct at either moment.
- **A reading at each feature pull request into a patch-numbered branch.** `frame/plan.md` *Alternatives considered* A3.
- **Edits to `agents/crafter.md`, `skills/implement/orchestration.md` or `skills/code-review/orchestration.md`.** Every writer of a title already reads `skills/commit-pr-convention/SKILL.md`, and #1167's later phases hold those files (`frame/plan.md` A8).
- **The rolling log's title, `chore: flow measurement — after X.Y.Z`.** It is a log a script writes and reads by that exact prefix, not a change (`docs/issues-and-milestones.md` *A rolling log is titled after the version it rolled from*).
- **This branch's name, `fix/1199-…`.** `routing.md` names it, and renaming it breaks the routing declaration. The pull request and the issue take `feat:` by *Data & interfaces*, *The first cases*.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a feat in a patch | Given head `release/v1.2.3` whose subjects since `main` include `feat: a thing (#10)`, when the step runs, then it exits 1 and an `::error::` line names that subject, the version as a patch, and the push: rename this milestone and every later planned one forward, cut the branch again under the new name, and move `plugin.json` in its first pull request | a case on the pure judge, seen red against the code with the refusal removed |
| S2 a feat in a minor | Given head `release/v1.3.0` with the same subject, then it passes and prints one line counting the `feat:` subjects against a minor | a case |
| S3 a patch with no feat | Given a patch whose subjects are `fix:`, `refactor:`, `chore:`, then it passes and prints the count line | a case |
| S4 a spelling the reading does not count | Given a patch whose only feature-like subject is `Feat: x` or `feat(agents): x`, then it passes on this reading and prints that subject as not read | a case |
| S5 no milestone | Given a patch head whose milestone does not exist and a `feat:` subject, then the milestone reading still warns that it verified nothing, and this reading still refuses | a case through `main` with the reads stubbed |
| S6 a hotfix | Given a head that is not `release/vX.Y.Z`, then nothing is judged, as today | the existing case still passes |
| S7 a minor with no feat | Given head `release/v1.3.0` with no `feat:`, then it passes and says the release ships under the minor it was named, since a milestone is never pulled back | a case |
| S8 the two named cases | Given the classification, when a writer titles #1167 and #1198, then both take `feat:`, each for the part *The first cases* names | the proofer reads the rewritten table against *The first cases* |
| S9 an issue for a gate change | Given a new issue whose change alters what a check refuses, then the table gives `feat:`, `fix:` or `refactor:`, never `chore:` | the proofer reads the rewritten table |
| S10 the writer's grounds and the proofer's reading | Given the rewritten *Commit messages* and *Pull request bodies*, when the proofer reads the section, then each sentence has one reading (`skills/writing-style/SKILL.md`, the rules for text an agent reads), no sentence states a decision procedure or a claim that two writers always agree, each *Worked examples* row's prefix and grounds follow from the text, and *Pull request bodies* asks the orchestrator for one sentence of grounds | the proofer reads the text and the examples; the sealer reads the grounds sentence of this work's own pull request body at its seal |

## Data & interfaces

### The classification

Reframed after round 3. The first frame decided by the first row that fits, and the reframe after round 2 by the highest kind among a change's parts. Both were decision procedures meant to give two writers one answer. Round 2 found 3 findings in the first, and round 3 found 5 in the second (`trail/rounds/round-3.md`), and each close opened the next edge. Whether a change is new, corrected, faster or the same reached another way is a judgment of meaning, and `skills/core/SKILL.md` *The first value: efficient development through the workflow* says the workflow delegates that judgment and does not re-encode it as grammar. So the classification is guidance a writer weighs, and the writer states its grounds where a party reads them. The one exact mechanism is the release check, which reads `feat:` in its one spelling against the version (*The release check*).

**A prefix is the writer's judgment of what the change does for whoever meets it after the merge, a user or a party working on a later change, and the writer states its grounds.** The skill gives each kind its meaning and examples, the precedence, and the clarifications below. They are what the writer weighs, not steps it executes.

| Kind | What whoever meets the change meets | Examples |
|---|---|---|
| `feat:` | something new to use or to meet | a command; a record format; a refusal on a rule the change itself states; a thing removed that its users must now work around |
| `fix:` | behaviour that was wrong against a rule the tree stated before the change, now matching it | a check that let through what its rule refused; a skill sentence that contradicted the policy it cites |
| `perf:` | the same behaviour, sooner or at less cost | a file parsed once instead of once per row |
| `refactor:` | the same kinds of outcome, reached another way | a judgment moved from a script to an agent; a gate retired because what it caught did not outweigh its cost; a skill nobody used, removed; a section moved to another file |
| `test:` | nothing outside the repository's own tests | a case added or corrected, even one that refuses where the suite gates the merge |
| `docs:` | text nobody acts on | a README's explanation; a comment |
| `chore:` | upkeep that changes nothing anyone meets | the version move; the changelog fold; a dependency pin that changes nothing met; a work item's records committed alone; a settle that writes the rule changes released work items stated |

The clarifications, each one sentence in the skill:

- **Precedence.** Where a change does more than one of these, its prefix is the one highest in the table, because whoever meets it meets the largest change, and a release reads any `feat:` as at least a minor.
- **A change's own tests and its work item's records never decide its prefix.** A speed-up with the case that pins it is `perf:`, and a README edit with the case that pins its words is `docs:`.
- **Text a party reads and acts on is behaviour.** A change to a skill, an agent definition, a template a party fills or a hook's message is never `docs:` and never `chore:`. A work item's own records describe their change and leave with it, so the previous clarification, not this one, governs them.
- **"Before the change" is the branch the change merges into.** A rule stated only in the change's own work item, such as its frame, belongs to the change, so a commit that builds it takes the kind its pull request takes.
- **An effect is counted once, by the change that decided it.** A settle that writes a rule change a released work item stated is `chore:`. A section it rewrites that no released work item decided is that rewrite's kind.
- **The writer states the grounds.** The orchestrator's part of the pull request body says in one sentence why the title takes its prefix, and names the kind that came closest where one did. `agents/sealer.md` step 4 reads that part against the design and the diff (read), so a prefix the change does not bear out is a disagreement the sealer names. An issue's title takes the prefix of the pull request that closes it and is retitled with it.

What this leaves open, stated as limits:

- Two writers can still weigh a close case differently. The grounds sentence puts the weighing where the sealer reads it, and a review of the skill text holds each sentence to one meaning, but no procedure makes the two agree.
- A `feat:` titled as another kind passes the release check, which reads the title and not the change. The grounds sentence and the sealer's reading are what meet it.

### Worked examples

The frame's own judgments, each with its grounds. They are examples for the writer and for the review, not a test the skill's text must pass by grammar.

| Case | Prefix | Grounds |
|---|---|---|
| #1167 | `feat:` | Items 11 and 12 add a record section and a reading in the settle's dry run, which are new to meet. Items 1 to 10 alone would be `refactor:`, and precedence gives the higher |
| #1198 | `feat:` | a record format and the commands that assemble, disassemble and stack it |
| #1199, this work | `feat:` | a refusal on the push rule this change states, and a prefix rule writers now meet |
| a test with the fix it pins | `fix:` | the test is the change's own |
| a dependency bump that changes nothing met, with its records | `chore:` | |
| a work item's records alone | `chore:` | |
| a speed-up with its case and records, as `97e29b7a` | `perf:` | its case and records never decide |
| a test change with `.test_durations` and its records, as `8cb58904` | `test:` | no one outside the suite meets the corrected case |
| a settle that writes released rule changes only | `chore:` | counted once, by the released work items |
| a settle that also rewrites guidance no released work item decided | the rewrite's kind | the rewrite is the settle's own effect |
| a README edit with its changelog fragment | `docs:` | |
| a case that refuses, added to the suite alone | `test:` | the suite is the repository's own tests, whether or not it gates the merge |
| a README edit with the case that pins its words | `docs:` | its own test never decides |
| a gate retired with nothing in its place; unused skills removed, as in `e391ea04` | `refactor:` | the outcomes its users met are reached without it, or nobody used it |
| a command users ran, removed | `feat:` | its users meet something new: they must work around it, and a release that asks them to act is a minor (*#653*) |
| a build commit on a work item's branch after its frame | its pull request's kind | the frame belongs to the change |
| a dependency bump that corrects a defect users met | `fix:` | |
| a skill's section moved to another file, its instructions unchanged | `refactor:` | |

### Round 3's findings under this design

Each finding of `trail/rounds/round-3.md` is answered by phase 3's rewrite of the skill, as follows.

| Finding | Becomes | Where |
|---|---|---|
| 1, records `chore:` by the row and never `chore:` by the behaviour paragraph | absorbed: the behaviour clarification leaves a work item's records to the own-tests-and-records clarification | *The classification*, the second and third clarifications |
| 2, a README with its pinning case becomes `test:` | absorbed: a change's own tests never decide its prefix, and no order among `test:`, `docs:` and `chore:` is drawn | the second clarification; the example |
| 3, a removal fits no kind | absorbed as examples, with the frame's judgment: a removal is judged by what its users now meet, `refactor:` where they meet the same outcomes or nobody used it, `feat:` where they must work around it | the `feat:` and `refactor:` examples; *Worked examples* |
| 4, "a gate" takes in a case the suite runs | absorbed: the behaviour clarification names text a party acts on and no gates, and the `test:` example names a refusing case where the suite gates the merge | the `test:` row; the third clarification |
| 5, "the base" undefined | absorbed: before the change is the branch it merges into, and the change's own frame is the change's. A limit stays: the commits already on this branch, `c6ed2331` `feat:` and `05b716f7` `fix:`, keep their subjects, and the squash takes the pull request's title | the fourth clarification |

### The version each prefix gives, and the push

This repository's rule, in `docs/branch-and-release.md` through `## Rule changes`. A release carrying a `feat:` is a minor, `X.Y.0`. Every other prefix fits a patch. The push renames the milestone that received the `feat:`, and every later planned `release:` milestone, one step each. Each keeps the step it had from the milestone before it: the pushed patch becomes the next minor, a patch after a minor stays a patch, and a minor stays a minor. Applied to today's names, 75 `0.26.1`, 76 `0.26.2` and 70 `0.27.0` become `0.27.0`, `0.27.1` and `0.28.0`, which is the shape of the two renames of 2026-10-31 (milestone 74's description, read). A milestone is never pulled back. A minor that ends up with no `feat:` ships as the minor it was named, because the owner's decision keeps numbers and order, and a pull-back renames every later milestone for no new content.

The push happens at the cheapest moment the `feat:` is known: when an issue titled `feat:` is filed into, or moved into, a patch-numbered milestone, or when a pull request takes `feat:` where its issue had another prefix. The release check is the backstop for what those moments missed.

### The release check

In `.github/scripts/release_completeness_check.py`, beside `judge`:

- A pure function takes the version and the subjects and returns `(lines, failed)`. A subject counts where it opens with `feat:` exactly. A subject whose first word, case folded and cut at the first `(`, `!` or `:`, is `feat` and that does not open `feat:` is printed as `not read: <subject>`, and it changes no exit code. No spelling list is kept (`skills/core/SKILL.md` *The rule a mechanism is kept against*, as #1167 rewrites it).
- The version is a patch where its third number is not `0`. A patch with one or more counted subjects fails, and the `::error::` line names each subject and the push, citing `docs/branch-and-release.md` *Work accumulates on a release branch*. Every run prints one line with the count and whether the version is a patch or a minor. A minor with no `feat:` prints that it ships under the minor it was named.
- `main` reads the subjects once and hands them to both readings. This reading runs before the early return for a milestone that does not exist, and the process exits 1 where either reading failed. A head that is not `release/vX.Y.Z` still judges nothing.
- No input is added, so the step's `env:` and the boundary case in `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py` stay as they are.
- The step's name becomes `the milestone this release claims is the work it carries, and a patch carries no feat:`, keeping the words `hygiene_step` finds it by.

A reverted `feat:` still counts, as a reverted squash still counts toward D (the module docstring, read). No release here has reverted a squash. The repair is the same push, and a minor with nothing new is harmless.

### What the release check owes `CONTRIBUTING.md`

- **Failure direction.** It blocks more. A wrong deny exists only for a reverted `feat:`, and it costs a minor number. A wrong allow ships a minor's content under a patch number, which 14 of the 37 patches since v0.8.1 did.
- **Prompt budget.** Zero questions.
- **Platforms.** Pure Python on the Linux runner, with no process inspection.
- **What it removes.** Nothing, and `## Removes` says why.
- **What it reads.** The release branch's own commit subjects in the one spelling `feat:`, and the version in the head branch's name. It names a subject that spells the word otherwise as not read. Whether a subject's prefix states what the change is, is judged by the subject's writer, the orchestrator titling the pull request, against `skills/commit-pr-convention/SKILL.md`.

### The first cases

- **#1167: `feat:`.** Its Scope items 1 to 10, taken alone, are `refactor:`: they move judgments from scripts to agents and rewrite sequences as guidance, and nobody gains anything to use. Items 11 and 12 add a record section, `## Judgments of the run`, and a reading, *The judgments* in `seal settle`'s dry run, which are new to meet. By the precedence, the change takes the highest of what it does. This is the frame's judgment, and it departs from the owner's note in the issue that #1167 is "strictly more `refactor:` than `feat:`". The note is true of its bulk. The precedence weighs what a reader meets, not which part is larger, and a `feat:` titled under another kind is hidden from the release reading. #1167 would be `refactor:` only if items 11 and 12 moved out of it into a change of their own. Milestone 74 stays `0.26.0`. The issue's title, `chore:` today, takes `feat:`.
- **#1198: `feat:`.** It adds a record format and the commands that assemble, disassemble and stack it. Its title already says so. It sits in 75, a patch, so 75, 76 and 70 are pushed when the result is applied. If its review decides to drop the build, 75 is not pulled back.
- **#1199, this work: `feat:`.** It adds a refusal on a rule it states, the push. The issue's title, `fix:` today, takes `feat:`. Milestone 74 is a minor, so nothing moves.

### Where this meets #1167

#1167 runs in parallel. This work's pull request opens only after #1167's has merged into `release/v0.26.0`, and the release branch is merged into this one before the broad gate (`frame/plan.md` *Operational impact*). No file this work edits is one #1167 edits: its diff from `f80f48e6` touches neither `skills/commit-pr-convention/`, `docs/`, nor `.github/` (executed, `git diff --stat f80f48e6 chore/1167-judgment-where-meaning-is-the-question -- <those paths>`, empty). Two overlaps are of meaning, not of files:

- **#1167's Table A.** The last item of `## Rule changes` changes a row of `docs/what-a-script-gates.md`, which #1167's design adds. The settle applies designs in merge order, and the merge order above is what makes it write that document from #1167's design before this row. Its `from` is the row as #1167's branch held it when this frame was read. If #1167 changes the row before it merges, this `from` is history, and the settling session reads both designs whole.
- **The core's script sentence.** The release check names a near spelling as not read, which is the rule #1167's phase 1 wrote into `skills/core/SKILL.md`. The merge of the release branch into this one brings that sentence into the tree before the broad gate and the review of the build's last state, as `docs/release-checklist.md` *0. Before starting* allows for a branch that needs what the release branch holds.

### #653

#653 closes against the owner's decision of 2026-10-31.

- **Take the number out of the milestone's name: not taken.** Milestones keep their numbers (issue #1199, read).
- **Bump on what an installing repository experiences: folded into the classification.** A change that makes an installing repository meet a refusal or a step on a rule the change states is `feat:`, a minor. A refusal that enforces a rule already stated is `fix:`, and a refusal that loosens is `refactor:`, both patches. So #653's minor list holds, and the version stays readable off the subjects, which #653 itself requires. One item of #653's patch list is not kept: "a new capability nobody has to act on" is `feat:` and a minor, because the owner's decision makes a `feat:` push the number whoever has to act.

## Rule changes

- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: **The version is named at the cut.** A release's milestone, `release: X.Y.Z`, names the version before its first work item starts, and the branch is cut as `release/vX.Y.Z` for it. A release whose content changes the answer, a minor become a patch or a patch become a minor, is cut again under the new name from the old branch, and the new branch's first pull request moves `plugin.json` to the new version.
  to: **The version is named at the cut, and a `feat:` pushes the milestones forward; the prefix is never lowered to fit the number.** A release's milestone, `release: X.Y.Z`, names the version before its first work item starts, and the branch is cut as `release/vX.Y.Z` for it. A release that carries a `feat:` is a minor, and every other prefix fits a patch; `skills/commit-pr-convention/SKILL.md` *Commit messages* says which change takes which prefix. When a `feat:` lands in a milestone numbered as a patch, that milestone and every later planned `release:` milestone are renamed one step in one act, each keeping the step it had from the milestone before it, and every description is rewritten for the new numbers. It lands when an issue titled `feat:` is filed into the milestone or moved into it, or when a pull request takes `feat:` where its issue had another prefix. A release branch already cut is cut again under the new name from the old one, and the new branch's first pull request moves `plugin.json` to the new version. A milestone is never pulled back: a minor that carries no `feat:` ships as the minor it was named. The release pull request refuses a patch-numbered release whose own commit subjects carry a `feat:`, and names each one. The reading is exact, and the rule it holds was approved on 2026-09-02, held by nothing, and broken by 14 of the 37 patch releases from v0.8.1 to v0.25.1.
    check: a-patch-carries-no-feat
- add
  file: docs/issues-and-milestones.md
  section: An issue is titled like a commit
  to: **An issue takes the prefix the pull request that closes it will take, by the same table, and `chore:` is never its default.** A title read in the tracker, the milestone and the release note says what kind of change is coming, and a `chore:` on a change to what a party does makes a design change read as housekeeping. Where the frame or the build finds the change is of another kind, the issue is retitled when the pull request is. A `feat:` filed into, or moved into, a milestone numbered as a patch pushes the milestones forward at that moment (`docs/branch-and-release.md` *Work accumulates on a release branch*).
    check: none reader: the orchestrator at each filing and each milestone move
- change
  file: docs/issues-and-milestones.md
  section: An issue is titled like a commit
  from: good   chore: the round cap is a ceiling and has been spent like a budget
  to: good   fix: the round cap is a ceiling and has been spent like a budget
- change
  file: docs/what-a-script-gates.md
  section: The checks
  from: | hygiene's other steps: `issue_claims_check.py`, the version step, `release_completeness_check.py`, the mode step, the READMEs step | the pull request | the body's closing keywords by GitHub's own grammar; `plugin.json`; the milestone through `gh`; commit subjects' `(#N)`; two files | the body is reported at exit 0, never failed; the rest refuse on the fact read | none |
  to: | hygiene's other steps: `issue_claims_check.py`, the version step, `release_completeness_check.py`, the mode step, the READMEs step | the pull request | the body's closing keywords by GitHub's own grammar; `plugin.json`; the milestone through `gh`; commit subjects' `(#N)` and their `feat:` prefix in that one spelling; the head branch's version; two files | the body is reported at exit 0, never failed; a subject spelling `feat` otherwise is named as not read; the rest refuse on the fact read | whether a subject's prefix states what the change is: its writer, by `skills/commit-pr-convention/SKILL.md` |

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The pull-back direction, "a minor become a patch" | `docs/branch-and-release.md` *Work accumulates on a release branch* | `## Rule changes` item 1: milestones are pushed forward and never pulled back (issue #1199, the owner's decision). |
| The `chore:` row's unbounded "release preparation, configuration, dependencies" | `skills/commit-pr-convention/SKILL.md` *Commit messages* | Rewritten in place with what `chore:` is not (*Scope* item 1). |
| The log outranking the table on which row a change takes | `skills/commit-pr-convention/SKILL.md` *Commit messages*, the paragraph opening "A repository's own log outranks the table" | Narrowed in place to spelling and to prefixes the table lacks (*Scope* item 2). |
| The first-row rule and the "only", "and nothing else" words of the `test:`, `perf:`, `docs:` and `chore:` rows, as 9944919e wrote them | `skills/commit-pr-convention/SKILL.md` *Commit messages*, the paragraph opening "A change takes the first row that fits" and the table | Replaced in phase 2 by the per-part rule, which phase 3 replaces in turn (next row). |
| The per-part rule, its claim that "the answers exclude one another, so no order is needed", and the table's order as a precedence among parts, as 05b716f7 wrote them | `skills/commit-pr-convention/SKILL.md` *Commit messages*, the paragraphs opening "Each part of a change has one kind" and "The order of the table is the precedence among kinds", and the `feat:`/`fix:` test paragraph | Replaced in phase 3 by the guidance in *Data & interfaces*, *The classification* (reframed after round 3). |
| The sentence that the settle "writes into the policy documents what the released work items' frames already decided", and the two named `chore:` cases it closes | `skills/commit-pr-convention/SKILL.md` *Commit messages*, the paragraphs opening "Text a party reads and acts on is behaviour" and "Apart from those two" | Replaced by *An effect is counted once, by the change that decided it*, in phase 2. |
| The example title `chore: the round cap is a ceiling…` | `docs/issues-and-milestones.md` *An issue is titled like a commit* | `## Rule changes` item 3. |
| No mechanism | | This work adds a refusal and removes none. The reading rides the existing step and script and reuses its two reads, the subjects since the fork and the version from the head branch, so it adds no step, workflow, file or input. Nothing in the tree reads a version against a prefix today: the 2026-09-02 rule was never built (#653, read), so there is nothing to retire in its place. What the refusal would have caught is 14 of 37 patch releases (*Grounding*). |

Framed 2026-10-31 by framer, before the build.
Reframed 2026-10-31 by framer, after round 2.
Reframed 2026-10-31 by framer, after round 3.
