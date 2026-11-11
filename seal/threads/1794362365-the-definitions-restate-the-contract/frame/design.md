# Design: 1794362365-the-definitions-restate-the-contract

## Grounding

The tree as read at `0eaaad4e1`.

Each row is labelled `read` where the framer opened the text and `executed` where a command printed the fact. The branch's one commit after `9c6907942` adds `routing.md` alone (executed: `git diff --stat 9c6907942 HEAD`), so every coordinate below also holds at `9c6907942`, the commit both issues' "before" is measured at. #1474 took its coordinates at `ba4d85629` and #1503 at `8657297d5`, before #1471, #1472 and #1473 merged, and each one is re-taken here.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *A document is cut by who opens it and at which step* (read) | A party pays for every byte it preloads, on every spawn. An agent's own rules live in its definition, and the contract holds what the agents share. |
| G2 `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A fact has one source and every other place links to it. When fixes chase one mechanism's edge cases, the question is what the mechanism decides. A change rewrites the text it amends in place and removes, in the same commit, each check, comment and copy that stood on the old fact. |
| G3 `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* (read) | "A rule that would need a per-role exception is not universal": what is true of every agent is the contract's, and what is one agent's own is in that agent's definition. |
| G4 Contract rules 2 to 5, `skills/agent-contract/SKILL.md:34-71` (read) | Rule 2 has the hand-over label the suite `unverified` with the orchestrator as its answerer. Rule 3 has a declined instruction named in the hand-back in one line. Rule 4 gives the labels `executed`, `read` and `unverified`. Rule 5 makes a fact in a prompt a claim to open, the implementer's account a claim for a reviewer, and the handoff's facts things an implementer opens. A definition sentence that says one of these again is a copy; one that says where the answer lands for that agent, or what counts for it, is a narrowing. |
| G5 The statements of rule 5 in the definitions (read; the issue's coordinates printed at `ba4d85629` with `git show ba4d85629:<path>` and matched to HEAD) | `agents/crafter.md:115-119` *The handoff's facts are coordinates to open*: the copy is "open its coordinate before you build on it", and the narrowing is the handoff's shape and "where a claim flips on where it is measured, measure where the handoff says and say so". `agents/framer.md:149-151`: the copy is "opened at its coordinate", and the narrowing is the carrying into `frame/design.md` with a label and an answerer. `agents/proofer.md:73-74` (*Never*) and `:97-99` (*The implementer's account is a claim*) state the same prohibition twice; the narrowings are the list of what the account is and the record's form, *claimed X; `a.py:41` does Y*. `agents/sealer.md:149-152` (*Never*) repeats the Job's "never an agent's word and never the summary in the prompt that spawned you" (`:26-28`); the narrowing is which records are claims for the sealer. |
| G6 The statements of rules 2, 3 and 4 in the definitions (read) | `agents/crafter.md` step 10 (`:65-74`) spells out the labels, the suite's label and its answerer, and the declined instruction's line, and repeats the account its own rule asks for ("each part's method and what it listed and each statement named for the orchestrator"); `:86-87` and `:164-165` point at step 10 for the labels. `agents/proofer.md:168-171` restates rule 3's refusal, and its narrowing is the row of `## Not judged`. `agents/sealer.md:138-139` spells out the labels. `agents/framer.md` step 8 (`:108-110`) cites rule 4 and says what counts as `executed` for a framer, which is a narrowing and stays. |
| G7 The scratch statements (read; executed: `git grep -n -i scratch -- agents skills docs templates README.md`) | These definitions state the shared-scratchpad reason and a directory: `agents/crafter.md:100-109`, `agents/proofer.md:89-95`, `agents/framer.md:156-158`, and `agents/sealer.md:167-168` with the directory alone. Contract rule 21 names `<scratchpad>/<work-item-id>/` at `:216-219`, for the removal. `agents/tracer.md` names no directory, although its probe is bound by rule 7 (`:66-67`). `skills/code-review/orchestration.md:385` and `:453` name the orchestrator's files, and `skills/verify/SKILL.md:277-285` the capture example; none of them states a removal. |
| G8 Every sentence that tells a party to remove scratch files (executed: `git grep -n -i -E 'remov\|delet\|clean ?up\|is gone\|are gone\|gone before\|leaves nothing\|rm -rf\|leftover\|leavings' -- agents skills`, scripts excluded, each hit read; the same over `README.md`, `README.ko.md` and `docs`) | Under `agents/` and `skills/`: `agents/crafter.md:106-108`; `agents/framer.md:164-165`; `agents/proofer.md:187-189`, whose probes run in the clone, which stands under the round's scratch directory; `agents/sealer.md:174`; contract rule 7 (`:90-93`, "a scratch clone, a virtual environment"), rule 17 (`:183-188`) and rule 21 (`:216-219`); `skills/code-review/SKILL.md:114` and `:117-118`; `skills/implement/orchestration.md:31-32`. Outside them: `README.md:377-378`, `README.ko.md:374-375`, and `docs/running/the-agent-set.md:140-142`. #1503's *Change* names some of these, and its *Done when* asks the whole list. |
| G9 The runner statements (read; executed: `git grep -n -i -E 'wrapper\|contribution guide\|runner' -- skills/verify/SKILL.md skills/code-review/SKILL.md skills/implement/SKILL.md`) | `agents/crafter.md:156-162` and `agents/proofer.md:176-185` share one clause of 14 words, "a wrapper in `bin/`, or whatever the contribution guide names first", and "cheap on the second call". No skill either agent opens states how a runner is found. `docs/running/the-run.md` *The handoff* states the orchestrator's half. `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:360-369` holds that both definitions carry the generic shape, and `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:706-718` pins a different sentence on a coverage probe in each. |
| G10 The test-group statements (read; executed: `git grep -n -i -E 'duplicate check\|layout --pairs\|its group\|covers nothing' -- skills docs agents templates`) | `agents/crafter.md:121-126` says what the builder does with a new case, and `agents/proofer.md:158-164` says what the reviewer finds. They share the definition of the group, 17 words, and the name of `seal layout --pairs`. No skill and no policy document states either. `tests/text/test_a_moved_rule_leaves_its_definition.py:408-412` pins the crafter's clauses. |
| G11 The repeats inside `agents/crafter.md` (read) | Step 4 (`:40-41`) and the rule at `:111-113` state the same stop. The rule at `:172-176` repeats the Job (`:19-21`), step 8 (`:55-61`), and `skills/implement/SKILL.md` *3. The SDD file set* (`:290`, `:314-317`), which the crafter opens at step 1 and which holds "every departure from the frame, a removal the frame's `## Removes` did not name among them". "A unit only renamed or moved owes no run" stands at step 6 (`:50-51`) and in the mutation rule (`:136-138`); step 5's sentence (`:46-49`) says something else, what such a unit owes the phase record, and stays. `:204-206` tells the crafter that merging is the user's act, and rule 6 already withholds a push and a pull request from every agent, so the crafter has no act the sentence governs. |
| G12 `agents/sealer.md` step 2 and the descriptions (read; executed: `awk` over each `description:` block, piped to `wc -c`) | Step 2 says at `:74-78` that the part of the body above the heading is `pr.<lang>.md` and then `pr.md`, and says it again at `:81-86` in the sentence that lists what the sealer reads. The descriptions hold 217 B (crafter), 391 B (framer), 215 B (proofer), 583 B (sealer) and 270 B (tracer); the sealer's lists its own steps, which its definition holds. #1478 wrote "`pr.<lang>.md`'s renderings in the commit language" into step 2 one release ago (executed: `gh release view --json tagName,body`, tag `v0.37.2`, *Process changes*), and that clause stays. |
| G13 The pins on the sentences this work changes (read) | `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py` pins the five directory spellings, the words "share" and "scratchpad" in three definitions' *Rules*, and rule 21's removal clause (`:122-137`). `tests/text/test_a_moved_rule_leaves_its_definition.py` pins "whether that label is honest", "a row of `## Not judged`" and "so it goes through the `Edit` or `Write` tool (rule 9)" in the proofer (`:323-325`), "the account the rule … asks for" and "a leftover for `seal/follow-up.md`" in the crafter's step 10 (`:533`, `:670`), and holds every definition under a run of `passages.py#WINDOW` words shared with a contract section (`:161-176`) and the widest kept run at 10 words or fewer (`:178-223`). `tests/text/test_broad_gate_rule.py` pins "rule 2" and "rule 3" in the crafter (`:57`) and "goes in as a row of `## Not judged` with the caller" in the proofer (`:131`). `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:770-789` pins the lead and "rule 2" of the crafter's broad gate rule. `tests/behaviour/test_the_sealer_guarantees.py:189-217` pins "the part of the body below the line" and "request body above that line, its first part" in step 2, and "the orchestrator's part of the pull request body" in the sealer's *Never*. `tests/behaviour/test_a_probe_that_commits_says_so.py` pins "rule 7" and "rule 9" in the proofer, "leaves nothing behind (rule 7)" in the tracer and "Contract rule 7 is about leavings, not files" in `skills/code-review/SKILL.md`. `tests/text/test_the_agent_contract_holds_the_universal_rules.py:65-68` pins rule 21's command forms, the `"${VAR:?}"` form among them. No file outside `agents/` cites a lead this work rewrites or removes (executed: `git grep -n -F` on each lead, `seal/threads` and `agents` excluded). |
| G14 Where the removal came from, and what it has cost (executed: `git log --oneline -S'is removed in one \`rm -rf\`' -- skills/agent-contract/SKILL.md` prints `54880ec37` alone; read: issue #1503) | #1460 (`54880ec37`) wrote rule 21 after "19 of 21 permission prompts in a week came from two command shapes the parser cannot read, an rm on a variable path and a zsh expansion flag", and gave the crafter its own directory after a crafter removed the scratchpad twice (#1445). One release later a crafter closed a phase with a loop of `rm` on a variable path, and the run waited for the owner (#1503). The removal is the one step of a hand-back that needs the command shape Claude Code holds most readily. |
| G15 What a second clone into a standing directory does (executed: a probe under the frame's scratch directory made a repository, cloned it with `git clone --no-local` into a directory, and cloned again into the same directory) | The first clone exited 0. The second exited 128 with "fatal: destination path … already exists and is not an empty directory". Once nobody removes a clone, a second sealer spawn of one work item fails at `at-base/`, and so does a proofer respawned for a round or a framer spawned again for a fold, unless the rule says what an agent does where its directory already stands. |
| G16 Sizes at HEAD (executed: `wc -c`) | `agents/crafter.md` 11,411 B, `agents/framer.md` 14,946 B, `agents/proofer.md` 10,999 B, `agents/sealer.md` 11,454 B, which is 48,810 B for the four definitions #1474 measures; `agents/tracer.md` 2,894 B; `skills/agent-contract/SKILL.md` 12,364 B; `skills/core/SKILL.md` 9,322 B. |
| G17 The texts of *Data & interfaces*, measured (executed: the probe of G15 read the files, put T1 to T21 in place of the text each replaces, matching each old text once with runs of whitespace collapsed, and printed the sizes) | With the texts in place as phase 1 built them at `39efee911` (executed: `wc -c`): crafter 10,215 B, framer 14,824 B, proofer 10,763 B, sealer 11,058 B, which is 46,860 B for the four, 1,950 B less; the contract 12,779 B, 415 B more. The probe measured the texts unwrapped and with the longer headings of rules 7 and 17, and read 46,807 B and 12,819 B. The longest run of words a definition then shares with a contract section is 10, the sealer's with rule 15, which stands at HEAD and which this work does not edit. |
| G18 The ten-word census #1320 used (read: `git show v0.30.1:seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/frame/design.md`, *D6 The measurement*, and its `trail/phases/phase-4.md`; executed: the probe of G15, written to D6's method) | The probe gave #1320's recorded reading in every cell at both commits that work item measured: 934 of 11,209 at `0c68b9933` and 754 of 10,733 at `20e140537`. So it is the same census. At `9c6907942` it reads: crafter 274 of 1,775 words, framer 140 of 2,391, proofer 151 of 1,733, sealer 102 of 1,794, tracer 26 of 442, the contract 90 of 2,048, the core 133 of 1,595, all 916 of 11,778. With T1 to T21 in place it reads: crafter 254 of 1,592, framer 140 of 2,369, proofer 141 of 1,695, sealer 81 of 1,727, the contract 90 of 2,133, all 865 of 11,553, as phase 1 measured it at `39efee911` with the headings T1 and T2 give. The probe ran three times, twice more than rule 7 asks: once more after the contract's texts were shortened, and once more to read the two old commits from the object store after a clone could not check `20e140537` out. Its directory is removed. |
| G19 The policy in force (read: `docs/README.md`, `docs/running/the-agent-set.md`; executed: the `## Rule changes` block of every `frame/design.md` under `seal/threads/` printed) | One paragraph of the policy root states the scratch rule: `docs/running/the-agent-set.md` *What each party writes, and when*, `:134-143`, which says the name "lives in the definitions" and that one directory per work item and round "lets the agent that made a leaving say every one of them is gone". No unsettled design changes that document. This work's subject is the plugin's agent texts, so the paragraph changes through *Rule changes* below. No policy document states a copy of rule 3, 4 or 5 that this work touches. |
| G20 `seal/follow-up.md` (read) | Both tables are empty, so no row waits on this work. |
| G21 The issues and their comments (executed: `gh issue view 1474 --json title,body,comments` and the same for 1503, 2026-11-11) | Neither issue has a comment. #1474's *Done when* asks that each coordinate hold "a citation or a narrowing of that agent's own, and nothing else", and that the definitions G16 sums be at least 1.5 KB smaller, "measured with the 10-word census #1320 used, before and after". #1503's asks that no text under `agents/` or `skills/` tell an agent or the orchestrator to remove its scratch directory or the files in it, and that the naming sentences of #544, #1047 and #1445 still stand with their case green. |
| G22 How this release reads a KB (read: `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/frame/plan.md` *Judgments of the run*, row 1) | A KB in a *Done when* is 1,000 B, so 1.5 KB is 1,500 B. |
| G23 `routing.md` (read) | It stands, declares a framer and a crafter under `agentic`, names the branch, and says the two issues are built in one work item. |
| G24 The release's other open items (executed: `gh issue view` for #1480 and #1475; `git branch -r` lists no branch naming either) | `frame/plan.md` *Overlap with the release* reads each against this work. |
| G25 The version (executed: `grep '"version"' .claude-plugin/plugin.json` printed `0.37.3`) | The release's version move landed with #1471, and this work takes none. |

## Scope

In:

1. **Contract rule 17, rewritten in place as T2.** It becomes the one statement of the scratch rule: where an agent's files outside the working tree go, why the name carries the work item, what an agent does where its directory already stands, and that no agent removes the scratchpad, a scratch directory or a file in one. It keeps the stopping of processes by PID, the ban on a glob delete in a shared directory, and the report of a leftover. It loses the recording of file paths and the removal by that record.
2. **Contract rule 7, its heading and two sentences, rewritten in place as T1.** What stands under the scratch directory stays, and everything else a probe made still goes.
3. **Contract rule 21 loses its scratch-removal sentence and the second target of its `check:` line (T3).** The `rm` sentence with the literal path and the `"${VAR:?}"` form stays.
4. **`agents/crafter.md`.** Step 4 takes the narrowing of the rule *A declared frame that is absent stops the build*, and that rule goes (T4). Step 6 loses its second sentence (T5). Step 10 cites rules 2, 3 and 4 and its own rule (T6), and the *Never* bullet and the broad gate rule that pointed at step 10 for the labels point at the rules (T7, T10). The scratch rule keeps its directories and cites rule 17 (T8). *The handoff's facts are coordinates to open* becomes T9. The rules *Each phase closes with its record* and *The chain ends at a pull request, never a merge* go.
5. **`agents/proofer.md`.** The scratch rule keeps its directory and the clone's path and cites rule 17 (T11). The *Never* bullet on the implementer's account goes, and the rule *The implementer's account is a claim* takes its list and cites rule 5 (T12). The broad gate rule cites rule 3 for the refusal and keeps the row of `## Not judged` (T13). The probe rule loses its removal clause (T14).
6. **`agents/sealer.md`.** The description says when to spawn and what comes back (T15). Step 2 states once what the first part of the body is (T16). Step 7 cites rule 4 (T17). The *Never* bullet cites rule 5 and keeps the records that are claims (T18). The rule on a `seen red` cites rule 17 and loses "Remove the clone once its runs are done." (T19).
7. **`agents/framer.md`.** The sentence on a fact in prose cites rule 5 (T20). The probe rule cites rule 17, keeps its directory, and loses the shared-scratchpad reason and "The directory is gone before you hand back (rule 17)." (T21).
8. **`skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*.** Step 1 (`:31-32`) loses "and the removal of its scratch files", and step 2 gains the one removal the work keeps: the orchestrator removes the work item's scratch directory once, after the pull request opens (T22; `frame/plan.md` *Judgments of the run*, the row on the owner's decision).
9. **`skills/code-review/SKILL.md` *Probes and regression tests*.** The Probe row and the paragraph under the table send the reader to contract rule 7 for what is deleted and what stays (T23).
10. **`README.md:377-378` and `README.ko.md:374-375`** say that no agent removes its directory or the scratchpad, and that the orchestrator removes the work item's directory once the pull request is open (T24).
11. **`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`.** The cases on the crafter's, the proofer's and the framer's definitions keep their directory spellings and lose the "share" and "scratchpad" clause, which moves to a case on contract rule 17 with the spelling `<scratchpad>/<work-item-id>/<leaf>/`. The case `test_rule_21_removes_the_agents_directory_and_never_the_scratchpad` goes. One clause holds the removal form out: `rm -rf` stands in no section of the contract and in no agent definition. The module's docstring and each case's docstring are rewritten to the facts at HEAD. Each changed or added clause is seen red as rule 15 asks: the rule 17 clauses with their sentence deleted, and the `rm -rf` clause against rule 21 as it stands at `9c6907942`. The crafter reads the module as its group first, as its own rule asks.
12. **The cases that pin a sentence this work rewrites** keep their pins, because each text of *Data & interfaces* holds the pinned words (G13). Where the crafter's narrow run shows one that does not, the case changes with its sentence in the same commit, and the phase record names it. The pin on the tracer's sentence is one: it changes with T25 (item 17). `.test_durations:5786` names the case item 11 removes, and the crafter reads `tests/censuses.py` for what that file owes.
13. **The measurement.** The last phase record holds `wc -c` of the definitions G16 sums and of the contract at `9c6907942` and at the work's last code commit, and the census of G18 at both, taken with a probe written to D6's method that first reproduces G18's reading at `9c6907942`. `changelog.md` carries the figures at the work's last code commit. A later commit of the branch that changes a measured file or the census's corpus, a fix or a merge of the release branch among them, has both taken again at the new HEAD; after such a merge the "before" of each is the merged release commit, so that the difference stays this work's own.
14. **The work item's `changelog.md`**, with its `### Process changes` rows: where the scratch rule stands, that no agent removes scratch files, that the orchestrator removes the work item's directory once after the pull request opens, what an agent does where its directory stands, and that a definition cites rules 2 to 5 where it restated them.

Decided, and nothing is built for it except where the item names a text:

15. The runner rules, `agents/crafter.md:156-162` and `agents/proofer.md:176-185`, keep their text (`frame/plan.md` *Alternatives considered*, row 5).
16. The test-group rules, `agents/crafter.md:121-126` and `agents/proofer.md:158-164`, keep their text (`frame/plan.md` *Alternatives considered*, row 6).
17. `agents/tracer.md` names no directory, and rule 17 gives an agent whose definition names none its own name as the leaf. Its sentence on a probe repeats rule 7's words as they stood before T1, so it takes T25, and the case `test_the_fact_finder_points_a_probe_at_rule_7` and the docstring of `tests/behaviour/test_a_probe_that_commits_says_so.py` follow in the same commit, the changed clause seen red as rule 15 asks (round 1, finding 1).
18. `agents/framer.md` step 8 keeps its sentence on rule 4 (G6).
19. Each definition names its directory by the whole path, not by the bare leaf (`frame/plan.md` *Alternatives considered*, row 4).
20. Rule 17 takes no `check:` line (`frame/plan.md` *Alternatives considered*, row 9).
21. No eval, hook, check script, gate or mark is added.

Out:

- Every `check:` line except the one target item 3 removes. #1475 deletes the lines of the six preloaded files.
- `agents/framer.md` step 5, which #1480 rewrites.
- The sentences #1472 and #1477 wrote: the crafter's rule *Before you hand back…* and the proofer's *Every round reads…*, with the proofer's sentence on a fix's account.
- `skills/code-review/orchestration.md:385` and `:453` and `skills/verify/SKILL.md:277-285`, which name scratch files and state no removal (G7).
- The records of other work items under `seal/threads/` that quote a sentence as it stood. They state the commit they were written at and leave at the settle.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The definitions #1474 measures are at least 1,500 B smaller | Given `agents/crafter.md`, `agents/framer.md`, `agents/proofer.md` and `agents/sealer.md` after the work, when their bytes are summed, then the sum is 47,310 B or less, against 48,810 B at `9c6907942`, or 1,500 B under the "before" *Scope* item 13 gives after a merge | `wc -c` of each at both commits, in the last phase record |
| S2 The census is taken before and after | Given `9c6907942` and the work's last code commit, when the census of G18 runs on each, then the first run gives G18's reading at `9c6907942` in every cell, and both readings stand in the last phase record with the commit each measured. The issue sets no bound on the census, and S1 holds the bound | *Scope* item 13 |
| S3 Each coordinate #1474 names holds a citation or that agent's own narrowing | Given the sentences G5, G6, G11 and G12 name, when each is read beside the contract rule or the step it repeated, then it cites that rule or step by number, or says only what is that agent's own, or is gone with a *Removes* row | review reads T4 to T21 against rules 2 to 5 and against *Removes*; `git grep -n 'read. or .unverified' -- agents`, where each `.` stands for a backtick, prints nothing, against two lines at `9c6907942` |
| S4 The scratch rule is stated once | Given the contract and every definition after the work, when the reason a scratch directory carries the work item is looked for, then rule 17 alone states it, and each definition G7 lists with a directory names it and cites rule 17 | `git grep -n -i 'share one scratchpad' -- agents skills` prints a line of `skills/agent-contract/SKILL.md` alone; the cases of *Scope* item 11 pass |
| S5 No text tells a party to remove scratch files | Given `agents/` and `skills/` after the work, when the search of G8 runs again, then no hit tells an agent to remove its scratch directory or a file in it, and the one hit that tells the orchestrator to is T22's sentence in `skills/implement/orchestration.md`, the removal the owner decided; `README.md`, `README.ko.md` and the *Rule changes* operation say the same | the `git grep` of G8, each hit read, in the phase record; the `rm -rf` clause of *Scope* item 11 passes |
| S6 The naming sentences of #544, #1047 and #1445 stand | Given those definitions after the work, when their *Rules* are read, then each holds its directory as the module's constants spell it: `round-<n>/clone` and `round-<n>/`, `frame/`, `phase-<n>/` and `fix-<n>/`, and `at-base/` | `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, the crafter's narrow run |
| S7 A second spawn of one work item does not fail on a standing directory | Given a scratch directory an earlier spawn left, when an agent of the same leaf starts, then rule 17 tells it to leave that directory and take the same leaf with `-2`, or the next number free | read: T2; the rule 17 case of *Scope* item 11 holds the clause |
| S8 A probe in the working tree is still deleted | Given a crafter's `test_tmp_*` file in the branch worktree, when the crafter hands back, then rule 7 still has it deleted, and a worktree, a branch or a checkout a probe made still goes | read: T1; the `shape-no-probe-left` graders under `evals/behaviour/crafter/` read the same fact and are not run here |
| S9 The contract grows by 500 B or less | Given `skills/agent-contract/SKILL.md` after the work, when its bytes are counted, then it holds 12,864 B or fewer, against 12,364 B at `9c6907942` | `wc -c skills/agent-contract/SKILL.md` |
| S10 The cases that read the edited files hold | Given the edits, when the narrow cases that read any text *Scope* items 1 to 10 edit run, then they pass | the crafter's narrow run, with the modules G13 names, `tests/text/test_every_agent_reads_the_contract.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py` and `tests/behaviour/test_docs_line_wrap.py` among them; the broad gate is the orchestrator's |
| S11 Nothing else changes | Given the branch's diff outside `seal/`, when it is listed, then it holds the files *Scope* items 1 to 12 and 17 name and no other | `git diff --stat 9c6907942...HEAD -- ':!seal/'` |

## Data & interfaces

No script, form, field, template, hook or eval changes. The work is the texts below, each written as it will stand, to be wrapped as its file wraps. A text marked "in place of" replaces exactly the quoted words.

### The contract

**T1, rule 7.** The heading becomes ``## 7 A probe is named `test_tmp_*`, run once, and leaves nothing outside your scratch``. A Markdown heading does not wrap, and `tests/behaviour/test_docs_line_wrap.py` holds a line to 88 columns.

In place of the second and third sentences, from "A probe is one file named" to "and those are examples, not a list.":

> A probe is one file named `test_tmp_*`, and it runs once. What stands under your scratch directory (rule 17) stays there: the probe file, a clone, a virtual environment inside one. The rule is about leavings, not about files: everything else the probe made is gone before you hand over, whatever kind of thing it is — the file itself in a working tree, a worktree, a branch, a checkout, a virtual environment — and those are examples, not a list.

The sentence after those, which opens "What the probe made for ITSELF is what goes:", opens instead "Outside your scratch directory, what the probe made for ITSELF is what goes:", so that a clone a probe made inside the scratch directory is kept by the sentence above and by no other (round 1, finding 2). The rule's first sentence, its last sentence and its `check:` line stay.

**T2, rule 17, whole.** The heading becomes `## 17 Name your scratch for the work item, keep it, stop only what you started`, short enough for the line limit T1 names, and the body:

> What you make outside the repository's working tree, such as a probe, a captured output, a list of files or a clone, sits under your scratch directory, `<scratchpad>/<work-item-id>/<leaf>/`. Your definition names the leaf, and where it names none the leaf is your agent's name. Agents of one session share one scratchpad, and that name keeps a parallel agent's files apart from yours. Where the directory already stands when you first need it, an earlier spawn made it: leave it as it is and add `-2` to the leaf, or the next number free. No agent removes the scratchpad, a scratch directory or a file in one. Record the PID of every process you start and stop it by that record, never by command name. Never delete by glob in a directory another session shares. Another session's process or file answers to the same name, so a leftover you did not start is reported in the hand-back, not stopped and not removed.

**T3, rule 21.** The sentence from "A directory you made under" to "which every agent of the session shares." goes, and the next sentence, "These forms are examples of the rule", follows the `rm` sentence. The `check:` line keeps its first target alone.

### `agents/crafter.md`

**T4, step 4.**

> 4. Where `routing.md` declares a framer and no `frame/design.md` is there, stop and hand back that `routing.md` and the directory disagree. A missing `frame/design.md` is not evidence about the rung, so do not guess which is true.

**T5, step 6.** "A unit only renamed or moved owes no run." goes; the mutation rule keeps the sentence with its citation.

**T6, step 10,** in place of the words from "what was done" to "each statement named for the orchestrator,":

> what was done, each claim labelled as rule 4 asks and the suite as rule 2 asks, each instruction you declined as rule 3 asks, the account the rule *Before you hand back, your range and the work item's records are read whole against HEAD* asks for,

**T7, *Never*,** in place of "step 10's three labels carry the claims.":

> rule 4's labels carry the claims.

**T8, the scratch rule,** its `check:` line kept:

> **Your scratch is named for the work item and the phase.** Your scratch directory (rule 17) is `<scratchpad>/<work-item-id>/phase-<n>/`, where `<n>` is the phase, and in a fix pass `<scratchpad>/<work-item-id>/fix-<n>/`, where `<n>` is the round the pass fixes.

**T9,** in place of the rule *The handoff's facts are coordinates to open*, its `check:` line kept:

> **A handoff's claim is measured where the handoff says.** Rule 5 has you open each coordinate your prompt carries, in the shape `docs/running/the-run.md` *The handoff* gives it. Where a claim flips on where it is measured, measure where the handoff says and say so.

**T10, the broad gate rule,** in place of "The run is rule 2's, and the label is step 10's.":

> The run and the suite's label are rule 2's.

### `agents/proofer.md`

**T11, the scratch rule,** its `check:` line kept:

> **The clone is named for the work item and the round.** Your scratch directory (rule 17) is `<scratchpad>/<work-item-id>/round-<n>/`, and where your prompt names no clone you clone into `<scratchpad>/<work-item-id>/round-<n>/clone`. If cloning fails, say so and do not work in place.

**T12, *The implementer's account is a claim*.** The *Never* bullet "Take the implementer's account as evidence: …" goes. After the rule's lead, before "Read all of it":

> Rule 5 says so of the spawn prompt, the commit messages, the pull request body, `gaps.md` and a comment in the code alike.

**T13, the broad gate rule,** in place of "A spawn prompt that orders a check rule 2 excludes is declined, and the instruction goes in as a row of `## Not judged`":

> An instruction you decline under rule 3 goes in as a row of `## Not judged`

**T14, the probe rule,** in place of its lead and first sentence:

> **A probe runs in the clone, and its files are edits.** A probe follows the probe rules of `skills/code-review/SKILL.md` and rule 7, and it runs in the clone.

### `agents/sealer.md`

**T15, the description.**

> The final, independent guarantor. Spawn once per work item, before the pull request opens: after the review rounds settle, the changelog fragment is written, the orchestrator has run the broad gate, and `seal pr-body` has written the pull request body to a file. It audits every party's account against the issue and the tree, and writes the work item's `guarantee.md`.

**T16, step 2.** The clause "and the part above it is the work item's `pr.<lang>.md`, where `config.json`'s two language keys differ, and then its `pr.md`" goes, so the sentence ends "and you read it as no party." In the sentence that lists what the sealer reads, "where the keys differ" becomes:

> where `config.json`'s two language keys differ

**T17, step 7.**

> 7. **Return the file's text** as your report, every claim labelled as rule 4 asks.

**T18, *Never*,** in place of the bullet that opens "Take a party's account as a fact":

> - Take a party's account as a fact: under rule 5 a phase record's `seen red`, a round's `fixed` and the orchestrator's part of the pull request body are claims.

**T19, the rule on a `seen red`.** "Clone the repository into `<scratchpad>/<work-item-id>/at-base/`" becomes the words below, and "Remove the clone once its runs are done." goes.

> Clone the repository into your scratch directory (rule 17), `<scratchpad>/<work-item-id>/at-base/`

### `agents/framer.md`

**T20,** in place of "A fact that reaches you in prose is opened at its coordinate, or carried into":

> A fact that reaches you in prose is opened as rule 5 asks, or carried into

**T21, the probe rule.** In place of the sentence that opens "Anything that writes runs under":

> Anything that writes runs under your scratch directory (rule 17), `<scratchpad>/<work-item-id>/frame/`.

"The directory is gone before you hand back (rule 17)." goes.

### The other files

**T22, `skills/implement/orchestration.md`,** in place of "its commits, the broad run and the removal of its scratch files among them":

> its commits and the broad run among them

In step 2 of the same section, after the sentence that ends "owns when).":

> Once the pull request is open, the orchestrator removes the work item's scratch directory, `<scratchpad>/<work-item-id>/`, in one `rm -rf` whose path is written out in full, with no variable in it, and removes nothing else of the scratchpad. No agent removes a scratch directory (contract rule 17).

The sentence stands in the skill the orchestrator opens and in no agent's preload. Where `routing.md` stops the work before the pull request, no pull request opens and the directory stays.

**T23, `skills/code-review/SKILL.md`.** The Probe row's Handling cell:

> you write it, named `test_tmp_*`, and run it once; contract rule 7 says where it is deleted and where it stays; what it settled goes into the record's `## Probes`

In place of the first sentence under the table:

> Contract rule 7 is about leavings, not files: outside the scratch directory, a worktree, a branch or a virtual environment a probe made for itself goes too.

**T24, the two READMEs.** In `README.md`, in place of "An agent removes its own directory and never the session's scratchpad.":

> No agent removes its directory or the session's scratchpad. The orchestrator removes the work item's directory once, after the pull request opens.

In `README.ko.md`, in place of the sentence that opens "에이전트는 자기 디렉터리만":

> 에이전트는 자기 디렉터리도 세션의 scratchpad 도 지우지 않습니다. orchestrator 가 pull request 를 연 뒤에 그 작업 항목의 디렉터리를 한 번 지웁니다.

In each README the text stands in place of the sentence phase 1 wrote there.

### `agents/tracer.md`

**T25, the rule *Constraints, enums and defaults are read, not probed*,** in place of "leaves nothing behind (rule 7).":

> leaves nothing outside your scratch directory (rule 7).

## Rule changes

- change
  file: docs/running/the-agent-set.md
  section: What each party writes, and when
  from: The name lives in the definitions, where a rule arrives by mechanism, and one directory per work item and round is what lets the agent that made a leaving say every one of them is gone.
  to: The rule stands in contract rule 17, which every agent receives, and each definition names its own directory under it. No agent removes its directory or a file in it. The name already keeps two agents' files apart, the one removal on record took the whole scratchpad with every other agent's files (#1445), and a removal written with a variable in its path is a command Claude Code holds for a person (#1503). An agent that finds its directory standing leaves it and takes the next free name. The orchestrator removes the work item's directory once, after the pull request opens, in one command whose path is written out in full, because nothing clears a session's scratch when the session ends.
- change
  file: docs/forms/the-round-record.md
  section: The round record
  from: A probe the line names was deleted under the agent contract's probe rule, so the round writes it again from its `## Probes` row.
  to: A probe the line names stands in the earlier round's scratch directory, or was deleted from a working tree under the agent contract's probe rule, so the round writes it again from its `## Probes` row.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the instruction to remove the crafter's scratch directory, with the shared-scratchpad reason and the list of what a phase puts there | `agents/crafter.md` *Your scratch is named for the work item and the phase*, `:100-108` | The removal goes: the directory's name keeps it apart, and the removal is the step that stopped a run (G14). The reason and the list stand once, in contract rule 17 (T2) |
| the scratch-removal sentence of rule 21, and the second target of its `check:` line | `skills/agent-contract/SKILL.md` *21 Write each command so Claude Code's parser can read it*, `:216-219`, `:222` | It can go with the removal it made safe. "No agent removes the scratchpad" in T2 keeps what its last clause guarded, the catch of #1445, and T22 has the orchestrator's one removal name the work item's directory and nothing else |
| the recording of each created path and the removal by that record | `skills/agent-contract/SKILL.md` *17 Clean up only what you started*, `:183-185` | It can go: no agent removes what it made under its scratch directory, and what a probe made elsewhere is rule 7's |
| "a scratch clone" among a probe's leavings, and "it is deleted before you hand over" as a rule without a place | `skills/agent-contract/SKILL.md` *7 A probe is named `test_tmp_*`, one file, run once, deleted*, `:90-93` | T1: what stands under the scratch directory stays, and everything else still goes |
| "The directory is gone before you hand back (rule 17)." and the shared-scratchpad reason | `agents/framer.md` *A question a command answers is answered by running it*, `:157-158`, `:164-165` | The removal goes (G14). The reason stands in T2 |
| "everything it made is gone before you hand back", and the shared-scratchpad reason of the scratch rule | `agents/proofer.md` *A probe leaves nothing, and its files are edits*, `:188-189`; *The clone is named for the work item and the round*, `:91-94` | A proofer's probe runs in its clone, under the round's scratch directory, so T1 keeps it. The reason stands in T2 |
| "Remove the clone once its runs are done." | `agents/sealer.md` *A `seen red` is re-run against the code before the change*, `:174` | The removal goes. A second audit takes `at-base-2/` by T2 (G15) |
| "and the removal of its scratch files" | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, `:31-32` | The orchestrator's commands follow rule 21 whatever they are, so the clause names nothing more. Its one removal is step 2's sentence (T22) |
| "delete it" and "everything else it made goes with it" in the Probe row, and "a clone" among what goes | `skills/code-review/SKILL.md` *Probes and regression tests*, `:114`, `:117-118` | T23 cites contract rule 7, which says where a probe is deleted |
| "An agent removes its own directory and never the session's scratchpad." and its Korean rendering | `README.md:377-378`, `README.ko.md:374-375` | T24 |
| "leaves nothing behind (rule 7)", the words of rule 7 before T1, and the clause that pins them | `agents/tracer.md` *Constraints, enums and defaults are read, not probed*; `tests/behaviour/test_a_probe_that_commits_says_so.py#test_the_fact_finder_points_a_probe_at_rule_7` | T25, and the same case holding "outside your scratch directory (rule 7)" |
| the rule *A declared frame that is absent stops the build* | `agents/crafter.md:111-113` | Step 4 holds the stop and takes the rule's narrowing (T4) |
| the rule *Each phase closes with its record*, with its `check:` line | `agents/crafter.md:172-176` | The Job names both writes, step 8 names the record and its template, and `skills/implement/SKILL.md` *3. The SDD file set* holds what the record carries (G11). `agents/framer.md` and `docs/forms/the-reader-registry.md` still name the test on their own `check:` lines |
| the rule *The chain ends at a pull request, never a merge* | `agents/crafter.md:204-206` | Rule 6 withholds a push and a pull request from every agent, so the crafter has no act the sentence governs. `docs/running/the-run.md` *The run* holds the chain's bound for the orchestrator |
| "A unit only renamed or moved owes no run." at step 6 | `agents/crafter.md:50-51` | The mutation rule states it, with its citation (`:136-138`) |
| step 10's spelling of the labels, of the suite's label and of a declined instruction's line, and its restatement of the account | `agents/crafter.md:65-72` | Rules 4, 2 and 3 state the first three (T6). The crafter's rule *Before you hand back…* states the account, and step 10 cites it |
| the copy of rule 5 in the crafter's handoff rule | `agents/crafter.md:115-118` | T9 cites rule 5 and keeps the narrowing |
| the *Never* bullet "Take the implementer's account as evidence" | `agents/proofer.md:73-74` | The rule *The implementer's account is a claim* takes its list (T12) |
| the copy of rule 3's refusal | `agents/proofer.md:168-169` | T13 cites rule 3 and keeps the row of `## Not judged` |
| the list of the sealer's steps in its description | `agents/sealer.md:7-11` | The definition's *Order of work* holds them (T15) |
| the first of step 2's two statements of what stands above the heading | `agents/sealer.md:76-78` | The second statement, `:81-86`, which the case pins (T16) |
| step 7's spelling of the labels, and "the prompt's summary" and "the command you re-ran and the tree are facts" in *Never* | `agents/sealer.md:138-139`, `:149-152` | Rule 4 (T17). The Job states the reference and names the prompt's summary (`:26-28`), and T18 keeps the records that are claims |
| the copy of rule 5 in the framer's sentence | `agents/framer.md:149-150` | T20 cites rule 5 and keeps the narrowing |
| the case on rule 21's removal clause, and the "share" and "scratchpad" clause of the cases on the definitions | `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py#test_rule_21_removes_the_agents_directory_and_never_the_scratchpad`, `#test_the_wardens_clone_is_named_for_the_work_item_and_the_round`, `#test_the_framers_probe_is_named_for_the_work_item`, `#test_the_crafters_scratch_is_named_for_the_work_item_and_the_phase` | A case on contract rule 17 holds the reason and the directory's shape, and one clause holds `rm -rf` out of the contract and the definitions (*Scope* item 11) |

The work adds no gate, check script, hook, CI step, rule number, line grammar, label or mark. The orchestrator's one removal (T22) is a step, taken once per work item in place of the removal every agent made at every hand-back, which *Removes* names above. Rule 17 keeps its number and takes a new subject in place of the removal it held, and the clauses *Scope* item 11 adds join a module that stands, in place of the case and the clauses the last row removes.

Framed 2026-11-11 by framer, before the build.
