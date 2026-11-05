# Review round 1: 1793853196-the-readme-names-every-network-place

```seal
target: ccf52fa3 against release/v0.32.4
```

The round reviewed the branch from `release/v0.32.4` (31558c76) to HEAD
ccf52fa3. It read the routing, the frame, `gaps.md`, `changelog.md` and
`trail/phases/phase-1.md` as the implementer's account, and checked each
claim against the tree. No earlier round exists, so no fact was carried:
every coordinate below was opened this round.

The record language is English, since `seal/config.md` has no
`Record language` row. No `seal/parity.md` is declared, so no parity
comparison applies.

## Findings

### 1. The new `uv run` sentence omits that uv downloads a Python interpreter from GitHub where none on the machine fits the project

```seal
severity: should
location: `README.md:308-314`, `README.ko.md:311-317`, `seal/threads/1793853196-the-readme-names-every-network-place/changelog.md:3`
evidence: executed `uv run --offline ruff --version` in a scratch project with `[project]`, `requires-python = "==3.10.*"` and `[tool.ruff]`, uv 0.9.18, with a scratch `UV_CACHE_DIR` and `UV_PYTHON_INSTALL_DIR` (exit 2); `strings` over the uv binary for its interpreter download base; read `hooks/lint-python.py:71-78`
```

Why it matters: the issue exists because the README is what the plugin
directory's data-handling answer points to, so a place the README leaves out
is the defect this work removes. Build commit b7e392d8 added a sentence on
lint-python's first runner, `uv run ruff`. The sentence says that uv
"installs the project's dependencies, from PyPI where its cache lacks them".
`hooks/lint-python.py:71-76` runs `uv run ruff --version` in the session's
directory whenever `uv` is on the PATH and the edited file's project
configures ruff. `uv run` resolves the project's interpreter before it runs
anything. Where no interpreter on the machine satisfies the project's
`requires-python`, uv downloads a managed CPython build by default.

The probe shows this step. With `--offline`, uv exited 2 and said: "No
interpreter found for Python ==3.10.* in managed installations or search
path" and "hint: A managed Python download is available for Python
==3.10.*, but uv is set to offline mode". Online, that download is what
happens. The uv 0.9.18 binary carries GitHub's release downloads of
`astral-sh/python-build-standalone` as its download base. So lint-python
can reach GitHub as well as PyPI, and neither edition says so. The phase
record's own probe measured only the dependency install
(`trail/phases/phase-1.md`, *Row 2 was short*). This finding extends the
same runner's reach by one more fetch.

The fix keeps the pinned first sentence. Both editions wrap within 88
display columns, and `tests/behaviour/test_docs_line_wrap.py` should be run
over them after the edit. The changelog fragment states the same sentence
and owes the same clause. `frame/design.md` *Scope* 1 and census row 2 state
the dependency install alone. They are the frame's, so the orchestrator
decides whether to fold the clause in.

```markdown
lint-python and version-check reach the network. lint-python first tries
`uv run ruff`, and in a project whose `pyproject.toml` has a `[project]`
table, uv then installs the project's dependencies, from PyPI where its cache
lacks them. Where no Python on the machine satisfies that project's
`requires-python`, uv first downloads one from GitHub. lint-python falls back
to `uvx ruff`, and uv fetches ruff from PyPI on first use. version-check runs
one `git ls-remote --tags` against this repository, once a day where `seal/`
exists, which tells GitHub that a machine somewhere runs AgenticSeal. Each
stays silent when the network is unavailable.
```

```markdown
네트워크를 타는 훅은 lint-python 과 version-check 입니다. lint-python 은 먼저
`uv run ruff` 를 시도합니다. `pyproject.toml` 에 `[project]` 테이블이 있는
프로젝트라면 이때 uv 가 그 프로젝트의 의존성을 설치하고, 캐시에 없는 것은
PyPI 에서 내려받습니다. 그 프로젝트의 `requires-python` 을 만족하는 Python 이
컴퓨터에 없으면 uv 가 먼저 GitHub 에서 Python 을 내려받습니다. lint-python 이
`uvx ruff` 로 넘어가면 uv 가 처음 한 번 PyPI 에서 ruff 를 내려받습니다.
version-check 는 `seal/` 이 있는 곳에서 하루에 한 번 이 저장소에
`git ls-remote --tags` 를 보내고, 이때 GitHub 은 어딘가의 기계가 AgenticSeal 을
쓴다는 것을 알게 됩니다. 어느 훅이든 네트워크가 없으면 아무 말 없이
넘어갑니다.
```

In `changelog.md:3`, the sentence beginning "The lint-python sentence now
also says" ends instead:

```markdown
The lint-python sentence now also says that its first runner, `uv run ruff`, installs the dependencies of a project whose `pyproject.toml` has a `[project]` table, from PyPI where uv's cache lacks them, and first downloads a Python from GitHub where none on the machine satisfies the project's `requires-python`.
```

```seal
verdict: fixed fea52aea
answer: Holds. `hooks/lint-python.py:71-76` runs `uv run ruff --version` in the session's directory, and a re-run of the round's probe (uv 0.9.18, `requires-python = "==3.10.*"`, scratch cache and interpreter directories, `--offline`) exited 2 with "A managed Python download is available for Python ==3.10.*, but uv is set to offline mode" (executed). The sentence the round proposed went into `README.md` and `README.ko.md` after the dependency sentence, as folded *Scope* 1 says, with the paragraph rewrapped to the current text; the pinned first sentence stands. `changelog.md` takes the proposed clause. The narrow modules, `tests/behaviour/test_docs_line_wrap.py` among them, passed at fea52aea (executed).
```

### 2. `CONTRIBUTING.md` still describes lint-python's network reach as the `uvx` fetch alone

```seal
severity: should
location: `CONTRIBUTING.md:447-450`
evidence: executed `git grep -n 'uvx' -- ':!seal/' ':!tests/'` and `git diff release/v0.32.4..HEAD --stat -- CONTRIBUTING.md` (no change); read `CONTRIBUTING.md:443-455`, `hooks/version-check.py:23-25`, `seal/threads/1793853196-the-readme-names-every-network-place/gaps.md`, `seal/threads/1793853196-the-readme-names-every-network-place/frame/plan.md` *Judgments of the run*
```

Why it matters: under the rule "Every hook that reaches the network is named
in the README's privacy section", `CONTRIBUTING.md:449` says what lint-python
sends: "`lint-python` fetches ruff through `uvx` when no local copy exists."
Build commit b7e392d8 established that lint-python's first runner, `uv run`,
also installs a project's dependencies, and the README now says so. This
work corrected the other statement of the old account,
`hooks/version-check.py`'s "after lint-python's `uvx ruff` fetch". It did
that on the ground the frame gives in its first *Grounding* row: "in the
same commit removes what stood on the old fact". Line 449 is one more
statement of that old fact. It is still literally true, but a contributor
reads it as everything lint-python sends.

The claim was that `frame/design.md` keeps `CONTRIBUTING.md` out of this
work. The frame's reason was about the reach of the rule, at lines 447 and
448: the rule covers hooks only, and Q1 asks whether it should widen. That
reason was written before the `uv run` reach was known, and it does not
weigh line 449. `gaps.md` *Not done* hands the line to the orchestrator.
The fold at 9dc97c37 took in `tests/hooks/test_version_check.py:1` and
recorded no judgment on line 449, so the line is left with no decision and
no owner.

The rule sentence the #1055 case pins
(`tests/behaviour/test_chain_hooks_hardening.py`, "Every hook that reaches
the network is named in the README's privacy section") stays as it is. So
does Q1's default (a), since the rule's reach does not change. The fix
replaces the two lines that restate per hook what the README now states in
full with a pointer to that passage. That removes the copy instead of
widening it, as `skills/core/SKILL.md` *The rule a mechanism is kept
against* asks: "A fact has one source, and every other place links to it".
Because the fix touches `CONTRIBUTING.md`, it departs from the frame's
sentence "This work leaves `CONTRIBUTING.md` alone". The fix pass records
that departure in the phase record, or the orchestrator amends the frame
row. `docs/running/measuring-a-run.md` *Where a reading goes* still names
this bullet through `## Rule changes`, and its `to` text ("names the hooks
that reach the network") stays true after this edit.

```markdown
  Every hook that reaches the network is named in the README's privacy
  section, because a rule with undisclosed exceptions is not a rule.
  `README.md` *What runs on your machine* says what each one sends, and when.
  A new one needs the same limits `version-check` carries (an opt-in
```

The remaining lines of the bullet, from "condition so unrelated repos are
untouched" on, stay as they are.

```seal
verdict: fixed fea52aea
answer: Holds, and the fix is written in my own words rather than the paste-ready text. Folded *Scope* 6 asks that the two per-hook sentences become one sentence that names both hooks and points to `README.md` *What runs on your machine*, and `hooks/version-check.py`'s docstring says "`CONTRIBUTING.md` names it as an allowed exception", which the proposed text would have made untrue by dropping version-check's name. `CONTRIBUTING.md:449-450` now reads "`lint-python` and `version-check` are those hooks, and `README.md` *What runs on your machine* says what each one reaches, what it sends and when." The #1055-pinned rule sentence, the limits after it, "privacy section" and Q1's default stand, and no sentence counts the hooks. `gaps.md` *Not done* no longer lists the line, and `changelog.md` names the change. `tests/behaviour/test_chain_hooks_hardening.py` passed at fea52aea (executed).
```

## Confirmations

What matched: the census rows 3 to 8 match the code each one cites, as both
editions now state them. Row 3, `/agentic:update`, matches
`skills/update/SKILL.md` steps 2 and 3: `claude plugin marketplace update`,
`claude plugin update`, then one `curl` with no token to the releases API
for the clone's `origin` (read). Row 4, `seal cost --post`, matches
`skills/verify/scripts/session_cost.py:2931-3092`. It runs
`gh issue list --label <label> --state all`, then `gh issue comment` on the
one open issue, and posts nothing at `NO_HISTORY` or where `gh` is missing.
It never opens an issue (read). Row 5, `seal gate`, matches
`skills/verify/scripts/broad_gate.py:3081-3086`, whose chain arm always runs
`chain_check.py`, and `skills/code-review/scripts/chain_check.py:536-590`,
which asks `gh pr view --json isDraft` where `GITHUB_EVENT_PATH` names no
file and `gh` is on the PATH. Running the check this round printed exactly
that lookup's answer (executed). Row 6, `seal settle`, matches
`skills/settle/scripts/settle.py:402-430` and `:504-511`, and the callers at
`:626` and `:695` (read). Row 7's markdown coordinates are `agents/framer.md:66`
and `:74`, `skills/commit-pr-convention/SKILL.md:30`,
`skills/code-review/orchestration.md:257-346` and `skills/settle/SKILL.md:234`.
Every `gh` there runs without `-R`, so each reaches the repository the session
works in, and the closing sentence's "no other" holds (read). Row 8 matches
`templates/setup/hygiene.yml:66-67` and its `permissions: contents: read`
with no `gh` step (read).

What matched: S2 holds. The `--post` row says the orchestrator runs it after
each crafter or proofer hand-back, that a person may type it, and that
nothing is posted where no issue ever carried `flow-measurement` or `gh` is
missing. That is what `skills/verify/scripts/session_cost.py#post` does (read).

What matched: the crafter claimed the S1 census over `git archive` was
complete for the processes and network imports under `hooks/`, `skills/` and
`bin/`. This round extracted `git archive` of ccf52fa3 (171 files) and
listed the argv of every `subprocess` call in the shipped Python (executed).
Outside the rows, every call runs a local `git` verb, `pytest`, the plugin's
own scripts or the user's `Broad gate` row. `hooks/lib/launch.py` starts no
process. The list is the same as the phase record's, apart from finding 1,
which is a further reach of row 2's runner and not a new place.

The markdown half is a sample, as both the frame and the phase record say.
Their search left out `docs/`, which `dist` ships. This round searched
`docs/` for `gh`, `git push`, `git fetch`, `curl` and `uvx` (executed). It
found nothing outside `docs/releasing/`, which holds the plugin
maintainer's release procedure. A shipped step points there once
(`skills/verify/orchestration.md:233`), and only for the tracker's label
conventions, so no step in a user's repository runs it.

What matched: the widened case holds its rows. Through the case's own
`network_passage`, each of the six `NETWORK_PLACES` markers stands exactly
once in each edition's passage, and the passage ends before `## Commands`
and `## 명령` (executed). So deleting any one table row takes away its
marker's only occurrence, and `assert place in passage` fails. That bears
out the claimed `seal mutate` result of 12 of 12 red, which this round
reached by the count and did not re-run. The README passages at 3538fd59
are the base lines this diff removes, and they name none of the markers
(read), as the case's docstring says.

What matched: the six narrow modules passed at ccf52fa3: 142 tests. They were
`tests/behaviour/test_chain_hooks_hardening.py`,
`tests/behaviour/test_both_editions_carry_the_same_folds.py`,
`tests/behaviour/test_docs_line_wrap.py`,
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/behaviour/test_release_hygiene.py` and
`tests/hooks/test_version_check.py` (executed). That covers S3 to S6. S7
holds: `git grep -n "second network touch" -- ':!seal/'` exited 1 (executed).

What matched: *Scope* 4 holds. `hooks/version-check.py:23-25` changed in
the docstring alone, and `tests/hooks/test_version_check.py:1` changed its
first line alone (read in the diff). Another sentence,
`tests/hooks/test_lint_python.py:1`, calls lint-python "the one hook that
rewrites the user's source and can hit the network". It describes the one
hook that has both properties, so it is still true and is no instance of
the old fact.

What matched: the three `## Rule changes` operations each place once in
`docs/running/measuring-a-run.md` *Where a reading goes*. Each was applied
in memory through `skills/settle/scripts/rule_changes.py#parse` and
`#apply_op` (executed). The chain check printed no notice of a test pin or
a copy at a line of `frame/design.md` (executed).

The uv dependency install the phase record probed with uv 0.9.18 was not
re-run. This round's probe found that `uv run` resolves the project's
interpreter before it runs ruff, which agrees with that claim (executed).
The `uv run` sentence is held by the S1 reading at review and by no case,
which is the verification `frame/design.md` S1 chose for a cell's content.

`gaps.md` *Not done* names one more item: the `.venv` and `uv.lock` that
`uv run` leaves in the user's project. That is a write the side-effects
paragraph at `README.md:298-306` does not name. It came before this branch
and is not a network place, so it is outside #1382 and this round opens no
finding for it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD; contract rule 2 keeps them from this round, and the crafter's `unverified` label for them is honest | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| Whether `CONTRIBUTING.md`'s hook rule widens to every shipped network call; the build took default (a) | `frame/questions.md` Q1 | the owner, through the orchestrator's report |
| Whether the plugin directory's reviewer reads a true README at the next `dist` commit | `frame/design.md` S8 | the owner |

## Probes

| Command | Result |
|---|---|
| `git archive HEAD` of ccf52fa3, extracted under the round's scratch directory, then a listing of every `subprocess` argv in `hooks/`, `skills/` and `bin/` | 171 files. The network calls are `hooks/version-check.py:129`, `hooks/lint-python.py:73` and `:78`, `session_cost.py:2944`, `chain_check.py:227` and `settle.py:224`; every other call is a local `git` verb, `pytest` or a plugin script |
| A search of shipped `docs/` for `gh`, `git push`, `git fetch`, `curl` and `uvx` | hits only under `docs/releasing/` and one prose mention of `--post` |
| `uv run --offline ruff --version` in a scratch project with `requires-python = "==3.10.*"` and `[tool.ruff]`, scratch cache and interpreter directories, uv 0.9.18 | exit 2: "No interpreter found for Python ==3.10.*", hint "A managed Python download is available ... but uv is set to offline mode". The project, the cache and the output file were removed afterwards |
| `strings` over the uv binary, filtered for `python-build-standalone` | the download base is GitHub's release downloads of `astral-sh/python-build-standalone` |
| `bin/test` over the six narrow modules named under *Confirmations* | exit 0, 142 passed |
| The case's `network_passage` and `NETWORK_PLACES`, called through the runner's `.venv` interpreter, counting each marker in each edition's passage | every marker counted 1 in both editions; the passage ends at the closing sentence |
| `skills/settle/scripts/rule_changes.py` `parse` and `apply_op` over `frame/design.md` and `docs/running/measuring-a-run.md`, in memory | all three operations placed; the policy file was not written |
| `chain_check.py --baseline release/v0.32.4 --root <the branch worktree> --worktree`, the installed 0.32.3 copy and the tree's copy | exit 0 before this record was written; it named the missing round, gate and guarantee files and no notice on `frame/design.md` |
