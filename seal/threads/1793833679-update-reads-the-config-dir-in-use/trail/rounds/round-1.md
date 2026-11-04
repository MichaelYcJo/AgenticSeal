# Review round 1: 1793833679-update-reads-the-config-dir-in-use

```seal
target: e2bb58bc against release/v0.32.2
```

This round read the branch at e2bb58bc against `release/v0.32.2` at
2ecb8d4b, in the repository's checkout of the branch, as the spawn prompt
named it. No earlier round exists, so no fact was carried and every fact
below was established here. `seal/parity.md` is not declared, so no
`original:` line is owed. `seal/config.md` has no `Record language` row, so
the record is in English.

The range holds seven commits: routing (5ce47e0d), the frame (ee1b1869,
475d018c), the build (f1c2782a), the fragment, version move, `gaps.md` and
phase record (3e87ebf6), the Status cell (56432b1f) and the orchestrator's
fold (e2bb58bc). `git diff --stat` lists `skills/update/SKILL.md`, the two
test modules, `.claude-plugin/plugin.json` and the work item's records, and
nothing else (executed).

## Findings

### 1. The repair printed for the user uses `$p`, which the user's terminal does not hold, so the `rsync` it prints copies into `/`

```seal
severity: should
location: `skills/update/SKILL.md:60`, `skills/update/SKILL.md:62-70`, `tests/behaviour/test_update_reads_the_config_directory_in_use.py`
evidence: read `skills/update/SKILL.md:16-21`, `skills/update/SKILL.md:60`, `skills/update/SKILL.md:66-70`, `seal/threads/1793833679-update-reads-the-config-dir-in-use/frame/plan.md:11`, `seal/threads/1793833679-update-reads-the-config-dir-in-use/frame/plan.md:22`; executed `bash -c 'unset p; printf "[%s] [%s]\n" "$p/" "$p/.in_use"'`, which printed `[/] [/.in_use]`
```

Why it matters: the mismatch row of step 2b (`skills/update/SKILL.md:60`)
tells the session to "print the repair below for the user to type". The
procedure sentence this build added (`:16-21`) says why each command spells
the directory on its own: "no two of them share a shell: a session runs
each block as a call of its own, and the user types the repair in a
terminal of their own". The frame states the same constraint
(`frame/plan.md:11`: "no variable carries it from one step to the next").
Its fourth alternative (`frame/plan.md:22`) rejects a `$config` set in
step 1 because "the repair the user types has no `$config` at all".

The repair this build edited (`:66-70`) still reads `$p`, which step 2b's
first command set in the session's own shell. By the frame's own argument,
the user's terminal has no `$p` either. Typed as printed, `mv "$p"
"$p.stale.bak"` fails, and `rsync -a --exclude '.git' <clone>/ "$p/"`
expands its target to `/` (executed above). A user who types it as root,
as in a container, copies the plugin's tree into the filesystem root. The
`$p` dependency was there before this branch, but the line the build
rewrote is the one that carries it, and the build's own sentence now
states the fact that breaks it.

The same cause reaches the config directory. The user's terminal holds
`CLAUDE_CONFIG_DIR` only where the user exported it there. A session
started as `CLAUDE_CONFIG_DIR=<dir> claude` passes the variable to the
session's shell and not to a terminal opened later. There the printed
`${CLAUDE_CONFIG_DIR:-$HOME/.claude}` falls back to `~/.claude`, the
directory this work item exists to stop reading. `gaps.md:8` asks only
whether the session's Bash call inherits the variable. It does not ask
about the user's terminal.

The fix lets the session's shell, which holds both values, write the
repair out with literal paths. The block only prints, so the step still
runs nothing that deletes. The session runs it and gives its output to the
user. This text replaces `:62-70`. Its precondition: `printf %q` is bash's
form, and the quoting it prints (backslash before a space) is read the
same by bash and zsh.

````markdown
The repair replaces the stale directory from the marketplace clone, and it
is the user's to type rather than this procedure's to run, because it
deletes a directory a session may be holding. The user's terminal holds
neither `$p` nor, unless it is exported there, `CLAUDE_CONFIG_DIR`, so run
the block below, which only prints the repair with this session's paths
written out, and give its output to the user to type:

```bash
p=$(python3 -c "import json,sys;d=json.load(open(sys.argv[1],encoding='utf-8'));print(d['plugins']['agentic@agenticseal'][0]['installPath'])" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/installed_plugins.json")
printf 'mv %q %q\nrsync -a --exclude .git %q %q\nmkdir -p %q\n' "$p" "$p.stale.bak" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/marketplaces/agenticseal/" "$p/" "$p/.in_use"
```
````

The snippet does not cover every statement of this fact. The fix pass
also owes these:

- The mismatch row at `:60`: "print the repair below for the user to type"
  becomes "run the block below and give the repair it prints to the user to
  type".
- The cautions paragraph at `:72-77`: "the `mv` above" becomes "the `mv`
  the repair prints".
- The fragment's sentence "Its repair copied from the marketplace clone
  under `~/.claude`" (`changelog.md:3`), which should also say that the
  repair is now printed with this session's paths written out.
- A case in `tests/behaviour/test_update_reads_the_config_directory_in_use.py`.
  It runs the printing block under `bash -c`, through `run_bash`, and
  asserts that the printed `rsync` line names the config directory's clone
  and the `installPath` that directory's record names. Its red must never
  come from running the current repair, whose target is `/` when `p` is
  empty. Show it red with a mutant of the new block instead, such as the
  printed source rewritten to `${HOME}/.claude/...`.

The pins of `tests/behaviour/test_release_hygiene.py` that
`frame/design.md` G8 lists for step 2b (`installed_plugins.json`,
`installPath`, `rsync`, and no machine's home path) all hold in this
snippet (read). The snippet names
no `~/.claude` outside the spelling, so finding 2's search holds it too.

### 2. The search that alone holds the repair's `rsync` source and step 5's path lets `${HOME}/.claude` through, and `gaps.md` cites the core for not widening it

```seal
severity: should
location: `tests/behaviour/test_update_reads_the_config_directory_in_use.py:105-113`, `seal/threads/1793833679-update-reads-the-config-dir-in-use/gaps.md:13`
evidence: executed `bin/seal mutate skills/update/SKILL.md --replace '"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/marketplaces/agenticseal/"' '"${HOME}/.claude/plugins/marketplaces/agenticseal/"' --replace '`${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/cache/' '`${HOME}/.claude/plugins/cache/' --tests "bin/test tests/behaviour/test_update_reads_the_config_directory_in_use.py tests/behaviour/test_the_old_block_leaves_through_update.py -q -p no:xdist"`, 2 mutants, 2 SURVIVED, exit 1; read `skills/core/SKILL.md` *The rule a mechanism is kept against*
```

Why it matters: the build changed the repair's `rsync` source
(`skills/update/SKILL.md:68`) and step 5's cache path (`:231`). No case
runs either of them. `test_the_skill_names_no_fixed_claude_directory`
(`:105-113`) is the one case that holds them. Its docstring says "Every
path to Claude Code's own files is spelled as the config directory in
use", but it searches for two strings, `~/.claude` and `$HOME/.claude`.
Both lines rewritten to `${HOME}/.claude/...` survived every case of the
two modules (executed above). An edit in that spelling puts back the
defect #1184 fixes, in the two places that have no other case. Under
`skills/code-review/SKILL.md` *The record*, this is the *Regression test*
`should`: the grounds name behaviour the diff changed that no case holds
against that edit.

The crafter claims (`gaps.md:13`) that widening the search was within
reach, but that "the core says no script carries a list of the spellings a
label is written in". On that ground the reading stays with review. The
claim does not hold.

- The core's sentence is about a script that decides whether a line of a
  form meant a label. A path into a directory is not a label.
- The case already carries a list of two spellings, so by the crafter's
  reading it breaks the rule now.
- One construct holds the fact with no list: no path segment `/.claude`
  stands outside the one spelling, however the part before the slash is
  spelt. Checked against the skill at e2bb58bc, the pattern below finds
  nothing. Against the surviving `rsync` mutant, it finds the mutated
  source. Both were read from one `python3 -c` run of the pattern over the
  file's text (executed). The lookahead keeps `.claude-plugin` out (`:24`,
  `:54`).

The frame's *Scope* 6d and S5 name the two spellings. The pattern finds
both, so it still meets them. The orchestrator may fold S5's "When it is
searched for `~/.claude` and `$HOME/.claude`" to the construct. The phase
record's mutation note is a past-state record of f1c2782a and stays. The
fix pass shows the new assertion red with the surviving `${HOME}` mutant
(contract rule 15), and removes `gaps.md`'s *Not done* paragraph, which no
longer holds.

```python
def test_the_skill_names_no_fixed_claude_directory():
    """S5. Every path into Claude Code's directory is spelled as the config
    directory in use, so the repair's `rsync` and step 5's sentinel method,
    which no case runs, read the directory the session loaded. The search is
    for the path segment `/.claude`, however the part before it is spelled;
    `.claude-plugin` is another name and does not count."""
    rest = read(UPDATE).replace(SPELLING, "")
    fixed = re.findall(r"\S*/\.claude(?![-\w])\S*", rest)
    assert not fixed, f"skills/update/SKILL.md names {fixed!r} outside {SPELLING!r}"
```

## Confirmations

What matched: step 2b's first command, the repair's `rsync` source, step
3's `repo=` line and step 5's path stand at `skills/update/SKILL.md:53`,
`:68`, `:88` and `:231`. Each is in the spelling `frame/design.md` *Data &
interfaces* gives, and step 4's argument at `:197` is unchanged (read). The
program at `:53` imports `sys` in place of `os` and opens `sys.argv[1]`, as
*Scope* 1 and *Removes* state (read). The procedure sentence of *Scope* 5
stands at `:16-21`, before step 1, and names the directory in the one
spelling (read).

What matched: the crafter claimed red before the code, 3 failed and 12
passed. This round rewrote step 2b's first command and step 3's line back
to their lines at 2ecb8d4b with `bin/seal mutate`, one at a time. Each
went red on the case it was written for. Step 2b's case failed `'9.9.0' ==
'9.9.1'`, and step 3's failed with `owner-home/repo-home` (executed).

What matched: the crafter claimed that `bin/seal mutate` showed S1 red.
This round rewrote `:197`'s argument to `"$HOME/.claude/CLAUDE.md"` over
`-k config_directory_in_use`. It read `red`, and the failing case was
`test_step_4_takes_the_block_out_of_the_config_directory_in_use`
(executed). The other mutation claims of `trail/phases/phase-1.md:20-26`
were read and not re-run.

What matched: the crafter claimed that the `${HOME}` spelling passes the
search case. That is finding 2's survivor, so the claim holds and its
grounds do not (executed).

What matched: the two modules ran 15 passed, exit 0, with `-rs`, so no
case skipped on this machine. The two update cases of
`tests/behaviour/test_release_hygiene.py` passed with no needle changed
(S6), 2 passed, exit 0. `tests/behaviour/test_docs_line_wrap.py` exited 0
(executed). `uvx ruff check` and `uvx ruff format --check` over the two
test modules alone exited 0. That is the narrow form, not the broad gate
(executed).

What matched: the crafter claimed that the new cases repeat no case of
their groups. `bin/seal layout --pairs` over the two modules read 2 files
and found 0 pairs, exit 0 (executed). The new step 4 case runs the whole
shell line, which none of `take_out`'s cases does. The step 2b and step 3
cases run commands that `test_release_hygiene.py`'s cases only pin by
their words (read).

What matched: `.claude-plugin/plugin.json` reads `0.32.2`.
`git grep -n 0.32.1` outside `seal/threads/` finds no other copy of the
version, and `.claude-plugin/marketplace.json` carries none (executed).
The fragment `changelog.md` holds one entry under `### Fixed`, in the
shape of the other fragments under `seal/threads/` (read).

What matched: the orchestrator claimed it filed #1367 as Q1's home.
`gh issue view 1367` shows the issue open. It names the six coordinates of
`frame/design.md` *Scope*'s first *Out* item (executed). Q1 stays `open`
for a person, as `frame/plan.md:41` says.

What matched: the orchestrator's dating sentence at `frame/design.md:5`
and `frame/plan.md:5` names 475d018c. `git diff --quiet release/v0.32.2
475d018c -- skills/update/SKILL.md tests` exited 0. At 475d018c the skill's
lines `:46`, `:61`, `:81`, `:190` and `:223` read as G1 says (executed).
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* asks the orchestrator to rewrite every statement HEAD contradicts.
A dated statement claims a past tree, as a Status cell's commit does
(`skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes*, the past-state paragraph). So HEAD no longer contradicts it.
The judgment row at `frame/plan.md:40` gives that grounds and the
documents it was judged against (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the new cases hold on the ubuntu and Windows legs (`frame/questions.md` Q2). This round ran them on macOS alone | `tests/behaviour/test_update_reads_the_config_directory_in_use.py`, `tests/behaviour/test_the_old_block_leaves_through_update.py:149` | the orchestrator, by a run of the `tests` workflow on the branch |
| Whether a session's Bash call inherits `CLAUDE_CONFIG_DIR` from the Claude Code process that started it | `gaps.md:8` | the orchestrator, by the measurement `gaps.md` names |
| Whether Q1's default, an issue for the class, stands | `frame/questions.md:15` | the owner |
| The full suite, the repository-wide lint and the format check at HEAD. The suite's `unverified` label in `gaps.md:9` is honest: nothing in the range claims it passed | `gaps.md:9` | the orchestrator's broad run of the `Broad gate` row in `seal/config.md` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_update_reads_the_config_directory_in_use.py tests/behaviour/test_the_old_block_leaves_through_update.py -q -rs -p no:xdist` | 15 passed, exit 0 |
| `bin/test tests/behaviour/test_release_hygiene.py -q -p no:xdist -k "test_update_reads_the_installed_copy_before_it_summarises or test_update_shows_what_changed_from_the_github_releases"` | 2 passed, exit 0 |
| `bin/test tests/behaviour/test_docs_line_wrap.py -q -p no:xdist` | exit 0 |
| `bin/seal layout --pairs` over the two modules | 2 files read, 0 pairs, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the two modules | exit 0 each |
| `bin/seal mutate skills/update/SKILL.md`, `:197`'s argument to `"$HOME/.claude/CLAUDE.md"`, over `-k config_directory_in_use` | red, exit 0; `test_step_4_takes_the_block_out_of_the_config_directory_in_use` failed |
| `bin/seal mutate skills/update/SKILL.md`, step 2b's first command back to its line at 2ecb8d4b, over `-k step_2b` | red, exit 0; `'9.9.0' == '9.9.1'` |
| `bin/seal mutate skills/update/SKILL.md`, step 3's `git -C` back to `~/.claude/plugins/marketplaces/agenticseal`, over `-k step_3` | red, exit 0; `owner-home/repo-home` |
| `bin/seal mutate skills/update/SKILL.md`, the `rsync` source and step 5's path each to `${HOME}/.claude/...`, over both modules | 2 mutants, 2 SURVIVED, exit 1 (finding 2) |
| `python3 -c` over the skill's text with the spelling removed, pattern `\S*/\.claude(?![-\w])\S*` | no hit at e2bb58bc; one hit, the mutated source, on the `rsync` mutant |
| `bash -c 'unset p; printf "[%s] [%s]\n" "$p/" "$p/.in_use"'` | `[/] [/.in_use]`, exit 0 (finding 1) |
| `gh issue view 1367 --json title,state,body` | open, names the six coordinates |

`git status --porcelain` printed nothing after each `bin/seal mutate` run,
so each restored the skill (executed).
