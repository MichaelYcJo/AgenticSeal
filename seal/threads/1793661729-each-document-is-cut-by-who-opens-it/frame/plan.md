# Implementation Plan: 1793661729-each-document-is-cut-by-who-opens-it

## Technical context

The work stands on these coordinates, each read by the framer at 2d38c75af:

- `skills/core/SKILL.md` *The first value* (lines 25-110) takes the rule.
  The sentence D2 removes stands at lines 85-90.
- `skills/agent-contract/SKILL.md` *20 Do not avoid the change a problem calls
  for* is 388 bytes (`awk | wc -c`, executed). Its only citation by number is
  a comment in `tests/text/test_the_rules_have_one_owner.py:206` (`git grep`,
  executed).
- `skills/implement/SKILL.md:73` holds the `docs/` row whose clause "a pull
  request does not edit it" D9 replaces. No other file states that clause
  (`git grep`, executed).
- `skills/settle/scripts/rule_changes.py#parse` (lines 152-278) holds the
  top-level check at lines 257-260.
- `skills/settle/scripts/fold_check.py#documents` (line 128) and
  `#index_problems` (line 174) read only the policy root's top level.
- `.github/scripts/rules.py:75` globs `docs/*.md`, and so does
  `.github/scripts/release_report.py:53`. `#preloads` (line 97) is S2's
  measure.
- `skills/settle/SKILL.md` (43,170 bytes), `skills/implement/SKILL.md`
  (30,663) and `skills/verify/SKILL.md` (25,263) are the three skills cut
  (`wc -c`, executed). Section sizes are in `frame/design.md` *Grounding*.
- 708 lines in 151 files outside `seal/` name a `docs/<name>.md` path
  (`git grep -c`, executed). Phase 5 re-points the ones naming a moved path.

What breaks in six months with the chosen approach:

- **A cross-reference with no path.** An italic cross-reference inside a moved
  section that phase 5 missed names a section of another document. No case
  reads such a reference (`frame/design.md` D7), so a reader follows it into
  the wrong file until a review finds it.
- **A user's subdirectory.** Where a user's index happens to name one file in
  a subdirectory of the policy root, `seal fold` measures that subdirectory's
  other files and holds them to the index from 0.30.0 on. It prints them and
  refuses nothing.
- **The boundary's judgment.** A work item that touches code and policy
  together may be framed as either kind. Two such items on one release could
  edit one section directly, which is what the boundary exists to prevent,
  and only the proofer reading the framer's call catches it (D9).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Cut and group the policy root in this pull request, under the boundary D9 states (chosen) | the boundary is a judgment no script holds, so a mis-framed work item edits the root directly beside another that does the same; a path-less cross-reference inside a moved section may be missed (D7) | chosen by the owner on 2026-11-03 (issue body, the paragraph after *What changes*): the subject here is the documents themselves, and restructuring them is recurring work |
| Group the policy root through a new `move` operation in `## Rule changes`, with the settle placing each move and rewriting the moved paths (the frame at 7849e7757 and 4acbbd215) | the benefit waits a release; the settle after 0.30.0 places 23 moves and rewrites hundreds of lines; the grammar and the settle gain an operation and a rewrite no other design needs | rejected by the owner's decision: a work item whose subject is the policy root edits it as the settle does, and this work item is the only unsettled design on `release/v0.30.0` (`ls seal/threads`, executed), so the settle would have no decision to gather. The `move` operation, the path rewrite and the excuser change leave the frame with it |
| Keep `docs/` flat and cut `docs/the-review-record.md` into five top-level documents | 22 top-level documents in one list, each reader finding its own through the index alone; the owner's item 4 unmet | rejected: the cost it saves is D4's readers, paid once, while every reader of the root pays for the flat list |
| Move documents through today's operations, a `remove` of the old document and an `add` whose `to` holds its text | the design would hold about 260 KB of the policy root verbatim, for the settle to paste back | rejected with the settle-moves approach |
| Re-point the 708 lines with a script | a substitution through the shell can miss and exit zero, and this spawn's rules forbid a script that rewrites a file (contract rule 9) | rejected: each file is edited through the `Edit` tool, `replace_all` per old path, and `git grep` of each old path proves the list empty (S8) |
| Group `skills/` into categories, or `agents/` into subfolders | a category-level skill is not documented as found and may stop loading; a subfolder renames every agent (orchestrator's finding of the Claude Code docs) | rejected for both directories |
| Put the cut rule in a policy document and leave the core as it is | every party writes documents and skills, and a rule only the orchestrator's documents state is not in front of an agent that writes a skill or a frame | rejected: the issue puts it in the core, and D2 pays its bytes |
| Pay D1's bytes by trimming each agent definition | five edits for one fact, and the tracer's 2,956-byte definition has little an agent does not act on | rejected: the offset is taken in the core and the contract, which every agent shares (D2) |
| Cut `skills/implement/SKILL.md` into one file per agent | the crafter reads most of it at every spawn anyway, and the parts it never reads are the orchestrator's, which already has `orchestration.md` | rejected in favour of moving the orchestrator's parts there (D5) |
| Cut the `orchestration.md` files by step | one reader holds them in one session, so a cut turns one read into several in the same context | rejected; out of scope (`frame/design.md` *Scope*) |
| Measure with a paid behaviour-suite run on both trees | `evals/README.md` *The behaviour suite* makes no later edit owe a run, and #1254 is narrowing that suite; a paid run measures recall, not what a spawn reads | rejected: D8's replay reads the reading itself, at no cost |
| Wait for the live run under the installed 0.30.0 and report only that | this pull request carries no reading | rejected as the only reading; kept as Q1, the live confirmation |
| Keep `docs/what-a-script-gates.md` in `checks/` and name the proofer in that group's line; or move `docs/the-routing-check.md` to `running/` because contract rule 9 cites it | a group line that names one agent and one section copies a citation, and goes stale when the citation moves. The routing check's agent-side citations give the reason for an act their own text states, so moving it would put a hook's reference in the group an agent acts on | rejected: `what-a-script-gates.md` moves to `running/`, since the proofer acts on it, and `checks/`'s line says how an agent-side citation into it reads (`frame/design.md` D3, the citation check) |
| Give each moved document a line naming its reader at its top | fifteen sentences restating the reader the group's index table states once | rejected: the group states it once; a new document states it, since it is written here (D3) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* 5 and D9: the boundary written into `skills/implement/SKILL.md` *Document layout*, S11; then the copies of D6 on both sides, `docs/the-review-record.md` *The run* among them | S11's `git grep`; the ten-word census re-run, its command and list in the phase record; the modules that read the changed files (`tests/hooks/test_question_gate.py` and any case pinning the removed text), run narrow | 4c4925bff |
| 2 | *Scope* 3: D4 whole, with S5 and S6; `skills/settle/SKILL.md` *Rule changes*, `templates/setup/config.md` *The fold's values* and `skills/config/SKILL.md` on group directories | new cases for S5 and S6, each seen red first; the settle's, fold's, rules' and release report's test modules, run narrow; the reader list's two `git grep` commands pasted in the phase record | 953699548 |
| 3 | *Scope* 2 for `settle` (D5's first row) and *Scope* 6 for its citations: the four supporting files, the ceiling sentence rewritten to the reader rule, and every citation re-pointed, the three in `docs/` among them; S3 | `tests/behaviour/test_a_cited_section_stands_in_its_file.py`; the settle's test modules | a5b6a06eb |
| 4 | *Scope* 2 for `implement` and `verify` (D5's other rows) and *Scope* 6 for their citations, the core's citation of *1.* among them; S4 | the cited-section case; the modules that read the two skills; bytes of `skills/implement/SKILL.md` before and after in the phase record | 362f8777f |
| 5 | *Scope* 4 and 6: D3 whole. The seven new documents with their titles and reader sentences; the section moves; `git mv` of the fifteen documents; `docs/the-review-record.md` deleted; `docs/README.md` rewritten into five group tables; every citation of a moved path re-pointed, path-less cross-references included (D7); the axis sentence in *Document layout*; the `ls seal/threads` record D9 asks for; S7 and S8 | S7's comparison and S8's `git grep`, commands and output in the phase record; the cited-section case; `seal fold`; the modules the moved paths' readers live in, run narrow | 2e7a946c9 |
| 6 | *Scope* 1: D1 and D2; S1 and S2 | S2's computation at the base and at HEAD, executed and pasted in the phase record; `tests/text/test_the_agent_contract_holds_the_universal_rules.py` and the cases that read the core and the contract | 308424df6 |
| 7 | *Scope* 7: S9 and S10. `seal fold` at HEAD; D8's replay over the transcripts; the readings and the weighing `docs/running/measuring-a-run.md` asks of a reading that moved toward more cost, in the phase record | the phase record | 44d0f6a09 |

## Operational impact

- `rule_changes.py` accepts a `file:` one group directory deep. A design
  written for 0.29.0 parses unchanged. A design naming a group path is
  refused by a 0.29.0 reader, so a repository's designs and its installed
  plugin move together.
- `seal fold` reads a subdirectory of the policy root once the index names a
  document in it. A user's subdirectory the index names nothing in is read as
  before, which is not at all.
- The boundary changes who edits a repository's policy root. A work item
  whose subject is the root edits it in its pull request, and re-points any
  unsettled design's operation naming what it moved. A user repository reads
  this rule from the installed skill at 0.30.0.
- Every `docs/` path in this repository changes at phase 5. A link from
  outside the repository to a `docs/` file on `main` breaks at the 0.30.0
  release.
- No new dependency, environment variable or migration.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-03 | `.claude-plugin/plugin.json` moves to 0.30.0 in phase 1's first commit (8a68b6c05), not in the changelog commit *Scope* named | this is the first work-item pull request into `release/v0.30.0`, whose tip was the settle #1310, so the branch's version moves with its first commit | `docs/releasing/branch-and-release.md` *The version is named at the cut* |
| 2026-11-03 | `frame/design.md` *Grounding*'s transcript row names the project directory as `~/.claude/projects/<project>/` instead of the owner's real path | the real path failed `tests/test_censuses.py`'s `real_identifiers` census at phase 1 (the crafter's handback, executed); the row's counts are unchanged | `tests/test_censuses.py` *Test_real_identifiers* |
| 2026-11-03 | `trail/phases/phase-7.md` keeps counting each ranged read of the two deleted documents at its base bytes, though not all their text moved unchanged. Phase 1 (4c4925bff) rewrote two passages of `docs/the-review-record.md`: *The guarantee*'s opening (base lines 288-291, 129 bytes shorter) and *The run*'s question-gate paragraph (base lines 531-544, cut to three lines, 778 bytes shorter). Phase 5 and its group commits lengthened that document's moved text by 149 bytes in seven places, four cross-references given a path and three re-pointed paths. Phases 3 and 5 lengthened `docs/the-record-layout.md`'s text by 20 bytes in three re-pointed paths | the round-1 fix pass's word diff found phase 1's two passages (`trail/rounds/round-1.md` finding 3). The round-2 fix pass's word diff of each deleted document at 2d38c75af against the files holding its text at b1880c1db, the replay's HEAD, found the rest. Of phase 7's 33 ranged reads of a deleted file, 28 read the review record and 5 the record layout. Nine of the 28 cover a shortened passage: 4 the guarantee's opening and 5 the question-gate paragraph (`trail/rounds/round-2.md` *Probes*). A range covers each lengthened place once at most, so the base count leaves out at most 149 bytes a read. The proofer's +0 of 375,093 bytes rests on 7 such reads. One of them starts at base line 541 and covers 4 of the question-gate paragraph's 14 lines, 276 of its 956 bytes, so it is overcharged by at most 276 bytes. The proofer's total therefore lies between 276 bytes fewer and 1,043 more (7 reads at 149 bytes each), under 0.3% either way. The sealer found that read's range and this bound (`guarantee.md`, the withheld verdict against b3872b934). The fix pass after that verdict found the same range with a read-only probe over the same transcripts and phase 7's filter (executed). Every other type's total falls by more than the gap can add. The readings and their weighing in that record stand on these figures, so the gap is named here rather than replayed | `docs/running/measuring-a-run.md` |
| 2026-11-03 | The orchestrator corrects `changelog.md`'s "one docstring" to the two docstrings the commits after b1880c1db reword, instead of spawning a crafter for it | the second sealer withheld on that count alone, with the two files named (`guarantee.md`, the verdict against 361aafb82); the fix is one phrase in a record, and `git diff --stat b1880c1db 361aafb82 -- ':!seal/'` lists exactly those two `.py` files beside the READMEs, the cut skills and the record layout (executed). The sealer spawned after 5645d2d62 reads this correction | `skills/core/SKILL.md` *The first value: efficient development through the workflow* |
