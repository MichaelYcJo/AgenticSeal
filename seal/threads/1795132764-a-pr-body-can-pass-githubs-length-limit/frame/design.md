# Design: a pull request body past GitHub's length limit folds its longest parts

## Grounding

The tree as read at `e685d989b`.

| Policy clause | What it fixes for this work |
|---|---|
| **G1** Issue #1559, its body as folded and its one comment (read: the body saved by the orchestrator with `gh issue view 1559 --json body --jq .body` on 2026-11-20; executed: `gh issue view 1559 --json comments,milestone`, one comment, milestone `release: 0.38.3`) | The request and the owner's decision in its *Decision*: past the limit, `compose` replaces whole parts with a fixed line naming the record's file, from the longest down, until the body fits; `## What changed` stays whatever its length; `compared` composes the same way. Its *Done when* is this design's acceptance. The comment records the fold of that decision and the milestone, and changes nothing the body asks. |
| **G2** `skills/code-review/scripts/pr_body.py#_composed`, `#compose`, `#compared` and `#main` (read: lines 776-858, 976-996, 1014-1084); the module docstring's *Limits* list, lines 79-80 (read) | Nothing reads the length of what is composed or compared, and the docstring says so: "GitHub refuses a pull request body over its length limit, and `gh pr create` prints the refusal; nothing here repeats it." The cause is shown by a probe (executed: `test_tmp_body_length.py` in a `git clone --no-local` of `e685d989b` under the scratch directory composed a body of 115,689 characters for a synthetic work item, and `compared` returned no cause and no note for that body). |
| **G3** `skills/code-review/scripts/chain_check.py#body` (read: lines 1815-1857) | The body arm composes nothing itself. It calls `pr_body.py#compared` and prints its `note` as one notice and its causes as problems. A fold that `compared` makes reaches the arm with no change to the arm's code. |
| **G4** `docs/forms/the-guarantee.md` *The guarantee*, the paragraph opening **A pull request body carries the seal mark only where the repository turns it on** (read) | "The orchestrator runs `seal pr-body` once more after it commits a `sealed` guarantee, and that run changes no copied line." A fold decided by the body's length would break this where the mark's line alone pushes the body past the limit. The fold therefore leaves room for the mark's line whether or not the mark is written (*Data & interfaces* D4). |
| **G5** `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* (read); `tests/skills/test_chain_check.py#Test_body.test_accepts_the_body_at_a_merge_past_a_later_base_commit` (read) | The check reads the body against what `seal pr-body` composes at HEAD, and CI checks out the pull request's merge commit, whose HEAD is not the branch head. A fold line that named a commit would differ between the branch head and the merge commit, so the fold line names the record's path alone (*Alternatives considered*, row 3 of `frame/plan.md`). |
| **G6** `docs/running/what-a-script-gates.md` *The checks*, the row of `seal pr-body` and `seal pr-body --check` (read) | Its *Reads* cell lists what the command reads. The length of the composed body against GitHub's limit becomes one more such fact, so the cell changes (*Rule changes*). |
| **G7** GitHub's unit of the limit (read: `https://github.com/dead-claudia/github-limits`, which lists a pull request body's maximum as "65536 codepoints", measured by `PATCH` requests to the pulls endpoint; the error text `Body is too long (maximum is 65536 characters)` in #1559's report) | The one source says the limit counts Unicode code points. It is a community measurement and not GitHub's documentation, and no probe here can settle it, because a probe posts a body to GitHub, so `frame/questions.md` Q1 holds it as a measurement. The body is measured in UTF-16 code units (D1). That count is never smaller than the code-point count, so a body within it also fits where GitHub counts code points. |
| **G8** `.github/scripts/label_merged_on_release_branch.py:96-112` (read) | The tree's one other number of GitHub's own, the label description's 100 characters, stands as a named constant in the script that sends the text, with a comment saying the number is GitHub's and what raising it would do. `LIMIT` follows that form. |
| **G9** `tests/skills/test_pr_body.py#unsourced` (read: lines 299-319) | The case that holds "every line is a record's or a fixed line" fills each line of `pr_body.py#FIXED` with `home`, `name` and `path` and nothing else. A new fixed line therefore takes `{path}` at most, and spells the limit's number into its text when it is defined. |
| **G10** The callers of `compose` and `compared` (executed: `git grep -n '\.compared(\|compared(\|_composed(\|\.compose(' -- . ':!seal/threads'`) | `compared` is called by `chain_check.py:1840` and `pr_body.py:1044`. `compose` is called by `tests/skills/test_chain_check.py:3182` (`composed_body`), `evals/scripts/rule_cases.py:973` and the cases of `tests/skills/test_pr_body.py`. Each of the first two adds the first part in front of what `compose` returns, so `compose` learns of the first part through a new argument. |
| **G11** Nothing in the tree already guards a body's length or shortens one (executed: `git grep -n -i 'truncat\|maximum is\|len(body)\|len(text) >' -- '*.py' ':!seal/threads'`) | The matches are the label constant of G8, a dry-run print in `.github/scripts/publish_release_note.py:926`, an eval fixture, comments and an unrelated test helper. No unit can be extended to hold this fold, so it is new code in `pr_body.py`. |
| **G12** `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read); `seal/config.json` (read: no `Policy root` key, so the policy root is `docs/`) | The subject of this work item is the code, so the rules it changes in `docs/` stand in `## Rule changes` for the settle. `skills/` and `pr_body.py`'s docstring are edited in the pull request. |
| **G13** `seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/` and commit `8f99b773e` (#1509) (read) | The changelog fragment stands above the fold, outside the `<details>` block, whole. That decision is not argued again: the fold here acts on the sections inside the `<details>` block and never on the fragment, as the owner decided (G1). |
| **G14** `seal/follow-up.md` (read: both tables are empty) | No follow-up item waits on this work. |
| **G15** The seal mark's line (executed: the same probe printed `len(pr_body._mark_line(pr_body.MANIFEST)[0])` as 112) | The room D4 reserves is that line and the blank line under it, read from the plugin's manifest as `seal_mark` reads it. |
| **G16** Issue #1557's branch `origin/docs/1557-the-process-has-no-name` at `e6d1945a0` (executed: `comm -12` of its `git diff --name-only origin/release/v0.38.3...` list against the files this design changes printed nothing; `git grep -n 'efficient development\|through the workflow'` over those files exited 1) | The two work items change no common file, and none of this work's files cites the core heading #1557 renames. `frame/plan.md` *Overlap with the release* states the merge order. |

## Scope

In:

1. **The fold in `skills/code-review/scripts/pr_body.py`.** `_unfolded` builds each section after `## What changed` as its own unit, `SECTIONS` pairing each section's builder with its fold paths, and `_folded` lays them out. Where the whole body would pass `LIMIT`, counted as D1 states with D4's room for the seal mark's line, `_folded` folds those sections one at a time, the longest first, until the body fits (*Data & interfaces* D1 to D4). `compose` and `compared` both compose through it, so `seal pr-body`, `seal pr-body --check` and the chain check's body arm read one body.
2. **The refusal where folding cannot fit the body.** Where the body still passes `LIMIT` with every foldable section folded, `seal pr-body` refuses on the work item's directory and writes nothing, and `compared` returns that cause (D5).
3. **Saying which sections were folded.** `seal pr-body`, in both forms, prints one line naming the folded sections, and `compared`'s note carries the same sentence, which the body arm prints as a notice (D6).
4. **The callers of `compose`** listed in G10 pass the first part, so a caller that puts the first part in front of `compose`'s text composes the body `main` writes.
5. **The module docstring** of `pr_body.py` states the fold where it describes the body, and the *Limits* bullet about the length leaves (`## Removes`).
6. **The cases** in `tests/skills/test_pr_body.py` and `tests/skills/test_chain_check.py` that *User scenarios & acceptance* names, each seen red as contract rule 15 asks.

Out, each with its reason:

- **A fold of a part smaller than a section, such as one round record.** The owner's decision folds whole parts, and the issue's measured table names sections. `frame/plan.md` *Alternatives considered* row 2 holds the grounds.
- **`## What changed`.** It stays on the page whatever its length (G1).
- **The part above `HEADING`, `pr.md` and `pr.<lang>.md`.** They are the orchestrator's files, copied as their bytes stand. Their length counts toward the limit, and a body they push past it is refused (Scope item 2), never shortened.
- **`chain_check.py#body`'s code.** It needs no change (G3).
- **A new sentence in `skills/code-review/orchestration.md` or `agents/sealer.md`.** Their sentences act on `seal pr-body`'s exit code and its `refused:` lines, and the refusal of Scope item 2 names its own repair in its text. A new sentence there would restate it in a file every spawn of those parties pays for. The one sentence of `skills/code-review/orchestration.md` that lists what a `refused:` line names is amended in place to name the work item's directory, because the refusal made that list incomplete (round 1, finding 3).
- **The release note's length.** `.github/scripts/publish_release_note.py` sends another surface with another limit, and nothing in #1559 reports it past that limit.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given records whose composed body passes `LIMIT`, when `compose` runs, then the body measures at most `LIMIT` in D1's count, each folded section is its heading followed by its fold lines, `## What changed` stands whole above the fold, and every line is a record's or a line of `FIXED` | A new case of `tests/skills/test_pr_body.py#Test_compose` asserts the length, the folded headings and `unsourced(...) == []`. Seen red against `_composed` at `e685d989b`, where the length passes `LIMIT` |
| S2 | Given two sections each long enough that folding either one fits the body, when `compose` runs, then only the longer one is folded and the other is copied whole | A new case of `Test_compose` with two long sections of different lengths. Seen red with the sort by length removed, so that the sections fold in body order |
| S3 | Given records whose body is within `LIMIT`, when `compose` runs, then nothing is folded and the text is the one composed at `e685d989b` | `Test_compose.test_accepts_a_work_item_as_the_records_text`, which pins `EXPECTED`, stays green unchanged |
| S4 | Given a body that fits without the mark's line and passes `LIMIT` with it, when the body is composed before the seal and again after it, then the two differ on the mark's line and its blank line alone | A new case of `tests/skills/test_pr_body.py` composes with no mark and with the mark over the same records and compares the two outputs. Seen red with the reserve of D4 removed |
| S5 | Given `changelog.md` and `pr.md` that pass `LIMIT` together, when `seal pr-body` runs, then it exits 1, prints one `refused:` line on the work item's directory naming the two files and their lengths, and writes nothing | A new case of `tests/skills/test_pr_body.py#Test_main`, asserting the exit code, the line and that the body file is not written. Seen red against `main` at `e685d989b`, which exits 0 |
| S6 | Given a body folded by S1's rule, when `seal pr-body` writes it and `seal pr-body --check` reads it, then the write prints the line naming the folded sections, the check exits 0 and prints the same line, and a body in which one folded section's text is copied back is refused at its line | A new case of `Test_main` over the written file and over an edited copy of it |
| S7 | Given a ready pull request whose body is the folded composition, when the chain check's body arm reads it, then it refuses nothing and prints the fold's notice; given the body composed without the fold, the arm refuses it | A new case of `tests/skills/test_chain_check.py#Test_body`. Seen red against `compared` at `e685d989b`, where the folded body is refused at the first folded section |
| S8 | Given a copied line `pr_body.py` refuses at `e685d989b`, such as one holding a `<details>` tag, inside a section that the fold removes, when `compose` runs, then the line is still refused | A new case of `Test_compose`. Seen red with the refusal loop run over the folded lines only |
| S9 | Given the build, when the docstring's *Limits* list is read, then it no longer holds the bullet saying the length is not guarded | `git grep -n "nothing here repeats it" -- skills/code-review/scripts/pr_body.py` prints nothing. At `e685d989b` it prints `skills/code-review/scripts/pr_body.py:80` alone (executed), the bullet `## Removes` names. The pathspec names one file outside `seal/threads/`, so this work item's records, which quote the bullet, are not searched |
| S10 | Given records whose body is within `LIMIT` counted in code points and past it counted in UTF-16 code units, because their lines hold characters outside the Basic Multilingual Plane, when `compose` runs, then a section is folded | A new case of `Test_compose`. Seen red with the count of D1 replaced by `len` |

## Data & interfaces

- **D1, the limit and its count.** `LIMIT = 65536` stands beside `HEADING` in `pr_body.py`, with a comment in the form G8 gives: the number is GitHub's, and raising it does not make a longer body reach a pull request. Every length the fold compares with `LIMIT` is counted in UTF-16 code units, `len(text.encode("utf-16-le")) // 2`, by one function that the fold, the section lengths of D2 and the refusal of D5 all call. A character outside the Basic Multilingual Plane, such as the 🤖 of an attribution line, counts as two, and every other character as one. That count is never smaller than the code-point count GitHub is reported to use (G7), so a body within it fits under either unit, and its comment says so. The length compared with `LIMIT` is that count of the whole body as `main` writes it: the first part's files as their bytes stand, `HEADING` and its line end, and `_joined(below)`.
- **D2, a section and its fold.** The sections that can fold are the six after `## What changed`, in body order: `## How it was built`, `## Review rounds`, `## Broad gate`, `## Not verified`, `## Not done` and `## Questions`. A section's length is D1's count of its laid lines in the body, its blank line included. A folded section keeps its heading, and its other lines become one fold line per path listed here, in this order. A directory is named once, as the directory, and never as each record in it, so a folded section holds the fold lines listed here whatever records the work item has, and its length does not grow with the number of phases or rounds:
  - `## How it was built`: `frame/plan.md`, then `trail/phases/`
  - `## Review rounds`: `trail/rounds/`
  - `## Broad gate`: `trail/gate.md`
  - `## Not verified` and `## Not done`: `gaps.md`
  - `## Questions`: `frame/questions.md`

  The fold line is a new member of `FIXED`, `FOLDED`, which takes `{path}` and no other field (G9) and names the limit in its text, ``Not copied here, so the body stays within GitHub's 65,536 characters: `{path}` holds what this section copies.``, since `frame/plan.md` holds more than `## How it was built` copies from it It names no commit (G5). The paths are the work item's, as every other fixed line names them, and the summary line of the fold names the work item's directory.
- **D3, the order.** The fold takes the longest section first, and a tie goes to the earlier section in body order. After each fold the body's length is measured again, and the fold stops once it is within `LIMIT`. A section whose folded form would not be shorter than its copy is not folded. The sections stay in body order whatever was folded, inside the one `<details>` block, below the seal mark and the changelog's section.
- **D4, the mark's room.** The fold measures the body as if the seal mark's line and the blank line under it stood in it, whether or not `seal_mark` writes the mark. The room is the line `_mark_line` builds from the manifest `compared` is given or the plugin's own, `MANIFEST`, and it is nothing where that line cannot be built. So the sealer's `seal pr-body --check`, run before any verdict, and the run after a `sealed` guarantee fold the same sections (G4).
- **D5, the refusal.** Where the body passes `LIMIT` with every section of D2 folded or left as D3 leaves it, `_folded` raises `Refused` with one cause on the work item's directory, `("", 0, why)`. `why` gives the body's length, counted with D4's room for the seal mark's line whether or not the mark is written and saying so, `LIMIT`, and the length of the first part's files and of `changelog.md`, each file named and each length in D1's count, and says that the one file, or one of them where it names several, is shortened before `seal pr-body` runs again. The refusals of copied lines, which `_unfolded` raises, are raised first, over every section before any fold, so a line is refused whether or not its section is folded (S8), and the order in which `compared` meets a record's refusal and the language keys' refusal stays as it is.
- **D6, the report of the fold.** Where any section was folded, `seal pr-body` prints, before its `wrote:` or `matches:` line, one line opening `seal pr-body: ` that names the folded headings in body order and the limit. `compared` keeps its `(note, causes)` shape, and its `note` holds `seal_mark`'s sentence and this one, joined with `; ` where both stand, so `chain_check.py#body` prints the fold as a notice and refuses nothing for it.
- **D7, the arguments.** `compose` gains `parts`, the first part's files as `first_part` lists them, `(name, text)` pairs, empty where it is not given, and composes the body that the first part's text followed by `compose(...)` makes. The first part is a list and not one text because D5 names each of its files with its length. `_folded` takes the same `parts` and the mark's room, which `_room(mark, manifest)` gives. `main` and `compared` read the first part between `_unfolded` and `_folded`. The callers of G10 pass `parts`.

## Rule changes

- add
  file: docs/forms/the-guarantee.md
  section: The guarantee
  to: **Where the body `seal pr-body` composes, counted in UTF-16 code units
    with room for the seal mark's line, would pass GitHub's limit of 65,536
    characters, the sections of the records' copy after the
    changelog's are folded, the longest first, until the body fits.** A folded
    section keeps its heading, and a fixed line in place of its text names
    the record that holds it, by its path in the work item. The changelog's
    section is never folded, and a body that passes the limit with every
    other section folded is refused, with nothing written, so `pr.md` or
    `changelog.md` is shortened first. The fold leaves room for the seal
    mark's line whether or not the mark is written, so the run after a
    `sealed` guarantee folds what the sealer's check folded and changes no
    copied line. GitHub refuses a longer body, and the pull request's check
    reads the body as `seal pr-body` composes it, so without the fold a work
    item whose records pass the limit has no body both accept (#1559).
    check: tests/skills/test_pr_body.py
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: the body against them, the records and the mark the `Pull request seal mark` key and the guarantee at HEAD give
  to: the body against them, the records and the mark the `Pull request seal mark` key and the guarantee at HEAD give; the composed body's length against GitHub's limit, which folds the longest sections of the copy and refuses a body that still passes it

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The *Limits* bullet saying GitHub refuses a body over its length limit and nothing here repeats it | `skills/code-review/scripts/pr_body.py`, module docstring, lines 79-80 | The docstring's description of the body states the fold, and `LIMIT`'s comment states the number and its unit (D1). The limit is now guarded, so the bullet would state the opposite of the code |

The fold adds one constant, `LIMIT`, and one fixed line, `FOLDED`, and no gate, check or mark. It answers the blocked step of #1559 by removing its cause, a body GitHub will not keep, and not by recording the block. The refusal of D5 is no new gate either: it moves to `seal pr-body` the refusal `gh pr create` gives today after the seal, so the orchestrator meets it before the sealer runs. Nothing else in the tree states the old fact (G11), so nothing more goes.

Framed 2026-11-20 by framer, before the build.
