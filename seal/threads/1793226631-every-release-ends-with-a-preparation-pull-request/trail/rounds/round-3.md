# Review round 3: 1793226631-every-release-ends-with-a-preparation-pull-request

target: 1c50a693, fixes 5ccb7a61..1c50a693

## Findings

No finding this round.

## Confirmations

confirms: round-2#1
The three sentences the finding named now carry the qualifier (read, in the
`5ccb7a61..1c50a693` diff). `frame/design.md:14` reads "The owner's one
required act at a release is the merge of the release pull request with
*Create a merge commit*." `frame/design.md:137-139` reads "That is his one
required act at the release; the reads and boxes the checklist still gives
him are `frame/questions.md` Q2's, and fail nothing." `frame/plan.md:12-13`
reads "and the owner's merge of it, his one required act." Each matches the
finding's block word for word. The plan's line is wrapped differently from
the block, which leaves the short line "0.24.0 is the first" at `:14`; the
words are the block's.

The orchestrator claimed that `git grep -n -E "one act"` over the work item
outside `trail/` finds no line. Re-run, it exits 1 (executed). This round
also re-ran both of the finding's `executed` lines. Outside `trail/rounds/`,
the work item's hits are the three qualified sentences and the step-5 `to:`
at `frame/design.md:268-269`, which was already qualified. Every hit in the
rest of the tree uses "one act" in another sense: the broad gate as a single
act, an issue leaving the backlog, an orchestrator act in a table. None of
them states what the owner does at a release (executed).

The sweep asked for in this round's prompt found no other sentence that
states the owner's acts without "required". `frame/questions.md:29`, Q2's
default (a), reads "the owner's required act is the merge", the same
wording. `frame/plan.md:101-105` lists his two merges at 0.24.0 and names Q2
for the steps the checklist still gives him. `trail/phases/phase-3.md:37`
says the checklist's other owner acts are untouched. `changelog.md:3` says
nobody pushes a tag at the end of a release, which the new workflow makes
true and which is not a claim about the owner's only act. The
`changelog.md:19` row's "two waits the owner did by hand" is in the past
tense. Each was read against the Q2 default, and none contradicts it (read).
`docs/branch-and-release.md:45`, "The tag push, the maintainer's last act",
is the `from:` of the operation at `frame/design.md:352-361`, so the settle
rewrites it (executed, the `maintainer's last act` grep in `## Probes`).

confirms: round-2#2
`changelog.md:4` and `frame/design.md:38-41` now read "as a branch named
`release/vX.Y.Z` does". That is the wording of
`skills/implement/orchestration.md:530`, so neither sentence misreports the
skill any more (read). The orchestrator claimed that
`git grep -n -E "as this (one|repository) does"` over the work item outside
`trail/` finds no line. Re-run over the whole tree, it finds only the
`trail/rounds/` records that quote the old text (executed).

The sweep of the shipped files was repeated over every line the branch adds
under `skills`, `agents`, `templates`, `hooks`, `bin`, `commands` and
`.claude-plugin`. Those lines were grepped for "this one", "this
repository", "this project", "this plugin", "this tree", "here", "our" and
the product and owner names, and no line matched (executed). This round also
read each added line of `agents/framer.md:63-70`,
`skills/implement/orchestration.md:526-540`, `skills/settle/SKILL.md:176`
and `templates/records/process.md`. The framer's read is conditioned "where
the repository publishes one", the skill names the branch's shape, and the
template speaks of "this work item", which is the host's own (read). The
fragment's four `### Changed` entries were read as the 0.24.0 Release body.
The first names this repository's own workflow and script, which is what
the note is about. The second now names the branch's shape. The fourth names
this repository's check. The third is a row of `## Not judged`.

Facts carried rather than re-established: `9dc8df11` touches
`frame/design.md`, `frame/plan.md` and `changelog.md`. Its changes to
`frame/design.md` sit at `:14`, `:40-41` and `:137-139`, above
`## Rule changes`, and change no operation. So round 2's parse of that block
(30 operations, no error) is carried, not re-run. `seal rules --check`
reads the block's check lines and holds (`## Probes`).

confirms: none
The four modules this round's prompt names pass. `bin/seal layout --check`
and `bin/seal rules --check` both exit 0, so S12 still holds at `1c50a693`
(executed, `## Probes`). `tests/behaviour/test_docs_line_wrap.py` is among
the four and passes with the plan's re-wrapped line in place.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the third `### Changed` entry of the fragment, the 0.24.0 Release body, reads to a person who installs the plugin as something the plugin now does in their repository. It says "A work item that changes the way of working writes its process row in its own changelog fragment". No shipped skill, agent or template tells an orchestrator to write a `### Process changes` table: the shipped hits are `agents/framer.md:64-68`, which reads one, and the template (executed, `git grep -n -E "Process changes\|process row\|records/process\.md" -- skills agents templates hooks bin commands`). The rule reaches this repository's own policy root through `## Rule changes` (`frame/design.md:452-464`). The archive it replaces was also this repository's practice, so the entry may be meant as this project's way of working, and no fix-pass commit made this sentence | `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/changelog.md:5` | the owner, when he reads the release note on the release pull request |
| Facts carried from rounds 1 and 2 and not re-derived, because no commit in `5ccb7a61..1c50a693` touches their paths: round 1's judgment that #1112, #1120 and #1116 write no process row, its confirmations of `tag_release.py#decide` and of the workflow's S8 behaviour, its S11 grep, and round 2's parse of `## Rule changes` | `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/trail/rounds/round-1.md`, `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/trail/rounds/round-2.md` | the sealer, which reads the records against the frame |
| Whether `gh api -X POST repos/<REPO>/git/refs` with the workflow's token creates `v0.24.0`, carried from round 1 unchanged | `frame/questions.md:31` (Q4), `.github/scripts/tag_release.py:153-179` | the orchestrator, reading `gh run list --workflow publish-release.yml --limit 1` and its log after 0.24.0's merge into `main` |
| Whether Q2's default (a) meets the owner's requirement that a release needs no act of his beyond the merge, carried from round 1 unchanged. The frame now states the default one way in every place | `frame/questions.md:29` (Q2) | the owner, through Q2 |
| The full suite, the repository-wide lint and the typecheck at `1c50a693`. No fix pass ran, so no hand-back carries a suite label; the suite is `unverified` | the whole tree | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git diff 5ccb7a61..1c50a693` | four files: `changelog.md`, `frame/design.md`, `frame/plan.md`, `trail/rounds/round-2.md`; each applied block matches round 2's text word for word |
| `git grep -n -E "one act"` over the work item outside `trail/` | exit 1, no line |
| `git grep -n -i -E "one (required )?act\|only act\|single act\|owner's (one\|only)\|no act of"` over the tree | in the work item, only the qualified sentences and `trail/rounds/`; elsewhere only other senses of "one act" |
| `git grep -n -i -E "owner('s)? (merge\|act)\|his (one\|only)\|what is left at the end"` over the work item | `frame/design.md:137-138` and `frame/plan.md:12-13`, both qualified; Q1 option (c) and `trail/phases/phase-3.md:37`, neither a claim of one act |
| `git grep -n -i -E "maintainer'?s? (last\|one\|only)\|last (manual )?act\|last act"` | `docs/branch-and-release.md:45`, reached by the operation at `frame/design.md:352-361`; the frame's own lines |
| `git grep -n -E "as this (one\|repository) does"` | only `trail/rounds/round-1.md` and `round-2.md`, quoting the old text |
| `git diff -U0 4134055a HEAD` over `skills`, `agents`, `templates`, `hooks`, `bin`, `commands` and `.claude-plugin`, its added lines grepped for self-referring phrases and product and owner names | exit 1, no line |
| `git grep -n -E "Process changes\|process row\|records/process\.md" -- skills agents templates hooks bin commands` | `agents/framer.md:64` and `:68`, `templates/records/process.md:1` |
| `bin/test -q tests/behaviour/test_docs_line_wrap.py tests/github/test_publish_release_note.py tests/github/test_tag_release.py tests/text/test_the_record_is_written_in_words.py` | exit 0: 109 passed |
| `bin/seal layout --check` | exit 0: 161 files read, 0 refused |
| `bin/seal rules --check` | exit 0: all 266 check lines in 55 rule files hold |
