# Design: each wording pin is kept or removed (#1233)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| **G1** `docs/what-a-script-gates.md` *The checks*, the row for the cases under `tests/text/` and `tests/behaviour/` that read prose (read); `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* (read); #1111's *What changes* (executed: `gh issue view 1111`) and the module it left, `tests/text/test_the_agent_contract_holds_the_universal_rules.py#FACTS` and its docstring (read) | The policy in force is "a case pins a fact a reader acts on; one that pins wording goes", and this work applies it without changing it. #1111 read a pin as a fact where its characters are what a reader needs fixed: a citation's spelling, a heading a reader resolves, a word a checker matches. Its `FACTS` constant kept rule 1's two command forms "which an agent copies into a shell" and named, beside each, what the fact is and who reads it. *The criterion* below is that reading, carried to 56 modules. |
| **G2** The measure: `48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md` *The table* row K5, *Command K5* and *Instances K5* (executed: `git show`). *Command K5* re-run at this work item's base, `361ed0cb` (executed: *The listing* below) | At `361ed0cb` the lister prints `pins 506 in 56 modules`; at `bf9efcba` it prints `pins 518 in 57 modules` (executed, both in a scratch copy). The one module that left is `tests/behaviour/test_one_word_one_meaning.py`, which #1243 deleted, so the 56 modules are the issue's list less #1197's. One module's count moved: `tests/skills/test_seal.py` lists 4 where it listed 3. The 506 asserts stand in 259 cases: 73 cases hold listed asserts alone and 186 hold other asserts beside them (executed: an `ast` walk mapping each listed line to its `test_*` function). A shape count of the literals, which rules on nothing, gives 22 asserts whose right side is a variable holding a program's output (`out`, `ln`, `said` and the like), 134 whose literal carries a code span, a heading mark, a path or a flag, and 350 plain prose (executed). *Instances K5* read 10 of the 518 and found 9 wording and 1 output. |
| **G3** `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*; `seal/config.md` (read: no `Policy root` row, so the policy root is `docs`); the unsettled designs under `seal/threads/` (read: each `## Rule changes`) | The policy in force is `docs/` plus the pending rule changes of #1258 (`docs/release-checklist.md` *5. The release pull request*) and #1231 (`docs/the-record-layout.md` *The root records*); #1235 and #1243 state none. None touches *The run* of `docs/the-review-record.md` or *Registration* of `docs/the-session-hooks.md`, the two sections this design changes. |
| **G4** `.github/scripts/rules.py`, its docstring at `:37-46` (read); `skills/settle/SKILL.md` *A rule has one shape* (read); `v0.27.1:seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md` *Scope* item 3 and *Out* (executed: `git show`) | `seal rules --check` refuses a check line naming a path that is no file of the repository, and a pending `change` "excuses nothing, so the test the line names stays until the settle". A module a `docs/` check line names cannot be deleted by this pull request. #1197 met the same constraint, stated its rule changes, left the module whole, and had the orchestrator file one successor issue for the deletion, which became #1243. This design does the same for the one such module (Scope item 7). |
| **G5** The `docs/` check lines that name a listed module (executed: `git grep -n '^check: .*<module>' origin/release/v0.27.3 -- docs/` for each of the 56, 106 hits on 92 lines), read against the listed asserts by a span probe: for each line, the listed asserts whose literal stands in that line's rule span, from the heading or the check line before it to the line itself (executed) | 23 lines name a module with a listed assert inside their own span. Two name a module that stops reading their rule once the build applies *The criterion*, and `## Rule changes` states both. `docs/the-review-record.md:428`, *The run*'s round cap, names `tests/text/test_the_rules_have_one_owner.py` alone. Its one case inside the span, `#test_the_cap_counts_from_the_last_design_change`, asserts phrases only (read). The module's `RULES` table holds no row for the cap (read: keys 3 to 20). The cap's default count is read elsewhere: `tests/behaviour/test_chain_hooks_hardening.py#test_the_run_names_its_default_round_count_and_the_follow_up_file` asserts "three finding rounds by default" and `follow-up.md` against the whole of `docs/the-review-record.md`, and each literal stands once in that file, inside *The run* (executed at `19957702`). The first stands in the lead sentence of the rule `:428` closes. The span probe listed that assert for `:428`, and the frame first read it as wording. Phase 4 kept it as a value, the count at which the orchestrator weighs whether the run still pays (`trail/phases/phase-4.md`), and review round 1, finding 1, found the frame's line change out of step with that ruling. No script reads the cap, which since #1167 is the orchestrator's judgment (read: `:427`). `docs/the-session-hooks.md:39`, *Registration*, names `tests/text/test_a_gate_that_fails_says_so.py`, whose one case asserts the rule's bold sentence and that this line names the module itself (read, whole). The other 21 keep a reader: each named module keeps a case outside the listed asserts that reads the rule, or a kept fact assert inside the span, or the line names another target that reads the behaviour. For eight lines the cases were read whole: `docs/branch-and-release.md:114`, `docs/issues-and-milestones.md:61`, `docs/the-broad-gate.md:42`, `docs/the-record-layout.md:144`, and `:371`, `:456`, `:509` and `:512` of `docs/the-review-record.md`. For the other 13 the reading is the names of the module's other cases and the line's other targets. Examples: `:144` of `docs/the-record-layout.md` keeps the command `seal no-work-item` and the trailer `Seal-Routing: no work item` in `tests/text/test_settle_reads_before_it_removes.py`; `:456` of `docs/the-review-record.md` keeps `RULES` row 16; `:59` of `docs/the-broad-gate.md` keeps the partition case of `tests/behaviour/test_the_gate_names_every_step_ci_runs.py`. The other 69 lines have no listed assert inside their span, so the listed asserts do not read their rule's paragraph. The span is a method with a gap: a listed assert can read a skill's restatement of a `docs/` rule, outside the span. Scope item 9 answers what a phase finds in that gap. |
| **G6** Three modules every assert of which is wording (read, each whole): `tests/text/test_the_handoff_names_the_form_it_ran.py`, `tests/text/test_absence_claims.py`, `tests/text/test_a_probe_does_not_outlive_its_round.py`; their readers (executed: `git grep -n` for each name outside `seal/threads`; `grep` of `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`) | Each asserts sentences of a rule and no command, path, heading or vocabulary word a reader resolves or a checker matches. `test_a_probe_does_not_outlive_its_round.py` asserts "A fixture chain is `&&`, never" followed by the pipe, a sentence of the rule: the operator the agent copies is the rule's meaning, which the proofer reads, and no command form stands in the literal the way rule 1's forms stand in #1111's `FACTS`. No `docs/` check line names any of the three, and no file imports one. They are named by `agents/tracer.md:72`, `skills/code-review/SKILL.md:97`, a comment at `tests/text/test_a_moved_rule_leaves_its_definition.py:602-603`, and rows 5864 to 5866, 5924, 5925 and 6071 of `.test_durations`. `APPLIES_THE_SHARED_GUARD` holds none of them. |
| **G7** The readers the two changed lines name (read): `tests/hooks/test_dispatch.py`, its docstring `:1-15`; `docs/the-review-record.md` *The run*, `:427` and the rule closed by `:498` | `tests/hooks/test_dispatch.py` drives `hooks/dispatch.py` as a subprocess and reads the failure record and the `systemMessage` that *Registration*'s rule states, so it stays the line's one target. `tests/behaviour/test_chain_hooks_hardening.py` is the module whose case reads the cap's default count (G5), so it becomes `:428`'s one target. A check line names targets or one reader and never both (`skills/settle/SKILL.md` *A rule has one shape*). What the case does not read is the orchestrator's weighing itself: each such decision is a row of `frame/plan.md` *Judgments of the run* ("Every such decision, past the third round or at it, is a row"), and `:498` names the settling session at the dry run's judgments as the reader of those rows, so that reading stands without `:428` repeating it. |
| **G8** `seal/follow-up.md` (read); `48d035aa:` *Command setup*, `audit.py#pins` (read) | No row waits on this work. Two rows concern asserts in tests: one on `assert ... not in folded` over a script's source, one on a guard phrase with `not in`. The lister reads an `in` comparison only, so neither row's asserts are listed, and neither is this work's prerequisite. |
| **G9** Sibling work of 0.27.3 (executed: `git diff --name-only origin/release/v0.27.3...<branch>` for `fix/1232-the-seal-root-files-listed-at-one-home` at `2dfbc3fe` and `chore/1263-a-band-flags-a-row-and-a-judgment-decides`) | #1263's branch holds its work item records alone. #1232's changes `skills/implement/SKILL.md`, `skills/implement/scripts/seal.py` and `skills/verify/orchestration.md`. Of the 38 listed asserts homed in the first and the 44 in the third, every one whose literal stands in no other file still stands in #1232's version (executed). Neither sibling touches a module or a check line this work edits. |
| **G10** `docs/the-record-layout.md` *A change writes fragments, never a shared file*, `:52-56` (read) | The diff changes check lines in `agents/tracer.md` and `skills/code-review/SKILL.md`, text an agent reads, so it owes a `changelog.md`. A change to an `agents/*.md` file ends that fragment with a `### Process changes` table, which the orchestrator writes with the fragment. |
| **G11** #1216 (executed: `gh issue view 1216`, open, `release: 0.28.0`); the latest release's `### Process changes` (executed: `gh release view`, one row, #1222's wait on a pull request's checks) | #1216 makes the pull request name each pin a design's operations will break. It is what meets the pins this work leaves out of scope (*Scope*, Out) at the next rewording. The process row bears on the orchestrator's wait, not on this frame. |
| **G12** `skills/settle/SKILL.md` *Rule changes* (read); `skills/settle/scripts/rule_changes.py#parse` (executed: `parse(<this file's text>, "docs")` from a `git clone --no-local` of the worktree at `6b8e2050`, and again after round 1 at `19957702`, each clone removed after its run) | `parse` returns the two `change` items with `errors=[]` and `unread=[]`. Each `from`, whitespace collapsed, stands exactly once in its section, and each target a `to` names is a file of the tree, at `19957702` (executed). The `from` of the first item carries the sentence before the check line because the same line closes two rules of *The run*, at `:428` and `:456`. |

## Scope

In:

1. The cases of group A (*The groups*) are ruled: each case that holds a listed assert is read whole, and each of its asserts is kept or removed by *The criterion*. A kept assert carries, on the comment line or lines directly above it, the fact it pins and who reads that fact. Where the literal sits in a tuple or table a loop asserts, the comment stands beside that entry. A case left with no kept assert is removed. A module left with no case is deleted.
2. The cases of group B are ruled the same way, except `tests/text/test_a_gate_that_fails_says_so.py`, which item 7 holds.
3. The cases of group C are ruled the same way.
4. The cases of group D are ruled the same way.
5. The three modules of G6 are deleted, in group B's phase. `agents/tracer.md:72` becomes `check: none reader: the orchestrator at each tracer report`. `skills/code-review/SKILL.md:97` becomes `check: tests/behaviour/test_a_probe_that_commits_says_so.py`. The comment at `tests/text/test_a_moved_rule_leaves_its_definition.py:602-603` drops `tests/text/test_absence_claims.py` and keeps the other module it names.
6. The case `tests/text/test_the_rules_have_one_owner.py#test_the_cap_counts_from_the_last_design_change` is removed in group A's phase, and `## Rule changes` moves `docs/the-review-record.md:428` to its reader (G5, G7).
7. `tests/text/test_a_gate_that_fails_says_so.py` stays whole in this change, and `## Rule changes` takes it off `docs/the-session-hooks.md:39` (G4). Before `seal pr-body` runs, the orchestrator files one successor issue, and the pull request body names it. The issue holds the module's deletion once the settle has written that change, its `.test_durations` row 5632, the citation at `tests/hooks/test_dispatch.py:14`, and whatever item 9 adds.
8. Each check line outside `docs/` that names a module a phase deleted, or whose named module keeps no case that reads the line's rule after the phase, is changed in place. The line names a target that reads the behaviour, or becomes `check: none reader: <who>`. The rule files outside the policy root are those `.github/scripts/rules.py#RULE_FILES` reads: `CLAUDE.md`, `CONTRIBUTING.md`, `agents/*.md`, `skills/*/SKILL.md`, `skills/*/orchestration.md` and `templates/*/*.md`.
9. A `docs/` check line other than the two of `## Rule changes`, whose named module the ruling would leave with no case that reads its rule, keeps the last such assert unchanged. The phase names the assert and the line in its `trail/phases/phase-N.md`, and the orchestrator adds both to item 7's issue, whose own frame states the line's change.
10. The rows of `.test_durations` for each removed case and deleted module leave in the commit that removes them, and the file stays one JSON object.
11. Each docstring or comment that states what a removed assert pinned, or that cites a deleted module, is rewritten in place to state what the code now holds (contract rule 19).
12. The work item's `changelog.md`, written by the last phase; the orchestrator writes its `### Process changes` table (G10).
13. A rehearsal of the settle, in group B's phase. In a scratch clone the crafter writes both `to` values into `docs/`, deletes `tests/text/test_a_gate_that_fails_says_so.py`, and runs `seal rules --check` and `git grep -n test_a_gate_that_fails_says_so -- . ':!seal/threads'`. The result, in `trail/phases/phase-2.md`, shows that item 7's list is whole.

Out, each with its reason:

- **Asserts the lister does not list, in cases that hold no listed assert**: a literal under four words, a literal reached through a name, a regular expression, a literal whose home is a template, `README.md`, `CLAUDE.md` or `CONTRIBUTING.md`. The class of a case pinning wording is unbounded in its spellings, so no method lists it whole (contract rule 12), and the issue scopes the work to *Command K5*'s list. Inside a case that holds a listed assert, every assert is in (item 1). What stays meets #1216 at the next pull request whose design breaks one, and the proofer at review (G11).
- **Every sentence under `docs/` other than the two check lines.** The policy sentence this work applies does not change (G1).
- **The deletion of `tests/text/test_a_gate_that_fails_says_so.py`** (G4, item 7).
- **A wider excuse in `.github/scripts/rules.py`** (`plan.md` A6).
- **The rows of `seal/follow-up.md`** (G8).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 Every listed assert is ruled | Given HEAD, when *The listing* runs over a scratch copy of HEAD, then each assert it prints stands with a comment above it naming a fact and its reader, or is in `tests/text/test_a_gate_that_fails_says_so.py`; and the phase records' kept and removed counts per module add up to the 506 asserts the listing printed at `361ed0cb` | the phase boundary per group, executed; the last phase for the whole |
| S2 Every check line resolves | Given HEAD, when `seal rules --check` runs, then it exits 0 | each phase boundary, executed |
| S3 No line names a deleted module | Given HEAD, when `git grep -n <module>` runs for each deleted module outside `seal/threads`, then it lists nothing and exits 1 | the phase that deletes it, executed |
| S4 The durations still parse | Given HEAD, when `.test_durations` is loaded as JSON, then it loads and holds no key of a removed case | each phase boundary, executed |
| S5 The rule changes parse | Given this file, when `skills/settle/scripts/rule_changes.py#parse` reads it with root `docs`, then it returns two `change` items, no errors and nothing unread, and each `from` stands once in its section | executed by the framer (G12); the pull request's chain check |
| S6 The settle's list is whole | Given a scratch clone with both `to` values written and the module deleted, when `seal rules --check` and the `git grep` of Scope item 13 run, then the first exits 0 and the second lists only the lines item 7's issue names | group B's phase, executed |
| S7 The narrow run passes | Given a phase's last commit, when the modules *The narrow run* gives for it run in one command, then each passes | each phase boundary, executed; the rest of the suite, the orchestrator's broad gate |
| S8 A kept assert pins a fact and a removed one pinned wording | Given the diff, when each kept assert's comment and each removed assert are read against *The criterion*, then each kept one names a fact of one of its kinds and its reader, and each removed one pinned a phrase of a rule | the proofer at review |

## Data & interfaces

### The listing

*Command K5*'s first and third lines, run at a commit `<C>` (executed at `361ed0cb` and `bf9efcba` by the framer):

```sh
S=<scratchpad>/1793542348-each-wording-pin-is-kept-or-removed/frame
mkdir -p "$S/tree"
git archive <C> | tar -x -C "$S/tree"
git show 48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md \
  | awk '/^cat > "\$S\/audit.py" <<.EOF.$/{f=1;next} /^EOF$/{f=0} f' > "$S/audit.py"
S="$S" python3 -I "$S/audit.py" pins -v
```

`audit.py#pins` lists each `assert` under `tests/` whose test holds a string literal `in` an expression, the literal at least four words, standing whitespace-folded in a file of `docs/`, `skills/` or `agents/`. Its rows are `path:line literal -> homes`, and its last line is the count. The directory goes once the run is read (contract rule 17).

### The criterion

An assert is kept where its literal is a fact a reader acts on, of one of these kinds:

- **A spelling a script or a parser matches**: a field name, a block or line keyword such as `reopens:` or `Verdict: sealed`, a routing answer, a template placeholder a reader such as `offered` parses, a marker.
- **A citation a reader resolves**: a path, a `path#unit`, a heading cited in italics, a contract rule number.
- **A command, flag or value a reader copies or runs**: a shell command, a `seal` subcommand, a `gh` call, a number a person waits on.
- **A program's output**: the right side reads what a script, hook or generator printed or wrote. It reads behaviour, and the lister lists it only because the same words stand in a rule file.

An assert is removed where its literal is a phrase of a rule's wording: its lead sentence, its grounds, its example, or a clause of it. Three shapes count as wording whatever their length: an assert that a check line names the asserting module itself, an absence assert that an old phrase is gone, and an assert that only locates the text a removed assert read. A literal holding a code span inside a sentence is wording unless the assert is about the span. Where the case keeps such an assert, its comment names the span as the fact.

### The groups

| Group | Modules | Listed asserts | Cases holding one |
|---|---|---|---|
| A | `tests/text/`: `test_the_rules_have_one_owner.py`, `test_broad_gate_rule.py`, `test_settle_reads_before_it_removes.py`, `test_the_handoff_before_round_one.py`, `test_a_segment_feeds_the_flow_log.py`, `test_review_axes.py` | 147 | 69 |
| B | the other 15 listed modules of `tests/text/`, and the 13 listed modules of `tests/skills/`, `tests/github/`, `tests/hooks/` and `tests/evals/` | 113 | 75 |
| C | `tests/behaviour/`: `test_waiver_decided_at_start.py`, `test_first_setup_asks_once.py`, `test_the_sealer_guarantees.py`, `test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `test_release_hygiene.py` | 129 | 52 |
| D | the other 17 listed modules of `tests/behaviour/` | 117 | 63 |

Group B's 28 modules and group D's 17 are the rows of *The listing* at `361ed0cb` under those directories less the modules named here (executed).

### The narrow run

Each phase runs, in one command at its boundary, the modules that read a path it changed, taken by `git grep -l` at its own base as `seal/threads/1793539662-the-wording-pin-module-leaves/frame/design.md` *The narrow run* took them (#1243's record, in the tree until the settle after 0.27.3). The kinds are its edited modules; `tests/github/test_rules.py` where a check line changed; the readers of a changed skill or agent file, by its path; the readers of `.test_durations` (at `361ed0cb`: `tests/behaviour/test_the_release_check_watches_what_ships.py`, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `tests/github/test_durations_union.py`, `tests/github/test_release_report.py`, `tests/test_censuses.py`); and, where it deleted a module, the modules that list tracked files or glob `tests/`. A module reading a changed path by another spelling is outside the list, which is why the list is a sample and the orchestrator's broad gate answers the rest.

## Rule changes

- change
  file: docs/the-review-record.md
  section: The run
  from: No person is asked mid-run.
    check: tests/text/test_the_rules_have_one_owner.py
  to: No person is asked mid-run.
    check: tests/behaviour/test_chain_hooks_hardening.py
- change
  file: docs/the-session-hooks.md
  section: Registration
  from: check: tests/hooks/test_dispatch.py tests/text/test_a_gate_that_fails_says_so.py
  to: check: tests/hooks/test_dispatch.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| each listed assert ruled wording, and each case left with no kept assert | the 506 rows *The listing* prints at `361ed0cb`, less the one in `tests/text/test_a_gate_that_fails_says_so.py` | nowhere: a phrase of a rule's wording is the proofer's to read for meaning (`docs/what-a-script-gates.md` *The checks*); a fact one of them carried stays as a kept assert of the same case (*The criterion*) |
| three modules | `tests/text/test_the_handoff_names_the_form_it_ran.py`, `tests/text/test_absence_claims.py`, `tests/text/test_a_probe_does_not_outlive_its_round.py` | nowhere: every assert of each pins wording (G6) |
| a check line's target | `agents/tracer.md` *An absence carries its search*, line 72 | `check: none reader: the orchestrator at each tracer report`, the party that receives the tracer's facts |
| a check line's target | `skills/code-review/SKILL.md` *Probes and regression tests*, line 97 | the line's other target, `tests/behaviour/test_a_probe_that_commits_says_so.py`, which reads rule 7's leavings |
| a citation of a deleted module | `tests/text/test_a_moved_rule_leaves_its_definition.py:602-603` | the comment keeps `tests/behaviour/test_a_probe_that_commits_says_so.py` |
| the round cap's case in the module the line names | `tests/text/test_the_rules_have_one_owner.py#test_the_cap_counts_from_the_last_design_change` | `tests/behaviour/test_chain_hooks_hardening.py#test_the_run_names_its_default_round_count_and_the_follow_up_file`, which stays and reads the cap's default count; `docs/the-review-record.md` *The run*'s line names its module (`## Rule changes`, G5, G7) |
| a check line's target, at the settle | `docs/the-session-hooks.md` *Registration*, line 39 | `tests/hooks/test_dispatch.py`, which reads the failure report the rule states (G7); the module itself leaves through the successor issue (Scope item 7) |
| duration rows | `.test_durations`, the row of each removed case and of each deleted module, the deleted modules' at 5864 to 5866, 5924, 5925 and 6071 | nowhere: the cases they price are gone |
| other check-line targets, docstrings and comments a phase's ruling makes false | the lines Scope items 8 and 11 reach | each phase names them in its `trail/phases/phase-N.md`; a removal the frame did not name is a divergence that record holds (`docs/the-reader-registry.md`) |

Framed 2026-11-01 by framer, before the build.
Reframed 2026-11-02 by framer, after round 1.
