# Review round 1: 1795742080-a-session-is-bound-by-the-crafters-rules

```seal
target: 342a46f31 against origin/release/v0.39.2
```

This round reviewed the branch at `342a46f31` against `origin/release/v0.39.2`, which stands at `6bd4f4426` and was merged into the branch at `69a3517bd`. The code reviewed is the work item's own diff, `git diff origin/release/v0.39.2...HEAD`, and the merge's resolution, `git show 69a3517bd`. The resolution keeps both sides of `seal/follow-up.md` and adds nothing of its own (executed). The text the merge brought, #1633's and #1632's, is not reviewed here. The work item's diff and records are held against the merged tree, the merged core row *No fix that no round reads* and contract rule 19 among it.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md` whole at `342a46f31`. The commit language and the record language are both English, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared, so no parity comparison is owed. There is no earlier round, so nothing was carried.

The issues were read with their comments (`gh issue view <N> --json title,body,comments` for 1624, 1628 and 1629). #1624's one comment is round 4's paste-ready rewording, which *Scope* item 2's account rule supersedes, as `frame/design.md` G19 says.

The question the spawn asked this round to weigh is whether the change reaches the orchestrator's own record-writing or only a builder's. It reaches the builder's read through `seal range` and the account's rule. It reaches the orchestrator's own records through one sentence of step 1 of `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* (`:36-40`), which binds them to contract rules 4 and 5, and through no command. The builder's read runs at a phase's or a pass's close. The orchestrator's *Judgments of the run* rows, its folds and `pr.md` are written after that read, so no `seal range` file prints them. In this run the orchestrator's records drew two corrections it made itself before this round. `ecbbfa0a9` corrected the row that said the framer folded the routing sentence, and `04b93478f` corrected the follow-up row's release name. This round finds one more, finding 6, in a row written at `1c045ac40`. That row predates the step 1 sentence, which `671dd2c17` wrote. The `f09656b7b` row came after the sentence and still needed `ecbbfa0a9`. The frame's grounds for this half, `frame/plan.md` row 14 and S9, are that the step 1 sentence binds the orchestrator and that the rounds and the sealer catch a breach. Those grounds hold for what they claim, since this round caught finding 6. Nothing counts that half, though. `frame/questions.md` Q1 and the rewritten `seal/follow-up.md:48` count only the builder's read and its account. That question is a row of `## Not judged`.

## Findings

### 1. `seal range` exits 2 and writes no file when the range moves a submodule's pointer

```seal
severity: should
location: `skills/implement/scripts/range_read.py:229-232`, `skills/implement/scripts/range_read.py:408-421`, `skills/implement/scripts/range_read.py:30-31`, `tests/skills/test_range_read.py`, `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md:99`, `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md:115`
evidence: executed `bin/test tests/skills/test_tmp_range_probe.py -q -s -p no:xdist` in a clone at `342a46f31` (the probe of `## Probes`, row 1); read `skills/implement/scripts/range_read.py:229-232`, `:341-354`, `:397-421`
```

Why it matters: `skills/implement/SKILL.md:269-276` has every builder run `seal range` after its last commit and read the file it writes. In a repository whose range moves a submodule's pointer, the command refuses the whole read and writes nothing. The builder then has no file to read and no `seal range` line to quote in its account. A submodule's pointer is an ordinary change, and the plugin runs in users' repositories.

The grounds. `_changed` (`:229-232`) reads `--name-status`, which gives a status and no mode. `_read` (`:408-421`) sends every path that is neither deleted nor binary to `_prose`. `_prose` asks `git cat-file blob <head>:<path>` (`:347`), and for a submodule that entry is a commit, not a blob. The probe planted a real submodule and moved its pointer in the range. The command printed ``seal range: `git cat-file blob <head>:sub` exited 128: fatal: ... bad file``, exited 2, and wrote no file. *Data & interfaces* (`frame/design.md:115-117`) names a binary path and a deleted path as not printed, and keeps exit 2 for an input it cannot read. A gitlink is neither: git answered every question correctly, and the script asked the wrong one. The frame does not name the gitlink case, so the fold owes `frame/design.md:99` (S6) and `:115` a gitlink beside the binary path and the deleted path.

The fix reads each path's modes and names a gitlink as not printed, as the script already names a binary path:

```python
# The mode git gives a submodule's entry, which holds a commit and no text.
GITLINK = "160000"

SUBMODULE = "==> {path}: submodule, not printed <=="


def _changed(root, start, head):
    """`[(path, status, gitlink)]` of each path the range changes, in git's
    order; GITLINK holds where either side of the path is a submodule's
    commit."""
    fields = _fields(_git(root, *DIFF, "--raw", "-z", start, head))
    changed = []
    # `--raw -z` prints `:<old mode> <new mode> <old> <new> <status>` NUL
    # `<path>` NUL, one path each, since DIFF holds `--no-renames`.
    for meta, path in zip(fields[0::2], fields[1::2], strict=True):
        old_mode, new_mode, _old, _new, status = meta.lstrip(":").split(" ")
        changed.append((path, status, GITLINK in (old_mode, new_mode)))
    return changed
```

```python
    for path, status, gitlink in _changed(root, start, head):
        if status == "D":
            lines.append(DELETED.format(path=path))
            summary.append(NOT_PRINTED.format(path=path, why="deleted"))
        elif gitlink:
            lines.append(SUBMODULE.format(path=path))
            summary.append(NOT_PRINTED.format(path=path, why="submodule"))
        elif path in binary:
```

The docstring's list at `:30-31` gains the submodule beside `BINARY` and `DELETED`. The case goes into `tests/skills/test_range_read.py` beside the binary case. It plants the gitlink in the index, so it needs no second repository. This round did not run it:

```python
    def test_accepts_a_submodule_by_name_and_does_not_print_it(
        self, tmp_path, monkeypatch, capsys
    ):
        """S6: a path that holds a submodule's commit is named in the file
        and in the summary, and the read goes on past it."""
        repo, base = built(tmp_path, {})
        # A gitlink entry, the one a submodule's pointer is; its commit need
        # not exist here, since no command of the range reads it.
        git(repo, "update-index", "--add", "--cacheinfo", f"160000,{base},sub")
        git(repo, "commit", "-qm", "a submodule")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        assert RANGE.SUBMODULE.format(path="sub") in written(out)
        assert RANGE.NOT_PRINTED.format(path="sub", why="submodule") in said
```

The fix crosses no OS boundary. It reads only what git prints.

### 2. No case holds **A new test starts from its group** where it now stands, and removing it leaves the suite green

```seal
severity: should
location: `tests/text/test_a_moved_rule_leaves_its_definition.py:194-203`, `skills/implement/SKILL.md:192-196`, `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md:74`
evidence: executed a removal of `skills/implement/SKILL.md:192-199` in a clone at `342a46f31`, then `bin/test` over the twenty test files `git grep -l -E "skills/implement/SKILL.md|\"implement\", \"SKILL.md\"" -- tests` lists, `tests/text` and `tests/test_censuses.py` (941 passed, exit 0), then restored (the probe of `## Probes`, row 2); executed `git grep -n -F -e 'starts from its group' -e 'seal layout --pairs' -- tests`
```

Why it matters: #1629's last *Done when* line asks that "A case holds each binding", and its list names *A new test starts from its group*. After the move, the rule binds an orchestrator that builds only because its paragraph stands in `skills/implement/SKILL.md`. The only case that names it, `MOVED_OUT_OF_CRAFTER`'s entry (`:53`), holds that `agents/crafter.md` does not carry the rule. No case holds that `skills/implement/SKILL.md` does, so a later trim can drop the rule with every case green. That is #107's failure, which `test_the_crafters_rules_name_what_their_readers_resolve`'s docstring names.

The grounds. *Scope* item 8 (`frame/design.md:74`) gives cases to the moved rules that had cases in `agents/crafter.md`, and this rule had none there. The issue's line asks for a case for each binding, so the frame is weaker than the issue here and does not say why. The probe removed the paragraph together with **The build holds to the request** (`:198-199`), and every file that reads the skill stayed green. The search on the evidence line prints only the `MOVED_OUT_OF_CRAFTER` entry. **The build holds to the request** is unpinned too, but it holds no path or code span a reader resolves. `docs/running/what-a-script-gates.md` *The checks* has a text case pin a fact and not wording, so this finding asks the case of the group rule alone.

The fix adds the rule to `BUILDERS_RULES`, which `test_the_crafters_rules_name_what_their_readers_resolve` already walks in `skills/implement/SKILL.md`. The fix pass shows it red with only the paragraph removed. The fold names the case in *Scope* item 8.

```python
BUILDERS_RULES = {
    # The lead `skills/verify/scripts/mutation_check.py` and step 6 of
    # `agents/crafter.md` cite in italics.
    "Commit before you mutate, and restore from `seal mutate`'s copy.": (
        # The command whose revert the rule warns of, and the command whose
        # copy restores the file.
        "`git checkout -- <file>`",
        "`seal mutate`",
    ),
    # #1629 listed it among the rules that bound no orchestrator that builds.
    "A new test starts from its group.": (
        # The command a builder runs for a new case's group where the test
        # files declare `TARGET`.
        "`seal layout --pairs`",
    ),
}
```

### 3. `skills/code-review/orchestration.md` still says a crafter's hand-back carries "the method of its read"

```seal
severity: should
location: `skills/code-review/orchestration.md:94-97`
evidence: executed `git grep -n -i -e 'method of its read' -e 'method of the read' -e 'names the method' -e 'method of its reading' -- ':!seal/threads'`; read `skills/code-review/orchestration.md:90-100`, `skills/implement/SKILL.md:302-312`
```

Why it matters: the orchestrator reads this paragraph for what a crafter's hand-back holds before it folds and spawns the verifying round. The account's new rule (`skills/implement/SKILL.md:302-312`) has the account quote its commands and describe no read in other words. This sentence still asks for "the method of its read", the description #1624 found false three rounds running. So it states, in the section the diff edited, the old fact the work replaced. An orchestrator that reads it takes a described method as the account.

The grounds. The search prints this line and `skills/agent-contract/SKILL.md:141`. Contract rule 12's "names the method" is the enumeration method of a class, not the account of a read, so it stays. The search is a sample under contract rules 12 and 19, since a statement in other words escapes it. The rest of the paragraph already calls the hand-back "that account", which the fix keeps.

```markdown
a later round; that is contract rule 12. A crafter's hand-back carries
the account of its read of its range and the work item's records that
`skills/implement/SKILL.md` *The account of that read quotes its commands
and describes no read in other words* states, each frame or `routing.md`
statement that read names, and the sample of statements across the tree,
as contract rule 12 asks of the party that fixes. The
round that follows reads that account as a claim. Where the hand-back names
```

### 4. `changelog.md` says `agents/crafter.md` cites each moved rule at the step that applies it, and it cites four of them

```seal
severity: should
location: `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/changelog.md:3`
evidence: executed `git grep -n -F -e 'starts from its group' -e 'holds to the request' -e 'Find the runner' -e 'Commit before you mutate' -e 'Mutation-test every unit' -e 'judged before it is built' -e 'Before the builder closes' -e 'The account of that read' -- agents/crafter.md`, `grep -rn -F -e "cites each" -e "at the step that applies" seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/`; read `agents/crafter.md:31-79`
```

Why it matters: the fragment becomes the release note. Its first item names seven rules and then says "`agents/crafter.md` cites each of them at the step that applies it". A reader takes that to mean each step points at its rule.

The grounds. The first command prints the citations step 3 (`:40`), step 6 (`:55-56`) and step 10 (`:72-75`) make. They cite the frame rule, the two mutation rules, the rule on the read and the account's rule. No step cites **A new test starts from its group**, **The build holds to the request** or **Find the runner, and type the narrow form**. Step 5 (`:48-50`) cites *2. Implement test-first, and let each rule name its test*, the section that holds the first two. Step 7 (`:58-60`), the step that applies the runner rule, cites no rule, where the old **Find the runner** paragraph had named "step 7's one command". *Scope* item 3 (`frame/design.md:65`) asks only that steps 3, 6 and 10 cite, so the build holds to the frame and the fragment says more than the build did. The second command prints only this line.

```markdown
`agents/crafter.md` opens the file at step 1, and cites the frame rule at step 3, the two mutation rules at step 6, and the rule on the read with the account's rule at step 10.
```

The sentence replaces "`agents/crafter.md` cites each of them at the step that applies it." in `changelog.md:3`.

### 5. The rule change's `to` repeats the opening of `skills/verify/seal-mutate.md`, so after the settle one fact stands in two files

```seal
severity: should
location: `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md:133`, `skills/verify/seal-mutate.md:3-6`, `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md:72`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.2 --root <the branch worktree> --worktree`, `git grep -n -F -e "the orchestrator that builds itself" -- .`; read `docs/running/what-a-script-gates.md:69`, `skills/verify/seal-mutate.md:1-6`
```

Why it matters: the check printed, at `frame/design.md:133`: "this `to` repeats a passage of `skills/verify/seal-mutate.md`: 1 of its runs of 15 words stand there, one of them "the builder, the crafter or the orchestrator that builds itself, at each unit that adds"". `agents/proofer.md` step 7 makes a `to` that repeats a passage another file keeps after the settle a finding. Once the settle writes the row of `seal mutate` in `docs/running/what-a-script-gates.md` *The checks*, the list of who runs the command stands there and in the opening of `skills/verify/seal-mutate.md`. The next change to who mutates has to find both. This work's own change had to find both: it edited both, in the same words.

The grounds. `docs/running/what-a-script-gates.md:69` is the table whose rows say who runs each check, and it is the fact's home. `skills/verify/seal-mutate.md` is opened by a party already about to run the command. That party gains nothing from the list, and a pointer to the row tells any other reader where it stands. *Scope* item 7 (`frame/design.md:72`) asks `seal-mutate.md` to name the builder, so the fold rewrites that clause with this fix. The second command prints only these two places. It is a sample, since a statement in other words escapes it.

```markdown
A party that proves condition 2 of `skills/verify/SKILL.md` *2. Able to
fail* for one unit opens this file before it runs `seal mutate`. Who runs
it, and at which step, is the row of `seal mutate` in
`docs/running/what-a-script-gates.md` *The checks*. It holds the command,
its verdicts with their exit codes, and its bound.
```

The fold's clause for *Scope* item 7: "`skills/verify/seal-mutate.md:3-5` cites the row of `seal mutate` in `docs/running/what-a-script-gates.md` *The checks* for who runs the command, in place of naming the crafter."

### 6. Both rows of *Judgments of the run* state what a fold commit changed, and `git show` of each commit says otherwise

```seal
severity: should
location: `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/plan.md:75`, `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/plan.md:76`
evidence: executed `git show 53883c4e2 -U0 --format=`, `git show 53883c4e2 --word-diff=plain -U0 --format=`, `git show f09656b7b -U0 --format=`, `git show --stat 53883c4e2 f09656b7b`; read `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/trail/phases/phase-2.md:7-18`
```

Why it matters: the settle reads these rows against what each judgment cost and caught (`skills/core/SKILL.md` *The first value: efficient development through the AgenticSeal process*, the paragraph opening **A judgment stands on a source document**). A row that misstates what a fold changed gives the settle a wrong record. These are also the orchestrator's records that step 1's sentence on contract rules 4 and 5 now binds. Each fact such a row states of a commit is one a command printed.

The grounds. The set is closed: the section holds these two rows, and the finding reads both.

- Row 1 (`:75`) says of `53883c4e2` that "The four other folded lines record what phase 1 built and change no phase-2 item". The commit changes eight lines of `frame/design.md` and three of `frame/plan.md`. *Scope* item 10's lines are `:77`, S11 at `:102`, rows 18 and 19, and most of the phase-2 row. Five lines record what phase 1 built and touch nothing of item 10: *Scope* item 1's `SHIPPED` row (`:58`), S5, S6, the exit line of *Data & interfaces*, and the `seal range` rule change's `to`. A sixth, the output line of *Data & interfaces*, holds both the local-mode clause and item 10's widening. The phase-2 row also gains `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`, which phase 1 named for the next phase. So "four" holds under no count of the commit's lines.
- Row 2 (`:76`) says "the framer folds what the phase-2 crafter names" and lists Q2, *Scope* item 6's sentence and the two amendments. The same commit also folds two more things the phase-2 record names: *Scope* item 4's "the newest block of `guarantee.md`" wording (`phase-2.md:18`), and *Scope* item 8's case of `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` (`phase-2.md:8`). The row lists neither, so a reader of the row takes the list as whole.

The rows are the orchestrator's to write, so this finding goes to the orchestrator. It is located in the work item's records alone.

```markdown
| 2026-11-27 | After phase 1, the framer's fold at `53883c4e2` is taken, and it widens phase 2 by *Scope* item 10: a hunk of prose inside a non-Markdown file is widened to its blank-line bound where `git diff -W` stops short of it. Its other lines record what phase 1 built and change no *Scope* item of phase 2: *Scope* item 1's `SHIPPED` row, S5, S6, the output and exit lines of *Data & interfaces*, and the `seal range` rule change's `to`. The phase-2 row also gains the test file phase 1 named for the next phase | <the row's grounds as they stand> | <as it stands> |
```

```markdown
| 2026-11-27 | After phase 2 and the merge of the release branch at `69a3517bd`, <as it stands up to "the framer folds what the phase-2 crafter names:"> `frame/questions.md` Q2, which `trail/phases/phase-2.md` answers, and the case of `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` that answer names; *Scope* item 4's commit of a sealer's verdict, as the newest block of `guarantee.md` names it; *Scope* item 6's sentence on rules 4, 5, 19 and 21, which step 1 no longer states as one list; the two amendments *Scope* items 5 and 6 did not name. <the rest of the row as it stands> |
```

The angle-bracketed spans stand for the cells' text as it stands at `342a46f31`. The fix pass copies each one from `frame/plan.md:75-76` and replaces only the named sentence.

## Confirmations

What matched: the acceptance searches of `frame/design.md` G18 at `342a46f31`. V1, V3 and V4 print nothing. V2 prints `skills/implement/SKILL.md:167`, `:192`, `:201`, `:244` and `:249` alone, as `trail/phases/phase-2.md:44` claims for `b6816d2b0`. The same five lines print at both commits (executed, with G18's commands).

What matched: the moved rules. Each paragraph *Scope* item 2 moves stands in `skills/implement/SKILL.md` *Procedure* said of the builder (`:122-135`, `:167-174`, `:192-208`, `:244-263`, `:269-312`). Each left `agents/crafter.md` with its *Never* line, and steps 3, 6 and 10 cite them as *Scope* item 3 asks (read). The builder paragraph's clause on rules that withhold an act from every agent answers the reading `trail/phases/phase-2.md:14` names. Without it, contract rule 2 would withhold the broad gate from the orchestrator (read: `skills/agent-contract/SKILL.md` rules 2 and 6).

What matched: the crafters' open claims. Phase 2's two amendments are folded at `frame/design.md:67` and `:70`. `MOVED_OUT_OF_CRAFTER` names the frame rule by its bold lead, `tests/text/test_a_moved_rule_leaves_its_definition.py:57`, and step 3 cites it in italics without the bold marks, so the entry holds. *Scope* item 8 at `frame/design.md:74` now says "a phrase its paragraph held" (read). The Windows row of `gaps.md:8` names an answerer that runs: `CONTRIBUTING.md` *Opening a pull request* says every push to an open pull request into the release branch runs the suite on Linux and Windows, and `.github/workflows/test.yml:81-84` holds the Windows shards (read).

What matched: the byte counts `trail/phases/phase-2.md:8` gives. They are 9219 to 5815 for `agents/crafter.md`, 22290 to 28907 for `skills/implement/SKILL.md` and 9404 to 8808 for `skills/implement/fix-pass.md` (executed: `git show <commit>:<path> | wc -c` at `1c045ac40` and `d48344a1f`).

What matched: `frame/plan.md` *Overlap with the release*. `git show --stat 0cde8c58f` prints `skills/agent-contract/SKILL.md`, `seal/follow-up.md`, `tests/text/test_the_rules_have_one_owner.py` and two templates outside its records. `git show --stat 6bd4f4426` prints `agents/proofer.md`, `agents/sealer.md`, `skills/core/SKILL.md`, `chain_check.py`, `seal/follow-up.md` and two test files. Neither touches a file this work changes but `seal/follow-up.md` and `tests/text/test_the_rules_have_one_owner.py`, as the rows say (executed). The merged core row *No fix that no round reads* is cited by name in this work's files and restated by none (executed: `git grep -n -F -e 'records alone' -e 'No fix that no round reads'` over the files the diff changes).

What matched: `seal range` on the inputs the frame names. The narrow set ran green: `bin/test tests/skills/test_range_read.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/behaviour/test_a_reference_root_is_read_and_never_taken.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/skills/test_mutation_check.py -q` gave 359 passed and 9 skipped, exit 0 (executed). The round read `range_read.py` whole. The `-U0` hunk numbering, the deletion anchor, the join of meeting spans, the old-side offset and the verbatim `-W` branch agree with *Data & interfaces*. The header and the exit codes do too (read). Every git command goes through `lib/gitcmd.py#git`, which builds the command with `argv`, and takes paths from `-z` output (read: `:151-154`, `:229-242`, `:388-394`).

What matched: `gaps.md` labels the suite `unverified` with the orchestrator as its answerer (`:7`), so the label is honest.

Three things this round saw and opens no finding for. A file that becomes a symlink prints its two `-U0` diffs as one hunk, under the first header, with the second diff's header lines inside it. Every line still prints, so nothing is missed (the probe of `## Probes`, row 1). A fix pass's range that holds a merge of the base makes `seal range` print the merged-in text too. The rule then has the builder read other work items' records to the file's last line. That costs lines and misses none. `frame/plan.md` *Technical context* names large ranges and not this one. Last, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py#test_crafter_cites_the_handoff_for_the_narrow_form` keeps a name that says the crafter, while it now reads the builder's rule in `skills/implement/SKILL.md`. Only the case's next editor reads that name.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether step 1's sentence on contract rules 4 and 5 needs a count of its own beside `frame/questions.md` Q1. Q1 and `seal/follow-up.md:48` count only the builder's read. This run's record so far is finding 6 here, and the two corrections `ecbbfa0a9` and `04b93478f` the orchestrator made before this round | `skills/implement/orchestration.md:36-40`, `seal/follow-up.md:48`, `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/questions.md:14` | the orchestrator, with the framer at the fold |
| `seal range` on Windows | `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/gaps.md:8` | CI's Windows leg |
| The mutation runs phases 1 and 2 report (36 mutants at `7efa46e24`, then 11 of 11) and the phase-boundary run of 1602 passed at `b6816d2b0`, which this round did not re-run | `trail/phases/phase-1.md:24-30`, `trail/phases/phase-2.md:22-28`, `trail/phases/phase-2.md:46` | the sealer, at step 4 of `agents/sealer.md` |
| The full suite, the repository-wide lint and the format check | the work item's tree | the orchestrator, at the broad run once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_range_probe.py -q -s -p no:xdist`, in a clone at `342a46f31`: one case builds a submodule and moves its pointer in the range, the other turns `docs/a.md` into a symlink | Both cases ran, exit 0. Submodule: `seal range` exited 2, printed `` `git cat-file blob <head>:sub` exited 128: ... bad file `` and wrote no file. Symlink: exit 0, the file holds both diffs of `docs/a.md` under one `@@ -1 +1 @@` header, every line present |
| A removal of `skills/implement/SKILL.md:192-199` in the same clone, then `bin/test` over the twenty test files that read the skill, `tests/text` and `tests/test_censuses.py`, then the paragraph restored | 941 passed, exit 0: no case reads **A new test starts from its group** or **The build holds to the request** in the skill |
