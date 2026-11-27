# Review round 1: 1795759278-the-cores-margin-depends-on-the-path

```seal
target: bce10d4a1 against origin/release/v0.39.3
```

This is the work item's first round, so no earlier round carries a coordinate or a verdict. The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` whole at `bce10d4a1`. The records language and the commit language are both English, so no `pr.<lang>.md` is owed. The diff read is `86f98018c..bce10d4a1`: `lib/core.py`, `tests/lib/test_core.py`, `tests/hooks/test_core_start.py`, `README.md`, `README.ko.md`, `CONTRIBUTING.md`, `.claude-plugin/plugin.json` and the work item's records. The round also followed the change into the one untouched caller of `core.rendered` in shipped code, `skills/verify/scripts/payload_meter.py#session_composition`. `seal/parity.json` is not declared, so no parity comparison is owed.

## Findings

### 1. `seal payload` in a tree deeper than about 165 characters counts the one line that names the core and labels it as the core

```seal
severity: should
location: `skills/verify/scripts/payload_meter.py:386-394`, `skills/verify/scripts/payload_meter.py:516-518`, `skills/verify/scripts/payload_meter.py:491-495`, `skills/verify/scripts/payload_meter.py:14-17`, `skills/verify/scripts/payload_meter.py:376-384`, `tests/skills/test_payload_meter.py`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/frame/design.md:56`
evidence: executed `bin/seal payload --agent proofer` in a `git clone --no-local` of the branch at `bce10d4a1` whose root is 177 characters long, and in this worktree at 55 characters; executed `git grep -n -F -e "the core the plugin's" -e "the core below its frontmatter" -e "SessionStart\` hook prints" -- skills/verify/scripts/payload_meter.py tests/skills/test_payload_meter.py docs skills/verify/SKILL.md`; read `lib/core.py:171-174`, `skills/verify/scripts/payload_meter.py:375-394`
```

Why it matters: `payload_meter.py#session_composition` passes the measured tree as both the repository and the plugin root, `core.rendered(core.origin(root, root), root)` (`:388-390`). The new branch of `lib/core.py#rendered` (`:172-174`) returns the line `TOO_LONG` and the closing line wherever the whole output reaches `CAP`. With the tree's core that happens at a tree root longer than 165 characters, and the agents of this process build their scratch clones at such paths: this round's clone is 177 characters deep, the framer's was 175 (`frame/design.md:27`). There the meter's hook row reads 932 bytes, against 9,935 in this worktree, and its note still says "what the `SessionStart` hook prints: its first line, the core below its frontmatter and its closing line" (`:516-518`). The session table's opening sentence says the same (`:491-495`). A person or a framer weighing a change to the core from a scratch clone reads a core of about 300 tokens. Before this change, the same clone counted the core's text plus three long roots. That was an overcount, but the core's bytes were in the figure.

The frame put the meter out of scope with the sentence "It counts `core.rendered` for the measured tree at that tree's path, which is what a session there receives, and it follows *Scope* items 1 and 2 through that call" (`frame/design.md:56`). The count follows item 2. The row's note does not, and a session that receives the line then opens the core, which no row counts.

The search on the evidence line is a sample under contract rules 12 and 19. It printed the module docstring at `:16`, the table's opening sentence at `:491-495`, the note at `:517`, and the case docstring and assertion at `tests/skills/test_payload_meter.py:9`, `:374` and `:395`. The docstring of `#session_composition` at `:376-384` says "header and closing line included", in other words. `docs/layout/the-record-layout.md:181` names the hook and not the meter's row, so it stays. The snippet covers the row and its note. The fix pass owes the docstrings at `:14-17` and `:376-384` the same clause. It also owes a case in `tests/skills/test_payload_meter.py` that builds a tree whose core reaches `CAP` and holds the note, by contract rule 14. The frame's sentence at `frame/design.md:56` says what the work concludes, so the framer folds it.

```python
# skills/verify/scripts/payload_meter.py, session_composition
    path = core.origin(root, root)
    if os.path.isfile(path):
        printed = core.rendered(path, root)
        hook.update({"bytes": len(printed.encode("utf-8")), "chars": len(printed)})
        # The hook names the core in place of printing it where the whole
        # output would reach `lib/core.py#CAP`; the session then opens the
        # file, which this row does not count.
        if printed.startswith(core.TOO_LONG.format(path=path, cap=core.CAP)):
            hook["named"] = True  # NAME NOT IN TREE: a new key of the hook row
    else:
        hook.update({"bytes": 0, "chars": 0, "missing": True})

# skills/verify/scripts/payload_meter.py, the session table's note
        elif row["share"] == "hook" and row.get("named"):
            note = (
                " — what the `SessionStart` hook prints where the whole output "
                "would reach `lib/core.py#CAP`: one line naming the core's file "
                "and the closing line. The session opens the core itself, and "
                "this row does not count it"
            )
        elif row["share"] == "hook":
            note = (
                " — what the `SessionStart` hook prints: its first line, the "
                "core below its frontmatter and its closing line"
            )
```

The `startswith` reads the module's own constant in its one spelling, the shape `skills/core/SKILL.md` *The rule a mechanism is kept against* lets a script hold a fact on. No precondition at an OS boundary: the row reads what `rendered` returned.

### 2. `lib/core.py`'s docstring says the plugin's root stands once in the output, and the output past the cap names it twice

```seal
severity: should
location: `lib/core.py:14-20`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/changelog.md:3`
evidence: read `lib/core.py:14-20`, `lib/core.py:171-174`, `lib/core.py:135-140`; executed `git grep -n -i -e "root once" -e "stands once" -e "occurs once" -- lib tests skills hooks docs` and `grep -rn -i -e "root once" -e "stands once" -e "occurs once" seal/threads/1795759278-the-cores-margin-depends-on-the-path/`
```

Why it matters: the module docstring opens its new paragraph with the bold claim "**The plugin's root stands once in the output.**" (`lib/core.py:14`). The module calls itself "the one definition of the core hook's output" (`:3`), so a crafter editing it reads the claim as a property of every output. For the plugin's own core past the cap it does not hold. `rendered` returns `TOO_LONG` naming `path`, which is `<root>/skills/core/SKILL.md`, then `closing(plugin_root)`, which names `<root>` again (`:174`). *Scope* item 2 asks for that closing sentence "whichever core it is", so the code is right and the docstring is wrong. The same paragraph then says what the output past the cap holds. It does not say that this output names the root a second time.

The search on the evidence line is a sample under contract rules 12 and 19. Outside this work item it printed `lib/core.py:14` and two case docstrings, `tests/lib/test_core.py:226` and `:246`, which describe whole outputs and hold. Inside the work item it printed `changelog.md:3`, whose bold title says "so an installed plugin's output holds that root once" with no limit on the root's length. The frame's statements, `frame/plan.md:21` and `frame/questions.md:6`, each go on in the same sentence to what a root past the cap receives, so they stay. The phase record is history and stays. The snippet covers the docstring and the changelog title.

```text
lib/core.py:14-20

**Where the core is printed, the plugin's root stands once in the
output.** Where the core printed is the plugin's own, the first line names
it under that root and the closing line says its paths are relative to it.
Where the core is a clone's, the closing line names the running plugin's
root. **An output that would reach the harness's cap is not printed**: one
line names the core's file for the session to open, above the closing line
naming the running plugin's root whichever core it is, because past the
cap the harness keeps only a preview and the closing line would be lost.

changelog.md:3, the bold title

- **The core's closing line names its two files relative to the plugin's root, so an installed plugin's printed core holds that root once (#1641).**
```

### 3. `gaps.md` *Not done* reports as undone a table that `frame/design.md` *Scope* item 8 no longer asks for, and an orchestrator's judgment that `frame/plan.md` records as made

```seal
severity: should
location: `seal/threads/1795759278-the-cores-margin-depends-on-the-path/gaps.md:13`
evidence: read `seal/threads/1795759278-the-cores-margin-depends-on-the-path/gaps.md:13`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/frame/design.md:49`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/frame/plan.md:58`; executed `git show 5a0909a80 -- seal/threads/1795759278-the-cores-margin-depends-on-the-path/frame`
```

Why it matters: the bullet opens with "The `### Process changes` table of `frame/design.md` *Scope* item 8", and it ends with "Whether the weighing `CONTRIBUTING.md` gains belongs in the release note's process table is the orchestrator's judgment." When the crafter wrote it at `48f4fc57f`, item 8 said "Its `### Process changes` row is the weighing of item 7", so the bullet named a departure. The fold at `5a0909a80` rewrote item 8 to "It carries no `### Process changes` table", and `frame/plan.md:58` records that "The orchestrator takes the crafter's reading of item 8". At the target, the bullet names a table that item 8 rules out and leaves open a judgment that is already made. The sealer reads `gaps.md` as what the work left undone. `skills/implement/orchestration.md:96-99` gives a statement found in `gaps.md` to a fix pass. The bullet is rewritten in place, since the decision not to write the table still stands.

```markdown
## Not done

- **No `### Process changes` table.** `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* asks for one where the diff changes the way-of-working files that section lists, and this diff changes none of them, so `frame/design.md` *Scope* item 8 asks for none. The weighing `CONTRIBUTING.md` gains stands there and in the fragment's third `### Fixed` entry. The orchestrator took this reading in `frame/plan.md` *Judgments of the run*, its row of 2026-11-27.
```

## Confirmations

What matched: *Scope* items 1 to 4 against `lib/core.py`. `START` holds the two paths joined with `/` at import and no slot for a root (`:78-84`). `closing` returns `OWN_ROOT` where no root is given and `RUNNING_ROOT` naming the root otherwise (`:135-140`). `whole` reads no file (`:143-147`). `rendered` compares with `os.path.samefile` and falls to another file on `OSError` (`:167-170`). It prints whole under `CAP` and otherwise returns `TOO_LONG`, a newline and `closing(plugin_root)` (`:171-174`). `ROOT_ROOM` is 100 with the comment item 3 asks for, and `CAP`'s comment names it (`:51-60`). `TOO_LONG` opens with `AgenticSeal core:` and formats the cap from `CAP` (`:67-71`). `hooks/core-start.py` and `hooks/hooks.json` are unchanged (read). Claimed in `trail/phases/phase-1.md:9`: `START` is still built from `ORCHESTRATION` and `REVIEW`. Found at `lib/core.py:84` (read).

What matched: the measurements. `core.whole` on the tree's core at `bce10d4a1` returns 9,897 characters at a 63-character root, 9,934 at 100, 9,999 at 165 and 10,000 at 166. A clone at 55 characters under a 63-character running root returns 9,964 (executed, `## Probes`). These are the figures of `changelog.md:3`, `trail/phases/phase-1.md:14` and `frame/design.md:31`. The phase's S2 claim, 65 characters left at `ROOT_ROOM`, is 10,000 less 9,934 less 1 (read against the executed figure).

What matched: S1 and S5. In this round's clone, 177 characters deep, `bin/test tests/lib/test_core.py tests/hooks/test_core_start.py -q -p no:xdist` passed 30 cases at `bce10d4a1`. With `if len(out) < CAP:` replaced by `if True:` in the clone's `lib/core.py`, `test_refuses_to_print_a_core_whose_whole_output_reaches_the_cap` failed alone. That is mutation (4) of `trail/phases/phase-1.md:13` (executed, `## Probes`). The clone's output passes `CAP` there, so the hook case `test_accepts_a_session_in_a_clone_of_the_plugin_with_the_clones_core` ran in the branch of *Scope* item 2 and passed. That is the claim of `trail/phases/phase-1.md:11` that it holds either output (executed). The other mutation rows of `phase-1.md:13` were not run again. S6: `git grep -n -e 'spelled absolute' -- . ':!seal/threads'` prints nothing and exits 1 (executed). S7: `git log --diff-filter=A` names `bb7168b57` for `changelog.md`, and `git show --stat bb7168b57` names `.claude-plugin/plugin.json`, now `0.39.3`. That is the milestone `release: 0.39.3` (executed: `gh issue view 1641 --json milestone`).

What matched: `frame/questions.md` Q1, judged from the text a session holds, and not measured. In the plugin's own branch the first line reads "AgenticSeal core from `<root>/skills/core/SKILL.md`, plugin 0.39.3." The core's opening paragraph follows it, and says each path is "relative to the plugin's root, the directory holding this file's `skills/`, never to the session's repository" (`skills/core/SKILL.md:18-21`). The closing sentence "Both paths are relative to the plugin's root." uses the core's own term, and the core defines that term against the file the first line names. So the root has one value in the output, and the core's own clause rules out the repository. That clause speaks of the paths "this file cites", and the closing line stands outside the file. A session that does not carry the definition across has the first line's path as the one root in its context. In a clone's branch and past the cap, the closing line spells the root out. It uses "the running plugin's root", a term the core does not define, so it does not clash with the core's definition, which there names the clone. Each branch gives one reading. Whether a real session takes it is the measurement `gaps.md:7` gives the orchestrator or the repository owner (`## Not judged`).

What matched: the tests against their groups. `bin/seal layout --pairs tests/lib/test_core.py tests/hooks/test_core_start.py` printed 0 pairs (executed). `Test_closing` and `Test_whole` each state in their docstring the input their two cases differ by, as `CONTRIBUTING.md` *The test layout* asks. No new case repeats another in its class. Two new cases have no docstring, `Test_whole.test_refuses_the_plugins_own_sentence_where_a_root_is_given` and `Test_rendered.test_accepts_a_core_one_character_under_the_cap_whole` (`tests/lib/test_core.py:211`, `:275`). No rule the round found asks a case for one, and this round opens no finding on it.

What matched: `frame/questions.md` Q2 as `trail/phases/phase-1.md:5` answers it. The search it names, run again at `bce10d4a1`, prints calls in `lib/core.py`, `skills/verify/scripts/payload_meter.py`, the three test files and the unrelated names in `lib/lines.py`, `tests/lib/test_lines.py` and `tests/gfm_table_oracle.py` alone (executed). `git grep -n -F -e "Where a request to change code" -e "closing line"` outside `seal/threads/` prints no copy of the closing line's text outside `lib/core.py` (executed).

What matched: the two failures `trail/phases/phase-1.md:15` reports from its boundary set. `tests/behaviour/test_every_tracked_file_meets_every_census.py` and `tests/behaviour/test_chain_hooks_hardening.py` pass at `bce10d4a1`, 24 cases (executed). `gaps.md` exists, and `frame/design.md:30` names the home by the placeholder `<home>` since `5a0909a80`.

What matched: *Scope* item 7. `README.md:347-350` and `README.ko.md:346-349` gain the sentence the item words, and `CONTRIBUTING.md:531-535` the weighing (read). `gaps.md:8`'s answerer is real: `.github/workflows/test.yml` runs its Windows legs on every `pull_request` event, a pull request into `release/*` included (read, `:3-12`, `:38-84`).

What matched: `pr.md:1-3` quotes `frame/plan.md:50`, `:50` and `:52` word for word (read). `changelog.md` states the measured lengths as measurements of 2026-11-27 and corrects the issue's figures (read). The issue's body now carries that correction in a note dated 2026-11-27 (executed: `gh issue view 1641 --json body,comments`). The sentence of `frame/design.md:29` that begins "The issue states that the root occurs once" says what the issue held when the framer read it. That section is dated to `7f388fa1f`, and the issue's own note explains the change, so this round opens no finding on it.

What matched: no other work item's frame in the tree changes what this one cites. `grep -n -F` for `lib/core.py`, `core-start` and the cap case over `seal/threads/*/frame/design.md`, outside this item, prints grounding rows of earlier releases' items and no rule change (executed). The release's parallel items stand on other branches, and `frame/plan.md:41-46` says they meet this work only through the cap case.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `bce10d4a1` beyond the five modules this round ran | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, after the findings are closed |
| Whether a fresh session in a repository that is no clone of the plugin opens `skills/implement/orchestration.md` under the plugin's root (`frame/questions.md` Q1). The round judged the text's reading, not a session's behaviour | `lib/core.py:87`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/gaps.md:7` | a measurement, run by the orchestrator or the repository owner |
| Whether the closing line's paths keep `/` on Windows, where the `os.path.join` mutant survived on macOS | `lib/core.py:84`, `tests/lib/test_core.py:168-181` | CI's Windows legs on the pull request |
| Whether the harness counts the newline the hook writes after the output, at an output of 9,990 to 9,999 characters. `CAP`'s comment puts the cap between 9,990 and 10,010, and `rendered` and the cap case compare the output without the newline against 10,000 | `lib/core.py:51-55`, `lib/core.py:172`, `hooks/core-start.py:44` | a measurement, run by the repository owner |
| The phase's boundary-set count, 1,558 passed, 11 skipped and 2 failed (`trail/phases/phase-1.md:15`), and its mutation rows other than (4), which this round did not run again because they are wider than the narrow form | `seal/threads/1795759278-the-cores-margin-depends-on-the-path/trail/phases/phase-1.md:13-15` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/lib/test_core.py tests/hooks/test_core_start.py tests/skills/test_payload_meter.py -q -p no:xdist`, in this worktree | 75 passed, exit 0 |
| `bin/test tests/lib/test_core.py tests/hooks/test_core_start.py -q -p no:xdist`, in a `git clone --no-local` at `bce10d4a1` whose root is 177 characters long | 30 passed, exit 0 |
| The same command in that clone, with `if len(out) < CAP:` in `lib/core.py#rendered` replaced by `if True:`, then restored with `git checkout` | 1 failed, `Test_rendered::test_refuses_to_print_a_core_whose_whole_output_reaches_the_cap`; 29 passed |
| `python -I -c` importing `lib/core.py` and printing `len(core.whole(...))` for the tree's core at roots of 63, 100, 165 and 166 characters, and for a 55-character clone under a 63-character running root | 9897, 9934, 9999, 10000; 9964 |
| `bin/test tests/behaviour/test_every_tracked_file_meets_every_census.py tests/behaviour/test_chain_hooks_hardening.py -q -p no:xdist`, in this worktree | 24 passed, exit 0 |
| `bin/seal payload --agent proofer`, in the 177-character clone and in this worktree | the `SessionStart hook: skills/core/SKILL.md` row reads 932 bytes in the clone and 9,935 in this worktree, with the same note naming the core below its frontmatter |
