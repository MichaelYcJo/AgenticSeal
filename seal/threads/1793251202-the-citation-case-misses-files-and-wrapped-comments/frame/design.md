# Design: 1793251202-the-citation-case-misses-files-and-wrapped-comments

Issue #1127, row R33 of #956's audit. The issue was measured at `c825fd2c`.
This frame reprobed at its own base, `02170cf5` (`8d8d6390` plus the routing
commit). The contract-rule citation reader is unchanged between the two:
`git diff c825fd2c HEAD` over
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` touches
no line of `CITATION`, `CITED_TREES`, `CITED_FILES`, `tree_files` or
`dangling` (executed). #1111 (#1146) rewrote only the module's pins.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source, and a change removes in the same commit what stood on the old fact. The repository already holds one corpus walk for citations: `tests/behaviour/test_a_cited_section_stands_in_its_file.py#citations` lists every tracked file outside `tests/censuses.py#RECORDS` and reads it through `#flowing`, which drops `#` comment markers. The contract-rule case keeps a second walk of six trees and one file, and that second copy is the defect #1127 names. So the contract-rule case reads through the first walk, and the second walk goes. |
| `CONTRIBUTING.md` *The test layout* | A test file whose cases load or run shipped code stands in `tests/behaviour/`, and one that only reads text stands in `tests/text/`. The sibling module loads `skills/settle/scripts/rule_changes.py` and `hooks/lib/config.py` at import (`:36-40`, read). Importing `flowing` from it into the `tests/text/` module would make that module load shipped code. Moving the contract-rule citation cases into the sibling module does not. |
| `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | A contract rule is cited as `contract rule <N>`, and as `rule <N>` inside the contract and `agents/`. A near miss is refused at its line. Its `check:` line already names both modules (`:268`, read), so moving the cases needs no edit there. The contract module keeps a case that reads this rule: a contract heading in another spelling is refused at its line (`test_a_heading_in_the_old_spelling_is_refused_at_its_line`). |
| `skills/agent-contract/SKILL.md`, the paragraph above rule 1 | A rule number is never reused. A citation in a permanent file such as `seal/follow-up.md` therefore stays true, and the case reads it. A file under `seal/threads/` or `evals/behaviour/` keeps what it said when it was written (`tests/censuses.py:848-850`, read), and the case does not read it. |
| `skills/agent-contract/SKILL.md` rules 12, 15, 19 and 20 | Rule 12: the class is a citation the reader cannot see, so the fix covers every comment-marked file type and adjacent string literals, not the `#`-in-a-hook coordinate alone. Rule 15: every new case is shown red against the reader as it stood before the change. Rule 19: the old walk, its constants and the moved cases' old timing keys go in the commit that replaces them. Rule 20: replacing the walk is weighed as an equal of widening it (`frame/plan.md` *Alternatives considered*). |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below names every unit that leaves the contract module and where it lands. |
| The 2026-10-29 process change of v0.24.1 (#1091) | A unit that is only moved is proved by its existing cases at the new path. Phase 1 moves the cases unchanged and writes no new case. Phase 2 adds behaviour and writes the red-first cases. |
| `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD` (a check, not policy) | Every test scope that lists paths from git is registered and passes its list through `conftest.on_disk`. The sibling module's `#citations` row is there now (`:85-87`, read). Where the build moves the `ls-files` call into a function both readers share, that row names the new scope. |

### What the probes answered

Each fact below is `executed` at `02170cf5`. They come from one read-only
`python3 -I` script under the scratchpad. It held the regexes of both modules
copied as they stand, imported nothing from the tree, and read the worktree
through `git ls-files`. The script and its output were deleted before this
frame was written.

- The contract has sections 1 to 20.
- `git ls-files` lists 908 paths. Outside `RECORDS` and on disk, 325 decode
  as UTF-8 and 9 do not; all 9 are `.png` files under `assets/` and
  `.claude-plugin/`. The old walk reads 262 files. Reading all 325 takes
  0.066 s.
- The wider corpus adds 63 files. They come from `.claude-plugin`,
  `.github`, `CLAUDE.md`, `README.md`, `README.ko.md`, `SECURITY.md`,
  `LICENSE`, `assets`, `bin`, `evals` (outside `evals/behaviour/`),
  `install.sh`, `uninstall.sh`, `ruff.toml`, `.gitattributes`,
  `.gitignore`, `.test_durations` and the `seal/` root's own files. One
  file sits inside the six trees and is still unread:
  `templates/setup/hygiene.yml`. The old walk keeps only `.md`, `.py`,
  `.yaml`, `.json` and `.txt`, so it skips every `.yml` file.
- Citations recognised: the old walk finds 230 and the wider corpus 232.
  The two added are `seal/follow-up.md:48` and `:50`, both `contract rule
  12`. Nothing dangles and nothing is a near miss in either corpus, with
  or without `flowing`. Running `flowing` over the 325 files changes the
  citation count in none of them. The change is green on the tree as it
  stands.
- `CLAUDE.md`, `.github/`, `evals/scripts/`, `README.md` and the `seal/`
  root's `README.md` and `config.md` hold no `contract rule <N>`.
  `evals/behaviour/` holds none either (`git grep -P` for each).
- The issue's shape, `# as the contract` over `# rule 99 says` in
  `hooks/x.py`: the current reader finds nothing. The same reader over
  `flowing`'s text finds rule 99 at line 1. The same shape indented under
  `  # ` in a `.yml` file is found at line 1 once `flowing` runs.

## Scope

**In.**

1. The contract-rule citation cases move from
   `tests/text/test_the_agent_contract_holds_the_universal_rules.py` into
   `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, unchanged
   (phase 1). These are the reader of `contract rule <N>` and `rule <N>`,
   the reader of near misses, and the seven cases that use them. Each
   moved case's `.test_durations` key is rewritten to the new path, with
   its measured seconds kept.
2. The moved reader reads the sibling module's corpus: every tracked path
   outside `tests/censuses.py#RECORDS` that is on disk and decodes as
   UTF-8. It reads one `git ls-files` listing per run, in one scope that
   both readers call (phase 2). `CITED_TREES`, `CITED_FILES` and
   `tree_files` go.
3. Both moved readers (the dangling-citation reader and the near-miss
   reader) read each file through the module's `flowing`. So a `#`
   comment marker at the start of a line is dropped in every file that is
   not `.md`, and adjacent string literals are joined in `.py` files.
   Line breaks are kept, so a citation is named at the line it starts on
   (phase 2).
4. The sibling module's docstring states what the module reads now: both
   citation shapes, which files are read, which are left out and why
   (phase 2).
5. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD`
   names the scope that holds the `ls-files` call, if that scope's name
   changes (phase 2).

**Out, and why.**

- `tests/text/test_the_agent_contract_holds_the_universal_rules.py`'s
  shape and fact cases (`FACTS`, `spans`, the check-line cases, the
  heading cases) stay where they are. They read the contract file alone,
  and none calls `tree_files` (read).
- A `#` at the start of a line in a `.md` file opens a heading, so
  `as the contract` followed by a `# rule 5` line in markdown is a heading
  and not a wrapped citation. `flowing` leaves `.md` text alone, as it
  does for section citations. This is a stated limit and gets no case.
- Comment markers other than `#` are not dropped. The corpus's extensions
  are `.py` (219), `.md` (71), `.png` (9), `.yml` (7), `.ans` (7), `.txt`
  (4), `.json` (4), `.svg` (2), `.sh` (2), `.cmd` (2), `.toml` (1), and
  `.gitignore` and `.gitattributes` (executed: `git ls-files` outside
  `RECORDS`). The two `bin/*.cmd` files comment with `REM` or `::`
  (`grep` executed), and the two `.svg` files are seal images under
  `assets/seals/`. Neither holds a contract citation. This is a stated
  limit and gets no case.
- `BARE_HOMES` stays `("agents",)`. A bare `rule <N>` in `CLAUDE.md`,
  `.github/` or anywhere else outside the contract and `agents/` can be any
  list's rule. The existing case
  `test_a_bare_rule_outside_the_contracts_homes_is_not_a_citation` pins
  this, and it moves unchanged.
- The `.test_durations` keys of cases #1111 removed or renamed, such as
  `test_dropping_an_enforcer_from_one_of_the_four_is_caught` and
  `test_deleting_a_pinned_phrase_is_caught[2]` to `[20]`, are not this
  work's. `test_the_durations_file_prices_the_suite` allows a stale share
  of 5 % (`STALE_SHARE`, read), and that case judges them at the broad
  gate.
- `skills/verify/scripts/deferral_check.py` (#1123),
  `skills/verify/scripts/pact_check.py` (#1132), and the framer's input
  and the `rule-framer-sharp-s` eval (#1158) are open in parallel work
  items. Nothing here edits them.
- No shipped script, `seal` subcommand or CI step changes. The check is a
  case of this repository's suite.

## User scenarios & acceptance *(mandatory)*

`the module` below is `tests/behaviour/test_a_cited_section_stands_in_its_file.py`.
`N` is one more than the contract's last section number, computed by the
case at run time, so the module's own source never holds a dangling
citation. Every fixture tree is built with the module's `repo(tmp_path,
files)`.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The moved cases pass at their new path | Given phase 1's commit, when the module runs, then each of the seven moved cases passes under its old function name and its old parameter ids. The contract module no longer defines them. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_the_agent_contract_holds_the_universal_rules.py. The phase 1 record lists each old node id beside its new one. |
| S2 The tree | Given the tracked files at the branch head, when the contract-rule case reads the corpus, then no citation dangles and no near miss stands. At least 50 citations are recognised and more than 100 files are read, so a reader that stops matching cannot pass on nothing. At `02170cf5` the reader recognises 232 citations over 325 files. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S3 A file outside the six trees is read | Given a fixture tree holding `contract rule N` in `CLAUDE.md`, `.github/workflows/x.yml`, `evals/scripts/x.py` and `templates/x.yml`, when the contract-rule reader reads it, then each file is named at its line. Against phase 1's walk, none is named. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py. Seen red against phase 1's commit, recorded in phase 2's record. |
| S4 A record is not read | Given the same citation in a file under each prefix of `RECORDS`, beside one in `a.md`, then only `a.md` is named. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S5 A citation wrapped across `#` comment markers | Given `hooks/x.py` holding `# as the contract` over `# rule N says`, then rule N is named at `hooks/x.py:1`. The same holds for a `.yml` file whose lines are indented before `# `. Against phase 1's reader, neither is named. This is the issue's second *Done when*. Its red is shown against the base's reader, which is the reader of `c825fd2c` (see the head of this design). | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py. Seen red against phase 1's commit, recorded in phase 2's record. |
| S6 A citation split across adjacent `.py` literals | Given `hooks/x.py` holding `"as the contract "` and, on the next line, `"rule N says"`, then rule N is named at line 1. Against phase 1's reader, it is not. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py. Seen red against phase 1's commit. |
| S7 A near miss wrapped across `#` | Given `hooks/x.py` holding `# per the contract's` over `# rule 7`, then the near-miss reader refuses it at line 1. Against phase 1's reader, it does not. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py. Seen red against phase 1's commit. |
| S8 The module says what it leaves out | The module's docstring names the corpus (the tracked files on disk, outside `RECORDS`, decoding as UTF-8). It names the three kinds of file left out, each with its reason: a record keeps what it said when written; a file that is not UTF-8 holds no text; a file the working tree deleted cites nothing. | Read at review. This is the issue's first *Done when*. |

## Data & interfaces

**The corpus.** One function of the module runs `git -C <root> ls-files
-z`. It keeps the paths outside `RECORDS` that `conftest.on_disk` finds on
disk, and opens each with the module's `text_of`. It hands back the
tracked listing and `[(rel, text)]` for every file that decoded. Both
readers call it: `citations(root)` for section citations, and the
contract-rule reader for `contract rule <N>`. The function's name is the
build's choice. `citations(root)` still needs the whole tracked listing
for its `top` and `skills` sets and for `target in tracked`, so the
function returns that listing too.

**The contract-rule reader.** It takes a root and the contract's section
numbers. The tree case passes `ROOT` and the numbers read from
`skills/agent-contract/SKILL.md`, and a fixture case passes its fixture
root and the same numbers. It returns `[(path:line, rule N)]` for each
dangling citation, in the shape `dangling` returns now. `cited_sections`
and `near_citations` read `flowing(rel, text)` in place of `text`. So
`near_citations` takes `rel` as well. The near-miss case for the tree
reads the same corpus.

**Imports.** The module imports `HEADING`, `spans` and `CONTRACT` (or
`read`) from `test_the_agent_contract_holds_the_universal_rules`, as five
modules already import `HEADING` from it (`git grep` executed). The
contract module's `os` import stays, because it builds `CONTRACT`.

**What the reader does with input it cannot read**, stated for #956's
audit.

| Input | Outcome |
|---|---|
| A file under a `RECORDS` prefix | not read |
| A tracked file that does not decode as UTF-8 | not read |
| A tracked file the working tree deleted | not read; the sweep judges what it finds |
| `# rule N` under `as the contract` in a `.md` file | not read; it is a heading |
| A bare `rule N` outside the contract and `agents/` | not a citation |

## Rule changes

- nothing
  why: no section of the policy root `docs/` states which files the contract-rule citation case reads or how it reads a citation across a comment marker (`seal/config.md` has no `Policy root` row, read; `git grep` for the module and for `contract rule` in `docs/` finds only `docs/the-broad-gate.md:42`, a `check:` line #1111's pending change already re-points). The citation shape is stated in `skills/writing-style/SKILL.md`, and that sentence does not change.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The second corpus walk and its two lists | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#tree_files`, `#CITED_TREES`, `#CITED_FILES` | the module's corpus function, which reads every tracked text file outside `RECORDS` |
| The contract-rule citation readers and constants | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#CITATION`, `#BARE_CITATION`, `#NEAR_CITATION`, `#BARE_HOMES`, `#cited_sections`, `#dangling`, `#near_citations` | moved to `tests/behaviour/test_a_cited_section_stands_in_its_file.py` |
| The seven contract-rule citation cases | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_every_cited_section_exists`, `#test_a_citation_above_the_last_section_is_caught`, `#test_a_wrapped_citation_is_named_at_the_line_it_starts_on`, `#test_a_bare_rule_outside_the_contracts_homes_is_not_a_citation`, `#test_no_file_cites_the_contract_in_a_near_miss`, `#test_a_near_miss_citation_is_refused_at_its_line`, `#test_the_one_spelling_is_no_near_miss` | moved to `tests/behaviour/test_a_cited_section_stands_in_its_file.py` under the same names |
| The moved cases' 15 timing keys under the old path | `.test_durations`, the keys under `tests/text/test_the_agent_contract_holds_the_universal_rules.py::` for the seven cases above | the same keys under the module's path, with the seconds kept |
| The section banner `# --- citations (#957)` | `tests/text/test_the_agent_contract_holds_the_universal_rules.py` | moves with the cases |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-29 by framer, before the build.
