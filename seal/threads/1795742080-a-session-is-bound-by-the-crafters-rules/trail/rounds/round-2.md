# Review round 2: 1795742080-a-session-is-bound-by-the-crafters-rules

```seal
target: 6a32674b1, fixes bac332952..6a32674b1
```

This round verifies the fixes for round 1. The range `bac332952..6a32674b1` holds the framer's fold `9f7f6e4d5`, the orchestrator's row corrections `6a1347cc5`, the crafter's fixes `837a27a18`, `ffcb56f24`, `780c45da1`, `29d2888bc`, `ed2a57793` and `1aa992343`, the orchestrator's fold `a1d478421`, and the close blocks `6a32674b1`. The range holds no merge. The code reviewed is `git diff bac332952..6a32674b1`. The round read outside that diff only where a fix reaches: `skills/implement/scripts/range_read.py#DIFF`, which the new `_changed` reads through, and the three fold commits that finding 6 is about.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md` and `trail/rounds/round-1.md` whole at `6a32674b1`. The commit language and the record language are both English, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared.

Carried from round 1 and not established again: where the moved rules stand in `skills/implement/SKILL.md`, the narrow set's file list, the *Overlap with the release* coordinates, and the Windows row's answerer. Established again at this target: the G18 searches, the contents of the fold commits `53883c4e2`, `f09656b7b`, `9f7f6e4d5` and `6a1347cc5` (read with `git show`), and every claim the close blocks make.

The claims weighed. The crafter's close for finding 1 says the case covers five shapes in its own words. `tests/skills/test_range_read.py:357` holds the ids `added`, `moved`, `in-place-of-a-file`, `a-file-in-its-place` and `deleted`. The close says a `SUBMODULE = BINARY` mutant survived until `1aa992343`. `git show 1aa992343` adds one line, `assert RANGE.BINARY.format(path="sub") not in text`. Without that line, a `SUBMODULE` equal to `BINARY` passes the header assertion and the summary assertion both, so the survival is what the code shows (read). At `6a32674b1` that mutant reads `red` (executed). Finding 5's close says the cited row still says "the crafter" until the settle writes it. `docs/running/what-a-script-gates.md:69` reads "the crafter at each unit that adds behaviour", and *Scope* item 7 (`frame/design.md:72`) makes the row the fact's home "once the settle writes it". The interval is the one every rule change has, so the close holds. The crafter's account of its read is in its hand-back, which the tree does not hold, so this round cannot read which lines of its `seal range` file it names as read whole. That is a row of `## Not judged`. The crafter's file, `fix-1/range-1.txt` in the work item's scratch, opens with the range line from `342a46f31` to `1aa992343` and prints `frame/plan.md` whole at its lines 1192 to 1272 (read).

`chain_check.py --worktree` printed no notice at a line of `frame/design.md` naming a test pin or a copy (executed).

## Findings

### 1. `seal range` names no submodule's path where `diff.ignoreSubmodules` or a `.gitmodules` entry says `ignore = all`

```seal
severity: should
location: `skills/implement/scripts/range_read.py:131`, `skills/implement/scripts/range_read.py:236-248`, `tests/skills/test_range_read.py:40-45`, `tests/skills/test_range_read.py:359-399`
evidence: executed `bin/test tests/skills/test_tmp_round2_submodule_ignore.py -q -s -p no:xdist` and `bin/test tests/skills/test_tmp_round2_ignore_override.py -q -s -p no:xdist` in a clone at `6a32674b1` (the probes of `## Probes`, rows 1 and 2); executed `git grep -n -E -e '--ignore-submodules|ignoreSubmodules' -- lib skills .github hooks`; read `skills/implement/scripts/range_read.py:125-131`, `:236-248`, `:421-447`, `lib/gitcmd.py:30-56`, `docs/running/what-a-script-gates.md:24-40`
```

Why it matters: *Scope* item 11 (`frame/design.md:79`) says a path whose entry is a gitlink on either side of the range is named in the file and in the summary. The builder's rule reads the summary's `not printed:` lines as the paths it has to read by hand. Under either setting, git leaves the submodule's path out of `git diff --raw`. The file and the summary then say nothing of a submodule the range moved, added or deleted. The builder reads the file to its last line and is never told the submodule changed. `docs/running/what-a-script-gates.md:24-31` asks that a script read git the same under any configuration, and names a key that takes a commit's paths out of a listing as one the script must hold. `ignore = all` in `.gitmodules` is committed with the repository, so every builder in such a repository meets it.

The grounds. `DIFF` (`:131`) holds `--no-color`, `--no-ext-diff`, `--no-textconv` and `--no-renames`, and no `--ignore-submodules`. The first probe ran the case's fixture three ways for an added and a moved gitlink. With no setting, `--raw` printed an `A` line for `sub`, and the file named `sub`. With `git config diff.ignoreSubmodules all`, and with a `.gitmodules` entry for `sub` holding `ignore = all`, `--raw` printed nothing, the command exited 0, and `SUBMODULE` for `sub` stood nowhere in the file. The second probe asked which form overrides each setting. `-c diff.ignoreSubmodules=none` restored the path under the configuration key and not under `.gitmodules`. `--ignore-submodules=none` restored it under both. So `lib/gitcmd.py#KEYS`, the home `lib/gitcmd.py:30-48` gives a key found later, cannot hold this one, because no `-c` key reaches the `.gitmodules` entry. The flag belongs beside the other switches in `DIFF`. The search prints nothing, so no script of the tree passes the flag. `HOSTILE` (`tests/skills/test_range_read.py:40-45`) sets neither, so the case of *Scope* item 11 passes against a command that drops the path.

The defect is in `DIFF`, which phase 1 built. Before `837a27a18`, `--name-status` dropped the path under the same settings. The fix pass did not introduce it, so this finding takes no `regression:` line. Finding 1 of round 1 closes on the inputs it named, as `## Confirmations` says. This round reads the defect because *Scope* item 11's rule reaches it. The other scripts that list a diff's paths, such as `skills/code-review/scripts/chain_check.py:401` and `:409`, are outside this range and are not judged here.

The fix:

```python
# The options of every `git diff` the command runs. `--ignore-submodules=none`
# keeps a submodule's path in the listing where `diff.ignoreSubmodules` or a
# `.gitmodules` entry's `ignore` would leave it out. It is a flag and not a
# key of `lib/gitcmd.py#KEYS`, because `-c diff.ignoreSubmodules=none` does
# not reach the `.gitmodules` entry.
DIFF = (
    "diff",
    "--no-color",
    "--no-ext-diff",
    "--no-textconv",
    "--no-renames",
    "--ignore-submodules=none",
)
```

The flag changes nothing in the `-U0` and `-W` prints of a text path. It crosses no OS boundary. Its one precondition is a git that knows `--ignore-submodules=none` on `diff`. git 2.50.1 does (executed, the second probe), and this round did not check the oldest git the plugin supports.

The case, in `tests/skills/test_range_read.py`. `HOSTILE` gains the configuration key, and its comment gains what the key does:

```python
# A configuration that would put text into what `git diff` prints, or take a
# path out of it: an external diff and a textconv filter that each fail,
# colour on every command, nearby hunks joined, and every submodule ignored.
# The command switches each off, and an oracle below asks git with the same
# switches.
HOSTILE = (
    ("diff.external", "false"),
    ("diff.hostile.textconv", "false"),
    ("color.ui", "always"),
    ("diff.interHunkContext", "20"),
    ("diff.ignoreSubmodules", "all"),
)
```

In `test_accepts_a_submodule_by_name_and_does_not_print_it`, the base gains a `.gitmodules` entry that ignores `sub`, which no `-c` key overrides, and the docstring says so:

```python
        """S6 and *Scope* item 11: a path whose entry holds a submodule's
        commit before the range, after it or both is named in the file and
        in the summary, none of git's lines on it is printed, and the read
        goes on past it to the records. A submodule the range deletes is
        named as deleted. The configuration and a `.gitmodules` entry each
        tell git to ignore the submodule, and the path is named all the
        same."""
```

```python
        # git leaves out a submodule this entry ignores, whatever `-c` says.
        gitmodules = '[submodule "sub"]\n\tpath = sub\n\turl = ./sub\n\tignore = all\n'
        repo, start = built(tmp_path, {".gitmodules": gitmodules})
```

The line replaces `repo, start = built(tmp_path, {})` at `:382`. `put` removes `sub` with `git rm --cached`, which leaves `.gitmodules` as it is.

The fix pass shows the case red with only the flag removed. With the flag replaced by the `KEYS` entry, the `.gitmodules` entry still hides the path, so the case stays red.

### 2. `frame/plan.md` row 22 says no case holds a file put in place of a submodule, and the fix pass's case holds it

```seal
severity: should
location: `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/plan.md:51`
evidence: read `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/plan.md:51`, `tests/skills/test_range_read.py:348-399`; executed `git show 9f7f6e4d5 -U0 --format= -- seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/plan.md`, `grep -rn -F -e 'no case of the script' -e 'holds that shape' seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/`
regression: round-1#1
```

Why it matters: the unit is row 22 of *Alternatives considered*, which the fold `9f7f6e4d5` wrote for round 1's finding 1. It rejects printing a file put in place of a submodule, and one of its grounds is "no case of the script holds that shape". *Scope* item 11 names that shape among its inputs and states its limit. The fix pass built the case over five shapes, `a-file-in-its-place` among them (`tests/skills/test_range_read.py:357`), at `837a27a18`, so the ground went false after the fold wrote it, and no later fold rewrote it. The settle reads this table for what each alternative was rejected on, and a framer who weighs the alternative again takes the row's word that no case reaches that shape. *Alternatives considered* carries no date, so the row states the present. The frame's dated sections are *Grounding* and *Technical context*, as `The tree as read at 99841677c.` marks them.

The grounds. The row's other two grounds hold. git's print of that shape was not run for the fold, and the case does not run it either, since the `gitlink` branch stands before every print. The case asserts that `A file.` is not in the file, which is the limit the row's verdict states. The search prints this line alone in the work item's records. It is a sample, since a statement in other words escapes it. `frame/plan.md` is the framer's file, so the fold writes the fix.

The fix, the row's middle cell in place:

```markdown
| 22. For the same finding, name a path only where HEAD's entry is the gitlink, and print a file put in place of a submodule | git's print of a path that changes from a submodule to a file was not run for this fold, no case of the script held that shape at `9f7f6e4d5`, and the round's fix was read on the other reading. The case `a-file-in-its-place` of `tests/skills/test_range_read.py#test_accepts_a_submodule_by_name_and_does_not_print_it` now holds the limit: the path is named and the file's text is not printed | Rejected for the limit *Scope* item 11 states: the path is named, so the builder reads that file by hand |
```

The crafter's read of its range printed `frame/plan.md` whole, so its account would name this line for the orchestrator's fold. Whether it did is in the hand-back, and the orchestrator's fold `a1d478421` touched *Scope* item 8 alone. `## Not judged` holds that question.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/implement/scripts/range_read.py:236-248` reads each path's two modes from `git diff --raw -z`. `:428-430` names a path whose either mode is `GITLINK` under `SUBMODULE` and as `not printed: <path>, submodule`, after the deleted branch, as *Scope* item 11 asks. The case holds the five shapes, the records after the path, and that the path is not called binary. `seal mutate` over five breaks read `red` for each: the branch removed, `SUBMODULE = BINARY`, the new mode alone, the old mode alone, and the summary word `binary` (executed, `## Probes` row 3). The narrow set ran green (executed, below). The `changelog.md:5` sentence on the submodule matches the code (read). Finding 1 of this round is a defect under two settings the inputs of round 1's finding did not name.

```seal
confirms: round-1#2
```
What holds: `BUILDERS_RULES` (`tests/text/test_a_moved_rule_leaves_its_definition.py:195-211`) holds **A new test starts from its group.** with `` `seal layout --pairs` ``, which stands at `skills/implement/SKILL.md:196`. `seal mutate` removing that sentence, and then the lead alone, read `red` for each against `test_the_crafters_rules_name_what_their_readers_resolve` (executed, `## Probes` row 4). *Scope* item 8 names the case since `a1d478421` (read: `frame/design.md:74`).

```seal
confirms: round-1#3
```
What holds: `skills/code-review/orchestration.md:94-99` now has a crafter's hand-back carry the account that `skills/implement/SKILL.md` *The account of that read quotes its commands and describes no read in other words* states. The finding's search, run again, prints `skills/agent-contract/SKILL.md:141` alone, which is contract rule 12's method of an enumeration (executed). `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/behaviour/test_docs_line_wrap.py` pass over the edited lines (executed, in the narrow set).

```seal
confirms: round-1#4
```
What holds: `changelog.md:3` says `agents/crafter.md` opens `skills/implement/SKILL.md` at step 1, and cites the frame rule at step 3, the two mutation rules at step 6, and the rule on the read with the account's rule at step 10. `agents/crafter.md:33`, `:40`, `:55-57` and `:72-77` hold each of those citations, and no other (read).

```seal
confirms: round-1#5
```
What holds: `skills/verify/seal-mutate.md:3-6` cites the row of `seal mutate` in `docs/running/what-a-script-gates.md` *The checks* for who runs it, and no longer lists the parties. `git grep -n -F -e "the orchestrator that builds itself" -- .` prints `frame/design.md:134`, the rule change's `to`, and round 1's quotes, and nothing in `skills/` (executed). `chain_check.py --worktree` prints no repeat notice for `frame/design.md` (executed). `skills/verify/scripts/mutation_check.py:109-110` cites `skills/implement/SKILL.md` (read).

```seal
confirms: round-1#6
```
What holds: row 1 of *Judgments of the run* (`frame/plan.md:78`) matches `git show 53883c4e2 -U0`. Besides *Scope* item 10, S11 and rows 18 and 19, the commit changes *Scope* item 1's `SHIPPED` row, S5, S6, the exit line and the rule change's `to`. `--word-diff` of the output line shows the rename clause and the local-mode sentence added beside item 10's widening, and the phase-2 row gains the test file (executed). Row 2 (`:79`) lists every line `git show f09656b7b -U0` changes: *Scope* items 2, 4, 5, 6 (both bullets), 8 (both bullets) and 9, the item of *Scope* Out, *Overlap with the release*, *Operational impact*, and Q1 and Q2 (executed). Row 3 (`:80`) says the fold of finding 1 adds *Scope* item 11, which `9f7f6e4d5` does, and that the orchestrator rewrote its two rows in that edit. `git show 9f7f6e4d5 -U0` shows both rows rewritten there, and `6a1347cc5` then writes the framer's three further departures (executed).

What matched: the searches of `frame/design.md` G18 at `6a32674b1`. V1, V3 and V4 print nothing. V2 prints `skills/implement/SKILL.md:167`, `:192`, `:201`, `:244` and `:249` alone (executed, with G18's commands).

What matched: the narrow set, run once in the clone at `6a32674b1`: `bin/test tests/skills/test_range_read.py tests/skills/test_seal.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/behaviour/test_chain_hooks_hardening.py tests/skills/test_mutation_check.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/behaviour/test_a_reference_root_is_read_and_never_taken.py -q` gave 754 passed and 9 skipped, exit 0 (executed).

What matched: the new cases against their groups. The submodule case stands beside the binary case and the renamed case. Its five shapes are the inputs *Scope* item 11 names, and its `deleted` shape holds the branch order the item states, which the deleted-path case does not reach (read). The `BUILDERS_RULES` entry is a parameter of the case that walks that dict, and no other case reads the rule in `skills/implement/SKILL.md` (read).

What matched: the frame lines the fix range changed. *Scope* items 7, 8 and 11, S6, *Data & interfaces*, the rule change's `to` and the *Removes* sentence state what the code and the tests hold at `6a32674b1` (read). `gaps.md` still labels the suite `unverified` with the orchestrator as its answerer (`:7`), so the label is honest.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Which lines of its `seal range` file the crafter's account names as read whole, and whether it named `frame/plan.md:51` for the fold. The account is in the hand-back, which the tree does not hold | the crafter's hand-back for round 1's fix pass | the orchestrator, which holds the hand-back |
| Whether other scripts that list a diff's paths drop a submodule under the two settings of finding 1, such as `skills/code-review/scripts/chain_check.py:401` and `:409` | outside the fix range | the orchestrator, which decides whether to file it |
| Whether step 1's sentence on contract rules 4 and 5 needs a count of its own, carried from round 1 and not judged again | `skills/implement/orchestration.md:36-40`, `seal/follow-up.md:48` | the orchestrator, with the framer at the fold |
| `seal range` on Windows | `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/gaps.md:8` | CI's Windows leg |
| The full suite, the repository-wide lint and the format check | the work item's tree | the orchestrator, at the broad run once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round2_submodule_ignore.py -q -s -p no:xdist`, in a clone at `6a32674b1`: an added and a moved gitlink, under no setting, under `diff.ignoreSubmodules=all`, and under a `.gitmodules` entry with `ignore = all` | 6 passed. With no setting, `--raw` printed the path and the file named `sub`. Under either setting, `--raw` printed nothing, `seal range` exited 0, and the file did not name `sub` |
| `bin/test tests/skills/test_tmp_round2_ignore_override.py -q -s -p no:xdist`, same clone: a moved gitlink under each setting, read by plain `git diff --raw`, by `-c diff.ignoreSubmodules=none` and by `--ignore-submodules=none` (git 2.50.1) | 2 passed, exit 0. Under the configuration key: plain printed nothing, the `-c` key and the flag printed the path. Under `.gitmodules`: plain and the `-c` key printed nothing, the flag printed the path |
| `bin/seal mutate skills/implement/scripts/range_read.py` with five `--replace` pairs (`elif gitlink:` to `elif False:`; `SUBMODULE` to `BINARY`; the mode test to `GITLINK == new_mode`, then to `GITLINK == old_mode`; `why="submodule"` to `why="binary"`) `--tests "bin/test tests/skills/test_range_read.py -q -x -k submodule -p no:xdist"`, same clone | 5 mutants, 5 red, exit 0 |
| `bin/seal mutate skills/implement/SKILL.md` removing `` `seal layout --pairs` is that check. ``, then the lead **A new test starts from its group.** alone, `--tests "bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -q -x -k test_the_crafters_rules_name_what_their_readers_resolve -p no:xdist"`, same clone | 2 mutants, 2 red, exit 0 |
