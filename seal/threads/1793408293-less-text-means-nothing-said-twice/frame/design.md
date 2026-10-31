# Design: nothing in the tree says that less text means nothing said twice (#1192)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| Ticket #1192, read with `gh issue view 1192 --json body,comments` on 2026-10-31 (executed): no comments | Two *Done when* bullets. The first: the core carries one sentence saying what "less text" means, and nothing in `skills/`, `agents/` or `templates/` holds a net line count as a criterion, with the `git grep` phrasings listed in the work item. The second: the orchestrator's local memory `compact-not-net-negative` is deleted after the merge. The issue's sentence is offered "for example", so its wording is not fixed |
| The owner's answer to Q2 of #1148, PR #1191 comment 6534214778, read with `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6534214778` (executed) | What "less text" means: text that restates another record or document is removed, and what stays says its thing once. A change that grows is kept where what it adds serves a reader. A net line count was never the criterion. The same comment reports word counts and the `tests/` additions as context for a reader, which is the use the new sentence keeps |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*, lines 105-106: "A fact has one source, and every other place links to it." | The home the issue names. The new sentence stands directly after this one, because "nothing said twice" is that sentence's consequence for the size of a change. The core reaches every party and every repository, so the framer drawing a scenario and the proofer raising a finding both read it, and no second copy goes anywhere else |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*: "a reading that is noisy or guessed from words is reported, never used to block" | No test sweeps shipped text for line-count phrasings. Such a sweep matches words, so it could only report, and the enumeration below is that report, made once for this work item (`frame/plan.md` *Alternatives considered*, rows C and D) |
| `docs/the-record-layout.md` *A change writes fragments, never a shared file*, as the unsettled design `seal/threads/1793273065-the-core-reaches-no-users-repository/frame/design.md` *Rule changes* changes it: "A work item whose diff changes `skills/core/SKILL.md`, `CLAUDE.md`, …" | The diff changes the core, so `changelog.md` ends with `### Process changes` and one row in the shape of `templates/records/process.md` |
| `skills/implement/orchestration.md` lines 318-325 and `docs/branch-and-release.md` lines 232-236: the release's first pull request into `release/vX.Y.Z` moves `plugin.json` to that version, in the commit that adds its changelog entry | This is the first pull request into `release/v0.25.2`: `gh pr list --base release/v0.25.2 --state all` returned `[]`, and `origin/release/v0.25.2` is `13dc7c63`, the merge base of this branch (executed). `.claude-plugin/plugin.json` moves from `0.25.1` to `0.25.2` |
| `hooks/lib/core.py#CAP` (10,000 characters) and `tests/hooks/test_core.py#test_the_trees_core_stays_under_the_harness_cap` | The hook prints the core whole only under the harness's cap on one hook's output. Probe P1 below measures the margin |
| Probe P1 (executed): `python3 -I test_tmp_core_len.py <clone>` in a `git clone --no-local` of this repository at `1dd83935` under `<scratchpad>/1793408293-less-text-means-nothing-said-twice/frame/`, calling the clone's `hooks/lib/core.py#output` before and after inserting the sentence of *Scope* item 1 after line 106's anchor; the directory was removed afterwards | `before 6431 after 6653 added 222`, against `CAP` 10,000. The sentence leaves 3,347 characters of margin |
| `skills/settle/SKILL.md` *Rule changes*: a `file` is a top-level `.md` file of the policy root | The core is a skill, not a policy document, and the pull request edits it in place. No document under `docs/` states what less text means or holds a line count as a criterion (*Data & interfaces*), so `## Rule changes` holds the no-change block |
| `docs/the-reader-registry.md` *A frame names what its work removes*, and `agents/framer.md`'s rule that a design adding a rule names what it takes out | The sentence is a rule. `## Removes` holds the no-change block, and its `why` says why nothing in the tree goes |
| The 0.25.1 release's `### Process changes` table (`gh release view --json body`, executed) and the three unsettled fragments under `seal/threads/` (read) | No row there states what less text means. #1148's rows remove copies ("each fact of a work item has one record"), which is the reading the owner's comment confirms; none states a size criterion |
| Milestone 74's description (read, from `gh issue view 1192 --json milestone`) | #1167 rewrites how checks and rules are written in the same release. This work item adds one sentence and touches no check, no `check:` line and no rule's shape |

## Scope

In:

1. **The sentence.** `skills/core/SKILL.md` *The rule a mechanism is kept against* gains one sentence, directly after "A fact has one source, and every other place links to it.":

   > Less text means nothing said twice, not fewer lines: a change that grows is kept where what it adds serves a reader, and the lines a change adds against those it removes are reported as context, never held as a criterion.

   The text departs from the issue's example in one clause. The issue's "a line count is reported as context, never held as a criterion" would read, word for word, against three limits on what one reader can take in, which are criteria by design: `hooks/lib/core.py#CAP` with its test, the 10,000-character cap on a `Stop` hook's message in `docs/the-review-record.md` line 493, and the 806,241-token bound on a resumed crafter in `skills/code-review/orchestration.md` line 30. The sentence names the count the owner ruled out, a change's additions against its removals, and leaves those limits standing. A builder who rewords the sentence keeps its three parts (nothing said twice, a growing change kept where it serves a reader, a change's net count held as context only), keeps that scope, and records the new text and why in its phase record.
2. **The fragment.** `seal/threads/1793408293-less-text-means-nothing-said-twice/changelog.md` with a `### Changed` entry and a `### Process changes` table holding one row, in the shape of `templates/records/process.md`. The row's change is the sentence's meaning, its why is #1148's round-1 finding 6 and Q2, and its source is the owner's comment of *Grounding*.
3. **The version.** `.claude-plugin/plugin.json` moves to `0.25.2` in the commit that adds the fragment.

Out:

- **Deleting the orchestrator's local memory `compact-not-net-negative`.** The issue's second *Done when*. The file is outside this repository, and the orchestrator deletes it after the merge, when the core is its one source. It has no scenario and no phase.
- **#1148's records that carry the old reading**: its `frame/design.md` S10, round 1's finding 6, `frame/questions.md` Q2 and `gaps.md` *Not done*, all under `seal/threads/1793343707-each-document-serves-one-reader/`. The records are not amended after the guarantee, the owner's comment is their answer, and they leave with their directory at the settle after 0.25.1.
- **Any change to shipped text other than the core.** The enumeration (*Data & interfaces*) found no shipped sentence or script that holds a change's net line count as a criterion, so nothing else is rewritten.
- **A test that pins the sentence, or one that sweeps for line-count phrasings.** `frame/plan.md` *Alternatives considered*, rows B to D.
- **#1167's rewrite of checks and rules**, which shares the milestone.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The core says what less text means | Given `skills/core/SKILL.md` at HEAD, when a party reads *The rule a mechanism is kept against*, then the sentence after "A fact has one source, and every other place links to it." says that less text means nothing said twice and not fewer lines, that a change that grows is kept where what it adds serves a reader, and that a change's added lines against its removed lines are context and never a criterion | `git grep -n -F 'Less text means nothing said twice' -- skills/core/SKILL.md` gives one line, the line after the anchor; the proofer reads the sentence for its three parts |
| S2 The sentence leaves a reader's limit standing | Given the sentence, when it is read against the three limits *Scope* item 1 names, then none of them reads as a line count held as a criterion against the sentence, because each bounds what one reader can take in and not what a change adds against what it removes | The proofer reads the sentence against `hooks/lib/core.py#CAP`, `docs/the-review-record.md` line 493 and `skills/code-review/orchestration.md` line 30 |
| S3 No shipped criterion counts a change's lines | Given the tree at HEAD, when the enumeration command of *Data & interfaces* runs, then it lists the fifteen lines recorded there and the new sentence, and none of them holds a change's net line count as a criterion | The command's output against the table under *Data & interfaces* |
| S4 The core still reaches a session whole | Given the core with the sentence, when the hook builds its output, then the output stays under `CAP` | `tests/hooks/test_core.py`, a narrow run by the builder; P1 measured 6,653 characters |
| S5 The release carries the change | Given the branch's last commit, when the fragment and the manifest are read, then `changelog.md` holds a `### Changed` entry and one `### Process changes` row in `templates/records/process.md`'s shape, and `.claude-plugin/plugin.json` reads `0.25.2` | Reading `changelog.md`; `git show HEAD:.claude-plugin/plugin.json` |

## Data & interfaces

**The enumeration.** One `git grep` carries every phrasing a criterion that counts lines could be written in. The phrasings, by kind:

| Kind | Phrasings |
|---|---|
| Net change | `net line(s)`, `net-negative`, `net reduction`, `net shrink`, `net growth`, `net delta` and their hyphenated forms |
| Comparison | `more lines than`, `fewer lines`, `lines than it adds`, `removes more lines than`, `removes more than it adds`, `adds more than it removes` |
| Diff statistics | `shortstat`, `numstat`, `diffstat`, `--stat` |
| Insertions against deletions | `deletions above`, `deletions exceed`, `deletions outnumber`, `insertions over` and the like |
| Budget | `line budget`, `line count`, `line limit`, `line cap`, `line ceiling`, `line quota` |
| Lines moved | `lines added`, `lines removed`, `lines deleted`, `lines saved`, `lines cut` |
| Change size | `diff size`, `change size`, a change or diff that is `smaller`, `shrinks`, `grows` or is `larger` |
| Figures | `+N / −M`, `−N lines`, and any figure followed by `words`, `lines`, `characters`, `chars`, `bytes` or `tokens` |
| Text size | `less text`, `shorter text`, `fewer words`, `word count`, `word budget`, `token ceiling` |
| Counting command | `wc -l` |

The command, run at `1dd83935` (executed):

```
git grep -n -i -E 'net[- ](line|lines|negative|positive|reduction|shrink|loss|gain|growth|delta)|more lines than|fewer lines|lines than it (adds|removes)|remove[sd]? more (lines|text) than|adds? more than it removes|removes? more than it adds|shortstat|numstat|diffstat|--stat[^e]|(deletions?|insertions?) (above|exceed|over|outnumber|greater|below|beat)|line[- ](budget|count|limit|cap|ceiling|quota)|lines? (added|removed|deleted|saved|cut)|(diff|change|patch)( size|.{0,10}(smaller|shrinks|grows|larger))|[+][0-9][0-9,]* ?/ ?[-−][0-9]|[-−][0-9][0-9,]* lines|less text|shorter text|fewer words|word[- ](count|budget|limit)|[0-9] (words|lines|characters|chars|bytes|tokens)|token ceiling|wc -l' -- skills agents templates docs CLAUDE.md CONTRIBUTING.md README.md README.ko.md ':!*.py'
```

`--stat[^e]` keeps `gh … --state` out. It found fifteen lines, and none is a criterion on a change's size:

| Line | What it holds | Judgment |
|---|---|---|
| `agents/framer.md:99`, `:224` | `wc -l` as a command a framer runs while reading | A read, not a criterion |
| `docs/the-review-record.md:493`, `:496` | The harness's 10,000-character cap on a `Stop` hook's message, and the 1,000 characters `MESSAGE_BUDGET` keeps back | A limit on what reaches one reader |
| `skills/code-review/orchestration.md:30` | A fix pass resumes the implementer only below 806,241 tokens of per-turn context | A limit on one agent's context |
| `skills/config/SKILL.md:50`, `:141`; `templates/setup/config.md:438`, `:444`, `:447`, `:448` | `Document token ceiling`: the estimated tokens past which `seal fold` reports one policy document as one to split | One document's size against its reader, reported and never failing (`skills/settle/scripts/fold_check.py` docstring, *One read*) |
| `skills/implement/SKILL.md:412` | `git diff --stat` already holds the file list, so `gaps.md` does not restate it | Context, and the rule the sentence states |
| `skills/settle/SKILL.md:248`; `skills/verify/SKILL.md:186` | A summary line counting outcomes | A match on the words "line count", not a size |
| `skills/verify/orchestration.md:429` | The run table's row "Records' share of the diff", from `git diff --numstat` | A measurement in a table that "carries no verdict" (line 458), which is the use the sentence keeps |

The same pattern over `skills/`, `agents/`, `templates/`, `hooks/`, `.github/scripts/` and `evals/scripts/` with `.py` files included (executed) finds no script that compares a change's insertions with its deletions. `evals/scripts/replay_targets.py:663` sums both from `git diff --shortstat` as a replay target's size, which is context.

**What the enumeration reads, and why.** `skills/`, `agents/` and `templates/` are the issue's. `docs/` is in: it is the policy root every party reads first, and it outranks the code. `CLAUDE.md` and `CONTRIBUTING.md` are in: `.github/scripts/rules.py#RULE_FILES` names both as rule files, and a session in this repository reads them. `README.md` and `README.ko.md` are in: they ship and a user reads them. `tests/` and `evals/` are out: no party follows them as instructions for real work, and a size figure there is a fixture or a measurement. `seal/threads/` is out: its records belong to shipped work and leave at the settle (*Scope*, out).

At HEAD after the build, the command also lists the new sentence in `skills/core/SKILL.md`, which matches `fewer lines`. That is the sixteenth line S3 expects.

## Rule changes

- nothing
  why: The sentence goes into `skills/core/SKILL.md`, which is a skill
    and not a document of the policy root, and the pull request edits it in
    place. No document under `docs/` states what less text means or holds a
    change's line count as a criterion (*Data & interfaces*).

## Removes

- nothing
  why: The sentence adds a meaning the tree did not hold, and nothing in
    the tree stood on the old reading: the enumeration under *Data &
    interfaces* found no shipped sentence or script that holds a change's
    net line count as a criterion. The one other copy of the meaning, the
    orchestrator's local memory `compact-not-net-negative`, is outside the
    tree and is deleted by the orchestrator after the merge (*Scope*, out).

Framed 2026-10-31 by framer, before the build.
