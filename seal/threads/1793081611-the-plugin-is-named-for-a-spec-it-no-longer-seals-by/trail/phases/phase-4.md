# Phase 4: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 0f694f67 |

## What this phase was asked

Build `frame/plan.md`'s row 4 and nothing of phase 5: the command line. That
is one subparser per tool in `seal.py#main`, the thirteen wrappers and their
`.cmd` twins removed from `bin/`, every document and skill printing the
subcommand, and `templates/hygiene.yml` and the hygiene workflow running
`seal` where they ran a wrapper. The names are the owner's answer (b) to Q1
of `frame/questions.md`: `gate`, `settle`, `cost`, `mutate`, `unverified`,
`arms`, `deferrals`, `fold`, `pact`, `payload`, `stamp`, `layout` and
`rules`. `bin/test` stays, because #1060 decides where it lives. Phase 3's
record left this phase the `bin/mutation-check` comment that named the old
agent file.

The owner's verification decision in `frame/plan.md` *Verification this work
item owes* bound the phase. A script reached under a new name is proved by
its existing cases passing through the new name. A case is written new, and
seen red once, only for behaviour that did not exist before, and here that
is the dispatcher. No `mutation-check` runs. The row's cases and the modules
`git grep -l` finds reading what changed run in one `bin/test` command.

## What this phase found

**The case written new, and the cases relied on.** One case is new:
`tests/test_seal.py::Test_main::test_accepts_each_tool_and_hands_its_script_every_argument`,
parametrised over the thirteen subcommands. Each parameter names the script
its wrapper ran, and the case asserts that `main` hands that script this
interpreter and every argument after the name, `--help` among them. It was
seen red once against the tree before `seal.py` changed: 13 failed, each on
`AttributeError: ... has no attribute 'hand_over'`. Everything else is an
existing case at the new name. Five cases already ran a wrapper the way a
person types it, and each now runs `bin/seal <subcommand>`: the `--help` of
`seal gate`, `seal fold` from `/`, `seal stamp` on a pipe, `seal pact` from
outside the pact's repository, and `seal mutate`, whose red verdict and exit
0 still arrive through the shell. Four cases asserted that a wrapper pair
ships, in `tests/test_deferral_check.py`, `tests/test_payload_meter.py`,
`tests/test_settle.py` and `tests/test_unverified_check.py`. Each now runs
`bin/seal <subcommand> --help` and reads the script's own usage line. The
message pins in each script's module follow the new prefix.

**The run.** The last run of the phase was 122 modules in one command:
5586 passed, 16 skipped, exit 0. The 65 changed Python files pass
`uvx ruff check` and `uvx ruff format --check`, each exit 0. `ls bin/` lists
`seal`, `seal.cmd`, `test` and `test.cmd`.

**How a subcommand runs its script.** `TOOLS` in `seal.py` names each
subcommand's script and the line `seal --help` prints for it. `main` reads
the first argument before it builds its parser. Where that argument names a
tool, `hand_over` runs the script on the same interpreter with the rest of
the arguments untouched, so each script keeps its own parser and its own
help. On POSIX the process is replaced with `os.execv`, as the wrapper's
`exec` replaced it. On Windows the script runs as a child and its exit code
is returned, as the `.cmd` twin returned it. That Windows branch did not run
here.

**The frame does not hold in two places.** First, the two hygiene workflows
ran no wrapper. `templates/hygiene.yml` and `.github/workflows/hygiene.yml`
run `chain_check.py` and `seal.py mode --check` by path, so only a comment
in `.github/workflows/test.yml` changed among the workflows. Second, the
frame says nothing of what each script prints. Every script spelt its old
command as its argparse `prog` and as the prefix of every message, such as
`broad-gate: --base x names no commit`, and a person who typed `seal gate`
would read the name of a command that no longer exists. Each `prog` and each
prefix now spells the subcommand, and each case that pins a message pins the
new text. `gaps.md` holds both, with the two readers below.

**Two readers needed the new name.** The behaviour suite's sealer cases bound
a Bash call matching `broad-gate\s+--base` at zero. After the rename that
bound passes whatever the sealer types, so the generator
`evals/scripts/rule_cases.py` and its five graders read `seal\s+gate\s+--base`,
and `tests/test_evals_layout.py` holds them to it.
`tests/test_one_word_one_meaning.py` refuses any `seal` word in the gate's own
files that is not a name, so `seal gate` and `seal stamp` join `seal mode` as
names there, and the two removed gate wrappers leave its lists.

**The locator rule reads `TOOLS`.**
`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py` asked
that every script a shipped document names have a `bin/` pair. It now asks
that the script have a subcommand in `TOOLS` or a classified reason. A
subcommand is two words and can be prose, as in "a seal stamp", so it counts
as a locator only where it opens an inline code span or a line of a code
block. The case for a half-shipped pair left with the pairs, because no such
state exists. The module's helper cases were rewritten for the two-word
form and were not seen red.

**The edit tool drops trailing whitespace from a replacement.** A
replace-all of `broad-gate: ` with `seal gate: ` wrote `seal gate:` glued to
the next character in six scripts. A grep of the diff found every instance
before the first run, and each was repaired. A later phase that replaces a
prefix ending in a space has to end its replacement on the next character.

**What is left, and whose it is.** Test docstrings that record a run, such
as "seen red by `mutation-check`", keep the name the tool had when that run
happened. The record name `broad-gate.md` and the prose compounds "the
broad-gate run" and "the broad-gate log" name no command, and are phase 5's
census. The replay prompt
`evals/behaviour/proofer/replay-1791779434-r5/prompt.md` keeps
`mutation-check` as it was recorded, next to that run's `seal/specs/` paths.
The scratch prefixes `broad-gate-` and `test-layout-moved-` and the CI job id
`arm-check-grammar` are names no person types as a command. The
`bin/mutation-check` comment that named `agents/smith.md` left with its file.

**The suite writes into the real home directory.** Each run that reached the
session-start group left `~/.claude/agentic/version-check`, as phase 2's and
phase 3's records say. Each was removed after its run, and
`~/.claude/specseal/` was never touched.
