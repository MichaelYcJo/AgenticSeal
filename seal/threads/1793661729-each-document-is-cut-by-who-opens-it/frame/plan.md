# Implementation Plan: 1793661729-each-document-is-cut-by-who-opens-it

## Technical context

The work stands on these coordinates, each read by the framer at 2d38c75af:

- `skills/core/SKILL.md` *The first value* (lines 25-110) takes the rule;
  the sentence D2 removes stands at lines 85-90.
- `skills/agent-contract/SKILL.md` *20 Do not avoid the change a problem calls
  for* (388 bytes, `awk | wc -c`, executed); its only citation by number is a
  comment in `tests/text/test_the_rules_have_one_owner.py:206` (`git grep`,
  executed).
- `skills/settle/scripts/rule_changes.py#parse` (lines 152-278) holds the
  top-level check at lines 257-260; `#apply_op` (lines 383-468) already
  deletes a document a whole-section `remove` empties and creates one an
  `add` with no section names; `settle.py:1727` already creates a missing
  directory when the draft writes. `#pending` (lines 562-579) skips a design
  `parse` refuses, so this frame's `move` items excuse nothing until phase 2
  lands.
- `skills/settle/scripts/fold_check.py#documents` (line 128) and
  `#index_problems` (line 174) read the policy root's top level only.
- `.github/scripts/rules.py:75` globs `docs/*.md`; `.github/scripts/release_report.py:53`
  globs the same; `#preloads` (line 97) is S2's measure.
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser`
  compares a citation's italic text alone with a pending change's `from` and
  `to`, so a change that keeps the text and changes the path excuses nothing
  today (S9).
- `skills/settle/SKILL.md` (43,170 bytes), `skills/implement/SKILL.md`
  (30,663) and `skills/verify/SKILL.md` (25,263) are the three skills cut
  (`wc -c`, executed); section sizes are in `frame/design.md` *Grounding*.

What breaks in six months with the chosen approach: a later design moves a
section with `move`, and an italic cross-reference without a path inside it
now names a section of another document. Nothing reads such a reference
(`frame/design.md` D7), so a reader follows it into the wrong file until a
review finds it. And a user's repository whose policy root has a
subdirectory its index happens to name a file in will have that
subdirectory's other files measured and held to the index from 0.30.0 on,
which `seal fold` prints rather than refuses.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Group the policy root through a new `move` operation, the settle rewriting the moved paths (chosen) | a reference without a path inside a moved section points into the wrong file (D7); the settle after 0.30.0 is larger than any before it, though most of it is the draft's | chosen: the owner asked for grouping where many documents read by different parties stand side by side, and the policy root is that directory (`frame/design.md` *Which directories are grouped*) |
| Keep `docs/` flat and cut `docs/the-review-record.md` into five top-level documents | 22 top-level documents in one list, each reader finding its own through the index alone; the owner's item 4 unmet | rejected: the cost it saves is D4's readers, which are paid once, while the flat list is paid by every reader of the root |
| Move the documents in this pull request, with no rule changes, since a move changes no rule's wording | `skills/implement/SKILL.md` *Document layout* says a pull request does not edit the policy root; a pull request that does is a policy break the sealer reads, and the next item would cite the exception | rejected; the premise that keeps the rule, that the settle after this release lands before the next release's first item, is checked: the settle 0.27.3 to 0.29.0 landed on `release/v0.30.0` (95cbd99a4) before this item's routing commit 2d38c75af (`git log`, executed by the orchestrator). The policy-root benefit waits one release, while the skills benefit, where the transcripts show most of the reading, ships with 0.30.0 |
| Move documents through today's operations: a `remove` of the old document and an `add` whose `to` holds its text | this design would hold about 260 KB of the policy root verbatim; every one of the 708 lines naming a moved path is rewritten by hand at the settle, and only the cited-section case finds the ones missed, and only those written as a path with a section | rejected |
| The settling session rewrites the moved paths by hand, guided by the cited-section case, with no rewrite in the draft | the case reads `` `path` *section* `` citations only; a bare path in a hook's output, a test's constant or `.test_durations` is found by whichever check happens to read it, or by nobody | rejected: the old and the new path are exact strings, so a script answers this (`skills/core/SKILL.md` *Judgment is spent where meaning is the question*) |
| Group `skills/` into categories, or `agents/` into subfolders | a category-level skill is not documented as found and may stop loading; a subfolder renames every agent (orchestrator's finding of the Claude Code docs) | rejected for both directories |
| Put the cut rule in a policy document and leave the core as it is | every party writes documents and skills; a rule only the orchestrator's documents state is not in front of an agent that writes a skill or a frame | rejected: the issue puts it in the core, and D2 pays its bytes |
| Pay D1's bytes by trimming each agent definition | five edits for one fact, and the tracer's 2,956-byte definition has little an agent does not act on | rejected: the offset is taken in the core and the contract, which every agent shares (D2) |
| Cut `skills/implement/SKILL.md` into one file per agent | the crafter reads most of it at every spawn anyway; the parts it never reads are the orchestrator's, which already has `orchestration.md` | rejected in favour of moving the orchestrator's parts there (D5) |
| Cut the `orchestration.md` files by step | one reader holds them in one session; a cut turns one read into several in the same context | rejected; out of scope (`frame/design.md` *Scope*) |
| Measure with a paid behaviour-suite run on both trees | `evals/README.md` *The behaviour suite* makes no later edit owe a run, and #1254 is narrowing that suite; a paid run here measures recall and not what a spawn reads | rejected: D8's replay reads the reading itself, at no cost |
| Wait for the live run under the installed 0.30.0 and report only that | this pull request carries no reading, and the docs part is not live until a release later | rejected as the only reading; kept as Q1, the live confirmation |
| Give each moved document a line naming its reader at its top | fifteen sentences restating the reader the group's index table states once | rejected: the group states it once; a new document states it, since it is written here (D3) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* 5: the copies on the code side (D6): `hooks/question-gate.py`'s docstring gains the one fact only the document held; `agents/sealer.md`, `skills/code-review/orchestration.md`, `skills/verify/scripts/seal_stamp.py`, `hooks/sealer-stamp.py` and `skills/code-review/scripts/chain_check.py` keep a link in place of each run the ten-word census lists | the census re-run, its command and list in the phase record; the modules that read the changed files (`tests/hooks/test_question_gate.py` and any case pinning the removed text), run narrow | |
| 2 | *Scope* 3 and 6's excuser: D4 whole, with S5, S6, S7, S8 and S9; the grammar's text, `move` included, written in `skills/settle/SKILL.md` *Rule changes* where it stands today; `templates/setup/config.md` *The fold's values* and `skills/config/SKILL.md` | new cases for S5 to S9, each seen red first; the settle's, fold's, rules' and release report's test modules and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, run narrow; the reader list's two `git grep` commands pasted in the phase record | |
| 3 | *Scope* 2 for `settle` (D5's first row) and *Scope* 6 for its citations: the four supporting files, the ceiling sentence rewritten to the reader rule, and every citation outside the policy root re-pointed; S3 | `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, with the three policy-root citations excused by this frame's rule changes; the settle's test modules | |
| 4 | *Scope* 2 for `implement` and `verify` (D5's other rows) and *Scope* 6 for their citations, the core's citation of *1.* among them; the axis sentence in *Document layout*; S4 | the cited-section case; the modules that read the two skills; bytes of `skills/implement/SKILL.md` before and after in the phase record | |
| 5 | *Scope* 1: D1 and D2; S1 and S2 | S2's computation at the base and at HEAD, executed and pasted in the phase record; `tests/text/test_the_agent_contract_holds_the_universal_rules.py` and the cases that read the core and the contract | |
| 6 | *Scope* 4 and 7: S10 and S11. A scratch clone of HEAD with this design's operations placed by phase 2's placement code, `seal fold` and the cited-section case run there; the D8 replay over the transcripts. Nothing of the scratch clone is committed; the phase record holds the commands and the readings, and the weighing `docs/measuring-a-run.md` asks of a reading that moved toward more cost | the phase record; a failure in the scratch clone is a defect of phase 2 or of this frame's rule changes, routed as the run decides | |

## Operational impact

- `rule_changes.py` accepts a `file:` one group directory deep and a new
  operation, `move`. A design written for 0.29.0 parses unchanged; a design
  written with a group path or a `move` is refused by a 0.29.0 reader, so a
  repository's designs and its installed plugin move together.
- `seal fold` reads a subdirectory of the policy root once the index names a
  document in it. A user's subdirectory the index names nothing in is read
  as before, which is not at all.
- The settle after 0.30.0 in this repository places 45 operations, 23 of
  them moves, and the draft rewrites the paths those moves change across the
  tracked files outside `seal/`; the settling session reads the moved
  sections for path-less cross-references (D7) and writes the blank lines
  the values cannot hold (D3).
- No new dependency, environment variable or migration.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
