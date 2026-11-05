# Phase 1: 1793853196-the-readme-names-every-network-place

## What this phase found

**The frame held where it was read.** Before the build, the crafter opened
each coordinate of the census table in `frame/design.md` *Grounding*:
`hooks/version-check.py:129`, `hooks/lint-python.py:77`,
`skills/update/SKILL.md` steps 2 and 3,
`skills/verify/scripts/session_cost.py#run_gh`, `#open_log` and `#post`,
`skills/code-review/scripts/chain_check.py#pull_request_state` and
`#pull_request_from_gh`, `skills/settle/scripts/settle.py#published_releases`,
`#merged_pull_requests` and `#released_local`, `templates/setup/hygiene.yml:66`,
and the row 7 lines in `skills/implement/orchestration.md`, `agents/framer.md`,
`agents/sealer.md`, `skills/code-review/orchestration.md`,
`skills/commit-pr-convention/SKILL.md` and `skills/settle/SKILL.md` (read).
Each says what its row says. The plan's line coordinates for both READMEs
and for the docstring were also right at `3538fd59` (read).

**Row 2 was short, and the hook paragraph changed beyond what *Scope* 1
said.** The census re-run below found that lint-python's first runner is
`uv run ruff --version`, run in the session's directory
(`hooks/lint-python.py#resolve_runner`). In a project whose `pyproject.toml`
has a `[project]` table, `uv run` resolves and installs that project's
dependencies before it runs anything. Two probes in the scratch directory,
with uv 0.9.18, a project depending on `six`, a `[tool.ruff]` table and an
empty `UV_CACHE_DIR`, showed it (executed). With `--offline` the run exited 1:
"Because six was not found in the cache and your project depends on six".
Online it exited 2 after "Installed 1 package", and left `.venv` and
`uv.lock` in the project. The README said lint-python reaches the network
only through `uvx ruff`. *Scope* 1 says the paragraph "stays as it is", but
S1 asks that the census find no place the passage lacks, and
`CONTRIBUTING.md` *House rules*, **Hooks stay local and quiet**, asks that
every hook network touch be named in the README. So both editions gained
one sentence after the pinned one, saying that lint-python first tries
`uv run ruff` and that uv then installs a `[project]`'s dependencies, from
PyPI where its cache lacks them (`b7e392d8`). The pinned sentence and the
rest of the paragraph stand.

**Row 7's marker is `gh pr create`, not `gh`.** *Scope* 3 let the crafter
pick a stronger marker. `gh` stands in the rows for `seal cost --post`,
`seal gate` and `seal settle` too, so deleting row 7 would have left it in
the passage. `gh pr create` stands in row 7 alone, in both editions.

**A marker that stands twice in the passage cannot see its row go.** The
first build (`a617cc44`) ended the passage with a sentence that named
`seal cost --post`, `seal gate` and `seal settle` again, and the Korean row 7
named `seal settle` in passing. Deleting any of those rows would have left
its marker in the passage, and the case green. `8bf96d71` rewrote the
closing sentence to speak of "each row above that goes through your own `gh`
login", and the Korean row 7 to say 정리(settle) without the command. After
it, each of the six markers stands exactly once in each edition's passage
(executed: a count over the passage the case reads). The closing sentence
still scopes the hook sentence the way *Scope* 1 asks.

**The widened case was seen red twice.** Against the READMEs as they stood
at `3538fd59`, with the new case in place, it failed on
`assert place in passage` with `('README.md', '/agentic:update')`
(executed). After `8bf96d71`, `seal mutate` deleted each table row in turn:

- `README.md`, the six rows in one call: 6 mutants, 6 red, 0 SURVIVED
  (executed).
- `README.ko.md`, the six rows in one call: 6 mutants, 6 red, 0 SURVIVED
  (executed).
- `README.ko.md`'s `seal cost --post` row alone, to read the failing line:
  `assert place in passage` with `('README.ko.md', '--post')` (executed).

The tests were
`bin/test tests/behaviour/test_chain_hooks_hardening.py -q -x -p no:xdist -k test_the_hooks_that_reach_the_network_are_named_without_a_count`.
The tree was clean after each run.

**The passage reader stops at the next heading.** `network_passage` finds
the pinned sentence across line breaks with a whitespace-tolerant pattern
and cuts at the first `\n#` after it, which is `## Commands` in English and
`## 명령` in Korean. The red run's output shows the passage ending at "when
the network is unavailable.", before the commands table that also names
`/agentic:update` and `seal settle`.

**The docstring stays on its three lines.** `hooks/version-check.py` lines
23 to 25 now say the hook "is one of the network touches `README.md` *What
runs on your machine* lists". The rewrap kept the change on those three
lines, because #238 works in the same area. The module still imports
(executed: `tests/hooks/test_version_check.py` passed).

**S7.** `git grep -n "second network touch" -- ':!seal/'` at `b7e392d8`
found nothing, exit 1 (executed).

**S1, the census re-run.** `git archive` of HEAD at `b7e392d8` was
extracted under the scratch directory: 171 files (executed). Two parts were
re-run.

- Every process a shipped Python file starts, and every network library it
  imports, over `hooks/`, `skills/` and `bin/`. No file imports `urllib`,
  `http.client`, `socket` or `requests`. Twenty-one files start processes.
  A search for the argv words `gh`, `curl`, `wget`, `uvx`, `uv`,
  `ls-remote`, `fetch`, `push`, `pull`, `clone` and `remote`, and for the
  `GH` constants, found `hooks/version-check.py:129`, `hooks/lint-python.py`
  (`uv run` and `uvx`), `session_cost.py#run_gh`, `chain_check.py#GH_DRAFT`,
  `settle.py#GH`, and `pact_check.py:311`'s `git remote get-url`, which reads
  a local config (executed). This part lists the whole class for these
  directories, as the design's first part does.
- Every command an agent or a person runs from shipped markdown, over
  `skills/`, `agents/`, `templates/`, `hooks/`, `bin/` and `.claude-plugin/`,
  by a search for `gh <verb>`, `git push|fetch|pull|clone|ls-remote`,
  `curl`, `wget`, `uvx`, `WebFetch` and `claude plugin` (executed), and then
  each less common hit read in place (read). Every hit falls in rows 1 to 8,
  or in the design's *What the census left out*, or is a comment or prose
  that names a command without running it, such as `broad_gate.py:474`'s
  `git fetch` and `skills/code-review/orchestration.md:347`'s `gh pr edit`.
  **This part is a sample of spellings**, as the design says of its own:
  a step written only in prose is found by reading, and the part this
  search did not reach would be the workflow's steps against the user's
  repository, which row 7 already covers.

The only place the passage lacked was the `uv run` touch above.

**Left as it stands, and why.** `CONTRIBUTING.md:449` says "`lint-python`
fetches ruff through `uvx` when no local copy exists". It is still true, and
it no longer names lint-python's whole network reach. The frame keeps
`CONTRIBUTING.md` out of this work (*Scope*, Out), so the hand-back names
it. `tests/hooks/test_version_check.py:1` calls version-check "the one hook
that reaches the network", which the README contradicts. #238 edits that
file's docstring on another branch, so the hand-back names it too.
