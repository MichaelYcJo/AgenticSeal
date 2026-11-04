# Review round 2: 1793833679-update-reads-the-config-dir-in-use

```seal
target: f8ed5efc, fixes e4db4f10..f8ed5efc
```

This is a verifying round. It read the diff of the fixes, `e4db4f10..f8ed5efc`,
in the repository's checkout of the branch, as the spawn prompt named it.
The range holds the fix pass (c2a1f208), round 1's two close blocks
(43e5359e) and the orchestrator's fold (f8ed5efc). `git diff --stat` over
the range lists `skills/update/SKILL.md`, the new module
`tests/behaviour/test_update_reads_the_config_directory_in_use.py`, and
the work item's `changelog.md`, `gaps.md`, `frame/design.md`,
`frame/plan.md` and `trail/rounds/round-1.md` (executed).
`tests/behaviour/test_the_old_block_leaves_through_update.py` is outside
the range, so step 4 and its case were not reviewed again.
`seal/parity.md` is not declared, and `seal/config.md` has no
`Record language` row, so the record is in English.

Carried from round 1, not re-established: the needles of
`tests/behaviour/test_release_hygiene.py` that `frame/design.md` G8 lists
for steps 2b and 3. This round ran the two cases rather than reading them
again. Also carried is round 1's reading of `skills/core/SKILL.md` *The
rule a mechanism is kept against*, which finding 2's close accepts.
Re-established here: every verdict below, round 1's finding 2 mutation
command, run again, and the narrow runs.

## Findings

### 1. The repair block prints a repair whose `rsync` copies into `/` when its read of the install record fails

```seal
severity: should
location: `skills/update/SKILL.md:62-72`, `tests/behaviour/test_update_reads_the_config_directory_in_use.py:85-115`, `seal/threads/1793833679-update-reads-the-config-dir-in-use/frame/design.md:65-70`, `seal/threads/1793833679-update-reads-the-config-dir-in-use/changelog.md:3`
evidence: executed a `test_tmp_` probe that ran the repair block from the skill under `bash -c` with neither directory holding `installed_plugins.json`: exit 0, stdout `mv '' .stale.bak`, then `rsync -a --exclude .git <config>/plugins/marketplaces/agenticseal/ /`, then `mkdir -p /.in_use`, and a `FileNotFoundError` on stderr; read `skills/update/SKILL.md:57-60`, `:70-71`, `seal/threads/1793833679-update-reads-the-config-dir-in-use/frame/plan.md:13`, `seal/threads/1793833679-update-reads-the-config-dir-in-use/gaps.md:8`
regression: round-1#1
```

The unit is step 2b's repair block (`skills/update/SKILL.md:69-72`), which
c2a1f208 added. The frame says a failed read of the install record makes
step 2b stop loudly (`frame/plan.md:13`), and that this block reads the
record and prints the repair with the session's paths
(`frame/design.md:65`). The fix made a block whose `printf` runs whatever
the read returned. So on a failed read it exits 0 and prints a repair
whose `rsync` target is `/`. The defect came from round 1's paste-ready
snippet, which c2a1f208's close says was applied as given.

Why it matters: this is the defect round 1's finding 1 named, the printed
`rsync` copying into `/`, reached by another path. Before the fix, the
user's empty `$p` produced the `/`. Now the session's own output spells
`/` and hands it over as the repair to type. The block's read fails
wherever step 2b's first read fails, because both run the same program on
the same path. The mismatch table (`:57-60`) has a row for a matching
version and one for a mismatch, and none for a read that raised. A session
that takes "no version could be read" for a mismatch runs this block.
`gaps.md:8` names one way to get there that this work item has not ruled
out. If a session's Bash call does not inherit `CLAUDE_CONFIG_DIR`, both
reads go to `$HOME/.claude`. A user who keeps everything under the config
directory has no record there. The plan's own failure scenario,
Claude Code moving its plugins (`frame/plan.md:13`), is another.

The fix ends the read with `&&`, so the `printf` runs only on a read that
succeeded. A line ending in `&&` continues onto the next line in bash and
zsh. Under both shells, a failed read printed nothing and exited 1, and a
read of a path with a space printed it quoted (executed). The two lines
still open with `p=$(` and `printf`. A `bin/seal mutate` run that
applied this edit to the skill left the repair case, the search case and
the hygiene case of step 2b green, so no current pin refuses it
(executed). The block's precondition is a POSIX `sh`-family shell. The
skill's fences are bash, and no other shell is assumed. This text replaces
`skills/update/SKILL.md:64-72`:

````markdown
directory a session may be holding. The user's terminal holds neither `$p`
nor, unless it is exported there, `CLAUDE_CONFIG_DIR`. So the block below
reads the copy again and only prints the repair, with this session's paths
written out and quoted; give its output to the user to type. Where the read
fails, the block prints nothing and fails: say that the installed copy could
not be found, and give no repair.

```bash
p=$(python3 -c "import json,sys;d=json.load(open(sys.argv[1],encoding='utf-8'));print(d['plugins']['agentic@agenticseal'][0]['installPath'])" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/installed_plugins.json") &&
printf 'mv %q %q\nrsync -a --exclude .git %q %q\nmkdir -p %q\n' "$p" "$p.stale.bak" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/marketplaces/agenticseal/" "$p/" "$p/.in_use"
```
````

And this case goes after `test_step_2b_prints_the_repair_with_this_sessions_paths`.
Against the skill at f8ed5efc it fails at its first assertion, because
the probe above read exit 0 there. The fix pass still shows it red itself
(contract rule 15).

```python
def test_step_2b_prints_no_repair_where_the_record_cannot_be_read(tmp_path):
    """Round 2 of #1184, finding 1. Where the install record cannot be read,
    `p` is empty, and a repair printed from it would copy the clone into
    `/`. So the repair block prints nothing and fails."""
    home, config = tmp_path / "home", tmp_path / "config"
    home.mkdir()
    config.mkdir()
    block = FENCE.findall(step("2b", "3"))[1]
    out = run_bash(block, home, config, tmp_path)
    assert out.returncode != 0, out.stdout
    assert out.stdout == "", out.stdout
```

The snippets do not cover every statement of this fact. The fix pass also
owes the fragment's sentence "The block itself runs nothing that deletes"
(`changelog.md:3`), which should also say that the block prints nothing
where it cannot read the record. The block shown in `frame/design.md`
*Data & interfaces* (`:65-70`) is a frame statement, which the fix pass
names for the orchestrator to fold.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the printed repair no longer depends on `$p` or on
`CLAUDE_CONFIG_DIR` in the user's terminal. The block at
`skills/update/SKILL.md:69-72` reads the record in the session's shell and
prints `mv`, `rsync` and `mkdir` with the paths written out and quoted by
`printf %q` (read). The crafter claimed that the new case
`test_step_2b_prints_the_repair_with_this_sessions_paths`
(`tests/behaviour/test_update_reads_the_config_directory_in_use.py:85-115`)
reads the three printed lines back with `shlex.split` and names the config
directory's clone and the copy its record names, each at a path holding a
space. The case does that (read), and it passes (executed). The crafter
claimed three mutants of the block red. This round ran them again in one
`bin/seal mutate` batch: the printed `rsync` source rewritten to
`${HOME}/.claude/...`, the block's record read rewritten to
`${HOME}/.claude/...`, and `%q` rewritten to `%s` for the `mv` and `rsync`
lines. A fourth mutant, the `mkdir` argument rewritten from `"$p/.in_use"`
to `"$p"`, went in the same batch. All four read `red` (executed). The
crafter claimed the case red against e4db4f10 at `assert 3 == 2`. The
skill's repair fence at e4db4f10 held three lines, so the case's line count
fails there before it runs anything (read in the diff). The run went to a
second shell too. A probe ran the block under `zsh -c` with the spaced
paths, and `shlex.split` read the same three commands as under `bash -c`
(executed). The mismatch row at `:60` and the cautions' `mv` at `:76` take
the wording round 1 gave (read). The fragment's step 2b sentences say what
the repair did and what it does now (`changelog.md:3`, read). The close
listed the repair's other statements by wording. `git grep` on
`stale.bak`, `"$p/"`, `repair below`, `print the repair` and the `mv`
above, outside the round records, finds only the skill, the new case and
the block in `frame/design.md` *Data & interfaces*, which f8ed5efc folded
(executed). The close holds for the defect the finding named. Finding 1
above is a defect of the new block, and it names this finding on its
`regression:` line.

```seal
confirms: round-1#2
```
What holds: `test_the_skill_names_no_fixed_claude_directory`
(`tests/behaviour/test_update_reads_the_config_directory_in_use.py:139-147`)
searches for the `/.claude` path segment outside the one spelling, and
keeps `.claude-plugin` out with its lookahead (read). This round ran round
1's evidence again: the `rsync` source and step 5's path, each rewritten to
`${HOME}/.claude/...`, went in the same `bin/seal mutate` batch as above
over both modules, and both read `red`, where round 1 read 2 `SURVIVED`
(executed). Step 5's path is held by this case alone, since no case runs
it, so its red is this case's. Unmutated, the case passes at f8ed5efc
(executed). `gaps.md` *Not done* reads `nothing`, and the core-based
paragraph is gone (read).

What matched: the orchestrator's fold (f8ed5efc) rewrites the statements
round 1's two closes named. *Data & interfaces* at `frame/design.md:65-70`
shows the block as the skill holds it, character for character (read in
the diff). *Scope* 6d at `:34` and S5 at `:54` state the segment search
(read). S5 still says the search, run against the skill as it stood, holds
four hits. With the segment pattern over the skill at 475d018c, a
`python3 -c` run found four hits, the four coordinates of G1, and none at
HEAD (executed). *Scope* 6e at `:35` states the new case as it stands
(read). The judgment row at `frame/plan.md:41` cites `skills/code-review/orchestration.md`
*Orchestrator: a phase is a fresh crafter, and a fix pass resumes the
implementer*. That section's paragraph *The fix pass then finds what the
fixes left standing* has the orchestrator fold, in a commit of its own, the
frame statements a fix pass names (read).

What matched: the crafter claimed 65 passed over the two modules, the
hygiene update cases and line-wrap. One `bin/test` command over the four
modules, with `-k` selecting those cases, ended 65 passed (executed). The
new case covers what no case of its group covers. The S3 case runs the
first fence of step 2b, the new case runs the second, and the hygiene
cases pin words. `bin/seal layout --pairs` over the two modules read 2
files and found 0 pairs, exit 0 (executed).

Two statements of the frame were left by the fold. Neither changes what the
release ships or what a party does, so neither is a finding.
`frame/plan.md:30`, the phase 1 row, says phase 1 delivers *Scope* 6, which
now holds 6e, and c2a1f208 built 6e. The S table at `frame/design.md:48-55`
has no row that cites *Scope* 6e.

## Not judged

| What | Location | Who answers |
|---|---|---|
| How `printf %q` quotes a Windows `installPath`, and whether the new case holds on the ubuntu and Windows legs (`frame/questions.md` Q2). This round ran it on macOS alone and, as the spawn prompt asked, did not probe it | `skills/update/SKILL.md:71`, `tests/behaviour/test_update_reads_the_config_directory_in_use.py:85-115`, `gaps.md:7` | the orchestrator, by the run of the `tests` workflow on the branch it is taking |
| Whether a session's Bash call inherits `CLAUDE_CONFIG_DIR` from the Claude Code process that started it | `gaps.md:8` | the orchestrator, by the measurement `gaps.md` names |
| Whether Q1's default, an issue for the class, stands | `frame/questions.md:15` | the owner |
| The full suite, the repository-wide lint and the format check at HEAD. The suite's `unverified` label in `gaps.md:9` is honest: nothing in the range claims it passed. Once finding 1 is answered, what comes due is the verifying round of that fix, then the orchestrator's broad run and the sealer's spawn | `gaps.md:9` | the orchestrator's broad run of the `Broad gate` row in `seal/config.md` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_update_reads_the_config_directory_in_use.py tests/behaviour/test_the_old_block_leaves_through_update.py -q -rs -p no:xdist` | 16 passed, none skipped, exit 0 |
| `bin/test tests/behaviour/test_release_hygiene.py -q -p no:xdist -k "test_update_reads_the_installed_copy_before_it_summarises or test_update_shows_what_changed_from_the_github_releases"` | exit 0 |
| `bin/test tests/behaviour/test_docs_line_wrap.py -q -p no:xdist` | exit 0 |
| one `bin/test` over the two modules, `test_docs_line_wrap.py` and `test_release_hygiene.py`, `-k` selecting the two modules' cases, line-wrap and the two hygiene update cases | 65 passed |
| `bin/seal layout --pairs` over the two modules | 2 files read, 0 pairs, exit 0 |
| `bin/seal mutate skills/update/SKILL.md` with five `--replace` pairs (the printed `rsync` source to `${HOME}/.claude/...`, step 5's path to `${HOME}/.claude/plugins/cache/`, the repair block's record read to `${HOME}/.claude/...`, `%q` to `%s` on the `mv` and `rsync` lines, the `mkdir` argument to `"$p"`) over both modules, run twice: once for the exit code, once for the lines | baseline passed; 5 mutants, 5 red, 0 SURVIVED, exit 0 |
| `bin/seal mutate skills/update/SKILL.md`, the repair block's read ended with ` &&`, over the repair case, the search case and `test_update_reads_the_installed_copy_before_it_summarises` | SURVIVED, exit 1: the guard finding 1 proposes keeps the three cases green. A first run, its output filtered by a `grep` that matched none of its lines, exited 1 with nothing shown, and was run again unfiltered |
| `tests/behaviour/test_tmp_round2_repair.py`, two cases, run once: the repair block under `bash -c` and `zsh -c` with spaced paths, and under `bash -c` with no install record | the two shells printed the same three commands; with no record, exit 0 and a repair targeting `/` (finding 1). The file was deleted after the run |
| `bash -c` and `zsh -c` over a two-line `p=$(...) &&` then `printf %q` script, once with a read that fails and once with a path holding a space | each shell: exit 1 and nothing printed; exit 0 and `/a\ b/` |
| `python3 -c` with the segment pattern over `git show 475d018c:skills/update/SKILL.md` and over HEAD's skill, the spelling removed | four hits at 475d018c, none at HEAD |
| `git grep -n -F` on `stale.bak`, `"$p/"`, `repair below`, `print the repair`, the `mv` above, outside the round records | the skill, the new case and `frame/design.md:69` |

`git status --porcelain` printed nothing after each `bin/seal mutate` run
and after the probe file was deleted (executed).
