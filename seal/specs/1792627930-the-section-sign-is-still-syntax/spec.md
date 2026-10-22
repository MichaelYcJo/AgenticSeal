# Feature Specification: #1005 the section sign is still syntax

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md holds WHAT this work
delivers and how we'll know. The policy documents in docs/ outrank this file;
the framer cites them and does not restate them. -->

In this file "the section sign" is the character U+00A7. The frame never
writes the character itself, so the check this work adds can read this file
like any other.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-agent-set.md` *One contract every agent receives, and one definition each* | The contract's rule numbers are stable, and a prompt and a round record cite a rule by its number. So the contract's rules keep their numbers and are cited by number with no symbol, never by heading text. The sentence itself changes from "section" to "rule" through `## Rule changes` below. |
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*, and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | No section sign in text an agent or a check reads. A check reads one spelling and refuses a near miss at its line. An instruction names who acts, when, on which file, and what counts as done. |
| `CLAUDE.md` *The rule a mechanism is kept against* | The one check this work adds replaces the section-sign arms of four readers (see `## Removes`). A check gates only a fact it reads, so the new check reads one byte value and no words. |
| `CONTRIBUTING.md` *What a change to a gate must carry* | The pull request names what this work removes and its prompt budget, which is zero: nothing here asks a person anything. |
| `CONTRIBUTING.md` *House rules* | Only the branch based on `main` writes `changelog/` and `CHANGELOG.md`. This branch edits neither. |
| `evals/README.md`, the five pass rules of the behaviour suite | A rewrite of a preload is proved not worse by the paid suite. Rule 4 (the preload is fewer bytes than the baseline's) is read for free with `evals/scripts/noninferiority.py#preload_bytes`. "Nothing in the tree makes a later edit owe a run." |
| `docs/branch-and-release.md` *Work accumulates on a release branch* | Each changelog entry is written under an HTML comment naming its work item, invisible to a reader. This is the marker spelling `questions.md` Q1 keeps by default. |
| `skills/settle/SKILL.md` *Rule changes* | The grammar of `## Rule changes` below. |

## Scope

**Living files** are every text file git tracks, except the records of a
moment: `seal/specs/`, `changelog/`, `CHANGELOG.md`, and `evals/behaviour/`,
whose cases `evals/README.md` says are generated from records and never
edited by hand. Counts below were taken at a16acb40 with `git grep -n -I`
for the section sign (executed).

| Where | Lines | Files |
|---|---|---|
| `tests/` | 535 | 90 |
| Python outside `tests/` (`hooks/`, `.github/scripts/`, `skills/*/scripts/`, `evals/scripts/`) | 120 | 37 |
| `skills/` Markdown (`agent-contract/SKILL.md` 26, the rest in three `orchestration.md` files and `code-review/SKILL.md`) | 38 | 5 |
| `agents/` | 31 | 5 |
| `README.md`, `README.ko.md`, `CONTRIBUTING.md` | 8 | 3 |
| `assets/seals/README.md` | 7 | 1 |
| `seal/follow-up.md` | 6 | 1 |
| `.github/workflows/` | 2 | 2 |
| All living files | 747 | 144 |
| Records of a moment, not touched | 5077 | 835 |

By form, the 747 living lines hold 391 occurrences of the sign before a
number, 271 before an italic heading, and 129 before anything else (executed).
`docs/` and `templates/` hold none (executed).

**In scope.**

1. The contract's numbering. Each of the 20 headings of
   `skills/agent-contract/SKILL.md` becomes `## <N> <title>`, the number, one
   space, the title. Rule 12's heading loses its dash. The preamble says a
   spawn prompt cites a rule as `contract rule <N>` and that a rule number is
   never reused or re-ordered.
2. Every citation of a contract rule in a living file becomes
   `contract rule <N>`. In the contract itself and in `agents/*.md`, which
   receive the contract at startup, a citation is the bare `rule <N>`. Each
   number is cited on its own: no plural and no list form.
3. Every citation of another file's section becomes the backticked path, a
   space, and the heading text in italics, exactly as the heading reads. A
   citation that named a section by number (`skills/implement/SKILL.md` and
   its step 3, `docs/release-checklist.md` and its step 5) names that
   section's heading text instead.
4. Every other section sign in a living file becomes words: a label a script
   prints, the seal emblem's description in `assets/seals/README.md` and
   `.github/scripts/release_seal.py`, and the remaining forms in comments
   that point at a lettered or named part of a document.
5. The readers that parse the section sign read the new spelling only, and
   change in the same commit as the text they read. They are listed under
   `## Data & interfaces`.
6. One case refuses a section sign in a living file, naming the path and the
   line. A fixture that needs the old spelling builds it with
   `"\N{SECTION SIGN}"` so the fixture's own file stays clean.
7. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
   읽히게 쓴다* states the citation shape of items 2 and 3 once, and its
   `check:` line names the module of item 6's case and the module of the
   contract citation reader.
8. Text a person reads that changes is pinned by a case (contract rule 14),
   and the case is seen red before it is planted (contract rule 15): the label
   `skills/verify/scripts/session_cost.py` prints for a spawn by an agent,
   the refusal messages of `skills/verify/scripts/broad_gate.py`, the message
   of `skills/settle/scripts/settle.py`, and the `specified_by` text
   `.github/scripts/tracker_labels.py` prints.
9. A citation this work touches, whose file exists in the tree, names a
   heading that file has at build time. Where it does not (for example
   `agents/sealer.md` cites `docs/the-review-record.md` *The broad run has
   one home*, and `tracker_labels.py` cites `docs/issues-and-milestones.md`
   *A label answers what it is about, and survives the move*; neither heading
   exists, executed), the party that builds the phase rewrites it to the
   heading that now holds the rule, and records each one in its phase record.

**Out of scope.**

- The records of a moment. They state what was true when written, and
  `changelog/` belongs to the branch based on `main`.
- The changelog markers. They stay `<!-- specs/<id> -->` by default
  (`questions.md` Q1). Refusing a near miss is not added either: 27 lines in
  11 release files open a comment naming `seal/specs/` in an older fragment
  convention (executed), so a reading that refused near misses would refuse
  released lines this branch may not edit.
- The coordinate grammar's `#` and `>` in `skills/verify/scripts/coordinates.py`
  and the pact anchors it reads (`questions.md` Q2). At a16acb40 that file
  carries one section sign, in a docstring, and its grammar reads none
  (executed), so the issue's claim that the grammar reads one no longer
  holds.
- A paid non-inferiority run (`questions.md` Q3).
- A resolver for every file-and-heading citation in the tree. A regex
  reading at a16acb40 found 311 such citations with 33 unresolved, and many
  of the 33 are false hits on Python strings split across lines or on
  f-string templates (executed). A reading that noisy is a report, not a
  gate. Item 9 covers the citations this work touches.
- The dash in the release heading `## X.Y.Z — <date>`, which
  `gather_changelog.py#heading_re` reads. Neither the issue nor
  `seal/specs/1792459424-docs-states-the-current-rule-in-one-read/questions.md`
  Q2 names it. Read, not run: a hyphen in its place still matches
  `heading_re`, with no date. The orchestrator reports it to the owner.
- Dashes, arrows and middle dots in lines this work touches for another
  reason, except the contract's rule 12 heading (item 1).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 contract headings | Given the contract at head, when its headings are read, then they are `## 1` to `## 20` with a title and no gap or repeat; and a heading written with the section sign is refused at its line by the one heading reader. | `tests/test_the_agent_contract_holds_the_universal_rules.py`, a case seen red with one heading put back in the old spelling |
| S2 contract citations | Given `contract rule 21` in `skills/x/SKILL.md`, or `rule 21` in `agents/x.md`, or `contract` and `rule 21` split across a line break, when the citation reader runs, then each is refused as a rule the contract does not have. Given `rule 21` in `hooks/x.py`, then it is not read as a citation. | the same module, parametrized cases seen red against the old reader |
| S3 the old spelling | Given a section sign in any living file, when the case of item 6 runs, then it fails naming `<path>:<line>`. Given one under `seal/specs/`, `changelog/`, `CHANGELOG.md` or `evals/behaviour/`, then it passes. At head it finds no line. | the case of item 6, seen red at the tree before phase 3's rewrite, where it lists the residue |
| S4 file citations | Given `` `skills/implement/SKILL.md` *9. No such step* `` in a living file, when the implement citation reader runs, then it is refused as dangling. | `tests/test_the_set_a_work_item_always_has.py`, a case seen red |
| S5 preload bytes | Given each of framer, smith, warden, sealer and scribe, when `noninferiority.py#preload_bytes` is read at the branch's base and at head, then head is fewer bytes for every agent. | the free measurement in `plan.md`, phases 1 and 3, recorded in each phase record |
| S6 printed text | Given each message of item 8, when it is printed, then it carries no section sign and its new text is pinned. | the module that pins each message, each case seen red |
| S7 touched citations resolve | Given a citation phases 2 and 3 touch whose file exists, when the phase closes, then the citation names a heading of that file, or the phase record lists what it became. | the phase records; read by the warden |
| S8 rule changes | Given this spec, when `rule_changes.parse` reads it, then it yields one `change`, and `apply_op` places it in `docs/the-agent-set.md` at the base. | executed by the framer at a16acb40; the pull request check re-reads it |
| S9 records untouched | Given the diff from the base to head, when it is listed for `seal/specs/`, `changelog/`, `CHANGELOG.md` and `evals/behaviour/`, then only this work item's own directory appears. | `git diff --name-only <base>..HEAD` over those four paths |

## Data & interfaces

**Spellings after this work.**

| What | Spelling |
|---|---|
| A contract heading | `## <N> <title>` |
| A contract rule, cited outside the contract and `agents/` | `contract rule <N>` |
| A contract rule, cited inside the contract or an agent definition | `rule <N>` (`contract rule <N>` is read there too) |
| A section of another file | the backticked path, a space, then the heading text in italics |

**Readers that change, each in the commit that rewrites the text it reads.**

| Reader | Now | After |
|---|---|---|
| `tests/test_the_agent_contract_holds_the_universal_rules.py#HEADING` | the sign, a number, a title | `## <N> <title>`, and the one copy every other module imports |
| `tests/test_the_agent_contract_holds_the_universal_rules.py#CITATION`, `#NUMBER`, `#cited_sections` | the sign before a number, after a contract name or bare in `agents/`, with a list form and a heuristic for a file name before it | `contract rule <N>` everywhere and `rule <N>` in the contract and `agents/`, read across a line break |
| `tests/test_no_passage_is_pasted_into_a_second_file.py#SECTION`, `#SECTION_TOKEN` | an arm for the sign before an italic heading, and a token holding the sign | the path arm alone, and a token in words |
| `tests/test_the_set_a_work_item_always_has.py#CITED_NUMBER`, `#CITED_TITLE` | the sign before a step number, and the sign or `skill's` before a title | `CITED_NUMBER` goes; `CITED_TITLE` reads the path or `` `implement` `` then the italic title |
| `.github/scripts/tracker_labels.py` `specified_by`, and `tests/test_a_declared_label_reaches_the_tracker.py`, which splits it on the sign | path, the sign, heading | path and italic heading; the test splits on the space before the italic |
| `tests/test_a_commit_names_its_repository.py#HEADING`, `tests/test_a_moved_rule_leaves_its_definition.py#HEADING`, `tests/test_a_probe_that_commits_says_so.py#HEADING`, the inline patterns in `tests/test_broad_gate_rule.py` and `tests/test_the_seal_is_taken_once_by_the_sealer.py` | five copies of the heading pattern | removed; each imports the one `HEADING` |

**The new case.** It lists every text file git tracks, skips the four
record paths, and fails with one line per hit, `<path>:<line>`, and a
sentence saying to cite a file by its heading text and a contract rule as
`contract rule <N>`. The module it lives in is the party that builds phase
3's choice, and the writing-style rule's `check:` line names it.

## Rule changes

- change
  file: docs/the-agent-set.md
  section: One contract every agent receives, and one definition each
  from: **The contract's section numbers are stable.** A prompt saying
    *section 3 is narrowed this round*, and a round record compared with
    another months later, hold only while the number still means what it
    meant;
  to: **The contract's rule numbers are stable.** A prompt saying
    *contract rule 3 is narrowed this round*, and a round record compared
    with another months later, hold only while the number still means what
    it meant;

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| Five copies of the contract heading pattern | `tests/test_a_commit_names_its_repository.py#HEADING`, `tests/test_a_moved_rule_leaves_its_definition.py#HEADING`, `tests/test_a_probe_that_commits_says_so.py#HEADING`, and the inline patterns in `tests/test_broad_gate_rule.py` and `tests/test_the_seal_is_taken_once_by_the_sealer.py` | `tests/test_the_agent_contract_holds_the_universal_rules.py#HEADING`, imported by each |
| The list form and the file-name heuristic of the contract citation reader | `tests/test_the_agent_contract_holds_the_universal_rules.py#OTHER_FILE`, and the list arm of `#CITATION` | A citation names one number, and another file's section is cited by heading text, so no number follows a file name |
| The step-number citation reader for `implement` | `tests/test_the_set_a_work_item_always_has.py#CITED_NUMBER` | `#CITED_TITLE` reads the heading-text citation that replaces every step-number citation |
| The section-sign arms of two citation readers | `tests/test_no_passage_is_pasted_into_a_second_file.py#SECTION`, `tests/test_the_set_a_work_item_always_has.py#CITED_TITLE` | The case of scope item 6 refuses the old spelling, so no reader keeps an arm for it |
| The docs sentence naming the contract's "section numbers" | `docs/the-agent-set.md` *One contract every agent receives, and one definition each* | `## Rule changes` above |
| The section sign in 747 lines of 144 living files | every living file, listed at build time by `git grep` | The spellings under `## Data & interfaces`; the case of scope item 6 keeps it out |

## Open questions

Anything a planner must answer lives in questions.md, not inline: unanswered
questions buried in prose read as decided.

Framed 2026-10-22 by framer, before the build.
