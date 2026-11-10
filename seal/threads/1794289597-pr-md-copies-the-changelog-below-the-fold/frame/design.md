# Design: 1794289597-pr-md-copies-the-changelog-below-the-fold

## Grounding

The tree as read at `53cab03ea`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | The subject of this work item is the code: what `skills/code-review/scripts/pr_body.py` composes, and the plugin's skill and agent texts that state it. So the documents of the policy root change through `## Rule changes` below, and the build edits no file under `docs/`. No unsettled design states an operation to re-point: each other `frame/design.md` under `seal/threads/` holds `- nothing` (executed, `awk` over the `## Rule changes` section of each). `docs/layout/one-root-by-lifetime.md` has a `.ko.md` edition, so its operation carries one on that edition, as `skills/settle/rule-changes.md` *Rule changes* asks since 0.37.1 (read, the `### Process changes` of the `v0.37.1` release, `gh release view`). |
| G2. `skills/code-review/scripts/pr_body.py#_composed` (`:766`, read) | The body's part below the line `HEADING` holds is built in one place. `_changed` (`:634`) gives the changelog's blocks first (`:783`), and every block is appended after `FOLD` and `SUMMARY` (`:793`). The first part above `HEADING` is `first_part`'s files (`:429`), and `split` (`:850`) cuts the body at `HEADING`. So moving the changelog's blocks from after `:793` to before it changes where the fragment stands and nothing else: the refusals of a copied line read `below` whole, wherever a line stands in it. |
| G3. `skills/code-review/scripts/chain_check.py#body` (`:1793`, read) | The pull request check's body arm holds no layout of its own. It calls `pr_body.py#compared` (`:1818`), the function `seal pr-body --check` calls. The arm's entry in the module docstring (`:77-90`) names the first part, the heading, the mark and "the records' copy", which stays true. So `chain_check.py` is not edited, though #1478 *Files* names it. |
| G4. #1478's counts, opened (executed) | `git grep -c -E '^- "' v0.37.0 -- 'seal/threads/*/pr.md'` gives 8, 9, 9 and 8 quotes, and `git grep -c changelog.md` on the same files gives 8, 9, 8 and 7. The four findings stand at `v0.37.0`: `1794200905…/trail/rounds/round-1.md:146`, `1794200906…/trail/rounds/round-1.md:15` and `:237`, and `1794200907…/trail/rounds/round-1.md:32`, each `location:` line naming a `changelog.md` line and a `pr.md` line. `1794200906…/guarantee.md:39` withholds on "changelog.md:4 and :10 (quoted at pr.md:8)". #1478 has no comment (executed, `gh issue view 1478 --json comments`). |
| G5. `docs/running/the-run.md` *The run* (read, `:36-47`) | A default taken with nobody to ask is written as one row of `frame/questions.md`, and the orchestrator "quotes that row in the work item's `pr.md` … where the owner can overturn it". The fold carries every table line of `frame/questions.md` (`pr_body.py#_questions`), so that policy has `pr.md` quote a record the fold carries. #1478 *Change* says `pr.md` keeps "quotations of records the fold does not carry". Policy outranks the ticket, so this design reads that phrase as the rule *Scope* item 3 states: `pr.md` quotes no sentence of `changelog.md`, and keeps quoting any other record. That reading meets #1478 *Done when* bullet 1 as written. |
| G6. `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/* (read, `:155`) | A record does not restate another record's fact. `pr.md` and `pr.<lang>.md` are "the one exception, because the pull request's reader meets them before the fold". Once `seal pr-body` writes the changelog fragment before the fold, the reader meets it there with no copy, and the exception's ground no longer covers a quote of `changelog.md`. |
| G7. `docs/forms/the-guarantee.md` *The guarantee* (read, `:22`) and `agents/sealer.md` step 2 (read, `:69-87`) | `HEADING` divides the orchestrator's account from the records' own text: the sealer reads the part below it "as no party" and compares the part above it with the other parties. The changelog fragment is a record's text. So it stands below `HEADING`, and the part above it stays `pr.<lang>.md` and `pr.md` alone. `frame/plan.md` *Alternatives considered* rows A to C weigh the placements. |
| G8. #1453 *Done when* bullet 2 (executed, `gh issue view 1453`) and its design at `v0.36.0:seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md` *Scope* (read) | "A repository can keep its records in one language and give the people reviewing the pull request a body in another." Its design rejected a body in the records' language because "the team could then read nothing of the body". With the changelog out of `pr.md`, a `pr.<lang>.md` that renders `pr.md`'s quotes alone would give the team nothing of what changed in its language. So `pr.<lang>.md` renders the sentence that opens each list item of `changelog.md` itself (*Scope* item 4). `frame/plan.md` *Alternatives considered* rows F to H weigh the three shapes. |
| G9. `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A thing is re-checked only when the diff or CI shows it changed", and "a change rewrites the text it amends in place, and in the same commit removes what stood on the old fact: … a copy". The paragraph #1478 *Change* says goes (`skills/code-review/orchestration.md:435-445`) holds these. Its closing sentences have the orchestrator open every quote's source before each spawn of the sealer, whatever the diff changed; that step goes. Its first sentence has the orchestrator rewrite a quote whose source a fix changed, which is the core's in-place rule given to the one party that writes `pr.md`; it stays, as one sentence. Its second sentence says who repairs a finding located in `pr.md` and how the close block reads; no other file states that, and it stays. `frame/plan.md` *Alternatives considered* row I weighs removing the paragraph whole. |
| G10. `refactor/1477-implement-orchestration-grew-back` at `10fc3a7f7` (executed, `git show <branch>:skills/implement/orchestration.md`, piped to `wc -w` and to `grep -n`) | #1477's body holds 5,233 words against its bound of 5,242 (`frame/design.md` S1 on that branch). Its steps 2 and 3 at `:35-50` are the base's `:38-53` unchanged (executed, `diff` of the two ranges prints nothing), as #1477's frame says it leaves them. Every clause of that step stays true under this design: `pr.md` is still the body's first part, written once the last phase has closed and before the first round, and `seal pr-body` still writes the body from `pr.md` and the records. The step already ends by citing the owner. So this work does not edit `skills/implement/orchestration.md` (*Scope*, out). |
| G11. Which copy composes and which copy checks (read: `bin/seal`, `.github/workflows/hygiene.yml:116`, `templates/setup/hygiene.yml:1-24`; `v0.36.0:seal/threads/1794187229-the-body-carries-the-seal-mark/frame/plan.md` *Alternatives considered* row K and *Operational impact*) | `seal` on the session's `PATH` is the installed plugin's, 0.37.1 here. This repository's `hygiene.yml` runs the tree's `chain_check.py`, and a user's repository runs the tag its workflow pins. Two copies of different releases compose the changelog in different places, so the body arm refuses the body at those lines. #1452 met the same class and kept one composition per release. `frame/plan.md` *Operational impact* states what this repository and a user's repository do. |
| G12. `seal/follow-up.md` (read) and `seal/` (executed, `ls seal`) | Both tables of `seal/follow-up.md` are empty, so no row waits on this work. No `seal/parity.json` stands, so no original is read. |
| G13. Milestone 103 (executed, `gh api repos/MichaelYcJo/AgenticSeal/milestones/103`) | "Then #1478 after #1476, because both edit `skills/code-review/orchestration.md` and `agents/proofer.md`." The branch is cut from `1959c3ea1`, which holds #1476. #1476 carried the release's version move, so this work moves no version. |
| G14. The operations of `## Rule changes` below, read by their reader (executed: `skills/settle/scripts/rule_changes.py#parse` over this file, from a `git clone --no-local` under the scratchpad, since removed; then a whitespace-collapsed count of each `from` in its document) | `parse` returns the operations with no error and no line named as not read, and each `from` stands once in the document its `file:` names at `53cab03ea`. |

## Scope

In scope:

1. **`seal pr-body` writes the changelog fragment above the fold.** `skills/code-review/scripts/pr_body.py#_composed` places the blocks `_changed` gives after the seal mark and before `FOLD`, as *Data & interfaces* D1 lays the body out. The fold holds the other sections in their present order. The first part, `HEADING`, the mark's place as the first line under `HEADING`, `split`, `compared`, `_check`, each refusal of a copied line and every exit code keep their behaviour. The module docstring and `main`'s parser description are rewritten where they say the copy stands in one fold or list the changelog among the fold's sections.
2. **Cases for item 1, each new one seen red before it is planted.** In `tests/skills/test_pr_body.py`: the written body holds the changelog's section between `HEADING` and `FOLD` and no line of it inside the fold; where `changelog.md` is absent, the line naming it absent stands there too; `--check` refuses, at the body's lines, a body that holds the changelog's section inside the fold, as 0.37.1 composed it. The cases that refuse a changelog line (`HEADING`, a `details` tag, a closing keyword, an unclosed `<!--`) stay green at the record's line. Every fixture that holds a whole body as a literal, in that module and in the modules `frame/plan.md` *Phases* row 1 names, takes the new layout. The `scaffold.sh` of each sealer case under `evals/behaviour/sealer/` holds a body `pr_body.compose` wrote (read, `evals/scripts/rule_cases.py:973-976`; executed, `grep -l '## What changed'` over the scaffolds), so each is written again from `evals/scripts/rule_cases.py` and none is edited by hand.
3. **`skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* owns the rule for `pr.md`, and states that `pr.md` quotes no sentence of `changelog.md`.** The paragraph opening **The pull request body's first part is the work item's `pr.md`** keeps what it holds and gains the rule with its ground: `seal pr-body` writes the fragment whole under the line `HEADING` holds, above the fold, so the reader meets it there and a fix to a changelog sentence touches no `pr.md`. The paragraph opening **You write the pull request body after `trail/gate.md` is committed** names the fragment between the heading line and the fold. D2 gives the clauses.
4. **The same section restates what `pr.<lang>.md` holds.** The paragraph opening **Where `config.json`'s `Commit and pull request language` and `Record language` keys name different languages** says the file holds, rendered in `Commit and pull request language` and each followed by its coordinate: first the sentence that opens each list item of the `changelog.md` fragment, in the fragment's order; then each quote of `pr.md`, in `pr.md`'s order, with the coordinate it carries there. It holds nothing else: it renders no other sentence of the fragment, which stands whole in the records' language under the line `HEADING` holds, above the fold. The rest of the paragraph stays.
5. **The paragraph opening Where a fix pass or a fold changes a sentence that `pr.md` quotes shrinks to two sentences.** The first covers a rendering beside a quote: where a fix pass or a fold changes a sentence `pr.md` quotes or `pr.<lang>.md` renders, the orchestrator rewrites the quote or the rendering and commits it before it spawns the next round. The second is today's sentence on a round finding located in `pr.md` or `pr.<lang>.md`, word for word. The sentences on opening each quote's source before each spawn of the sealer go (*Removes*).
6. **`agents/proofer.md` and `agents/sealer.md` read `pr.<lang>.md` as item 4 states it.** In `agents/proofer.md`, the rule **Every round reads the work item's records that state the present, whole, against its target** names as a finding a line of `pr.<lang>.md` that does not render, in `Commit and pull request language`, the sentence at the coordinate it carries, a list item of `changelog.md` whose opening sentence it leaves without a rendering, and a quote of `pr.md` it leaves without a rendering. In `agents/sealer.md` step 2, the clause "the quotes rendered in the commit language where the keys differ" becomes the file's renderings in the commit language. Neither file gains a statement of what `pr.md` holds.
7. **Each other file of the plugin that states what `pr.md` or `pr.<lang>.md` holds cites the owner, and each sentence the new facts make false is rewritten.** D3 lists the files and what each loses or rewords. `tests/text/test_the_rules_have_one_owner.py#RULES` gains one row: the owner, the sentence of item 3 it states, and each linking carrier of D3 with the sentence that names the owner.
8. **The work item's `changelog.md`**, written by the last phase's crafter: what changed for a user, an `Updating:` paragraph from `frame/plan.md` *Operational impact*, and `### Process changes` with one row for each of items 3, 4, 5 and 6.

Out, each with its ground:

- **`skills/implement/orchestration.md`.** G10: no clause of step 2 becomes false, the step cites the owner already, and #1477's body has nine words of headroom. `git diff --stat origin/release/v0.37.2...HEAD -- skills/implement/orchestration.md` prints nothing at the end of the build (S7).
- **`skills/code-review/scripts/chain_check.py`.** G3.
- **Every file under `docs/`.** G1: `## Rule changes` carries them to the settle.
- **A copy of part of the changelog, such as each item's bold opening alone.** `pr_body.py` copies lines and composes none (its docstring, `:9-18`), and choosing lines by their emphasis is a grammar of spellings. `frame/plan.md` *Alternatives considered* row D.
- **A second composition the check accepts, for a body an earlier release wrote.** G11, and `frame/plan.md` *Alternatives considered* row K.
- **A check that refuses a `pr.md` line citing `changelog.md`.** Whether a line quotes the changelog is read from words. The cost of the rule not being kept is the cost the tree pays today.
- **Moving any other section of the copy above the fold.** #1478 asks for the changelog alone, and G5 keeps the quote as the way a row of another record reaches the reader before the fold.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The changelog stands above the fold | Given a work item holding `changelog.md`, `pr.md` and its other records. When `seal pr-body <item> --body <file>` writes the body. Then the lines D1 gives stand between the line `HEADING` holds and `<details>`, and the fold holds no line of `changelog.md` and no `## What changed`. | The layout case of `tests/skills/test_pr_body.py`, seen red against `_composed` as it stands. |
| S2. An absent changelog is named above the fold | Given a work item with no `changelog.md`. When the body is written. Then `## What changed` and the line naming `changelog.md` absent stand between `HEADING` and `<details>`. | A case of the same module, seen red the same way. |
| S3. A refused changelog line is still refused at its record | Given a `changelog.md` holding a line equal to `HEADING`, a `details` tag outside a code span, a closing keyword or an unclosed `<!--` at a line's start. When the body is written. Then exit 1 with the cause at `changelog.md`'s line, and nothing is written. | The existing refusal cases of the module stay green with no change to what they assert. |
| S4. A body an earlier release composed is refused by line | Given a body file holding the changelog's section inside the fold, as 0.37.1 writes it. When `seal pr-body <item> --body <file> --check` runs. Then exit 1, each `refused:` line naming the body file and a line. When `seal pr-body` writes the file again, `--check` exits 0. | A new case of the module, seen red against `_composed` as it stands, where that body matches. |
| S5. The pull request check reads the same layout | Given a ready pull request whose body `seal pr-body` wrote at HEAD. When `chain_check.py` runs with that body in its payload. Then the body arm refuses nothing. Given the body of S4, it refuses at the body's lines. | The body-arm cases of `tests/skills/test_chain_check.py`, green with fixtures in the new layout. The second half rests on `pr_body.py#compared`, which the arm calls (G3): `tests/skills/test_pr_body.py` `Test_main::test_refuses_the_changelog_inside_the_fold_until_written_again` drives the S4 body through it, and `Test_body::test_refuses_a_drifted_body_at_its_line` of `tests/skills/test_chain_check.py` holds the arm's refusal at the body's line, so no case of the arm holds a whole stale body (`trail/phases/phase-1.md`). |
| S6. A fix to a changelog sentence touches no `pr.md` | Given the owner section after the build. When it is read. Then it says `pr.md` quotes no sentence of `changelog.md`, with the ground of *Scope* item 3. Given this work item's own `pr.md`. Then no line of it carries a `changelog.md` coordinate. | The new row of `tests/text/test_the_rules_have_one_owner.py#RULES` holds the owner's sentence; the proofer reads `pr.md` at each round. |
| S7. One file states the rule | Given the files of D3 after the build. When each is read. Then none says which records `pr.md` quotes or what `pr.<lang>.md` renders, and each that kept a sentence on what the two files hold names the owner's file and section in one sentence; `README.md`, `README.ko.md`, `seal/README.md`, `templates/setup/seal-README.md` and `pr_body.py` state none after the rewording and add no citation. `skills/implement/orchestration.md` is unchanged against the base. | The same `RULES` row, one link per carrier; `git diff --stat origin/release/v0.37.2...HEAD -- skills/implement/orchestration.md`, run by the last phase's crafter and by the proofer. |
| S8. `pr.<lang>.md` is restated for the new shape | Given the owner section, `agents/proofer.md` and `agents/sealer.md` after the build. When each is read. Then the owner states *Scope* item 4, the proofer names the findings of item 6, and no shipped text outside `docs/` says `pr.<lang>.md` holds "the quotes of `pr.md`" alone. | `git grep -n -E 'quotes? of .pr\.md.'` outside `docs/`, `tests/` and `seal/threads/`, each hit read by the crafter and by the proofer; this lists one spelling of an open class, so it is a sample and D3's list is the method. |

## Data & interfaces

**D1. The body `seal pr-body` writes.** Each line is fixed, or copied from the file named. A blank line follows each block, as it does today.

```
<pr.<lang>.md, first where the two language keys differ, after pr.md where they name one language>
<pr.md>
## From the records

<the seal mark, where pr_body.py#seal_mark gives one>

## What changed

From `changelog.md`.

<the lines of changelog.md, blank lines at either end dropped>

<details>
<summary>Copied from the records in <root>/threads/<name>/ by seal pr-body.</summary>

## How it was built
…
## Review rounds
…
## Broad gate
…
## Not verified
…
## Not done
…
## Questions
…

</details>
```

Where `changelog.md` is absent, the two lines under `## What changed` are replaced by `` `changelog.md` is not in this work item. ``, as `pr_body.py#ABSENT` formats it today. No constant of `FIXED` is added or renamed.

**D2. The owner's clauses**, in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*. The crafter writes the sentences; these are what they say.

| Paragraph, by its bold opening | Keeps | Gains or loses |
|---|---|---|
| **The pull request body's first part is the work item's `pr.md`** | every sentence it holds at `:396-420` | gains, after the sentence listing what `pr.md` holds: `pr.md` quotes no sentence of `changelog.md`, because `seal pr-body` writes the fragment whole under the line `skills/code-review/scripts/pr_body.py#HEADING` holds, above the fold, so a fix to a changelog sentence touches no `pr.md` |
| **Where `config.json`'s `Commit and pull request language` and `Record language` keys name different languages** | when the file is written and committed, what `<lang>` is, where `seal pr-body` writes it, that every round reads it, and the last sentence | the sentence on what it holds becomes *Scope* item 4; "no `Closes`, `Part of` or attribution line … and no sentence of the orchestrator's own" stays |
| **Where a fix pass or a fold changes a sentence that `pr.md` quotes** | the sentence on a round finding located in `pr.md` or `pr.<lang>.md`, word for word | the opening sentence covers a rendering as *Scope* item 5 words it; loses the sentences from "Before each spawn of the sealer" to the paragraph's end |
| **You write the pull request body after `trail/gate.md` is committed** | every other sentence | "then the records' copy" becomes: then the changelog fragment, then the rest of the records' copy in one fold |

**D3. The other files that state the rule**, listed by `git grep -n -E 'pr\.md|pr\.<lang>'` outside `tests/`, `evals/`, `seal/threads/` and `docs/`, each hit read. A file the list names and this table does not is one whose sentences name `pr.md` and state nothing the new facts change, as the command lists them at `e4b9b6f99`, after #1477's merge: `skills/implement/orchestration.md`, `skills/implement/routing-question.md`, `skills/implement/scripts/seal.py`, `skills/code-review/scripts/chain_check.py`, `lib/optin.py` and `templates/records/sdd-plan.md`.

| File and place | What it does |
|---|---|
| `skills/commit-pr-convention/SKILL.md` *Pull request bodies* | Keeps which language each kind of line is in. The sentence "`pr.md` holds the `Closes` and `Part of` lines, quotes of the records, each with its coordinate, and the attribution line" becomes one citation of the owner for what `pr.md` and `pr.<lang>.md` hold. "then the second part under that line from the work item's other records, inside one `<details>` fold" names the changelog fragment before the fold. In the paragraph on the mirror, "the quotes of `pr.md` in the commit language, each with its coordinate, in the shape … gives it" becomes: written in the commit language, in the shape `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* gives it, cited by its path and heading, since that file never calls the section the owner. |
| `skills/implement/SKILL.md` *3. The SDD file set*, the `pr.md` row | The Holds cell keeps "the pull request body's first part, after `pr.<lang>.md` where `config.json`'s two language keys differ, which `seal pr-body` writes above the records' copy" and cites the owner, which the Starts from cell already names, for what the two files hold. The When cell loses "both rewritten where a fix pass or a fold changes a sentence it quotes", which the owner states. |
| `skills/writing-style/outside-the-review.md`, the paragraph opening **리뷰 체인을 거친 작업 항목의 PR 본문은 두 부분이고** | The two sentences on what `pr.md` and `pr.<lang>.md` hold become one citation of the owner, and the paragraph's later citation of the same section goes, so the section is cited once; the owner states that `pr.<lang>.md` is committed with `pr.md` before the first round. "`<details>` 하나로 접혀 있다" says the changelog fragment stands open above the fold and the rest is folded. Written in Korean, as the file is. |
| `templates/setup/config.md` *What no key governs*, the paragraph opening "Where the two language keys name different languages" | "holding each quote of `pr.md` rendered in `Commit and pull request language`" becomes: written in `Commit and pull request language`, and a separate sentence cites `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* by path and heading. |
| `templates/setup/seal-README.md` and `seal/README.md`, the tree's `pr.<lang>.md` line | "pr.md's quotes in the commit language, opening the first part where the two language keys differ" becomes: the first part's opening in the commit language, where the two language keys differ. The two files stay identical. |
| `README.md` and `README.ko.md`, the paragraph on the sealer | "the body opens with `pr.<lang>.md`, the quotes of `pr.md` in the pull request language" becomes: the body opens with `pr.<lang>.md`, written in the pull request language. The Korean edition says the same. |
| `skills/code-review/scripts/pr_body.py`, the module docstring | *Scope* item 1 owns it; "the quotes of `pr.md` rendered in the commit language" at `:40-41` becomes the file's renderings in the commit language. |

## Rule changes

- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: **The pull request body opens with the orchestrator's part, the work item's `pr.md`, and the records' copy follows it in one fold; the sealer reads only the orchestrator's part.**
  to: **The pull request body opens with the orchestrator's part, the work item's `pr.md`, and the records' copy follows it, the changelog fragment first and the rest in one fold; the sealer reads only the orchestrator's part.**
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: Below that line it writes the copy of the work item's records inside one `<details>` block whose `<summary>` names the copy and is followed by a blank line, with nothing inside it folded again.
  to: Below that line it writes the copy of the work item's records: the changelog fragment first, whole and outside any fold, and then the rest inside one `<details>` block whose `<summary>` names the copy and is followed by a blank line, with nothing inside it folded again.
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: `pr.md` holds the `Closes` lines, in the pull request's language, and quotes of the records, in the records' language, each with its coordinate, and no sentence of the orchestrator's own account; `pr.<lang>.md` holds those quotes rendered in the pull request's language, each with the same coordinate, and nothing else. The orchestrator commits them before the first round, so every round reads them (`skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*).
  to: What `pr.md` and `pr.<lang>.md` hold is stated in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, and neither holds a sentence of the orchestrator's own account. The orchestrator commits them before the first round, so every round reads them.
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: each quote of `pr.md` rendered in `Commit and pull request language`, with its coordinate, where that key and `Record language` name different languages
  to: the body's opening in `Commit and pull request language`, where that key and `Record language` name different languages
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: `pr.md` holds the `Closes` lines and quotes of the other records, each standing word for word at the coordinate it names, `pr.<lang>.md` holds those quotes rendered in the pull request's language, and neither holds a fact of its own.
  to: what each holds is stated in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, and neither holds a fact of its own. `changelog.md` is no part of the exception, because `seal pr-body` writes it before the fold whole.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: pull request body opens with `pr.<lang>.md`, the quotes of `pr.md` rendered in
    the team's language, and `pr.md` follows it
  to: pull request body opens with `pr.<lang>.md`, written in the team's
    language, and `pr.md` follows it
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: 본문은 `pr.md` 의 인용을 팀의 언어로 옮긴 `pr.<lang>.md` 로 시작하고, 그 뒤에
    `pr.md` 가 옵니다.
  to: 본문은 팀의 언어로 쓴 `pr.<lang>.md` 로 시작하고, 그 뒤에 `pr.md` 가
    옵니다.
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: whether `pr.<lang>.md` renders `pr.md`: the rounds and the sealer
  to: whether each line of `pr.<lang>.md` renders the sentence at its coordinate: the rounds and the sealer

## Removes

This work adds one mechanism, the row of `tests/text/test_the_rules_have_one_owner.py#RULES` (*Scope* item 7). In return it takes out the step of row 2 below and the copies of rows 1 and 4.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The quotes of `changelog.md` in a work item's `pr.md`, and their renderings by way of `pr.md` in `pr.<lang>.md` | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the paragraph opening **The pull request body's first part is the work item's `pr.md`** | `seal pr-body` writes the fragment whole above the fold (*Scope* item 1). Its record: the findings and the withheld verdict of G4, each a changelog sentence named a second time at its copy. |
| The orchestrator's step before each spawn of the sealer: opening each quote's source at HEAD, finding the quote there verbatim, and rewriting one it does not find | the same section, the sentences from "Before each spawn of the sealer" to the end of the paragraph opening **Where a fix pass or a fold changes a sentence that `pr.md` quotes** | It can go. It re-reads every quote whatever the diff changed (G9). A round reads `pr.md` whole against its target and names a quote it does not find (`agents/proofer.md`, **Every round reads the work item's records that state the present, whole, against its target**), and the sealer reads the first part against the records (`agents/sealer.md` steps 2 and 4). The step's one recorded miss is the quote at `pr.md:8` of G4, which the sealer caught. |
| The changelog's section inside the fold | `skills/code-review/scripts/pr_body.py#_composed` | The same blocks, between the mark and `FOLD` (D1). |
| The statements of what `pr.md` and `pr.<lang>.md` hold outside the owner | each place D3 names, and each `from` of `## Rule changes` | The owner, `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, which each cites. |

Framed 2026-11-10 by framer, before the build.
