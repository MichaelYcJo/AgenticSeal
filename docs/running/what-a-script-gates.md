# What a script gates, and what an agent judges

Every check that gates is listed here with what it reads, what it does with
what it did not read, and the agent that judges the meaning of the same
text. The rule is
`skills/core/SKILL.md` *Judgment is spent where meaning is the question,
and a script answers the rest* and *The rule a mechanism is kept against*;
this document is the standing account of its application.

## Which gate a script holds

**A script gates a closed form, in one spelling; a judgment of meaning
belongs to the agent that already reads the text, at a named step.** A
closed form is an exit code, a real parser's result, a structure a command
wrote, or a line of a form the plugin defines, spelt as that form spells it, such as a field inside a `seal` block or the header `| Pact | Clause | Hash |`. A line spelt otherwise is
prose to the script: where the form requires the line, its absence is
refused; where it does not, the line is named as one the script did not
read, and whether it meant the label is the reading agent's judgment, by
the core's sections cited above. A check added or changed names, in its pull
request, the form it reads, what it names as unread, and the agent and
step that judge the meaning of the same text.
check: tests/skills/test_chain_check.py tests/skills/test_pact_check.py tests/github/test_rules.py tests/skills/test_rule_changes.py

**A script reads git the same under any configuration: each git
command a script under `hooks/`, `skills/` or `.github/scripts/` starts
whose subcommand `hooks/lib/gitcmd.py` names is built by its `argv`, and
a script that takes a path out of output git quotes under
`core.quotePath` asks for it with `-z`.** A person's or a repository's
git configuration can put text into the fields a script parses, take a
commit's paths out, or follow a path into another one's history. `argv`
sets each key measured to do that with `-c`, which outranks every
configuration file. Its docstring names each key, what it changes and
the subcommands it changes, and a key or subcommand found later is added
there and nowhere else. Git quotes the paths its listings print, such as
those of `ls-tree`, `ls-files` and `status --porcelain` and the
`--name-only`, `--name-status` and `--raw` output of `log`, `diff` and
`diff-tree`. `-z` ends each such path with a NUL and quotes none,
whatever `core.quotePath` says. A reader that only asks whether git
printed anything, prints git's line as it came, or compares the line
with an ASCII path the script names takes no path out. `rev-parse` and
`worktree list --porcelain` print a path unquoted, and a path that holds
a newline breaks the second, a limit no flow of the plugin reaches. A
key nobody has measured is a limit until a run shows it changes a
reading. Whether a call is one of these is read at review, and
`tests/hooks/test_gitcmd.py` holds each key.

## The checks

The table reads: "Runs at" is the moment the check decides; "Unread" is
what it does with what it cannot read; "Agent" is the judgment of meaning
left to a party on the same text.

| Check | Runs at | Reads | Unread | Agent |
|---|---|---|---|---|
| `hooks/routing-edit-gate.py` | every `Write`, `Edit`, `NotebookEdit` | `routing.md`'s rows for the checked-out branch through `hooks/lib/routing.py`; the `seal no-work-item` record | refuses the edit while no declaration it can read names the branch | none; the routing answer is the person's |
| `hooks/question-gate.py` | every `AskUserQuestion` | the `Automation` row | a declaration it cannot read is the attended answer: silence | none |
| `hooks/mode-gate.py` | the session's commands | `config.md`'s `Mode` row | a table it cannot read is silence, a stated limit | none |
| `hooks/review-skill-gate.py` | a `Skill` call naming a review | the skill's name | nothing to read otherwise | the person picks the review |
| `hooks/sealer-stamp-queue.py`, `hooks/sealer-stamp.py` | the write of `guarantee.md`; the turn's end | the verdict blocks, through `hooks/lib/fields.py` | queues nothing where the reader refuses a line of the file or the newest block does not read `Verdict: sealed` | the verdict is the sealer's |
| `hooks/lint-python.py` | the write of a `.py` in a repository with a ruff config | ruff's exit code and output | nothing | none |
| `skills/code-review/scripts/chain_check.py`, as hygiene's chain step and `seal gate`'s arm 2 | the pull request; the preflight and the broad run | routing rows; the frame's mark; `## Rule changes` through `rule_changes.py`, and the `check:` lines of its `add` and `change` `to` values through `.github/scripts/rules.py`; against each operation, the string constants under `tests/` through `ast` and the rule documents through `skills/settle/scripts/passages.py`; the `seal` blocks of the round records, `trail/gate.md` and `guarantee.md` through `hooks/lib/fields.py`, and the finding headings; the branch's commits and `Seal-Routing` trailers; `seal/parity.md`'s `Baseline commit` | refuses at its line a block line that does not parse, and a required block that is absent; names each file under `trail/rounds/` it did not read, each fence opener near the block's, each line of a `to` that opens like a `check:` line and is not one, and each source it cannot read, as `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* lists them; names each test pin a `from` takes out and each run a `to` shares with another rule document, refusing neither; a line outside a block is prose | whether a fix holds: the verifying round; whether the parties agree: the sealer; what a named unread line meant: the orchestrator at the preflight; whether a named pin or copy is a finding: the proofer at review |
| `seal gate`'s `Broad gate` row and arm 3 | the orchestrator's one run | the row's command's exit code; the gate's pytest recorder; the `Mode` row | refuses at exit 2 a row it would not run as the command it reads as, which goes to a person | none; `new`, `failing on base too` and `new?` are reported and the orchestrator acts |
| hygiene's other steps: `issue_claims_check.py`, the version step, `release_completeness_check.py`, the mode step, the READMEs step | the pull request | the body's closing keywords by GitHub's own grammar; `plugin.json`; the milestone through `gh`; commit subjects' `(#N)` and their `feat:` prefix in that one spelling; the head branch's version; two files | the body is reported at exit 0, never failed; a subject spelling `feat` otherwise is named as not read; the rest refuse on the fact read | whether a subject's prefix states what the change is: its writer, by `skills/commit-pr-convention/SKILL.md` |
| `ruff check`, `ruff format --check`, `pytest` | CI and the broad run | code | a real tool's own | none |
| `seal rules --check`, through `tests/github/test_rules.py`, and hygiene's step that prints the `check:` lines it did not read | the suite; each pull request | `check:` lines in the one shape | names a near line as not read; a target it cannot resolve is refused; a target wrapped onto the next line is not read | whether a target enforces its rule: review |
| `seal layout --check`, `seal arms` | the crafter; the suite | test files and modules through `ast` | refuses on the tree | none |
| `seal unverified` | the settle; a session | `## Not verified` rows and the no-change block | fails on a section it cannot read, never on an open row; names a near heading and a near block | none |
| `seal settle`, `skills/settle/scripts/rule_changes.py` | the owner | `## Rule changes`, open rows, `frame/plan.md` *Judgments of the run* of the released plans and, through `git log` and `git show`, of every plan an earlier settle removed | a section that does not parse is refused at its line at the pull request and read whole at the settle; a near heading outside the section is named and is another section, one inside it is a line of the section, and a design with a named line is read whole at the settle; a heading near *Judgments of the run* is named, a `trail/rounds` it cannot list is named, and a file in a work item's directory with the name of a record it reads, at another path, is named and removed with the directory | the settling session writes the latest decision |
| `seal pact` | a person, at the pact's repository | the anchor table under the exact header, through `gfm_table` | refuses at exit 2 a row it cannot grade; names a table under a near header and grades none of it | the proofer: a line meant as an anchor that the tool did not read is a finding |
| `seal deferrals` | a session, before it writes an `unverified` row | the command lines of workflows and hooks that run a kind of check | names each workflow holding a runner for the reader to open; reads no trigger | whether the workflow runs on pull requests: the agent that opens it |
| `seal pr-body --check` | the sealer | the body file against the records | withholds | none |
| the cases under `tests/text/` and `tests/behaviour/` that read prose | the suite | a sentence, a citation, a heading | a case pins a fact a reader acts on; one that pins wording goes | the proofer reads prose for meaning |
| `seal fold`, `seal core` | the owner at the settle; the orchestrator | document sizes and the index; the transcript's first core line | reports; `seal fold` refuses a document the index does not name | none |
| `seal mutate` | the crafter at each unit that adds behaviour; a round or the sealer re-running a claim | the tests command's exit code, against the file as it is and against each mutant; for a `.py` target, `compile`'s result over the bytes each mutant would put on disk, before anything is written or run | refuses a `.py` mutant that does not compile; names a `.py` file that does not compile as it is under the running interpreter as not compiled, and decides its mutants by the exit code alone; compiles no other kind of file | whether a red's failure is the unit's, an import error's or a collection error's: the crafter reading the run, and the proofer and the sealer re-running it |

**How this table is kept true.** No case holds it against the tree. Each
row names a script that has its own tests and its own home sentence, so a
row that drifts is found when that script's home is read, and the settle
reads this document against the code as it reads every policy document.
A test that held the table from both sides would be a mechanism with no
catch to its name on the day it was added, and
`skills/core/SKILL.md` *The rule a mechanism is kept against* is why it is
not built.
