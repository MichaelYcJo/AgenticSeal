# Review round 1: 1794142458-config-dir-readers

```seal
target: 8b101e85e against release/v0.35.1
```

The base is `release/v0.35.1` at `9e758b0b0` (executed: `git log --oneline 9e758b0b0..8b101e85e` lists the 15 commits of the branch). This is a finding round over the whole branch. No earlier round exists, so this round carried no fact and re-established every one it uses. `seal/parity.md` is absent, so no parity comparison applies. The record language is English, since `seal/config.md` has no `Record language` row.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md` whole at `8b101e85e`, and issue #1367 with its comment (executed: `gh issue view 1367 --json title,body,comments`).

## Findings

### 1. The frame says S8's run passes without the `conftest.py` removal, and at the target it fails

```seal
severity: should
location: `seal/threads/1794142458-config-dir-readers/frame/design.md:31`
evidence: read `seal/threads/1794142458-config-dir-readers/frame/design.md:31`, `seal/threads/1794142458-config-dir-readers/frame/design.md:54`, `tests/skills/test_payload_meter.py:256-261`, `tests/skills/test_payload_meter.py:1617-1639`, `skills/verify/scripts/payload_meter.py:1213`, `seal/threads/1794142458-config-dir-readers/trail/phases/phase-2.md:108-110`, `seal/threads/1794142458-config-dir-readers/trail/phases/phase-2.md:126-127`
```

Why it matters: *Scope* item 4 ends "pins the removal, since S8's run alone passes with it gone". The orchestrator's fold `f6bbfb0f9` wrote that sentence after phase 1, when S8's run held only `tests/skills/test_session_cost.py`. S8 (`frame/design.md:54`) now runs "the two modules of S1 and S3". Without the removal, the `[unset]` case of `test_an_unset_or_empty_variable_reads_the_home_directory` (`tests/skills/test_payload_meter.py:1617-1639`) calls `run` with `extra=None`. `run` (`:256-261`) copies `os.environ`, so the child inherits the outer `CLAUDE_CONFIG_DIR`. `main` (`payload_meter.py:1213`) passes it on, and the case's label assertion fails. Phase 2 records the same result: the removal as `pass`, under an outer variable, made that module red (`phase-2.md:108-110`), and "this run can fail on the `conftest.py` pop" (`:126-127`). The fold `822f8dd82` after phase 2 left the sentence standing. A sealer or a settle reading item 4 takes the conftest case's grounds to be a run that cannot fail, and that is false at the target.

The fix touches only the last sentence of item 4. S8's row (`:54`) already says the conftest case "fails where the removal is gone" and needs no change. The first row of `frame/plan.md` *Judgments of the run* (`:44`) gives its grounds from the phase-1 hand-back, which a dated row states, so the fix owes it nothing.

```markdown
4. **The suite runs with the variable unset.** `tests/conftest.py` removes `CLAUDE_CONFIG_DIR` from `os.environ` at import, beside the `GH_CONFIG_DIR` block, with a comment saying why (G9). A case that needs the variable sets it. `tests/test_conftest.py#Test_module::test_the_conftest_takes_the_claude_config_directory_away` pins the removal, since S8's run of `tests/skills/test_session_cost.py` passes with it gone: every `Test_newest` case sets or deletes the variable itself.
```

### 2. The release note names one row a `--baseline` stops pairing, and the rows of the files that row imports stop pairing too

```seal
severity: should
location: `seal/threads/1794142458-config-dir-readers/changelog.md:3`, `seal/threads/1794142458-config-dir-readers/frame/plan.md:38`, `seal/threads/1794142458-config-dir-readers/pr.md:3`
evidence: read `skills/verify/scripts/payload_meter.py:503-527`, `skills/verify/scripts/payload_meter.py:936-953`, `tests/skills/test_payload_meter.py:1660-1668`
```

Why it matters: the claim is that under a set variable "a `--baseline` taken before this release does not pair the user's `CLAUDE.md` row, because its label changed" (`changelog.md:3`, quoted into `pr.md:3`). `plan.md:38` says the same thing: "does not pair that row". `delta_against` pairs an agent's rows by `row["path"]` (`payload_meter.py:946-953`). `pair_rows` builds each import row's label as `ARROW.join((display, *chain))` (`:519-526`), where `display` is the user file's label. So every row imported from the user's `CLAUDE.md` changes its label too, from `~/.claude/CLAUDE.md → …` to `$CLAUDE_CONFIG_DIR/CLAUDE.md → …`. S6's case pins that label (`tests/skills/test_payload_meter.py:1660-1668`). A person who reads the note and then sees several `added` and `removed` import rows in the delta is told that one row moved, and has to work out that the rest moved for the same reason. The fix covers the note, its quote in `pr.md` and the plan's sentence. `pr.md:3` has to match the new `changelog.md` text word for word.

```markdown
changelog.md:3, the sentence:
Where it is set, a `--baseline` taken before this release does not pair the user's `CLAUDE.md` row or the row of each file it imports, because their labels changed.

pr.md:3:
- "Where it is set, a `--baseline` taken before this release does not pair the user's `CLAUDE.md` row or the row of each file it imports, because their labels changed." (`changelog.md` *Fixed*, the first item)

frame/plan.md:38, the two sentences:
On a machine that sets the variable, a `seal payload` row moves from `~/.claude/CLAUDE.md` to `$CLAUDE_CONFIG_DIR/CLAUDE.md`, and the row of each file it imports moves with it. A `--baseline` taken there before the fix pairs none of those rows (G7), and those readings measured the wrong file anyway.
```

### 3. Two executed absence searches use `\b` under `git grep -E`, which matches nothing on this machine, so they could not fail

```seal
severity: should
location: `seal/threads/1794142458-config-dir-readers/frame/design.md:11`, `seal/threads/1794142458-config-dir-readers/trail/phases/phase-1.md:13-14`
evidence: executed `git grep -n -E '\bPROJECTS\b' 9e758b0b0 -- '*.py'` (lists nothing), `git grep -n -P '\bPROJECTS\b' 9e758b0b0 -- '*.py'` (lists five lines: `session_cost.py:83`, `:2887` and three in `tests/skills/test_session_cost.py`), `git grep -n -E '\bPROJECTS\b|session_cost\.HOME|module\.HOME' 9e758b0b0 -- . ':!seal/threads'` (exit 1), `git grep -n -P '\bPROJECTS\b|session_cost\.HOME|module\.HOME' 8b101e85e -- . ':!seal/threads'` (exit 1)
```

Why it matters: G1 claims that "`git grep -n -E '\bPROJECTS\b' -- '*.py'` outside the script lists only `tests/skills/test_session_cost.py`". On this machine (git 2.54.0, Apple Git-157) that command lists nothing, even at the base where `PROJECTS` stands on five lines. So it could not have printed what G1 says it printed. Phase 1 claims that `HOME` and `PROJECTS` "had no reader outside the script and `Test_newest`", and rests that on `git grep -n -E '\bPROJECTS\b|session_cost\.HOME|module\.HOME' -- . ':!seal/threads'` listing nothing after the build. That search also exits 1 at the base, where the constant still stood, so it cannot fail. Phase 2 found the cause (`phase-2.md:23-25`: "under `git grep -E` on this machine its `\b` matched nothing"), but left the two earlier claims standing. Both facts hold: with `-P`, the search lists nothing at `8b101e85e`, and `git grep -n -w PROJECTS 8b101e85e -- . ':!seal/threads'` also lists nothing. The evidence does not hold. A sealer re-running G1's command gets an empty listing that contradicts its sentence, and re-running phase 1's command gets a pass that proves nothing. The fix rewrites each command into a form that can fail, re-runs it, and records what the re-run prints. It must not put into a record a command that nobody ran.

```markdown
frame/design.md:11, the parenthesis in G1's second cell:
(executed: `grep -n PROJECTS` lists `:83` and `:2887` alone, and `git grep -n -w PROJECTS -- '*.py'` outside the script lists only `tests/skills/test_session_cost.py`)

trail/phases/phase-1.md:12-15:
`README.ko.md:316` (read). `HOME` and `PROJECTS` had no reader outside the
script and `Test_newest` (executed: `git grep -n -P
'\bPROJECTS\b|session_cost\.HOME|module\.HOME' c4deded61 -- . ':!seal/threads'`
lists nothing, and the same search at `9e758b0b0` lists the script and
`Test_newest`, so it can fail).
```

## Confirmations

What matched: *Scope* item 1. `projects_dir()` (`skills/verify/scripts/session_cost.py:84-92`) returns `os.path.join(os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude"), "projects")` at each call, and `newest` (`:2898`) calls it. `HOME` and `PROJECTS` are gone, and nothing names them (executed: `git grep -n -w PROJECTS 8b101e85e -- . ':!seal/threads'` lists nothing). The docstring (`:41-42`) and the two comments (`:2890`, `:3111`) use the new spelling. Phase 1 claimed that no `__doc__` of the script is read, and `grep -n __doc__ skills/verify/scripts/session_cost.py` lists nothing (executed).

What matched: *Scope* item 2 and *Data & interfaces*. `user_dir` (`skills/verify/scripts/payload_meter.py:453-464`) returns `(home/.claude, "~/.claude")` for `None` or empty and `(config, "$CLAUDE_CONFIG_DIR")` otherwise. `measure` takes `config=None` (`:795`) and threads the pair into `session_composition`, `composition` and `pair_rows`. `main` is the one reader of the variable (`:1213`). `imports_of` keeps `home` (`:518`). Phase 2 claimed that `.github/scripts/release_report.py:127` is the meter's one outside caller, and that it calls `composition` with five arguments. A search over the whole tree finds no other caller of `composition`, `pair_rows`, `session_composition`, `user_dir`, `measure` or `newest` outside the two scripts and their tests (executed: `git grep -n -P '\b(composition|pair_rows|session_composition|user_dir|imports_of|measure|projects_dir|newest)\(' 8b101e85e -- . ':!seal/threads'`). So making `session_composition`'s `sections` required breaks no caller. The docstring edits at `:7-10` and `:70-74` stand outside the first paragraph that `main` hands argparse (read: `:1-3`, `:1195`).

What matched: *Scope* item 3 and S7. G2's second search at `8b101e85e` lists `settle.py:908`, `pact_check.py:613`, `payload_meter.py:441`, `payload_meter.py:1207` and `session_cost.py:90`. None of these is a coordinate of *Scope* items 1 to 3 (executed). A wider search, `git grep -n -E '~/\.claude|HOME/\.claude'` outside history, tests and evals, lists only the plugin's own `~/.claude/agentic/` state and code that builds the fallback (executed). The `README.md:291` and `README.ko.md:290` lines it lists name `~/.claude/agentic/parity-paths.md`, which *Scope* Out excludes for that reason. The README's history line is now right: v0.34.1's launcher wrote into `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json` (read: `git show v0.34.1:skills/implement/bootstrap.md`, `:167`, `:175`). The first G2 search at `8b101e85e` lists no root outside the two scripts, `pact_check.py` and `skills/update/SKILL.md` (executed). `evals/scripts/noninferiority.py:208` matches `.claude` but only drops PATH entries, and reads no file there (read).

What matched: *Scope* items 4 and 5, and S1 to S6, S8. Each case stands where its row says, with the assertions the row describes (read: `tests/skills/test_session_cost.py:5405-5432`, `tests/skills/test_payload_meter.py:1561-1668`, `tests/test_conftest.py:532-541`, `tests/conftest.py:377-386`). The narrow run of the touched modules passed (executed: `bin/test tests/skills/test_session_cost.py tests/skills/test_payload_meter.py tests/test_conftest.py tests/github/test_release_report.py tests/behaviour/test_docs_line_wrap.py -q`, 441 passed). This is a narrow run and not the suite. S8 passed under an outer `CLAUDE_CONFIG_DIR` naming a scratch directory that holds a `CLAUDE.md` and an `alpha` shadow (executed, 368 passed). The round did not re-run the seen-red claims of either phase. Finding 1 rests on reading why the `[unset]` case fails without the removal.

What matched: the new tests against their groups. `bin/seal layout --pairs tests/skills/test_payload_meter.py tests/skills/test_session_cost.py tests/test_conftest.py` names 24 pairs: 4 in `Test_imports_of`, 4 in `Test_main` and 16 in `Test_post` (executed). None of them is a new or changed case, which matches phase 1's count of 20 and phase 2's count of 4. Within their groups, S2 `[unset]` is the one case of `newest`'s fallback, since the two older `Test_newest` cases now set the variable through `two_roots`. S5 `[unset]` is the one case that reaches `main`'s read, and phase 2's mutant that gave `main` a default named only that case. No new case covers only what its group already covers.

What matched: `.claude-plugin/plugin.json` reads `0.35.1` (`:4`), and the fragment that adds it comes in the same commit, `dfb42e4e2` (executed: `git show --stat dfb42e4e2`). No `0.35.0` stands in the tree outside history (executed: `git grep -n -F '0.35.0' 8b101e85e -- . ':!CHANGELOG.md' ':!seal/threads'`). This is as `docs/releasing/branch-and-release.md:30-42` asks. The fragment ends with `### Process changes` in the shape of `templates/records/process.md`, because the diff changes `skills/verify/orchestration.md`, as `docs/layout/the-record-layout.md:51-60` asks.

What matched: every quote in `pr.md`, except the one finding 2 changes, stands word for word at the coordinate it names (read: `changelog.md:3-4`, `frame/plan.md:46`, `gaps.md:7`). Each `gaps.md` row still states the present, and no row has left the memo.

The docstring of `tests/test_conftest.py#Test_module::test_the_conftest_takes_the_claude_config_directory_away` says a case that needs the variable "sets it with `monkeypatch.setenv`". The meter's cases set it through `run`'s `extra` (`tests/skills/test_payload_meter.py:256`). Only the next editor of the case reads this, so the round opens no finding for it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether Claude Code 2.1.319 under a set `CLAUDE_CONFIG_DIR` loads the user's `CLAUDE.md` and skills and writes transcripts in that directory. `changelog.md:3` states it as fact, and `gaps.md` rows 1 and 3 and `frame/questions.md` Q1 hold it unmeasured | `seal/threads/1794142458-config-dir-readers/changelog.md:3`, `seal/threads/1794142458-config-dir-readers/frame/questions.md:15` | the repository owner, by Q1's measurement in a signed-in session |
| Whether the new cases pass on Windows, where `expanduser("~")` reads `USERPROFILE` | `tests/skills/test_session_cost.py:5372-5384`, `tests/skills/test_payload_meter.py:256-261` | CI's Windows leg, at the pull request |
| The broad gate (`seal/config.md` `Broad gate` row). The suite is `unverified`, as the crafter labelled it, and that label is honest: neither phase record claims a full run | the whole tree at `8b101e85e` | the orchestrator's broad run, then the sealer's spawn |

## Probes

| Command | Result |
|---|---|
| `git grep -n -E '\bPROJECTS\b' 9e758b0b0 -- '*.py'` and the same with `-P` | `-E` printed nothing, and `-P` printed five lines, so `\b` matches nothing under `-E` on this machine |
| `git grep -n -E '\bPROJECTS\b\|session_cost\.HOME\|module\.HOME' 9e758b0b0 -- . ':!seal/threads'` | exit 1 at the base, where `PROJECTS` stood |
| `git grep -n -P '\bPROJECTS\b\|session_cost\.HOME\|module\.HOME'` at `c4deded61` and at `8b101e85e` | exit 1 at each |
| `bin/test tests/skills/test_session_cost.py tests/skills/test_payload_meter.py tests/test_conftest.py tests/github/test_release_report.py tests/behaviour/test_docs_line_wrap.py -q` | 441 passed, a narrow run and not the seal |
| `env CLAUDE_CONFIG_DIR=<scratchpad>/1794142458-config-dir-readers/round-1/outer-config bin/test tests/skills/test_session_cost.py tests/skills/test_payload_meter.py tests/test_conftest.py -q`, with a `CLAUDE.md` and `skills/alpha/SKILL.md` written in that directory | 368 passed. The scratch directory was removed afterwards |
| `bin/seal layout --pairs tests/skills/test_payload_meter.py tests/skills/test_session_cost.py tests/test_conftest.py` | 24 pairs, none of them a new or changed case |
