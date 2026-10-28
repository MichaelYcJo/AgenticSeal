# Review round 1: 1793163944-the-issues-were-filed-against-the-old-tree

target: f12a768c against 0b75346f

This is the first round, so no fact is carried from an earlier one. The
branch changes no tree file outside the work item's directory (S7, executed),
so the deliverables reviewed are on GitHub in `MichaelYcJo/AgenticSeal`: the
three filed issues, the 22 folded bodies, #1040's title, the comment on
#1044, and the descriptions of milestones 65 and 67. Each body was fetched
with `gh issue view`, and the version before the fold was taken from the
issue's `userContentEdits` history, so every change was read as a word diff
against the body the frame read. Every coordinate a folded body names was
opened at `origin/release/v0.24.0` (`c9b366f1`), which differs from
`0b75346f` outside `seal/threads/` only in the four documents #1108 settled.

## Findings

### 1. The owner's order decisions on #1109 and #1111 reached the frame and milestone 65's description, but not the two issues' bodies

severity: should
location: `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:505-508`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:569-570`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/phases/phase-1.md`
evidence: executed `gh issue view 1109 --repo MichaelYcJo/AgenticSeal --json title,body,milestone`, `gh issue view 1111 --repo MichaelYcJo/AgenticSeal --json title,body,milestone`, `gh issue view 1110 --repo MichaelYcJo/AgenticSeal --json body`, `gh pr view 1112 --repo MichaelYcJo/AgenticSeal --json title,state,body,baseRefName,files`, `gh api repos/MichaelYcJo/AgenticSeal/milestones/65 --jq .description`
verdict: open

Phase 1 filed #1109 and #1111 before the owner changed their order on
2026-10-28. The orchestrator folded both changes into `frame/design.md` at
`2cdc12b8`, and phase 4 wrote them into milestone 65's description. Neither
change was folded into the issue it is about. `docs/issues-and-milestones.md`
*An issue is its body and its comments together* says a decision is folded
into the body in place, and *A milestone answers when* says that grounds
belonging to one ticket sit on that ticket.

The defect shows in two places:

- **#1109.** The owner routed it `no work item`, and the description says
  "#1109 was fixed directly, before the small fixes, without a work item".
  The body's third *Done when* bullet still reads "This issue's frame says
  whether one census case that reads a new name inside a longer word is
  worth adding". A `no work item` change has no frame. Pull request #1112
  (open, into `release/v0.24.0`) carries `Closes #1109`, changes only the
  six sites and the `.test_durations` key, and does not answer the census
  question. Its body says "#1110 carries the rest of the rename's leftovers
  in living text", but #1110's body holds no census question. When #1112
  merges, #1109 closes with that bullet unmet, and nothing records where
  the census decision went. The frame carries the same sentence at
  `frame/design.md:505-508` ("the issue's frame says whether one census case
  is worth adding"), under a heading that `2cdc12b8` changed to "fixed
  directly".
- **#1111.** The description orders it "after #956, whose audit it builds
  on". The body's only order sentence is "#1040 removes sentences two of
  these pins read, so this issue runs after #1040". Its one sentence on
  #956, "#956 asks which way a reader fails on input it cannot read. This
  issue asks whether a pin reads a fact at all", sets the two apart and
  names no dependency. A framer who reads only #1111 learns nothing of the
  wait, or of the ground the owner gave for it. The frame's F3 section has
  the same gap: only its heading at `:539` says "after #956", and the
  paragraph at `:569-570` still contrasts the two issues.

Enumerated (contract rule 12): the owner made three decisions after the
frame. Q1 keeps #920 in 0.24.0. #920's folded body states no milestone, and
#1049's body does not gain #920, so Q1 needs no body edit. The other two are
the two instances above.

The fix for #1109 replaces the third *Done when* bullet and gives the census
question a home. The fix for #1111 replaces its order bullet. The frame lines
change to match:

```text
#1109, third bullet of "## Done when", replacing it whole:
- No census case is added here: this issue is fixed directly, without a work item (owner, 2026-10-28). Whether a census case reads a new name inside a longer word is decided in #1110's frame, which owns the rest of the rename's leftovers in living text.

#1110, one bullet added to "## What this work decides":
- Whether `tests/censuses.py` gains a case that reads a new agent name inside a longer word, the class #1109 fixed at six sites (`detracer`), given that #1109's search found no other instance.

#1111, the second bullet of "## How it differs from the issues beside it", replacing it whole, followed by a new section:
- #1040 removes sentences two of these pins read.

## Order

After #956 and #1040 in `release: 0.24.0`. #956's audit settles which way each reader of written text fails, and this issue decides each phrase pin against what that audit settles (owner, 2026-10-28). #1040 changes the sentences two of these pins read.

frame/design.md:505-508, the Done-when sentence of F1, replacing "and the issue's frame says whether one census case is worth adding, given that the search above found no other instance." with:
and the census question goes to F2's frame (#1110), because F1 is fixed without a work item.

frame/design.md:569-570, replacing "#956 asks which way a reader fails on input it cannot read; F3 asks whether a pin reads a fact at all." with:
F3 runs after #956, whose audit settles which way each reader fails on input it cannot read, and F3 decides each pin against that (owner, 2026-10-28).
```

answer:

### 2. The frame keeps every title but #1040's on a premise that does not hold, and eight titles still state an old name or a figure the fold corrected

severity: should
location: `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:47-50`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/phases/phase-2.md:132-137`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/phases/phase-3.md:103-105`
evidence: executed `gh issue view <N> --repo MichaelYcJo/AgenticSeal --json title`, `git cat-file -e 0b75346f:tests/test_the_hook_surface_git_offers.py`, `git cat-file -e origin/release/v0.24.0:tests/test_the_hook_surface_git_offers.py`
verdict: open

`frame/design.md:47-50` puts titles out of scope because "the read found no
title naming a file that no longer exists in a way the body cannot correct",
and makes #1040 "the one exception". It retitles #1040 because "a title that
names three agents that no longer exist is the first line a framer reads"
(`:190-194`). That reason applies to other titles too, and the premise
behind keeping them is false. #1039's title names
`tests/test_the_hook_surface_git_offers.py`, which is absent at `0b75346f`
and at `origin/release/v0.24.0` (both `git cat-file -e` calls failed). The
body can correct a title's old name in every case, #1040's included, so that
clause does not tell #1040 apart from the rest.

The class, enumerated over every title of both milestones (contract rule 12;
the crafter's hand-back in phases 2 and 3 named six of these and missed
#1042 and #1049):

| Issue | What the title says | What the folded body or the tree says |
|---|---|---|
| #712 | "session-cost's spawn rows" | `seal cost --spawns` |
| #1039 | `tests/test_the_hook_surface_git_offers.py`, "at 19.5 s" | `tests/behaviour/test_the_hook_surface_git_offers.py`, 16.3 s |
| #1042 | "`.git/specseal-eval/` input paths and a `specseal-eval-` plugin tree" | `.git/agentic-eval/`, `prefix="agentic-eval-"` (`evals/scripts/noninferiority.py:611`) |
| #1043 | "docs/the-review-record.md cites Measure the segment in skills/verify/SKILL.md" | corrected by `de11df75`; `docs/the-review-record.md:682-683` at the release branch names `skills/verify/orchestration.md` |
| #1045 | "overview.md's divergence table goes" | `gaps.md` |
| #1046 | "1,836 of the 7,047 words" | 1,993 of 7,649 |
| #1048 | "a sample of the smith's claims" | the crafter |
| #1049 | "99 s of tests" | about 106 s |

A framer reads the title first. For #1043, the title's first clause states
as current a defect the body says is fixed. The frame's argument for
keeping titles, that a title is cited in commit subjects and changelog
lines, is a reason to retitle before the work lands: the pull request that
closes each issue is titled from it.

```bash
gh issue edit 712  --repo MichaelYcJo/AgenticSeal --title "fix: seal cost's spawn rows push every cell past its header when an agent's name is longer than the label column"
gh issue edit 1039 --repo MichaelYcJo/AgenticSeal --title "test: after #1027's settle, three cases of tests/behaviour/test_the_hook_surface_git_offers.py still pin what only the retired commit gate inside git needed, at 16.3 s of the serial suite; they go with their .test_durations entries"
gh issue edit 1042 --repo MichaelYcJo/AgenticSeal --title "test: the behaviour suite tells the agent under test it is being evaluated, through an eval commit author, .git/agentic-eval/ input paths and an agentic-eval- plugin tree that holds the truth graders"
gh issue edit 1043 --repo MichaelYcJo/AgenticSeal --title "docs: gather_changelog.py cites a heading docs/the-record-layout.md does not have, and no check reads a citation of any file but implement's"
gh issue edit 1045 --repo MichaelYcJo/AgenticSeal --title "chore: a fix to a work item's own records still costs a verifying round, and 36 of 0.22.x's 226 findings named only seal/ files; chain-check and the sealer confirm a records-only fix, and gaps.md's divergence table goes"
gh issue edit 1046 --repo MichaelYcJo/AgenticSeal --title "chore: every orchestrating session reads Bootstrap and Parity setup, 1,993 of the 7,649 words of implement's orchestration, which apply only to a first session or a migration; they move to a file opened when they apply"
gh issue edit 1048 --repo MichaelYcJo/AgenticSeal --title "feat: the sealer re-runs a sample of the crafter's claims and leaves the rest on its word, 23 of 28 mutation claims in #955; it checks every executed claim against the implementer's transcript and re-runs a sample"
gh issue edit 1049 --repo MichaelYcJo/AgenticSeal --title "chore: the worktree guard has never been weighed against what it costs, about 6,500 lines of hooks and 106 s of tests against no recorded catch; the record decides keep, narrow or remove"
```

`frame/design.md:47-50` then reads: "The issues' titles, except where a
title names a path, an agent, a command or a figure that the fold
corrected: those titles take the folded form (#712, #1039, #1040, #1042,
#1043, #1045, #1046, #1048, #1049), and every other title is unchanged."
Each `gh issue edit` is read back with `gh issue view <N> --json title`, and
the phase record lists the old and new titles. Where the owner keeps the
titles instead, the clause "the read found no title naming a file that no
longer exists" is replaced by the reason they stay, so that the frame does
not rest on a false premise.

answer:

## Confirmations

confirms: none
S1, the 22 folded bodies. Each body was word-diffed against its version
before the fold, taken from the issue's `userContentEdits` history (executed,
`gh api graphql` per issue). Every change is either the issue's row in
`frame/design.md` *Verdicts* or an instance of a mapping row, and every other
sentence is unchanged. The six instances folded beyond the rows that
`trail/phases/phase-2.md` lists, and the two in `trail/phases/phase-3.md`,
are each a mapping row's class. The plan's old-form search over each body,
with `<commit>:<path>` citations masked, leaves only the hits the phase
records judge: history the rows keep (#947's *Before* heading, #1020's
`6fb3b2fd` tables, #1045's "then `overview.md`", #1047's "then the
warden's", #1048's and #1091's "then named the smith", #992's "recorded as
the warden's"), the current path `docs/worktree-guard-spec.md`,
`seal rules --check`, and #1040's "a broad-gate failure" (executed, a
Python regex over each body).

confirms: none
Every coordinate a folded body names holds at `origin/release/v0.24.0`
(executed, `git show origin/release/v0.24.0:<path> | sed -n <line>p` and
`git grep` for each). Among them: `tests/skills/test_chain_check.py:249`,
`:2326`, `:2785`, `:2875`, `:2891`, `:2906`; `tests/conftest.py:514`,
`:536`; `skills/verify/scripts/pact_check.py:249`, `:269`;
`hooks/lib/config.py:98`, `:102`; `hooks/worktree-guard.py:1382`, `:1389`,
`:1394`, `:197`; `skills/verify/scripts/session_cost.py:2225`, `:2318`,
`:2328`, `:2333`, `:2419`, `:2425`; `docs/worktree-guard-spec.md:360`,
`:587`; the three cases and markers of
`tests/behaviour/test_the_hook_surface_git_offers.py` at `:176`,
`:273-274`, `:317-318`; `agents/crafter.md:65-70`, `:138-140`;
`agents/proofer.md:59`, `:61`, `:138-147`; `agents/sealer.md:78-81`,
`:109-110`, `:125-128`; `agents/framer.md:23-25`, `:83-85`, `:106`;
`agents/tracer.md:34`, `:46`; `skills/code-review/orchestration.md:54-55`,
`:100`, `:191`; `skills/implement/SKILL.md:484`;
`chain_check.py#verdict_of` (`:883`) and `#verdicts_of` (`:1864`);
`evals/scripts/rule_cases.py:205`, `:280`, `:288`, `:370`, `:636`;
`evals/scripts/seed_defects.py:313`; `evals/scripts/noninferiority.py:611`,
`:762`; `.github/scripts/gather_changelog.py:38`, `:43-44`;
`docs/the-record-layout.md:140`; `docs/the-review-record.md:135-136` (equal
at `0b75346f`) and `:682-683`;
`tests/behaviour/test_the_set_a_work_item_always_has.py:443`, `:487`;
`README.md:417`, `:529`; `README.ko.md:168-169`, `:408`, `:522`;
`hooks/dispatch.py:81-105`; `skills/config/SKILL.md:168`;
`agentic_pytest_record.py:294`, `:310`;
`skills/implement/scripts/seal.py:1162`; `hooks/worktree_consent.py:603`;
`.github/scripts/label_merged_on_release_branch.py:113`;
`skills/implement/orchestration.md:88`, `:280`, `:607-611`, `:657-658`,
`:660`; `skills/settle/SKILL.md:189-193`;
`templates/records/sdd-gaps.md:11`; `skills/verify/SKILL.md:329-334`. Each
released record a body cites at a commit exists (executed, `git cat-file
-e`), and no body names a live path under the three threads #1108 removed.

confirms: none
`gaps.md`'s divergences hold against the tree. `hooks/worktree-guard.py:197`,
`hooks/implementer-notice.py:47` and `hooks/lib/tokens.py:71` import
`cmdline`, so the frame's list for #1049 was wrong and the body's is right.
`tests/github/test_tracker_labels.py:146` is a second reader of
`LABEL_DESCRIPTION_LIMIT`. Re-run at `0b75346f`: #1110's eight line counts
(`docs/` 18) and #1111's six assert counts (182, 308, 224, 57, 31, 13) are
reproduced exactly (executed, the commands each body states).

confirms: none
S2: #1053, #1096 and #1102 read `updatedAt` 2026-10-27T02:26:00Z,
2026-10-28T04:03:25Z and 2026-10-28T04:05:42Z, the frame's values. S3: #920
is in `release: 0.24.0` and has one comment, the owner's of 2026-10-18. S4:
#1109, #1110 and #1111 are open in `release: 0.24.0` under the frame's
titles. S6: #1044's second comment says its count now lives in #947. S7:
`git diff --stat 0b75346f..HEAD` outside the work item's directory printed
nothing (all executed).

confirms: none
S5: each milestone description equals the frame's quoted text at HEAD,
`frame/design.md:643` and `:647`, with F1 to F3 replaced by #1109 to #1111.
The only difference is the closing newline (executed, `diff`). The 22 open
issues of `release: 0.24.0` and the 7 of `release: 0.24.1` are the sets each
description names (executed, `gh issue list --state open`). `gaps.md`
discloses the repeats and the mentions of #1044 and #1103 against S5's
"once" wording, and each is a later step's reason naming an earlier issue,
as the frame's text writes it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate over this branch; the round ran no suite, lint or typecheck, and no tree file outside the work item's directory changed | `trail/gate.md`, not yet written | the orchestrator |
| Milestone 65's sentence "#1109 was fixed directly" holds only once #1112 merges; it is open at this round | `gh api repos/MichaelYcJo/AgenticSeal/milestones/65` | the orchestrator, who owns #1112 |
| Whether each parallel group's "share no file" holds was read from the files each body names, not from the work each issue will do | milestone 65 and 67 descriptions | the framer of each issue, at its frame |
| `frame/questions.md` Q2 still reads `open`, though phases 2 and 3 record that it did not arise | `frame/questions.md` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `gh issue view <N> --json number,title,body,state,milestone,updatedAt,comments` for the 25 issues and #1044, #1053, #1096, #1102 | each fetched, exit 0 |
| `gh api graphql` for `userContentEdits` of the 22 folded issues | the body before the fold for each, edited at or before 2026-10-27T07:37:50Z |
| `git diff --no-index --word-diff=plain` of each body before and after the fold | only the row's and the mapping's changes |
| `grep -h -E 'assert \(?\s*"[^"]{25,}"\s*\)?\s+in\b' -r tests/<dir> \| wc -l` at `0b75346f` | 182, 308, 224, 57, 31, 13 |
| `git grep -h -i -w -E 'specs?' 0b75346f -- <path> ':!*.ko.md' \| grep -v -c worktree-guard-spec` | 11, 201, 18, 14, 42, 1, 2, 12 |
| `diff` of each milestone description against the frame's line | equal but for the closing newline |
| `git cat-file -e` on `tests/test_the_hook_surface_git_offers.py` at `0b75346f` and at `origin/release/v0.24.0` | absent at both |
