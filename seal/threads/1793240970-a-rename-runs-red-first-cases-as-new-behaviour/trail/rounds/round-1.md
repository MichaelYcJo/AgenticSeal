# Review round 1: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

target: d1a06992 against origin/release/v0.24.1

## Findings

### 1. Contract rule 2 writes the phase-boundary set as the test modules that name a changed path, which leaves out the modules that import it or glob its directory

severity: should
location: `skills/agent-contract/SKILL.md:38-40`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/changelog.md:4`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/changelog.md:10`
evidence: read `skills/agent-contract/SKILL.md:38-40`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/frame/design.md:51-53`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/frame/plan.md:15-16`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/frame/design.md:171`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/gaps.md:12`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/trail/phases/phase-2.md:58-64`, `evals/behaviour/crafter/rule-crafter-rename/scaffold.sh:17-21`
verdict: fixed c545690b

Rule 2 is the one statement of the phase-boundary set. The crafter's step 7
and the verify skill's *Scope* row both cite it. Every crafter runs the set
it names at each phase boundary.

The frame names the set as the test modules that read a path the phase
changed: `frame/design.md:51-53` for step 7, `frame/plan.md:15-16`, and the
`## Removes` row at `frame/design.md:171`. The build writes "the test
modules that name a path the phase changed" at
`skills/agent-contract/SKILL.md:38-40`. The changelog repeats "name" at
lines 4 and 10. `gaps.md:12` records only where the set is written, not this
change of word.

The narrower word drops modules the old "the ones it touches" covered. A
test module reaches code by importing it, and an import names a module
rather than a path. The rename case's own fixture shows this.
`tests/test_textutil.py` reads `from src.textutil import shout`
(`scaffold.sh:17-21`). Read literally, it does not name the path
`src/textutil.py`.

The phase-2 record shows the word was too narrow for this branch as well.
It says the run covered modules "that name a path this work changed or read
every agent, skill, eval case or work-item record", "with the modules that
glob `agents/*` or `skills/*` added" (`phase-2.md:58-64`). The crafter went
beyond the rule's set to reach the modules that read the changed files.

```markdown
Run the tests for the slice you touched while you work, and at a phase
boundary, in one command, the cases the phase's plan row names and the test
modules that read a path the phase changed, whether they name it, import it
or glob the directory that holds it. The broad gate — the full suite, the
```

In `changelog.md`, change "the test modules that name a path the phase
changed" on line 4 and "the test modules that name a changed path" on line
10 to "read" in the same way.

answer: Holds. Rule 2 now names "the test modules that read a path the phase changed, whether they name it, import it or glob the directory that holds it", the frame's word with the three ways a module reads a path. The changelog's line 4 says the same, and its process row says "read a changed path". The verify *Scope* row and crafter step 7 cite rule 2, so they carry no copy to correct. With the word now the frame's, `gaps.md` needs no row for it. The narrow run, one `bin/test` command over the 72 modules that name a changed path or glob `agents/`, `skills/`, `evals/behaviour/` or `seal/threads`, passed 3984 with exit 0.

### 2. Crafter step 5 makes the rename branch depend on the whole phase, so a phase that renames one unit and adds another gives no instruction for the renamed one

severity: should
location: `agents/crafter.md:40-47`
evidence: read `agents/crafter.md:40-49`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/frame/design.md:57-62`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/frame/questions.md:23-26`, `seal/threads/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/changelog.md:3`
verdict: fixed c545690b

The frame applies the rule to each unit. "A phase that both renames and adds
behaviour owes the full cadence for the units that add behaviour and none
for the units it only moved" (`frame/design.md:57-62`). The question it
settled from the tree says the same (`frame/questions.md:23-26`), and the
changelog says it of a unit: "for a unit it only renamed or moved it names
the proving cases and the census in the phase record" (`changelog.md:3`).

Step 5 at `agents/crafter.md:40-47` has two conditions. The first applies to
a unit: "Where a unit adds behaviour". The second applies to the phase:
"Where the phase only renames or moves a unit". Read one way, the second
condition means a phase that does nothing but rename. Under that reading, in
a mixed phase step 5 says nothing about the renamed unit. It does not tell
the crafter to skip a new case for that unit, and it does not tell it to
record the proving cases and the census. Step 6 is written per unit ("A
unit only renamed or moved owes no run"), so steps 5 and 6 now apply to
different things. A mixed phase is the shape #1051 had, and this issue was
filed about that phase.

The repository's rule for text an agent reads (`CLAUDE.md`, *Repo rule: text
an agent or a check reads has one reading*) asks for a single reading.

```markdown
5. Read what the phase changes against the table in `skills/verify/SKILL.md`
   *The narrow command still has to be able to fail*. Build the phase as a
   vertical slice. Where a unit adds behaviour: each case first, seen red
   against the tree as it stands, then the code, then the case green. Where
   a unit is only renamed or moved, write no case new for it: the existing
   cases that prove it at the new name or path, and the census that table's
   row asks for, go into `trail/phases/phase-N.md`'s
   `## What this phase found`.
```

answer: Holds. Step 5 now reads "Where a unit is only renamed or moved, write no case new for it", so steps 5 and 6 both apply per unit. The same phase-wide condition stood in the sealer's `seen red` rule ("A phase whose record says it only renamed or moved"), so a renamed unit in a mixed phase had no rule there either. It now reads "A unit the phase record says was only renamed or moved claims no `seen red`", with the cases the record names for it re-run at HEAD. The changelog's sealer sentence and its process row now speak of a unit too. No case pins either sentence.

### 3. The rename case's old-name graders say the file no longer names shout, and pass a test file that still holds ShoutTest and test_shout

severity: should
location: `evals/scripts/rule_cases.py:504-512`, `evals/behaviour/crafter/rule-crafter-rename/graders/shape-old-name-gone-code.md:4`, `evals/behaviour/crafter/rule-crafter-rename/graders/shape-old-name-gone-test.md:4`, `evals/behaviour/crafter/rule-crafter-rename/graders/shape-old-name-gone-readme.md:4`
evidence: executed `python3 -c "import re; print(re.search(r'\bshout\b', 'class ShoutTest(unittest.TestCase):\n    def test_shout(self):\n        self.assertEqual(exclaim(\"hi\"), \"HI!\")'))"`
verdict: fixed c545690b

Each grader's body says "`<path>` no longer names `shout`"
(`rule_cases.py:509`). The case's own frame asks for the same thing. Its
scenario S1 reads "no file names `shout`" (`rule_cases.py:475`), and its
scope reads "`shout` is renamed `exclaim` everywhere it is named".

The pattern is `\bshout\b`, which is case-sensitive and bounded by word
characters. The fixture's test file holds `class ShoutTest` and
`def test_shout` (`scaffold.sh:17-30`). Neither one matches, because an
underscore is a word character and the class name starts with a capital S.
The probe gave `None` for a test file that calls `exclaim` but keeps both
old identifiers. So the test-file grader passes a rename that left the old
spelling in the case's own names. That is the half-rename the verify row's
census exists to catch.

None of the six measured runs left that shape: their traces show
`class ExclaimTest` and `def test_exclaim`. So tightening the pattern does
not touch the red and green this work recorded. `shape-proved-by` can keep
accepting either test name, because a phase record may cite the case by its
old name.

```python
        *(
            shape_regex(
                f"old-name-gone-{word}",
                {"source": "file", "path": path},
                r"shout",
                f"`{path}` no longer names `shout`, in any case or as part of a name.",
                flags="i",
                match="not_contains",
            )
            for word, path in RENAMED.items()
        ),
```

Then rerun `python3 evals/scripts/rule_cases.py` to regenerate the three
grader files. Also change the `shape-old-name-gone` row of
`frame/design.md` *Data & interfaces*, line 150, which names `\bshout\b`.

answer: Holds. The three graders now match `shout` with flag `i` and `not_contains`, and say "no longer names `shout`, in any case or as part of a name". `python3 evals/scripts/rule_cases.py` exited 0 and rewrote only those three grader files. Seen red with `node -e` running both patterns as the runner's JavaScript regexes. Over a test body keeping `class ShoutTest` and `def test_shout`, `/\bshout\b/` found nothing, so the old grader passed it, and `/shout/i` found a match, so the new grader fails it. Over the measured runs' shape, `class ExclaimTest` and `def test_exclaim`, neither pattern matched. No paid run was made. The changelog now says the case refuses `shout` in any case or inside a name. The row at `frame/design.md:150` is the orchestrator's to fold.

## Confirmations

confirms: none
The new case was seen red against the base's definitions, as phase 1 and
the changelog claim. Read: `base-rename.json` in the work item's scratchpad
directory names `rev` `1e82fd0a`. Both runs fail `shape-no-mutation`
("Bash called 1x (expected 0..0)" on run 0), and every other grader passes.
Both traces hold `seal mutate src/textutil.py --replace 'return
text.upper() + ...`, so the red comes from a real mutation run on the
renamed unit and not from a read that only names the command. The branch
side, `branch-rename.json` at suite `a2464236`, passes every grader on both
runs with zero matching Bash calls. `branch-slugify.json` passes every
grader on both runs. Its traces hold two `seal mutate` calls on run 0 and
one on run 1, so the arm that adds behaviour still mutates. The three
sides' `costUsd` add up to 3.59, as the `frame/questions.md` Q1 Status cell
says.

confirms: none
Phase 1 says moving the three closing graders into `crafter_closing`
(`evals/scripts/rule_cases.py:415`) left the four build cases byte for byte
the same. Executed: `python3 evals/scripts/rule_cases.py` in the round's
clone exited 0, and `git status --short` afterwards printed nothing.

confirms: none
The verify row's `check:` line at `skills/verify/SKILL.md:337` names a
directory that holds a case. Executed: `bin/seal rules --check` exited 0
with "all 267 check lines in 55 rule files hold".

confirms: none
The three clauses in the `## Removes` table of `frame/design.md` are gone
from the living text. Executed: `git grep -n -iE` for "the ones it
touches", "module at a time" and the new set's wording, outside
`seal/threads` and `docs/experiments`. The only hits were
`skills/agent-contract/SKILL.md:40`, which holds the new wording, and an
unrelated comment at `hooks/lib/config.py:594`. Rule 12's search for the old
cadence ("seen red", "case first", "unit you added", "every unit", "each
unit", "seal mutate") over `agents`, `skills`, `templates`, `docs`,
`README.md` and `CONTRIBUTING.md` found no other statement of the
unconditional cadence. The `CONTRIBUTING.md` and `docs/` hits concern new
cases or this repository's rebuilt modules.

confirms: none
A re-pointed pin turns red when its old sentence comes back, as phase 2
claims. Executed: `seal mutate` put "run one module at a time" back in
`agents/crafter.md`.
`test_crafter_finds_the_runner_before_inventing_a_command` failed, and the
command printed `red` and exited 0.

confirms: none
The narrow modules that read the changed paths pass at d1a06992. Executed:
one `bin/test` command over fifteen modules gave 460 passed and exit 0. The
modules were the four whose pins changed, the passage, moved-rule,
writing-style-heading, contract, broad-gate, review-axes, sealer and
chain-hooks modules, and the eval layout, rule-case, evaluated-wording and
mutation-check modules. `uvx ruff check` and `uvx ruff format --check` over
the five changed Python files exited 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck at d1a06992; the suite stays `unverified` in this round | the branch | the orchestrator, through `seal gate` |
| Whether `rule-crafter-count-words`, `rule-crafter-truncate` and `rule-crafter-is-palindrome` still pass against the branch's crafter, now that step 5 opens by reading the verify table | `evals/behaviour/crafter/` | the orchestrator, at the next crafter comparison |
| Whether the `crafter_closing` extraction collides with sibling #1047's edit of the same file. Phase 1 was asked to change no other line of the file (`trail/phases/phase-1.md:10-14`), and it moved the tail of `crafter_case` into a new function. The generated cases are unchanged | `evals/scripts/rule_cases.py:403-439` | the orchestrator, when the second of the two branches merges |
| Whether rule 2's "in one command" can hold when a plan row's *Verified by* names a paid eval run next to a pytest run, as this work's own row 1 did | `skills/agent-contract/SKILL.md:38-40` | the orchestrator |
| `shape-no-mutation` matches any Bash input that names `seal mutate` or `mutation_check.py`, including a read such as a grep of the crafter definition. None of the six runs made such a read, so whether a read alone turns the grader red is not measured | `evals/scripts/rule_cases.py:521-527` | the orchestrator, at the next crafter comparison |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/round-1/clone`, at d1a06992 | exit 0; every command below ran in this clone |
| `python3 evals/scripts/rule_cases.py`, then `git status --short` | exit 0; no file changed |
| `bin/seal rules --check` | exit 0; all 267 check lines in 55 rule files hold |
| `bin/test` over the fifteen modules named in the last confirmation, `-q` | exit 0; 460 passed |
| `uvx ruff check` and `uvx ruff format --check` over the five changed Python files | exit 0 for each |
| `bin/seal mutate agents/crafter.md --replace "type step 7's one command, never the whole suite" "run one module at a time" --tests "bin/test tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py -q -k test_crafter_finds_the_runner -p no:xdist"` | exit 0; `red`, the case failed against the old sentence, and the file was restored |
| `python3 -c` searching `\bshout\b` in a test body that keeps `ShoutTest` and `test_shout` | exit 0; printed `None` |
