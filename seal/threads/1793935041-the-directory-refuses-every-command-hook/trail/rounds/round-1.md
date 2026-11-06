# Review round 1: 1793935041-the-directory-refuses-every-command-hook

```seal
target: fa496f3f against release/v0.33.0
```

The round read the branch against its base, `git diff release/v0.33.0...fa496f3f`,
in a `git clone --no-local` at `fa496f3f`. No earlier round record exists, so
no coordinate was carried and every fact below was established this round.
The frame, the plan, `questions.md`, `gaps.md`, the seven phase records and
the changelog fragment were read as the implementer's account and checked
against the tree; where a claim is weighed below, the record says what was
claimed and what the tree holds.

## Findings

### 1. First setup's batch is stated as two questions, and as the `Broad gate` question alone, where the stamp question is a third

```seal
severity: should
location: `skills/implement/bootstrap.md:42`, `skills/implement/bootstrap.md:44-47`
evidence: read `skills/implement/bootstrap.md:40-47`, `skills/implement/bootstrap.md:158-175`, `tests/behaviour/test_first_setup_asks_once.py:148`
```

Why it matters: the orchestrator builds its one `AskUserQuestion` call from
this file. Line 42 says that where `<repo>/seal/` is the project's own, the
call "carries the `Broad gate` question alone", so an orchestrator on that
branch leaves out the stamp question the paragraph at lines 158-175 adds.
Step 1 opens "carrying **two questions**" and then names three. *Scope* item
7 of `frame/design.md` puts the stamp question into "`bootstrap.md`'s one
batch for a repository set up after this release" with no exception for a
project-owned `seal/`. The case at `tests/behaviour/test_first_setup_asks_once.py:148`
pins the words "two questions", so the fix keeps them.

```markdown
mode"*. The one call of step 1 then carries the `Broad gate` question, and
the stamp's where nothing records an answer to it.

1. The orchestrator asks once, with one `AskUserQuestion` carrying **two
   questions**, or three: the mode, the `Broad gate` row, and the stamp
   where nothing records an answer to it. The mode's three options come
   first, in this order:
```

```seal
verdict: fixed 1f412308
answer: Applied as written after reading it against `skills/implement/bootstrap.md:158-175`, which puts the stamp question as the third where `seal stamp --hook` prints `neither`, and against `frame/design.md` *Scope* item 7. Line 42 now says the one call carries the `Broad gate` question and the stamp's where nothing records an answer, and step 1 keeps "two questions" for `tests/behaviour/test_first_setup_asks_once.py:148` and adds "or three". `bin/test tests/behaviour/test_first_setup_asks_once.py` is in the set that passed, exit 0.
```

### 2. The opt-in section of the root-by-lifetime document still says the hooks read the root and act on it

```seal
severity: should
location: `docs/layout/one-root-by-lifetime.md:68-69`, `docs/layout/one-root-by-lifetime.md:81-87`, `docs/layout/one-root-by-lifetime.ko.md:64-65`, `docs/layout/one-root-by-lifetime.ko.md:76-82`, `skills/implement/bootstrap.md:26-27`
evidence: executed `git grep -n -i -w -E 'hooks?' -- docs skills agents templates README.md README.ko.md CONTRIBUTING.md SECURITY.md CLAUDE.md lib bin` and `git grep -n -i -E 'gated|agentic-scratch|gates off|every gate here'` over the clone at fa496f3f; read `seal/threads/1793935041-the-directory-refuses-every-command-hook/frame/plan.md:9`
```

Why it matters: these sentences tell a reader that hooks resolve the
opt-in and act on an opted-in repository, and after this branch no hook is
registered. The English section says "The hooks look at the two places in
that order", "because the hooks are the plugin's" and "a hook that cannot
tell does nothing"; its table says a collaborator who set nothing up is
"gated, once the plugin is installed"; and it says a throwaway repository
"turns the gates off". The Korean edition says the same at lines 64 and
76-82 ("훅은 두 자리를 그 순서로 보고", "훅이 플러그인의 것이기
때문입니다", "판단하지 못하는 훅은", "게이트에 걸린다", "게이트를
끕니다"). `skills/implement/bootstrap.md:26-27` tells the orchestrator that
"from the next command on, every gate here is awake".

`frame/plan.md` *Technical context* names `docs/layout/one-root-by-lifetime.md:83-85`
among the closed set the crafter edits. The branch changed only the
`check:` lines and one path in that file, and the phase records do not name
these sentences. Who reads the opt-in now was found by the grep for
`home_at(` and `opted_in(` outside `tests/`: the `seal` commands, the pull
request's check and the stamp's `--stop` (`skills/verify/scripts/seal_stamp.py:1505`).
`skills/core/SKILL.md` *The rule a mechanism is kept against* removes, in
the change that drops a fact, every sentence that stood on it.

The fix stops at `templates/setup/seal-README.md:62,68` and the module
docstring of `lib/optin.py`, which say "gates" for the readers of the root.
A reading of "gate" as the pull request's check and the commands that
refuse still holds there, so the fix pass judges them.

```markdown
The `seal` commands, the pull request's check and the stamp's `--stop` look
at the two places in that order; whichever exists with the marker says both
"on" and which mode.

| A collaborator who set nothing up | in the workflow, once the plugin is installed | runs nothing, because their clone has no root under its git directory |

A collaborator who never installed the plugin runs nothing in either mode,
because the entry skill and the `seal` commands are the plugin's. The fail
direction is that no folder at either place means not opted in, and a
command that cannot tell reads the repository as not opted in.
A throwaway repository reads as not opted in with an empty file,
`.git/agentic-scratch`, under the common git directory, which no commit can
carry to another clone.
```

```markdown
`templates/setup/seal-README.md` 의 첫 줄이고, 처음 설정이 이것을 씁니다.
`seal` 명령과 pull request 검사, 도장의 `--stop` 은 두 자리를 그 순서로 보고,

| 아무것도 설정하지 않은 협업자 | 플러그인을 깔면 워크플로를 따른다 | 그 클론의 git 디렉터리 아래에 루트가 없으니 아무것도 돌지 않는다 |

플러그인을 깔지 않은 협업자에게는 어느 모드에서도 아무것도 돌지 않습니다.
entry 스킬과 `seal` 명령이 플러그인의 것이기 때문입니다. 실패 방향은, 두
자리 어디에도 폴더가 없으면 옵트인하지 않은 것이고, 판단하지 못하는 명령은
저장소를 옵트인하지 않은 것으로 읽는다는 것입니다. 버릴 저장소는 공통 git
디렉터리 아래의 빈 파일 `.git/agentic-scratch` 하나로 옵트인하지 않은
저장소로 읽힙니다. 어떤 커밋도 이 파일을 다른 클론으로 옮기지 못합니다.
```

```markdown
Creating the root is what opts the repository in: from the next command on,
the `seal` commands and the pull request's check read it. Where the root lands,
```

```seal
verdict: fixed 1f412308
answer: The three blocks were applied after `git grep -n -E 'home_at\(|opted_in\('` outside `tests/` confirmed the readers: the `seal` commands, `chain_check.py`, `pr_body.py`, `settle.py`, `fold_check.py`, `pact_check.py`, `unverified_check.py`, `release_seal.py` and the stamp's `--stop` at `seal_stamp.py:1505`. Both editions of `docs/layout/one-root-by-lifetime.md` *The opt-in signal is the root itself* now name those readers, the table's shared-mode cell reads "in the workflow", and the scratch file reads the repository as not opted in. `skills/implement/bootstrap.md:26-31` says the commands and the pull request's check read the root, rewrapped to the 88-column limit `tests/behaviour/test_docs_line_wrap.py` holds. Judged and left: `templates/setup/seal-README.md:57,62,68`, `seal/README.md` at the same lines and the module docstring of `lib/optin.py` say "gate" for a reader of the root. In this repository "gate" names any command or check that reads the root and refuses, as `skills/config/SKILL.md:85` and `templates/setup/config.md:182` use it, so those sentences hold without a hook. The class was listed with the round's own two `git grep` commands (`-w hooks?` over the shipped roots, and `gated|agentic-scratch|gates off|every gate here`). The hits left name pytest's hooks, git's hooks, a generic mechanism list, or "gate" in the sense above. That list is a sample: it is built from spellings, and a sentence that describes a hook's act without either word is outside it.
```

### 3. The README's local-mode limit names "the last four rows" of a table that has four, and phase 6's record says the core still reads that way

```seal
severity: should
location: `README.md:169-172`, `README.ko.md:169-172`, `tests/behaviour/test_first_setup_asks_once.py:477-489`, `seal/threads/1793935041-the-directory-refuses-every-command-hook/trail/phases/phase-6.md:66-68`
evidence: read `skills/core/SKILL.md:98-109`, `README.md:169-172`, `README.ko.md:169-172`; executed `git show bd971897:skills/core/SKILL.md | grep -n "four rows"`, which prints line 106, "the four rows"
```

Why it matters: phase 2 (`e29a20ba`) took row 1 out of the core's table and
rewrote the sentence under it from "the last four rows" to "the four rows",
as *Scope* item 3 asks. Phase 6 then wrote the README paragraph with "the
last four rows". A person reading it looks for an earlier row the limit
does not cover, and the table holds none.

Claimed: `trail/phases/phase-6.md:66-68` says the core's "closing sentence
already says that in local mode the last four rows are held by
`agents/sealer.md` step 1 and the orchestrator". Found: at `bd971897`, the
commit that added the README paragraph, the core reads "the four rows", and
so does HEAD. The phase record restates the core's sentence and has drifted
from it, so `docs/forms/the-round-record.md` answers it by removing the
copy and citing the home. The case at `tests/behaviour/test_first_setup_asks_once.py:477-489`
pins both editions' wording, so the fix changes it in the same commit.

```markdown
In local mode no pull-request check reads the records, so
`agents/sealer.md` step 1 and the orchestrator's guidance alone hold the
four rows of `skills/core/SKILL.md` *Judgment is not licence to skip a
party*, and that is a limit.
```

```markdown
local 모드에서는 기록을 커밋하지 않으므로 pull request 검사가 읽을 기록이
없습니다. 그래서 `skills/core/SKILL.md` *Judgment is not licence to skip a
party* 표의 네 행은 sealer 의 1단계(`agents/sealer.md`)와 작업을
이끄는 세션이 따르는 지침만이 지키며, 이것이 local 모드의 한계입니다.
```

The two `LOCAL_LIMIT` strings of the case take the same words. In
`trail/phases/phase-6.md`, the sentence becomes: "It cites
`skills/core/SKILL.md` *Judgment is not licence to skip a party*, whose
closing sentence says who holds the table's rows in local mode."

```seal
verdict: fixed 1f412308
answer: Read `skills/core/SKILL.md:98-109`: four rows, and "the four rows" under them. Both READMEs now say "the four rows" and "네 행". The two `LOCAL_LIMIT` strings in `tests/behaviour/test_first_setup_asks_once.py` were changed first, and both parameters of `#test_the_readme_states_what_local_mode_leaves_unchecked_under_the_table` ran red (exit 1, 2 failed) before the READMEs were edited, then passed. `trail/phases/phase-6.md` takes the sentence the finding gives. `git grep -n -E 'last four rows|마지막 네 행'` outside `seal/threads/` now lists nothing.
```

### 4. The changelog tells a person updating from 0.32 that `/agentic:update` asks about the stamp, and names `seal stamp --install` without the arguments it requires

```seal
severity: should
location: `seal/threads/1793935041-the-directory-refuses-every-command-hook/changelog.md:15`
evidence: executed `grep -n stamp ~/.claude/plugins/cache/agenticseal/agentic/0.32.6/skills/update/SKILL.md`, which printed nothing; read `skills/verify/scripts/seal_stamp.py:1784-1810`, `skills/update/SKILL.md:39-42`, `seal/threads/1793935041-the-directory-refuses-every-command-hook/frame/plan.md:63`
```

Why it matters: the fragment's *Updating* line is what a person reads in
the release note before acting. It says "`/agentic:update` asks once whether
to draw the terminal stamp". The update that installs 0.33.0 runs the
update skill of the copy the session started on, and 0.32.6's has no step
4b: the grep above found no line naming the stamp. The 0.32.x stamp hooks
stop at the restart onto 0.33.0, which registers none. So the person who
just ran `/agentic:update` was asked nothing, and their stamp stops with
nothing saying so. That is the case *Scope* item 7 names as the reason the
update asks at all. `frame/plan.md` *Operational impact* says the owner
meets the question "at the first `/agentic:update` after 0.33.0", and the
fragment drops "after".

The line also tells a person who answered no to run `seal stamp --install`.
`seal_stamp.py#main` gives `--install` a required `DATA_DIR` and refuses it
without `--settings`, so the command as written exits 2.

The data directory below is the one the frame's *Grounding* listed on one
machine with `ls ~/.claude/plugins/data/`. Where the fix pass would rather
not name it, the line can send the person to `seal stamp --hook` in
`README.md` *What runs on your machine* instead.

```markdown
Updating: nothing to do for the hooks, since none is registered. The update that installs 0.33.0 runs the earlier release's `/agentic:update`, which does not ask about the stamp, and the earlier release's stamp hooks stop at the restart onto 0.33.0. Run `/agentic:update` once more after that restart: it asks once whether to draw the terminal stamp. A person who answered no and changes their mind runs `seal stamp --install ~/.claude/plugins/data/agentic-agenticseal --settings ~/.claude/settings.json`.
```

```seal
verdict: fixed 1f412308
answer: Read `skills/update/SKILL.md:39-42` at HEAD: where the update reports the plugin current, step 4b still runs, so a second `/agentic:update` after the restart onto 0.33.0 asks the stamp question. The fragment's *Updating* line now says that 0.32.x's update does not ask, that its stamp hooks stop at the restart, and that a second `/agentic:update` reports the plugin current and asks once. For a person who answered no, it gives `seal stamp --install ~/.claude/plugins/data/agentic-agenticseal --settings ~/.claude/settings.json` with both paths under `CLAUDE_CONFIG_DIR` where that is set. `ls ~/.claude/plugins/data/` on this machine lists `agentic-agenticseal`, and `seal_stamp.py#main` (lines 1784-1792) takes `--install DATA_DIR` with `--settings` as that command spells them.
```

### 5. CONTRIBUTING and the pull request template still say a gate decides whether a commit proceeds, which the README this branch rewrote no longer says

```seal
severity: should
location: `CONTRIBUTING.md:342`, `.github/PULL_REQUEST_TEMPLATE.md:29-30`, `seal/threads/1793935041-the-directory-refuses-every-command-hook/gaps.md:46-52`
evidence: read `CONTRIBUTING.md:340-344`, `.github/PULL_REQUEST_TEMPLATE.md:29-32`, `README.md:398-401`, `seal/threads/1793935041-the-directory-refuses-every-command-hook/gaps.md:46-52`
```

Why it matters: `CONTRIBUTING.md` *What a change to a gate must carry* opens
"The gates decide whether someone's commit or branch switch proceeds", and
the pull request template says "a gate decides whether somebody else's
commit proceeds". After this branch no gate stands at a session's commit or
branch switch: the hooks that refused a session's tool calls are removed.
The README paragraph that sends a contributor to this section was rewritten
in this branch to "a gate decides whether someone's pull request or run
goes ahead", so the two documents now disagree. `CLAUDE.md` names this
section as where every pull request to this repository answers the core's
rule, so it is read at every gate change.

Claimed: `gaps.md` *Not done* leaves both sentences because "no phase's
Delivers cell names it". Found: the core's *The rule a mechanism is kept
against* removes, in the change that drops a fact, every sentence that
stood on it, and the closing memo is the implementer's account and no
source that defers a stale sentence the branch made stale. Phase 7 edited
the template's line 29 to name `lib/` and left line 30.

```markdown
The gates decide whether someone's pull request or run goes ahead, so a
change to one is judged by what it does when it is wrong, and a change that
adds any mechanism by what it takes away:
```

```markdown
higher bar, because a gate decides whether somebody else's pull request or
run goes ahead. CONTRIBUTING.md, "What a change to a gate must carry", lists
```

The second block replaces lines 30-31 of the template and keeps its line 29
as it stands. The paragraph of `gaps.md` *Not done* that opens
"`CONTRIBUTING.md` *What a change to a gate must carry* still opens" goes
with the fix.

```seal
verdict: fixed 1f412308
answer: Both blocks applied as written, with the template's line 31 rewrapped. The `gaps.md` *Not done* paragraph is gone. The same section of `CONTRIBUTING.md` held two more sentences that stood on hooks stopping a session, so they are fixed in the same commit. Under *A stated failure direction*, "A wrong deny costs a prompt; a wrong allow can break another session's tree" now reads that a wrong deny stops a correct pull request or run until someone repairs the gate, and a wrong allow lets through what the gate was there to stop. Under *A gap only work with no work item passes through*, "A gate that stops a session" now reads "A gate". `git grep -n -E "commit or branch switch|commit proceeds|wrong deny"` lists no other statement of the old gate outside `seal/threads/` and two test docstrings about the release check's own deny. That list is a sample built from spellings.
```

### 6. CONTRIBUTING says the stamp hook's fallback runs only when `python3` cannot start, and a settings entry whose launcher is gone fails at every turn

```seal
severity: should
location: `CONTRIBUTING.md:455-459`, `docs/checks/the-stamp.md:168-172`, `skills/verify/scripts/seal_stamp.py:1584-1587`
evidence: executed `sh -c 'python3 "<a path that does not exist>/stamp.py" || py -3 "<a path that does not exist>/stamp.py"'; echo $?`, which printed 127; read `CONTRIBUTING.md:449-462`, `README.md:50-52`
```

Why it matters: `CONTRIBUTING.md` says the fallback "is safe because the
launcher exits 0 whatever happens, so `||` is reached only when the first
interpreter could not start". That holds while the launcher file exists.
Where the `Stop` entry outlives its launcher, `python3` exits 2 on the
missing file, `py -3` runs, and on a machine with no `py` the entry exits
127 at the end of every turn in every repository. That state arises where
the data directory is removed while the entry stays, such as an uninstall
without the `seal stamp --remove` that `README.md:50-52` asks for first.
`docs/checks/the-stamp.md` lists where the hook draws nothing and says
nothing, and names no such state. A shape outside the normal flow is stated
as a limit, not guarded, so the fix is three sentences. What the harness
shows the person for that exit was not measured (`## Not judged`).

```markdown
  is the one name its official installer does not create. While the
  launcher stands, the fallback is reached only when the first interpreter
  could not start, because the launcher exits 0 whatever happens. Where the
  entry outlives its launcher, both halves fail at the end of every turn
  until `seal stamp --remove` takes the entry out. It reaches no network;
```

```markdown
gone. Where the settings entry outlives its launcher, its command fails at
the end of every turn until `seal stamp --remove` takes the entry out.
Where a file was written, the line `--guarantee` printed names
```

```python
def hook_command(data_dir):
    """The command of the `Stop` entry for the launcher under DATA_DIR:
    `python3` first and `py -3` where the first exits non-zero, which,
    while the launcher stands, is only where it could not start
    (`CONTRIBUTING.md` *House rules*)."""
```

```seal
verdict: fixed 1f412308
answer: Ran `sh -c 'python3 "/nonexistent-agentic-probe/stamp.py" || py -3 "/nonexistent-agentic-probe/stamp.py"'` on this machine, and it exited 127, as the finding measured. The three blocks were applied as written, as a limit and with no guard: `CONTRIBUTING.md` *House rules*, the list in `docs/checks/the-stamp.md` of where the hook draws nothing, and the docstring of `seal_stamp.py#hook_command`. `git grep -n -E 'could not start|exits 0 whatever|py -3'` outside `tests/` and `seal/threads/` lists no other sentence saying the fallback is reached only when `python3` cannot start. `README.md:307`'s "It exits 0 whatever happens" is about the launcher, and it holds. `uvx ruff check` and `uvx ruff format --check` on `seal_stamp.py` exited 0, and `tests/skills/test_seal_stamp.py` passed in the set, exit 0.
```

## Confirmations

What matched: the tree registers no hook. `git ls-files hooks/` prints
nothing at `fa496f3f`, and `git grep -n '"type": "command"' -- '*.json'`
exits 1 (executed). This is the first acceptance row of `frame/design.md`.

What matched: `git archive HEAD | tar -t` lists `.github/scripts/close_issues_on_release.py`,
`rules.py` and `run_tests.py` and no other script there, and no path under
`hooks/` (executed). This is *Scope* item 10 and the second acceptance row.

What matched: the frame's census grep for the eleven hook names,
`hooks/lib`, `seal no-work-item`, `seal core` and `the-session-hooks` lists,
outside `seal/threads/`, only the paths `trail/phases/phase-7.md` names as
kept on purpose: `.test_durations`, the recorded eval case
`evals/behaviour/proofer/seeded-7a8899d5/`, `evals/scripts/replay_targets.py`,
`tests/censuses.py`, `tests/test_censuses.py`, `tests/evals/test_replay_targets.py`,
and the two behaviour modules whose cases assert a removed name is absent
(executed).

What matched: the stamp's install, draw and removal behave as *Data &
interfaces* states. A probe installed into a scratch settings file holding
a model key, a person's own `Stop` entry and a `PreToolUse` entry. Every
key stayed, and a second install added nothing. The hook command ran under
the 3.9.6 `python3` macOS ships and under the default `python3`, in a plain
repository and in this opted-in clone. It exited 0 and printed nothing,
at a median of 37 to 44 ms per call. A values file queued in a scratch
local-mode clone drew once under 3.9 and was renamed `.drawn.json`.
`--remove` left the settings as they stood before the install (executed,
`## Probes`).

What matched: `skills/core/SKILL.md:98-109` holds four rows and reads "the
four rows" under them, as *Scope* item 3 states (read). `agents/sealer.md`
step 4 holds the sentence on a declared crafter's phase records and step 6
the one `seal stamp --guarantee` run, as *Scope* items 6 and 7 state (read).

What matched: phase 2's claim that `lib/gate.py` stays for the parity arm
holds. `skills/code-review/scripts/chain_check.py#parity_readers` loads
`lib/config.py` and `lib/gate.py` by path, and `originals_of` asks
`touches_code` (read `skills/code-review/scripts/chain_check.py:1485-1491`).

What matched: the narrow modules for the stamp, first setup, the packaging
cases, the sealer's definition and the archive census pass at `fa496f3f`
(executed, `## Probes`). This is a narrow run and no seal: the broad gate is
the orchestrator's.

The new cases were read against their groups. `seal layout --pairs` prints
one pair inside this diff, `tests/skills/test_seal_stamp.py::Test_main`'s
two `--stop` cases. They are no duplicate: one breaks `drawn_at_stop` and
reads the silence, and the other draws twice from a queued file.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the repository-wide lint and the format check at `fa496f3f`: `unverified`, since contract rule 2 leaves the broad gate to the orchestrator and this round ran five modules alone | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| Whether the harness substitutes `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}` and `$ARGUMENTS` in `skills/start/SKILL.md`, and whether a plain request makes the model invoke `agentic:start`; no case can run the harness | `skills/start/SKILL.md:27-52` | the owner, at the first request under the installed 0.33.0, as `gaps.md` *Not verified* rows 1 and 2 state |
| Whether `/plugin uninstall` removes the plugin's data directory, and what the harness shows the person for a `Stop` entry that exits 127 (finding 6) | `README.md:50-52` | the owner |
| Whether the portal's Validate refuses nothing in the release's `dist` | `seal/threads/1793935041-the-directory-refuses-every-command-hook/frame/questions.md` Q1 | the owner, after the tag |
| Whether the hook's `py -3` half starts the launcher on Windows | `skills/verify/scripts/seal_stamp.py:1584-1589` | the owner or a Windows user, as `gaps.md` *Not verified* row 6 states |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/skills/test_seal_stamp.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_a_cited_section_stands_in_its_file.py` in the clone | 360 passed, exit 0 |
| `python3 test_tmp_stamp_probe.py` in the clone, then deleted with its scratch directory | `--install` into a scratch data directory and settings file printed the line naming the launcher and kept every other key; a second `--install` added no entry; the hook command exited 0 with no output, median 44 and 38 ms in a plain repository and 43 and 37 ms in the opted-in clone, under the 3.9.6 and the default `python3`, against 20 ms for a bare 3.9.6 start; a queued values file in a scratch local-mode clone drew once under 3.9.6, 8,126 bytes of `systemMessage` JSON, and was renamed `.drawn.json`; `--remove` printed both removals and left the settings as before the install |
| `sh -c 'python3 "<a path that does not exist>/stamp.py" \|\| py -3 "<a path that does not exist>/stamp.py"'; echo $?` | 127 |
| `bin/seal layout --pairs` in the clone | exit 0; one pair inside this diff, read as no duplicate under `## Confirmations` |
| `git grep -l -E` for the frame's census names, `git ls-files hooks/`, `git archive HEAD \| tar -t` in the clone | as `## Confirmations` states |
