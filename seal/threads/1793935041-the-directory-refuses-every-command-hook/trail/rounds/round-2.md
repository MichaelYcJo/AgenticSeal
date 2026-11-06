# Review round 2: 1793935041-the-directory-refuses-every-command-hook

```seal
target: 11d6c3b9, fixes fa496f3f..11d6c3b9
```

This is the verifying round for round 1. It read `git diff fa496f3f..11d6c3b9`
in a `git clone --no-local` at `11d6c3b9`. The range holds four commits:
`c6ec999a` refreshes `.test_durations`, `7b26c345` and `11d6c3b9` carry round
1's record and its close blocks, and `1f412308` is the fix pass. The round
answers each of round 1's six closes and reviews `c6ec999a` as new work,
since no round had read it.

Carried from round 1, not re-established: the frame's census and its kept
paths, the stamp probe's install, draw and removal measurements, and the
pair `seal layout --pairs` printed. The fix diff touches none of them.
Re-run, as round 1's `evidence: executed` lines name them: the `sh -c`
fallback probe of finding 6, the grep of the installed 0.32.6 update skill
for the stamp (finding 4), the two `git grep` commands of finding 2, and
the "four rows" search of finding 3 (`## Probes`). Each answered as it did
in round 1, apart from the change the fix made.

## Findings

### 1. The closing memo says `.test_durations` still holds 850 stale lines, and `c6ec999a` removed them

```seal
severity: should
location: `seal/threads/1793935041-the-directory-refuses-every-command-hook/gaps.md:40-44`
evidence: executed `git show fa496f3f:.test_durations | grep -c 'tests/hooks/'`, which printed 848, and the same at `11d6c3b9`, which printed 0; read `skills/code-review/scripts/pr_body.py:13-14`, `skills/code-review/scripts/pr_body.py:626-627`
```

Why it matters: `gaps.md` *Not done* says "`.test_durations` still holds
850 lines naming `tests/hooks/` or a renamed case. Phase 7 left them to
CI's rebuild". `c6ec999a` replaced the file with the `test-durations`
artifact of run 42179293981, and at HEAD no line of it names `tests/hooks/`.
The paragraph records a decision not to act, and the act has now been taken.
`seal pr-body` copies `gaps.md`'s `## Not done` into the pull request body
(`pr_body.py:626-627`), so the body would tell the reviewer about a stale
file that is no longer stale. `docs/forms/the-round-record.md` counts a
wrong line that `seal pr-body` copies as a `should`.

The defect stands in a unit no fix commit changed. `c6ec999a` made the
sentence false, and no finding named that commit. So the finding carries
neither a `regression:` nor a `reopens:` line.

The paragraph goes whole. `trail/phases/phase-7.md:37` keeps the count for
the commit it names, and `frame/plan.md:55` keeps the grep's kept paths, so
nothing else needs to change.

```diff
-`.test_durations` still holds 850 lines naming `tests/hooks/` or a renamed
-case. Phase 7 left them to CI's rebuild, as `frame/plan.md`'s judgment row
-of phase 1 does for every stale id, so the plan's grep for phase 7 lists
-that file. `trail/phases/phase-7.md` lists the other paths the grep keeps
-on purpose.
-
```

```seal
verdict: fixed 05f8cd36
answer: The paragraph is removed whole, as the diff gives it. `git grep -c 'tests/hooks' -- .test_durations` at fcdb46f3 printed nothing and exited 1, which agrees with the finding. `trail/phases/phase-7.md` states the commit it names and stays.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/implement/bootstrap.md:43-44` now says that where
`<repo>/seal/` is the project's own, step 1's call "carries the `Broad gate`
question, and the stamp's where nothing records an answer to it". Step 1 at
lines 46-48 reads "**two questions**, or three: the mode, the `Broad gate`
row, and the stamp". Both agree with the paragraph at lines 160-171, which
puts the stamp question only where `seal stamp --hook` prints `neither`. The
words "two questions" that `tests/behaviour/test_first_setup_asks_once.py:148`
pins stay. A `git grep` for "two questions" and "question alone" outside
`seal/threads/` finds no other statement of the batch's size. That module
passed in the narrow run (read and executed).

```seal
confirms: round-1#2
```
What holds: both editions of `docs/layout/one-root-by-lifetime.md` *The
opt-in signal is the root itself* now name the readers. These are the `seal`
commands, the pull request's check and the stamp's `--stop`. The section
also says a command that cannot tell reads the repository as not opted in,
and that `.git/agentic-scratch` makes it read as not opted in. `lib/optin.py#home_at`
(lines 215-254) reads `<root>/seal/` and then the common directory's,
returns "" where the scratch file stands, and returns "" on every failure.
`seal_stamp.py:1505` reads it through `opted_in`. The shared-mode cell now
reads "in the workflow" and "워크플로를 따른다". `bootstrap.md:26-27` now says
the commands and the pull request's check read the root. Round 1's two
`git grep` commands were re-run at `11d6c3b9`. The hits left in `docs/layout/`
and `bootstrap.md` are the generic mechanism list at
`one-root-by-lifetime.md:130` and the stamp's own hook. The `gated` hits
elsewhere use "gated repository" or "gated command" for a repository the
workflow covers. The fix pass judged "gate" in `templates/setup/seal-README.md`
and `lib/optin.py`'s docstring to mean any command or check that reads the
root and refuses. That reading holds at `templates/setup/seal-README.md:56-72`.
Its hand-back calls its list a sample built from spellings, and says where
the unreached part stands. `tests/lib/test_optin.py` and
`tests/behaviour/test_docs_line_wrap.py` passed in the narrow run (read and
executed).

```seal
confirms: round-1#3
```
What holds: `README.md:171` and `README.ko.md:171` now say "four rows" and
"네 행", as `skills/core/SKILL.md:106` does. The two `LOCAL_LIMIT` strings
at `tests/behaviour/test_first_setup_asks_once.py:478-490` carry the same
words. The old README text does not contain the new strings, so the case
fails against it (read). `trail/phases/phase-6.md:66-68` now cites the core's
closing sentence instead of restating it. A `git grep` for "last four rows"
and "마지막 네 행" outside `seal/threads/` exits 1 (executed).

```seal
confirms: round-1#4
```
What holds: the fragment's *Updating* line now says three things. The
update that installs 0.33.0 runs the earlier release's update skill, which
does not ask about the stamp. The earlier stamp hooks stop at the restart.
A second `/agentic:update` reports the plugin current and asks. The grep of
the installed 0.32.6 update skill for "stamp" again printed nothing, exit 1
(executed). `skills/update/SKILL.md:39-42` takes step 4b where the update
reports the plugin current. Step 4b's table, lines 225-230, asks where
`--hook` prints `neither` (read). The command now carries the data
directory and `--settings` that `seal_stamp.py#main` requires (lines
1785-1811). `seal_stamp.py#install` (lines 1643-1664) removes the
`stamp-declined` marker, so the command works for a person who answered no.
`README.md:309-311` spells `seal stamp` the same way for a person (read).
Whether the data directory sits under `CLAUDE_CONFIG_DIR` where that is
set is under `## Not judged`.

```seal
confirms: round-1#5
```
What holds: `CONTRIBUTING.md:342` and `.github/PULL_REQUEST_TEMPLATE.md:30-31`
now say a gate decides whether a pull request or run goes ahead, as
`README.md` does. The fix pass also rewrote two more sentences of the same
section that stood on a hook stopping a session. The "wrong deny" sentence
at lines 352-354 is one. The other is line 387, where "A gate that stops a
session" now reads "A gate". The bullet at lines 386-391 still has a gate to describe:
`chain_check.py:1782` reads a `no work item` trailer and prints it as a
notice. A `git grep` for "commit or branch switch", "commit proceeds" and
"wrong deny" outside `seal/threads/` lists only line 352 and two test
docstrings about the release check (executed). The `gaps.md` paragraph that
deferred the two sentences is gone, as the finding asked. It stood under
`## Not done`, not as a `## Not verified` row, so taking it out owes no
`closed` mark (read).

```seal
confirms: round-1#6
```
What holds: the three blocks stand as round 1 gave them. They are at
`CONTRIBUTING.md:458-462`, `docs/checks/the-stamp.md:172-173` and the
docstring of `seal_stamp.py#hook_command` (lines 1584-1590). The command
the docstring describes is unchanged. The re-run of the fallback probe
exited 127 (executed). `seal_stamp.py#remove` (lines 1667-1699) matches the
entry by its command string, built from the data directory, and needs no
launcher. So `seal stamp --remove` does take out an entry that outlived its
launcher, as the new sentences say (read). `docs/checks/the-stamp.md:93`
spells `--remove` with its arguments, so the short form at line 173 refers
back to it. `tests/skills/test_seal_stamp.py` passed in the narrow run
(executed).

What matched: `c6ec999a`'s `.test_durations` is byte-identical to the
`test-durations` artifact of run 42179293981. `cmp` against the downloaded
file exited 0. `gh run view` gives the run's head as `fa496f3f` on this
branch. In that run, every `pytest` job that failed reported "1 failed",
and the one case was `test_the_durations_file_prices_the_suite`. At
`11d6c3b9` that case passes when the whole suite is collected (executed).
The orchestrator's account of the commit holds.

No test was added in the range. The one test change is the edit to the
`LOCAL_LIMIT` strings under `confirms: round-1#3`, so no new case had to be
read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the repository-wide lint and the format check at `11d6c3b9`: `unverified`, since contract rule 2 leaves the broad gate to the orchestrator and this round ran eleven modules and one collected case | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| Whether the plugin's data directory sits under `CLAUDE_CONFIG_DIR` where that is set, as the fragment's *Updating* line says; `skills/update/SKILL.md:221` reads `installed_plugins.json` there, and no case or probe here can set the variable for the harness | `seal/threads/1793935041-the-directory-refuses-every-command-hook/changelog.md:15` | the owner |
| What the harness shows a person for a `Stop` entry that exits 127, carried from round 1's row | `docs/checks/the-stamp.md:172-173` | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_first_setup_asks_once.py tests/lib/test_optin.py tests/skills/test_seal_stamp.py tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/behaviour/test_release_hygiene.py` in the clone | 509 passed, 2 skipped, exit 0; one skip is the durations case, which declines without the whole suite collected |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` in the clone | 1 passed, exit 0 |
| `gh run download 42179293981 -n test-durations -D` a scratch directory, then `cmp` against the clone's `.test_durations` | download exit 0, `cmp` exit 0 |
| `gh run view 42179293981 --json headSha,headBranch,conclusion,jobs` and `--log-failed` | head `fa496f3f` on this branch; each failing `pytest` job reports `1 failed`, the durations case |
| `git show <sha>:.test_durations \| grep -c 'tests/hooks/'` at `fa496f3f` and `11d6c3b9` | 848 and 0 |
| `sh -c 'python3 "<a path that does not exist>/stamp.py" \|\| py -3 "<a path that does not exist>/stamp.py"'`, exit code read directly | 127 |
| `grep -c stamp` over the installed 0.32.6 copy's `skills/update/SKILL.md` | 0, exit 1 |
| round 1's two `git grep` commands for finding 2, and `git grep` for "last four rows", "two questions", "question alone", "commit or branch switch", "commit proceeds" and "wrong deny", in the clone | as `## Confirmations` states |
