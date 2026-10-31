# Design: 1793437163-fields-stand-in-marked-blocks (#1198)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*: "a script does not re-encode that judgment as a grammar rule: it reads what a command wrote or what a real parser returns" (read) | Today a reader decides, for every line of a round record or a guarantee, whether it is a field, a line that only looks like one, or prose. Inside a `seal` block every line is a field and parses or is refused, and outside it no line is a field, so no reader decides whether a prose line meant a label. What stays a judgment is whether a field states the truth, which the proofer, the orchestrator and the sealer keep. |
| the same, *The rule a mechanism is kept against*: "when fixes chase one mechanism's edge cases, ask what it decides", "before a fix adapts to an existing structure, ask whether the structure should change", and "It names as not read a line or a file that looks like one of its form's and is not one, and decides nothing on it" (read) | The labelled-line grammar's edges were chased across #1123 (five rounds) and #1132 (four) (read, the issue body), and 8 of #1167's 16 findings were near-miss naming or where a form starts and ends: round 3 findings 1 and 2, round 4 finding 1, round 6 findings 1 to 3, round 9 finding 2, round 10 finding 1 (executed, `grep -E '^### [0-9]+\.\|^regression:' seal/threads/1793411151-*/trail/rounds/round-*.md`). The block replaces the mechanism instead of adapting to it. The naming sentence still binds: the one look-alike left is a fence opener near the block's, and Scope item 1 names it. |
| the same, the same clause, "A script holds a gate only on a fact it reads exactly: an exit code, a parser's result, or a line of the plugin's own forms in the one spelling the form gives it" | A block whose opener is exact is the form, so a line inside it that does not parse makes the form malformed, and refusing it is a parser's result on the form, not a decision about a look-alike. `skills/settle/SKILL.md` *Rule changes* already refuses a `## Rule changes` item that does not match whole on the same footing. The core needs no change. |
| `agents/framer.md` *A mark is not the answer to a blocked step*, and `CONTRIBUTING.md` *What a change to a gate must carry*, **What it removes** and **What it reads** (read) | The block is a line grammar and a mark, so `## Removes` names what goes with it, and *Data & interfaces* names the form each reader reads, what it names as unread, and the agent that judges the meaning. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*: "The policy root ... is the baseline, and a pull request does not edit it" | Every `docs/` change is an item of `## Rule changes`. `chain_check.py` loads its grammar from `docs/the-review-record.md` *The round record* at import (`skills/code-review/scripts/chain_check.py:195-199`, `:510`, read), so a new grammar there would reach the code only at the settle after the release. #988 edited the table in its own pull request to get past that (executed, `git show 0d62145a -- docs/the-review-record.md`), and #1167's A15 kept the loader only because its change removed a table. This work moves the grammar into the code (Scope item 1, `frame/plan.md` A8). |
| The policy in force: `docs/` plus the unsettled designs' `## Rule changes` in merge order; 8 work items under `seal/threads/` are released in 0.26.0 and unsettled (executed, `ls seal/threads/`) | #1167's design (`seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md`, read whole) changes the paragraphs of *The round record*, *What the check reads at the pull request* and *The guarantee* this work changes again, and adds `docs/what-a-script-gates.md`. Each `from:` below quotes the text with #1167's `to:` applied where #1167 changed it. No other unsettled design names these sections (executed, `grep -n 'section: The round record\|section: The guarantee\|section: The stamp\|section: What the check reads' seal/threads/*/frame/design.md`). |
| `docs/the-review-record.md` *What the check reads at the pull request*: the check "opens the records of the work items this pull request's own commits declare or change and no other" (read; `chain_check.py#edited_work_items` at `:1703`, read) | A record written before the change is read by the new reader only in a work item whose pull request is still open. The 39 round records, 8 guarantees and 8 gate records under `seal/threads/` (executed, `ls seal/threads/*/trail/rounds/round-*.md \| wc -l` and the same for the others) belong to released work items and are never judged again. Scope item 9 decides the open case. |
| `docs/the-review-record.md` *The guarantee* and *The stamp* (read) | The verdict, the `Target SHA` row and its `; earlier run:` chain are read by `chain_check.py#guarantee` and by `seal_stamp.py` through `verdicts_of`, `target_of`, `table_rows`, `field` and a cell split of its own (`skills/verify/scripts/seal_stamp.py:1164-1167`, `:1247-1249`, `:1347-1361`, read). |
| #1122, reprobed at `15a5ce66` (executed, a probe script loading `chain_check.py` from a `git clone --no-local` under the scratchpad): a guarantee reading `Verdict: sealed`, then a fence nobody closed, then `Verdict: withheld reason: the gate failed` | `verdicts_of` returned one line, `Verdict: sealed`; `comment_lines` returned none; `unclosed` returned one refusal at line 9. `seal_stamp.py` calls `comment_lines` and never `unclosed` (executed, `grep -n unclosed skills/verify/scripts/seal_stamp.py`: no line). So the stamp still queues where the pull request refuses. Scope item 4 closes it. |
| The near-miss net at `15a5ce66`, the same probe | `chain_check.opens_like` names `Verdict: open`, `**verdict:** open` and `verdict : open` as the `verdict:` label and `Regression: round-1#1` as `regression:`, and does not name `the verdict: open is wrong`. `hooks/lib/blocks.py#fence_opener` returns a backtick fence of length 3 for both the line of three backticks and `seal` and the same line with `Seal`, a tilde fence of length 3 for a tilde opener, and `None` for a four-space indent, and it does not return the info string. The reader needs the info string, so Scope item 1 asks `hooks/lib/blocks.py`'s fence pattern for it. |
| The issue, whole, with its one comment (executed, `gh issue view 1198 --json body,comments`, 2026-10-31) | *First step: a review, not a build* is *The review* below. The comment adds `skills/verify/scripts/broad_gate.py#job_steps` (`:2124`, the split at `:2161`) and `skills/verify/scripts/payload_meter.py#frontmatter` (`:235`, the split at `:249`) to the inventory (read). They read the plugin's own YAML, not a work item's records, so the block does not reach them, and Scope item 10 takes their line split. |
| The class of the comment's two readers, listed by the census's own exemption lines (executed, `git grep -n 'exempt from splitlines: YAML' -- ':!seal/'`) | Two lines, `broad_gate.py:2161` and `payload_meter.py:249`, and no third. The census in `tests/censuses.py#splitlines` lists every `.splitlines(` call that is not exempted, so the list is whole. #1167's round 8 fixed the same defect in `deferral_check.py#runners_in` by splitting at LF after universal newlines and measured it (`seal/threads/1793411151-judgment-where-meaning-is-the-question/trail/rounds/round-8.md:135`, read). |
| Milestone 75 (executed, `gh api repos/:owner/:repo/milestones/75`, 2026-10-31): `release: 0.27.0`, nine open issues and one closed | Its description puts #1198 first and orders the rest against it. *The order against milestone 75* below gives each issue's place. |
| The issues the milestone and the issue name (executed, `gh issue view <N> --json state,milestone`, 2026-10-31) | #1121 and #1125 are CLOSED in milestone `release: 0.26.0`; #1149 is CLOSED in 0.27.0; #1122, #1126, #1128, #1150, #1147, #1197, #1154 and #1020 are OPEN in 0.27.0. |
| `docs/branch-and-release.md` *The version is named at the cut* (read); `.claude-plugin/plugin.json` reads `0.26.0`, and `origin/release/v0.27.0`, `origin/main` and this branch's parent are all `15a5ce66` (executed, `grep`, `git rev-parse`) | No pull request has reached `release/v0.27.0` yet. #1154 is framed beside this work and may reach it first, so this work moves `plugin.json` to `0.27.0` only where the base does not already read it (Scope item 11). |
| `evals/README.md`: a change to "a prompt, a scaffold or a `shape-` grader asks the agent something its runs never answered, and only a run measures that" (read) | The proofer's nine `shape-findings.md` graders and the sealer cases' scaffolds and `shape-verdict.md` graders read the record's shape (executed, `git grep -ln` over `evals/behaviour`). Changing them means the next comparison of either suite runs both sides fresh; no recorded side is regraded across this change. That cost is stated in `frame/plan.md` *Operational impact*. |
| The latest release's `### Process changes` (executed, `gh release view --json body`) and the 8 released fragments | None changes how a record is written or read beyond #1167's rows, which this work builds on. |
| `seal/follow-up.md` (read whole) | No row waits on this work. |

## The review

### Every field a script reads in a work item's records

Listed by two methods, and their union is the list: every shipped `.py` outside `tests/` that names a record's file or directory (executed, `git ls-files '*.py' \| grep -v '^tests/' \| xargs grep -l -E 'threads\|guarantee\.md\|round-\|rounds\|routing\.md\|gate\.md\|plan\.md\|design\.md\|gaps\.md\|changelog\.md\|phase-\|questions\.md'`), and every one that loads a record reader by path (executed, `git grep -ln '"chain_check.py"\|"optin.py"\|"routing.py"\|"unverified_check.py"\|rule_changes.py"'`). Each hit was opened at the coordinate below (read).

| Record | Field | Written today by | Read by |
|---|---|---|---|
| `trail/rounds/round-N.md` | `target:`, `original:` | the proofer, by hand from `templates/records/sdd-round.md` | `chain_check.py#read_whole`, `#record_lines`, `#round_of`, `#original_of`, `#originals_of` (`:1275-1388`, `:1858-1938`); `pr_body.py#_round` copies `target:` through `chain_check.label_of` |
| the same | `## Findings`, `### <n>. <symptom>` | the proofer | `chain_check.py#sections_of`, `#finding_spans`, `#finding_number` (`:997-1031`) |
| the same | `severity:`, `location:`, `evidence:`, `regression:`, `reopens:` | the proofer | `chain_check.py#findings`, `#finding_of` (`:1065-1213`); `pr_body.py` copies each |
| the same | `verdict:` | the proofer writes `open`; the fix pass rewrites it in place; the orchestrator writes `deferred <home>` for a finding it closes | `chain_check.py#finding_of`, `#records`, `#channel`, `#verdict_problems`; `.github/scripts/release_seal.py#chain_counts` and `skills/verify/scripts/broad_gate.py#rounds_rows` through `chain_check.record_findings` and `#issue_of`; `evals/scripts/replay_targets.py` through `round_of` as the commit that wrote the record holds it; `pr_body.py` copies it |
| the same | `answer:`; the fix pass's coordinate appended to `location:` | the fix pass, in the proofer's finding | `chain_check.py#finding_of` counts `answer:`; `pr_body.py` copies it |
| the same | `## Confirmations`, `confirms:` | the proofer | `chain_check.py#confirmations`, `#confirmations_span`, `CONFIRMATIONS_TABLE` (`:567`, `:1056`, `:1329`) |
| the same | a line that opens like any label above | nobody means to | `chain_check.py#opens_like`, `#unread_lines` (`:523-546`, `:1032-1055`), as notices |
| the same | the file name `round-N.md` | the proofer | `hooks/lib/routing.py#round_number`, `#rounds`; `chain_check.py#round_records`; `settle.py` and `release_seal.py` count through `routing.rounds` |
| `guarantee.md` | `Target SHA` row with its `; earlier run: <sha> <word>` chain | the sealer, by hand | `chain_check.py#target_of`, `#target_row`, `#earlier_verdicts` (`:1497-1531`, `:2009`); `seal_stamp.py#queue_for_written_guarantee`, `#sealed_before`, and the values at `:1247` |
| the same | `Verdict:` with `reason:` or `question:`; a line that opens like it | the sealer | `chain_check.py#verdicts_of`, `#unread_verdicts`, `#verdict_word` with `RETIRED_VERDICTS` (`:154-171`, `:1965-2008`); `seal_stamp.py` through `verdicts_of` and `verdict_word` |
| the same | `original:` | the sealer, where owed | `chain_check.py#originals_of` with `direct` |
| the same | `Broad gate` row | the sealer | no script |
| `trail/gate.md` | `Broad gate` row, newest run first, then `; earlier run: …` | `seal gate --record`, a command (`broad_gate.py#kept_runs` at `:2462`) | `chain_check.py#newest_run`, `#broad_gate` (`:1532`, `:1939`); `seal_stamp.py:1249`; `pr_body.py#_gate` copies the table |
| `routing.md` | the `\| Axis \| Answer \|` table: `Review`, `Destination`, `Planning`, `Implementation`, `Automation`, `Answer pressed`, `Branch` | the orchestrating session, by hand from `templates/records/sdd-routing.md` | `hooks/lib/routing.py#parse` through `hooks/lib/blocks.py#walk`; `hooks/routing-edit-gate.py`, `hooks/question-gate.py`, `hooks/dispatch.py`, `chain_check.py#frame`, `settle.py#declared_branch`, `release_seal.py`, `seal_stamp.py`, `replay_targets.py` |
| `frame/design.md` | the foot mark `Framed <date> by <who>, before the build.` and `Reframed` lines | the framer | `chain_check.py#frame_foot` (`:1598`) against `Planning` |
| the same | `## Rule changes` items and the no-change block | the framer | `skills/settle/scripts/rule_changes.py#parse`; `chain_check.py#rule_changes_read`; `settle.py`; `.github/scripts/rules.py` through `pending` and `removed_by` |
| `frame/plan.md` | `## Phases` | the framer, the builder's Status cells | `pr_body.py` copies the section |
| the same | `## Judgments of the run` table | the orchestrator | `settle.py#judgments` through `hooks/lib/config.py#gfm_table`, with a near heading named |
| `frame/questions.md` | every table line | the framer and each row's answerer | `pr_body.py` copies them |
| `gaps.md` | `## Not verified` table, `closed`, the no-change block; `## Not done` | the builder | `unverified_check.py`, against the merge base as well; `settle.py#open_rows`; `pr_body.py` copies both sections |
| `changelog.md` | the fragment, its `### Process changes` table | the orchestrator | `.github/scripts/publish_release_note.py#fragments`, `#split_process`; `pr_body.py` copies it |
| `trail/phases/phase-N.md` | the file name | the builder | `pr_body.py` lists the paths |
| The comment's two readers, outside the records | `name:` and `skills:` of an agent's frontmatter; a workflow job's `- name:` steps | a person, in the plugin's own files | `payload_meter.py#frontmatter`, `broad_gate.py#job_steps`, each splitting with `str.splitlines` |

### Labelled lines against marked blocks

| | Labelled lines, as #1167 left them | `seal` blocks, assembled from the templates, disassembled by one reader, stacked |
|---|---|---|
| Where a field is | any line of the record outside a fence, placed by headings | a line inside a fenced block opened by three backticks and `seal`, placed by the finding heading around it |
| What a reader decides about a prose line | whether it opens like one of 12 labels (`OPENS_LIKE`, `OPENS_LIKE_VERDICT`), to name it | nothing: prose is never a field; the one look-alike named is a fence opener near the block's |
| A misspelt field | prose, named as not read; refused only where its absence is owed | inside a block, refused at its line with the keys its kind takes; outside, prose, and refused where its absence is owed |
| A close | the fix pass edits three lines of the proofer's finding: `verdict:`, `answer:`, and `location:` where the fix went elsewhere | the fix pass appends a close block under the finding and edits nothing of the proofer's; a finding with none is open |
| A later sealer run | rewrites the `Target SHA` row with each earlier run as `; earlier run: <sha> <word>`, a cell grammar read in two places | appends a verdict block; the last is the newest, the rest are the earlier runs |
| A later broad run | the command rewrites the one `Broad gate` cell, newest first | the command appends a `run:` block |
| Where the grammar lives | `docs/the-review-record.md` *The round record*, loaded at import, which a pull request may not edit | `hooks/lib/fields.py`, edited in place; the template shows it and a case reads the template through it |
| What it removes | nothing more; each later reader fix (#1122, #1128's R2) is one more patch to the same mechanism | the line nets, the retired verdict words, the docs loader, the `Target SHA` and `Broad gate` cell grammars, the stamp's own cell split, the in-place close; `## Removes` has each with its coordinate |
| What it costs | each new near miss a round finds | `chain_check.py`'s record and guarantee readers rewritten (about 550 of the 1,057 lines its record-reading functions hold, executed, `ast` over the file), `pr_body.py`'s copy, `seal_stamp.py`'s reads, `broad_gate.py#kept_runs`; two templates; the proofer's, the crafter's and the sealer's instructions; `tests/skills/test_chain_check.py` (148 cases), `test_seal_stamp.py` (103), `test_pr_body.py` (16), `test_broad_gate.py` (190, five naming the earlier-run cell), `tests/behaviour/test_the_sealer_guarantees.py` (16) (executed, `grep -c '^\s*def test_'`); nine proofer graders and five sealer cases, whose recorded runs no longer compare |
| A record written before the change | read as it stands | refused, with one message naming the template (Scope item 9) |

### Why build, and what a block does not fix

**Build.** The core asks a script to read a form exactly and to name what only looks like it. With labelled lines the form is any of twelve labels on any line of a record, so the naming has to classify every line of prose, and that classifier is where #1167's rounds went. With a block the form is one fence opener, and naming it classifies one line kind. The block takes the guess out of a reader rather than moving it: every field's absence still fails closed, so nothing a prose line held passes silently. A close outside a block leaves its finding open, which is refused. A `regression:` or `reopens:` outside a block leaves the earlier finding unnamed, which is refused. A `Verdict:` outside a block leaves the guarantee with no verdict, which is refused. Stacking gives each block one writer, which `docs/the-review-record.md` *The round record* already asks of a finding's closing lines, and it makes the sealer's and the gate's earlier runs blocks instead of a list inside a table cell.

The scope is the three records whose readers read only the work item in flight: the round records, `guarantee.md` and `trail/gate.md`. The other records keep their forms (Out, below).

**Where this is narrower than the issue's *Done when*, and why each remaining form already meets it.** The issue says "Each record a script reads holds its fields in one marked block" and "Each reader reads the block alone". This frame moves three records into `seal` blocks and keeps the rest in their forms. It also reads the finding heading `### <n>. <symptom>` and `## Findings` outside any block, as an exact heading form that opens a finding's span and gives its number, and not as a field. The issue defines a marked block by three properties: a start and an end a script reads exactly, every line inside it parsing or refused at its line, and nothing outside it read. It names "a table through `hooks/lib/config.py#gfm_table`" as one such body. Each form this work keeps has those properties already:

- **`routing.md`'s `| Axis | Answer |` table.** The exact header starts it, and GFM's table end closes it. `hooks/lib/routing.py#parse` reads it through `hooks/lib/blocks.py#walk` and refuses a doubled row. Nothing outside it is read.
- **`frame/plan.md`'s *Judgments of the run*.** It is a table under an exact header, read through `gfm_table`.
- **`gaps.md`'s `## Not verified`.** It is a table under the exact header `| Item | Who must answer |`, or the no-change block, each read in one spelling by `unverified_check.py`.
- **`frame/design.md`'s `## Rule changes`.** Its exact heading starts it and the next heading ends it. `rule_changes.py#parse` refuses at its line every line that is not an item's, so every line inside parses or is refused.
- **The finding heading.** It is a CommonMark ATX heading of one exact shape. A `###` heading under `## Findings` that is not that shape is refused, and a finding section with no finding block is refused.
- **The frame's foot mark.** It is one line, read exactly at a fixed place.

In each of these forms the near-miss naming that is left covers the start mark only: a heading or header near the exact one. That is the same naming the `seal` opener keeps. So these forms owe no later work to meet the clause, and no follow-up row is filed for them. They also keep their form for a reason of their own. The next settle reads the 8 released designs and plans of 0.26.0, `seal unverified` compares `gaps.md` against the merge base, and `hooks/routing-edit-gate.py` reads this branch's own `routing.md`. Each of those would need a reader of the old form beside the new one for a release (`frame/plan.md` A10).

**What a block does not fix.** When a field is owed stays a rule of its reader, as the issue says: round 4 of #1167 named `original:` where no arm reads it, and a block would not have changed that. A whole finding written inside another fence stays no finding (the limit #1121 R3 left). A finding written as a heading and prose, with no block, still has no fields; its section exists, so it is refused for lacking its block, which keeps the anchor the heading gives (`frame/plan.md` A7).

### The order against milestone 75

| Issue | State | Against this result | When |
|---|---|---|---|
| #1121 | closed in 0.26.0 by #1202 | its R3 limit is restated for blocks in *What the check reads at the pull request* | none |
| #1125 | closed in 0.26.0 by #1202 | `check:` lines of rule files, which no block reaches | none |
| #1122 | open | closed here: the stamp reads the guarantee through the reader the pull request's check reads it through, and queues nothing where that reader refuses, a fence nobody closed among them; its probe is a case seen red at `15a5ce66` | this work, phase 1 |
| #1128 | open | R2, a blank line inside the docs grammar table, is moot: no table is loaded. The six other limits and R16 are about readers of other files, which this work does not touch | after this work, without R2 |
| #1150 | open | kept as filed: `replay_targets.py` reads each record with the `chain_check.py` of the commit that wrote it, through `round_of`, which keeps its signature and return here (Scope item 6), so block records read through the check of their own commit; the 0.22.x layout is #1150's | after this work |
| #1126 | open | kept: where `gaps.md` stands is no field's form, and `gaps.md` keeps its form | after this work |
| #1147, #1197, #1154 | open | no record form | beside, sharing no file |
| #1020 | open | last, as the milestone says; it also edits `chain_check.py` and now reads closes and findings as blocks | last |

## Scope

In. Each item is one decision of this frame; `frame/plan.md`'s Delivers cells cite them by number.

1. **One reader and one spelling of the blocks: `hooks/lib/fields.py`.** It holds the grammar in *Data & interfaces*, Table F, as code. It reads a record's text with `hooks/lib/blocks.py`'s fence walk, which gains the opener's info string, and returns each block's kind, line and fields, each refusal as `(line, why)`, and each notice as `(line, why)`. A notice is a fence opener outside every fence whose info string's first word, case folded, is `seal`, and whose line is not exactly three backticks and `seal`; it changes no exit code. The module also assembles a block from `(key, value)` pairs, the one way a command writes one. It reads nothing outside a block as a field and names no prose line. A hook imports it; `chain_check.py`, `seal_stamp.py`, `pr_body.py` and `broad_gate.py` load it by path, as they load `hooks/lib/routing.py`.
2. **`trail/gate.md` stacks run blocks.** `seal gate --record <item>` appends one block, `run: <tree> against <base commit>`, below the blocks already there, and appends nothing where the last block names the same run. `kept_runs` and `EARLIER_RUN` go from `broad_gate.py`. `chain_check.py#broad_gate` reads the last run block; a file with none is refused with the sentence that names `seal gate --record`. `seal_stamp.py` reads the newest run the same way, and `pr_body.py#_gate` copies the blocks.
3. **`guarantee.md` stacks verdict blocks.** `templates/records/sdd-guarantee.md` holds one verdict block, `target:`, the `original:` line and `Verdict:`, and keeps `## Claims re-run`, `## The parties` and the broad gate's run as tables for people. The sealer appends one block per run and edits no earlier one (`agents/sealer.md`). `chain_check.py#guarantee` reads the last block for the target and the verdict, refuses a guarantee with no verdict block or with any block that does not parse, and keeps the closing-records rule. `originals_of` reads the last block's `original:` for the guarantee. `target_of`, `target_row`, `earlier_verdicts`, `verdicts_of`, `unread_verdicts`, `RETIRED_VERDICTS` and the `Target SHA` constants go.
4. **The stamp reads the guarantee through the same reader, and #1122 closes.** `seal_stamp.py#queue_for_written_guarantee` and `#sealed_before` read through `hooks/lib/fields.py`, and queue or count nothing for a text that reader refuses at any line, a fence nobody closed and a line beginning `<!--` among them. "Drawn once" reads the earlier verdict blocks where it read the `; earlier run:` chain, and keeps the refusal record. A guarantee in the history that holds no verdict block counts nothing. #1122's probe is a case seen red at `15a5ce66`.
5. **Round records stand in blocks, and the docs-loaded grammar goes.** `templates/records/sdd-round.md` holds a round block (`target:`, and `original:` where owed), under each `### <n>. <symptom>` a finding block (`severity:`, `location:`, `evidence:`, and `regression:` or `reopens:` where one is owed), a close block after the fix fence, and one confirmation block per `confirms:` under `## Confirmations`, each followed by its prose. `chain_check.py` reads the round, finding, close and confirmation blocks through the reader, and keeps `## Findings`, the finding heading and every cross-record rule: references, one of `regression:` and `reopens:`, every `fixed` or `rejected` finding named by the next record, `fixed` commits that descend and touch a located path, the last record at HEAD, and the parity arm's `original:`. A finding with no close block is open. The grammar loader (`load` of the document, `section_end`, `code_span`, `table_at`, `grammar`, `grammar_row`, `GRAMMAR_DOC`), the label net (`LABELS`, `SPELT`, `OPENS_LIKE`, `UNREAD_LINE`, `opens_like`, `unread_lines`, `label_of`, `value_of`, `record_lines`), `unread_originals` and `CONFIRMATIONS_TABLE` go. The refusal texts a person reads are pinned, each seen red (contract rules 14 and 15).
6. **The readers of the round records keep their interface.** `chain_check.record_findings`, `round_of`, `issue_of`, `OPEN`, `DEFERRED` and `SHARED_READER` keep their names and return shapes: a finding's `verdict` is `(kind, commit or home)`, and an open finding's is `(OPEN, None)`. So `release_seal.py#chain_counts`, `broad_gate.py#rounds_rows` and `replay_targets.py` need no change. `pr_body.py#_round` copies each round's blocks and each finding's heading and blocks verbatim, and `--check` compares the same.
7. **The writers' instructions say where a field goes.** `agents/proofer.md` (the record and its self-check with `chain_check.py --worktree`, which stays), `agents/crafter.md` (the fix pass appends a close block and edits nothing else in the record), `agents/sealer.md`, `skills/code-review/SKILL.md`, `skills/code-review/orchestration.md` (the orchestrator's close for a finding it files, and its preflight reading), `templates/setup/config.md` *What no row governs* (the info string `seal` and every key stay English), and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, whose sentence that a check names a line spelt otherwise and never refuses it for its spelling becomes: a field a check reads stands inside a `seal` block, a line there that does not parse is refused at its line, and a line outside a block is prose. Every other statement of the moved facts is found with `git grep` on their words and changed in the commit that changes the fact (contract rule 19); `docs/` is `## Rule changes`.
8. **The evals read the new shape.** The nine proofer `shape-findings.md` graders, and the sealer cases' scaffolds and `shape-verdict.md` and `truth-*.md` graders that read a round record, a gate record or a verdict, read blocks. No recorded side is regraded across the change, and no run is part of this work.
9. **A record written before the change is refused with one message.** A round record with no round block, a guarantee with no verdict block and a gate record with no run block are refused by their missing-block refusal. That refusal names the template and says the fields stand in `seal` blocks since 0.27.0. No reader detects the old shape and none reads it. A released work item's records are never judged again (*Grounding*), so the message reaches only a work item whose pull request is open across the upgrade, which rewrites its records, or for the guarantee and the gate record re-runs the sealer and `seal gate --record`, each appending its block below the old text.
10. **The comment's two YAML readers split lines as YAML does.** `broad_gate.py#job_steps` and `payload_meter.py#frontmatter` split at LF after universal newlines, as `deferral_check.py#runners_in` does, and both `# exempt from splitlines: YAML keys` lines go. Each gets a case with a U+2028 inside a line, seen red.
11. **The release.** A feature, `feat:`: a record format and the process that assembles, disassembles and stacks it (the owner, the issue's *Done when*). Milestone 75, `release: 0.27.0`; base `release/v0.27.0` at `15a5ce66`. The fragment commit moves `.claude-plugin/plugin.json` from `0.26.0` to `0.27.0` only where the base does not already read `0.27.0`, since another work item of the milestone, #1154 among them, may merge into the branch first and move it (`docs/branch-and-release.md` *The version is named at the cut*: the branch's first pull request moves it). The orchestrator reads the base's `plugin.json` at the fragment commit. `changelog.md` opens with the feature under `### Added`, keeps `### Changed` for the readers, the templates and the instructions, and holds one `### Process changes` row each for the close block appended by the fix pass and for the sealer appending a block per run. The pull request closes #1122.
12. **The policy root's changes are `## Rule changes` below**, applied at the settle.

Out.

- `routing.md`. Its fields are one GFM table under an exact header, read by the shared walk, which is a marked block in the issue's own terms ("a table through `hooks/lib/config.py#gfm_table`"). `hooks/routing-edit-gate.py` reads it on every edit, this branch's committed `routing.md` among them, so changing its form mid-branch refuses the work item's own edits (`frame/plan.md` A10).
- `frame/design.md`'s `## Rule changes`, `frame/plan.md`'s *Judgments of the run* and `gaps.md`'s `## Not verified`. Each is a closed grammar under one heading, and its near-miss net covers that one heading. Their readers read records written before any change: the settle reads the 8 released designs and plans of 0.26.0 at the next settle, and `seal unverified` compares `gaps.md` against the merge base. A block there would need a second reader for at least a release (A10).
- The frame's foot mark. It is one line at a fixed position, read exactly by `frame_foot`, with no chased edge case on record.
- `frame/questions.md`, `changelog.md` and `trail/phases/`. Their readers copy them and decide nothing.
- A command that writes a finding, a close or a verdict. The agent writes the block with the `Edit` tool from the template and reads it back through `chain_check.py --worktree` (A5).
- A check that the fix pass left the proofer's blocks unchanged (A13).
- A second reader of the old forms (A9).
- `skills/core/SKILL.md`: unchanged (*Grounding*, the third row).
- #1126, #1128, #1150, #1147, #1197, #1154 and #1020: by the order above.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| An open finding | Given a round record whose finding block has no close block, when the check reads it at a ready pull request, then it is refused at the finding's heading as open | `tests/skills/test_chain_check.py` |
| A misspelt key inside a block | Given a close block holding `Verdict: fixed abc1234`, when the check reads it, then it is refused at that line with the keys a close block takes, and the finding has no close | the same, seen red against a reader that skips the line |
| A close written as prose | Given `verdict: fixed abc1234` and `answer: done` on lines outside any block under a finding, when the check reads it, then the finding is refused as having no close block, and no line names the prose | the same |
| A near opener | Given a fence whose opener reads three backticks and `Seal`, when the check reads the record, then one notice names its line as not read, the exit code is the one the missing block gives, and its lines are no fields | the same and `tests/hooks/test_fields.py` |
| A block that never closes | Given a `seal` block with no closing fence, when the check reads it, then it is refused at its opener | the same |
| A block inside the fix fence | Given a finding block written inside a four-backtick fence, when the check reads it, then the finding is refused for lacking its finding block | the same |
| A record from before the change | Given a round record in the 0.26.0 shape, when the check reads it, then it is refused with one message naming `templates/records/sdd-round.md` and the block | the same, seen red against the 0.26.0 reader, which passes the record |
| Two sealer runs | Given a guarantee whose first block reads `Verdict: withheld reason: …` at an older commit and whose second reads `Verdict: sealed` at HEAD, when the check reads it, then it passes, and the stamp queues once | `test_chain_check.py`, `tests/skills/test_seal_stamp.py` |
| #1122 | Given a guarantee whose verdict block reads `sealed`, followed by a fence nobody closed and a second block reading `withheld`, when the guarantee is written, then no stamp is queued and the check refuses the fence | `test_seal_stamp.py`, the case seen red at `15a5ce66` |
| Drawn once | Given an earlier block reading `sealed` whose target this clone did not record refusing, when a later block reads `sealed`, then no second stamp is queued | `test_seal_stamp.py` |
| Two broad runs | Given `seal gate --record` run green at two commits, then `trail/gate.md` holds two run blocks, the second the newer, and the check reads the second | `tests/skills/test_broad_gate.py`, `test_chain_check.py` |
| The body copies blocks | Given a work item with two rounds, when `seal pr-body` writes and `--check` reads, then the copy holds each round's blocks verbatim and `--check` passes | `tests/skills/test_pr_body.py` |
| The release seal counts deferrals | Given a close block reading `deferred #12`, when `release_seal.py#chain_counts` runs, then #12 is counted | `tests/github/test_release_seal.py`, unchanged |
| The templates parse | Given `templates/records/sdd-round.md` and `sdd-guarantee.md`, when each is read through the reader, then every block opens with its kind's key and no line outside a value's placeholder is refused | a case in `tests/hooks/test_fields.py` |
| A YAML line break | Given a step name or a `skills:` entry holding U+2028, when `job_steps` or `frontmatter` reads it, then the line is read whole | `tests/skills/test_broad_gate.py`, `tests/skills/test_payload_meter.py`, each seen red |

## Data & interfaces

### Table F. The block grammar, as `hooks/lib/fields.py` holds it

A block is a fenced code block outside every fence and every HTML comment block, by `hooks/lib/blocks.py#walk`. Its opener is a line of three backticks then `seal`, with nothing before it and nothing after it. It closes where CommonMark closes it. Each line inside is `<key>: <value>`, or `<key>:` where the value's shape takes nothing, with the key spelt as below and one space after the colon. The first line's key names the kind. A line that is not a field of its kind, a key over its count, and a blank line are each refused at their line, and the block is read no further.

| Kind | File | Opens with | Fields, and how many | Where | Writer |
|---|---|---|---|---|---|
| round | `trail/rounds/round-N.md` | `target:` | `target:` one; `original:` at most one | outside every finding; one per record | the proofer |
| finding | the same | `severity:` | `severity:`, `location:`, `evidence:` one each; one of `regression:` and `reopens:` at most | in a `### <n>. <symptom>` section under `## Findings`; one per finding | the proofer |
| close | the same | `verdict:` | `verdict:` one, as `fixed <commit>`, `rejected` or `deferred <home>`; `answer:` one; `location:` at most one | in the finding's section; at most one | the fix pass, or the orchestrator for a finding it closes |
| confirmation | the same | `confirms:` | `confirms:` one | outside every finding; any number | the proofer |
| verdict | `guarantee.md` | `target:` | `target:` one, as `<sha> against <base>`; `original:` at most one; `Verdict:` one, in the three shapes of `chain_check.py#VERDICT_SHAPE` | anywhere; one or more, the last the newest run | the sealer, one per run |
| run | `trail/gate.md` | `run:` | `run:` one, as `<tree> against <base commit>` | anywhere; one or more, the last the newest | `seal gate --record` |

Each value's shape is the `Shape` cell of today's grammar row for that label, moved into the module as it stands, except that `verdict:` loses `open`. The key names are today's labels, so every sentence that names `target:`, `original:`, `verdict:` or `Verdict:` stays true; only the sentences that say where a field stands change.

### Table G. What each reader reads, names and leaves to an agent

| Reader | Reads | Names as not read | Leaves to |
|---|---|---|---|
| `chain_check.py`, the records arm | the blocks of each `round-N.md`, its `## Findings` and finding headings | a fence opener near the block's; a file under `trail/rounds/` that is no `round-N.md` | the verifying round: whether a fix holds; the orchestrator at the preflight: what a named opener meant |
| `chain_check.py`, the guarantee and gate arms | the last verdict block; the last run block | a fence opener near the block's | the sealer: the verdict |
| `seal_stamp.py`, the hook | the verdict blocks, through the same reader | nothing; it queues nothing where the reader refuses | none |
| `pr_body.py` | the blocks and finding headings, copied verbatim | nothing; a record the reader refuses is refused with its sentence | the sealer: whether the parties agree |

## Rule changes

- change
  file: docs/the-review-record.md
  section: The round record
  from: a `target:` line, then `## Findings` with one `### <n>. <symptom>` section per finding, `## Confirmations` where the round confirmed something, `## Not judged` and `## Probes`. A finding holds the labelled lines the table below places in a finding, why it matters with its grounds, and the paste-ready fix in a fenced block.
  to: a `seal` block holding its `target:` line, then `## Findings` with one `### <n>. <symptom>` section per finding, `## Confirmations` where the round confirmed something, `## Not judged` and `## Probes`. A finding holds one `seal` block of its fields, why it matters with its grounds, the paste-ready fix in a fenced block, and, once it is closed, its close block.
- change
  file: docs/the-review-record.md
  section: The round record
  from: **The record's grammar is the table below, and nothing else states it.** Each labelled line and finding heading of a record is one row's, and the check accepts it only where it matches the row's `Shape` whole, stands where `Where` says and is as many as `How many` allows. Otherwise it is refused at its line with the row's `Refused as`. `How many` counts per finding for a line in a finding, and per record for every other line. A label is its `Line` cell exactly: lowercase, at the start of the line, followed by one space or by nothing, with no emphasis and no table cell. A line spelt otherwise, in another case, under emphasis or with a space before the colon, is prose to the check, and the check names it at its line as one it did not read, which changes no exit code. A finding that then lacks a line the table says is `one` is refused as lacking it. An optional line spelt otherwise does what prose does, so a `reopens:` or `regression:` line the check did not read leaves the finding it meant to name unnamed in the next record, which is refused at that finding's heading. Whether the line meant the label is the orchestrator's reading at the preflight and the sealer's at the records, never the check's, and no table of spellings stands beside the grammar: a list of the ways a label is written grows by one row for every near miss a round finds and never converges (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*). Three rules span rows: a finding carries at most one of a `regression:` and a `reopens:` line, no two findings share a heading number, and `## Confirmations` holds no table row. No `Record language` translates a cell of the table.
  to: **The record's fields stand in `seal` blocks, and `hooks/lib/fields.py` is the one spelling of their grammar.** A `seal` block is a fenced block opened by a line of three backticks and `seal`, with nothing before or after them, outside every other fence. The first line of a block names its kind. `target:` opens the round's one block, which stands outside every finding and holds at most one `original:` line. `severity:` opens a finding's one block, which stands in the finding's `### <n>. <symptom>` section with its `location:` and `evidence:` lines and at most one of a `regression:` and a `reopens:` line. `verdict:` opens a finding's close block, at most one in its section, with its `answer:` line and a `location:` line where the fix went to a path the finding does not name. `confirms:` opens a confirmation's block outside every finding. Every line of a block is a field its kind takes, written `<key>: <value>` with the key exactly as the module spells it and the value matching the key's shape whole; a line that is not, a key over its count and a blank line are refused at their line, and the block is not read past it. Nothing outside a block is a field: a line shaped like one in prose decides nothing and is named by nothing, and where a field is owed its absence is refused. A finding with no close block is open. The record holds one `## Findings` heading, under which each `### <n>. <symptom>` heading opens a finding, and no two findings share a number. No `Record language` translates a key, a value's fixed words or the info string. A list of the ways a label is written grows by one row for every near miss a round finds and never converges, and a block leaves a reader nothing to guess: inside it every line is the form, and outside it none is (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*).
- remove
  file: docs/the-review-record.md
  section: The round record
  from: | Line | Shape | Where | How many | Refused as |
    |---|---|---|---|---|
    | `target:` | `target: (?P<commit>[0-9a-f]{7,40})(?: against [\w./-]*\w\|, fixes [0-9a-f]{7,40}\.\.[0-9a-f]{7,40})` | outside every finding | one | it names the reviewed commit as `<sha> against <base>`, or `<sha>, fixes <a>..<b>` for a verifying round |
    | `original:` | `original: (?P<commit>[0-9a-f]{7,40})` | outside every finding | at most one | it names the migration config's baseline commit this round compared against, as 7 to 40 hex digits |
    | `## Findings` | `## Findings` | the record | one | a round record holds one, with a `### ` section and one `verdict:` line per finding |
    | `### <n>. <symptom>` | `### (?P<number>[1-9][0-9]*)\. .+` | `## Findings` | each number once | no number: a finding's heading reads `### <n>. <symptom>`, and a later round names it by that `n` |
    | `severity:` | `severity: (?:must\|should)` | a finding | one | a severity is `must` or `should` |
    | `location:` | `` location: `[^`\s:/#][^`\s:#]*(?::[0-9]+(?:-[0-9]+)?)?`(?:, `[^`\s:/#][^`\s:#]*(?::[0-9]+(?:-[0-9]+)?)?`)* `` | a finding | one | a location is one or more of `path`, `path:line` or `path:first-last`, each backticked, joined by `, ` |
    | `evidence:` | `` evidence: (?:executed `[^`]+`(?:, `[^`]+`)*\|read `[^`\s:/#][^`\s:#]*:[0-9]+(?:-[0-9]+)?`(?:, `[^`\s:/#][^`\s:#]*:[0-9]+(?:-[0-9]+)?`)*) `` | a finding | one | evidence is `executed` and each command run, or `read` and each `path:line` or `path:first-last` opened, each backticked, joined by `, ` |
    | `verdict:` | `verdict: (?:open\|rejected\|fixed (?P<commit>[0-9a-f]{7,40})\|deferred (?P<home>\S(?:.*\S)?))` | a finding | one | a verdict is `open`, `fixed <commit>`, `rejected` or `deferred <home>` |
    | `regression:` | `regression: round-(?P<round>[1-9][0-9]*)(?:#(?P<finding>[1-9][0-9]*))?` | a finding | at most one | a reference is `round-<N>#<n>` or `round-<N>` |
    | `reopens:` | `reopens: round-(?P<round>[1-9][0-9]*)#(?P<finding>[1-9][0-9]*)` | a finding | at most one | a reopened close is a finding's, so the reference is `round-<N>#<n>` |
    | `answer:` | `answer:(?: .*)?` | a finding | one | an answer is prose after the label |
    | `## Confirmations` | `## Confirmations` | the record | at most one | each entry is a `confirms:` line at the start of a line, then its prose |
    | `confirms:` | `confirms: (?:none\|round-(?P<round>[1-9][0-9]*)#(?P<finding>[1-9][0-9]*))` | `## Confirmations` | any | it is `round-<N>#<n>` or `none` |
- remove
  file: docs/the-review-record.md
  section: The round record
  from: **`chain_check.py` reads the table from this section and stops at exit 2 where it cannot.** It loads it once, when it is imported, from `docs/the-review-record.md` beside itself, which every copy of the plugin carries, the hygiene workflow's clone among them. It finds the table by this section's heading and its header row. A document it cannot open, a section or a header row it cannot find, and a row it cannot read stop it at exit 2 naming this file, never a pass. A row of the first table it cannot read is one whose shape does not compile, whose `Where` or `How many` is a word the table does not use, a row the check reads a meaning from that is missing, one whose shape lacks the named part, such as `(?P<commit>…)`, the check reads out of it, or one that stands where the check does not look for it or whose `How many` the check cannot keep. `target:` stands outside every finding and is `one`, and `original:` stands there and is `at most one`. `location:`, `verdict:`, `regression:` and `reopens:` stand in a finding, and since the check reads one line of each, the first two are `one` and the last two `one` or `at most one`. `confirms:` stands in `## Confirmations`. Every other row may take any `Where` and `How many` the table uses for its kind, because the check counts each: a section, or a line in a section, that the table says is `one` is refused where a record leaves it out, `## Confirmations` included. So a change that moves this heading or either table moves the loader's path in the same commit, or every check that reads a record stops. check: tests/skills/test_chain_check.py
- change
  file: docs/the-review-record.md
  section: The round record
  from: The proofer writes `open`; the fix pass answers with `fixed <commit>`, `rejected` (the finding does not hold, and `answer:` says why) or `deferred <home>`.
  to: A finding with no close block is open; the fix pass's close block answers it with `fixed <commit>`, `rejected` (the finding does not hold, and `answer:` says why) or `deferred <home>`.
- change
  file: docs/the-review-record.md
  section: The round record
  from: **The fix pass writes two lines per finding and nothing else in the file.** It rewrites the finding's `verdict:` line, with the commit for `fixed`, and writes its `answer:` line: what was done, why the finding does not hold, or where it went. Where its fix went to a path `location:` does not name, it appends that coordinate to the line, joined by `, `, and its answer says so.
  to: **The fix pass appends one close block per finding and edits nothing else in the file.** The block stands in the finding's section, after its paste-ready fix, and holds its `verdict:` line, with the commit for `fixed`, and its `answer:` line: what was done, why the finding does not hold, or where it went. Where its fix went to a path the finding's `location:` does not name, the close block carries a `location:` line naming it, and its answer says so. The finding's own block is the proofer's and is never edited.
- change
  file: docs/the-review-record.md
  section: The round record
  from: **Each finding's `verdict:` and `answer:` lines have one writer, and the lines closed at one step reach the branch in a single commit.** A finding a fix pass answers is the pass's to write: it writes both lines last,
  to: **Each finding's close block has one writer, and the blocks written at one step reach the branch in a single commit.** A finding a fix pass answers is the pass's to close: it writes the close block last,
- change
  file: docs/the-review-record.md
  section: The round record
  from: the orchestrator writes and commits the lines of every finding it closes at that step together. A second hand on either line gives a reader nothing:
  to: the orchestrator writes and commits the close block of every finding it closes at that step together. A second hand on a close block gives a reader nothing:
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: **Of a round record the check reads its labelled lines, and refuses what it cannot read.** It reads every line *The round record*'s table has a row for, and a ready pull request fails for any line that table refuses. It names each file under `trail/rounds/` whose name is no `round-N.md` as one it did not read, so a record under another name is a line of the check's output and never a silent pass, and it names each line outside a fence that opens like a label and is not one. It fails, too, while a finding reads `open`; for a `fixed` naming a commit HEAD does not descend from, or one that changed no located path; for a reference naming no earlier record, or a finding that record does not hold, and any reference in round 1; and for a `fixed` or `rejected` finding the next record names on no `confirms:`, `reopens:` or `regression:` line. A labelled line inside a fence is not a line, so a finding whose only verdict stands in its fix block has none, and a whole finding written inside a closed fence is no finding: a fenced block is the paste-ready fix by the template, and the orchestrator's read of the record before its commit, against the template, is what catches a finding written there. A fence that never closes, which would hide every finding after it, is refused at the line that opened it.
  to: **Of a round record the check reads its `seal` blocks and its finding headings, and refuses what it cannot read.** It reads every block *The round record* describes, and a ready pull request fails for any line that grammar refuses. It names each file under `trail/rounds/` whose name is no `round-N.md` as one it did not read, so a record under another name is a line of the check's output and never a silent pass, and it names each fence whose info string's first word, case folded, is `seal` and whose opener is not the block's, which changes no exit code. It fails, too, while a finding has no close block; for a `fixed` naming a commit HEAD does not descend from, or one that changed no path the finding's or its close's `location:` names; for a reference naming no earlier record, or a finding that record does not hold, and any reference in round 1; and for a `fixed` or `rejected` finding the next record names on no `confirms:`, `reopens:` or `regression:` line. A `seal` block inside another fence is part of that fence, so a finding whose block stands inside its fix block lacks its finding block and is refused for it, and a whole finding written inside a closed fence is no finding: the orchestrator's read of the record before its commit, against the template, is what catches it. A record written before the fields stood in blocks holds no round block, and is refused with one message naming the template. A fence that never closes, which would hide every block after it, is refused at the line that opened it.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: `seal gate --record <item>` writes `<tree> against <base>` there on a green run, newest first, every earlier run kept behind it as `; earlier run: …`. At a ready pull request its newest run is HEAD, or only the work item's records follow it.
  to: `seal gate --record <item>` appends there, on a green run, a `seal` block holding `run: <tree> against <base>`, below the block of every earlier run, and appends nothing where the last block names the same run. At a ready pull request its newest run, the last block, is HEAD, or only the work item's records follow it.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: One of the old shape under an item this pull request carries has no `## Findings` section, and is refused by name. A work item in flight across a change to the table meets the change as its records stand: a renamed line is rewritten into its new spelling, and an added line is never supplied after the round that would have written it, so an item whose records predate an added line merges before the change or has its rounds written after it.
  to: A record of an older shape under an item this pull request carries holds no round block, and is refused with the message that names the template. A work item in flight across a change to the grammar meets the change as its records stand: its round records are rewritten into blocks, and its `guarantee.md` and `trail/gate.md` take a block below their old text when the sealer and `seal gate --record` run again. An added field is never supplied after the round that would have written it, so an item whose records predate an added field merges before the change or has its rounds written after it.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: every round record of a work item declaring `through the review chain` carries one `original:` line naming the migration config's baseline.**
  to: every round record of a work item declaring `through the review chain` carries one `original:` line in its round block naming the migration config's baseline.**
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: `straight to the PR` carries one `original:` line naming the migration config's baseline.**
  to: `straight to the PR` carries one `original:` line in its newest verdict block naming the migration config's baseline.**
- change
  file: docs/the-review-record.md
  section: The guarantee
  from: **Its verdict is `guarantee.md`, from `templates/records/sdd-guarantee.md`**: the commit and base, the broad gate's result, the claims re-run, the parties compared, and one `Verdict:` line, `sealed`, `withheld reason: <the claim, its party, its coordinate>` or `undecided question: <the question, for the owner>`, written exactly so and with no emphasis. A line that opens like the label and is not it is prose, named by the check as one it did not read, and a guarantee with no `Verdict:` line, or with two, is refused naming the file. The `Target SHA` row holds `<sha> against <base>`, each one word, then nothing or one `; earlier run: <sha> <word>` entry per earlier run, with `against <base>` after its SHA where it names one and its verdict's word alone; any other text on the row is refused at it. An undecided question is the owner's: the answer goes on a line under the verdict, and the sealer runs again at the new HEAD.
  to: **Its verdict is `guarantee.md`, from `templates/records/sdd-guarantee.md`**: the broad gate's run, the claims re-run and the parties compared, in tables for people, and one `seal` block per run of the sealer, appended below the blocks of earlier runs and never edited after its run. A verdict block holds `target: <sha> against <base>`, each one word, the `original:` line where *What the check reads at the pull request* owes one, and one `Verdict:` line, `sealed`, `withheld reason: <the claim, its party, its coordinate>` or `undecided question: <the question, for the owner>`, written exactly so. The last block is the newest run and the others are the earlier runs, which the stamp reads. A guarantee with no verdict block, or with a line of a block that does not parse, is refused naming the file and the line. An undecided question is the owner's: the answer goes on a line below the newest block, and the sealer runs again at the new HEAD and appends its block.
- change
  file: docs/the-review-record.md
  section: The guarantee
  from: **A ready pull request passes only where `guarantee.md` names HEAD and reads `sealed`.**
  to: **A ready pull request passes only where the newest verdict block of `guarantee.md` names HEAD and reads `sealed`.**
- change
  file: docs/the-review-record.md
  section: The guarantee
  from: `withheld`, `undecided`, an unfilled template, two `Verdict:` lines or a stale commit each fail naming the file; a draft prints them. A word the verdict used before it read `sealed` fails naming its line and saying the word changed.
  to: A newest block reading `withheld` or `undecided`, an unfilled template, a block that does not parse or a stale commit each fail naming the file; a draft prints them.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: Where its one `Verdict:` reads `sealed`,
  to: Where the reader the pull request's check reads it through refuses none of its lines and its newest verdict block reads `Verdict: sealed`,
- change
  file: docs/the-review-record.md
  section: The stamp
  from: or whose `Target SHA` row's `; earlier run:` chain reads `sealed`, counts as stamped then, which holds across clones; the earlier-run chain alone skips a `sealed` this clone recorded refusing (the next rule).
  to: or one of whose earlier verdict blocks reads `sealed`, counts as stamped then, which holds across clones; the earlier blocks alone skip a `sealed` this clone recorded refusing (the next rule). A guarantee in the history that holds no verdict block, written before the fields stood in blocks, counts nothing.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: There once is held by that, by the `Target SHA` row's earlier-run chain, and by the audited commit
  to: There once is held by that, by the earlier verdict blocks, and by the audited commit
- change
  file: docs/the-review-record.md
  section: The stamp
  from: and the earlier-run chain skips a `sealed` this clone recorded, so the sealer's new audit draws the work item's one stamp.** The new audit keeps the refused verdict on its `Target SHA` row as `; earlier run: <sha> sealed`, and without a record the chain would count that entry as the stamp.
  to: and an earlier verdict block reading `sealed` that this clone recorded refusing is skipped, so the sealer's new audit draws the work item's one stamp.** The new audit's block stands below the refused verdict's block, and without a record that earlier block would count as the stamp.
- change
  file: docs/the-review-record.md
  section: The stamp
  from: The hook judges a write's newest verdict alone, never the `; earlier run:` chain,
  to: The hook judges a write's newest verdict block alone, never the earlier blocks,
- change
  file: docs/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: Its template holds headings, table headers, placeholders, the labelled lines the record's grammar asks for and the foot line, and nothing else.
  to: Its template holds headings, table headers, placeholders, the `seal` blocks the record's grammar asks for and the foot line, and nothing else.
- change
  file: docs/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: **A record holds a fence only around a finding's paste-ready fix, and a labelled line a check reads stands outside every fence, at the start of its line.** The readers keep one fence state, by the fence rule of `hooks/lib/blocks.py`, because a fix to a record's own grammar can hold a line shaped like a label, and that line belongs to the fix.
  to: **A record holds a fence around a finding's paste-ready fix and around each of its `seal` blocks, and a field a check reads stands inside a `seal` block and nowhere else.** The readers keep one fence state, by the fence rule of `hooks/lib/blocks.py`, so a `seal` block quoted inside a fix belongs to the fix and is not read, and `hooks/lib/fields.py` is the one reader of the blocks.
- change
  file: docs/what-a-script-gates.md
  section: Which gate a script holds
  from: or a line of the plugin's own forms in the one spelling the form gives it, such as `verdict:` at the start of a line or the header `| Pact | Clause | Hash |`.
  to: or a line of the plugin's own forms in the one spelling the form gives it, such as a field inside a `seal` block or the header `| Pact | Clause | Hash |`.
- change
  file: docs/what-a-script-gates.md
  section: The checks
  from: | `hooks/sealer-stamp-queue.py`, `hooks/sealer-stamp.py` | the write of `guarantee.md`; the turn's end | the one `Verdict:` line, through `chain_check.verdicts_of` | queues nothing where the file holds no one `Verdict: sealed`; a line spelt otherwise is named by the check | the verdict is the sealer's |
  to: | `hooks/sealer-stamp-queue.py`, `hooks/sealer-stamp.py` | the write of `guarantee.md`; the turn's end | the verdict blocks, through `hooks/lib/fields.py` | queues nothing where the reader refuses a line of the file or the newest block does not read `Verdict: sealed` | the verdict is the sealer's |
- change
  file: docs/what-a-script-gates.md
  section: The checks
  from: routing rows; the frame's mark; `## Rule changes` through `rule_changes.py`; the round records' labelled lines in one spelling each; `trail/gate.md`; `guarantee.md`'s rows and verdict line; the branch's commits and `Seal-Routing` trailers; `seal/parity.md`'s `Baseline commit` | refuses at its line a required line it cannot read; names each file under `trail/rounds/` it did not read and each line that opens like a label and is not one; a line spelt otherwise is prose |
  to: routing rows; the frame's mark; `## Rule changes` through `rule_changes.py`; the `seal` blocks of the round records, `trail/gate.md` and `guarantee.md` through `hooks/lib/fields.py`, and the finding headings; the branch's commits and `Seal-Routing` trailers; `seal/parity.md`'s `Baseline commit` | refuses at its line a block line that does not parse, and a required block that is absent; names each file under `trail/rounds/` it did not read and each fence opener near the block's; a line outside a block is prose |

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The grammar table of a round record, and the loader that reads it at import (`GRAMMAR_DOC`, `GRAMMAR_SECTION`, `GRAMMAR_COLUMNS`, `section_end`, `code_span`, `table_at`, `grammar`, `grammar_row`, and the `GRAMMAR = grammar(...)` call) | `docs/the-review-record.md` *The round record* (`## Rule changes`); `skills/code-review/scripts/chain_check.py:195-199`, `:326-510` | `hooks/lib/fields.py`, Table F; a pull request edits the module in place, and #1128's R2 goes with the loader |
| The label net (`LABELS`, `SPELT`, `OPENS_LIKE`, `UNREAD_LINE`, `opens_like`, `unread_lines`) and the line-by-line placement (`label_of`, `value_of`, `record_lines`, `counted` for lines outside findings) | `chain_check.py:523-546`, `:896-908`, `:1032-1055`, `:1248-1300` | no prose line is a field, so none is classified; each field's absence is refused where owed; the one naming left is a near fence opener, in the module |
| The verdict net and the retired words (`OPENS_LIKE_VERDICT`, `UNREAD_VERDICT`, `unread_verdicts`, `RETIRED_VERDICTS`, `RETIRED_SAYS`, the retired branch of `verdict_word`, `verdicts_of`) | `chain_check.py:154-171`, `:1965-2008` | a `Verdict:` line is read inside a verdict block, where a value outside its three shapes is refused at its line with the shapes; the old words need no list |
| `unread_originals` | `chain_check.py:1882-1894` | `original:` is a field of the round and verdict blocks |
| The `Target SHA` row's cell grammar (`TARGET`, `COMMIT_WORD`, `BASE_WORD`, `TARGET_HEAD`, `EARLIER_ENTRY`, `TARGET_WRITTEN`, `target_of`, `earlier_verdicts`, `target_row`, and `fields`, `field`, `table_rows` where nothing else calls them) | `chain_check.py:120`, `:178-193`, `:870-893`, `:1497-1531`, `:2009-2016`; `templates/records/sdd-guarantee.md`'s `Target SHA` row | the verdict blocks, stacked; the last is the newest run and the rest are the earlier runs |
| The `Broad gate` cell's `; earlier run:` list (`EARLIER_RUN` and `newest_run` in the check, `EARLIER_RUN` and `kept_runs` in the writer) | `chain_check.py:173`, `:1532-1539`; `skills/verify/scripts/broad_gate.py:164`, `:2462-2468` | the run blocks the command appends |
| The stamp's own reading of the guarantee (`chain.verdicts_of`, `chain.target_of`, `chain.table_rows`, `chain.field`, `chain.earlier_verdicts`, and its split of the cell) | `skills/verify/scripts/seal_stamp.py:1164-1167`, `:1247-1249`, `:1347-1361` | `hooks/lib/fields.py`, the reader the pull request's check reads through, which also refuses the fence #1122 names |
| `CONFIRMATIONS_TABLE` and the rule that `## Confirmations` holds no table row | `chain_check.py:567`, `:1354`; `docs/the-review-record.md` *The round record* (`## Rule changes`) | a confirmation is a block; a table under the heading is prose |
| The proofer's `verdict: open` line, and the fix pass's three edits into the proofer's finding: rewriting `verdict:`, writing `answer:`, appending to `location:` | `templates/records/sdd-round.md`; `docs/the-review-record.md` *The round record*; `agents/crafter.md`, the fix pass | the close block the fix pass appends; a finding with none is open |
| The sentence that a check names a line spelt otherwise and never refuses it for its spelling | `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | rewritten in place (Scope item 7): inside a block a line that does not parse is refused at its line, and outside a block a line is prose |
| `# exempt from splitlines: YAML keys`, twice | `broad_gate.py:2161`, `skills/verify/scripts/payload_meter.py:249` | the split at LF after universal newlines, which the census does not flag |

Framed 2026-10-31 by framer, before the build.
