# Feature Specification: 1793171930-no-check-reads-a-citation-of-most-files

Issue #1043. The spec is the issue body as #1052 folded it to the renamed
tree. Its first citation, in `docs/the-review-record.md`, was corrected by
the 0.22.4 settle `de11df75` and needs nothing here (read at
`docs/the-review-record.md:682-683`). What remains is the check, and every
citation that check finds pointing at nothing.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source, and a change removes in the same commit what stood on the old fact. The new case replaces the `implement`-only case instead of standing beside it, and it takes the list of record directories it skips from `tests/censuses.py#RECORDS` instead of keeping a second copy. |
| `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | Another file's section is cited as the backticked path followed by its heading text in italics, and a line a check reads is read in one spelling, a near miss refused at its line. So the case matches the cited text case-sensitively, and the sentence that states the citation shape names what the case now holds. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | A pull request does not edit the policy root (`docs/` here: `seal/config.md` has no `Policy root` row, read). A heading renamed outside `docs/` can leave a `docs/` citation pointing at nothing until the settle writes the correction a spec's `## Rule changes` states. That citation is reported, not failed. |
| `skills/settle/SKILL.md` *Rule changes* | `skills/settle/scripts/rule_changes.py` is the one reader of a `## Rule changes` section. The case reads the pending corrections through its `parse`, and reads headings through its `headings`, and writes no second parser. |
| `CONTRIBUTING.md` *The test layout* | A test file that loads shipped code stands in `tests/behaviour/`; it takes `ROOT` from `tests/conftest.py`; a helper two test files use is defined once, in `tests/conftest.py`. The new case loads `rule_changes.py` and `hooks/lib/config.py`, so it stands in `tests/behaviour/`. |
| `CONTRIBUTING.md` *What a change to a gate must carry* | The case is seen red before the citations it finds are corrected, the failure direction is stated (it refuses more), and what it removes is named below. |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below names the old case, its helpers, its timing entries and the imports it alone used. |
| `docs/the-record-layout.md` *seal/threads/<work-item-id>/* | A document that cites a record as it once stood writes the path a commit holds, as `<commit>:<path>`. The one living comment that cites a heading on purpose because it is gone is rewritten to that form. |
| `skills/agent-contract/SKILL.md` rules 12, 15 and 19 | The class is enumerated (every cited file, not `implement`'s alone), each new case is seen red, and the three citations the case finds are corrected in place. |

## Scope

**In.**

1. One case, in a new module
   `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, resolves
   every citation of another file's section in the tracked text files
   outside the records against that file's headings and bold rule leads. It
   replaces `tests/behaviour/test_the_set_a_work_item_always_has.py#test_every_cited_heading_of_implement_exists`
   and that file's refusing case for it.
2. The three citations the case finds at the head this branch was cut from
   (executed: a throwaway read-only scan, described under *Data &
   interfaces*, run at `de2a30fd`) are corrected in place:
   - `.github/scripts/gather_changelog.py:43-44` names
     `docs/the-record-layout.md`'s *A marker counts only on a live line*.
     The document has no heading or rule lead with those words; the phrase
     is the script's own bold lead at `:38`. The rule meant is the one that
     opens *Whether a line is live is asked by what the line does*
     (`docs/the-record-layout.md:140`), whose second bullet names
     `unverified_check.py#live_lines` and the changelog marker (`:149-156`,
     read). The citation names that lead.
   - `skills/verify/scripts/mutation_check.py:103-104` names
     `agents/crafter.md`'s *commit before you mutate*. The rule lead there
     opens *Commit before you mutate* (`agents/crafter.md:105`, read), and a
     case-sensitive reader refuses the lowercase spelling. The citation takes
     the lead's capital.
   - `tests/behaviour/test_one_word_one_meaning.py:461-462` names
     `docs/the-broad-gate.md` *Where the stamp is drawn* in a comment that
     says the section is gone. It is gone (`f1c9932d`, #975, removed it;
     `git log -S` executed), so the comment cites it as the commit before
     the removal held it, `f6ae6db6:docs/the-broad-gate.md`, where the
     heading stands at line 117 (`git show` executed; `f6ae6db6` is an
     ancestor of `HEAD`, executed).
3. A citation in a file of the policy root that a pending `## Rule changes`
   item corrects is reported as a warning naming the work item, and the case
   passes. Every other unresolved citation fails the case.
4. The sentence of `skills/writing-style/SKILL.md` that states the citation
   shape names the bold rule lead as a citable target beside the heading,
   and its `check:` line names the new module.

**Out, and why.**

- `tests/text/test_broad_gate_rule.py:78-86` pins one citation of
  `skills/code-review/orchestration.md` by its exact text. It stays: its
  assertion is that the broad gate section names the owner of when the run
  comes, which a resolver does not hold. The file is #1040's to edit.
- `tests/text/test_the_agent_contract_holds_the_universal_rules.py` resolves
  `rule <N>` citations, a different shape with its own reader. Untouched.
- #1053 removes the gather step, edits `gather_changelog.py` and removes
  `changelog/`. This work edits only the one citation at
  `gather_changelog.py:43-44`. `changelog/` and `CHANGELOG.md` stay outside
  the corpus through `tests/censuses.py#RECORDS`, and that entry is #1053's
  to change when the directory goes.
- #956 audits how every reader of written text fails on input it cannot
  read, this case among them once it lands. The table under *Data &
  interfaces* states that behaviour for the audit to start from; this work
  files no audit row and changes no other reader.
- Whether `CLAUDE.md` gains the rule *a gate fails closed* is #923's Q9,
  decided with #956's table. Not here.
- No shipped script, `seal` subcommand or CI step: the check is a case of
  this repository's suite. A plugin user's repository cites in its own
  conventions, and nothing asks for a gate there.
- A citation of a work item's own record by a path relative to the work
  item, such as `frame/design.md` *Scope* or `plan.md` *Alternatives
  considered*, names no file of the repository and cannot be resolved
  without knowing which work item is meant. It is not read.
- A heading in `docs/` renamed or removed by a pending `change` or `remove`
  still stands in the tree until the settle, so citations of it resolve
  until then. The settle's own suite run meets any that the settle leaves
  dangling; `skills/settle/SKILL.md` *Answer every check that reads the
  corpus* is where that session answers it.
- Other citation shapes: `path#unit`, `pact:<name>/"<heading path>"@<hash>`,
  and a section named in prose without the path immediately before it.

## User scenarios & acceptance *(mandatory)*

The module is `tests/behaviour/test_a_cited_section_stands_in_its_file.py`,
written `the module` below. Each fixture scenario builds its own scratch tree
under `tmp_path`.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The tree | Given the tracked files at the branch head, when the case reads every citation outside the records, then each resolves, or is excused by S9. Before the three corrections of *Scope* item 2 it fails naming `.github/scripts/gather_changelog.py:43`, `skills/verify/scripts/mutation_check.py:103` and `tests/behaviour/test_one_word_one_meaning.py:461` (line of the opening backtick). It also asserts it recognised at least 100 citations, so a reader that stops matching cannot pass. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py. Red run against the tree before the corrections recorded in phase 1's record. |
| S2 A heading renamed in a scratch copy | Given a scratch tree where `a.md` cites `` `docs/b.md` *Old name* `` and `docs/b.md` has `## Old name`, when the heading is renamed to `## New name`, then the case names `a.md`, the line, and `*Old name*` as dangling; before the rename it resolves. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S3 A prefix at a word boundary | Given `## 2b. Settle what earlier releases left behind`, then `*2b*` and `*2b. Settle*` resolve, and `*2*` and `*2b. Settl*` do not: the heading resolves a cited text that equals it or begins it with the next character neither a letter nor a digit. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S4 A bold rule lead | Given a paragraph or list item opening `**Commit before you mutate, and restore.**`, then `*Commit before you mutate*` resolves and `*commit before you mutate*` does not. The same lead inside a fenced block does not resolve, and neither does a heading inside one. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S5 The other spellings of a citation | `` `docs/b.md`'s *X* ``, `` `implement` *X* `` and `` the `implement` skill's *X* `` are each read, the two name forms against `skills/<name>/SKILL.md` for any `<name>` whose `SKILL.md` is tracked. A citation wrapped across a line break resolves and is named at the line it starts on. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S6 A citation inside Python | In a `.py` file, a citation wrapped across consecutive `#` comment lines is read with the comment markers dropped, and one split across adjacent string literals is read joined. A cited text holding `{` is a placeholder of an f-string or a format string and is not read. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S7 A path the case does not read, and a path it refuses | A path whose first segment is not a tracked top-level entry of the repository (`frame/design.md`, `plan.md`, `code.claude.com/...`) is not read, and neither is a `<commit>:<path>` citation. A path whose first segment is one (`docs/`, `skills/`, `CONTRIBUTING.md`) and that names no tracked file is refused as dangling: a file that moved leaves its citations as a renamed heading does. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S8 The records are not read | A dangling citation in a file under a prefix of `tests/censuses.py#RECORDS` is not read. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S9 A pending correction in the policy root | Given `docs/a.md` citing a heading no file has, and `seal/threads/1-x/frame/design.md` holding a `change` with `file: docs/a.md`, a `from` that holds `*<cited text>*` and a `to` that does not, then the case passes and raises one warning naming `docs/a.md`, the line, the citation and `seal/threads/1-x/`. A `remove` with no `from` excuses a citation standing in the section it names. Without the item, or with the item naming another file, or with the same dangling citation in a file outside the policy root, the case fails. A `## Rule changes` section `rule_changes.parse` refuses excuses nothing. | check: tests/behaviour/test_a_cited_section_stands_in_its_file.py |
| S10 The rule names its case | `skills/writing-style/SKILL.md`'s citation sentence names the bold rule lead as a citable target, and its `check:` line names the module. | check: tests/github/test_rules.py. `bin/seal rules --check` reads the edited `check:` line. |

## Data & interfaces

**What the case reads.** Every path `git ls-files` lists that reads as UTF-8
text and does not start with a prefix of `tests/censuses.py#RECORDS`
(`seal/threads/`, `changelog/`, `CHANGELOG.md`, `evals/behaviour/`, read at
`tests/censuses.py:871`). The old case read six extensions and its own
three-prefix list (`tests/behaviour/test_the_set_a_work_item_always_has.py:449`
and `:476-479`). `seal/process/` is read: it holds no citation of this shape
at the head (executed: `git grep` over it, zero).

**What counts as a citation.** One of three spellings, read over the file's
text with every run of whitespace collapsed to one space, and, outside a
`.md` file, with a `#` comment marker at the start of a continuation line
dropped; in a `.py` file adjacent string literals are joined first.

| Spelling | Resolved against |
|---|---|
| `` `<path>.md` *<text>* ``, or `` `<path>.md`'s *<text>* `` | `<path>` |
| `` `<name>` *<text>* `` | `skills/<name>/SKILL.md`, where that file is tracked |
| `` the `<name>` skill's *<text>* `` | `skills/<name>/SKILL.md`, where that file is tracked |

`<path>` is the backticked text alone, with no `:` before it, so
`<commit>:<path>` is never read. `<text>` runs to the next `*` and holds none.

**What a citation resolves to.** A live heading of the named file at any
level, as `rule_changes.headings` and `rule_changes.heading_text` read it
(`skills/settle/scripts/rule_changes.py:61-76`), or a live bold rule lead: a
paragraph or list item whose text opens with `**`, the lead running to the
closing `**`, whitespace collapsed. A citation resolves when its text equals
a heading or lead, or begins one and the next character is neither a letter
nor a digit. Matching is case-sensitive and character for character
otherwise, markup included: a heading holding a code span is cited with the
code span, as `skills/settle/SKILL.md`'s heading *What `--apply` does* is.

**What the reader does with input it cannot read**, stated for #956's audit.

| Input | Outcome |
|---|---|
| A citation whose path names no tracked file, first segment tracked | refused, dangling |
| A citation whose path's first segment is not tracked | not read |
| `<commit>:<path>` | not read |
| Cited text holding `{` | not read |
| A section named in another shape | not read; outside the grammar |
| A `## Rule changes` section `parse` refuses | excuses nothing, so the citation fails |
| A file that does not decode as UTF-8 | not read |

**The measurement this frame stands on** (executed at `de2a30fd`, a
read-only `python3 -I -c` over `git ls-files`, not the case): 363
citations resolved against a heading, 3 against a bold lead and 1 through
the `skill's` spelling; 42 named a path outside the repository; 4 held a
placeholder; 3 did not resolve, the three of *Scope* item 2. The scan's
first pass, which read exact headings only and no Python joins, also showed
what the prefix rule and the joins are for: `docs/the-review-record.md:409`
cites `docs/the-broad-gate.md` *One act, one owner*, whose heading is
*One act, one owner, and the owner is the orchestrator*;
`docs/the-record-layout.md:283` cites `docs/release-checklist.md` *2b*;
`tests/behaviour/test_a_release_publishes_its_note.py:30` cites that file's
*5*; and fourteen citations of repository files in `.py` files wrap across
`#` lines or adjacent literals.
These counts are of the scan, which reads the grammar above approximately;
the case is what decides.

**The warning of S9.** One `warnings.warn` per excused citation, naming the
citing file and line, the citation, and the work item directory whose
`frame/design.md` holds the correcting item. The policy root is
`hooks/lib/config.py#policy_root` over the `seal/` root.

## Rule changes

- nothing
  why: no document of the policy root states how a section is cited or that a cited section is checked; the citation shape lives in `skills/writing-style/SKILL.md`, which this pull request edits in place

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `implement`-only citation case | `tests/behaviour/test_the_set_a_work_item_always_has.py#test_every_cited_heading_of_implement_exists` | S1 of the new module reads every file's citations, `implement`'s two name forms among them |
| Its refusing case and fixture constant | `tests/behaviour/test_the_set_a_work_item_always_has.py#test_a_cited_heading_implement_lacks_is_dangling`, `#MISSING_STEP` | S2 and S5 of the new module |
| Its reader | `tests/behaviour/test_the_set_a_work_item_always_has.py#SKILL_NAMED`, `#CITED_TITLE`, `#implement_headings`, `#dangling_implement_citations`, `#cited_files` | the new module's reader; no other file uses them (`git grep` executed) |
| A second list of the record directories | `tests/behaviour/test_the_set_a_work_item_always_has.py#NOT_CITATIONS` | `tests/censuses.py#RECORDS` |
| The three timing entries of the removed cases | `.test_durations`, the keys for `test_a_cited_heading_implement_lacks_is_dangling` (two) and `test_every_cited_heading_of_implement_exists` | the cases are gone |
| The imports only the removed cases used | `tests/behaviour/test_the_set_a_work_item_always_has.py`, `import subprocess`, `import pytest` and `on_disk` from `conftest` | nothing else in the module uses them (`grep` executed); ruff confirms at the build |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.
