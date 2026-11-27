# Review round 2: 1795759277-scripts-read-git-past-submodule-settings-and-a-floor

```seal
target: 2743287e8, fixes 851641519..2743287e8
```

This is a verifying round over the fix range `851641519..2743287e8`. The range holds round 1's record (`ba56de9e0`), the framer's fold of its three findings (`e8f3dd853`), the orchestrator's row and `pr.md` quotes (`a7086edde`), the crafter's fix of `agents/sealer.md` with its pin (`a8e8087ea`), the crafter's `changelog.md` (`a5688a103`) and round 1's close blocks (`2743287e8`). The range holds no merge of the base. Carried from round 1 without being established again: `chain_check.py#touched`, `#records_only` and `#follows` (`skills/code-review/scripts/chain_check.py:974-1033`), the fixture `tests/lib/test_gitcmd.py#submoduled`, and G3's measurement of which subcommand each setting reshapes. The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and both phase records whole at `2743287e8`. `seal/parity.json` is not declared. The probes ran in a `git clone --no-local` of the branch at `2743287e8` under the round's scratch directory, and nothing was changed in the branch's worktree but this record.

## Findings

### 1. The diff now changes `agents/sealer.md`, and `changelog.md` carries no `### Process changes` row for it

```seal
severity: must
location: `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/changelog.md:4`
evidence: read `docs/layout/the-record-layout.md:50-58`, `agents/crafter.md:20-27`, `templates/records/process.md:1-5`, `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/changelog.md:1-4`, `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/design.md:38`; executed `git diff --stat 851641519..2743287e8`
regression: round-1#1
```

Why it matters: the unit is `changelog.md` as the fix pass for round 1's finding 1 left it, after `a8e8087ea` changed `agents/sealer.md` step 1. `docs/layout/the-record-layout.md:50-58` states the rule: "A work item whose diff changes ... an `agents/*.md` file ... ends its `changelog.md` with the line `### Process changes` and a table in the shape `templates/records/process.md` gives". `agents/crafter.md:20-27` gives that table to the crafter "in every fix pass ... where `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* asks for one". `changelog.md` at `2743287e8` ends at line 4, inside `### Fixed`. The release note lifts each fragment's process rows into one table, and the next framer reads that table for what the way of working became. So the change to the sealer's step reaches neither of them as a process change. *Scope* item 8 of the fold (`frame/design.md:38`) names the step's line and its pin and not the fragment's table, and the fix pass built the item as written and missed a table that the policy asks of any diff touching an agent definition.

The `Source` cell of the snippet below reads `#1640`. The fix pass writes the issue's full URL there, as the other fragments under `seal/threads/` write theirs.

```markdown

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-27 | `agents/sealer.md` step 1 types its listing of what followed the gate's run as `git -C <root> log --ignore-submodules=none --no-merges --name-only <named>..HEAD ^<base>` | Under `diff.ignoreSubmodules` or a `.gitmodules` entry's `ignore`, the listing without the flag showed a commit that moved only a submodule's pointer with no path, so step 1 went on where `chain_check.py#follows` refuses that commit | #1640 |
```

### 2. Three new sentences say `routing.md` scopes this work to each git read a gate decides on, and `routing.md:19` names the reads of three scripts

```seal
severity: should
location: `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/plan.md:42`, `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/plan.md:73`, `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/design.md:47`
evidence: read `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/routing.md:19`, `skills/core/SKILL.md:114`; executed `grep -n -F 'routing.md' seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/*.md`
regression: round-1#1
```

Why it matters: the units are the grounds the fold and the orchestrator wrote for widening *Scope* to the sealer's step 1. `frame/plan.md:42` (*Alternatives considered* row 12) reads "`routing.md` scopes the item to each git read a gate decides on; step 1 is such a read". `frame/plan.md:73` (the orchestrator's row, as `a7086edde` rewrote it) reads "since `routing.md` takes this work as each git read a gate decides on and step 1 is one". The *Out of scope* bullet at `frame/design.md:47` reads "which is what `routing.md` scopes this work to". `routing.md:19` reads "The item judges each git read that a gate decides on, in `chain_check.py`, `seal.py` and `broad_gate.py`". The three sentences drop that list. A sealer that checks the widening against `routing.md` finds three scripts and no agent definition, and reads the grounds as a claim the record does not hold. The fold's *Scope* item 8 stands on firmer grounds that the same records already state: `skills/core/SKILL.md:114` gives *No seal without the broad run* to step 1 beside the chain check's broad gate arm, and this work's flag made the two read one commit two ways (`frame/design.md` G16; `frame/plan.md:42` (a)). The defect came from round 1's finding 1, which quoted `routing.md:19` without its list, and the fold and the orchestrator's row carried that quote. The `grep` above lists the records' citations of `routing.md`, and it is a sample by the file's name. It prints `frame/plan.md:33` and `:53`, which cite it for other facts and stand, and the three lines located here.

The snippets replace the clause in each line. `frame/plan.md:42` and `frame/design.md:47` are the framer's to fold, and `frame/plan.md:73` is the orchestrator's.

```markdown
step 1 holds *No seal without the broad run* beside the chain check's broad gate arm (`skills/core/SKILL.md` *Judgment is not licence to skip a party*), and this work's flag made the two read a pointer-only commit two ways (`frame/design.md` G16); `routing.md` names the reads of `chain_check.py`, `seal.py` and `broad_gate.py`, and this fold adds step 1 to them
```

```markdown
since step 1 holds *No seal without the broad run* beside the chain check's broad gate arm and this work's flag made the two read one commit two ways (`frame/design.md` G16), though `routing.md` names the reads of three scripts alone
```

```markdown
No gate's branch is decided on the paths they list, which is what separates them from step 1 (G16), so neither changes here.
```

```seal
verdict: fixed 62ca128a2
answer: The framer folded the round's snippets into `frame/plan.md` *Alternatives considered* row 12 and the `frame/design.md` *Out of scope* bullet at `62ca128a2`, and also dropped row 12's clause that #1640 asks every read judged, the same overstatement; the orchestrator rewrote its round-1 routing row to the round's snippet for `plan.md:73`, committed with that fold, and `c2b0448cf` corrected round 2's two route rows on the framer's hand-back.
```


## Confirmations

```seal
confirms: round-1#1
```
What holds: `agents/sealer.md:54-64` has the sealer run `git -C <root> log --ignore-submodules=none --no-merges --name-only <named>..HEAD ^<base>`, in a fenced block under the sentence that says what the flag keeps, and `tests/behaviour/test_the_sealer_guarantees.py:167-170` pins that form (read). The fence departs from round 1's paste-ready text. `tests/behaviour/test_docs_line_wrap.py:43` holds prose to 88 columns, and the command inline runs past that limit. The case reads fenced lines through `lib/blocks.py`'s fence rule (`:80-84`) and passes (read; executed below), so the departure holds. *Scope* item 8 asks the step to say "in the same sentence what the flag keeps". The sentence says it of "the command below", which satisfies the item. The pin was seen red: with the fence's command put back to `log --no-merges` in the round's clone, `test_step_1_reads_the_record_and_runs_nothing` failed at `:167` (executed, `## Probes`). What the command lists was probed on `submoduled`'s repository. Without the flag, the command listed the commit with no path under `diff.ignoreSubmodules=all` and under the `.gitmodules` entry. With the flag directly after `log`, it listed `sub` under no setting and under both settings (executed). That confirms G16's finding that the configuration key shortens this read too, which round 1 did not name. S9's search, `git grep -n -F 'log --no-merges --name-only' HEAD -- agents tests/behaviour`, prints nothing (executed). `git grep -n -F 'name-only <named>' -- . ':!seal/threads'` prints the step and its pin alone, and no eval grader or other document states the command (executed). The modules that read `agents/sealer.md` ran green (executed). Finding 1 and finding 2 of this round are defects in units this fix made, and neither touches the step's line.

```seal
confirms: round-1#2
```
What holds: `changelog.md:3` gives each setting its own reach. The configuration key reaches `diff`, `log` and `status`, and the `.gitmodules` entry reaches `diff-tree` as well. The records arm's miss is placed under the `.gitmodules` entry alone, and `changed`'s under either setting. The added clauses on the sealer's step 1 match `frame/design.md` G16 and the probe above (read; executed). `frame/plan.md:64` places the records arm under the `.gitmodules` entry and adds the sealer's step under either setting (read). Each `pr.md` quote is a substring of `frame/plan.md` at `2743287e8` (executed: a `python3` read of each `- "..."` line of `pr.md` against the file, four of four found). The new quote at `pr.md:4` is the grounds cell of the `fix:` row at `frame/plan.md:72`, which already named the `.gitmodules` setting.

```seal
confirms: round-1#3
```
What holds: `frame/questions.md:7` and G9's right-hand cell at `frame/design.md:17` say that #1642 gave 2.24 when the frame read it and that its body was corrected to 2.30 on 2026-11-27 (read). The close's search, `git grep -n -F -e '2.24' -- <the work item's directory> lib/gitcmd.py README.md README.ko.md`, prints those two lines and lines of round records alone (executed).

What matched: the rest of the fold. G17's search, run at `ba56de9e0`, prints the lines G17 lists. The two `hygiene.yml` lines it names run in this repository alone, since the workflow `seal pr-checks install` writes is `templates/setup/hygiene.yml`, which types no `git diff`, `git log` or `git status` (executed: G17's `git grep` and `grep -n 'name-only\|git diff\|git log' templates/setup/hygiene.yml`). The narrowed S4 and its search print `lib/gitcmd.py` alone (executed). *Removes* row 5, *Data & interfaces*' gate entry and S9 state what the tree holds at `2743287e8` (read). The orchestrator's row at `frame/plan.md:73` cites `skills/implement/orchestration.md:83`, whose paragraph gives a decision's fold to the framer and a round finding on a frame sentence to the framer, as the row claims. Finding 2 is on the row's first clause.

What matched: round 1's close answers. The commands they report were run again where this round could. The pin seen red, the S9 search and the `2.24` search agree with the answers (executed above). The fix pass's `seal range` read and its whole-file reads were not run again. This round read the same files whole itself.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `2743287e8` beyond the seven modules this round ran | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, once findings 1 and 2 are closed |
| Whether a row of `seal/follow-up.md` carries the two typed diffs `frame/design.md:47` leaves, `agents/sealer.md` step 2's `git diff <base>...HEAD` and `agents/proofer.md:157`'s `git log --no-merges -p`, which under either setting show no moved pointer | `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/design.md:47` | the orchestrator, as the bullet names it |
| Whether git 2.30 reads each command the scripts start as 2.50.1 does | `frame/questions.md` Q1, `gaps.md:8` | a measurement under a git whose `git --version` prints 2.30, which the repository owner arranges |
| The `FLAGGED` cases and the real-git case of `Test_older` under the Linux and Windows runners' git | `gaps.md:9` | CI's Linux and Windows legs on the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py tests/text/test_the_rules_have_one_owner.py -q`, in the round's clone at `2743287e8`, the test files that open `agents/sealer.md` by `git grep -l -F 'sealer.md' -- tests` less `tests/skills/test_chain_check.py`, which names it in a docstring alone | `162 passed` |
| `bin/test tests/behaviour/test_the_sealer_guarantees.py -q -p no:xdist -k test_step_1_reads_the_record_and_runs_nothing`, with the fence's `log --ignore-submodules=none --no-merges` edited to `log --no-merges` in the clone's `agents/sealer.md` | `1 failed`, at `tests/behaviour/test_the_sealer_guarantees.py:167`. The edit was reverted |
| `bin/test tests/lib/test_tmp_round2_probe.py -q -s -p no:xdist`, which builds `submoduled(tmp_path, setting)` for each setting and prints `log --no-merges --name-only --format=%h HEAD~1..HEAD` without the flag and with `--ignore-submodules=none` directly after `log` | under no setting `sub` both ways; under `configuration` and under `.gitmodules` the commit alone without the flag, and `sub` with it |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.3 --root <the branch worktree> --worktree`, before this record was written | exit 0; it named round 1's finding 1 as read by no later round and a verifying round as owed, which this record answers, and the gate record and guarantee as absent; no notice at a line of `frame/design.md` |
