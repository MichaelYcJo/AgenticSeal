# Phase 1: 1793599987-a-script-reads-git-the-same-under-any-config

## What this phase found

**The frame holds, with one drawing error.** `frame/plan.md` *Technical
context* lists `close_issues_on_release.py#run` among the wrappers that
serve a `log` call, and `frame/design.md` *Scope* item 2 says such a
wrapper builds every call it serves with `gitcmd.argv`. `run` is no git
wrapper: it runs `gh` as well, and `argv` would prefix a `gh` call with
`git -c`. So the two `git log` calls in `close_issues_on_release.py#arrived`
are built by `argv` at the call, and `run` stays as it was.
`release_completeness_check.py#subjects_since` reaches the helper as
`closer.gitcmd`, through the module it already reaches `run` through.
Judged against `frame/design.md` *Scope* item 2, whose criterion is the
command's output, not the wrapper's name. Every other wrapper and inline
call the plan names stands where it says (read), and every `show` call in
the shipped scripts is `show <rev>:<path>`, which no measured key changes
(read).

**The `## Rule changes` block parses.** `rule_changes.py#parse` over
`frame/design.md` with policy root `docs` gives one `add` to
`docs/what-a-script-gates.md` *Which gate a script holds*, errors `[]` and
unread `[]` (executed). The section stands at line 10 of that file (read).

**How each script loads the helper**, each the way that script already
loads `hooks/lib/`, as `frame/design.md` *Data & interfaces* asks:

- `chain_check.py` loads it at import, in the `try` that loads `FIELDS`,
  so a check run as a command that cannot load it exits 2 with the reason.
- `settle.py` loads it through its own `load` at each wrapper call, with a
  `PURPOSES` sentence. A load at import would make a copy of the script
  taken alone stop at the helper before `OPTIN`, and
  `tests/skills/test_settle.py#Test_module::test_a_script_copied_alone_exits_2_and_names_what_it_misses`
  holds that the copy names `OPTIN`'s purpose.
- `broad_gate.py` loads it through its own `load` inside `git`, with the
  path written there, so the edit stays inside the wrapper (#883 edits the
  file in parallel) and a copy beside a broken `seal_stamp.py` still
  refuses through `STAMP` first, as
  `tests/skills/test_broad_gate.py` *test_refuses_a_copy_whose_sibling_will_not_load* holds.
- `seal_stamp.py` loads it by path in `_gitcmd`, the shape of its
  `_chain_check`; `rule_changes.py` loads it once in `gitcmd()`, the shape
  of its `config()`.
- `seal.py` names it in `HOOK_PURPOSES` and imports it; `publish_release_note.py`
  and `close_issues_on_release.py` import it from the `hooks/lib` entry on
  `sys.path`, which `close_issues_on_release.py` gains here.

**Two refusal sentences are new, and each is pinned.** `settle.py` and
`seal.py` now name `hooks/lib/gitcmd.py` and its purpose where it is
missing. A row for it joins
`tests/skills/test_settle.py#Test_module::test_each_sibling_is_refused_with_its_own_purpose`
and
`tests/skills/test_seal.py#Test_refuse_without_hooks::test_a_script_copied_alone_exits_2_and_names_what_it_misses`
(contract rule 14). Each was seen red by `seal mutate` deleting that
script's purpose entry: the settle row failed at `assert phrase in ...err`,
and the seal row at `assert purpose in done.stderr` (executed).

**A line a person reads grew, and it is not pinned.** Where a `git` call
fails, `publish_release_note.py#run` and `close_issues_on_release.py#run`
print the argv they ran, which now opens with the five `-c` pairs. The
words around it are unchanged, the argv is printed as it ran, and no case
pinned the line before. Judged against contract rule 14: the line's text
is the command, not a message the change wrote.

**Files the frame did not name had to change**, each because it stood on
the argv the scripts built before:

- `evals/scripts/replay_targets.py#CHECK_FILES` lists what a commit's
  `chain_check.py` loads at import, and now names `hooks/lib/gitcmd.py`.
  Without it, three cases of `tests/evals/test_replay_targets.py#Test_module`
  failed in the phase-boundary run, each at a copied check that would not
  load the helper (executed); with it, the module passes (executed).
- `tests/skills/test_chain_check.py#copied_tree` copies the files the check
  loads at import, and now copies `gitcmd.py`.
- The stubs `tests/github/test_publish_release_note.py#Releases.run` and
  `tests/github/test_release_completeness_check.py#Tracker.run`, and one
  filter in the second module, matched `args[:2] == ("git", "log")`. They
  now match a `git` argv holding `log`. 40 cases of the two modules failed
  at these stubs on the first narrow run and pass after (executed). A 41st,
  the census of `release_completeness_check.py`, failed where the
  formatter moved `.splitlines()` off the line under its exemption, and
  passes since the call reads its output first. The stubs of
  `test_close_issues_on_release.py`, `test_broad_gate.py` and
  `test_seal.py` needed nothing.

**The removals are the frame's `## Removes` and nothing else.** The five
flags at `settle.py`'s three readers, the four sentences, and the three
cases went. `Test_adding_commit` keeps one accepts case, renamed
`test_accepts_the_oldest_add_of_each_path`, with no key set.

**The helper's cases read the key, not the reader.**
`tests/hooks/test_gitcmd.py` builds, per key, a repository where the key
set otherwise changes one command's output, and names that output under
git's default. `Test_argv::test_accepts_...` holds that `argv` prints it
where nobody sets the key. `Test_argv::test_refuses_...` sets the key in
`GIT_CONFIG_COUNT` and in the repository's own config, and holds that the
bare command prints something else, so a fixture that stopped showing the
key's effect fails, and that `argv` still prints git's default.
`Test_module::test_every_key_has_a_case` holds `KEYS` and the parameters
to one list. The signed-commit parameter ran here and did not skip
(executed).

**Mutation, with `bin/seal mutate` from this worktree (executed).** #898 has
not landed, so each red below was read at the line it failed on before it
was counted.

| Mutant | Cases | Result |
|---|---|---|
| each key's line deleted from `KEYS`, five runs | `-k 'refuses and <key>'` | red, both `where` parameters failing at `assert printed(gitcmd.argv(...)) == expected.encode()` |
| each key's value set to the person's value, five runs | `-k 'accepts and <key>'` | red, one failure each at the same assertion |
| `settle.py#adding_commit` put back to `("git", "-C", root, "log", ...)` | `tests/skills/test_settle.py -k adding_commit` | survived |

Each deletion mutant was also written to a scratch copy and imported, and
each loaded with its key absent from `argv()`; a value mutant changes one
string literal. The survivor is the frame's accepted miss: no case pins a
call site (`frame/plan.md` *Alternatives considered*, rows 6 and 7), and the
proofer reads the rule at review.

**The call sites were listed by a search, which is a sample of its class.**
`git grep` for the string literals `"log"` and `"status"` in the `.py`
files under `hooks/`, `skills/` and `.github/scripts/` listed 15 calls,
and each is now built by `argv` (executed). A subcommand passed in a
variable would not be listed; the framer's `ast` walk of 60 calls is the
whole list the frame stands on.

**Checks run at the boundary (executed).** `ruff check` and `ruff format
--check` over every changed `.py` passed. `seal layout --check tests`
exited 0 with no refusal; it reports `rule_changes.py: function gitcmd has
no class Test_gitcmd`, as it reports `config`, `reader` and `passages`.
`seal layout --pairs` over the three changed test modules names one pair,
in `tests/skills/test_seal.py#Test_pinned`, which this phase did not touch.

**For phase 2.** `settle.py#earlier_judgments` already reads with `-z`.
The readers *Scope* item 4 names still split on newlines. The docstring of
`hooks/lib/gitcmd.py` cites `docs/what-a-script-gates.md` *Which gate a
script holds*, which holds the rule only once the settle writes this
design's `## Rule changes`.
