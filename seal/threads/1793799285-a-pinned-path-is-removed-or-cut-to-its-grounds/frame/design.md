# Design: 1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "History goes to git, the release notes and the work record." A sentence that tells where a rule or a case came from is history, and it goes. "A mechanism stays only while its record of what it caught outweighs what it costs" decides D2. "A script holds a gate only on a fact it reads exactly" and "whether such a line meant the label is the judgment of the agent that reads the text" also bear on D2 |
| `skills/core/SKILL.md` *The first value: efficient development through the workflow* (read) | A party pays for every byte of a file it opens. A script does not re-encode a judgment of meaning as a grammar rule. Whether a citation holds grounds a reader acts on, or only provenance, is a judgment of meaning (D2) |
| #1355, `release: 0.32.0` (executed: `gh issue view 1355 --json title,body,comments,milestone`, 2026-11-04) | The issue has no comments. Its body gives the measure, *What changes* (the three dispositions D1 applies), *Done when*, *Order* (built last in the release) and *Out of scope* (`seal/`, and `path#name` citations of the present tree). The owner stated on 2026-11-04 that text which costs lines and which no check can catch when it drifts is cleared. That statement is carried in the body, and the spawn prompt relays it |
| The measure at `f93d70ea4` (executed: the issue's command, run 2026-11-04 on `refactor/1355-…` at `aab7ea8bd`, whose tree outside `seal/` is `f93d70ea4`'s) | It prints 25 lines in 17 files. `evals/scripts/noninferiority.py`'s line is gone, because #1254 rewrote that comment at `f93d70ea4`. The same 25 lines are what `tests/censuses.py#COMMIT_PATH` matches over the tree outside `seal/` (executed: `git grep -nP` with that pattern). The filter on `sha256` and `https?://` drops no line that holds a token (executed). So the measure lists the whole class of `<commit>:<path>` tokens in shipped text |
| Reachability of the cited commits (executed: `git for-each-ref --contains <commit> refs/remotes/origin/main 'refs/remotes/origin/release/*'` for each of the 10 distinct commits) | `refs/remotes/origin/main` reaches every one of them. So `tests/text/test_a_cited_commit_outlives_the_squash.py` refuses none, and no line sends its reader to a commit that cannot be opened. The harm of the 25 is what they cost and that they cannot drift visibly. None of them misdirects |
| `feat/1255-the-census-reads-every-entry-point` (executed: the measure via `git grep -nP` on the branch, and `git diff origin/release/v0.32.0...<branch>`) | Its diff changes the text of none of the 25 lines. It moves one line: `tests/test_censuses.py:934` moves further down the file on the branch. Its merge base is `479a79d15`, which still holds `evals/scripts/noninferiority.py`'s cited line. Its own diff touches that file only in the `__main__` block, so the line #1254 removed does not come back with it |
| `feat/1256-a-cited-name-stands-in-its-file` (executed: the measure on the branch and its three-dot diff; read: its `frame/design.md` *Grounding* and *Scope*) | Its diff changes the text of none of the 25 lines. It moves one line: `tests/behaviour/test_a_cited_section_stands_in_its_file.py:445` stands at `:590` on the branch. It edits `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` at line 488 and `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py` at line 634, neither a listed line. Its frame leaves `<commit>:<path>#<name>` unread, adds none to shipped text, and builds its own fixture of that shape when the case runs. It names whether the form may stand in shipped text as #1355's decision |
| `tests/text/test_a_cited_commit_outlives_the_squash.py` (read, whole docstring and `read_here`, `cited`, `unreached`) | It reads every `COMMIT_PATH` token in each tracked file, except under `evals/behaviour/`, a work item's `trail/` and its `guarantee.md`. It refuses a commit that no `main` or release ref contains. "Every token in the cases below is built when the case runs, from a commit the case makes, so this file holds no `<commit>:<path>` of its own" is the precedent for *Scope* item 2 |
| `tests/censuses.py#HISTORY_PATH`, `#COMMIT_PATH`, `#OLD_NAME_RECORDS` (read, lines 990-1175) | `seal/specs` is an old name (`OLD_NAME`, line 997). `old_names` passes it only inside a `HISTORY_PATH` token, and it passes only `seal/threads/` whole. So a rewrite that drops the commit and keeps a `seal/specs/…` path is refused by `old_names`. A rewrite names the issue instead. `seal/follow-up.md:42` holds the one token outside `seal/threads/` (executed: `git grep -nP` over `seal/`), and it still needs `HISTORY_PATH` |
| `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/* and `docs/layout/one-root-by-lifetime.md` *The dependency rule* (read) | "A document that still cites a record of it writes the path a commit holds, as `<commit>:<path>`" states the form a citation of a settled record takes. "A `<commit>:<path>` citation names a commit that `main` or a release branch reaches" states the squash rule. Neither tells a test or a workflow to cite where a rule came from. Both stay true after this work, so `## Rule changes` holds the no-change block |
| `docs/README.md` *docs/layout/* (read) | The layout documents are opened "where they place or write a record". A test docstring or a workflow comment is not a record, so a rule placed there would reach no writer of the 25 lines' kind (plan A7) |
| `seal/threads/1793750411-rule-text-carries-no-history/frame/plan.md` *Alternatives considered* A2 (read) | #1317 rejected a history-marker lint because history has no spelling, and its probe matched about 41 correct sentences of 58. The form here has one spelling, so D2 does not rest on that ground. It rests on what a refusal of the spelling would catch and move |
| `seal/follow-up.md` (read) | No row waits on this work, and its riders table is empty |
| Process changes (executed: `gh release view --json body` for `v0.31.2`; `grep` over `seal/threads/*/changelog.md`) | `v0.31.2`'s notes hold no `### Process changes` table. Ten fragments under `seal/threads/` hold one, and no row in them changes how a citation is written (executed: `grep -iE 'cit|history|commit|provenance|pinned'` over their rows, rows read) |
| Pending rule changes (executed: `grep` of `file: docs/layout/the-record-layout.md` over `seal/threads/*/frame/design.md`) | The one pending operation on that file is work item `1793732301-the-readme-is-written-for-a-first-reader`'s, in *The root records*. No pending operation touches *seal/threads/<work-item-id>/* |
| `routing.md` (read, committed at `aab7ea8bd`) | Planning framer, Implementation crafter, Review through the review chain, Destination open the pull request, Automation yes. Nobody can be asked anything for this run |

**D1. Each line is read for what its reader acts on today, and takes one of four dispositions.**

- **P, provenance.** The sentence tells where a rule, a case or a decision came from, and the rule stands in the text without it. The sentence that holds the token goes, or its citing clause goes and the rest of the sentence stays.
- **G, grounds.** The cited record holds the grounds of a value or a decision a person may change. The grounds stay in one short sentence, or the issue or pull request number that holds them (`#N`) replaces the commit and the path.
- **N, present.** The sentence needs the past file's text to be understood, such as the ids or the table a docstring leans on. The sentence is rewritten to say what it needs in the present, and so is each other sentence of the same docstring paragraph or comment block that leans on the same record.
- **F, fixture.** The token is a case's input. The token is built when the case runs or the module loads, so the file holds no token of its own. The case asserts what it asserted, and the line numbers the case expects stay.

| # | Line at `f93d70ea4` | Disposition | What the rewrite leaves |
|---|---|---|---|
| 1 | `.github/workflows/test.yml:85` | G | Windows count four. The clause naming the arithmetic's record goes, and the arithmetic itself moves into the comment: the fixed cost, the second, slower run, and the minutes three and four shards take, since #841 holds none of it (round-1#1) |
| 2 | `.github/workflows/test.yml:90` | G | macOS count three. The same, with the macOS fixed cost, so "the same arithmetic" points at the Windows sentence above it; #864 holds none either (round-1#1) |
| 3 | `.github/workflows/test.yml:135` | P | The sentence ends at each leg's own `--durations` table, and the record of the run ids goes |
| 4 | `tests/behaviour/test_a_cited_section_stands_in_its_file.py:445`, `:590` once #1256 lands | F | `ELSEWHERE`'s commit-pinned line, built when the module loads, from `AT`. The S7 case's expected lines 9 and 11 stay |
| 5 | `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py:33` | P | The clause from "the real-tree case was seen red" to "names it" goes. A real-tree red is contract rule 15's evidence, which a phase record holds. The sentence on the planted cases stays |
| 6 | `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:37` | P | The clause naming the module this guard was modelled on goes. The two decisions below it stay, introduced as this guard's own |
| 7 | `tests/behaviour/test_chain_hooks_hardening.py:539` | P | The parenthesis goes. The rule it quotes, pin the thing the production path calls and never a copy beside it, stays in the sentence |
| 8 | `tests/behaviour/test_chain_hooks_hardening.py:632` | P | The citation goes, and the rule stays as a sentence of its own |
| 9 | `tests/behaviour/test_chain_hooks_hardening.py:726` | G | One sentence holds the grounds: refusing more words makes a legitimate definition unwritable. `#422` names the guard |
| 10 | `tests/behaviour/test_chain_hooks_hardening.py:842` | G | The grounds already stand in the sentence before it. The clause naming the record goes |
| 11 | `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py:15` | N | The sentence says where each scenario is stated now. Its seen-red clause goes with the sentence: a bare commit cited as evidence is contract rule 15's, which a phase record holds |
| 12 | `tests/behaviour/test_first_setup_asks_once.py:5` | N | The work item's record goes, and no issue is cited, since none holds it (phase record, Q1), and the clauses each case names are readable without the past spec |
| 13 | `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:39` | P | The sentence naming the precedent goes. The comment's first paragraph states the defect |
| 14 | `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:176` | P | The sentence naming the precedent goes. The rule in the sentence before it stays |
| 15 | `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:3` | N | The line says the module holds the acceptance property stated below it. `#667` already stands in the title line |
| 16 | `tests/behaviour/test_the_set_a_work_item_always_has.py:155` | P | The sentence naming the precedent goes. The rule after its colon stays as a sentence of its own |
| 17 | `tests/block_shapes.py:2` | N | The docstring describes the shapes and `RENDERER` in present terms, with `(#667)`. "that table", "the frame's *Renderer* column" and "(the frame's Q2)" in the same docstring are rewritten with it |
| 18 | `tests/config_shapes.py:2` | N | The same, with `(#871)`. "that table" and "keyed by the row's number" are rewritten with it |
| 19 | `tests/hooks/test_mode_gate.py:7` | N | The scenario ids' source goes, and the sentence names no record and no issue, since the phase found no issue page that holds them (phase record, Q1) |
| 20 | `tests/hooks/test_routing.py:73` | N | The shape ids and their texts are named as `tests/block_shapes.py`'s, with no record |
| 21 | `tests/hooks/test_routing.py:76` | G | "red at base" keeps its meaning, a case that fails against the routing reader before #667's change, the path left out because `hooks/routing.py` moved to `hooks/lib/routing.py` and the census refuses a vacated path. The issue or pull request number replaces the commit and the path |
| 22 | `tests/test_censuses.py:934`, below #1255's cases once it lands | F | `test_accepts_the_new_path_a_longer_path_a_file_still_there_and_a_commit`'s commit-pinned line, built when the case runs |
| 23 | `tests/text/test_no_passage_is_pasted_into_a_second_file.py:34` | P | The parenthesis naming row K2's record goes. The grounds stand in the sentence it closes |
| 24 | `tests/text/test_no_passage_is_pasted_into_a_second_file.py:46` | G | The paraphrase half was measured once, by hand, and is not checked. The record's path goes |
| 25 | `tests/text/test_the_rules_claude_md_names_have_one_home.py:39` | P | The sentence on where the carriers started goes |

The text of each rewrite is the phase's (`frame/questions.md` Q1). Where an issue number is named above, it was read from `git log --all` on the cited work item's directory (executed), and the phase confirms with `gh` that the page it cites holds what the sentence sends the reader there for.

**D2. No case is added to keep the form from returning, and `tests/text/test_a_cited_commit_outlives_the_squash.py` stays as it is.** The grounds are in `frame/plan.md` *Alternatives considered*, rows A2 and A3. The test was weighed against `skills/core/SKILL.md` *The rule a mechanism is kept against*:

- The existing case already refuses the one failure that misdirects a reader, a commit no `main` or release ref reaches.
- None of the 25 lines misdirects (*Grounding*, the reachability row). What a new case would refuse is cost and history, and the judgment of whether a line holds grounds a reader acts on is a judgment of meaning, which the proofer reads in the diff.
- A writer refused by a spelling check moves the provenance to a bare commit or to prose, which the check does not read. That moves the text without removing its cost. The tree outside `seal/` holds 51 distinct bare hex tokens that resolve as commits (executed: `git grep -ohP` with a 7-to-40-hex word pattern, then `git cat-file -e <token>^{commit}` for each). The squash case reads none of them, by its docstring's "A bare commit is not read".
- On the day it would land, the case has caught nothing, because this work removes the 25 by hand. The measure in #1355's body finds the class again on demand.

## Scope

In scope:

1. **The 23 comment and docstring lines.** Each line of D1 with disposition P, G or N is rewritten as its row says, and so is each sentence of the same paragraph or block that leans on the same record (D1, N).
2. **The two fixtures.** D1 rows 4 and 22 build their token when the case runs. Each case asserts what it asserted before (*User scenarios & acceptance*, S2).
3. **The record of each rewrite.** The phase record lists each of the 25 lines: its path and its line at the base the phase was built on, its disposition, and the text that replaced it or `removed`. *Done when* asks for this.

Out of scope:

- `seal/`. The records keep what they said when written (#1355 *Out of scope*). `seal/follow-up.md:42`'s token is among them.
- `path#name` citations of the present tree, which #1256 reads (#1355 *Out of scope*).
- Bare commits in shipped text, 51 distinct tokens (D2's count). They are not the issue's `<commit>:<path>` form, and the squash case does not read them. The one bare commit inside a sentence D1 rewrites, row 11's, goes with that sentence. The others, such as `.github/workflows/test.yml:84`'s figure taken at a commit, stand. Whether to clear them is a new issue's to decide, which the orchestrator may file.
- Tag-pinned paths, `<tag>:<path>` (executed: `git grep -nP 'v[0-9]+\.[0-9]+\.[0-9]+:[A-Za-z._/-]+'`): five redraw commands in `assets/seals/README.md`, `evals/scripts/replay_targets.py:24`, and fixtures in `tests/evals/test_replay_targets.py`. A tag is never squashed away, and each is acted on: a command a person runs, or the grammar a labelled record is judged by.
- `tests/censuses.py#HISTORY_PATH` and `#COMMIT_PATH`, the passes the censuses give the form (plan A4).
- The assertion message below `tests/behaviour/test_chain_hooks_hardening.py:726`, which names `frame/design.md` *Out* with no commit. It reads as the frame of whoever reverses the guard, and it is not the issue's form.
- `.claude-plugin/plugin.json`'s version. This work item is not the release's first.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The class is gone | Given the phase's commit, when #1355's measure runs, then it prints no line | the measure, run at the phase's commit, its empty output in the phase record |
| S2. A fixture still carries the form | Given row 22 built when its case runs, when `tests/censuses.py#vacated_paths` stops taking `COMMIT_PATH` out of a line, then `test_accepts_the_new_path_a_longer_path_a_file_still_there_and_a_commit` fails on the commit-pinned line. Given row 4 built when its case runs, then `ELSEWHERE` equals, byte for byte, the literal the base held | row 22: the guard removed in a scratch clone, the case run red and its failing line read (contract rule 15). Row 4: the module imported at the base and at the phase's commit in a scratch clone, and the two values compared. Both recorded in the phase record |
| S3. The squash case holds | Given the phase's commit, when `tests/text/test_a_cited_commit_outlives_the_squash.py` runs, then it passes, and `cited(ROOT)` lists no file outside `seal/` | the module's narrow run, and `cited` called once in the phase |
| S4. No old name is left bare | Given a rewrite that dropped a commit, when the censuses read the touched files, then `old_names` and `vacated_paths` refuse none | each touched module's own `test_census`, and `tests/test_censuses.py`'s run over the files no module declares as its `TARGET`, run narrow |
| S5. The workflow changes only comments | Given `.github/workflows/test.yml` at the phase's commit, when its diff against the base is read, then every added or removed line is a YAML comment | `git diff -U0 <base> -- .github/workflows/test.yml`, each `+` and `-` line read |
| S6. Each rewrite is named | Given the phase record, when it is read, then it lists all 25 lines of D1 with their disposition and replacement | the phase record against D1 |

## Data & interfaces

No interface changes. Two fixtures change their source spelling and keep their value (D1 rows 4 and 22).

## Rule changes

- nothing
  why: The rule this work applies, that history goes to git, the release notes and the work record, stands in `skills/core/SKILL.md`, which every party receives. `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/* states the form a citation of a settled record takes and the squash rule, and both stay true. A second statement of the core rule in a layout document would reach no writer of a test comment (plan A7).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| two clauses naming the shard counts' records, and one naming the run ids' record | `.github/workflows/test.yml`, the `pytest` job's comments on its checkout and on `-n auto` | the arithmetic moves into the comment, and no issue is cited, since #841 and #864 hold no record of it |
| a fixture's literal token | `tests/behaviour/test_a_cited_section_stands_in_its_file.py#ELSEWHERE` | the same text, built when the module loads |
| the clause naming where the real-tree red was seen | `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py`, the module docstring | contract rule 15's evidence is a phase record's; git holds the record |
| the clause naming the module the guard was modelled on | `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, the comment above the class's re-enumeration | git; the two decisions stay as the guard's own |
| two citations of a rule's record, and two of the records of refused alternatives | `tests/behaviour/test_chain_hooks_hardening.py`, the comment on the asking stems, the batch-phrase sweep's docstring, and the two residue comments | the rule and the grounds stay in the text; #422 names the guard |
| a sentence pointing at a past spec's scenario numbering, with its seen-red clause | `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`, the module docstring | each case states its scenario; #664 holds the work |
| the work item's path at a commit | `tests/behaviour/test_first_setup_asks_once.py`, the module docstring | nothing |
| two sentences naming a precedent | `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py`, the comments above the two readers and above `REVIEW_ORCH` | git; the rule each states stays |
| the spec path naming the acceptance property | `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py`, the module docstring | the property is stated below it; #667 |
| the sentence naming a precedent | `tests/behaviour/test_the_set_a_work_item_always_has.py`, the comment above `INSTRUCTING` | git; the rule stays |
| the spec paths the shapes are read against, and the sentences that lean on them | `tests/block_shapes.py` and `tests/config_shapes.py`, the module docstrings | the docstrings in present terms; #667 and #871 |
| the scenario ids' spec path | `tests/hooks/test_mode_gate.py`, the module docstring | nothing |
| the shapes' spec path, and the base named as a commit and a path | `tests/hooks/test_routing.py`, the comment above `declared` | `tests/block_shapes.py`; the issue or pull request before which the base stood |
| a fixture's literal token | `tests/test_censuses.py#Test_vacated_paths.test_accepts_the_new_path_a_longer_path_a_file_still_there_and_a_commit` | the same text, built when the case runs |
| the record paths of row K2 and of the paraphrase measurement | `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, the module docstring | the grounds stay in the sentence; #730 |
| the sentence on where the carriers started | `tests/text/test_the_rules_claude_md_names_have_one_home.py`, the module docstring | git; `CARRIERS` and `LINKED` state what the cases hold |

This work adds no mechanism, so no row names a return.

Framed 2026-11-04 by framer, before the build.
