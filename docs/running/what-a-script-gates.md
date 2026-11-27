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
check: tests/skills/test_chain_check.py tests/skills/test_pact_check.py tests/skills/test_rules.py tests/skills/test_rule_changes.py

**A script reads git the same under any configuration: each git
command a script under `lib/`, `skills/`, `.github/scripts/` or
`evals/scripts/` starts is started by `lib/gitcmd.py#git`, which builds
it with `argv`, and a script that takes a path out of output git quotes
under `core.quotePath` asks for it with `-z`.** A person's or a repository's
git configuration can put text into the fields a script parses, take a
commit's paths out, or follow a path into another one's history. `argv`
sets each key measured to do that with `-c`, which outranks every
configuration file. A setting measured to do it that no `-c` key
reaches, such as one a file of the repository carries, is held by a flag
`argv` puts on every command of each subcommand the setting reshapes, so
no script passes it. `lib/gitcmd.py`'s docstring names each key, and
each such setting with its flag, with what it changes and the
subcommands it changes, and one found later is added there and nowhere
else. Git quotes the paths its listings print, such as those of
`ls-tree`, `ls-files` and `status --porcelain` and the `--name-only`,
`--name-status` and `--raw` output of `log`, `diff` and `diff-tree`.
`-z` ends each such path with a NUL and quotes none, whatever
`core.quotePath` says. A reader that only asks whether git printed
anything, prints git's line as it came, or compares the line with an
ASCII path the script names takes no path out. `rev-parse` and
`worktree list --porcelain` print a path unquoted, and a path that holds
a newline breaks the second, a limit no flow of the plugin reaches. A
key nobody has measured is a limit until a run shows it changes a
reading. Whether a call is one of these is read at review, and
`tests/lib/test_gitcmd.py` holds each key and each flag.

**A git or `gh` command that did not start, or did not finish within
`lib/gitcmd.py#TIMEOUT`, is no answer, and no script reads it as one.**
Each `gh` command a script starts is started by `lib/gitcmd.py#gh`
under the same bound. Both runners raise `lib/gitcmd.py#Unrun`, whose
one line names the command, and neither reads an exit code unless asked
to with `check=True`, which raises `lib/gitcmd.py#Exited` on a non-zero
exit, because for some commands, such as `merge-base --is-ancestor`,
`diff --quiet` and `config --get`, exit 1 is an answer. Both are a
`lib/gitcmd.py#Failed`, a `SystemExit`, as `lib/sibling.py#Absent` is,
so a script that does not catch one ends with its line at exit 1 and
never in a traceback. A
reader whose unanswered question has a documented default, such as the
*not opted in* of `lib/optin.py#repo_root`, catches it at the call, and
a command whose error code is not 1 catches it in `main` and returns
that code. A script that loads nothing from `lib/` at import names why
in its docstring, as `.github/scripts/release_seal.py` does, and loads
the runner at first use.
check: tests/lib/test_gitcmd.py tests/skills/test_seal.py tests/skills/test_settle.py

**A script under `lib/`, `skills/` or `hooks/` starts no git command
that a git older than `lib/gitcmd.py#OLDEST` refuses or reads otherwise,
and the script whose command set that version asks
`lib/gitcmd.py#older` before its first command.** A person's machine
runs these scripts on the git it has, and an agent that meets git's own
refusal mid-run reads it as a fact about the repository. `OLDEST` is the
version git's release notes give for the newest option those scripts
pass, and its docstring names that option. A change that adds a command
only a newer git reads raises `OLDEST` in the same commit and moves the
ask to its script. `older` reads the one line `git version` prints, and
a line in another shape refuses nothing.
check: tests/lib/test_gitcmd.py tests/skills/test_range_read.py

## The checks

The table reads: "Runs at" is the moment the check decides; "Unread" is
what it does with what it cannot read; "Agent" is the judgment of meaning
left to a party on the same text.

| Check | Runs at | Reads | Unread | Agent |
|---|---|---|---|---|
| `seal stamp --guarantee` and `seal stamp --stop` (`skills/verify/scripts/seal_stamp.py`) | the sealer's run after it writes `Verdict: sealed`; the end of the main session's turn, by the plugin's `Stop` hook | the verdict blocks, through `lib/fields.py` | queues nothing where the reader refuses a line of the file or the newest block does not read `Verdict: sealed` | the verdict is the sealer's |
| `skills/code-review/scripts/chain_check.py`, as hygiene's chain step and `seal gate`'s arm 2 | the pull request; the preflight and the broad run | routing rows; the frame's mark; `## Rule changes` through `rule_changes.py`, and the `check:` lines of its `add` and `change` `to` values through `skills/settle/scripts/rules.py`; against each operation, the string constants under `tests/` through `ast` and the rule documents through `skills/settle/scripts/passages.py`; the `seal` blocks of the round records, `trail/gate.md` and `guarantee.md` through `lib/fields.py`, and the finding headings; the branch's commits and `Seal-Routing` trailers; `seal/parity.json`'s `Baseline commit`; the pull request's body, from the run's event payload, against what `seal pr-body` composes at HEAD | refuses at its line a block line that does not parse, a required block that is absent, and, on the work item's directory at line 0 with the body's line in its message, a line of the body that is not what `seal pr-body` composes; names the body as not read where the payload holds none, or the pull request carries more than one judged work item with a `pr.md`, or several and none with one; names each file under `trail/rounds/` it did not read, each fence opener near the block's, each line of a `to` that opens like a `check:` line and is not one, and each source it cannot read, as `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* lists them; names each test pin a `from` takes out and each run a `to` shares with another rule document, refusing neither; a line outside a block is prose | whether a fix holds: the verifying round; whether the parties agree: the sealer; what a named unread line meant: the orchestrator at the preflight; whether a named pin or copy is a finding: the proofer at review |
| `seal gate`'s `Broad gate` key and arm 3 | the orchestrator's one run | the key's command's exit code; the gate's pytest recorder; the `Mode` key | refuses at exit 2 a key it would not run as the command it reads as, which goes to a person | none; `new`, `failing on base too` and `new?` are reported and the orchestrator acts |
| hygiene's other steps: `issue_claims_check.py`, the version step, `release_completeness_check.py`, the mode step, the READMEs step | the pull request | the body's closing keywords by GitHub's own grammar; `plugin.json`; the milestone through `gh`; commit subjects' `(#N)` and their `feat:` prefix in that one spelling; the head branch's version; two files | the body is reported at exit 0, never failed; a subject spelling `feat` otherwise is named as not read; the rest refuse on the fact read | whether a subject's prefix states what the change is: its writer, by `skills/commit-pr-convention/SKILL.md` |
| `ruff check`, `ruff format --check`, `pytest` | CI and the broad run | code | a real tool's own | none |
| `seal rules --check`, through `tests/behaviour/test_this_repository_passes_its_own_checks.py`, and hygiene's step that prints the `check:` lines it did not read | the suite; each pull request | `check:` lines in the one shape | names a near line as not read; a target it cannot resolve is refused; a target wrapped onto the next line is not read | whether a target enforces its rule: review |
| `seal layout --check` | the crafter; the suite | test files and modules through `ast` | refuses on the tree | none |
| `seal unverified` | the settle; a session | `## Not verified` rows and the no-change block | fails on a section it cannot read, never on an open row; names a near heading and a near block | none |
| `seal settle`, `skills/settle/scripts/rule_changes.py` | the owner | `## Rule changes`, open rows, `frame/plan.md` *Judgments of the run* of the released plans and, through `git log` and `git cat-file --batch`, of the plans the two newest removing commits deleted, or of every removed plan under `--all-earlier` | a section that does not parse is refused at its line at the pull request and read whole at the settle; a near heading outside the section is named and is another section, one inside it is a line of the section, and a design with a named line is read whole at the settle; a heading near *Judgments of the run* is named, a `trail/rounds` it cannot list is named, and a file in a work item's directory with the name of a record it reads, at another path, is named and removed with the directory | the settling session writes the latest decision |
| `seal pact` | a person, at the pact's repository | the anchor table under the exact header, through `gfm_table` | refuses at exit 2 a row it cannot grade; names a table under a near header and grades none of it | the proofer: a line meant as an anchor that the tool did not read is a finding |
| `seal deferrals` | a session, before it writes an `unverified` row | the command lines of workflows and hooks, against the runner words `skills/verify/scripts/deferral_check.py#RUNNERS` holds for a kind of check | names each workflow and hook holding a line those words match, for the reader to open, and exits 0 whatever it matched; refuses only a path or an argument it cannot use; reads no trigger | whether a file it named or left out runs the check, and whether that file runs on pull requests: the agent that opens it |
| `seal pr-body` and `seal pr-body --check` | the orchestrator, writing the body; the sealer, before its verdict; the pull request's check, through the same function | `seal/config.json`'s two language keys; `pr.md`, and each quote of it, a line in the form `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* gives, against the file of the work item its path names; the one `pr.<lang>.md` where the keys differ; the body against them, the records and the mark the `Pull request seal mark` key and the guarantee at HEAD give; the composed body's length against GitHub's limit, which folds the longest sections of the copy and refuses a body that still passes it | refuses where a language key is absent, where the keys differ and the work item holds no `pr.<lang>.md` or more than one, and at each line of `pr.md` whose quote the file its path names does not hold; withholds at the sealer; refuses at the pull request | whether each line of `pr.<lang>.md` renders the sentence at its coordinate, and whether what a quote's coordinate names after its path holds the quote: the rounds and the sealer |
| the cases under `tests/text/` and `tests/behaviour/` that read prose | the suite | a sentence, a citation, a heading | a case pins a fact a reader acts on, and the absence of a command, a path or a spelling is such a fact where a rule of that text itself forbids it there, whether or not a shipped release removed it; one that pins wording goes, and so does one that pins the absence of text or a design that a shipped release removed and that no rule of that text forbids. A rule that binds every text alike, such as one source for a fact, keeps no absence. A line a step or a script prints, read from its file by a case that runs nothing, is weighed as any other text | the proofer reads prose for meaning |
| `seal fold` | the owner at the settle | document sizes and the index | reports; refuses a document the index does not name | none |
| `seal mutate` | the builder, the crafter or the orchestrator that builds itself, at each unit that adds behaviour; a round or the sealer re-running a claim | the tests command's exit code, against the file as it is and against each mutant; for a `.py` target, `compile`'s result over the bytes each mutant would put on disk, before anything is written or run | refuses a `.py` mutant that does not compile; names a `.py` file that does not compile as it is under the running interpreter as not compiled, and decides its mutants by the exit code alone; compiles no other kind of file | whether a red's failure is the unit's, an import error's or a collection error's: the builder reading the run, and the proofer and the sealer re-running it |
| `seal pr-wait` (`skills/code-review/scripts/pr_wait.py`) | the orchestrator, when a pull request opens and before and after each push to its branch | `gh pr view`'s `state`, `mergeable`, `headRefOid` and `statusCheckRollup`, `gh pr checks`'s `event` and `bucket`, and `gh run list`'s `status`, each as `gh`'s JSON | a check of another CI service, or of an event other than `pull_request`, counts toward the result and never toward the start, so a pull request whose checks all come from elsewhere ends at exit 3 naming the commit; a `gh` call that fails is exit 2 with its message, never a reading of the pull request | which failed or cancelled check is a defect of the work, and its repair: the orchestrator reading the check's log |
| the `PreToolUse` hook (`hooks/ask-under-automation.py`) | each `AskUserQuestion` call of a session | the `Automation` row of each `routing.md` through `lib/routing.py`, under the root of each worktree `git worktree list --porcelain` lists, where the row's `Branch` is checked out in one of them; and, where one of those rows reads `yes`, the text of each question of the call, for `hooks/ask-under-automation.py#MARKER` followed on the same line by a reason, refusing the call where a question lacks it | lets the call through, printing nothing, where the payload, the question list, git or a root cannot be read; names a question holding the marker with its case changed as not read and refuses the call; reads no other spelling | whether a question is one only the owner can decide: the orchestrator writing the reason, and the person reading it |
| the `PostToolUse` hook on `Edit` (`hooks/hooks.json`) | each `Edit` call of a session or a subagent | the call's `file_path`, `old_string` and `new_string`; where the file is a work item's record outside `trail/` and `guarantee.md` under a root whose `README.md` opens with the marker, the words the edit replaced, with the words beside them in the edited file, looked for with whitespace collapsed in the item's such records, the edited file among them | prints nothing where the payload, the path, the root or a file cannot be read; reads no `Write` call, no record that is a link, and no file outside the item's directory but a root's `README.md`, through the marker read of `lib/optin.py#marked`, bounded at the marker's length plus two characters and printed nowhere; refuses nothing | whether a place it names states the fact the edit changed: the party that made the edit |
| `seal range` | the builder, after the last commit of a phase or of a fix pass | `git diff` from the commit it is given to HEAD, HEAD's text of each changed text file, and the work item's records that state the present, at HEAD or on disk where the root is local | names as not printed a binary path, a deleted path and a submodule's path, and as not read a tracked path with an uncommitted change; exits 2 and writes nothing where the commit is no ancestor of HEAD, the file cannot be written, or the git that answers is older than `lib/gitcmd.py#OLDEST` | whether a printed statement is one HEAD contradicts: the builder reading the file, and the round that follows |

**How this table is kept true.** No case holds it against the tree. Each
row names a script that has its own tests and its own home sentence, so a
row that drifts is found when that script's home is read, and the settle
reads this document against the code as it reads every policy document.
A test that held the table from both sides would be a mechanism with no
catch to its name on the day it was added, and
`skills/core/SKILL.md` *The rule a mechanism is kept against* is why it is
not built.
