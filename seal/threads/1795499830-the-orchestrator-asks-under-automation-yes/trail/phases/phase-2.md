# Phase 2: 1795499830-the-orchestrator-asks-under-automation-yes

## What this phase found

### The frame, read against the tree before the build

The frame holds for this phase. At `4ae5d9f2b`, the coordinates it hands the build stand where it says (read): `skills/implement/orchestration.md:289` opens **`Automation` is a record, and no script decides anything on it.**, the first paragraph of *Orchestrator: what needs a person is asked in one batch, before the first edit* stands at lines 196 to 200, `hooks/ask-under-automation.py#MARKER` is `"No default:"`, and `.claude-plugin/plugin.json` reads `0.38.7`. S10's search printed `skills/implement/orchestration.md:289` alone (executed), the line phase 1 left for this phase. `git grep -n '0\.38\.7' -- ':!seal/threads'` printed `.claude-plugin/plugin.json:4` alone (executed), so `frame/design.md` G9 holds at HEAD.

### Decisions settled while building

- **The first passage keeps a sentence that the pull request's check decides nothing on the row.** The paragraph it replaces said no script decides anything on `Automation`, and the half that stays true is the check's. `lib/routing.py`'s comment on `AUTOMATION` and `parse`'s docstring, which phase 1 rewrote, say the same, so the skill and the code state one fact. Grounds: `frame/design.md` *Scope* item 4, and `skills/core/SKILL.md` *The rule a mechanism is kept against*, the sentence that a change rewrites the text it amends in place.
- **The first passage states the form by citation and does not spell the marker.** It says each question holds the marker `hooks/ask-under-automation.py#MARKER` gives, followed on the same line by the reason. Grounds: `frame/design.md` *Data & interfaces*, which names `MARKER` as the form's one home, and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, which keeps one value in one place.
- **The *Done when* sentence goes into the batch section's first paragraph, with one sentence of why.** The paragraph already lists what the orchestrator reads before the batch. The added why says that a *Done when* line is what the run must deliver, so a need the batch missed stops the run when the work reaches it. Grounds: `frame/design.md` *Scope* item 7, the second passage, and #1608's *Done when* item 3.
- **The paragraph on a rule that restricts agents stands after the paragraph on what a session cannot do for itself, and before *Once the batch is answered*.** Both earlier paragraphs say what the batch must hold. The new paragraph says where a restriction may come from, and the paragraph after it says where what surfaces later goes. Grounds: `frame/design.md` *Scope* item 7, the third passage, and #1608's *Done when* item 2.
- **The changelog fragment describes the whole work item, phase 1 included.** No earlier phase wrote `changelog.md`, and the release note is built from the fragment alone. Grounds: `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file*, and `agents/crafter.md` *Job*, which gives the fragment to the last phase.

### Departures from the frame

None.

### What this phase adds and how it was proved

The phase changes prose and one version string, and adds no behaviour a case can hold. Under `skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the row for prose changes applies, so no case was written and no `seal mutate` ran. `frame/design.md` S10 is read at review. What could fail was run (executed):

- S10's search, `git grep -n -i -E 'decides anything on it' -- . ':!seal/threads'`, prints nothing at `e130d7656` and exits 1.
- `git grep -n '0\.38\.8' -- ':!seal/threads'` prints `.claude-plugin/plugin.json:4` alone at `e130d7656`, and the same search for `0\.38\.7` prints nothing.
- `bin/test tests/text/test_the_rules_claude_md_names_have_one_home.py tests/behaviour/test_waiver_decided_at_start.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q`, the plan's command, passed 94 cases before the commit.

### Other statements of the reworded rules

The search for each rule's words is a sample (contract rule 12). Each line it printed stays true at `e130d7656` (executed, then read):

- *No script decides on `Automation`*: S10's search prints nothing. `git grep -n -i -E 'no script decides|decides nothing on (the|it)'` over `skills`, `agents`, `docs`, `lib` and `CLAUDE.md` prints `lib/routing.py:103` and `:209`, which phase 1 rewrote, and lines on other fields. `README.md:150` to `:157` and `docs/running/the-review-and-parity-arms.md:107` state what the orchestrator does under `yes` and why `no` is never written unasked, and stay true, as `frame/design.md` *Scope* says.
- *What the batch reads*: `git grep` for `each ticket`, `every ticket` and `every issue` prints the batch section alone. `skills/core/SKILL.md` *The first value: efficient development through the AgenticSeal process* and `README.md:127` to `:129` say the batch is asked once, before the first edit, for every issue, and stay true.
- *Where a rule that restricts agents comes from*: the rule is new. `git grep` for `real session`, `real CLI session`, `restricts what agents` and `run rule` over `skills`, `agents`, `docs`, `templates`, `README.md` and `CLAUDE.md` prints the two new passages alone. `skills/implement/orchestration.md` *What the answer writes* says `## Why this way` holds one or two sentences on the rows. The section already holds more, an issue line's answer with its coordinate (*Orchestrator: what needs a person is asked in one batch, before the first edit*), so that sentence states what it holds on the rows and stays.

### The boundary run

One `bin/test ... -q` over 24 paths passed 3,144 cases and skipped 10, at `e130d7656` with this record, `gaps.md` and `frame/plan.md`'s Status cell on disk (executed). The paths hold the three modules `frame/plan.md`'s phase 2 row names, two of them through `tests/text` and `tests/behaviour`, which `CONTRIBUTING.md` names as the tree-wide files. They also hold every other test file outside those two that names `orchestration.md`, `plugin.json` or `changelog.md` (`git grep -l` over `tests/*.py`), and every one that walks `skills/` or the records with a glob, a walk or `ls-files` (`tests/skills/test_rules.py`, `test_rule_changes.py`, `test_test_layout.py`, `tests/evals/test_rule_cases.py` and `tests/test_censuses.py`).
