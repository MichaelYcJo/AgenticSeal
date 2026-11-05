# Review round 2: 1793853196-the-readme-names-every-network-place

```seal
target: 50cae2cd, fixes ccf52fa3..50cae2cd
```

This is a verifying round. It read the diff `ccf52fa3..50cae2cd`: the fix
commit fea52aea, the close blocks at fb045c93, the orchestrator's folds
9d7bf35c and 84ea3c3b, and the phase record's correction at 50cae2cd. It
answers round 1's two findings, both closed `fixed fea52aea`, and reads the
new text in that diff against the frame. The record language is English,
since `seal/config.md` has no `Record language` row. No `seal/parity.md` is
declared.

Facts carried from round 1 and not re-derived: the census of network calls
under `hooks/`, `skills/` and `bin/` (round 1 *Probes*, first row), since
this diff changes no code; the dependency install `uv run` makes, which the
phase record probed; and the network passage's markers counting once in
each edition. The fix diff adds no test, so no new test is read against its
group.

The crafter's account was read as claims. It claimed the offline probe was
re-run and exited 2 with "A managed Python download is available"; this
round ran a variant of that probe and got the same hint (*Probes*). It
claimed six narrow modules exit 0 at fea52aea; this round ran the same six at
HEAD 50cae2cd, and they exit 0. It called its `git grep` for restatements a
sample, which is honest: this round's search for the two removed
`CONTRIBUTING.md` sentences and their old wording outside the work item
found none (executed). It labelled the full suite `unverified`, which is
honest under contract rule 2.

## Findings

### 1. The new `uv run` sentence states the Python download's condition as `requires-python` alone, and uv also downloads for a `.python-version` pin

```seal
severity: should
location: `README.md:311-312`, `README.ko.md:314-315`, `seal/threads/1793853196-the-readme-names-every-network-place/changelog.md:3`, `seal/threads/1793853196-the-readme-names-every-network-place/frame/design.md:56`, `seal/threads/1793853196-the-readme-names-every-network-place/frame/design.md:98-101`
evidence: executed `uv run --offline ruff --version` with uv 0.9.18 and a scratch `UV_CACHE_DIR` and `UV_PYTHON_INSTALL_DIR`, in two scratch projects with `.python-version` set to `3.10`: one whose `pyproject.toml` holds `[tool.ruff]` alone, one with `[project]`, `requires-python = ">=3.9"` and `[tool.ruff]` (exit 2 in both); `uvx --offline ruff --version` in the first (exit 1, on ruff missing from the cache); `uv python list --only-installed`; read `hooks/lint-python.py:71-78`
reopens: round-1#1
```

Why it matters: the close of round 1's finding 1 does not hold in full. The
finding was that the README leaves out lint-python's Python download from
GitHub. The sentence fea52aea added names the download, and it was round
1's own paste-ready text. But it states the condition too narrowly: "Where
no Python on the machine satisfies that project's `requires-python`, uv
first downloads one from GitHub". uv also reads a `.python-version` file,
which `uv init` writes into every new project. The README is what the
plugin directory's data-handling answer points to, so a reader with such a
file learns the wrong answer to whether lint-python reaches GitHub.

The probe shows two cases the sentence does not cover. This machine has
CPython 3.9, 3.11, 3.12, 3.13, 3.14 and 3.15 installed and no 3.10.

- A project with `[project]` and `requires-python = ">=3.9"`, which installed
  interpreters satisfy, and `.python-version` set to `3.10`. uv exited 2:
  "No interpreter found for Python 3.10 in managed installations or search
  path", with the hint "A managed Python download is available for Python
  3.10, but uv is set to offline mode". Online, that download happens,
  although `requires-python` is satisfied.
- A project whose `pyproject.toml` has no `[project]` table, only
  `[tool.ruff]`, and the same `.python-version`. uv gave the same error and
  hint. The sentence ties the download to "that project", the one with a
  `[project]` table, so this case is outside it.

`hooks/lint-python.py:71-76` runs `uv run ruff --version` whenever `uv` is
on the PATH and the project configures ruff, so both cases reach the
download. The fallback is not affected: `uvx ruff` in the first project
failed only on ruff missing from the cache and asked for no Python 3.10. So
the README's `uvx` sentence stays true.

The fix names both sources of the version the project asks for, and moves
the download out of the `[project]` clause. It keeps the pinned first
sentence. Both editions wrap within 88 display columns as written, and
`tests/behaviour/test_docs_line_wrap.py` should be run over them after the
edit.

```markdown
lint-python and version-check reach the network. lint-python first tries
`uv run ruff`, and in a project whose `pyproject.toml` has a `[project]`
table, uv then installs the project's dependencies, from PyPI where its cache
lacks them. Where no Python on the machine satisfies the version the project
asks for, in a `.python-version` file or in `requires-python`, uv first
downloads one from GitHub. lint-python falls back to `uvx ruff`, and uv
fetches ruff from PyPI on first use. version-check runs one `git ls-remote --tags`
against this repository, once a day where `seal/` exists, which tells GitHub
that a machine somewhere runs AgenticSeal. Each stays silent when the network
is unavailable.
```

```markdown
네트워크를 타는 훅은 lint-python 과 version-check 입니다. lint-python 은 먼저
`uv run ruff` 를 시도합니다. `pyproject.toml` 에 `[project]` 테이블이 있는
프로젝트라면 이때 uv 가 그 프로젝트의 의존성을 설치하고, 캐시에 없는 것은
PyPI 에서 내려받습니다. 프로젝트가 `.python-version` 파일이나
`requires-python` 으로 요구하는 버전을 만족하는 Python 이 컴퓨터에 없으면
uv 가 먼저 GitHub 에서 Python 을 내려받습니다. lint-python 이 `uvx ruff` 로
넘어가면 uv 가 처음 한 번 PyPI 에서 ruff 를 내려받습니다.
version-check 는 `seal/` 이 있는 곳에서 하루에 한 번 이 저장소에
`git ls-remote --tags` 를 보내고, 이때 GitHub 은 어딘가의 기계가 AgenticSeal 을
쓴다는 것을 알게 됩니다. 어느 훅이든 네트워크가 없으면 아무 말 없이
넘어갑니다.
```

In `changelog.md:3`, the clause added by fea52aea ends instead:

```markdown
and first downloads a Python from GitHub where none on the machine satisfies the version the project asks for, in a `.python-version` file or in `requires-python`.
```

The snippets cover the two README editions and the changelog. They leave
three statements, which the fix pass or the orchestrator owes too. Two are
frame cells: census row 2 at `frame/design.md:56` ("where no installed
interpreter satisfies `requires-python`") and *Scope* 1 at
`frame/design.md:98-101`. Those are the frame's, so the orchestrator folds
the same condition into them. The third is `trail/phases/phase-1.md:38-40`,
which reports what round 1 found in round 1's words. It is an account of
that round and stays true as one, so it needs no edit.

uv can also download a managed Python because of its own settings, such as
`python-preference = "only-managed"` or `UV_PYTHON`. This round did not
probe them, and they are a user's configuration of uv rather than what the
project asks for. They stand under `## Not judged`.

```seal
verdict: fixed 8e605e8c
answer: Holds. A re-run of the round's second shape, a `pyproject.toml` with `[tool.ruff]` alone and `.python-version` at `3.10`, uv 0.9.18 `--offline`, exited 2 with "A managed Python download is available for Python 3.10" (executed). The sentence is written in my own words rather than the paste-ready text, following the orchestrator's judgment at c9f27afb (`frame/plan.md` *Judgments of the run*): `README.md` now reads "Where a project asks for a Python version the machine does not have, such as through a `.python-version` file or `requires-python`, uv first downloads that version from GitHub", so it names the condition by what the person sees and stays true under uv settings no round probed, and "a project" no longer ties it to the `[project]` clause before it. `README.ko.md` says the same, and `changelog.md:3` ends with the same condition, "with or without a `[project]` table". The paragraphs are rewrapped, and the narrow modules, `tests/behaviour/test_docs_line_wrap.py` among them, passed (executed). `trail/phases/phase-1.md` now states round 2's condition and 8e605e8c (0c820872).
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: `CONTRIBUTING.md:449-450` now reads "`lint-python` and
`version-check` are those hooks, and `README.md` *What runs on your
machine* says what each one reaches, what it sends and when" (read). The
sentence that called `uvx` lint-python's only network path is gone. The
crafter wrote its own sentence instead of round 1's snippet, which dropped
both hook names. Its reason holds. Folded *Scope* 6 at
`frame/design.md:138-147` asks for one sentence that names both hooks.
`hooks/version-check.py:23-24` says "`CONTRIBUTING.md` names it as an
allowed exception", and round 1's text would have made that untrue (read).
The #1055 rule sentence, the limits after it and "privacy section" stand.
No sentence counts the hooks.
`tests/behaviour/test_chain_hooks_hardening.py#test_the_hooks_that_reach_the_network_are_named_without_a_count`
passes at HEAD (executed). `git grep` for "fetches ruff", "newest release
tag" and "through `uvx` when" outside this work item finds only the
README's own `uvx` sentence and its hook-table row, which state the
README's facts and are no copy of the removed lines (executed). The `to`
text of the second `## Rule changes` operation, "`CONTRIBUTING.md` names
the hooks that reach the network", is now literally true (read).

What matched: the README half of finding 1 landed as round 1's text in both
editions at `README.md:311-312` and `README.ko.md:314-315`, and the
changelog took the proposed clause (read). Finding 1 above concerns that
text's condition, not whether it was applied.

What matched: the orchestrator's folds state the tree at HEAD. *Grounding*'s
`CONTRIBUTING.md` row, *Data & interfaces*, *Removes* and the new
*Judgments of the run* row in `frame/plan.md` each name the sentences
fea52aea changed (read). `gaps.md` no longer lists `CONTRIBUTING.md:449`,
which fea52aea settled (read).

What matched: the two paragraphs 50cae2cd rewrote in
`trail/phases/phase-1.md`, at lines 29-43 and 131-138, state round 1's two
findings and what fea52aea did, and HEAD contradicts neither (read).

What matched: the six narrow modules pass at HEAD 50cae2cd, 142 tests. They
are `tests/behaviour/test_chain_hooks_hardening.py`,
`tests/behaviour/test_both_editions_carry_the_same_folds.py`,
`tests/behaviour/test_docs_line_wrap.py`,
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/behaviour/test_release_hygiene.py` and
`tests/hooks/test_version_check.py` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD; contract rule 2 keeps them from this round, and the crafter's `unverified` label for them is honest | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| Whether uv's own settings, such as `python-preference = "only-managed"` in a project's `[tool.uv]` or `UV_PYTHON`, make `uv run` download a Python where an installed one fits, and whether the README should say so | `README.md:311-312` | the orchestrator, through the fix pass for finding 1 |
| Whether `CONTRIBUTING.md`'s hook rule widens to every shipped network call; the build took default (a) | `frame/questions.md` Q1 | the owner, through the orchestrator's report |
| Whether the plugin directory's reviewer reads a true README at the next `dist` commit | `frame/design.md` S8 | the owner |

## Probes

| Command | Result |
|---|---|
| `uv run --offline ruff --version`, uv 0.9.18, scratch cache and interpreter directories, in a project with `[tool.ruff]` alone and `.python-version` set to `3.10` | exit 2: "No interpreter found for Python 3.10 in managed installations or search path", hint "A managed Python download is available for Python 3.10, but uv is set to offline mode" |
| The same, in a project with `[project]`, `requires-python = ">=3.9"`, `[tool.ruff]` and `.python-version` set to `3.10` | exit 2, the same error and hint |
| `uvx --offline ruff --version` in the first project | exit 1: ruff not found in the cache; no Python 3.10 asked for |
| `uv python list --only-installed`; `uv python find 3.10` | CPython 3.9.6, 3.11, 3.12, 3.13, 3.14 and 3.15 installed; `find 3.10` exit 2 |
| `bin/test -q` over the six narrow modules named under *Confirmations*, at 50cae2cd | exit 0, 142 passed |
| `git grep -n` for "fetches ruff", "newest release tag", "through .uvx. when", "allowed exception" and "privacy section", outside this work item | the README's `uvx` sentence and hook-table row, `hooks/version-check.py:24`, and two lines of #1102's frame; nothing restates the removed `CONTRIBUTING.md` sentences |
