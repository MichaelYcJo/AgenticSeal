# Design: the roll docstring describes the guard

Coordinates are at `c9f08a03` on `fix/146-the-docstring-teaches-the-removed-defect`, whose tree outside this work item's `routing.md` is `31558c76` (v0.32.3) (executed: `git diff --stat 31558c76 c9f08a03` lists `routing.md` alone).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A fact has one source, and every other place links to it." "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact." "History goes to git, the release notes and the work record." These decide D1: the lag rule is stated once, and each sentence that leaned on the old absolute is corrected in the same commit |
| `skills/core/SKILL.md` *The first value* (read) | "Text no agent acts on, such as a hook's edge cases, stands in the code's docstring or in a document only a person opens." The module docstring is the right home for the roll's rationale, so D1 keeps it there rather than moving it |
| Milestone `release: 0.32.4` (executed: `gh api repos/MichaelYcJo/AgenticSeal/milestones/88`, 2026-11-05) | "Docstrings and comments under tests/ and .github/scripts/ state only what the tree holds now, and text that costs lines with nothing to catch its drift is removed before it is corrected." It carries "#146's two docstrings of `roll_flow_measurement_issue.py` (its request for mutation pins is not carried)". This fixes the scope and puts the two mutation cases out |
| #1355's principle, as work item `1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds` applied it (read: its `frame/design.md` *D1*) | Its disposition G: where a sentence holds grounds a person may act on, the grounds stay in one short sentence and the issue number replaces the record. The lag paragraph's "Phase 1 of this work item measured" takes that disposition (D1, item 1). This frame departs from it nowhere |
| Issue #146 (executed: `gh issue view 146 --repo MichaelYcJo/AgenticSeal --json body,comments,title`, 2026-11-05; no comments, which the spawn's line also states) | Its *Done when* asks that the two passages "describe the guard that exists, and the lag rule says which kind of write it holds for". Its line numbers are the old layout's (`:43-45`, `:76-80`) |
| Where the issue's two passages stand now (read: `.github/scripts/roll_flow_measurement_issue.py`, all 574 lines) | The absolute "a search-index lag can only ever produce a reading that is short a result, never one with an extra issue in it" stands at `:76-78`. "a reading that is no longer empty ends the ladder with the issue that landed" stands at `:114-115`. `landed_create`'s docstring at `:450-453` states the contrary for a lag behind a close, and its code at `:460` excludes `closed_number` |
| The class of sentences that lean on the absolute (executed: `git grep -n -i -E "lag\|undercount\|extra issue\|short a result\|no longer empty\|ends the ladder"` over the script, both roll test modules, `docs/releasing` and `skills/verify/orchestration.md`; and `git grep -n -i -E "search.index\|index lag\|undercount\|search index"` over the tree outside `seal/`) | Beyond the two passages, three more sentences state or lean on the absolute: `open_flow_measurement_issues`'s docstring `:318-321` ("a lag can only ever undercount", "never what a lag produces"), the transaction paragraph `:136-138` ("the retry-once hardening above treats as never a lag artifact"), and `tests/github/test_roll_flow_measurement_issue.py:256-257` ("never what a search-index lag produces -- a lag can only undercount"). `skills/verify/seal-arms.md:63` is about a walk that skips, not this lag. The script was read whole, so its list is whole. The tree-wide list is a grep, so it is a sample over the spellings searched |
| The replacement paragraphs the issue names (executed: `git log --all` on `seal/specs/1788486395-the-roll-opens-the-next-log-with-no-body/rounds/round-2.md`, then `grep -i "replacement\|lag"` over each of its two versions; read: the issue body) | Neither version of round 2's record holds the reviewer's replacement text. It names them as handed to #146, and #146's body does not hold them either. So D1 states what each passage must say, and the phase writes the words |
| `seal/ledger/` and `seal/specs/` (executed: `ls seal`, and `git log --all --diff-filter=A/D` on the round record) | Neither stands today. `f51e634d` (#497, #504) folded the work items into standing statements and removed round 2's record. #146's fourth *Done when* item, extending the ledger's F1 and F3 rows, names a file that no longer exists, so it is gone rather than out of scope |
| Where the lag was measured (executed: `git log --diff-filter=A -- .github/scripts/roll_flow_measurement_issue.py` gives `23d35b53`, #109; `git blame -L 68,80` gives the same commit for the whole paragraph) | "Phase 1 of this work item" at `:68-69` is #109's phase 1. The sentence can name #109 |
| `.github/workflows/close-issues-on-release.yml` (executed: `grep -n` on its steps) | `close_issues_on_release.py` and `tracker_labels.py` run before the roll in the same job. The roll's own lookup in `main` follows no write by the roll itself. That fact is what the existing "A release does not write the label it is about to look for" sentence states, and it stays true |
| `docs/releasing/issues-and-milestones.md` *`flow-measurement` is a label that is not an index* (read, `:87-104`) | It says the roll "fails loudly on zero or on two rather than guessing which is current" and states nothing about the lag's direction. It stays true, so `## Rule changes` holds the no-change block |
| Docstring readers (executed: `git grep -n -E "__doc__\|docstring"` over both roll test modules) | No case reads the script's docstring text. `tests/github/test_roll_flow_measurement_issue.py:528` and `:955` refer to the recovery message and the unreadable-title direction, neither of which this work changes |
| Bare commit hashes, #1359's class (executed: `grep -n -E '\b[0-9a-f]{7,40}\b'` over the script, and over `tests/github/test_roll_flow_measurement_issue.py:250-260`; both exit 1) | No bare hash stands in any sentence this work rewrites, so none falls to this work item |
| Siblings (executed: `grep -n -i -E "commit gate\|commit-gate\|version.check"` over the script and its function test module; exit 1) | #1352's and #238's sentences are not in either file. #1381, #1382 and #1359 touch other files |
| `seal/follow-up.md` (read) | No row waits on this work |
| Process changes (executed: `gh release view --json body` for `v0.32.3`, which holds no `### Process changes` table; `grep -A30 "### Process changes"` over the ten fragments under `seal/threads/` that hold one) | No row changes how a docstring states a rule |
| Earlier decisions: MichaelYcJo/SpecSeal#110's floor (read: round 2's record at `v0.8.0`, its last paragraph) | The floor ended that run at `Loses a record or crashes: no` and handed the three findings to #146. This work carries the docstring finding and, by the milestone, not the two pins. That is consistent with the floor: none of the three loses a record or crashes |
| `routing.md` (read, committed at `c9f08a03`) | Planning framer, Implementation crafter, Review through the review chain, Destination open the pull request, Automation yes. Nobody is asked anything during the run |

**D1. The lag rule is stated once, in the module docstring, by kind of write. Every other sentence that stated it or leaned on its absolute is corrected to cite it or to state its own decision.** The phase writes the words. Each passage must hold what its item says:

1. **The lag paragraph, `:68-80`.** It states that `gh issue list` reads a search index that lags writes. A lag behind a write that adds an issue to a reading, a create or a label added, gives a reading short a result. A lag behind a close gives a reading with an extra issue in it. It keeps the decision: a zero reading in `main`'s lookup gets one retry after `RETRY_DELAY_SECONDS`, and a reading of two or more is not retried and fails loudly. The grounds for not retrying two or more are not that a lag cannot produce them. They are the invariant paragraph's own rule at `:62-66`, which fails loudly rather than guessing which issue is current, and the fact that the lag was measured as an undercount. The measurement's grounds stay in one sentence naming #109, and "Phase 1 of this work item" goes (#1355's disposition G).
2. **The guard paragraph, `:111-117`.** "a reading that is no longer empty ends the ladder with the issue that landed" goes. The paragraph says a failed create is followed by `landed_create`'s lookup, and the ladder ends where that lookup finds the create landed. It does not restate `landed_create`'s condition, which that function's docstring holds. The sentences on why a retry would open a second issue, and on the last rung using `run`, stay.
3. **The transaction paragraph, `:136-138`.** The clause "the retry-once hardening above treats as never a lag artifact and always the invariant broken" becomes a clause naming the reading `main` fails on without a retry. The rest of the paragraph stays.
4. **`open_flow_measurement_issues`'s docstring, `:316-322`.** "a lag can only ever undercount" and "it is never what a lag produces" go. The docstring cites the module docstring for the lag rule and states its own decision: one retry on an empty reading, none on two or more.
5. **`landed_create`'s docstring, `:447-455`.** Its condition stays as it reads. Its restatement of the lag direction for a close cites the module docstring's rule instead of stating it a second time.
6. **`tests/github/test_roll_flow_measurement_issue.py:256-258`, `test_refuses_two_open_issues_loudly_without_retrying`'s docstring.** The claim that a lag can only undercount goes. The docstring states what the case holds: a reading of two or more fails loudly without the retry.

## Scope

In scope:

1. The two passages #146 names, D1 items 1 and 2, in `.github/scripts/roll_flow_measurement_issue.py`'s module docstring.
2. The three other sentences of the script that state or lean on the absolute, D1 items 3, 4 and 5. They are the same class (contract rule 12). The script was read whole, so the list is closed.
3. The one test docstring sentence that states the absolute, D1 item 6. It is the same class in the file that tests the script. The milestone's purpose covers docstrings under `tests/`.
4. No code line of either file changes. The diff touches docstring text alone.
5. `.claude-plugin/plugin.json`'s version moves to `0.32.4`, in the commit that adds this work item's `changelog.md`. This work item is the release's first, as `docs/releasing/branch-and-release.md` *Cutting a release* places the version move.

Out of scope:

- **The two mutation cases**, a case red when `RETRY_DELAY_SECONDS` is zero and a case red when the ambiguous-baseline note is dropped from the last rung. The milestone states that #146's "request for mutation pins is not carried". The two requests stand in #146's body and nowhere else. The changelog fragment and the pull request body say they were not carried, by the milestone's decision, so #146 closing does not read as the pins built.
- **The ledger's F1 and F3 rows.** `seal/ledger/` no longer exists (*Grounding*), so the item has nothing to extend.
- **Other history in the same module docstring**: "Issue #109 part 3" and "phase 1 of this work item" at `:4-6`, the #155 narrative at `:28-33`, and the `(#136)` citations at `:92` and `:109`. None of them states the lag rule or the guard. The milestone carries #146's two docstrings, not a sweep of this file.
- **`tests/github/test_roll_flow_measurement_issue.py:174-178`**, "Phase 1 measured the lookup returning `[]`". It states the measured undercount, which stays true. It does not state the absolute.
- **The sleep assertions at `:201` and `:483`** and the `_ladder_harness` docstring at `:62-66`. They belong to the mutation-pin request.
- **`landed_create` tolerating its own lookup failing.** Round 2 at `v0.8.0` handed that to #146's context and declined to call it a defect. #146's body does not ask for it.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The absolute is gone | Given the phase's commit, when the two files are searched for the absolute's spellings, then nothing is printed | `git grep -n -i -E "only ever undercount\|can only undercount\|never one with an extra\|never what a .*lag produces\|never a lag artifact\|no longer empty"` over the script and `tests/github/test_roll_flow_measurement_issue.py`, exit 1, in the phase record. This is a sample over spellings, so S2 is the check that counts |
| S2. The docstring agrees with the code | Given the module docstring and `landed_create`, when a reader reads the lag paragraph, the guard paragraph and the two function docstrings against `:323-327` and `:457-463`, then no sentence contradicts another or the code, and the lag rule is stated in one place | the proofer's reading of D1's six items against the code |
| S3. No code changed | Given the base and the phase's commit, when each file's `ast` is dumped with every docstring removed, then the two dumps are equal | a probe in a scratch clone that strips module, function and class docstrings and compares `ast.dump` at the two commits, its result in the phase record |
| S4. The modules still load and pass | Given the phase's commit, when the two roll test modules run, then they pass, and `ruff check` and `ruff format --check` pass on the two touched files | `tests/github/test_roll_flow_measurement_issue.py` and `tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py` run narrow; ruff on the two paths |
| S5. What was not carried is named | Given the changelog fragment, when it is read, then it names the two mutation cases as not carried by the milestone's decision, and the ledger item as gone | the fragment against this *Scope* |

## Data & interfaces

No interface changes. `RETRY_DELAY_SECONDS`, `open_flow_measurement_issues` and `landed_create` keep their behaviour. Only their docstrings and the module docstring change.

## Rule changes

- nothing
  why: The work corrects a script's docstring to its code. `docs/releasing/issues-and-milestones.md` *`flow-measurement` is a label that is not an index* says the roll fails loudly on zero or on two and states nothing about the lag's direction, and that stays true.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the absolute that a lag only ever gives a reading short a result | `.github/scripts/roll_flow_measurement_issue.py`, the module docstring's paragraph opening "One retry on a zero-open reading" | the same paragraph, stated by kind of write (D1, item 1). `landed_create`'s code is what showed it false |
| "Phase 1 of this work item" as the source of the measurement | the same paragraph | one sentence naming #109; git holds the record |
| the guard's condition as "a reading that is no longer empty" | the module docstring's paragraph opening "A failed attempt re-reads the open-issue list" | `.github/scripts/roll_flow_measurement_issue.py#landed_create`'s docstring, which the paragraph names |
| the clause "never a lag artifact and always the invariant broken" | the module docstring's paragraph opening "The close and the open are not one transaction" | a clause naming the reading `main` fails on without a retry |
| the second and third statements of the lag rule | `.github/scripts/roll_flow_measurement_issue.py#open_flow_measurement_issues` and `#landed_create`, their docstrings | the module docstring, which both already cite |
| the claim that a lag can only undercount | `tests/github/test_roll_flow_measurement_issue.py#Test_main.test_refuses_two_open_issues_loudly_without_retrying`, its docstring | the case's own rule: two or more fails loudly without the retry |

This work adds no mechanism, so no row names a return.

Framed 2026-11-05 by framer, before the build.
