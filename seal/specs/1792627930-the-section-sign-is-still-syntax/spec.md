# Feature Specification: #1005 the section sign is still syntax

In this file "the section sign" is the character U+00A7. The frame never
writes the character itself, so the check this work adds can read this file
like any other. "A comment" is an HTML comment, and "a fence" is a fenced
code block.

The owner widened the scope on 2026-10-22, relayed by the orchestrator: a
symbol that is not truly needed is not written, and records stop carrying
comments and needless fences. Scope items 10 to 14 are that widening.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-agent-set.md` *One contract every agent receives, and one definition each* | The contract's rule numbers are stable, and a prompt and a round record cite a rule by its number. So the contract's rules keep their numbers and are cited by number with no symbol, never by heading text. The sentence itself changes from "section" to "rule" through `## Rule changes` below. |
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*, and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | No section sign in text an agent or a check reads. A check reads one spelling and refuses a near miss at its line. An instruction names who acts, when, on which file, and what counts as done. |
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source: guidance copied into every record from its template is a second copy of the skill its writer reads, and a fence rule written in two modules is two copies. The one check this work adds replaces the section-sign arms of four readers (see `## Removes`). |
| `CONTRIBUTING.md` *What a change to a gate must carry* | The pull request names what this work removes and its prompt budget, which is zero: nothing here asks a person anything. |
| `CONTRIBUTING.md` *House rules* | Only the branch based on `main` writes `changelog/` and `CHANGELOG.md`. This branch edits neither. |
| `evals/README.md`, the five pass rules of the behaviour suite | A rewrite of a preload is proved not worse by the paid suite. Rule 4 (the preload is fewer bytes than the baseline's) is read for free with `evals/scripts/noninferiority.py#preload_bytes`. "Nothing in the tree makes a later edit owe a run." |
| `docs/branch-and-release.md` *Work accumulates on a release branch* | Each changelog entry is written under a comment naming its work item, invisible to a reader. This is the marker spelling `questions.md` Q1 keeps by default. |
| `docs/the-review-record.md` *The round record* and *What the check reads at the pull request* | A finding holds its paste-ready fix in a fence, and a labelled line inside a fence or a comment is not a line. The fence state stays (scope item 12); the comment half stays while old records carry comments (`questions.md` Q6). |
| `docs/the-record-layout.md` *seal/specs/<work-item-id>/* | Where the two new rules on comments and fences in records are added, through `## Rule changes`. |
| `skills/settle/SKILL.md` *Rule changes* and *A rule has one shape* | The grammar of `## Rule changes` below. |

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

**In scope: the section sign.**

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

**In scope: comments and fences in records.**

10. **The record templates carry no comment and no guidance.** The eight
    `templates/sdd-*.md` (spec, plan, questions, routing, overview, phase,
    round, guarantee) hold 23 comments at a16acb40 (executed), and plan and
    questions also carry guidance as body prose. After this work a template
    holds only headings, table headers, placeholders in angle brackets, the
    labelled lines a record's grammar asks for, and the foot line. Every
    comment in them is guidance (read, all eight); none is a marker a reader
    reads.
11. **Each guidance sentence lands once, in what its writer reads.** The
    party that builds phase 4 searches each sentence's home with `git grep`
    on its words. A sentence its home already states is removed. One it does
    not state moves there. The homes are in the table under
    `## Data & interfaces`. A home that is preloaded (an agent definition)
    takes a sentence only where no other home fits, and phase 4 measures the
    preload.
12. **One fence state, written once.** The readers keep reading a fence,
    because a finding's paste-ready fix stays fenced and a fix to a record's
    own grammar can hold a line shaped like a label. In 150 round records at
    a16acb40 no labelled line stands at a line start inside a fence
    (executed), but #986's evaluation reports held one, and a reader that
    trusted "never" would read it. The fence delimiter rule and the line
    split are each written twice today, in `hooks/blocks.py` and
    `skills/verify/scripts/unverified_check.py`, held in step by two tests.
    After this work the skill module imports the hook module's copy, and the
    two tests go.
13. **The new rules are stated in docs, through `## Rule changes`:** a record
    a template starts carries no comment, and a record holds a fence only
    around a finding's paste-ready fix, with every labelled line a check
    reads outside every fence at the start of its line. A case refuses a
    comment in `templates/sdd-*.md`.
14. **The old records, under `questions.md` Q6.** 611 files across all 125
    work items carry a comment, about 12,240 lines of them (executed; the
    line figure is a regex count, not the shared reader's). By default (Q6
    answer b) they stay as written, and the readers keep the comment and
    code-span states until the owner's settle retires the backlog; a later
    item removes those states. Under answer (a), phase 6 strips them and
    removes the states now.

**Out of scope.**

- The records of a moment, for the section sign. They state what was true
  when written, and `changelog/` belongs to the branch based on `main`.
  Their comments are Q6's.
- The changelog markers. They stay `<!-- specs/<id> -->` by default
  (`questions.md` Q1). Refusing a near miss is not added either: 27 lines in
  11 release files open a comment naming `seal/specs/` in an older fragment
  convention (executed), so a reading that refused near misses would refuse
  released lines this branch may not edit.
- `unverified_check.py#live_lines` keeps its comment, code-span and fence
  states. Its callers read files that are not records: the release files
  and their comment markers (`gather_changelog.py`), the policy root's index
  (`fold_check.py`) and the policy documents a rule change is applied to
  (`rule_changes.py#apply_op`). Those files are the consuming project's,
  written in its own convention.
- `hooks/blocks.py`'s comment-block walk. It serves `seal/config.md`, where
  `templates/config.md` documents parking a row in a comment, and old
  `routing.md` files until Q6 is settled.
- The `<!-- specseal:start -->` and `<!-- specseal:end -->` lines of
  `templates/claude-md-block.md`. An installer and two tests read them to
  find the block in a person's `CLAUDE.md`, and they must not render there:
  they are the needed case.
- The comment `skills/implement/scripts/seal.py` writes at the head of a new
  `seal/config.md`, and the comment in `templates/pact.md`. Neither file is a
  work item's record, and the config reader keeps comments for the reason
  above. The pact file is Q2's.
- The coordinate grammar's `#` and `>` in `skills/verify/scripts/coordinates.py`
  and the pact anchors it reads (`questions.md` Q2). At a16acb40 that file
  carries one section sign, in a docstring, and its grammar reads none
  (executed).
- A paid non-inferiority run (`questions.md` Q3).
- A resolver for every file-and-heading citation in the tree. A regex
  reading at a16acb40 found 311 such citations with 33 unresolved, and many
  of the 33 are false hits on Python strings split across lines or on
  f-string templates (executed). A reading that noisy is a report, not a
  gate. Scope item 9 covers the citations this work touches.
- The dash in the release heading `## X.Y.Z — <date>`, which
  `gather_changelog.py#heading_re` reads. Neither the issue nor
  `seal/specs/1792459424-docs-states-the-current-rule-in-one-read/questions.md`
  Q2 names it. Read, not run: a hyphen in its place still matches
  `heading_re`, with no date. The orchestrator reports it to the owner.
- Dashes, arrows and middle dots in lines this work touches for another
  reason, except the contract's rule 12 heading (scope item 1).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 contract headings | Given the contract at head, when its headings are read, then they are `## 1` to `## 20` with a title and no gap or repeat; and a heading written with the section sign is refused at its line by the one heading reader. | `tests/test_the_agent_contract_holds_the_universal_rules.py`, a case seen red with one heading put back in the old spelling |
| S2 contract citations | Given `contract rule 21` in `skills/x/SKILL.md`, or `rule 21` in `agents/x.md`, or `contract` and `rule 21` split across a line break, when the citation reader runs, then each is refused as a rule the contract does not have. Given `rule 21` in `hooks/x.py`, then it is not read as a citation. | the same module, parametrized cases seen red against the old reader |
| S3 the old spelling | Given a section sign in any living file, when the case of scope item 6 runs, then it fails naming `<path>:<line>`. Given one under `seal/specs/`, `changelog/`, `CHANGELOG.md` or `evals/behaviour/`, then it passes. At head it finds no line. | the case of scope item 6, seen red at the tree before phase 3's rewrite, where it lists the residue |
| S4 file citations | Given `` `skills/implement/SKILL.md` *9. No such step* `` in a living file, when the implement citation reader runs, then it is refused as dangling. | `tests/test_the_set_a_work_item_always_has.py`, a case seen red |
| S5 preload bytes | Given each of framer, smith, warden, sealer and scribe, when `noninferiority.py#preload_bytes` is read at the branch's base and at head, then head is fewer bytes for every agent. | the free measurement in `plan.md`, phases 1, 3 and 4, recorded in each phase record |
| S6 printed text | Given each message of scope item 8, when it is printed, then it carries no section sign and its new text is pinned. | the module that pins each message, each case seen red |
| S7 touched citations resolve | Given a citation phases 2 and 3 touch whose file exists, when the phase closes, then the citation names a heading of that file, or the phase record lists what it became. | the phase records; read by the warden |
| S8 rule changes | Given this spec, when `rule_changes.parse` reads it, then it yields one `change` and two `add`, and `apply_op` places each in its document at the base. | executed by the framer at a16acb40; the pull request check re-reads it |
| S9 records untouched | Given the diff from the base to head, when it is listed for `seal/specs/`, `changelog/`, `CHANGELOG.md` and `evals/behaviour/`, then only this work item's own directory appears (under Q6 answer b). | `git diff --name-only <base>..HEAD` over those four paths |
| S10 templates carry no comment | Given `templates/sdd-*.md` at head, when the template case reads them, then none holds `<!--`; with one comment put back, the case fails naming the file and line. | `tests/test_a_record_carries_no_comment.py`, seen red |
| S11 guidance lands once | Given each sentence phase 4 takes out of a template, when the phase closes, then its phase record names where the sentence now stands (file and heading) or the owner that already stated it; and each case that pinned a template sentence pins it at its new home. | phase 4's record; the 17 test modules that read `templates/sdd-*` at a16acb40 (executed count) |
| S12 one fence rule | Given `unverified_check.py` at head, when its fence delimiter rule and line split are asked, then they are `hooks/blocks.py`'s; a labelled line inside a closed fence in a round record is still not read, and a fence that never closes is still refused at its opening line. | `tests/test_chain_check.py` and `tests/test_unverified_rows_close.py` at head, with the two in-step cases gone |
| S13 old records, under Q6 answer (a) only | Given the records stripped, when the check reads a record that holds a line beginning `<!--`, then it refuses that line, and `comment_scan` and `strip_comments` no longer exist. | phase 6's cases, built only under Q6 answer (a) |

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
| `skills/verify/scripts/unverified_check.py#fence_opener`, `#fence_closes`, `#GFM_LINE_RE`, `#gfm_lines` | a second copy of `hooks/blocks.py`'s rule and split | imported from `hooks/blocks.py`, which `unverified_check.py` already reaches by path for `hooks/config.py` (read, its line 1047) |

**The section-sign case.** It lists every text file git tracks, skips the
four record paths, and fails with one line per hit, `<path>:<line>`, and a
sentence saying to cite a file by its heading text and a contract rule as
`contract rule <N>`. The party that builds phase 3 chooses its module, and
the writing-style rule's `check:` line names it.

**The template case.** `tests/test_a_record_carries_no_comment.py` reads
every `templates/sdd-*.md` and fails with `<path>:<line>` for each line
holding `<!--`. The first `add` under `## Rule changes` names this module.

**Where template guidance lands.**

| Template | Its writer | Home for a sentence its owner does not already state |
|---|---|---|
| `sdd-spec.md`, `sdd-plan.md`, `sdd-questions.md` | the framer, or the orchestrator where `Planning` answers `the session` | `skills/implement/SKILL.md` *3. The SDD file set* |
| `sdd-overview.md`, `sdd-phase.md` | the party that builds | `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show*, and *3. The SDD file set* |
| `sdd-routing.md` | the orchestrator | `skills/implement/orchestration.md` *What the answer writes* |
| `sdd-round.md` | the warden | `docs/the-review-record.md` *The round record* already owns the grammar; a sentence it lacks goes to `skills/code-review/SKILL.md` *The record* |
| `sdd-guarantee.md` | the sealer | `docs/the-review-record.md` *The guarantee* already owns the rules; a sentence it lacks goes to `agents/sealer.md`, measured |

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
- add
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  to: **A record a template starts carries no HTML comment.** Its template
    holds headings, table headers, placeholders, the labelled lines the
    record's grammar asks for and the foot line, and nothing else. The
    guidance for writing the record is in the skill or agent definition its
    writer reads, stated there once. A comment copied into every record is
    a second copy of that guidance, and every reader of the record has to
    model it.
    check: tests/test_a_record_carries_no_comment.py
- add
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  to: **A record holds a fence only around a finding's paste-ready fix, and
    a labelled line a check reads stands outside every fence, at the start
    of its line.** The readers keep one fence state, by the fence rule of
    `hooks/blocks.py`, because a fix to a record's own grammar can hold a
    line shaped like a label, and that line belongs to the fix.
    check: tests/test_chain_check.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| Five copies of the contract heading pattern | `tests/test_a_commit_names_its_repository.py#HEADING`, `tests/test_a_moved_rule_leaves_its_definition.py#HEADING`, `tests/test_a_probe_that_commits_says_so.py#HEADING`, and the inline patterns in `tests/test_broad_gate_rule.py` and `tests/test_the_seal_is_taken_once_by_the_sealer.py` | `tests/test_the_agent_contract_holds_the_universal_rules.py#HEADING`, imported by each |
| The list form and the file-name heuristic of the contract citation reader | `tests/test_the_agent_contract_holds_the_universal_rules.py#OTHER_FILE`, and the list arm of `#CITATION` | A citation names one number, and another file's section is cited by heading text, so no number follows a file name |
| The step-number citation reader for `implement` | `tests/test_the_set_a_work_item_always_has.py#CITED_NUMBER` | `#CITED_TITLE` reads the heading-text citation that replaces every step-number citation |
| The section-sign arms of two citation readers | `tests/test_no_passage_is_pasted_into_a_second_file.py#SECTION`, `tests/test_the_set_a_work_item_always_has.py#CITED_TITLE` | The case of scope item 6 refuses the old spelling, so no reader keeps an arm for it |
| The docs sentence naming the contract's "section numbers" | `docs/the-agent-set.md` *One contract every agent receives, and one definition each* | `## Rule changes` above |
| The section sign in 747 lines of 144 living files | every living file, listed at build time by `git grep` | The spellings under `## Data & interfaces`; the case of scope item 6 keeps it out |
| The 23 comments of the eight record templates, and the body guidance of `sdd-plan.md` and `sdd-questions.md` | every `templates/sdd-*.md` | The homes under `## Data & interfaces`, or the owner that already states each sentence; phase 4's record lists which |
| The second copy of the fence rule and of the line split | `skills/verify/scripts/unverified_check.py#fence_opener`, `#fence_closes`, `#GFM_LINE_RE`, `#gfm_lines` | `hooks/blocks.py`, imported |
| The two cases that held the copies in step | `tests/test_unverified_rows_close.py#test_the_fence_rule_agrees_with_the_config_reader`, `tests/test_the_hooks_hide_what_a_renderer_hides.py#test_the_walks_line_rule_is_the_readers` | One copy has nothing to agree with |
| Under Q6 answer (a) only: the comment states of the record readers, and the old records' comments | `skills/verify/scripts/unverified_check.py#comment_scan`, `#strip_comments`, the comment half of `skills/code-review/scripts/chain_check.py#unclosed`, and the comments of 611 record files | Records carry no comment; a line beginning `<!--` in a record is refused at its line |

## Open questions

Anything a planner must answer lives in `questions.md`, not inline.

Framed 2026-10-22 by framer, before the build.
