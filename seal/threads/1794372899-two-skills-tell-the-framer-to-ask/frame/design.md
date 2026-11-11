# Design: 1794372899-two-skills-tell-the-framer-to-ask

## Grounding

The tree as read at `b578ffb77`, which differs from the branch's base `7b2b0fe6a` only by this work item's `routing.md` (executed, `git diff --stat 7b2b0fe6a b578ffb77`).

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The first value: efficient development through the workflow*, **Asking a person is the most expensive step.** (`:92`), and `agents/framer.md` *Rules*, **You ask nobody anything.** (`:138-143`) (read) | The rule the two skills contradict. `skills/feature-planner/SKILL.md:42` says "Get user confirmation before starting", and `skills/confidence-check/SKILL.md:47` says "Where any check is unsatisfied, say which, and ask" (executed, `grep -n`). The issue's coordinates `:44` and `:53` predate the files as they stand. A framer that follows either sentence breaks its own definition, so the sentences go. |
| G2 `skills/core/SKILL.md` *The rule a mechanism is kept against*: a mechanism stays only while its record of what it caught outweighs its cost, and a change removes in the same commit what stood on the old fact (read) | The owner's decision, fold and remove (the issue's *Decision*), is folded as made. Every text and case that names either skill changes in the commit that removes the skills (*Scope* items 2 to 5). |
| G3 Every reader of either skill (executed, `git grep -n -i -E 'feature-planner\|confidence-check' -- . ':!seal/threads/1794372899-two-skills-tell-the-framer-to-ask'`, which lists each line holding either name) | Outside the two skills: `agents/framer.md:101,103`; `README.md:276`; `README.ko.md:277`; `tests/behaviour/test_chain_hooks_hardening.py:1058,1080`; `tests/behaviour/test_the_set_a_work_item_always_has.py:102,162,282`; and `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:40`, another work item's record stating the commit it read. The issue named `README.md:282` and did not name `README.ko.md` or the comment at `:102`; both are re-taken here. `docs/` names neither skill (executed, the same `git grep` over `docs`, 0 lines). |
| G4 How often a framer opened either skill (executed, 2026-11-11: a `grep -l` over the 2,225 `.jsonl` transcripts under `~/.claude/projects/` for a `Skill` call naming either skill or a tool call whose `file_path` is either `SKILL.md`) | Two transcripts match, and in both the call is a maintenance session's `Edit` or `Write` of `skills/feature-planner/SKILL.md` (2026-10-21 and 2026-10-27). No transcript holds a `Skill` call naming either skill or a `Read` of either file. This agrees with the issue's finding. The premise for keeping the skills, a reader that uses them, does not hold (`frame/plan.md` *Alternatives considered* row 3). |
| G5 The framer's preload (executed, `wc -c` at `b578ffb77`; `agents/*.md` frontmatter read) | Every definition's `skills:` list names `core` and `agent-contract` alone, so neither skill is preloaded by any agent. The framer's preload is `skills/core/SKILL.md` 9,322 B, `skills/agent-contract/SKILL.md` 12,806 B and `agents/framer.md` 14,824 B, 36,952 B in all. The two skills hold 2,473 B and 3,067 B. |
| G6 What this work adds to that preload (executed: step 5, `agents/framer.md:96-103`, is 539 B by `sed -n` with `wc -c`; D1's text is 726 B; D1 applied to a `git clone --no-local` under the scratch directory gives `agents/framer.md` 15,011 B, and every line of D1 fits in 88 columns by `awk 'length > 88'`) | `agents/framer.md` grows by 187 B, and the framer's preload becomes 37,139 B. The core and the contract do not change. The release reads a KB as 1,000 B, so the work adds 0.187 KB to every framer spawn, and the plugin loses 5,540 B of skill text that no spawn preloaded (G5). |
| G7 `docs/running/the-agent-set.md:51-52` *One contract every agent receives, and one definition each*: "The readiness and decomposition questions belong to the frame, because they are about work nobody has started." (read) | The sentence stays true: D1 puts the readiness checks in the framer's own definition, and decomposition is `frame/plan.md`'s Phases table (D2). `docs/` is the policy root, since `seal/config.json` has no `Policy root` key (read), and the work's subject is a definition, two skills, the READMEs and tests, none of them in the policy root, so `## Rule changes` holds the no-change block. |
| G8 The issue's first *Done when* item, "No text the framer opens tells it to ask a person" (executed: in the scratch clone with D1 applied, `grep -n -i -E '\b(ask\|asks\|asking)\b\|confirm'` over `agents/framer.md`, `skills/implement/fold-and-reframe.md`, the three frame templates, `skills/writing-style/SKILL.md`, `skills/settle/rule-changes.md` and `skills/legacy-parity/SKILL.md`; each hit read in its section) | No hit tells the framer to ask. `agents/framer.md`'s hits state that it asks nobody. `skills/legacy-parity/SKILL.md:57-58` lies in *The migration config*, outside *The original's coordinates* that the framer opens, and already says "a reader that cannot ask returns `original not found`"; `:127` is a verdict word of *Parity review*. The other hits use "asks" of a rule or a script. After *Scope* items 1 and 2, the framer opens no text that tells it to ask a person. |
| G9 The cases that read the texts this work changes (read) | `tests/behaviour/test_chain_hooks_hardening.py#test_the_skills_row_lists_the_on_demand_skills_without_a_count` (`:462-479`) asserts that the on-demand sentence of each README edition's skills row names exactly the skills no agent preloads and nobody has to type, derived from the `skills/*/SKILL.md` glob. Removing the directories without *Scope* item 3 turns it red, so it pins that item. `tests/behaviour/test_docs_line_wrap.py#COVERED` holds `agents/framer.md` at 88 display columns (G6). `#skill_groups`, `#test_auto_firing_skills_declare_when_not_to_fire` and `#test_user_invoked_skills_do_not_carry_trigger_scaffolding` read the glob and need no change. `tests/text/test_review_axes.py:74` reads step 4 of `agents/framer.md`, not step 5. The batch sweep of `tests/behaviour/test_chain_hooks_hardening.py#batch_instructions` opens a window only at a batch phrase, and D1 holds none. |
| G10 `.test_durations:236,257,1238` name the three cases *Scope* items 4 and 5 remove (executed, `git grep -n` on the case names) | `CONTRIBUTING.md:180` says a work item never commits `.test_durations`, and `docs/releasing/release-checklist.md:142` has the release refresh it (read). The entries stay. |
| G11 The title's prefix, `skills/commit-pr-convention/SKILL.md` *Commit messages*, the table of kinds (`:133-141`) and the rule that the kind highest in the table wins (`:143-144`) (read) | `fix:` fits: the skills told the framer to do what `agents/framer.md` and the core already forbade (G1), the table's "a skill sentence that contradicted the policy it cites". The removal half is `refactor:`'s "a skill nobody used, removed" on G4's measurement, and `fix:` stands above `refactor:`. `feat:`'s "a thing removed that its users must now work around" would rank higher and fits only where an installation used a typed `/agentic:feature-planner` or `/agentic:confidence-check`; G4 measures the owner's machine alone, and no record of another installation's use reaches the tree. The reading for `fix:` rests on that premise. |
| G12 The issue's comments (executed, `gh issue view 1480 --json title,body,comments`, 2026-11-11) | The issue has no comment, so the body is the request. |
| G13 The release's other items (executed, `git log --oneline release/v0.37.3`: #1514, #1515, #1517 and #1518 merged at `7b2b0fe6a`; `gh issue view 1475`; `git branch -a --list '*1475*'` lists none) | #1471, #1472, #1473, #1474 and #1503 are merged at the base. #1475 is open, with no branch and no frame, and is read from its issue (`frame/plan.md` *Overlap with the release*). |

## Scope

In:

1. **`agents/framer.md` *Order of work* step 5 (`:96-103`) becomes D1's text.** The step's first sentence keeps its words. The sentence that sends the framer to the two skills, and "Most frames need neither.", give way to the three assumptions and the line that routes an unsettled one to `frame/questions.md`. No other line of the definition changes, and no `check:` line is added.
2. **`skills/feature-planner/` and `skills/confidence-check/` are removed**, each with its one file, `SKILL.md` (executed, `ls -la`: each directory holds that file alone).
3. **`README.md:276` and `README.ko.md:277`**: the skills row's list of on-demand skills loses `` `confidence-check` `` and `` `feature-planner` ``, and nothing else in the row changes.
4. **`tests/behaviour/test_chain_hooks_hardening.py:1055-1125`**: the comment that opens `:1055-1057`, `UTILITY_SKILLS`, `definitions_naming`, `test_each_utility_skill_is_callable_from_exactly_one_definition` and `test_the_skills_stand_down_for_whichever_definition_calls_them` go, and the module keeps two blank lines between the units on each side.
5. **`tests/behaviour/test_the_set_a_work_item_always_has.py`**: the comment paragraph at `:101-106` (the `#` separator line and the five lines on `feature-planner`) goes; the tuple `("skills", "feature-planner", "SKILL.md")` at `:162` leaves `INSTRUCTING`; `test_the_planner_writes_into_the_plan` (`:279-285`) goes.

Out:

- `docs/running/the-agent-set.md:51-52` keeps its text (G7).
- `.test_durations` keeps its three entries (G10).
- `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:40` keeps its text: the record states the commit it read (G3).
- `skills/legacy-parity/SKILL.md:57-58` keeps its text (G8).
- No case is added for D1 or for the removal (`frame/plan.md` *Alternatives considered* row 6).
- The installed plugin's copies under `~/.claude/plugins/cache/` are not the tree; the release replaces them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 No text names either skill | Given the build commit, when `git grep -n -i -E 'feature-planner\|confidence-check' -- . ':!seal/threads' ':!.test_durations'` runs, then it exits 1. | The command, at the build commit. |
| S2 Both skills are gone | `git ls-files skills/feature-planner skills/confidence-check` prints nothing at the build commit. | The command. |
| S3 The framer settles the three assumptions itself | `agents/framer.md` step 5 holds D1's text, and `git diff 7b2b0fe6a -- agents/framer.md` changes no line outside step 5. | Reading step 5 against D1, and the diff. |
| S4 The framer's preload grows by what D1 adds and nothing else | `wc -c agents/framer.md` reads 15,011 B where D1 goes in as written; the phase record states the figure and why where it differs. `git diff --stat 7b2b0fe6a -- skills/core/SKILL.md skills/agent-contract/SKILL.md` prints nothing. | The two commands at the build commit. |
| S5 No text the framer opens tells it to ask a person | G8's `grep` over the same files at the build commit finds no instruction to the framer to ask. | The command, and each hit read in its section. |
| S6 The READMEs list the skills that ship | Each edition's skills row names exactly the on-demand skills the glob derives. | `tests/behaviour/test_chain_hooks_hardening.py#test_the_skills_row_lists_the_on_demand_skills_without_a_count` (G9). |
| S7 The touched modules and the wrapped definition still pass | The narrow run of `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/text/test_review_axes.py` exits 0. | The crafter's narrow run. |

## Data & interfaces

No schema, payload or command changes. The interfaces that leave are the two skills, reached by name as `/agentic:feature-planner` and `/agentic:confidence-check` or by a session that matched either description.

**D1 The text of step 5**, as it reads after *Scope* item 1:

```
5. Judge: answer everything the tree can answer, by reading it, and by a
   probe where the answer is a behaviour, a time or an output (*A question
   a command answers is answered by running it* below). Settle three
   assumptions the same way before the frame rests on one: that nothing in
   the tree already does what the work adds, or could be extended to do
   it, found by searching for what it does and not for its name; that a
   library's API is the one its installed version holds, read there and
   not recalled; and that a bug's cause is shown, by the code read or by a
   probe that reproduces the bug, and not guessed. An assumption that
   neither reading nor a probe settles is a row of `frame/questions.md`.
```

The three assumptions are the ones the step named at the base, "a library nobody here has used, a component that may already exist, a cause still guessed at", and they are `skills/confidence-check/SKILL.md`'s checks 1, 3 and 5. Its last sentence leaves the row's `Who can answer` to *`questions.md` is the residue, not a collection*.

**D2 Where each part of the two skills stands after the work.** Each section of each file has a row, and confidence-check's five checks are split by where they land.

| Part | Where it stands after the work, or why it goes |
|---|---|
| feature-planner *1. Requirements Clarification*: what is requested and not, acceptance, constraints | `templates/records/sdd-design.md` *Scope* ("what is in, and what is explicitly out") and *User scenarios & acceptance* |
| feature-planner *2. Existing Code Analysis*: related code, patterns, reuse, what breaks | `agents/framer.md` step 4's wide reading; *Replacing a structure is weighed with keeping it*; `templates/records/sdd-plan.md` *Technical context*; reuse is D1's first assumption |
| feature-planner *3. Implementation Plan*: ordered tasks, files, risks | `templates/records/sdd-plan.md` *Phases* and *Alternatives considered*, whose failure scenarios carry the risks; the skill itself says its parallel markers do not survive into the file |
| feature-planner *4. Scope Lock*: in and out, then "Get user confirmation before starting" | In and out: *Scope*. The confirmation goes (G1): the approval is the orchestrator reading `plan.md` and spawning the build (`skills/implement/SKILL.md` *3. The SDD file set*) |
| feature-planner *Rules*: no gold-plating, the minimum path, unknowns flagged early, phasing past ten files | *Scope* holds only what is in; an unknown is a row of `frame/questions.md`; whether a work item is phased is `frame/plan.md`'s Phases table, and a file count as a rung was removed from the ladder before (`tests/behaviour/test_the_set_a_work_item_always_has.py:96-100`) |
| feature-planner *Where the output goes* and *Output Format*, its *Questions* line among them | `agents/framer.md` *Job* and `templates/records/sdd-plan.md`; questions go to `frame/questions.md` |
| confidence-check checks 1, 3 and 5: no duplicate, the API against the installed version, the cause understood | D1 |
| confidence-check check 2, *Architecture compliant* | Step 4's reading in the order of authority; a new dependency is named in `templates/records/sdd-plan.md` *Operational impact* |
| confidence-check check 4, *Working reference found* | Goes. An approach nobody has run is a behaviour, which *A question a command answers is answered by running it* settles with a probe; an outside example adds nothing a frame cites |
| confidence-check *What to do with the answers*: "say which, and ask", and no score | The asking goes (G1); D1's last sentence routes an unsettled assumption to `frame/questions.md`. No score was kept, so none is folded |
| confidence-check *Output format*, and "never report a check as satisfied because it was skipped" | A row's `Who can answer` cell (`skills/implement/SKILL.md` *3. The SDD file set*), and contract rule 4's `unverified` label |
| confidence-check *Skip When* | D1 applies where the frame rests on one of the three assumptions, so a frame that rests on none has nothing to settle |

## Rule changes

- nothing
  why: no document of the policy root, `docs/`, changes (G7). The work removes two plugin skills and rewrites a step of `agents/framer.md`, none of them in the policy root, and `docs/running/the-agent-set.md` keeps its sentence that the readiness and decomposition questions belong to the frame.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The feature-planner skill, whole (2,473 B) | `skills/feature-planner/SKILL.md` | Each part's place is D2. No framer opened it (G4) |
| The confidence-check skill, whole (3,067 B) | `skills/confidence-check/SKILL.md` | Checks 1, 3 and 5 land in D1, the rest as D2 gives. No framer opened it (G4) |
| The sentence that sends the framer to the two skills, and "Most frames need neither." | `agents/framer.md` *Order of work* step 5 (`:98-103`) | D1. This is the rule sentence D1 adds in return for the two skills (*A mark is not the answer to a blocked step*) |
| The two names in the skills row | `README.md:276`, `README.ko.md:277` | The skills no longer ship, so no row lists them |
| `UTILITY_SKILLS`, `definitions_naming`, and the two cases that read the skills' homes and stand-down clauses, with their opening comment | `tests/behaviour/test_chain_hooks_hardening.py:1055-1125` | The files they read are gone. Their docstrings record the defect each was written after, the 0.11.0 stand-down clauses naming an agent that no longer called the skills, and no later catch (read) |
| The tuple naming `skills/feature-planner/SKILL.md` | `tests/behaviour/test_the_set_a_work_item_always_has.py#INSTRUCTING` (`:162`) | The file is gone; the sweep keeps its other documents |
| `test_the_planner_writes_into_the_plan` | `tests/behaviour/test_the_set_a_work_item_always_has.py:279-285` | The file it read is gone. The fact it pinned stands in `skills/implement/SKILL.md` *3. The SDD file set*: "`plan.md`'s Phases table is the task list, and there is no other." |
| The comment saying why `feature-planner` is not in the file-count sweep | `tests/behaviour/test_the_set_a_work_item_always_has.py:101-106` | It states a reason about a file that no longer ships |

Framed 2026-11-11 by framer, before the build.
