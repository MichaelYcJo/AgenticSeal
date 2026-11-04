# Design: 1793795356-a-cited-name-stands-in-its-file

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work item's subject is the code: one test module and five citations in code text. It states the rule it changes in `## Rule changes` for the settle and edits no document of the policy root. The issue asks for the same ("through this issue's work item's `## Rule changes`") |
| `docs/layout/one-root-by-lifetime.md` *The dependency rule* (read at HEAD `31554e36a`) | The issue names `docs/one-root-by-lifetime.md`. The file stands at `docs/layout/one-root-by-lifetime.md` since `ea220c9cd` (#1314) (executed: `git log -- docs/layout/one-root-by-lifetime.ko.md`), and `docs/README.md` names it on the `docs/layout/` row with its Korean edition. The section's second rule, "nothing may need to be found and updated when something else moves", is the rule a `path#name` breaks when its name moves. The section carries no `check:` line at HEAD (read), and neither does its Korean edition's *종속 규칙* (read, lines 31 to 54) |
| `skills/settle/rule-changes.md` *Rule changes* and *A rule has one shape* (read) | A check line alone is an `add` whose `to` is the line; it lands at the end of the section's own text, after the paragraph of the wider rule. Precedent: the frame committed at `98d05a656` writes `to: check: tests/hooks/test_dispatch.py` (executed: `git show 98d05a656`). Each `file:` is picked from `docs/README.md` |
| `CONTRIBUTING.md` *House rules*, "Both READMEs move together, and so does every document with a `.ko.md` edition" (read) | The Korean edition takes the same check line, which stays English in every edition. Precedent: #1270's design (in `1854b5e9f`) wrote one operation per edition of *The dependency rule* (executed: `git show 1854b5e9f`) |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | Whether a name is defined in a `.py` file is read with `ast`, a real parser, and never by a pattern over the source. A cited file the parser cannot read is named as not read and decides nothing. No list of exempt citations is kept. "History goes to git, the release notes and the work record": a sentence about a name the past held is rewritten to say what its reader needs now, or its provenance clause goes (the #1355 row below) |
| #1355, `release: 0.32.0` (read: `gh issue view 1355`, 2026-11-04) | #1355 removes the 26 `<commit>:<path>` citations of shipped tests, workflows and evals, or keeps the grounds such a citation holds in one sentence or an issue number. Its body says the owner stated on 2026-11-04 that text that costs lines and that no check can catch when it drifts is to be cleared, and that this frame is proposed not to add a `<commit>:<path>#<name>` shape to shipped text. The orchestrator's reading of this frame at `1081c4265` proposed the same (P1), and this frame takes it. That decision postdates #1256's body and overrides its sentence "A sentence about a name the past held … cites it at its commit". Whether a `<commit>:<path>` may stand in shipped text at all is #1355's to decide, so this work adds no handling of the form beyond leaving it unread (P2). #1355's list holds one line each of three files this work also edits: `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py` and `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` |
| The module docstring of `tests/behaviour/test_a_cited_section_stands_in_its_file.py` (read, all 783 lines) | The name reader reuses what the section reader decided: one corpus, `corpus(root)`, which leaves out `tests/censuses.py#RECORDS` (`seal/threads/` and `evals/behaviour/`, executed: `grep -n RECORDS tests/censuses.py`) because a record keeps what it said when it was written; each file read through `flowing`; a cited path whose first segment is no tracked top-level entry not read (S7); a cited path under a tracked entry that names no tracked file dangling (S7); a pending rule change in the policy root excusing a citation it corrects (S9); fixtures citing under `manual/`, a top-level entry the repository lacks |
| `tests/text/test_a_cited_commit_outlives_the_squash.py` (read) and `tests/censuses.py#COMMIT_PATH` (read) | `COMMIT_PATH` is `[0-9a-f]{7,40}:[\w./-]+`, and that case reads every such token outside a work item's `trail/`, its `guarantee.md` and `evals/behaviour/`. The fixture of *Scope* item 3 that shows a `<commit>:<path>#<name>` unread builds its token when the case runs, from a commit the case makes, as that case's own fixtures do, so this module gains no such literal |
| Where each past name went (executed: `git log -S`, `git log --diff-filter=D` and the parent of each commit) | `skills/verify/scripts/broad_gate.py#PANEL_VALUE_WIDTH` stood there until #832 (`149ca9ecc`) widened the gate's value to 41; `tests/behaviour/test_unverified_rows_close.py#test_the_fence_rule_agrees_with_the_config_reader` was removed by `6046f0622` (#1005); `hooks/mode-gate.py#unreadable` by `56ade5c8c` (#867); `skills/code-review/scripts/round_record.py` was deleted by `8350c5788` (#959). Each sentence's issue number is what it may keep where its grounds are needed |
| `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-3.md` at `569780eff`, *The decisions* rows C6 and C10, *Command C10*, *Instances C10* (read with `git show`) | C10 is `build`: 113 `path#name` names at `813665f0`, 2 defined nowhere in their file; the comment at `skills/verify/scripts/unverified_check.py:115` named a function removed before the comment was written and stood in 25 release tags, `v0.16.0` to `v0.27.1`, with nothing naming it. That is the catch the new case is kept against. The measure read the shipped text outside `tests/` and `evals/behaviour/`, skipped a path that names no tracked file, and found definitions by a regular expression |
| `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` at `48d035aa6`, *The table* row K13 and *Instances K13* (read with `git show`) | A name after a path with no directory, and a name cited from `tests/`, were that measure's open part. The new case reads `tests/` (the corpus does), and leaves the bare file name unread, as the issue's *Out of scope* says |
| The tree's `path#name` tokens at HEAD `31554e36a` (executed, below) | 280 tokens whose path's first segment is a tracked top-level entry, read in the corpus. Five do not resolve to a name their file defines at module scope or as a `def` or `class` at any depth, and one more is cited at a commit. Each is listed under *Data & interfaces* with its repair |
| `skills/verify/scripts/unverified_check.py` and #1235 (executed: `git grep -n overwide_rows` prints nothing) | The dangling comment the issue puts out of scope is gone at HEAD, so the tree case does not wait on #1235 |
| Contract rule 15 (read) | A case that asserts a citation is not read is shown red with only its named guard removed, and its failing line is read for that guard. *Scope* item 3 names the guard of each case |
| #1256's comments (executed: `gh issue view 1256 --json comments` returns none, 2026-11-04) | Nothing beside the body changes the request |
| `seal/follow-up.md` (read) and `seal/parity.md` (executed: absent) | No follow-up row is about a cited name, so none joins this scope. No migration config stands |

The probe behind the HEAD row, executed 2026-11-04 by the framer as `python3 -I <scratch>/probe.py <worktree>` from a scratch directory, since deleted. It listed `git ls-files`, left out the `RECORDS` prefixes and files that do not decode as UTF-8, matched `(?<![\w./:-])((?:[\w.-]+/)*[\w.-]+\.py)#(\w+)` on each line, kept a token whose path's first segment is a tracked top-level entry, and parsed the cited file with `ast.parse`. It printed `read 280`, 246 tokens with no tracked top-level first segment, two cited paths that name no tracked file, three names not bound in the file, five names bound only by a `def` inside a class or a function, and one token at a commit.

The design's `## Rule changes` was parsed by `skills/settle/scripts/rule_changes.py#parse` and each item applied by `#apply_op`, from a `git clone --no-local` of this worktree in the same scratch directory (executed 2026-11-04 by the framer): two `add` items, no error and nothing unread, and each check line lands after the section's last paragraph, before the next heading.

## Scope

In:

1. **The name reader.** `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads a third shape beside the cited section and the contract rule: a `path#name`, read in `corpus(root)` through `flowing`, wherever it stands on a line, in backticks or not.
   - A token is read where its path ends in `.py` and its path's first segment is a tracked top-level entry. A token preceded by a word character, `.`, `/`, `:` or `-` is not read, so a `<commit>:<path>#<name>` and a path inside a longer path or a URL are not read. The reader does nothing more with a `<commit>:<path>#<name>`: it opens no commit and runs no `git show`.
   - The name resolves where the cited file, parsed with `ast`, binds it: a `def`, `async def` or `class` at any depth, or a name bound at module scope (an assignment, an annotated or augmented assignment, or an import, including those inside a module-level `if`, `try` or `with`). A name bound only inside a function body, such as a local variable or a parameter, does not resolve.
   - A path that names no tracked file has no names, so its citation is dangling, as S7 has it for a section.
   - A cited file that is tracked and that `ast` cannot parse, or that does not decode as UTF-8, is named in one warning as not read, and its citations are neither dangling nor resolved.
   - A dangling citation in a file of the policy root that a pending rule change corrects is excused and warned, as S9 has it, with the `path#name` token standing where the section reader matches `*<cited text>*`.
2. **The tree case.** Every `path#name` the tree's corpus cites resolves, or is excused. A floor on the count read keeps a reader that stops matching from passing on nothing; at HEAD 280 are read (executed, the probe), and the section case's floor of 100 is the default.
3. **The fixture cases**, each seen red with only the guard it names removed (contract rule 15):
   - a name resolves while its file defines it as a function, a class, a module constant, an import and a method, and is named with its file and line once the definition is renamed; guard: the resolution against the parsed names;
   - a name bound only as a local variable does not resolve; guard: the restriction to module scope;
   - a path under a tracked entry that names no tracked file is dangling; guard: the tracked-file test;
   - a `<commit>:<path>#<name>`, its token built when the case runs (*Grounding*, the `COMMIT_PATH` row), a path whose first segment no tracked entry has, and a path inside a longer path are not read; guards: the `:` and `/` in the look-behind, and the top-level test;
   - a `path#name` in a file under a `RECORDS` prefix is not read, by extending S8's fixture; guard: the corpus's `RECORDS` filter;
   - a pending correction excuses a policy citation of a name and warns, by one entry in S9's excusing table and one in its refusing table; guard: the excuser call;
   - a cited file that does not parse is named as not read and decides nothing; guard: the parse failure's branch.
4. **The tree's five instances**, each rewritten in place. A sentence about a name the past held is rewritten to say what its reader needs now, or its provenance clause goes, and none is re-pointed at a commit. Where the clause carries the grounds of a value a person may change, the grounds stay in one sentence or as the issue that holds them (`#N`), with no path to the gone name:
   - `.github/scripts/release_seal.py:126` to `:129`, "It was `skills/verify/scripts/broad_gate.py#PANEL_VALUE_WIDTH` until #832 widened the gate's to 41 …": the grounds of `PANEL_VALUE_WIDTH = 23`, a value a person may change, so they stay, as the gate's 41 and the release's 23 kept apart since #832;
   - `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:636` to `:638`, "`tests/behaviour/test_unverified_rows_close.py#test_the_fence_rule_` / `agrees_with_the_config_reader` held that reader to exactly this", a provenance clause about a test `6046f0622` removed, wrapped across a docstring line: it goes, or the docstring says what the helper reproduces now;
   - `tests/hooks/test_config.py:1112` to `:1113`, "so no caller opens the file again to find out -- `hooks/mode-gate.py#unreadable` did, and is gone": the clause after the dash goes;
   - `tests/skills/test_settle.py:3236` to `:3238`, "`skills/code-review/scripts/round_record.py#load` had that shape until #590; this copy arrived repaired": the history goes, and the docstring keeps what the case holds now;
   - `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:491`, the planted key `tests/test_tmp_seventh.py#sweep`, builds the key when the case runs, so the module holds no literal of it.
5. **The module docstring** says the module reads three shapes, and what the name reader reads and leaves unread, rewritten in place (contract rule 19). "This module reads two shapes of citation, the two that `skills/writing-style/SKILL.md` states" stops being true and goes in the same commit.
6. **The rule change** under `## Rule changes`: *The dependency rule* and *종속 규칙* each gain the check line naming the module.

Out:

- The dangling comment in `skills/verify/scripts/unverified_check.py`, which #1235 repairs; gone at HEAD (*Grounding*).
- The bare-name and blockquote shapes the C6 row names, which have no failure in the record. For names, the bare shape is a file name with no directory, such as `settle.py#VERSION_RE`: no tracked file is named by it alone, and 246 tokens at HEAD are of that kind or stand under a path no tracked top-level entry has (executed, the probe).
- `path:line` coordinates, the other half of K13, which the issue does not ask for.
- Every `<commit>:<path>` citation in shipped text, and whether the form may stand there at all, which #1355 decides and repairs: among them this module's S7 fixture line and `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:37`. This work adds none.
- The records under `seal/threads/` and `evals/behaviour/`: the corpus leaves them out for the reason the module docstring gives, and the name reader reads the same corpus.
- `skills/writing-style/SKILL.md`'s citation sentence, which states the section and contract rule shapes and not the name shape. The issue asks for the case and the check line, and no failure in the record asks for a rule of how to write a name citation.
- `tests/censuses.py`, `CONTRIBUTING.md`, `evals/README.md`, `evals/scripts/noninferiority.py`, `tests/evals/test_noninferiority.py` and `.claude-plugin/plugin.json`, which #1254 and #1255 edit; this work imports `RECORDS` from `tests/censuses.py` and changes nothing there.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A function cited by name is removed | Given a comment citing `hooks/x.py#helper`, when a commit removes `helper` from `hooks/x.py`, then the tree case fails naming the citing file, its line and the token | the fixture case of *Scope* item 3's first bullet; the tree case, red at HEAD before item 4's repairs |
| A sentence about a name the past held | Given a comment that a constant "was" a name until an issue, when the case runs, then the citation is named dangling, and the writer rewrites the sentence to say what its reader needs now, keeping the issue number where the grounds of a value hang on it | the tree case, red at HEAD on the four sentences of item 4 and green after their rewrite |
| A token cited at a commit | Given `<commit>:<path>#<name>` in a file of the corpus, when the case runs, then it is not read and nothing opens the commit | the fixture case of item 3's fourth bullet |
| A cited method or nested function | Given `tests/x.py#test_case` where `test_case` is a method of a class, when the case runs, then the citation resolves | the fixture case of item 3's first bullet; the tree's four method citations in `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` and the nested function `skills/verify/scripts/unverified_check.py:491` cites |
| A policy document cites a name a work item removes | Given a `docs/` file citing `hooks/x.py#gone` and an unsettled design whose `## Rule changes` `change` corrects that sentence, when the case runs, then the citation is excused and warned once | S9's tables, extended |
| The settle writes the check line | Given this design's two `add` items, when the settle after the release applies them, then *The dependency rule* and *종속 규칙* each end with `check: tests/behaviour/test_a_cited_section_stands_in_its_file.py` | `chain_check.py` reads the line inside the `to` at the pull request; `seal rules --check` after the settle |
| The tree holds | Given the tree after item 4, when the module runs, then every case passes and the name floor holds | the module's narrow run by the crafter; the broad gate by the orchestrator |

## Data & interfaces

New in `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, names the crafter's to choose:

- a pattern for the token, the probe's `(?<![\w./:-])((?:[\w.-]+/)*[\w.-]+\.py)#(\w+)` as the starting point;
- a function from a file's text to the set of names it binds as *Scope* item 1 states, or `None` where it does not parse;
- a function over `corpus(root)` returning the module's `Found(read, dangling, excused)`, its `dangling` and `excused` entries shaped as the section reader's are, the cited text being the `path#name` token;
- `excuser` takes the cited text as written, so the section reader passes `*<said>*` and the name reader passes the token; `rules.removed_by` is called as before.

The six tokens the probe found that do not resolve at HEAD (executed), with what *Scope* item 4 does to each:

| Citing line | Token | Why it does not resolve | Repair |
|---|---|---|---|
| `.github/scripts/release_seal.py:126` | `skills/verify/scripts/broad_gate.py#PANEL_VALUE_WIDTH` | the constant left `broad_gate.py`; the sentence is about the past | keep the grounds of 23 in one sentence with #832, no path |
| `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:637` | `tests/behaviour/test_unverified_rows_close.py#test_the_fence_rule_` | the name wraps at a line break; the whole name was removed by `6046f0622` | the provenance clause goes, or says what the helper reproduces now |
| `tests/hooks/test_config.py:1113` | `hooks/mode-gate.py#unreadable` | removed by `56ade5c8c` (#867); the sentence says so | the clause goes |
| `tests/skills/test_settle.py:3236` | `skills/code-review/scripts/round_record.py#load` | the file was deleted by `8350c5788` (#959) | the history goes; the docstring says what the case holds |
| `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:491` | `tests/test_tmp_seventh.py#sweep` | a planted key naming no file, by design | build the key when the case runs |
| `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:37` | `f975ea66a:tests/test_a_corrected_sentence_survives_elsewhere.py#_derives_a_path_list` | cited at a commit | none here; not read, and #1355 lists the line |

## Rule changes

- add
  file: docs/layout/one-root-by-lifetime.md
  section: The dependency rule
  to: check: tests/behaviour/test_a_cited_section_stands_in_its_file.py
- add
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 종속 규칙
  to: check: tests/behaviour/test_a_cited_section_stands_in_its_file.py

## Removes

- nothing
  why: The work adds a check, a third shape in an existing case module, and takes nothing out. No other mechanism reads a `path#name` citation: a `git grep` for a `.py#` reader over `tests/` and the `.py` files found none outside `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, which splits the keys of its own table and reads no other file's citations (executed), so the case duplicates nothing that could go. Its catch record is C10's: `skills/verify/scripts/unverified_check.py:115` cited a function removed before the comment was written, through 25 release tags, `v0.16.0` to `v0.27.1`, and nothing in the tree named it (the C10 row of the measure, read at `569780eff`). Its cost is a reader of about the section reader's size over the corpus the module already reads. *Scope* item 4 removes the provenance clauses of three past sentences and the gone name's path from a fourth, as text and not as a mechanism, and the review reads each against the diff there.

Framed 2026-11-04 by framer, before the build.
