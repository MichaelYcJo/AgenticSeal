# Review round 1: 1794986401-the-process-has-no-name

```seal
target: 083fd5d74 against release/v0.38.3
```

The branch was read against `release/v0.38.3` at `fab41dc91`, the merge
base, over its five commits, in a `git clone --no-local` checked out at
`083fd5d74`. This is the first round, so no coordinate or verdict was
carried from an earlier one; every fact below was established here.
`seal/parity.json` is not declared, so no parity comparison was owed. The
work item's records were each read whole at `083fd5d74`: `routing.md`, the
three frame files, `gaps.md`, `changelog.md`, `pr.md` and
`trail/phases/phase-1.md`. `seal/config.json` names English for both
language keys, so no `pr.<lang>.md` is owed and none stands. Issue #1557
was read with `gh issue view 1557 --json body,comments,title`: no comment,
and its *Decision* and *Change* are the ones `frame/design.md` G1 reports.

The axes this change has are its own: whether each place in scope now uses
one name, whether every "workflow" left in those files names a GitHub
Actions workflow, whether each statement of a renamed fact elsewhere was
moved with it, whether each citation of the renamed heading resolves,
whether the manifest descriptions stay equal, and whether the records state
the tree truly. The table's axes of inputs, authorization, query scope,
ordering, state, concurrency and security have nothing to compare in a diff
that changes prose, docstrings and comments only: no executable line
changes (read: `git diff fab41dc91...083fd5d74 -- lib tests`, which changes
docstrings, comments and one string literal that a case compares to a
heading).

## Findings

### 1. The changelog says `CONTRIBUTING.md` uses the name wherever "workflow" meant the process, and `CONTRIBUTING.md:58` still calls the process "a spec-driven workflow"

```seal
severity: should
location: `CONTRIBUTING.md:58`, `seal/threads/1794986401-the-process-has-no-name/changelog.md:3`
evidence: executed `git grep -n -i workflow -- CONTRIBUTING.md`; read `CONTRIBUTING.md:56-62`, `README.md:460-464`, `seal/threads/1794986401-the-process-has-no-name/changelog.md:3`
```

Why it matters: `changelog.md:3` claims "The plugin's description, the
core, `CLAUDE.md`, `CONTRIBUTING.md`, the `seal/README.md` template, the
pull-request check's header and `lib/optin.py`'s docstrings use the name
wherever "workflow" meant the process." The release note is built from that
sentence. The search over `CONTRIBUTING.md` prints ten lines. Nine name a
GitHub Actions workflow or its file (`:51`, `:89`, `:158`, `:206`, `:211`,
`:241`, `:278`, `:439`, `:460`). `CONTRIBUTING.md:58` names the process:
"This repository runs a spec-driven workflow on itself: work items under
`seal/threads/`, review rounds, a version that moves once per release." The
change only rewrote the heading citation at `CONTRIBUTING.md:392-393`.

The same thing now has two names across two files a reader goes between.
`README.md:460-464` points at `CONTRIBUTING.md` *What a contribution is not
asked for* and now says "none of the AgenticSeal process this repository
runs on itself applies to one". The section it points at, at
`CONTRIBUTING.md:56-58`, calls that "a spec-driven workflow".
`frame/design.md` G5 holds that one thing is called by one name. The
frame's *Out* list leaves "the workflow" in `docs/`, `skills/` and
`agents/`, and `CONTRIBUTING.md` is in none of them, so no scope decision
keeps this line.

The fix renames the line, which makes the changelog sentence true as it
stands. The paragraph's next line is unchanged, since the new first line
stays inside the width.

```markdown
This repository runs the AgenticSeal process on itself: work items under
```

```seal
verdict: fixed bc092878b
answer: The finding holds. `CONTRIBUTING.md:58` now says the repository runs the AgenticSeal process on itself, in bc092878b, and *Scope* item 4 of `frame/design.md` names the line.
```

### 2. `lib/core.py:14` restates the opt-in fact that `lib/optin.py`'s renamed docstrings state, and keeps "runs the workflow"; nothing in the records names it

```seal
severity: should
location: `lib/core.py:14`, `tests/lib/test_core.py:219`, `tests/skills/test_seal_stamp.py:1564`, `seal/threads/1794986401-the-process-has-no-name/gaps.md:13`
evidence: executed `git grep -n -i -E 'run(s|ning)? the (agenticseal )?workflow|into the workflow|in the workflow|outside the workflow|the workflow off|AgenticSeal workflow' -- . ':!seal/threads'`; read `lib/core.py:13-15`, `lib/optin.py:326-331`, `tests/lib/test_core.py:216-219`, `tests/skills/test_seal_stamp.py:1563-1564`
```

Why it matters: issue #1557 *Change* item 4 names its class: "The texts
that say whether a repository runs the process". The change renamed that
fact in `lib/optin.py`: `opted_in` now reads "True when this repository runs
the AgenticSeal process" (`lib/optin.py:331`), and `home` reads the same
way (`:326`). `lib/core.py:13-15` cites that function and restates its
fact: "the root is what says the repository runs the workflow
(`optin.opted_in`)". Two case docstrings state the same fact the old way:
`tests/lib/test_core.py:219` ("the root is what says the repository runs
the workflow") and `tests/skills/test_seal_stamp.py:1564` ("the root only
while the repository runs the workflow"). `skills/implement/SKILL.md:90`
says it too, and stays by the frame's *Out* list for `skills/`.

`skills/core/SKILL.md` *The rule a mechanism is kept against* has a change
remove, in the same commit, what stood on the old fact: "a check, an
exception, a comment, a copy". The frame's *Scope* does not name
`lib/core.py` or the two cases. Its *Out* list does not name them either,
since they sit outside `docs/`, `skills/` and `agents/`. And `gaps.md:13`
*Not done* names what keeps the word only "in `docs/`, `skills/` and
`agents/`". So the pull request body, which quotes that line, tells the
sealer and a reader that nothing else keeps it.

The search is a sample by wording (contract rule 12): it lists the
spellings of the opt-in sentence found in the files above, and a sentence
stating the fact in other words is not reached by it. The fix renames the
three lines. The `lib/core.py` paragraph is refilled because the name makes
its line longer than the file's 76 columns.

```markdown
**A session in a repository with no `seal/` root receives nothing**: the
root is what says the repository runs the AgenticSeal process
(`optin.opted_in`), and a session doing other work pays for no core.
```

```python
        the marker, a directory outside git and a cwd not given each receive
        nothing: the root is what says the repository runs the AgenticSeal
        process."""
```

```python
        """`seal/` under a worktree is the root only while the repository
        runs the AgenticSeal process; the throwaway marker takes it back."""
```

The snippets reach the three lines in `lib/` and `tests/`. Where the fix
pass keeps any of them instead, `gaps.md:13` owes a sentence naming it,
since the line as it stands names only the three directories.

```seal
verdict: fixed bc092878b
answer: The finding holds. `lib/core.py:14`, `tests/lib/test_core.py:219` and `tests/skills/test_seal_stamp.py:1564` use the name in bc092878b, and *Scope* item 4 names them. `gaps.md` *Not done* now says the remaining test docstrings keep the word and that the list is a sample found by wording.
```

### 3. `frame/design.md` reports two searches at `c637848af` that print otherwise, and *Removes* says no copy stands on "the workflow" while a test comment names the README row by its old label

```seal
severity: should
location: `seal/threads/1794986401-the-process-has-no-name/frame/design.md:62`, `seal/threads/1794986401-the-process-has-no-name/frame/design.md:42`, `tests/behaviour/test_chain_hooks_hardening.py:415-419`
evidence: executed `git grep -n -i 'the workflow' c637848af -- tests | wc -l`, `git grep -n -i workflow c637848af -- README.md skills/core/SKILL.md lib/optin.py .claude-plugin templates/setup/hygiene.yml templates/setup/seal-README.md seal/README.md CLAUDE.md docs/layout/one-root-by-lifetime.md | wc -l`, `git grep -n 워크플로 c637848af -- README.ko.md docs/layout/one-root-by-lifetime.ko.md | wc -l`; read `tests/behaviour/test_chain_hooks_hardening.py:415-419`, `README.md:389`, `README.ko.md:387`
```

Why it matters: *Removes* at `frame/design.md:62` claims "No copy, reader
or check stands on "the workflow" (executed: `git grep -n -i 'the workflow'
-- tests`, two lines, ...)". At `c637848af`, the commit *Grounding* dates
the frame to, that search prints 106 lines, not two. Most of them name a
GitHub Actions workflow. Three name the process. Two are the docstrings of
finding 2. The third is the comment at
`tests/behaviour/test_chain_hooks_hardening.py:415-419`. It lists "the
name each place that reaches the network carries in the READMEs' passage",
and among them "the workflow's own steps". The change renamed that row's
label to "the AgenticSeal process's own steps" (`README.md:389`) and
"AgenticSeal 프로세스 자체의 단계" (`README.ko.md:387`). So the comment
names a README row by a label neither README carries any more. The branch
already edits this file at `:775`.

S2 at `frame/design.md:42` claims "Run at `c637848af` (executed), the two
searches printed 58 lines." They print 64, 48 and 16. The line lists G2 and
S2 give are consistent with 64: 39 process lines and citations, plus 27
kept lines, less the two rows counted in both (`README.md:383` and
`README.ko.md:380`). The lists are right, and the total is not.

The fix renames the comment's name for the row, and corrects the two frame
sentences.

```python
# The name each place that reaches the network carries in the READMEs' passage,
# spelt alike in both editions: `/agentic:update`, `seal cost --post`, the
# chain arm of `seal gate`, `seal settle`, the AgenticSeal process's own steps
# (which open the pull request with `gh pr create`), and the checks
# `seal pr-checks install` writes.
```

```markdown
  why: the work replaces a word at each place G2 lists and adds one definition paragraph per README and one clause to the core. No reader or check stands on "the workflow" (executed: `git grep -n -i 'the workflow' -- tests`, 106 lines at `c637848af`). Each line names a GitHub Actions workflow, except the heading at `tests/text/test_every_agent_reads_the_contract.py:139`, which *Scope* item 3 updates, and three comments or docstrings that call the process "the workflow", `tests/behaviour/test_chain_hooks_hardening.py:417`, `tests/lib/test_core.py:219` and `tests/skills/test_seal_stamp.py:1564`, which the build renames.
```

In `frame/design.md:42`, "the two searches printed 58 lines" becomes "the
two searches printed 64 lines". The *Removes* snippet assumes the fix pass
renames the two docstrings of finding 2. Where it keeps them, the sentence
names them as kept instead.

```seal
verdict: fixed bc092878b
answer: The finding holds. In bc092878b S2 counts 64 lines, 48 and 16, and *Removes* gives the 106 lines, names the two that held an old label, and says *Scope* item 4 updates both. The comment at `tests/behaviour/test_chain_hooks_hardening.py:415-419` now names the row as the AgenticSeal process's own steps. `frame/plan.md` *Judgments of the run* records the fold.
```

### 4. The phase says every paragraph whose lines grew past their width was refilled, and six lines the build lengthened stand past 76 columns

```seal
severity: should
location: `seal/threads/1794986401-the-process-has-no-name/trail/phases/phase-1.md:6`, `lib/optin.py:25`, `lib/optin.py:315`, `lib/optin.py:326`, `seal/README.md:18`, `templates/setup/seal-README.md:18`, `skills/settle/SKILL.md:449`
evidence: executed `git diff -U0 fab41dc91...083fd5d74 -- . ':!seal/threads'`, measuring the display width of each added line; read `lib/optin.py:22-27`, `lib/optin.py:312-316`, `seal/README.md:17-19`, `skills/settle/SKILL.md:446-450`
```

Why it matters: `trail/phases/phase-1.md:6` claims "The paragraphs whose
lines grew past their width were refilled at 76 display columns, or 80 for
Korean prose". The Korean lines hold, all at 80 or under. Six English lines
the build lengthened were not refilled. `lib/optin.py:25` is 85 columns,
`:315` is 83 and `:326` is 88. `seal/README.md:18` and
`templates/setup/seal-README.md:18` are 82 each, and
`skills/settle/SKILL.md:449` is 84. `tests/behaviour/test_docs_line_wrap.py`
holds its files to 88 columns and passes, and ruff selects no line-length
rule, so no gate is red. What is wrong is the sentence: the sealer reads the
phase record as the build's account, and this sentence tells it the wrap was
handled everywhere. The `seal/README.md` template is the one that first
setup writes into every user's repository.

The fix refills the six lines. The phase sentence then holds as written.
`seal/README.md` and `templates/setup/seal-README.md` take the same text.

```markdown
It lives at one of two places, and its presence at either, with this file's
first line as it stands, is what opts the repository into the AgenticSeal
process. There is no config key. **Shared mode** keeps
```

```python
in the root would silence every gate in every clone with nothing in the diff
that read as the AgenticSeal process being switched off. Nothing under
`.git/` can be committed, and a linked worktree shares the common directory,
so it shares the opt-out. `seal/README.md` says so too.
```

```python
    # so a directory created where the opt-out goes would turn every
    # gate off with nothing in the diff that reads as the AgenticSeal
    # process being switched off.
```

```python
    """This repository's `seal/`, or "" when it does not run the AgenticSeal
    process."""
```

```markdown
and at which step, as `skills/core/SKILL.md` *The first value: efficient
development through the AgenticSeal process* states, in that pull request
or a later one, and nothing is cut to fit.
```

The `skills/settle/SKILL.md` refill keeps the citation broken across a
line, which `tests/behaviour/test_a_cited_section_stands_in_its_file.py`
reads across line breaks, as it does at the three citations the phase
moved.

```seal
verdict: fixed bc092878b
answer: The finding holds. The six lines are refilled within 76 columns in bc092878b, and `trail/phases/phase-1.md` says round 1's fix pass refilled them. The phase's cases and the two modules round 1 named pass, 476 cases (executed), and `uvx ruff check` and `uvx ruff format --check` pass on the changed Python files (executed).
```

## Confirmations

What matched: *Data & interfaces* D1, read against `README.md:23-28`. The
paragraph names everything the opening paragraph describes, from the
routing question to the sealer's guarantee, as the AgenticSeal process, and
says the diagram draws it. It tells another repository to point at it by
that name, says the name is not translated, keeps *seal* to the last
agent's guarantee, and keeps *the review chain* to the review rounds. The
stamp it calls a drawing of the seal is the one `README.md:169-171` has the
`Stop` hook draw.

What matched: D2, read against `README.ko.md:25-30`. It gives "AgenticSeal
프로세스", says the name is not translated, and names "도장 체인" and "인장
과정" as renderings not to use. The 도장 it calls a drawing of the seal in
the terminal is the one `README.ko.md:173-174` has the `Stop` hook draw.

What matched: D3, read against `README.md:8-9`, `README.ko.md:8-9`,
`.claude-plugin/plugin.json:5` and both descriptions in
`.claude-plugin/marketplace.json:3` and `:11`. The three descriptions carry
the tagline verbatim, as `tests/behaviour/test_chain_hooks_hardening.py:176-181`
requires.

What matched: D4 and D5, read against `skills/core/SKILL.md:18-51`. The
opening sentence is D4 word for word. The heading is D5's, the first bold
sentence says "through a process of agents", and every later place uses
the full name. `skills/core/SKILL.md:112-113` now says "GitHub Actions
workflow". The core is 9,476 bytes at the target and 9,322 at `c637848af`
(executed: `wc -c`), the 154 bytes the phase reports.

What matched: S2. Both searches were run at the target (executed). Each
line they print names a GitHub Actions workflow, its file, its run or the
`${{ github.workflow }}` expression: `README.md:11`, `:187`, `:225`,
`:230`, `:389`, `:390`; `README.ko.md:233`, `:387`;
`skills/core/SKILL.md:113`; `seal/README.md:33` and its template;
`templates/setup/hygiene.yml:7`, `:23`, `:43`, `:46`; and the six lines
each of `docs/layout/one-root-by-lifetime.md` and its Korean edition.

What matched: G3 and the phase's count of the heading's citations. A
search across line breaks over every tracked file outside `seal/threads/`
finds one match at the target, `tests/github/test_release_completeness_check.py:436`,
a docstring about a GitHub Actions workflow (executed: a Python
`re.finditer(r"through\s+(#\s*)?the\s+workflow")`).

What matched: S3, S4 and the phase's count of cases. The phase's six
modules pass, 271 cases (executed), and ruff check and ruff format pass on
the three Python files the branch changes (executed). The version search
prints nothing, exit 1 (executed), and `.claude-plugin/plugin.json:4`
reads `0.38.3`.

What matched: G7. `changelog.md` ends with `### Process changes`, with one
row for `skills/core/SKILL.md` and one for `CLAUDE.md`, the two files of
the list at `docs/layout/the-record-layout.md:52` that the diff changes.

What matched: G9. `skills/implement/SKILL.md:72` has a work item whose
subject is the policy root's text edit the policy root directly in its
pull request. The row of `docs/layout/one-root-by-lifetime.md:84` and its
Korean edition is that text, and the change moves no section, so no
unsettled design needs re-pointing.

What matched: the plan's judgment that the prompt budget is zero.
`CONTRIBUTING.md:389-391` defines a prompt budget as the times a change
puts a question in front of a person, and this change adds none.

What matched: `pr.md`. Each of its seven quotes stands word for word, runs
of whitespace collapsed, at the source its coordinate names (executed: a
Python comparison of each quote with its file). The sources say what the
quotes say at the target.

The rest of each record holds at the target. `routing.md` names the branch
and the base, and its version paragraph matches the diff. `frame/plan.md`
names the phase's commit `61c98fac8`, which the branch carries.
`frame/questions.md` leaves no row open. The phase's other claims hold,
apart from the one finding 4 names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a reader in another repository takes the name from the two paragraphs without translating it. This round read the paragraphs against D1 and D2, and they say what those require; no reading here can stand for that reader | `README.md:23-28`, `README.ko.md:25-30` | the owner, in the repository that documents the plugin |
| The full suite, the repository-wide lint and the format check, the `Broad gate` key of `seal/config.json`, at the work item's HEAD. The label `unverified` in `gaps.md` is honest: nothing in the records claims the broad gate ran | `seal/config.json` | the orchestrator, once the review rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_release_hygiene.py tests/text/test_every_agent_reads_the_contract.py tests/lib/test_optin.py -q` | exit 0, 271 passed, 5 warnings, none naming this work item |
| `uvx ruff check` and `uvx ruff format --check` over `lib/optin.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/text/test_every_agent_reads_the_contract.py` | exit 0 each |
| `git grep -n -i 'the workflow' c637848af -- tests` | 106 lines; three name the process, the rest a GitHub Actions workflow |
| the two S2 searches at `c637848af` | 48 and 16 lines |
| `git grep -n -F '0.38.2' -- . ':!seal/threads'` at the target | exit 1, no line |
