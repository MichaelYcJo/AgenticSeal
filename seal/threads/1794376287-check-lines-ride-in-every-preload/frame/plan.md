# Implementation Plan: 1794376287-check-lines-ride-in-every-preload

## Technical context

The tree as read at `f47b1d5ae`.

The lines are read by one reader, `.github/scripts/rules.py`, through the globs of `RULE_FILES` (`:75-81`), and no agent acts on one (`frame/design.md` G7). The test units G8 lists anchor on a line in a preloaded file: some assert that a line is there, and the others end a slice at one. A commit that deleted the lines without *Scope* items 5 to 10 would leave those units red, so the deletion and the test edits go in one commit. D2 is the one case added. It is red at the base, which holds *Scope* item 1's lines, and green once they go, so it is written first and seen red against the tree as it stands (`skills/implement/SKILL.md` *2.*), then the deletion makes it green.

`rules.py` and `tests/github/test_rules.py` do not change (`frame/design.md` *Scope*, Out). After the work the reader still opens the six files, finds no line in them, and resolves any line written back as it resolves every other. D2 is what refuses such a line, in the suite that CI runs on every pull request.

Failure scenario of the chosen approach, in six months: a person changing a rule in an agent definition looks for the case that holds it, and finds nothing in the file to name it. `git grep` on the definition's path finds most cases, but the targets G13 lists as holding no definition name are not found that way: the contract's evals sit under another agent's directory, and the proofer's `tests/skills/test_settle.py` names no definition. That person opens `evals/behaviour/` and reads, which D1 tells them to do. That is the cost the owner accepted in the issue's *Decision*. A second failure: a definition's frontmatter changes shape, so `listed_skills` reads no skill and D2 reads the definitions alone. The module's shape case is already red on that change, because it asserts the `skills:` list.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Delete the lines (*Scope* item 1) and the sealer rule that stood only for its line (item 2); keep `RULE_FILES`; state the rule once in `skills/settle/rule-changes.md` (D1), held by one suite case over every preloaded file (D2) | The person of *Technical context*'s failure scenario spends a search to find a rule's case. D2 is a mechanism with no catch on the day it lands | Chosen. It is the owner's deletion as made (G1), and the case costs no preloaded byte. Why the case is kept is row 2's failure: the agents spawned in this repository until the release preload the installed 0.37.2 copies, which still carry the lines G5 counts, and suite cases asked for a line until this work (G8). `## Removes` names what goes in return for the case |
| 2. Delete the lines, state the rule in `skills/settle/rule-changes.md`, and leave its keeping to review alone | A crafter adds a rule to a definition and ends it with a check line, as many rules of its own preload end (G5). The suite passes, because the target resolves. The proofer preloads the same copies. Each spawn pays for the line until someone measures the preloads again | Rejected. A script answers this exactly, and `skills/core/SKILL.md` *The first value*, **Judgment is spent where meaning is the question, and a script answers the rest.**, gives such a fact to a script. The case's cost is one parametrized unit |
| 3. Have `rules.py` refuse any check line in a preloaded file | The grammar's reader gains a refusal keyed by path for a fact the suite can hold. `tests/behaviour/test_this_repository_passes_its_own_checks.py:93-112` plants a gone target in `agents/crafter.md` and counts one refusal per glob, so it breaks. `docs/running/what-a-script-gates.md:60`'s refusal column then changes, a rule change in the policy root. `chain_check.py` asks the same reader for a design's `to` lines, which never name a preloaded file | Rejected. It costs more than row 1 for the same catch |
| 4. Drop `agents/*.md` from `RULE_FILES`, and exclude the contract from `skills/*/*.md` (replace the structure) | A line written back is not read at all, so its target can rot and nothing names it. The contract needs an exclusion no glob has today, and `tests/github/test_rules.py:518-527`'s fixture moves. The premise that keeps the globs was checked: `skills/*/*.md` still covers the other skills' lines G7 counts, and `agents/*.md` costs nothing while it reads none (G7) | Rejected. Keeping the globs means a line written back is still resolved until D2 refuses it |
| 5. Keep the sealer rule *A missing or stale gate record earns what step 1 says.* without its line | Every sealer spawn pays for a pointer at step 1 and contract rule 2, which state it whole (G14) | Rejected |
| 6. An index file mapping each rule to its tests | A coordinate kept beside the tree, which `skills/core/SKILL.md` *The rule a mechanism is kept against* forbids | Rejected by the owner (G1) |
| 7. Strip the lines at the `dist` build | A second copy, and this repository's own spawns keep paying for the lines | Rejected by the owner (G1) |
| 8. Turn the presence assertions of G8 into assertions that each rule holds no line | Each restates D2 for one rule, and a rule no such case reads gets no pin | Rejected. D2 reads every preloaded file once |
| 9. State the rule in the contract, or in `skills/implement/SKILL.md` *2.* | In the contract every spawn pays for the rule that saves it bytes. Step 2 already sends a check line to `docs/` or to a design's *Verifiable how* cell, and cites *A rule has one shape* as the grammar (G15) | Rejected |
| 10. Limit D1 and D2 to the six files the issue names, leaving out `skills/core/SKILL.md` | The core is preloaded by every spawn as the contract is. A line added there costs the same and nothing refuses it. The core holds none today (G6), so including it costs nothing | Rejected. D2 derives the set from the definitions' `skills:` lists |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 11. Item 4's case is written first and seen red against the base; the other items follow, and all of them land in one commit; then the records | S1 to S5 and S7 by their commands at the build commit. S5 is D2 shown red at the base. S6 is the crafter's narrow run | `e9658c727` |

## Overlap with the release

The spawn names no other open work item of the release. It says this is the release's last agent item, and names #1471, #1472, #1473, #1474, #1503 and #1480 as merged into the base, where `git log --oneline release/v0.37.3` holds their commits from `af923302c` to `896f50cab` (executed). So no row meets this work.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|

## Operational impact

No migration, environment variable or dependency changes. After an update, each spawn of each agent preloads less, by the bytes `frame/design.md` D3 gives. `seal rules <file>` prints `(no check line)` under every heading of an agent definition and of the contract. `.claude-plugin/plugin.json` reads `0.37.3` at the base (read), and this work moves no version.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
