# Phase 1: 1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds

## What this phase found

**The frame holds for this phase, with one line moved.** The phase was built on `6e23af058`, the merge of `release/v0.32.0` after #1255 and #1256 landed. #1355's measure, run there, prints 25 lines in 17 files (executed). They are the 25 lines of `frame/design.md` D1, at the lines D1 names, except row 22: its line stands at `tests/test_censuses.py:1059`, where D1 and `frame/plan.md` *Technical context* expect `:1057`. The text of the line is the one D1 names. The measure printed no line D1 does not list, and `evals/scripts/noninferiority.py` printed none.

**Each of the 25 lines, at `6e23af058`** (read: each rewrite at its line after the edit). "removed" means the clause or sentence holding the token went and the text around it stands as it was.

| # | Line | Disposition | What replaced it |
|---|---|---|---|
| 1 | `.github/workflows/test.yml:85` | G | the arithmetic the record held, in the comment: a shard's job is a fixed cost, about 62 s on Windows, plus the leg's case time over the count, and four is the smallest count under 12 minutes on both run 37458654434 and run 37457228586, 1.08 times slower, where three gives 11.9 and 12.8 minutes and four 9.2 and 9.8 (round 1, finding 1) |
| 2 | `.github/workflows/test.yml:90` | G | the record's clause removed, and the sentence gains the macOS fixed cost, "about 45 s", beside its factor of 1.45 (round 1, finding 1) |
| 3 | `.github/workflows/test.yml:135` | P | removed: the sentence ends "each leg's own `--durations` table below." |
| 4 | `tests/behaviour/test_a_cited_section_stands_in_its_file.py:590` | F | `AT = "f6ae6db6"` above `ELSEWHERE`, which is now an f-string whose line reads `` `{AT}:manual/b.md` *Gone* ``, with a two-line comment saying why |
| 5 | `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py:33` | P | removed: the paragraph is "Red-first, per contract rule 15: the planted cases build a temp tree with the defect in it." |
| 6 | `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:37` | P | "This is what stops that, and two decisions shape it:" |
| 7 | `tests/behaviour/test_chain_hooks_hardening.py:539` | P | "the pattern IS the behaviour this repair changes, and a case pins the thing the production path calls, never a copy beside it." |
| 8 | `tests/behaviour/test_chain_hooks_hardening.py:632` | P | "Pin the function the production path calls, never the helper beside it." |
| 9 | `tests/behaviour/test_chain_hooks_hardening.py:726` | G | "Widening the stem set is refused, because refusing more words makes a legitimate definition unwritable (#422), so this is residue and not a defect." |
| 10 | `tests/behaviour/test_chain_hooks_hardening.py:842` | G | removed: the bullet ends "and it is ruled out." |
| 11 | `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py:15` | N | "Each scenario is stated at the case or the census that holds it, under the number #664's work gave it." The seen-red clause and its bare commit went with the sentence |
| 12 | `tests/behaviour/test_first_setup_asks_once.py:5` | N | "Each case states the clause it holds and names it by its number, and a number another work item gave carries that item's issue, as `S2 of #952` does." |
| 13 | `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:39` | P | removed: the comment ends at "with nothing in the tree comparing them." |
| 14 | `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:176` | P | removed: the sentence ends "is not the fact stated." |
| 15 | `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:3` | N | "This module holds the acceptance property below." Item 3 reads "on every shape `tests/block_shapes.py` holds", the next paragraph "over those shapes", and the last paragraph "it had to give `RENDERER` on every shape, which was derived by reading the specification and could not be executed." |
| 16 | `tests/behaviour/test_the_set_a_work_item_always_has.py:155` | P | removed: the comment reads "Everything a session installing this plugin reads to learn the layout. A path may not appear in an instructing document at all, …" |
| 17 | `tests/block_shapes.py:2` | N | "The shapes the readers of fences and HTML comments are held to, as lines (#667)." The next paragraph says `SHAPES` holds each shape as a document's lines keyed by its id, `RENDERER` the lines a CommonMark renderer hides for each id, and that the renderer case holds the oracle to `RENDERER` |
| 18 | `tests/config_shapes.py:2` | N | "The sixteen config shapes, as texts (#871)." The next paragraph says `SHAPES` holds each shape as a config document keyed by its number. The last paragraph says "against a measurement of what cmark-gfm renders" |
| 19 | `tests/hooks/test_mode_gate.py:7` | N | "Each case states the scenario it holds and names it by its id, and an id another work item gave carries that item's issue, as `S7 of #952` does." |
| 20 | `tests/hooks/test_routing.py:73` | N | "The shape ids and their texts are `tests/block_shapes.py`'s." |
| 21 | `tests/hooks/test_routing.py:76` | G | the comment's second sentence: `"red at base" means the case fails against the routing reader as it stood before #667 changed it; "pins" means it passes there too.` |
| 22 | `tests/test_censuses.py:1059` | F | `commit = "5f11923f"` at the top of the case, and the fixture line is `` f"measured in `{commit}:hooks/moved.py`\n" `` |
| 23 | `tests/text/test_no_passage_is_pasted_into_a_second_file.py:34` | P | removed: the sentence ends "and remove nothing said twice." |
| 24 | `tests/text/test_no_passage_is_pasted_into_a_second_file.py:46` | G | "The paraphrase half was measured once, by hand, and is not checked." |
| 25 | `tests/text/test_the_rules_claude_md_names_have_one_home.py:39` | P | removed: the paragraph goes from "`CLAUDE.md` first." to "Each file in `LINKED` …" |

**`frame/questions.md` Q1, answered by the work.** For each G and N line, the phase read the page D1 names with `gh issue view` or `gh pr view` (executed), and kept the number only where the page holds what the sentence sends its reader there for, as Q1's default says.

- Rows 1 and 2, option (c). Neither #841 nor #864 holds the shard-count arithmetic. #841's body proposes the split and holds no count. PR #845, which closed it, holds the four shards and their measured times. #864's body says it will use "the same arithmetic #841 recorded". So the arithmetic goes into the sentences, with the fixed cost and the second, slower run that decide the Windows count (round 1, finding 1), and the comment's first line names both issues: "macOS in three shards (#864) and Windows in four (#841)". A third citation of each would send the reader to a page that does not hold the arithmetic.
- Row 9, option (a), `#422`. Its body says "Refusing more words makes legitimate definitions unwritable", which is the grounds the sentence now states.
- Row 10, option (c). The grounds stand in the sentence before the citation.
- Row 11, option (a), `#664`, which the title line already names. The case numbers S17 and S19 are #664's work's, and each scenario is stated at its case or, for S19, at the comment naming the census.
- Row 12, option (c). #95's page is a stub that says the pull request could not move with the repository, and it holds no clause. The rewrite names no issue for the clauses and says how a case names one: the cases already state each clause, and the clauses another work item numbered carry its issue (`S2 of #952`, `#1055 S6`).
- Rows 15 and 17, option (a), `#667`, already on each title line. Its page holds the three readers and the constraint, and the docstrings now state the acceptance property and the shapes in the module without leaning on the past spec.
- Row 18, option (a), `#871`, already on the title line.
- Row 19, option (c). #151's body holds no scenario ids, and PR #245's number is a stub page. The rewrite has the same shape as row 12's, with `S7 of #952`, which the module's own case docstring holds.
- Row 20, option (c). The ids and texts are `tests/block_shapes.py`'s, which needs no number.
- Row 21, option (a), `#667`. The routing reader at `3911a8cf` is the one `v0.15.6` holds (executed: `git diff --quiet` on the file between the two), and `v0.16.0` holds it changed, so "before #667 changed it" names the same base.
- Row 24, option (c). #730's body and its one comment do not hold the paraphrase measurement, and #730 already stands in the title line.

**Departures from the frame**, each judged against the document named.

- **Row 21 does not name `hooks/routing.py`.** D1 gives "a case that fails against `hooks/routing.py` before #667's change". The first scoped run refused it (executed): `tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census` named `tests/hooks/test_routing.py:73`, because `vacated_paths` reads `hooks/routing.py` as a path no file holds since it moved to `hooks/lib/routing.py`. Before the rewrite the commit-pinned token kept that path out of the census's reading. The rewrite names the reader and not its path, so `frame/design.md` S4 holds without an exemption. Writing `hooks/lib/routing.py` would name a path the base did not hold.
- **Rows 15 and 18 reach past the paragraph.** D1's N disposition rewrites each sentence of the same docstring paragraph or comment block that leans on the same record. Rows 15 and 18 left sentences in later paragraphs of the same docstring that name "the frame" and "(its Q2)" with no antecedent, once the citation went. Row 17's own row extends its rewrite to the whole docstring, and rows 15 and 18 follow it. Grounds: `skills/core/SKILL.md` *The first value*, a party pays for every byte it opens, and a sentence whose referent is gone costs its reader a search. Comment blocks and case docstrings outside the rewritten docstrings keep "the frame" (`gaps.md` *Not done*).
- **Rows 1, 2, 12, 19, 20 and 24 cite no number** where D1 named one or left the choice open (Q1 above).

**Seen red and the fixtures' values** (`frame/design.md` S2).

- Row 22: red with only `vacated_paths`' `COMMIT_PATH` cut removed (executed: `bin/seal mutate tests/censuses.py --replace 'spelling.search(COMMIT_PATH.sub("", line))' 'spelling.search(line)'` over `-k test_accepts_the_new_path_a_longer_path_a_file_still_there_and_a_commit`, at `762225c29`, verdict `red`, exit 0, tree clean after the restore). The failing line is the case's `assert censuses.vacated_paths("docs/x.md", root) == []`, and it names `docs/x.md:4`, the commit-pinned line, as `hooks/moved.py` vacated.
- Row 4: `ELSEWHERE` at `6e23af058` and at `762225c29` is the same 195-character string (executed: each file's `AT` and `ELSEWHERE` assignments compiled alone and run, with the two values compared). Line 7 of the value is `` `f6ae6db6:manual/b.md` *Gone* ``, so the S7 case's expected lines 9 and 11 stand, and it passes.
- No unit adds behaviour: the work changes comments, docstrings and two fixtures' spelling, so no `seal mutate` run is owed (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the docstring row). The run above is contract rule 15's evidence for S2.

**The scenarios at `762225c29`** (executed unless marked).

- S1: #1355's measure prints no line, exit 1 from the last `grep`. A `git grep -nP` with `tests/censuses.py#COMMIT_PATH`'s pattern outside `seal/` prints none either.
- S2: above.
- S3: `cited(ROOT)` from `tests/text/test_a_cited_commit_outlives_the_squash.py` reads 21 tokens, all under `seal/`. The module passes in the scoped run.
- S4: `tests/test_censuses.py` passes in the scoped run, and so do the touched modules, each of which runs the censuses on itself where it declares a `TARGET`.
- S5: `git diff -U0` on `.github/workflows/test.yml` adds and removes only lines that open with `#` after their indent (read: each of the 11 lines).
- S6: the table above (read against D1).

**The scoped run.** `bin/test` over the 12 touched test modules, `tests/text/`, and the 22 other test modules that name a changed path or import `tests/block_shapes.py` or `tests/config_shapes.py`, found by `git grep -l` on each changed file's name: 3084 passed, 4 skipped, exit 0 (executed, with this record, `gaps.md` and `changelog.md` staged, so `git ls-files` listed them). Before `gaps.md` was written, `test_every_spec_directory_that_reached_the_ladder_has_an_overview` was red on this work item's directory, as that case expects of a phase not yet closed.

**Five docstrings were rewrapped after the read of the range.** Reading the diff whole showed five docstring paragraphs whose rewritten lines ran past the width around them, in `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py`, `tests/hooks/test_mode_gate.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/block_shapes.py` and `tests/config_shapes.py`. The commit that rewraps them changes no word (executed: `git diff --word-diff=porcelain` printed no added or removed word). The scoped run over the same modules, on the rewrapped tree with this record as it now reads: 3084 passed, 4 skipped, exit 0 (executed).
