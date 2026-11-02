# Implementation Plan: a script reads git the same under any config (#1283)

## Technical context

The code this builds on, at `5dc1f37e`:

- Each script writes its own argv. The wrappers are
  `skills/settle/scripts/settle.py#git_out` (`:476`) and `#git_fields`
  (`:1384`), `skills/code-review/scripts/chain_check.py#git` (`:318`),
  `skills/verify/scripts/seal_stamp.py#_git` (`:1075`),
  `skills/verify/scripts/test_layout.py#_git` (`:1043`),
  `skills/verify/scripts/pact_check.py#git` (`:285`),
  `skills/verify/scripts/broad_gate.py#git` (`:233`),
  `skills/implement/scripts/seal.py#git_asked` (`:280`) and `#git`
  (`:323`), `.github/scripts/publish_release_note.py#git` (`:188`),
  `.github/scripts/tag_release.py#git` (`:114`),
  `hooks/routing-edit-gate.py#git` (`:147`) and
  `hooks/review-skill-gate.py#git` (`:77`). `close_issues_on_release.py#run`
  and `release_completeness_check.py`, through `closer.run`, take `"git"` as
  their first argument. Every other call is an inline `subprocess.run`. The
  `ast` walk in `frame/design.md` *Grounding* lists all 60 by file and line.
  Of these wrappers, those that serve a `log` or `status` call are
  `settle.py#git_out` and `#git_fields`, `chain_check.py#git`,
  `seal_stamp.py#_git`, `broad_gate.py#git`, `publish_release_note.py#git`
  and `close_issues_on_release.py#run`. The inline ones are
  `settle.py#adding_commit`, `rule_changes.py#order`, `seal.py`'s status at
  `:1727`, `publish_release_note.py:425` and
  `release_completeness_check.py:144`. Those are what Scope item 2 changes.
- How each caller reaches `hooks/lib/`. A hook puts `hooks/lib` on
  `sys.path` and imports, as `hooks/routing-edit-gate.py:51` does. A skill
  script loads a module by path with `importlib.util`, as
  `skills/verify/scripts/unverified_check.py#_load_hook` (`:86`) and
  `skills/settle/scripts/settle.py`'s `OPTIN` (`:184`) do.
  `.github/scripts/publish_release_note.py:121` already puts `hooks/lib` on
  `sys.path`. `.github/scripts/close_issues_on_release.py` loads nothing
  from `hooks/lib` today.
- Test stubs that read git's argv by its first word change with it. Among
  the modules of the files Scope item 2 touches, `git grep` over `tests/`
  finds `tests/github/test_close_issues_on_release.py`,
  `tests/github/test_publish_release_note.py`,
  `tests/skills/test_broad_gate.py` and `tests/skills/test_seal.py`
  patching `subprocess` or a `run` (a sample, not a whole list). A phase
  finds the rest when its narrow run goes red.
- `seal layout --check tests` refuses a `Test_<function>` class with no
  `test_accepts_` case or no `test_refuses_` case. So
  `tests/skills/test_settle.py#Test_adding_commit` keeps its accepts case
  when its parametrization goes (`frame/design.md` *Removes*).
- `tests/conftest.py:338` sets `GIT_CONFIG_COUNT=1` for the whole suite.
  A case that sets a key monkeypatches the three variables, as
  `tests/skills/test_settle.py:3125` does, and `-c` outranks them
  (executed). The ssh-signed commit fixture is in
  `tests/skills/test_settle.py#Test_main::test_a_signed_removal_is_read_under_any_show_signature`
  (`:1497`), which this work removes. It skips where `ssh-keygen` is
  absent or makes no key, and the helper's case reuses that shape.
- Sibling items of the milestone `release: 0.28.1` (read). #898: until it
  lands, `seal mutate` reads a mutant that does not compile as caught. So a
  mutation offered as seen red in this run names the assertion it failed
  at, as #1139's phase records did. #1299 edits
  `publish_release_note.py#sealed_header` and its header helpers in
  parallel. This item's edits in that file stay inside `git`, `fragments`,
  the `log -1 --format=%B` call and one import beside `import console`.
  #883 edits `broad_gate.py`, and #1270, still being framed, may touch
  `chain_check.py` (the orchestrator's frame read, read). In each of those
  two files this item changes the wrapper `git` and the line that loads
  the helper, and nothing else.

The failure scenario of the chosen approach, six months on. git adds a key,
or someone finds one this frame did not read, that reshapes `log` output.
Every reader goes wrong at once until the key is measured, and then one line
in `hooks/lib/gitcmd.py#argv` fixes all of them. A second scenario: a new
`git log` is written by hand in a script. No case catches it, and the
proofer reads it against the rule at review. Where the proofer misses it,
the reader is exposed to the five keys until someone meets the failure, as
#1054, #1139 and #1281 did. The rule names that reader so the miss is a
finding against a named party.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the per-reader flags (`--no-show-signature`, `--root`, `--no-follow`) and add them at each reader that lacks them, as #1054, #1139 and #1281 did | The next key means another visit to every reader. A reader written next month gets no flags unless its builder knows the list: three builders wrote three readers without it before 2026-11-02. Each site also needs its own judgment of which key matters. #1139 judged `--no-show-signature` unneeded at `adding_commit`, which was right there and has to be judged again everywhere else | rejected: the structure is what produced the class |
| Drop the person's config in a helper, with `GIT_CONFIG_GLOBAL=/dev/null` and `GIT_CONFIG_NOSYSTEM=1` | The repository's own `.git/config` still applies: a repository-level `log.showSignature=true` changed the output (executed). And the helper would drop `safe.directory`, which a container job or a shared machine sets globally, so git would refuse the repository. On Windows it would also drop git's own system settings, such as `core.longpaths` (read) | rejected |
| One helper that sets each measured key with `-c`, and every `log` and `status` call built by it | A key nobody has measured is not set, and a hand-written `log` is caught only at review (above) | chosen |
| The helper also sets `core.quotePath=false`, in place of `-z` at each reader of paths | A name that holds a newline, a tab, a quote or a backslash is still quoted (measured in the comment of `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` above its `ls-files`), and a reader split on newlines still splits such a name | rejected: `-z` at each reader of paths, as `settle.py` reads every other listing (#1281) |
| All 60 git calls in 23 files built by the helper, hooks and `rev-parse` callers included, so that a pin needs no exemption (the framer's first frame) | Every hook that fires in a session, and every script that calls only `rev-parse`, `merge-base` or `tag`, is edited for a call no measured key changes (executed and read, `frame/design.md` *Data & interfaces*). Each edit adds review load and changes no reading. The sweep also collides with #883 on `broad_gate.py`, with #1299 on `publish_release_note.py` and `release_seal.py`, and possibly with #1270 on `chain_check.py`. Each collision costs a merge and a verifying round on the resolution (`skills/code-review/orchestration.md` *A conflict with the base is integrated by merging the base into the branch*) | rejected after the orchestrator's frame read, proposal 1: the helper builds the `log` and `status` calls, and its docstring names those subcommands |
| An `ast` pin keyed on subcommand: any argv headed `"git"` whose subcommand the helper's docstring names must be built by `argv` (the orchestrator's frame read, proposal 2, first option) | Most of these calls name their subcommand at a wrapper's caller, `git_out(root, "log", ...)`, `git(root, "log", ...)` or `_git(top, "log", ...)`. The argv display the wrapper builds is `["git", "-C", root, *args]` and holds no subcommand, so the pin would have to work out which function builds which argv, across modules too: `release_completeness_check.py` calls `close_issues_on_release.py#run`. Reading the callers' literals instead refuses honest code, because `"log"` and `"status"` are ordinary words in calls such as `.get("status")`. Either reader is a judgment a test would encode | rejected: the call-site rule is read by the proofer at review, as its `check: none reader:` line says, and `tests/hooks/test_gitcmd.py` holds each key |
| No pin case: the helper, the rule sentence and the proofer | A new `git log` written by hand passes unless the proofer reads it against the rule. The catch record is three such readers written in one day, before the rule or the helper existed | chosen, with the orchestrator's frame read, proposal 2, second option: the helper is the easy path, the rule names its reader, and a pin that reads the class exactly would cost more than the misses it could catch |
| Keep each per-reader key case beside the helper's case | Two cases hold one fact. The removed flags can no longer be mutated, so the old cases' "seen red with `--no-follow` removed" stands on code that is gone | rejected: `frame/design.md` *Removes* |
| Leave `status.showUntrackedFiles` and `i18n.logOutputEncoding` to a later item, because the issue names `log.` keys and `core.quotePath` | Both change what a script reads (executed), and with the helper each costs one line. A later item would pay a frame, a build and a review for a line | rejected: contract rule 12 asks for the class, not the keys the issue happened to name |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 1, 2 and 5 | `tests/hooks/test_gitcmd.py`, one parameter per key of `frame/design.md` *Data & interfaces*, each seen red with that key's `-c` removed from `argv`; then the narrow run over the test modules that read a changed path, at least `tests/skills/test_settle.py`, `test_rule_changes.py`, `test_chain_check.py`, `test_seal_stamp.py`, `test_broad_gate.py` and `test_seal.py`, and `tests/github/test_publish_release_note.py`, `test_close_issues_on_release.py` and `test_release_completeness_check.py`, and `seal layout --check tests` | c8246d3c |
| 2 | Scope 4 | one case per reader with a work item, fragment or test file whose name is not ASCII, as `frame/design.md` *User scenarios & acceptance* lists, each seen red against `5dc1f37e`; the narrow run over the modules those cases sit in | |

## Operational impact

No migration, no environment variable and no dependency. `-c` exists in
every git the plugin runs under, and a git that does not know a key ignores
it. The new cases set keys through `GIT_CONFIG_COUNT`, which needs git 2.31
or later, as the cases they replace did.

A repository meets the change in two places at two times. Its sessions'
`seal` commands run from the installed plugin, so they read git
this way once the release that holds this work is installed. Its pull
request check runs `chain_check.py` from the release its `hygiene.yml` pins,
so the check reads git this way once that pin moves.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
