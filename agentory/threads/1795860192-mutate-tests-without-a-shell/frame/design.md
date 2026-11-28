# Design: 1795860192-mutate-tests-without-a-shell

## Grounding

The tree as read at `8e130543`.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/verify/scripts/mutation_check.py#command_words`, `#main` | `--tests` is split into words and run with no shell, so a shell's operators reach the first program as its arguments |
| `skills/verify/agentic-mutate.md` *`agentic mutate` asks condition 2 of one unit, one break at a time* | exit 2 is every run that measured nothing, `refused` among them, and nothing is written |
| `skills/verify/agentic-mutate.md`, the paragraph opening **The bound ends what the run started** | the timeout kills the command's process group on POSIX, which the verdict's bound rests on |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | a script holds a gate only on a fact it reads exactly |
| `.github/workflows/test.yml` | the suite runs on Windows, where no `sh` can be assumed |

G1, the choice the issue leaves: refuse, not `sh -c`. A `sh -c` run would need a POSIX shell where the cases run on Windows. It would make the shell, not the cases, the direct child whose exit code is the verdict, and it would read quoting twice, once for `--tests` and once for the shell. A refusal reads one fact exactly: a character of `; & | < >` that a POSIX shell would read as an operator, outside quotes and not escaped. It writes nothing, and names the `sh -c '…'` form, which a person with a shell can pass on purpose.

G2, `executed` on 2026-11-28: `shlex.shlex(text, posix=False, punctuation_chars=";&|")` separates `&&` outside quotes from one inside them, and reads an escaped `\;` as an operator. A POSIX shell reads `\;` as a literal `;`, so that reader would refuse a command a shell would run as one. The reader is therefore a scan that follows the shell's quoting: single quotes, double quotes, and a backslash outside single quotes, the last on POSIX only, as `command_words` reads it.

## Scope

In:

1. `mutation_check.py#shell_operators(text, windows=None)`: the characters of `; & | < >` in `text` outside single and double quotes and, where `windows` is false, not after a backslash, each operator run once, in order. `main` refuses with exit 2, and writes nothing, where it names any. The message names each operator and the form `--tests "sh -c '<command>'"`.
2. `skills/verify/agentic-mutate.md`: one paragraph after the command's synopsis, saying `--tests` is split into words and run with no shell, and what the refusal reads.
3. The cases in `tests/skills/test_mutation_check.py`, `Test_main` beside the case for a command that names nothing, and `Test_module` beside `command_words`' cases, each seen red against `8e130543`.
4. The work item's `changelog.md`.

Out: `$( )`, backticks and `$VAR` expansions. A shell would expand them, and here they reach the program as literal text. A program that receives them fails or reads them as its own, and no case of this issue shows one passing silently.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given `--tests "a && b"`, when `agentic mutate` runs, then it exits 2, prints `refused` naming `&&` and the `sh -c` form, and writes nothing | `Test_main` case |
| S2 | Given an operator inside quotes, `--tests 'bin/test -k "a or b; c"'`, or `sh -c 'a && b'`, when it runs, then nothing is refused for it | `Test_module` cases of `shell_operators` |
| S3 | Given `find . -exec x {} \;` on POSIX, then `\;` is no operator, and on Windows it is one | `Test_module` cases of `shell_operators` with `windows` both ways |

## Data & interfaces

`shell_operators(text: str, windows: bool | None = None) -> list[str]`, beside `command_words`, with the same `windows` default.

## Rule changes

- nothing
  why: `skills/verify/agentic-mutate.md` is the skill's supporting file, not the policy root, and the change states the command's own reading there

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| nothing | | the change adds a refusal and one paragraph |

Framed 2026-11-28 by the session, before the build.
