# Review round 1: 1793599987-a-script-reads-git-the-same-under-any-config

```seal
target: 4de1472c against release/v0.29.0
```

The branch was reviewed at `4de1472c` against its merge base `40e6c23e`,
since it has not merged `release/v0.29.0` yet. This is round 1, so no
earlier round's coordinates were carried. The review ran in a
`git clone --no-local` of the branch worktree. In the commands below, `$S`
is the round's scratch directory, and the clone is `$S/clone`. No
`seal/parity.md` is declared, so the record holds no `original:` line.

The orchestrator asked two questions as the reader the rule's `check:` line
names. First, is every `git log` and `git status` a plugin script parses
built by `gitcmd.argv`? Second, does any other script take paths out of
git's output without `-z`? Both crafters' searches were word samples, and
`gaps.md` hands both questions to this round. So this round listed the
calls by taking the scripts apart: an `ast` walk of every tracked `.py`
under `hooks/`, `skills/`, `.github/scripts/` and `bin/`. The walk printed
each argv display that opens with the literal `git`, each call whose first
argument is `git`, each call of a function that builds such an argv from
`*args`, and each `argv` call (`## Probes`, row 1). Then every listed caller
was read for how it uses the output. `bin/` holds shell and batch launchers
with no git call (read).

## Findings

### 1. `seal gate` run as a copy without `hooks/lib/gitcmd.py` stops in a traceback at exit 1, not in a sentence at exit 2

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:233-246`, `skills/verify/scripts/broad_gate.py:3168`, `tests/skills/test_broad_gate.py:2675`
evidence: executed `sh test_tmp_gate.sh $S $S/clone`
```

Why it matters: the gate's own contract for a sibling that will not load
is a sentence and exit 2. The docstring of `broad_gate.py#load`
(`:202-210`) says such a sibling "ends the gate at exit 2 with that
sentence and nothing run, rather than in a traceback".
`Test_gate_copy::test_refuses_a_copy_whose_sibling_will_not_load`
(`tests/skills/test_broad_gate.py:2675`) holds that for `seal_stamp.py`.
This branch adds a second sibling, loaded inside `git` (`:236`). `main`
first reaches `git` through `repo_root` at `:3168`. That call stands
before the `try` at `:3186`, the one that turns a `Refused` into exit 2.
So a missing helper raises `Refused` out of `main`.

Phase 1 claimed: "a copy beside a broken `seal_stamp.py` still refuses
through `STAMP` first". That holds for a broken `seal_stamp.py`. The probe
took the other case: a copy of the gate beside a `seal_stamp.py` that
loads, with no `hooks/lib/gitcmd.py`. It exited 1, and stderr ended in a
Python traceback whose last line is `Refused: cannot load
.../hooks/lib/gitcmd.py — this copy of the plugin is missing it`. A person
reads exit 1 as a gate that ran and failed, while nothing ran. This is a
new failure path the change introduces, on the error-path axis. The other
scripts this branch changes refuse a missing helper with a sentence:
`settle.py` and `seal.py` through their purpose tables, each pinned, and
`chain_check.py` at exit 2 through the `try` at its import.

The fix loads the helper once per process, and `main` catches the refusal
where it first calls `git`. `functools` is already imported for
`stamp_module`. `lru_cache` caches no exception, so a later call raises
again. Both edits stay inside `git` and `main`, which #883 does not touch
by the plan's account (`frame/plan.md` *Technical context*). The fix
assumes no OS precondition beyond the one `PLUGIN` already resolves.

```python
@functools.lru_cache(maxsize=1)
def gitcmd_module():
    """`hooks/lib/gitcmd.py`, loaded once per process, or `Refused`."""
    return load(
        os.path.join(PLUGIN, "hooks", "lib", "gitcmd.py"),
        "agentic_gitcmd_for_broad_gate",
    )


def git(root, *args):
    """stdout of a git call in `root`, or None on a non-zero exit. The argv
    is `hooks/lib/gitcmd.py#argv`'s."""
    r = subprocess.run(
        gitcmd_module().argv("-C", root, *args),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return r.stdout if r.returncode == 0 else None


# in main, in place of the bare call at :3168
    known, _unknown = parser.parse_known_args(argv)
    try:
        root = repo_root(os.path.abspath(known.root or os.getcwd()))
    except Refused as exc:
        sys.stderr.write(str(exc) + "\n")
        return 2
```

The case goes in `tests/skills/test_broad_gate.py#Test_gate_copy`, beside
`test_refuses_a_copy_whose_sibling_will_not_load`. It copies the gate into
`plugin/skills/verify/scripts/` with a `seal_stamp.py` that defines
`is_utf8` and with no `plugin/hooks/lib/gitcmd.py`. It then asserts exit
2, `this copy of the plugin is missing it` in stderr, and no `Traceback`.
The case is seen red against the code at `4de1472c`.

### 2. The rule the settle writes says every script that takes paths out of git's output asks for them with `-z`, and the tree keeps readers that do not

```seal
severity: should
location: `seal/threads/1793599987-a-script-reads-git-the-same-under-any-config/frame/design.md:181-195`
evidence: executed `sh test_tmp_paths.sh $S/probe`, `python3 -I test_tmp_gitcalls.py $S/clone`
```

Why it matters: the reader the rule names acts on its wording. The rule
lands in `docs/what-a-script-gates.md` *Which gate a script holds* with
`check: none reader: the proofer at a change that adds or edits a git call
in a script`. Its bold sentence reads "a script that takes paths out of
git's output asks for them with `-z`", with no exception. The frame keeps
readers outside that sentence on purpose. *Scope*, Out
(`frame/design.md:98-100`), keeps `worktree list --porcelain` without `-z`
as a limit. Scope item 4 (`:64-69`) bounds the `-z` change to six named
readers. The settle deletes the frame, so the exceptions go with it and
the bare sentence is left. After the settle, the tree holds these readers,
which take a path out of git's output without `-z`:

- `skills/implement/scripts/seal.py:1873` and
  `skills/verify/scripts/seal_stamp.py:1341` read the worktree path out of
  `worktree list --porcelain`. `worktree list` takes `-z` from git 2.36
  on.
- Each `rev-parse --show-toplevel`, `--git-common-dir` or
  `--absolute-git-dir` reader returns a path, such as
  `hooks/lib/optin.py:86` and `:142`, `hooks/lib/routing.py:314`,
  `hooks/dispatch.py:308` and `skills/verify/scripts/broad_gate.py:250`.
- `seal.py#indexed` (`skills/implement/scripts/seal.py:1784`) compares
  `line[3:]` of a `status --porcelain` line with `seal/config.md`.

Each of these reads correctly, for reasons the rule does not state. The
probe ran at a top whose name holds Hangul, a double quote and a tab.
`rev-parse` and `worktree list --porcelain` printed that path unquoted,
and `status --porcelain` quoted an untracked name holding Hangul. The
comparison in `indexed` is with an ASCII path the script itself names,
which git never quotes. So a later proofer reads the rule one of two
ways. Read as written, it raises findings on code that is correct, and a
crafter who answers them adds `-z` where git offers none, as for
`rev-parse`. Read with these exceptions in mind, its reader works from
something the rule does not say. Either way, the sentence does not give
one reading (`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은
한 가지로만 읽히게 쓴다*). The frame's own claim about the class is
sound. The ast walk and the reading found no reader that takes a quoted
path out without `-z` beyond the six that phase 2 changed (`##
Confirmations`).

The fix rewrites the rule's `to` so that it bounds itself. Only the bold
sentence's last clause and two sentences after `-z ends each path` change:

```markdown
  to: **A script reads git the same under any configuration: each git
    command a script under `hooks/`, `skills/` or `.github/scripts/` starts
    whose subcommand `hooks/lib/gitcmd.py` names is built by its `argv`,
    and a script that reads a path out of a listing git quotes under
    `core.quotePath`, which is `ls-tree`, `ls-files`, `status --porcelain`
    and the `--name-only`, `--name-status` and `--raw` output of `log`,
    `diff` and `diff-tree`, asks for it with `-z`.** A person's or a
    repository's git configuration can put text into the fields a script
    parses, take a commit's paths out, or follow a path into another one's
    history. `argv` sets each key measured to do that with `-c`, which
    outranks every configuration file. Its docstring names each key, what
    it changes and the subcommands it changes, and a key or subcommand
    found later is added there and nowhere else. `-z` ends each path with a
    NUL and quotes none, whatever `core.quotePath` says. A reader that only
    asks whether git printed anything, prints git's line as it came, or
    compares it with an ASCII path the script names, reads no path.
    `rev-parse` and `worktree list --porcelain` print a path unquoted, and
    a path that holds a newline breaks the second, a limit no flow of the
    plugin reaches. A key nobody has measured is a limit until a run shows
    it changes a reading. Whether a call is one of these is read at review,
    and `tests/hooks/test_gitcmd.py` holds each key.
    check: none reader: the proofer at a change that adds or edits a git call in a script
```

## Confirmations

```seal
confirms: none
```
What matched: every `git log` and `git status` a script under `hooks/`,
`skills/` or `.github/scripts/` starts is built by `gitcmd.argv`
(executed and read). The ast walk listed every git call, and 16 of them
run `log` or `status`:
`.github/scripts/close_issues_on_release.py:394` and `:396`;
`.github/scripts/publish_release_note.py:235`, `:259` and `:429`;
`.github/scripts/release_completeness_check.py:143`;
`skills/code-review/scripts/chain_check.py:415`, `:418` and `:1812`;
`skills/implement/scripts/seal.py:1730`;
`skills/settle/scripts/rule_changes.py:654`;
`skills/settle/scripts/settle.py:346`, `:1114` and `:1428`;
`skills/verify/scripts/broad_gate.py:3109`; and
`skills/verify/scripts/seal_stamp.py:1203`. Each is built by `argv`, at
the call or through a wrapper that builds every argv it runs with `argv`.
Phase 1 claimed its search listed 15 calls. The same word search, run
here, lists the same 16 lines (`## Probes`, row 2). The count was off by
one, and no call is left unbuilt. Six calls pass their subcommand through
a variable: `settle.py:1453` and `:1473`, `seal.py:334`,
`hooks/review-skill-gate.py:109` and the two wrappers they reach. Their
values are `diff`, `ls-files`, `worktree`, `config`, `rev-parse` and
`cat-file`, and none is `log` or `status` (read). No hook runs `log` or
`status`, so the frame's claim that no hook changes holds (executed). No
shipped script hands git a shell string (read). Phase 1 judged that
`close_issues_on_release.py#run` is no git wrapper, because it runs `gh`
as well. That judgment holds: `argv` would put `git -c` in front of a `gh`
call, so each `log` there is built at its call.

```seal
confirms: none
```
What matched: apart from the six readers phase 2 changed, no reader takes
a path that git quotes under `core.quotePath` out of git's output without
`-z` (executed and read). Every path listing the walk found passes `-z`,
or else it reads no path in the sense that matters here.
`publish_release_note.py:253` and `:262`, `settle.py:609` and
`chain_check.py:1927` only check whether `ls-tree` printed anything.
`unverified_check.py:1573` reads only the mode field. The
`status --porcelain` readers at `chain_check.py:415` and
`broad_gate.py:3109` read only whether the output is empty. `seal.py:2533`
prints `line[3:]` in a note, and `seal.py:2400-2406` returns the
`ls-files --stage` lines it prints. `rev-parse` and
`worktree list --porcelain` print paths unquoted (`## Probes`, row 3).
Finding 2 is about the rule's wording, not about these readers.

```seal
confirms: none
```
What matched: `hooks/lib/gitcmd.py#argv` holds each of the five keys
against a person's and a repository's setting (executed). The narrow run
of `tests/hooks/test_gitcmd.py` gave 17 passed, and the signed-commit
parameter did not skip. Each value in `KEYS` is the one the readers need.
One docstring word is loose: `i18n.logOutputEncoding` defaults to
`i18n.commitEncoding`, not to UTF-8. `UTF-8` is still the value every
reader decodes with, so it is the right value, and the docstring's phrase
"git's own default" holds wherever `i18n.commitEncoding` is unset (read).

```seal
confirms: none
```
What matched: `color.ui=always` is a key outside the frame's measurements,
and it changes none of the argv shapes the scripts parse (executed,
`## Probes`, row 4). The probe ran 14 commands, each with and without the
key, and their bytes were the same: each `log` form, `status --porcelain`,
`diff --name-only -z`, `diff --raw -z`, `diff-tree -z`, `ls-tree -z`,
`ls-files -z` and `show <rev>:<path>`.

```seal
confirms: none
```
What matched: phase 2's six non-ASCII cases and the `adding_commit` cases
pass at `4de1472c`, 9 passed (executed). Two mutants of
`rule_changes.py#order` were run by #898's fixed copy of `seal mutate`,
from the `fix/898-a-mutant-that-does-not-compile-reads-as-caught`
worktree. One dropped `-z` and one dropped the newline strip, and both
went red against
`test_merge_order_of_an_id_that_is_not_ascii_is_its_designs_add`. The
clone was clean after the run (executed).

```seal
confirms: none
```
What matched: the frame's `## Removes` is carried out and nothing else
was removed (executed and read). The five flags and four sentences are
gone, and a `git grep` for each key's name and flag finds them only in
`hooks/lib/gitcmd.py`, its test, and the `core.quotePath` comments the
`-z` readers gained. The three per-reader cases and the parametrization
are gone from `tests/skills/test_settle.py`.
`Test_adding_commit::test_accepts_the_oldest_add_of_each_path` keeps the
accepts case `seal layout --check` needs. `seal layout --pairs` over the
eight changed test modules reports one pair, in
`tests/skills/test_seal.py#Test_pinned`, which this branch does not touch
(executed). Each new case covers a non-ASCII path or a key that its group
did not cover before (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `4de1472c`; the suite stays `unverified` here, by contract rule 2 | the branch | the orchestrator, by `seal gate --base release/v0.29.0 --record 1793599987-a-script-reads-git-the-same-under-any-config` once the rounds settle |
| Whether `tests/hooks/test_gitcmd.py` and the six non-ASCII cases read the same on the Windows and Linux legs; this round ran on macOS with git 2.50.1 | `.github/workflows/test.yml` | the orchestrator, reading the legs of the pull request's test run |
| Git config keys beyond the five set and `color.ui`; the domain is unbounded, and the frame states it as a limit | `hooks/lib/gitcmd.py` | the proofer at the next change that adds or edits a git call in a script |

## Probes

`$S` is the round's scratch directory. Each probe ran once and was deleted
with the clone before the hand-back.

| Command | Result |
|---|---|
| `python3 -I test_tmp_gitcalls.py $S/clone` | 136 lines: every git argv display, call and wrapper call in the tracked `.py` under `hooks/`, `skills/`, `.github/scripts/` and `bin/`; 16 run `log` or `status`, and each is built by `argv` |
| `git grep -n -E '"(log\|status)"' -- hooks skills .github/scripts` | 16 `.py` lines, the same 16 calls |
| `sh test_tmp_paths.sh $S/probe` | under no global or system config, at a top named with Hangul, a double quote and a tab, `rev-parse --show-toplevel`, `--absolute-git-dir` and `worktree list --porcelain` printed the path unquoted; `status --porcelain` printed an untracked Hangul name as `"\354\240\225.txt"` |
| `sh test_tmp_color.sh $S/probe` | 14 commands, each the same bytes with and without `color.ui=always` |
| `sh test_tmp_gate.sh $S $S/clone` | a copy of `broad_gate.py` beside a loading `seal_stamp.py` and no `hooks/lib/gitcmd.py` exited 1 with a traceback ending in `Refused: cannot load .../hooks/lib/gitcmd.py — this copy of the plugin is missing it` |
| `bin/test tests/hooks/test_gitcmd.py -q` | 17 passed, exit 0 |
| `bin/test tests/skills/test_settle.py tests/skills/test_unverified_check.py tests/github/test_publish_release_note.py tests/skills/test_test_layout.py -q -k "not_ascii or adding_commit"` | 9 passed, exit 0 |
| `seal mutate skills/settle/scripts/rule_changes.py` with two `--replace` pairs, `-z` dropped and the newline strip dropped, `--tests "bin/test tests/skills/test_settle.py -q -p no:xdist -k merge_order_of_an_id_that_is_not_ascii"`, by #898's fixed copy | baseline passed; 2 mutants, 2 red, 0 survived |
| `seal layout --pairs` over the eight changed test modules | 8 files read, 1 pair, in `tests/skills/test_seal.py#Test_pinned`, which the branch does not touch |
