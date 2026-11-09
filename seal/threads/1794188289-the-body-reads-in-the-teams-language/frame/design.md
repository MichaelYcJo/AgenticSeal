# Design: 1794188289-the-body-reads-in-the-teams-language

## Grounding

The tree as read at `28fe66be`. The other open work item of the release,
#1452, is read at `d949a652` on `origin/fix/1452-the-body-carries-the-seal-mark`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. The ticket, #1453: the body as folded and its one comment, read with `gh issue view 1453 --json body,comments` on 2026-11-09 (executed) | The comment is the owner's decision and this design builds it: both language rows become required, asked for and written at three points, and a commit is never refused for them. Where nobody is there to answer, the orchestrator writes the rows as the language of the recent pull request titles and records the default in `routing.md`. *Done when*'s first item reads as the comment rewrote it. |
| G2. `skills/core/SKILL.md` *Asking a person is the most expensive step*, and `skills/implement/orchestration.md` *Orchestrator: what needs a person is asked in one batch, before the first edit* (read) | The two rows are asked in the batch that already exists, at first setup and before a work item's first edit, and nowhere later. A question answered by the tree is not asked: where both rows stand, nothing is asked. |
| G3. `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* and *The rule a mechanism is kept against*: a script holds a gate only on a fact it reads exactly, and carries no list of spellings (read) | Whether a row is present is such a fact, so `seal pr-body` may refuse on it (*Scope* item 3). Which language the recent titles are in is a reading of text, so the orchestrator makes it and no script does; the titles are shown to the person, or read for the default, and never block anything. The script compares the two rows' values and derives no file name from either (`plan.md` *Alternatives considered*, row K). |
| G4. `skills/commit-pr-convention/SKILL.md` *Every way of not naming a language lands on English* (read) | Four ways, one rule, and the reason: a config nobody can read must not stop a commit. The reason holds for a commit and this design keeps it there. It does not hold for the pull request body, whose language the team reads, so the body's composer refuses (*Scope* item 5). |
| G5. `skills/commit-pr-convention/SKILL.md` *Pull request bodies* (read) | The body has two parts; `pr.md`'s `Closes`, `Part of` and attribution lines are in `Commit and pull request language` and its quotes in `Record language`. A translated body is a file, `pr.<lang>.md`, named for its own language, that the writer links from the body; its *Where*, *Why there*, *So not under the git directory* and *Not a hosted document* bullets. `seal pr-body` places nothing of it: `skills/code-review/scripts/pr_body.py#read_own` reads `pr.md` alone (read). This design makes the file the body's first part where the rows differ, and the link and the git-directory bullet leave (*Removes*). |
| G6. `templates/setup/config.md`, the table and the sections *Commit and pull request language*, *Record language* and *What no row governs* (read) | The template ships both rows with the value `English`; the mirror paragraph at the end of *What no row governs* states today's rule. The two sections gain the sentence that the rows are required, and the mirror paragraph is rewritten (*Scope* item 4). |
| G7. `skills/config/SKILL.md` *Procedure* step 1 and its table (read) | "Every row but `Mode` and `Broad gate` has a default", and the two language rows' Default cells read `English`. Both sentences stood on the old fact and are rewritten (*Removes*). |
| G8. `skills/implement/bootstrap.md` step 1 (read) | First setup asks once, with one `AskUserQuestion` carrying two questions, the mode and the `Broad gate` row. `seal mode` then writes a config file carrying `Mode` and nothing else, and the orchestrator adds the `Broad gate` row the way `/agentic:config` step 3 adds one, because `skills/implement/scripts/seal.py#write_row` writes the `Mode` row and `skills/config/SKILL.md` *What this does not do* refuses a generic setter. The language rows take the same path: two more questions in the one call, two rows the orchestrator writes into the stub (*Scope* item 1). |
| G9. `skills/implement/scripts/seal.py#NEW_CONFIG` and `#write_row` (read) | The stub `seal mode` writes holds the `Mode` row alone, and its comment names `templates/setup/config.md` as the documentation of every row. So the orchestrator writes the two language rows only, and no prose: the pointer the person needs is already in the file. |
| G10. `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 1 (read) | `routing.md` is written and committed before the first edit. The rows the batch answers, or the default the orchestrator takes, go into that commit, so the first pull request of the repository under this release shows them. |
| G11. `docs/running/the-run.md` *The run*, the paragraph opening **On a run whose `routing.md` reads `Automation` `yes`** (read) | A default taken mid-run is a row of `frame/questions.md`, quoted in `pr.md`. The language default is taken before the frame exists, at the routing commit, and the owner's decision (G1) names `routing.md` as its record. So the sentence stands in `routing.md` *Why this way*, and `pr.md` quotes it as it quotes any record; the paragraph's rule for a question that arises after the frame is unchanged. |
| G12. `skills/code-review/scripts/pr_body.py`: the module docstring, `#read_own`, `#compose`, `#split`, `#_check` and `#main` (read) | The body is `pr.md`'s bytes, the `HEADING` line, the fold. `--check` compares the part above the line with `pr.md` line by line and the part below with the composition. The `Pull request seal mark` row is read through `lib/config.py#declared_value`, so the two language rows are read the same way. The *Limits* paragraph on local mode holds the fact this design stands on: a reader of the pull request cannot open the paths the body names, and the copied text still stands in the body. |
| G13. The 0.35 decision, work item 1793966252 at `4531133b`: `frame/design.md` *Grounding* and *Scope* items 2 and 4, read with `git show 4531133b:seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/design.md` (executed) | `pr.md` holds quotes of the records with their coordinates and no sentence of the orchestrator's own account, committed before the first round so that every round reads it. Its ground was #1415: the orchestrator's part was written after the rounds, so no round read it, and the sealer was its first reader. The record behind it is #1103's subject at `5e5275e5`, read with `git log` (executed): the sealer withheld most verdicts over a hand-written body that restated a record wrongly. This design keeps the decision whole: `pr.<lang>.md` holds the same quotes rendered in the team's language, each with its coordinate, is written before the first round, and is read by every round. No summary returns (`plan.md` *Alternatives considered*, row C). |
| G14. #1452's frame at `d949a652`: `frame/design.md` *Scope* items 1, 2 and 5 and *Data & interfaces*, `frame/plan.md` *Alternatives considered* row A and *Phases* (read through `git show`) | Its `body` arm in `chain_check.py` compares a ready pull request's body with what `seal pr-body` composes at HEAD, through one function `pr_body.py` exposes for `main --check` and the arm alike. A part this work adds to the composition passes that arm, and a part added by hand fails it. Its cases in `tests/skills/test_chain_check.py` and `tests/skills/test_pr_body.py` build a `config.md` holding the mark row, so under *Scope* item 3 each of those fixtures needs the two language rows too. `plan.md` *Overlap with the release* orders the two. |
| G15. `agents/proofer.md` step 3 and the paragraph opening **Every round reads the work item's records that state the present** (read) | Every round reads `pr.md` whole and finds each quote verbatim at its source. `pr.<lang>.md` joins that read, and a rendering is read against the quote it renders, which is the judgment the workflow delegates to the rounds (G3). |
| G16. `agents/sealer.md` step 2 (read) | The sealer runs `seal pr-body --check`, then reads the part above the heading as the work item's `pr.md`. The part gains `pr.<lang>.md` where the rows differ, and the sentence names both files. |
| G17. `docs/forms/the-guarantee.md` *The guarantee*, the paragraph opening **The pull request body opens with the orchestrator's part**; `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*, its file table and the sentence that `pr.md` is the one exception to citing by coordinate; `docs/layout/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read*; `docs/running/what-a-script-gates.md`, the `seal pr-body --check` row (read) | The `docs/` sentences that state the body's parts, the mirror's place and what `seal pr-body` reads. This work item's subject is the code and the skills, so each goes through *Rule changes* (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). |
| G18. `skills/implement/SKILL.md` *The language the records are written in* and *3. The SDD file set*, the `pr.md` row (read) | The record language's independence from the commit language is the premise of a body in one language over records in another. The file table's `pr.md` row gains the mirror. |
| G19. `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` (read: the module docstring and the case names) and `tests/text/test_the_settings_have_a_front_door.py#ROWS` (read) | The language reader `configured_language` and `LANGUAGE_CODES` live in the test module, so a case may hold the name-to-code table and no script does. The mirror cases pin today's rule: `pr.en.md` is the mirror of a Korean repository. Under this design the mirror's language is the commit language where the rows differ, so those cases are rewritten to it (*Scope* item 7). The front-door module pins that the config skill names every row the template ships, which this work keeps. |
| G20. `git grep -l 'pr_body\|pr-body' -- tests evals` (executed): the set of test and eval files that run or scaffold the command, listed by the method of contract rule 12: ten files under `tests/`, ten under `evals/` | The closed set of fixtures that build a `config.md` and run `seal pr-body`, each of which carries the two language rows once *Scope* item 3 lands. The crafter lists the set again at build time with the same command. |
| G21. `git ls-files 'seal/threads/*/pr.*.md' 'seal/threads/*/pr.md'` (executed): nine `pr.md` files and no mirror in any work item of this repository | No committed mirror has to move or be renamed, and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_the_existing_mirrors_are_consistent_with_the_rule` reads an empty set either way. |
| G22. `gh pr list --state all --limit 10`, run here (executed): ten titles, each English with a prefix of the vocabulary | The command the convention already names gives the titles the orchestrator reads for the language it shows beside the question, or takes as the default. In this repository it reads English. |
| G23. `seal/config.md` of this repository (read) | Neither language row is present. Under *Scope* item 3 `seal pr-body` would refuse here, so this work writes both rows as `English` (*Scope* item 6). |
| G24. `seal/follow-up.md` (read) | No row concerns the language rows or the body, so nothing there joins this scope. |
| G25. `skills/settle/rule-changes.md` *Rule changes* and the policy index `docs/README.md` (read) | The shape of each operation below and the files it may name. |

## Scope

In. The items are eight:

1. **First setup asks for the two language rows in its one call.** `skills/implement/bootstrap.md` step 1's one `AskUserQuestion` carries the mode, the `Broad gate` row, `Commit and pull request language` and `Record language`. Beside the language questions the orchestrator shows the titles `gh pr list --state all --limit 10` returned and names the language it reads them in; where the list is empty or `gh` cannot read it, it says so. The option listed first is the titles' language where one was read, and `English` otherwise. Each option names what the row governs in one line, from `templates/setup/config.md`'s two sections. After `seal mode` writes the stub, the orchestrator adds the two rows to its table the way `/agentic:config` step 3 adds a language row, as rows alone (G9), then the `Broad gate` row as today.
2. **A work item whose repository lacks either row starts with the rows.** Before the routing commit, the orchestrator reads both rows of `config.md`. Where either is absent in any of the four ways G4 names, the batch of `skills/implement/orchestration.md` *Orchestrator: what needs a person is asked in one batch, before the first edit* carries the question for both, with the titles shown as item 1 shows them, and the routing commit carries the rows. Where the batch reaches no person, because the routing answer was given for the release and the run is unattended, the orchestrator writes both rows as the language it reads the titles in, `English` where the list is empty, and `routing.md` *Why this way* says in one sentence that the two rows were written as a default taken until answered, naming the language and what it was read from. `pr.md` quotes that sentence. A repository that already has a `config.md` from an earlier release is caught here, so no separate step for the plugin update is written.
3. **`seal pr-body` reads the two rows and composes the body from them.** Both forms refuse, exit 1 and nothing written, where either row is absent in any of the four ways, with one `refused:` line per row naming `config.md`, the row and the section of `templates/setup/config.md` that documents it. Where the two values differ, compared with surrounding whitespace removed and case folded, the body's first part is the work item's one translated file, then `pr.md`, then the `HEADING` line and the fold. The translated file is the one file matching `pr.*.md` in the work item's directory other than `pr.md`; where the rows differ and no such file or more than one is there, the command refuses naming the two rows and the count it found. Where the two values are the same, `pr.md` leads and one `pr.*.md`, where present, follows it. The translated file is read as `pr.md` is read (`#read_own`: as its bytes stand, UTF-8, a line equal to `HEADING` refused), and `--check` compares the whole first part line by line as it compares `pr.md` today. The rows are read through `lib/config.py#declared_value`, as the mark row is. The composition and the comparison stay in the one function #1452 exposes, so the sealer's check and the pull request's arm read the same body (G14). The module docstring states the new first part and its refusals.
4. **`pr.<lang>.md` is the quotes of `pr.md` in the team's language.** Where the two rows differ, the orchestrator writes it beside `pr.md`, before the first round, and commits both together. It holds each quote of `pr.md` rendered in `Commit and pull request language`, in `pr.md`'s order, each followed by the same coordinate, and nothing else: no `Closes`, `Part of` or attribution line, which stand in `pr.md` in that language already, and no sentence of the orchestrator's own (G13). Its name is `pr.<lang>.md` with `<lang>` the writer's spelling for its own language, as today, which is the commit language where the rows differ. Where a fix pass or a fold changes a quote, the orchestrator rewrites the quote and its rendering and commits both before the next spawn. Every round reads it whole against its target, and a rendering that does not render the quote at its coordinate is a finding located in the file (G15). The sealer reads it as part of the first part (G16). The sentences are written in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, `skills/commit-pr-convention/SKILL.md` *Pull request bodies*, `skills/implement/SKILL.md` *3. The SDD file set* in the `pr.md` row, `templates/setup/seal-README.md`'s tree, `agents/proofer.md` step 3 and its whole-read paragraph, `agents/sealer.md` step 2, `templates/setup/config.md`'s two language sections and the mirror paragraph of *What no row governs*, and `skills/config/SKILL.md`'s table. The `docs/` sentences are the operations of *Rule changes*.
5. **The convention says the rows are required and what still lands on English.** `skills/commit-pr-convention/SKILL.md` *Every way of not naming a language lands on English* keeps its four ways and its rule for a commit: the writer writes English and carries on. It gains that the two rows are required: the orchestrator asks for them before the first edit (item 2), `seal pr-body` refuses without them (item 3), and no commit is refused for them (G1). *Before the pull request opens* items 3 and 4 are rewritten to the rows and to the translated file `seal pr-body` places. `skills/config/SKILL.md`'s opening paragraph says four rows have no default, *Procedure* step 1's paragraph on the language rows says the two rows are required, and the two language rows' Default cells say what happens without them.
6. **This repository's `seal/config.md` gains both rows**, `| Commit and pull request language | English |` and `| Record language | English |`, before item 3's refusal lands, so `seal pr-body` and the pull request's arm read a repository that declares its languages (G23).
7. **Cases, each new one seen red before it is planted.** In `tests/skills/test_pr_body.py`: without either row the command exits 1 and its `refused:` line names that row; with rows that differ and one `pr.ko.md`, the body file holds that file, then `pr.md`, then the heading, then the fold; with rows that differ and no `pr.*.md`, and with two, the command refuses naming the rows; with rows that are the same the body is as today; `--check` refuses at the first differing line a body whose first part lacks the translated file. Each fixture of G20's set carries the two rows; the sealer cases under `evals/behaviour/sealer/` are written again from `evals/scripts/rule_cases.py`. Text cases pin what a reader acts on: the bootstrap's one call names the two rows; the batch section of `skills/implement/orchestration.md` names the rows and `routing.md` as the default's record; `skills/config/SKILL.md` no longer gives the two rows the default `English`; the mirror cases of `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` pin the mirror's language as the commit language where the rows differ, and the case that pins `pr.en.md` as a Korean repository's mirror is rewritten to that rule.
8. **The work item's `changelog.md`**, ending with `### Process changes`, one row for item 1, one for item 2 and one for item 4, written by the last phase's crafter.

Out, each with its ground:

- A summary part in `pr.md`, written by the orchestrator in the commit language. It reverses the 0.35 decision and the record under it (G13). `plan.md` *Alternatives considered*, row C, weighs it. The issue's complaint that quotes are not in reading order is the orchestrator's to answer with the order it quotes in: nothing in `skills/code-review/orchestration.md` fixes an order.
- Dropping the claim that `Commit and pull request language` governs the body. The team could then read nothing of the body, which is the issue's second *Done when* item unmet. `plan.md` *Alternatives considered*, row D.
- A warning in place of a required row. The owner rejected it (G1): the first gap went through every party with no warning.
- Refusing a commit for a missing row. The owner kept the convention's rule (G1, G4).
- A script that reads the language of a title, a body or a quote. G3 forbids it; the orchestrator reads the titles and the rounds read the renderings.
- `seal mode` writing the language rows, or a `seal config` setter. G8 and G9: the stub is the `Mode` row's, and the config skill refuses a generic setter.
- A translation of the fold. The records have no mirror (G6): one file, one checker.
- More than one translated file, or a translation in a repository whose rows are the same beyond the one file `seal pr-body` places after `pr.md`. These are limits stated in item 3, not guarded shapes.
- Local mode's place for the translated file. It stands beside `pr.md` under the git directory, and `seal pr-body` copies it into the body as it copies `pr.md`, so the reasons the convention gave for moving it leave with the bullet (*Removes*; G12's limit).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| First setup asks for both rows | Given no `seal/` root at either place, when the orchestrator follows `skills/implement/bootstrap.md` step 1, then its one call carries the mode, the `Broad gate` row and the two language rows, with the recent titles' language beside them, and the config file it commits carries both rows | a text case on the bootstrap, seen red against the file as it stands; the next bootstrap of a repository under the installed release, read by the owner |
| A work item starts in a repository without the rows, with a person present | Given a `config.md` with neither row, when the orchestrator collects the batch before the first edit, then the batch carries the two rows and the routing commit writes them | a text case on `skills/implement/orchestration.md`, seen red against the section as it stands |
| The same, unattended | Given the same repository and a routing answer given for the release, when the orchestrator starts the work item, then `config.md` carries both rows as the language it read the titles in, `routing.md` *Why this way* says so in one sentence, and `pr.md` quotes it | the same text case; the first such pull request, read by the owner |
| `seal pr-body` refuses without a row | Given a `config.md` lacking `Record language`, when either form runs, then it exits 1, writes nothing and prints one `refused:` line naming `config.md`, the row and the template's section | a new case in `tests/skills/test_pr_body.py`, seen red against `pr_body.py` as it stands |
| The body opens in the team's language | Given rows reading `Korean` and `English` and a work item holding `pr.ko.md` and `pr.md`, when `seal pr-body <item> --body <file>` runs, then the file holds `pr.ko.md`, then `pr.md`, then the heading line, then the fold | a new case, seen red against `pr_body.py` as it stands |
| A missing translation is refused | Given the same rows and no `pr.*.md` beside `pr.md`, when either form runs, then it exits 1 and its `refused:` line names the two rows and that no translated file is there | a new case, seen red |
| Two translations are refused | Given the same rows and two `pr.*.md` files, when either form runs, then it exits 1 and its `refused:` line names the count | a new case, seen red |
| One language leaves the body as it is | Given rows that both read `English` and no `pr.*.md`, when the command runs, then the file is `pr.md`, the heading and the fold, as before this work | the existing cases of `tests/skills/test_pr_body.py`, green with the rows added to their fixtures |
| A body without the translation fails the check | Given the differing rows and a body file whose first part is `pr.md` alone, when `--check` runs, then it exits 1 at the first line that differs | a new case, seen red with the translated file left out of the comparison |
| The pull request's arm passes the composed body | Given #1452's arm on the base and a body `seal pr-body` composed with the translated file, when the arm compares the payload's body, then it finds no difference | #1452's own cases in `tests/skills/test_chain_check.py`, green with the rows added to their fixtures after the base is merged in |
| A commit is never refused | Given a repository without the rows, when a commit is made, then nothing this work adds reads the rows at a commit | `git grep` of the diff for readers of the two rows finds `pr_body.py`, the skills' prose and the tests alone |
| The issue's second *Done when* item | Given a downstream repository with `Record language` `English` and `Commit and pull request language` `Korean`, when its next work item reaches the pull request, then the body opens with `pr.ko.md`, passes `seal pr-body --check` and passes #1452's arm | that repository's next pull request under the installed release, read by the owner |

## Data & interfaces

`seal pr-body <item> --body <file>` writes the body file as, in order:

```
<pr.<lang>.md's bytes, where the two language rows differ>
<pr.md's bytes>
## From the records
<the seal mark where the row and the guarantee give one>
<details>
...
</details>
```

Where the rows are the same, the first part is `pr.md`'s bytes and then the bytes of the one `pr.*.md` where one is present. A file that does not end in a line end gets one, as `pr.md` does today, so the next part starts on its own line. Exit codes are unchanged: 0 written or matching, 1 refused, 2 the arguments are unusable.

The two rows are read by `lib/config.py#declared_value(home, item)` with the row names `Commit and pull request language` and `Record language`, from the same `config.md` the mark row is read from, in the work item's own checkout. No file, no such row and an empty value are one state, absent; a file that does not parse, such as a doubled row or a table the walker refuses, is not read as absent and reaches the command as a refusal naming that line, as it does for the mark row. Both exit 1 on `seal/config.md`. The two values are compared after surrounding whitespace is removed and case is folded, and nothing else is read from them: `Korean` and `korean` are one language, and `Korean` and `한국어` are two, which the template's sentence that the value is a language's English name already asks the writer to avoid.

The translated file is found by listing the work item's directory for names matching `pr.*.md` other than `pr.md`; the name's middle part is read by nothing.

The new `refused:` lines take the form `pr_body.py#_place` writes, one per cause, each naming the file under the root and the line where a line applies:

```
refused: <root>/config.md: has no `Record language` row; `templates/setup/config.md` *Record language* says what it governs, and the orchestrator asks for it before the first edit
refused: <root>/config.md: has no `Commit and pull request language` row; `templates/setup/config.md` *Commit and pull request language* says what it governs, and the orchestrator asks for it before the first edit
refused: <root>/threads/<id>: `Commit and pull request language` reads `Korean` and `Record language` reads `English`, and no `pr.<lang>.md` stands beside `pr.md`; the orchestrator writes it before the first round
refused: <root>/threads/<id>: holds 2 files matching `pr.*.md`, and one body has one translation
```

The exact words are the crafter's; what each line names is fixed here.

`seal/threads/<work-item-id>/pr.<lang>.md`, written and committed by the orchestrator with `pr.md`:

```
"<a quote of pr.md, rendered in Commit and pull request language>" (`<path>` *<heading>*)
```

One line, list item or table cell per quote, in `pr.md`'s order, each with the coordinate the quote carries in `pr.md`.

`seal/config.md` of this repository gains two rows, each `| <row> | English |`.

## Rule changes

- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: `seal pr-body` writes `pr.md` above the line
    `skills/code-review/scripts/pr_body.py#HEADING` holds, as its bytes
    stand, and below that line the copy of the work item's records
  to: `seal pr-body` writes above the line
    `skills/code-review/scripts/pr_body.py#HEADING` holds the work item's
    `pr.<lang>.md`, where `seal/config.md`'s
    `Commit and pull request language` and `Record language` rows name
    different languages, and then
    `pr.md`, each as its bytes stand, and below that line the copy of the
    work item's records
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: `pr.md` holds the `Closes` lines, in the pull request's language,
    and quotes of the records, in the records' language, each with its
    coordinate, and no sentence of the orchestrator's own account; the
    orchestrator commits it before the first round, so every round reads it
  to: `pr.md` holds the `Closes` lines, in the pull request's language,
    and quotes of the records, in the records' language, each with its
    coordinate, and no sentence of the orchestrator's own account;
    `pr.<lang>.md` holds those quotes rendered in the pull request's
    language, each with the same coordinate, and nothing else; the
    orchestrator commits them before the first round, so every round reads
    them. `seal pr-body` refuses where either language row is absent, so a
    body is composed only for a repository that declared its languages
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: and withholds where the part above the line is not `pr.md` or the
    part below it is not what the records give.
  to: and withholds where the part above the line is not what `pr.md` and,
    where the rows differ, `pr.<lang>.md` give, or the part below it is not
    what the records give.
- add
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  to: | `pr.<lang>.md` | each quote of `pr.md` rendered in `Commit and pull request language`, with its coordinate, where that row and `Record language` name different languages; written and committed with `pr.md`, read by every round, and placed by `seal pr-body` as the body's first part |
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: | `pr.md` | what the pull request body opens with:
  to: | `pr.md` | what the pull request body opens with, after
    `pr.<lang>.md` where the two language rows differ:
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: (`gaps.md`, `changelog.md`, `guarantee.md`, `pr.md`, and a `pr.*.md`
    where one was written)
  to: (`gaps.md`, `changelog.md`, `guarantee.md`, `pr.md`, and `pr.<lang>.md`
    where the two language rows differ)
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: `pr.md` is the one exception, because the pull request's reader
    meets it before the fold: it holds the `Closes` lines and quotes of the
    other records, each standing word for word at the coordinate it names,
    and no fact of its own.
  to: `pr.md` and `pr.<lang>.md` are the one exception, because the pull
    request's reader meets them before the fold: `pr.md` holds the `Closes`
    lines and quotes of the other records, each standing word for word at
    the coordinate it names, `pr.<lang>.md` holds those quotes rendered in
    the pull request's language, and neither holds a fact of its own.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: so the language lives in a config row, and the mirror file a
    translated pull-request body goes in is named for the language it holds
    rather than for one language.
  to: so the language lives in a config row, and the mirror file a
    translated pull-request body goes in is named for the language it holds
    rather than for one language. The two language rows are required: first
    setup and the batch before a work item's first edit ask for them, with
    the language of the recent pull request titles shown beside the
    question, and `seal pr-body` refuses to compose a body without them.
    Where nobody is there to answer, the orchestrator writes them as the
    titles' language and `routing.md` says so. A commit is never refused for
    them.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: a pull request is read by whoever opens it, and a record by whoever
    comes back to the decision six months later.
  to: a pull request is read by whoever opens it, and a record by whoever
    comes back to the decision six months later. Where the two rows differ,
    the pull request body opens with `pr.<lang>.md`, the quotes of `pr.md`
    rendered in the team's language, and `pr.md` follows it, so the records
    keep one language and the team reads the body in theirs.
- change
  file: docs/running/the-run.md
  section: The run
  from: `pr.md`, the pull request body's first part, where the owner can
    overturn it.
  to: `pr.md`, which the pull request body's first part holds, after
    `pr.<lang>.md` where the two language rows differ, where the owner can
    overturn it.
- add
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  to: Where `seal/config.md`'s two language rows differ, the body the check
    compares opens with the work item's `pr.<lang>.md` and then `pr.md`, as
    `seal pr-body` composes it, and where either row is absent the check
    refuses on `seal/config.md`, as `seal pr-body` does.
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: | `seal pr-body --check` | the sealer | the body file against the records | withholds | none |
  to: | `seal pr-body` and `seal pr-body --check` | the orchestrator; the sealer | `config.md`'s two language rows; `pr.md`; the one `pr.<lang>.md` where the rows differ; the body file against them and the records | refuses without a row, and without the one `pr.<lang>.md` the rows ask for; withholds | whether `pr.<lang>.md` renders `pr.md`: the rounds and the sealer |

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the sentence *Where a translated body is wanted, the writer puts it in the repository as a file and links it from the body.* and the link as the way the translation reaches the reader | `skills/commit-pr-convention/SKILL.md` *Pull request bodies* | `seal pr-body` places the file as the body's first part where the rows differ (*Scope* item 3); the sentence is rewritten to say so |
| the bullet *So not under the git directory.* with its three reasons | `skills/commit-pr-convention/SKILL.md` *Pull request bodies* | the file is copied into the body as `pr.md` is, so a reviewer reads it in the pull request, and the local-mode limit of `pr_body.py`'s docstring already covers the paths a reader cannot open (G12) |
| the paragraph *That folder sits under the root, which is resolved rather than spelled … The mirror then goes beside the documents the pull request already touches.* | `templates/setup/config.md` *What no row governs* | the same reason as the row above; the preceding paragraph is rewritten to the new rule |
| the sentences *An English repository keeps a Korean mirror at `<root>/threads/<work-item-id>/pr.ko.md`; a Korean one keeps an English mirror at `pr.en.md`.* and the test pins that read a Korean repository's mirror as `pr.en.md` | `skills/commit-pr-convention/SKILL.md` *Pull request bodies*; `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_a_korean_row_is_what_flips_the_refused_mirror_name` and the docstring of `#test_a_config_holding_the_templates_default_row_reads_as_english` | the mirror's language is the commit language where the rows differ, and the sentence and the pins are rewritten to that rule (*Scope* items 4 and 7) |
| the sentence *Every row but `Mode` and `Broad gate` has a default*, the paragraph opening *Every way of not naming a language lands on English*, and the two Default cells reading `English` | `skills/config/SKILL.md` opening paragraph, *Procedure* step 1 and its table | rewritten: four rows have no default, the two language rows are required, and each language cell says `seal pr-body` refuses without the row while a commit writes English |
| the instruction to copy a missing language row with the `## Broad gate` section *rather than writing a bare row* | `skills/config/SKILL.md` *Procedure* step 3 | rewritten: a missing language row is added as a row alone, and the section is copied for the `Broad gate` row only (*Scope* item 1, G9) |
| the paragraph opening *This file is optional, and an absent row is not an error, with two exceptions*, and the case `test_the_template_says_the_file_is_optional` that pinned `optional` | `templates/setup/config.md`; `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` | rewritten to four exceptions, the two language rows among them; the case is rewritten as `#test_the_template_names_the_rows_an_absent_one_is_refused_for` |
| the *Record language* reason that an absent row's default is what every repository got, and the *Mode* sentence *Every other item here falls back to what repositories got before the row existed* | `templates/setup/config.md` *Record language* and *Mode* | rewritten: the language rows have no default |
| the paragraph saying the body's first part is `pr.md` and the orchestrator translates neither part | `skills/writing-style/outside-the-review.md`, the paragraph opening *리뷰 체인을 거친 작업 항목의 PR 본문은 두 부분이고* | rewritten: `pr.<lang>.md` opens the first part where the rows differ, and the translation stays in that record (*Scope* item 4) |
| the lists of what the orchestrator writes and what a verifying round reads, without `pr.<lang>.md` | `skills/code-review/orchestration.md` the verifying round's `Target` row; `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 2 | rewritten to name `pr.<lang>.md` (*Scope* item 4) |
| the sealer's `description` naming `pr.md` alone as the body's first part, and the convention's sentence *one that says nothing writes English* | `agents/sealer.md` `description`; `skills/commit-pr-convention/SKILL.md` | rewritten to the first part *Scope* item 3 lays out and to the required rows (*Scope* item 5) |
| the sentence *writes English and carries on rather than asking* as the whole rule for a missing row | `skills/commit-pr-convention/SKILL.md` *Every way of not naming a language lands on English* | rewritten: it stays the rule for a commit, and the rows are asked before the first edit and required by `seal pr-body` (*Scope* item 5) |
| *one `AskUserQuestion` carrying **two questions*** and *`seal mode` has just written a config file carrying `Mode` and nothing else, so the orchestrator adds the row* | `skills/implement/bootstrap.md` step 1 | rewritten to four questions and to the rows the orchestrator adds (*Scope* item 1) |
| the sentences that named `pr.md` alone as the body's first part, or as the one part with no sentence of the orchestrator's own | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the bold opening; `skills/commit-pr-convention/SKILL.md` *Pull request bodies*; `templates/setup/config.md`; `lib/optin.py`'s `PR` comment; the `pr.md` lines of `templates/setup/seal-README.md` and `seal/README.md`; `skills/implement/SKILL.md`'s `pr.md` row; two sentences of `skills/writing-style/outside-the-review.md` | rewritten: the first part is `pr.<lang>.md` and then `pr.md` where the rows differ (*Scope* items 3 and 4; round 1, finding 2) |
| the sentence *Every other item in `config.md` falls back to* | `lib/config.py#declared_mode` docstring | rewritten: four rows have no default (*Scope* item 5; round 1, finding 3) |
| *The body opens with the work item's `pr.md`, the orchestrator's part, written as its bytes stand, and `HEADING` follows it on its own line.* | `skills/code-review/scripts/pr_body.py` module docstring | rewritten to the first part *Data & interfaces* lays out |

What this work adds is a refusal in `seal pr-body`, on two rows and one file it reads exactly. What goes in return is the hand step that linked the translation from the body and the exception that moved it out of the git directory, both above. What the refusal would have caught is the issue's record: two pull requests opened on 2026-11-09 with bodies no reader of the team could read, which every party passed because nothing read the rows.

Framed 2026-11-09 by framer, before the build.
