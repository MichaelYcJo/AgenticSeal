# Phase 8: 1792540458-on-demand-files-state-the-current-rule

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | d03330d7 |


## What this phase was asked

`CONTRIBUTING.md` rewritten to the current rule, its *House rules* and *What
a change to a gate must carry* headings kept, with the 29 test modules naming
it as the smith's module set. `tests/test_the_rules_have_one_owner.py`'s
`CONTRIBUTING.md` link moves from the section-sign spelling to the
`AFTER_THE_SEAL_LINK` form. Every imperative sentence whose actor or
condition the smith chose is listed here.

## What this phase found

**The frame holds for this phase.** No heading of the file changed, so S14
has nothing to grep, and the file now holds one section sign, the
`skills/agent-contract/SKILL.md` §2 citation, which S8 keeps (executed
`git grep`). The phase closed in two commits: 6e4c2034 rewrote the file, and
d03330d7 named the contributor in four sentences the first commit had left
in the passive, which hid the actor the owner's direction (b) asks for.

**"you" became "the contributor".** The file is read by a person
contributing and by the parties of a maintainer's run (the smith finds the
runner in it), so every "you" and every bare imperative now names the
contributor, the pull request, or the maintainer. The test modules that
quoted "on your machine" and "your OS keyring" follow.

**Stored values left.** The file counted CI's jobs ("six"), its shards
("three", "four", "the four parts"), the case ceiling ("90 s") and the
artifact's retention ("seven days", twice). Each is a value `test.yml` or
`tests/conftest.py` holds, so the file now names the constant or the file
and states no copy. The one number kept is the fallback's cost, "close to
sixty seconds each", because `tests/test_the_suite_has_a_command_that_is_cheap_twice.py`
holds that the cost is stated, and it is a property of the form rather than a
setting anything stores.

**Census (S11): what left, and why it could go.**

| What left | Grounds |
|---|---|
| `#667`, `#718`, `#832`, `#647`, `#337`, `#133`, `#156`, `#841`, `#864`, `#931`, `#684`, `#510`, `#866` | history; each sentence stands without its number |
| "It is the form this section used to name first" | history |
| "55–58 seconds each, paid on all seventeen test calls of one measured segment" | anecdote; the cost stays as "close to sixty seconds each" |
| "Established by reading every step of `.github/workflows/hygiene.yml` and `.github/workflows/test.yml` against a live contribution that carried none of the following and came back green" | how the table was made; each row keeps its reason |
| "CI runs six jobs", "macOS in three shards and Windows in four", "(90 s)", "the four parts", "kept seven days", "older than seven days" | stored values; the constant or the file is named |
| "Three branches running in parallel once shared exactly one file between them … the conflict was three lines" | anecdote; the rule and its link stay |
| "both incidents that forced a rewrite of this repository's history entered exactly this way" | history; the reason stays as a property of a real identifier |
| "see the counterfeit rule below" | a dash and a bare imperative; "as the counterfeit rule below says" |

**Cases rewritten** (each seen red after 6e4c2034 or d03330d7 by
`mutation-check` on the new text, executed):

| Case | What changed |
|---|---|
| `tests/test_the_rules_have_one_owner.py`, rule 6's `CONTRIBUTING.md` link | `AFTER_THE_SEAL_LINK`. Red with the section sign put back |
| `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py#test_the_rule_is_where_a_contributor_reads_it` | "The call names `encoding=\"utf-8\"`." |
| `tests/test_the_rules_claude_md_names_have_one_home.py`, the `identifiers` row | the allowlist sentence with its actor, and the reason as a property |
| `tests/test_the_suite_runs_with_gh_logged_out.py#test_contributing_says_the_suite_runs_logged_out` | "on a contributor's machine", "the OS keyring" |
| `tests/test_the_suite_has_a_command_that_is_cheap_twice.py#test_the_section_keeps_the_broad_once_rule` | "The broad runs come once" |
| `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` | "over the committed file and commits it" |

`tests/test_the_suite_has_a_command_that_is_cheap_twice.py#test_the_slow_form_says_what_it_is_for_and_what_it_costs`
was not edited; it went red when the first wording dropped the cost, and the
cost came back.

**Imperative sentences whose actor or condition the smith chose.**

| Sentence | What was chosen |
|---|---|
| "**A contributor bases the branch on the open release branch, not on `main`.**" | the actor, which was "your branch" |
| "The contributor sets it as the base when opening the pull request" | the actor and the moment |
| "Changing the base instead takes the refusal with it" | stated as a fact, which was an imperative |
| "**The contributor opens the pull request when the work is done, and opens it ready.** … the branch is pushed as often as the contributor likes" | the actor |
| "a maintainer adding a CI step reads the row rather than this sentence" | "should read" made a statement |
| "**A contributor names a module.**" | the actor of "Name a module" |
| "A contributor using it checks `python3 -V` first" | the actor and the moment |
| "The contributor makes it cheaper, splits it, or samples what it walks" | the actor |
| "The contributor refreshes the file from the artifact of the branch's latest `tests` run … moves … and commits it" | the actor |
| "Where the run's artifact has expired, the contributor re-runs it first" | the condition, which was "older than seven days" |
| "The contributor writes the test against the unfixed code and watches it fail before fixing anything" | the actor |
| "The pull request says whether the change makes the gate block more or allow more"; "The pull request says how many times the change puts a question in front of a person" | the place the answer goes, which the next paragraph names |
| "The contributor names in the pull request each platform they could not test" | the actor and the place |
| "a contributor extends its allowlist deliberately"; "a contributor classifies a unit in its `ALLOWED` deliberately" | the actor, in place of a bare imperative and then a passive |
| "The call names `encoding=\"utf-8\"`"; "its writer names the encoding there" | the actor of "Name" and of "yourself" |
| "A maintainer reads it before merging anything, not after" | the actor |
| "A proposal opens an issue first" | the actor |

**Restatement pairs of this file** (Scope 10, measured at d03330d7 with the
module's own `shared_counts`, executed):

| Pair | Measured | `BASELINE` | Whose the residue is |
|---|---|---|---|
| `CLAUDE.md`, `CONTRIBUTING.md` | 0 | 14 | drained; phase 9 removes the entry |

No other pair names `CONTRIBUTING.md`.

**Bytes** (executed `wc -c`): `CONTRIBUTING.md` 21,240 at b3154f43 and
20,968 at d03330d7. No agent's definition directs it to open the file, so it
is in no S13 set.
