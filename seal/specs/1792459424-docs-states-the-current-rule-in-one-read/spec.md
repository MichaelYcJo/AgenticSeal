# Feature Specification: docs/ states the current rule in one read (#941)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source; a change rewrites the text it amends in place and removes what stood on the old fact; history goes to git, the changelog and the work record, never into a document |
| `skills/settle/SKILL.md` *Rule changes* | The field-word grammar a spec states rule changes in. This item extends it with the no-change block (Data and interfaces) |
| `skills/settle/SKILL.md` *A rule has one shape* | A rule is one bold sentence, its grounds, and one line naming what reads it. This item renames that line to `check:` |
| `skills/settle/SKILL.md` *The index* | `docs/README.md` names every top-level document on exactly one row; each split adds its rows |
| `skills/settle/SKILL.md` *A document past its ceiling is split, never trimmed* | A document past `Document token ceiling` (25000 in `seal/config.md`) is split along its own headings |
| `skills/settle/SKILL.md` *A released work item with no `spec.md`* | A row is closed with what closed it, and the closure merges to the branch the release merges to before the directory goes |
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion* | `unverified_check.py#settled`: a directory goes cleanly when nothing in its record is open at the merge base and every rule change it states holds |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below is the list the review reads against the diff |
| `CONTRIBUTING.md` *What a change to a gate must carry* | The `check:` reader is a suite case that fails a pull request: a red case per refusal, a failure direction, and what it removes |
| `CONTRIBUTING.md` *House rules* | `docs/one-root-by-lifetime.md` and its `.ko.md` edition move together, outline for outline |
| `seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/questions.md` Q2 | A released spec with no `## Rule changes` and nothing open passes the CI readers when removed. Open there with default (a), and (a) is what `unverified_check.py#settled` does (read: lines 1290 to 1302) |

## Scope

**In.**

1. **The `check:` line replaces `Enforced by:` everywhere a rule is stated**:
   `docs/`, `agents/`, `skills/`, `templates/`, `CLAUDE.md`,
   `CONTRIBUTING.md` (the `RULE_FILES` list in `.github/scripts/rules.py`).
   One-shot conversion of all 240 lines: the `::name` parts dropped, a file
   named twice in one line named once, a rule that gates a commit or a merge
   given a named marker carried by its tests, and each of the 18
   `nothing` lines rewritten by hand to the no-target form. The grammar is in
   Data and interfaces, stated there once. `bin/rules --check` reads it and
   refuses every other spelling. The prose that names the label (the
   implement skill's section 2, `agents/framer.md`, `agents/smith.md`,
   `agents/warden.md`, `skills/code-review/orchestration.md`,
   `skills/gap-analysis/SKILL.md`'s description, `skills/settle/SKILL.md`) is
   rewritten to the new label in the same commit.
2. **The 127 `<!-- specs/<id> -->` marker lines leave `docs/`**, with the
   readers that exist only for them: `fold-check`'s shape arm and its
   `Fold shape from` row, the marker arm of
   `tests/test_both_editions_carry_the_same_folds.py`, the marker exemption of
   `tests/test_docs_line_wrap.py`, and the `CONTRIBUTING.md` sentence that
   requires the same fold markers in both editions.
3. **The no-change block.** `nothing — <why>`, with its em dash, is the one
   syntax left in the settle grammar that a near miss trips: the reader
   refuses a hyphen and names the dash. It becomes field words in both places
   a frame writes it, `## Rule changes` and `## Removes`. #1000 also names
   this form; it is taken here because it shares
   `unverified_check.py#NOTHING` with the `Enforced by:` form, and #1000 keeps
   the other two shapes (`none — <why>`, and the sealer's `withheld — ` and
   `undecided — `).
4. **Every document under `docs/` states the current rule, once.** Narrated
   history, dated decision sections and issue numbers a sentence can stand
   without leave. A sentence stays only if an agent not editing that
   component would decide wrongly without it: what the component decides,
   when it asks, its limits, the promises others rely on. Internal mechanics
   move to the first sentence of the docstring of the test that holds them,
   or to the code's docstring. Headings and labels this item writes hold no
   dash, arrow, middle dot, pipe or section sign; a cross-reference is the
   backticked path followed by the heading in italics. `docs/one-root-by-lifetime.md`
   and its `.ko.md` edition are rewritten to what still rules (#923 Q1).
5. **A document still past 25000 estimated tokens after its rewrite is split
   along its own `##` headings**, into new top-level files in the same flat
   `docs/`, each named on its own `docs/README.md` row. Measured at ac83bdf3:
   `docs/worktree-guard-spec.md` 37,178 and `docs/one-root-by-lifetime.ko.md`
   28,936; every other document is under the ceiling.
6. **The census.** Every rule the old text stated is mapped to its new home
   (the document, a test docstring, a code docstring, or gone with the
   reason), recorded in the phase record of its document group. No test file
   an old line named is left unnamed by a new line unless `## Removes` names
   it.
7. **The backlog of pre-#953 work items is read and prepared for one
   settle.** 117 released work items hold a `spec.md` with no
   `## Rule changes`, and 8 hold no `spec.md`. For each spec: what it decided
   that `docs/` lacks and an agent outside the component needs is written
   into its document; what a later change overturned goes nowhere; what is
   internal is left to the test that holds it. Each spec then gains a
   no-change block whose `why:` says which of the three it was. Every open
   `## Not verified` row in the 125 directories is closed with what closed
   it (the closing rule is in Data and interfaces).
8. **What can leave now, leaves.** The 8 released directories with nothing
   open at the working tree and at `origin/main` are removed in this item:
   `1788177600`, `1788395377`, `1790134781`, `1791019421` (no `spec.md`), and
   `1790260563`, `1790263216`, `1792126889`, `1792368014`. Each check that
   reads `seal/specs` gets its answer under `skills/settle/SKILL.md`
   *Answer every check that reads the corpus*.
9. **The preload is not larger.** No paid non-inferiority run (owner,
   `questions.md` Q1): the only preload change is the label lines, so rule 4
   of the proof, preload bytes, is read with `wc -c` on `agents/*.md` and the
   skills their `skills:` lists inject, at ac83bdf3 and at phase 9's commit.

**Out, and why.**

| Left out | Why |
|---|---|
| Removing the other 117 backlog directories | Their open rows are open at `origin/main`, and the CI readers on the release pull request ask at main's tip (`hygiene.yml` passes `--baseline origin/<base>`; read). A row closed and its directory removed before the closure reaches main is refused there. The owner's `settle --apply` after 0.22.3 merges removes them, because each then carries a no-change block and nothing open |
| The prose of `skills/`, `templates/`, `CLAUDE.md`, `CONTRIBUTING.md` | #940's. This item edits those files only where they state a fact it changes: the label, the markers, the no-change spelling, and citations of a `docs/` heading it renames or moves |
| The layout of `tests/` | #942's. This item edits tests only to add the gate markers, receive a docstring sentence, update or retire a case that pins text it rewrites, and retire the marker and shape readers. #942 moves the files afterwards, and `bin/rules --check` names any `check:` target the move leaves behind |
| A topic taxonomy for `docs/` | The owner, 2026-10-20: split along a document's own headings, the tree stays flat |
| `docs/experiments/` | Kept as it is (owner, `questions.md` Q3) |
| A section sign, a coordinate's `#` and `>`, the changelog's `<!-- specs/<id> -->` lines, and the template headings' arrow outside `docs/` | #940 and a later item take them (owner, `questions.md` Q2) |
| The paid non-inferiority run | Not run (owner, `questions.md` Q1) |
| `seal/specs/1792449518-*/questions.md` Q2, Q3 and Q4 | #953's own rows |
| A converter shipped for other repositories | `bin/rules --check` refuses the old label and its refusal names the new spelling; `Operational impact` in `plan.md` says what a consuming repository meets |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a file target | Given `check: tests/test_chain_check.py` under a rule, when `bin/rules --check` runs, then it resolves and exits 0, and `bin/rules <doc>` prints the module docstring's first sentence | a case in `tests/test_the_rules_command_reads_each_rule_off_its_test.py` |
| S2 several targets | Given `check: tests/test_a.py tests/test_b.py`, then both resolve | the same module |
| S3 a marker target | Given `check: verdict-line` and one test carrying `@pytest.mark.rule("verdict-line")`, then it resolves, and `bin/rules <doc>` prints that test's docstring first sentence; with no test carrying it, exit 1 naming the marker | the same module |
| S4 the no-target form | Given `check: none reader: the warden at review`, then it passes; `check: none` alone, or `reader:` with nothing after it, is exit 1 at its line | the same module |
| S5 every other spelling is refused loudly | Given a shown line opening `Enforced by:`, `Check:`, `**check:**`, `check :`, `- check:`, or a `check:` value holding `::`, a comma or `—`, then exit 1 with `<path>:<line>` and the spelling it expected; never skipped | one case per spelling, each seen red with the refusal deleted |
| S6 a line inside a fence or a comment is not read | Given an example `check:` line in a fence, then it is neither resolved nor refused | the same module |
| S7 no protection dropped | Given the base's 240 lines and the converted tree, then every target path the base named is named by a `check:` line, carried by a marker, or a `## Removes` row | the comparison command in `plan.md` phase 1, re-run per group |
| S8 no marker | `git grep -c '<!-- specs/' -- docs` prints nothing | grep |
| S9 one read | `bin/fold-check` names no document past 25000 and its index arm passes | `bin/fold-check`, exit 0 and no `split` line |
| S10 the no-change block | Given `## Rule changes` holding `- nothing` and `  why: <reason>`, then `rule_changes.py#parse` returns no operations and no errors; `nothing — x` is refused at its line naming the block; a block with no `why:` is refused | cases in `tests/test_settle_applies_rule_changes_in_place.py`, seen red |
| S11 the backlog is ready for one settle | Given the 117 backlog specs after this item, when `bin/settle` dry-runs, then each is listed with nothing to apply and none as refused or as having no `## Rule changes`; at `--released-at` holding this item's merge, each is listed under what `--apply` would remove | `bin/settle` dry run, read |
| S12 nothing open | `skills/verify/scripts/unverified_check.py` over each backlog directory reports no open row | the command per group |
| S13 what can leave now | Given the 8 directories removed, `unverified_check.py --baseline origin/release/v0.22.3 seal/specs/` and `--baseline origin/main` both name each as settled and exit 0 | both commands |
| S14 a moved or renamed heading leaves no stale citation | `git grep` of each old heading text outside `seal/` and `changelog/` finds only its new home | grep per renamed heading, listed in the phase record |
| S15 both editions | `tests/test_both_editions_carry_the_same_folds.py`'s outline arm passes over the rewritten pair | the module |
| S16 the preload is not larger | `wc -c` over each agent's definition and the skills its `skills:` list injects is no larger at phase 9's commit than at ac83bdf3 | the two readings in `phases/phase-9.md` |

## Data & interfaces

**The `check:` line.** The one statement of the grammar; every other file
points here until settle moves it to `skills/settle/SKILL.md` *A rule has one
shape*.

- A check line is a shown line (outside a fence and an HTML comment) of a
  rule file whose text, after any leading spaces, starts with `check: `
  (lowercase, one space after the colon).
- Its value is either the no-target form, exactly `none reader: <who reads
  it>` with a non-empty reader, or one or more targets separated by single
  spaces.
- A target is a repository path that exists (a file, or an eval case
  directory `evals/behaviour/<agent>/<case>/` holding `case.yaml`), or a
  marker name: lowercase letters, digits and hyphens, no `/`, carried by at
  least one test as `@pytest.mark.rule("<name>")`.
- A marker is used only for a rule whose test drives a script that can refuse
  a commit (the git hooks, the PreToolUse commit gate) or fail a required
  job of a pull request (a `hygiene.yml` step). Every other rule names files.
- Refused, exit 1, at `<path>:<line>`: a shown line whose text after leading
  spaces and emphasis marks matches `check`, `checks` or `enforced by`, in
  any case, followed by optional spaces and a colon, and is not the exact
  form above; a value holding `::`, `,` or `—`; a path that does not exist;
  a marker no test carries.
- The `rule` marker is registered by a `pytest_configure` hook added to
  `tests/conftest.py` (it has none today, and no pytest ini file exists), so
  pytest reads it without an unknown-mark warning.
- `rules` prints a finding as `rules: <path>:<line>: <heading>: <why>`, with
  no section sign.

**The no-change block**, in `## Rule changes` and in `## Removes`, in place
of the items or the table:

```
- nothing
  why: the reason, on one line or continued four spaces in.
```

`rule_changes.py#parse` reads `- nothing` as an operation line with one
field, `why`, and refuses any other field. The em-dash form is refused at its
line, naming the block. `unverified_check.py#NOTHING` and the two readers
that load it (`fold_check.py#names_targets` goes with the shape arm) move to
the block.

**Closing a backlog row.** A cell's `closed` says what closed it, and only
these close one:

- a row about the full suite, lint, typecheck or the broad run: the merged
  pull request whose CI ran it green, by number;
- a row about a platform leg whose cases still exist: the CI run of a later
  merged pull request on that leg, by number;
- a row whose subject left the tree: the commit that removed it;
- a row still true about behaviour the tree cannot observe (a screen, a live
  harness, another person's sessions): a limit sentence in the owning
  document, and the row closed naming that document and heading.

A row none of these closes stays open, and its directory stays, named in the
phase record.

**Backlog assignment.** A backlog spec belongs to the document group whose
documents name, by `check:` line, the most of its live test files; a spec
naming none goes to the group its title is about; phase 9 takes any not yet
assigned. Measured at ac83bdf3 with `Enforced by:` targets (executed, a
script over every `spec.md`): 39 specs have every live test file they name
also named by a rule file, 63 some, 4 none, 11 name no live test file; 68
name at least one shipped path that no longer exists.

## Rule changes

- nothing
  why: this item rewrites docs/ in its own diff, so nothing is left to apply.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `Enforced by:` label, its `::name` targets and its comma list | `.github/scripts/rules.py#RULE_CLOSER`, `.github/scripts/rules.py#targets_of`, `skills/settle/scripts/fold_check.py#target_problem` | the `check:` grammar above, read by `rules.py` alone |
| 240 `Enforced by:` lines (docs 163, agents 43, skills 34) | every rule file `RULE_FILES` names | the same number of `check:` lines, one per rule |
| The shape arm and its cutoff | `skills/settle/scripts/fold_check.py#shape_problems`, `#numbered_statements`, `#statements`, `#enforced_lines`, `#bound`, `#names_targets`, `#ENFORCED`, `#BOLD_OPENING`, the `--shape-from` flag | it binds statements by marker id, and no marker remains; a rule written with no `check:` line is the review's to find, as it already is for every unmarked paragraph |
| The `Fold shape from` row | `seal/config.md`, `templates/config.md#"The fold's values"` | nothing reads it |
| The shape cases | `tests/test_a_folded_statement_names_what_enforces_it.py` | its grammar cases move to `tests/test_the_rules_command_reads_each_rule_off_its_test.py`; its marker and cutoff cases retire with the arm |
| 127 fold marker lines | `docs/*.md`, every `<!-- specs/<id> -->` line | git history; the settled predicate replays rule changes since #953 and reads no marker |
| The marker arm and the marker exemption | `tests/test_both_editions_carry_the_same_folds.py`, `tests/test_docs_line_wrap.py` | the outline arm stays; nothing is left to exempt |
| The editions sentence about fold markers | `CONTRIBUTING.md#"House rules"` | the outline sentence stays |
| `FOLD_MARKER`, where no reader is left | `skills/verify/scripts/unverified_check.py#FOLD_MARKER` | removed only if `gather_changelog.py` and every test read their own pattern; otherwise kept and named in the phase record |
| The em-dash no-change form | `skills/verify/scripts/unverified_check.py#NOTHING`, `skills/settle/scripts/rule_changes.py#parse`, `skills/settle/scripts/settle.py#write_outcome`, `templates/sdd-spec.md`, `skills/settle/SKILL.md#"Rule changes"`, `docs/the-reader-registry.md#"A frame names what its work removes"` | the no-change block; `seal/specs/1792449518-*/spec.md`'s section is rewritten to it in the same commit |
| Narrated history and dated decision sections | `docs/one-root-by-lifetime.md` and `.ko.md` from *The problem, as measured* through *Decided when the process record stopped waiting for the fold (2026-10-04)*, and every such paragraph elsewhere in `docs/` | git, the changelog and the issues; each removed paragraph is a census row of its phase |
| Cases that pin a sentence this item removes | `tests/`, each case named in its group's phase record | retired with the sentence, or rewritten to the new sentence where the rule stays |
| 8 work-item directories | `seal/specs/1788177600-*`, `1788395377-*`, `1790134781-*`, `1791019421-*`, `1790260563-*`, `1790263216-*`, `1792126889-*`, `1792368014-*` | nothing open in each at the tree and at `origin/main`; git history |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

<!-- The line below is the framer's mark, and it is the only evidence in the
     TREE that the framing happened — the existing framer mark lives in the
     repository's git dir, and a git dir does not travel, so CI cannot see it.
     Fill in the date and `<who>`; `<who>` takes the two values the `Planning`
     row of `routing.md` takes, `framer` or `the session`, and a mark that
     disagrees with that row is refused at the pull request rather than
     guessed at.
     The shape — verb, date, who, the moment — is the one `routing.md` and
     `plan.md` already end with, which is what keeps three feet-lines from
     becoming three conventions.
     A reframe adds `Reframed <date> by <who>, after round <N>.` UNDER this
     line when the review chain sends the work item back to its framer. It is
     never in this template; only a reframe writes it. -->

Framed 2026-10-20 by framer, before the build.
