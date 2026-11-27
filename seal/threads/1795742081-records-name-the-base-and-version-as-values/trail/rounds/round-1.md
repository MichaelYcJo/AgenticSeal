# Review round 1: 1795742081-records-name-the-base-and-version-as-values

```seal
target: 338204606 against origin/release/v0.39.2
```

The base is the release branch at `68bb3d5a9`, the merge base this round read. No earlier round stands, so nothing was carried: every coordinate below was opened at `338204606`. The work item's records were read whole at that commit: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`. No `pr.<lang>.md` stands, since `Commit and pull request language` is English. `seal/parity.json` is not declared.

## Findings

### 1. Clause R4 lets a value stated of "a release" stand, so a value of the open release passes the clause R1 refuses

```seal
severity: should
location: `skills/agent-contract/SKILL.md:228-231`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/design.md:80`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/changelog.md:3`
evidence: executed `git grep -n -F -e 'a release, a dated measurement' -e 'a named commit, a release' -- skills agents docs templates seal/threads/1795742081-records-name-the-base-and-version-as-values`; read `skills/agent-contract/SKILL.md:215-233`
```

Why it matters: every party that writes a record preloads rule 19, and this sentence decides which values stay. At `skills/agent-contract/SKILL.md:215-219` the paragraph refuses "the value of a state outside the work item's branch", and it names "the version a release carries" as an example. At `:228-231` it then lets stand "a value stated of a named commit, a release, a dated measurement, or a date or a cut the sentence names". A version is always stated of a release. So does a base: "release 0.0.5 merges into `release/v0.0.5`" is a value stated of a release, and it is the sentence of the issue's evidence that went false when the work moved to the next release. One reader takes "a release" as a moment and keeps such a sentence. Another takes R1's example and refuses it. The old count clause could say "a release" because a count stated of a release meant a release that had shipped. A value of the release still open is the state R1 is about.

Claimed: `frame/design.md:80` (R4) takes the moments "the rule's second paragraph names for a count and a universal", and `trail/phases/phase-1.md:9` says the sentence is stated once for the three. That holds, and it is how the count clause's "a release" reached the value. The search printed `skills/agent-contract/SKILL.md:229`, `frame/design.md:80`, `changelog.md:3`, and also `frame/design.md:12` and `:131`. Those two quote the old sentence in a dated *Grounding* row and in the *Removes* table, so the fix leaves them. The search is a sample under contract rules 12 and 19: a statement of the same exemption in other words escapes it.

```markdown
<!-- skills/agent-contract/SKILL.md, the sentence at :228-231 -->
names the file or the command that reads it at that time. A count, a
universal or a value stated of a named commit, a published release, a
dated measurement, or a date or a cut the sentence names is a claim about
that moment and stays. A line of the plugin's forms that a check reads by
value

<!-- frame/design.md:80, R4 -->
- R4. A value stated of a named moment is a claim about that moment and stays. The moments are the ones the rule's second paragraph names for a count and a universal, a named commit, a published release and a dated measurement, with a date and a cut the sentence names. A release still open is no moment. The sentence is stated once for the three.

<!-- changelog.md:3, the clause in the first item -->
and may state a value of a named commit, a published release, a dated measurement, a date or a cut.
```

### 2. R1's example "the version a release carries" refuses the `changelog.md` line that states the version move, which the frame keeps

```seal
severity: should
location: `skills/agent-contract/SKILL.md:215-219`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/design.md:54`
evidence: executed `git grep -n -i -E 'version moves to|moves the version' -- 'seal/threads/*/changelog.md'`; read `skills/agent-contract/SKILL.md:215-233`, `skills/implement/orchestration.md:380-390`, `docs/releasing/branch-and-release.md:30-40`
```

Why it matters: the work item that carries the version move writes the number into the version file in the commit that adds its `changelog.md` (`skills/implement/orchestration.md:380-390`). Its fragment says so in a line of the form "The version moves to 0.39.2.". At the target the search prints that line in the `changelog.md` of each work item that carried a move, from `1794465688-feature-prs-wait-on-the-macos-runner` to `1795736973-the-preflight-passes-where-a-round-is-owed`. `frame/design.md:54` keeps the line out of scope because "It states what its own commit writes to the version file, which is a state the work item's commits make". The rule does not carry that reason. Its paragraph lists "the version a release carries" among the states outside the branch at `:218` and names no moment the fragment line states. The next crafter that carries a move can drop the line, and the release notes then lose the version. Or a proofer raises it as a finding against a frame that kept it. Either reader acts on the rule as written. The fix puts the frame's reason in the rule, beside R5.

```markdown
<!-- skills/agent-contract/SKILL.md, after the sentence that ends "the `target:` line of a round record and of `guarantee.md`." -->
A value the work item's own commit writes is a state of its branch, not
outside it, and stays: the version that the work item carrying the move
writes to the version file and states in its `changelog.md`.
```

### 3. The work item's frame says, naming no moment, which files another work item changes, and one of the three it names is in neither that item's issues nor its frame

```seal
severity: should
location: `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/design.md:50`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/plan.md:16`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/plan.md:27`
evidence: executed `git grep -n -F -e 'changes those files' -e 'also changes' -e 'changes that file' -- seal/threads/1795742081-records-name-the-base-and-version-as-values/`; `gh issue view <N> --json body,comments` for 1624, 1628 and 1629, searched for `fold-and-reframe`, `fix-pass.md` and `orchestration.md`; `git show <commit>:seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md` and `frame/plan.md` at `762f284f7` and `c1563c7a4`, counted for `fold-and-reframe` with `grep -c -F`
```

Why it matters: acceptance row A8 (`frame/design.md:69`) asks that each sentence of these records stating another item's state names a moment or a role. Rule 19's new paragraph lists "what another work item has branched, framed or been ordered to do" among the states it governs (`skills/agent-contract/SKILL.md:218-219`). `frame/design.md:50` says "the work item for #1624, #1628 and #1629 changes those files", meaning `skills/implement/fix-pass.md`, `skills/implement/fold-and-reframe.md` and `skills/code-review/orchestration.md`. `frame/plan.md:16` says each citation "is reworded in a file the work item for #1624, #1628 and #1629 also changes", over the same three files. `frame/plan.md:27` says that work item "changes that file" of `skills/implement/orchestration.md`. *Scope* and *Alternatives considered* are not dated sections, so a reader holds these sentences against today.

On 2026-11-27 the three issues named `skills/implement/fix-pass.md` and `skills/code-review/orchestration.md`, and #1628 named "the orchestration files". None named `skills/implement/fold-and-reframe.md`. That work item's frame, committed at `762f284f7` and unchanged in that respect at `c1563c7a4`, changes `skills/implement/fix-pass.md` (*Scope* item 4), `skills/code-review/orchestration.md` (item 5) and `skills/implement/orchestration.md` (item 6). The count of `fold-and-reframe` in its design and plan was 0 at both commits. So `frame/design.md:50` and `frame/plan.md:16` state one file with no source. `frame/plan.md:27` is true of `762f284f7`, but it names no moment. `frame/plan.md:38` dates the rows of *Overlap with the release*, and these three sentences stand outside that table. `frame/plan.md:26`, "The work item for #1632 may change that file", is a hedged possibility and stays true either way, so the fix leaves it. The search is a sample under contract rules 12 and 19: a statement of the other item's work in other words escapes it.

```markdown
<!-- frame/design.md:50 -->
- `skills/implement/fix-pass.md`, `skills/implement/fold-and-reframe.md` and `skills/code-review/orchestration.md`, whose citations name "a count or a universal contract rule 19 refuses". Each stays true, and the party that reads it preloads or has opened the contract. The frame of the work item for #1624, #1628 and #1629, committed at `762f284f7`, changes `skills/implement/fix-pass.md` and `skills/code-review/orchestration.md` (its *Scope* items 4 and 5), and does not name `skills/implement/fold-and-reframe.md`.

<!-- frame/plan.md:16, the second cell's first sentence -->
The three citations above name "a count or a universal contract rule 19 refuses", which the rule would no longer state apart, so each is reworded, two of them in files the frame of the work item for #1624, #1628 and #1629 changes at `762f284f7`.

<!-- frame/plan.md:27, the second cell's last sentence -->
The template's placeholder is what the orchestrator fills, and the frame of the work item for #1624, #1628 and #1629 changes that file at `762f284f7`, in its *Scope* item 6
```

## Confirmations

What matched: rule 19's third paragraph holds clauses R1 to R5 of `frame/design.md:77-81` in that order (`skills/agent-contract/SKILL.md:215-235`), read sentence by sentence. The second paragraph's other sentences stand unchanged, and the sentence on the rule's reach ends the rule. That is as `trail/phases/phase-1.md:9` claims.

What matched: the heading at `skills/agent-contract/SKILL.md:193` is 87 columns wide, and the design's proposed wording is 96, against `LIMIT = 88` at `tests/behaviour/test_docs_line_wrap.py:43` (executed: `awk` length and `wc -c`). The reworded heading keeps the number, which `frame/design.md:75` allows. That is as `trail/phases/phase-1.md:7` claims.

What matched: the rule holds no value it forbids. Its examples are roles, and the form lines it names are the `Branch` row and the `target:` line (read). R5's two lines are the form lines a check reads that can hold a branch name: `lib/fields.py` reads the round block's `target:` and the verdict block's `target:` with a base word, and the run block's `run:` and the `original:` line with commits alone (read `lib/fields.py:126-220`). A commit is a named commit under R4, so the list is whole for what R5 is for.

What matched: the three placeholders each cite `contract rule 19` (executed: `git grep -n -F 'contract rule 19' -- templates/records` printed `templates/records/sdd-plan.md:23`, `:31` and `templates/records/sdd-routing.md:16`). Each asks for one thing. The routing placeholder asks the grounds to name the base, the version move and the merge order by decision and role. The *Overlap with the release* placeholder asks for the date or commit of another item's state and keeps *Merges first* undated. The *Operational impact* placeholder asks for no number but the phase and the file or command. `seal/follow-up.md:49` holds #1633's one row, naming the repository owner.

What matched: the crafter's open point that the `RULES` row reads each template whole holds by a read of `tests/text/test_the_rules_have_one_owner.py:434-444`. `names_the_owner in flat(*carrier)` is a substring of the whole file, so removing one of the plan template's two citations leaves the row green. *Scope* item 4 asks for one link per template, so the case holds what the frame states, and the gap at `templates/records/sdd-plan.md:23` and `:31` owes no finding.

What matched: the narrow modules of the plan's *Verified by* cell pass at the target, with `tests/behaviour/test_docs_line_wrap.py` beside them (executed, see `## Probes`). `gaps.md:7` labels the broad gate unverified and names the orchestrator, which is honest: the crafter ran `tests/text`, `tests/behaviour` and `tests/lib/test_routing.py` and no repository-wide lint.

What matched: the records hold to R1 elsewhere. `routing.md:16` and `:24` date the owner's answer and name the base by role. `frame/design.md` G7, G17, G19 and G20 name the date or the commit of each ref, version and release they state. `frame/plan.md:38` dates the rows of *Overlap with the release*, and `frame/plan.md:47` states the version move by decision and at `68bb3d5a9`. `changelog.md` states its counts of named releases and states no version move. `pr.md:1` quotes `frame/plan.md:47` word for word. The plan's lead sentence at `frame/plan.md:38` dates a table. R4 says "the sentence names", and this round reads a sentence that names the moment of each row it introduces as naming it.

What matched: `agents/sealer.md:118`, "That rule also says how a frame section dated to the framer's commit reads", follows "a sample under rule 12 and rule 19", so its nearest antecedent is rule 19, while the intended rule is the proofer's rule named two sentences before. This change does not make that worse. R4 speaks of what a sentence names, never of a dated section, and the old count clause offered the same misreading before it. The line is outside this diff, and no finding is opened on it here.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check, run once at the settled HEAD | `seal/config.json` `Broad gate` | the orchestrator's broad run |
| Whether the next release counts fewer findings of this class than #1632's comment counted | `seal/follow-up.md:49`, `frame/questions.md` Q1 | the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_every_agent_reads_the_contract.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_waiver_decided_at_start.py tests/lib/test_routing.py tests/behaviour/test_docs_line_wrap.py` | 247 passed, exit 0, at `338204606` |
