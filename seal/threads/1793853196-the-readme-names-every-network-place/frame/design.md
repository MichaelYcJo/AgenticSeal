# Design: the README names every network place (#1382)

## Grounding

Every line coordinate and every present-tense statement of the tree in this
section was read at commit `d7f4d9bf` (`routing: declare #1382 under
automation`, on `release/v0.32.4` cut from `31558c76`, v0.32.3). A crafter
reading a later HEAD reads them as of that commit.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has one source, and every other place links to it" and "in the same commit removes what stood on the old fact" | The README is the one place that lists where the plugin reaches the network, because the owner's directory answer points there. Two shipped sentences state the old, shorter list: `hooks/version-check.py`'s module docstring calls version-check "the plugin's second network touch", and `docs/running/measuring-a-run.md` *Where a reading goes* says `--post` writes only when a person types it. Both are corrected in this work (*Scope* 4 and `## Rule changes`), as contract rule 19 asks. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | This work item's subject is the two README editions, not the policy root. So the one policy paragraph this work makes untrue, in `docs/running/measuring-a-run.md`, changes through `## Rule changes` for the settle, and the crafter does not edit `docs/` directly. `docs/README.md` indexes that file under `docs/running/`. |
| `CONTRIBUTING.md` *House rules*, the bullet **Hooks stay local and quiet**, "Every hook that reaches the network is named in the README's privacy section" | The rule covers hooks only, and its conditions (an opt-in, a throttle, silence on failure) are shaped for a hook. lint-python and version-check stay named, so the rule stays true. The new rows are commands and workflow steps, which the rule does not reach, and `docs/running/measuring-a-run.md` *Where a reading goes* gives that reason for `--post`. This work leaves `CONTRIBUTING.md` alone (`plan.md` *Alternatives considered*, row 5). |
| `CONTRIBUTING.md` *House rules*, "Both READMEs move together" | `README.md` and `README.ko.md` change in the same commit. They tell the same story and keep the same sequence of heading levels (`tests/behaviour/test_both_editions_carry_the_same_folds.py`). |
| Prior decision #1102, `seal/threads/1793732301-the-readme-is-written-for-a-first-reader/frame/design.md` *Scope* item 2 | The README keeps a fact only where no other shipped file states it or the issue requires it, and "the hooks that reach the network" is named as one it keeps. This work follows that decision: the network list stays on the page as one passage, and a row may link the shipped file that holds its detail rather than restate it. |
| Prior decision #1055 S4, `tests/behaviour/test_chain_hooks_hardening.py#test_the_hooks_that_reach_the_network_are_named_without_a_count` | Both editions and `CONTRIBUTING.md` name the network places without counting them. The new text states no count, such as "four places" or "two hooks". The pinned sentences "lint-python and version-check reach the network." and "네트워크를 타는 훅은 lint-python 과 version-check 입니다." stay verbatim. |
| Prior decision #1374, `seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/design.md` *Scope* item 1, and `.gitattributes` | The issue's *Done when* reads "the files `dist` holds", which is `git archive` of the tree with the `export-ignore` lines of `.gitattributes`: `/tests/`, `/evals/`, `/seal/`, `/.test_durations`, `/CLAUDE.md` and `/.github/workflows/` leave. `.github/scripts/` stays in `dist`. |
| `tests/behaviour/test_chain_hooks_hardening.py#GATE_TABLE` and `#gate_table_names` (lines 68 to 83) | The hook table is found by the line opening `\| Gate \|` (`\| 게이트 \|` in Korean), and its rows run to the first line that is not a table row. A new table must not open with that header and must not follow the hook table without a blank line between them. |
| `tests/behaviour/test_docs_line_wrap.py#LIMIT` | Prose lines in both editions stay within 88 display columns. Table rows are not prose. |
| `skills/settle/scripts/passages.py#TOP_FILES`, read by `tests/text/test_no_passage_is_pasted_into_a_second_file.py` | `README.md` is in the paste corpus. The new English text shares no 15-word run with a file under `docs/`, `skills/`, `agents/` or `templates/`, or with `CONTRIBUTING.md`. A row states its fact in fresh words or links the file that holds it. |
| `tests/behaviour/test_release_hygiene.py::test_no_loaded_file_names_a_version_at_or_above_the_running_one` | Neither edition names a release number. The `/agentic:update` row names the releases list and no version. |
| `docs/running/measuring-a-run.md` *Where a reading goes* and `skills/verify/orchestration.md` *Measure the segment, and feed the flow log* | After every crafter or proofer segment, the orchestrator runs `seal cost --segments ... --post` without asking. It posts only where an issue of the repository has ever carried the `flow-measurement` label. Most installed repositories never create that label, and then nothing is posted. The issue's table says `seal cost --post` runs "only when the user types it", which these two documents contradict. The README states the documents' account. |
| `routing.md` | Read: framer, crafter, the review chain, open the pull request, `Automation` `yes`, answered 2026-11-05. |
| The issue, #1382 | Read by `gh issue view 1382 --json body,comments` on 2026-11-05: the body as quoted in the spawn prompt, and no comments. That matches the orchestrator's line. |

### The census of every place the files `dist` holds reach the network

**How the list was made.** `git archive HEAD` at `d7f4d9bf` was extracted
under the scratch directory: 171 files (executed). The list was then built
from what produces a network call, in three parts.

- **Every process a shipped Python file starts, and every network library it
  imports.** `grep` for `subprocess` calls and for `urllib`, `http.client`,
  `socket` and `requests` over `hooks/`, `skills/`, `bin/`, then the argv
  head of each call, listed file by file (executed). Every call outside the
  rows below runs a local `git` verb (`rev-parse`, `ls-files`, `ls-tree`,
  `show`, `merge-base`, `rev-list`, `cat-file`, `add`, `rm`, `diff`,
  `worktree remove`, `remote get-url`), `pytest`, or the plugin's own
  scripts. This part lists the whole class for these directories.
- **Every command an agent or a person runs from shipped markdown.** A `grep`
  over `skills/`, `agents/`, `templates/`, `hooks/`, `bin/` and
  `.claude-plugin/` for `gh <verb>`, `git push`, `git fetch`, `git pull`,
  `git clone`, `git ls-remote`, `curl`, `wget`, `uvx` and `WebFetch`
  (executed), and then the prose around each hit (read). **This part is a
  sample of spellings.** An instruction written in prose, such as "push the
  branch" at `skills/code-review/orchestration.md:251`, is found only by
  reading. The rows it did not reach would be workflow steps against the
  user's own repository, which row 7 already covers.
- **Templates the plugin writes that run somewhere else.** All files under
  `templates/setup/` (read).

| # | Place | Reaches | What is sent | When | In the README at `d7f4d9bf` | Label |
|---|---|---|---|---|---|---|
| 1 | version-check hook, `hooks/version-check.py:129` | GitHub | one `git ls-remote --tags` against the plugin's own repository | at session start, once a day, where `seal/` exists | yes | read |
| 2 | lint-python hook, `hooks/lint-python.py:77` | PyPI, and GitHub for a managed Python | `uv run ruff --version`, the first runner, installs the project's dependencies where `pyproject.toml` has a `[project]` table, and downloads a Python build from GitHub where no installed interpreter satisfies `requires-python`; uv fetches ruff on first use when the hook falls back to `uvx ruff` | after a `.py` edit, in a project that configures ruff | yes | read |
| 3 | `/agentic:update`, `skills/update/SKILL.md` *Procedure* steps 2 and 3 | GitHub | `claude plugin marketplace update` pulls the marketplace clone and `claude plugin update` installs from it. Then one `curl` with no token to `https://api.github.com/repos/<repo>/releases?per_page=100`, where `<repo>` is the marketplace clone's `origin` | when the user runs the command | no | read |
| 4 | `seal cost --post`, `skills/verify/scripts/session_cost.py#run_gh`, `#open_log`, `#post` | GitHub, through the user's `gh` login | `gh issue list --label flow-measurement --state all`, then `gh issue comment` on the one open issue carrying that label. The body is the orchestrator's sentence and the segment's reading. The transcript is named by its file name and never by its path (`#emit` docstring). It never opens an issue | after every crafter or proofer segment, run by the orchestrator, and by a person who types it. Nothing is posted where no issue of the repository has ever carried the label, or where `gh` is missing | no | read |
| 5 | `seal gate`'s chain arm, and `chain_check.py` run outside GitHub Actions, `skills/code-review/scripts/chain_check.py#pull_request_from_gh` | GitHub, through the user's `gh` | `gh pr view --json isDraft`, run in the repository | each run where `GITHUB_EVENT_PATH` names no file and `gh` is on the PATH. `skills/verify/scripts/broad_gate.py` docstring item 2 runs this check as its second arm | no | executed: in a `git clone --no-local` of this branch, `chain_check.py --baseline HEAD~1` was run with a `gh` on the PATH that logs its arguments and with `GITHUB_EVENT_PATH` unset. Exit 0, and the log held `gh pr view --json isDraft` |
| 6 | `seal settle`, `skills/settle/scripts/settle.py#published_releases` and `#merged_pull_requests` | GitHub, through the user's `gh` | `gh api --paginate` of the repository's releases. In local mode only, `gh pr list --head <branch> --state merged` once per branch | where a released work item's directory holds a changelog and is about to be removed, for its release note. In local mode, to tell which branches merged | no | read for the code. Executed: the dry run at this tree, with the logging `gh`, made no call. The call depends on the condition |
| 7 | the workflow's own steps, run by the session through the user's `git` and `gh` | the user's repository on GitHub | reads the issue and its comments (`skills/implement/orchestration.md:78`, `agents/framer.md:74`, `agents/sealer.md:75`) and the latest release note (`agents/framer.md`). Pushes the work item's branch, opens the pull request with `gh pr create --body-file` and updates its body with `gh api -X PATCH`, reads its state and checks, and can start a workflow run (`skills/code-review/orchestration.md:251` to `:346`). Lists recent pull requests before a commit (`skills/commit-pr-convention/SKILL.md:30`). At a settle, may open an issue for a measurement (`skills/settle/SKILL.md:234`) | reading the issue happens in every run. Pushing and the pull request happen where `routing.md` answers `Destination` with `open the pull request` | no | read |
| 8 | the pull-request checks `seal pr-checks install` writes, `templates/setup/hygiene.yml` | GitHub, from the user's CI runner | `git clone --depth 1 --branch v<version>` of `https://github.com/MichaelYcJo/AgenticSeal.git` | on each pull request, in a repository that installed the checks | no | read |

**What the census left out, and why.**

- **The network calls in `.github/scripts/`** (`publish_release_note.py`,
  `release_seal.py`, `close_issues_on_release.py`, `tag_release.py`,
  `release_completeness_check.py`, `label_merged_on_release_branch.py`,
  `roll_flow_measurement_issue.py`, `tracker_labels.py`, `dist_branch.py`,
  and `plugin_directory_check.py` through `urllib`). This repository's own
  workflows run them, and `dist` does not hold those workflows. Shipped
  code imports only functions that start no process from that directory:
  `skills/code-review/scripts/pr_body.py` imports
  `close_issues_on_release.py#keywords_in`, and `chain_check.py`, `seal.py`
  and `rule_changes.py` read `rules.py` (read).
- **`bin/test`.** `.github/scripts/run_tests.py#main` (lines 564 to 574)
  exits 2 before it installs anything where no `tests/` stands beside it,
  and `dist` holds none. `repo_root` is the plugin's own directory, not the
  user's (read).
- **The command in `seal/config.md`'s `Broad gate` row**, such as this
  repository's `uvx ruff check .`. It is the user's own command, and
  `seal gate` runs it as written.
- **`git clone --no-local`** in `agents/framer.md`, `agents/proofer.md` and
  `skills/code-review/orchestration.md`. It copies a local repository.
- **`/plugin marketplace add` and `/plugin install`** under `## Install`.
  Claude Code runs them, and the README already shows them.

## Scope

In:

1. **`README.md` *What runs on your machine* names every place of the census
   table, rows 1 to 8, each with what it reaches, what is sent and when.**
   The paragraph opening "lint-python and version-check reach the network."
   keeps its pinned first sentence and holds rows 1 and 2; it gains one
   sentence on lint-python's first runner, `uv run`, which installs the
   project's dependencies where `pyproject.toml` has a `[project]` table
   (phase 1 found it; `trail/phases/phase-1.md`), and which downloads a
   Python build from GitHub where no interpreter on the machine satisfies
   the project's `requires-python` (round 1 found it;
   `trail/rounds/round-1.md` finding 1).
   A lead sentence and a table follow it for rows 3 to 8, with one row per
   place and four columns: what, where it reaches, what it sends, and when.
   The table's header does not open with `| Gate |`. A blank line or a
   paragraph stands between the hook table and every later table. The
   passage closes with a sentence that scopes the earlier "No hook sends
   your code, your paths or your prompts anywhere": rows 4 to 7 go through
   the user's own `gh` login to the repository the user works in, and the
   workflow's steps push the branch and the pull request's text there,
   because that is what they are for. No sentence counts the places. Each
   row may link the shipped file that holds its detail.
2. **`README.ko.md` says the same in Korean**, under `## 문장 규칙` of
   `skills/writing-style/SKILL.md`. The paragraph opening "네트워크를 타는
   훅은 lint-python 과 version-check 입니다." stays, the table has Korean
   headers whose first cell is not `게이트`, and the sequence of heading
   levels is unchanged.
3. **`tests/behaviour/test_chain_hooks_hardening.py#test_the_hooks_that_reach_the_network_are_named_without_a_count`
   also asserts that each edition's network passage names rows 3 to 8.**
   The passage is read from the pinned hooks sentence to the next heading,
   and not over the whole file, since the commands table elsewhere names
   `/agentic:update` and `seal settle` too. The case looks for one name per
   row: `/agentic:update`, `--post`, `seal gate`, `seal settle`, `gh pr create`
   for row 7, and `seal pr-checks install`. The crafter may pick a stronger
   marker for row 7 and names it in the phase record. The case's
   assertions against a count stay, and its docstring says what it now
   holds. It is seen red by deleting one row from one edition.
4. **`hooks/version-check.py`'s module docstring** stops calling the hook
   "the plugin's second network touch, after lint-python's `uvx ruff`
   fetch". It says the hook is one of the network touches that `README.md`
   *What runs on your machine* lists, and keeps "`CONTRIBUTING.md` names it
   as an allowed exception" and the three limits that follow. Only the
   docstring changes, and the code does not. The first line of
   `tests/hooks/test_version_check.py`'s module docstring, "version-check —
   the one hook that reaches the network", states the same old fact and
   is corrected the same way; that line is the only one of the module
   this work touches, since #238 rewrites another paragraph of it.
5. **The rule changes below**, for the settle.
6. **`CONTRIBUTING.md` *House rules*, the bullet *Hooks stay local and
   quiet*.** The two sentences that say what each hook reaches,
   "`lint-python` fetches ruff through `uvx` when no local copy exists."
   and "`version-check` asks the plugin's own repository for its newest
   release tag.", become one sentence that names both hooks and points to
   `README.md` *What runs on your machine* for what each reaches and sends.
   The first of them states the old fact the README now corrects (round 1
   finding 2). The rule sentence #1055 pins, the limits that follow it,
   the words "privacy section" and the rule's reach (Q1, default (a)) stay
   as they read.

Out:

- **`CONTRIBUTING.md`'s hook rule widened to every shipped network call.**
  The issue says "Nothing else changes", and the rule stays true as it
  reads. `frame/questions.md` Q1 asks the owner, and the build goes ahead
  on the default, which leaves the rule alone.
- **The word "privacy section" in `CONTRIBUTING.md`**, which names no
  heading of either README. That sentence is unchanged and still true in
  substance, and the issue does not ask for the edit. The orchestrator's
  report names it as a leftover.
- **A check that compares the README's list against the code's network
  calls.** It would decide on spellings in prose, which
  `skills/core/SKILL.md` *The rule a mechanism is kept against* rules out
  for a script that blocks. `plan.md` *Alternatives considered*, row 4.
- **Submitting `@dist` again, and answering the directory.** The directory
  picks up the next release's `dist` commit. These are the owner's acts.
- **The `.github/scripts/` network calls and `bin/test`**, for the reasons
  under *What the census left out*.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 Every place is named | Given the census table's rows 1 to 8, when a reader reads each edition's network passage, then every row has a sentence or a table row that says what reaches where, what is sent, and when | The widened case of *Scope* 3 for the names, seen red by deleting one row. Read at review for each cell against the census table. Executed by the crafter: the census re-run over `git archive HEAD` of the build commit, its method and output in the phase record, finding no place the passage lacks |
| S2 The `--post` row tells the truth about when | Given `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, when the `--post` row is read, then it says the orchestrator runs it after each crafter or proofer segment, that a person may run it, and that nothing is posted where no issue has ever carried `flow-measurement` | Read at review |
| S3 No count | Given both editions and `CONTRIBUTING.md`, when the case reads them, then no sentence counts the places and the pinned hook sentences stand | `tests/behaviour/test_chain_hooks_hardening.py#test_the_hooks_that_reach_the_network_are_named_without_a_count` |
| S4 The hook table is still one row per registered hook | Given the new table after the hook table, when `gate_table_names` reads each edition, then it returns the registered hooks and nothing from the new table | `tests/behaviour/test_chain_hooks_hardening.py#test_the_gate_table_has_one_row_for_each_script_groups_registers` |
| S5 One structure | Given both editions, when their heading levels are read in order, then the two sequences are equal | `tests/behaviour/test_both_editions_carry_the_same_folds.py` |
| S6 Prose wraps and nothing is pasted | Given the new text, when the line-wrap and paste checks read it, then every prose line is within 88 columns and no 15-word run is shared | `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py` |
| S7 No ordinal is left | Given the build commit, when `git grep -n "second network touch"` runs over the tree outside `seal/`, then it finds nothing | Executed by the crafter, in the phase record |
| S8 The directory reads a true README | After the release, the directory's reviewer reads the README at the next `dist` commit and finds each place the plugin reaches the network | The owner's reading. The run does not wait on it |

## Data & interfaces

- `README.md` *What runs on your machine* and `README.ko.md` *내 컴퓨터에서
  도는 것*: the network passage in each grows by one sentence in the hook
  paragraph, a lead sentence, one table of six rows and a closing sentence. No heading is added, moved or renamed.
- `tests/behaviour/test_chain_hooks_hardening.py`: one case gains
  assertions (*Scope* 3). No new module or fixture is added.
- `hooks/version-check.py`: the module docstring changes. No code changes.
- No interface, schema, command or exit code changes.

## Rule changes

- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: A network write only a person's typing starts is not a hook, and the
    list of hook network touches does not reach it.
  to: A network write a person or a session starts is not a hook, and the
    list of hook network touches does not reach it.
- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: `CONTRIBUTING.md` counts the plugin's network touches under *Hooks
    stay local and quiet*,
  to: `CONTRIBUTING.md` names the hooks that reach the network under *Hooks
    stay local and quiet*,
- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: `--post` fires on no hook and writes only when typed, only through
    `gh`, and only what it was handed.
  to: `--post` fires on no hook, and writes only when a person or a session
    runs it, only through `gh`, and only what it was handed.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sentence that calls version-check "the plugin's second network touch, after lint-python's `uvx ruff` fetch" | `hooks/version-check.py`, module docstring | `README.md` *What runs on your machine* lists every place (*Scope* 1). The docstring points there (*Scope* 4) |
| The claims that `--post` writes only when a person types it, and that `CONTRIBUTING.md` counts the plugin's network touches | `docs/running/measuring-a-run.md` *Where a reading goes* | The three operations of `## Rule changes`, for the settle |

This work adds no mechanism. *Scope* 3 adds assertions to a case that
already pins this passage, and it adds no gate, hook, CI step, rule, label
or mark. So nothing else is taken out in return.

Framed 2026-11-05 by framer, before the build.
