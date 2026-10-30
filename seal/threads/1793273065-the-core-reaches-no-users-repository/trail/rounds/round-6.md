# Review round 6: 1793273065-the-core-reaches-no-users-repository

target: f0c4aff2 against origin/release/v0.25.0

This round is round 1 of the count. The frame was reframed after round 5,
from A1 (the preset block's `@` line) to A5 (a plugin `SessionStart` hook
that prints the core), at `85e61e11`. The foot of `frame/design.md` reads
`Reframed 2026-10-30 by framer, after round 5.` Under
`docs/the-review-record.md` *The run*, the first finding round that reviews
new work starts the count again at one, whatever the record's number. Round
5 closed nothing `fixed` or `rejected`, so this round owes it no line that
confirms or reopens a close.

Rounds 1 to 5 reviewed the A1 build. This round carried their coordinates
and none of their verdicts. Round-1#1 and round-2#1 closed the core's
routing sentence as it stood at `3c43b42e`. Phase 8 rewrote that sentence,
so their closes do not cover the text at HEAD, and finding 3 reads it again.
Round 1's diff of the old `CLAUDE.md` against the core and its reading of
the one-line block both judged A1 text that phases 5 to 10 replaced. This
round did not carry them. Rounds 4 and 5 confirmed the `.test_durations`
refresh of `a63a9b4a`. The orchestrator refreshes that file after these
rounds, so this round neither carried nor re-established it. The
coordinates this round did carry: `skills/implement/orchestration.md:102`
for the routing question's place in the batch, and
`hooks/routing-edit-gate.py` as the gate that holds it.

## Findings

### 1. The core's new scope sentence reads as taking one source, rewrite in place and "do not avoid the change" off everything but the plugin's gates, checks and hooks

severity: should
location: `skills/core/SKILL.md:99-102`, `seal/threads/1793273065-the-core-reaches-no-users-repository/frame/design.md:224-231`
evidence: read `skills/core/SKILL.md:97-114`, `CONTRIBUTING.md:378-382`, `CLAUDE.md:18-23`, `seal/threads/1793273065-the-core-reaches-no-users-repository/frame/design.md:224-232`
verdict: open

Every session and every agent reads the core, and it ranks above every
skill. Phase 8 added this sentence to *The rule a mechanism is kept
against*, right after the section's bold lead: "This rule governs this
plugin's own gates, checks and hooks; a user's repository keeps or drops its
own by its own policy." The sentence can be read two ways, and both readings
change what the core decides.

First, "This rule" can mean the whole section. The section's heading calls
everything under it "the rule", and so does `CLAUDE.md:18-21` ("the rule
`skills/core/SKILL.md` *The rule a mechanism is kept against* states"). The
sentences after the new one are not about whether a mechanism stays: a fact
has one source, a script blocks only on a fact it reads exactly, do not
avoid the change a problem calls for, a change rewrites the text it amends
in place, history goes to git. Read with "This rule" as the section, all of
those now govern only the plugin's gates, checks and hooks. They no longer
govern a skill's prose, a record, or a user's code. Contract rules 19 and 20
restate two of them for agents. The orchestrating session receives no
contract, though, and for it the core is the only carrier.

Second, even read as the bold lead alone, "gates, checks and hooks" is
narrower than the mechanisms this repository keeps against the rule.
`CONTRIBUTING.md:378-382` lists "a mechanism (a gate, a checker, a hook, a
CI step, a rule)" and cites this section as the reason. Under the new
sentence, a CI step or a rule of the plugin is no longer kept against the
record of what it caught. The old core put no such limit on it.

The frame says (*Scope* item 10, *Whose mechanisms*, `frame/design.md:224-231`)
that the sentence scopes the keep test by owner. "Existing is no reason to
keep it" must not let a crafter remove a user's guard. It also says these
sentences "change how the core is read, not what its values decide". The
owner's choice it records was between this plugin's mechanisms and every
mechanism the workflow adds. It was not about which kinds of the plugin's
mechanisms count. The build copied the frame's apposition "its gates,
checks and hooks" as a closed list and put "This rule" where the section
heading's antecedent is nearest. So the defect is in the frame's wording,
and the build carries it. The fix scopes the keep test, names it as the
keep test, and lists the kinds as examples. The orchestrator folds the same
wording into *Scope* item 10.

```markdown
**A mechanism stays only while its record of what it caught outweighs what
it costs**; existing is no reason to keep it. This test of whether a
mechanism stays governs this plugin's own mechanisms, a gate, a check, a
hook, a CI step or a rule among them; a user's repository keeps or drops
its own mechanisms by its own policy. A fact has one source, and every
other place links to it.
```

answer:

### 2. The core's sentence on what stays a script now names four scripts instead of the class "what a script answers exactly"

severity: should
location: `skills/core/SKILL.md:42-44`
evidence: executed `git diff 6ebfada5 f0c4aff2 -- skills/core/SKILL.md`
verdict: open

At `6ebfada5` the sentence was a rule over a class, with four examples:
"What a script answers exactly, the suite, the lint, the broad gate, the
merge check, stays a script, and the session waits on its exit code rather
than reasoning about what it would print." At HEAD it is a closed list:
"The suite, the lint, the broad gate and the merge check answer exactly and
stay scripts, and the session waits on their exit code rather than
reasoning about what they would print." Two directives now reach those four
scripts alone. One is "stays a script". The other is "waits on its exit
code rather than reasoning about what it would print". Other scripts answer
exactly too: `seal core`, which this work adds and which
`skills/implement/orchestration.md` step 1 has the orchestrator run before
its first edit, `chain_check.py` and `seal rules --check`. The core no
longer says that a session waits on their exit codes. The bold lead,
"a script answers the rest", keeps that a script answers. It does not keep
the second directive.

`frame/design.md` *Scope* item 9 (`:198-205`) asks the refactor to keep
"every directive". Item 11 lists each rewrite the owner asked for, and this
sentence is not among them. The behaviour suites S11 names did not run for
the proofer or the crafter (`gaps.md` *Not verified*). So this reading of
the diff is the one check of what the sentence still decides. The fix
restores the class and keeps the examples, at about the old length.

```markdown
command wrote or what a real parser returns. What a script answers
exactly, such as the suite, the lint, the broad gate and the merge check,
stays a script, and the session waits on its exit code rather than
reasoning about what it would print.
```

answer:

### 3. Phase 8 put a pronoun back into the routing sentence's middle clause, the two-way reading round 2 finding 1 fixed

severity: should
location: `skills/core/SKILL.md:84-88`, `tests/text/test_review_axes.py:102-133`
evidence: executed `git show 3c43b42e -- skills/core/SKILL.md`, `git diff 6ebfada5 f0c4aff2 -- skills/core/SKILL.md tests/text/test_review_axes.py`
verdict: open

Round 2 finding 1 found the routing sentence two-way. After "The routing
question is one of that batch", the nearest noun to a following pronoun is
"that batch". Read that way, the routing section states how the whole batch
is put, which `skills/implement/orchestration.md:102` and
`skills/implement/SKILL.md` *1.* contradict. The fix `3c43b42e` named the
question in every clause: "the orchestrating session puts the routing
question as …", and round 3 confirmed it. Phase 8 (`769a1413`) rewrote the
clause as "and the orchestrating session puts it as
`skills/implement/orchestration.md` *Orchestrator: how the work is routed*
states". That is the same pronoun after the same noun. *Scope* item 11 asks
phase 8 to rewrite a sentence that reads two ways, and here it made one.

`tests/text/test_review_axes.py#test_the_core_names_where_the_routing_question_is`
pins the last clause ("refuses the first edit until the routing question is
answered") but not the middle one. That is why the suite stayed green.
Phase 8 changed only the split marker in that case. This is a unit a build
phase made, so it takes no `regression:` line. Round-2#1's close covered the
text at `3c43b42e`, not this text. The class is a pronoun whose nearest
antecedent is the batch rather than the question. In the paragraph at HEAD
this middle clause is its one instance. "its question" in the sentence
before refers to "the design that asks", and the last clause names the
question.

```markdown
first* states with its reasoning. The routing question is one of that batch,
and the orchestrating session puts the routing question as
`skills/implement/orchestration.md` *Orchestrator: how the work is routed*
states; in a repository opted in by its `seal/` root,
`hooks/routing-edit-gate.py` refuses the first edit until the routing
question is answered.
```

```python
    assert "the orchestrating session puts the routing question as" in paragraph, (
        "the core's middle clause names its question by a pronoun, which can "
        "read as the whole batch (round 2 finding 1)"
    )
```

The assertion is red against HEAD, which reads "puts it as" at
`skills/core/SKILL.md:85`.

answer:

### 4. The frame's grounding cites a scratchpad path that spells a real user's home directory, and the census that guards the house rule does not read that spelling

severity: should
location: `seal/threads/1793273065-the-core-reaches-no-users-repository/frame/design.md:42`, `tests/censuses.py:898-935`
evidence: executed `python3 -c "import sys; sys.path.insert(0, 'tests'); import censuses as c; print(c.real_identifiers('seal/threads/1793273065-the-core-reaches-no-users-repository/frame/design.md'))"`, `git grep -n -E -- "-Users-[A-Za-z]"`, `git log -S"core-draft/SKILL.md" --oneline`
verdict: open

`frame/design.md:42`, the grounding row for the owner's refactor decision,
names the draft at a session scratchpad path. That path spells a real
user's home directory in the dashed slug Claude Code gives a projects
directory, `-Users-<name>-Documents-GitHub-SpecSeal`, followed by a real
session id. `4d436388` added it. `CONTRIBUTING.md` *House rules*,
**No real identifiers**, says fixtures and docs use `/Users/x/` only,
because an inlined real path is "the leak that forces a rewrite of the
repository's history". The squash merge carries this line into `main`'s
history. The settle that later removes the work item's directory does not
take it out of that history.

The `real_identifiers` census returns nothing for the file (executed): its
`USER_PATH_RE` reads only a user path written with slashes. The tree's own fixtures already
spell the slug form with the fixture user, `-Users-x-repo`
(`tests/conftest.py:1528`, `tests/hooks/test_press.py:120`). So the slug is
a spelling of a user path that the house rule covers and the census misses.
`git grep` over the branch finds the real slug in this one line and the
fixture slug everywhere else. The fix rewrites the line. It also teaches the
census the slug spelling, so the next one is refused in CI rather than by a
reader.

```markdown
<!-- frame/design.md:42, the path only -->
A draft at `<scratchpad>/core-draft/SKILL.md`, in the orchestrating session's scratchpad, is 5,518 B
```

```python
# A projects directory spells the path its session started in with dashes,
# `-Users-<name>-<repo>`, so a user path reaches a record that way too.
# Built from two halves, like USER_PATH_RE. The name is word characters, so
# a placeholder such as `<name>` or a pattern such as `[A-Za-z]` is not one.
SLUG_USER_RE = re.compile("-" + r"Users-([\w.]+)-")


def refused_user_paths(line):
    """The match of every user path in `line` outside the fixture one, in
    order, written with slashes or as a projects directory's dashed slug;
    `refused_domains` says who else reads it."""
    return [
        m
        for m in USER_PATH_RE.finditer(line)
        if not m.group(0).startswith(ALLOWED_USER_PATH)
    ] + [m for m in SLUG_USER_RE.finditer(line) if m.group(1) != "x"]
```

Precondition: the slug pattern assumes the user name holds no dash. A name
that holds one is still matched at its first part. This record's own
`-Users-<name>-` and `-Users-[A-Za-z]` do not match it.

answer:

## Confirmations

confirms: none
Phase 8's removal of the core's list of its source documents keeps the rule
(the orchestrator's second question). At `6ebfada5` the core named "the
policy root, the work item's design, then the issue" after citing
`skills/implement/SKILL.md` *1. Read the documents that outrank the code
first* for the order. That section states the order with its ranks at
`skills/implement/SKILL.md:141-145`: policy (`docs/`), the SDD set, the
ticket, existing code, and the original between the ticket and the code
where a migration config exists. So the list was a copy, and an incomplete
one, since it left out the code and the original. The core at
`skills/core/SKILL.md:66-69` still says which documents are source
documents ("this file and the ones that outrank the code") and where their
order is. The orchestrator worried that an agent that does not open the
section would no longer read the order. Each party reaches the order
without the core's copy (read). The crafter is told to follow `implement`
"the precedence" (`agents/crafter.md:27`). The framer opens section *1.* by
name (`agents/framer.md:53`). The proofer's `code-review` stage 1 puts
`docs/` before the SDD set (`skills/code-review/SKILL.md:23`). Every agent's
contract rule 3 ranks a prompt where a ticket ranks, above the code and
below the ratified documents (`skills/agent-contract/SKILL.md:53`). The
orchestrator works from `skills/implement/SKILL.md`, which
`skills/implement/orchestration.md:11` names as its other half. Under the
core's own "a fact has one source", the citation is the form the rule asks
for. A copy that already disagreed with its source by two ranks was the
risk.

confirms: none
`skills/verify/scripts/core_check.py#_normal` cannot pass a session whose
context does not hold the core whole (the orchestrator's third question).
Read `:76-77` and `:181-186`. The function changes two things. It turns
each run of `\r` that ends in a `\n` into one `\n`. Then it strips the
trailing `\r` and `\n` characters, and nothing else. Two texts with equal
normal forms therefore differ only in how many carriage returns stand before
each newline, and in the line-ending characters at the very end. `judge`
applies it to both sides of each comparison: `content` against `stdout` at
`:213`, and the body against the file below its frontmatter at `:237`. So
`content` equals the file in every character outside line endings. A
preview past `CAP` holds about 2,400 characters of a 6,180-character output
(design *Grounding*, probe S), so it still fails. A lone `\r` inside a line
is not touched, and neither is a missing last line. The digest is still
taken over the file's bytes and compared with the header (`:230-235`), not
with `content`. The folded *Scope* item 3 (`frame/design.md:110-112`) states
what the code does. CI run 40989182473 failed six cases on Windows, all in
`tests/skills/test_core_check.py` (executed, *Probes*), which is the set
phase 8 names. The two new cases write the scratch core with `write_bytes`,
so they are red on any platform before the fix, and the phase record shows
each half of the fix killed by `seal mutate`. The failure message for a
`content` mismatch still says "past about 10,000 characters the context
holds a preview". For a mismatch with another cause, such as a harness that
trims differently, it gives a wrong reason. This round judges that no
finding, because the check still fails closed.

confirms: none
The rest of the core's rewrite decides what the old core decided (S12, read
sentence by sentence, `git diff 6ebfada5 f0c4aff2 -- skills/core/SKILL.md`,
executed). Findings 1 to 3 are the exceptions. The `##` headings and the
frontmatter are unchanged. The five invariants are word for word the same.
Each rewrite *Scope* item 11 lists is in place: "by buying time and
stability", "the most expensive step" with "the design that asks argues
why its question is worth that cost", "reads exactly, such as an exit code
or a parser's result" with "reported, never used to block", "its record of
what it caught outweighs what it costs". "nothing comes back mid-run" now
stands only in the fifth invariant, as item 11 asks. The `#1167` pointer
is gone. The `CONTRIBUTING.md` sentence moved to `CLAUDE.md:18-23`, with
both section names. These dropped clauses decide nothing on their own:
"already" before "gate a pull request", "is a relay", "to judge in the
direction this project wants", "one more" before "grammar rule". The same
holds for the records clause "how one agent understands another's work, not
a theory the next one is asked to adopt". Its directive, read them as
claims and reach your own result, stays at `:52-53`, and so does its
reason, that a mistake does not pass through unread. The opening paragraph
(`:18-23`) states where the core applies and whose paths it cites, as item
10 asks. The exception for `seal/`, recorded in `gaps.md`, is needed
because the core cites `seal/threads/` in the session's repository. The
clause "in a repository opted in by its `seal/` root" matches what the gate
does (`skills/implement/SKILL.md:201-204`). "a command run by the owner of
the repository whose release made the judgments" names the owner item 10
names. No sentence names this plugin's own repository.

confirms: none
The hook matches *Scope* item 2 and *Data & interfaces* (read
`hooks/lib/core.py:1-123`, `hooks/core-start.py:1-47`, `hooks/hooks.json`,
`hooks/dispatch.py` `GROUPS`). `session-core` is a group of its own. The
`SessionStart` entry has the matcher `startup|clear|compact` and the
two-interpreter command of its neighbours. `origin` returns the tree's core
only where the top level's manifest `name` equals the running plugin's and
the core file is there. A missing core prints `MISSING`. `parse` is anchored
at both ends, so a path holding a comma parses. The narrow run over the
hook, check, meter, update, axes, contract, paste and dispatch modules
passed 199 (executed, *Probes*).

confirms: none
Item 12's cases pin both halves (executed, *Probes*; phase 8's record says
the build crafter left no red run on record). With `core.py#output`
printing the whole file, `Test_output::test_accepts_the_header_then_the_files_body_under_its_digest`
and `Test_module::test_the_trees_core_stays_under_the_harness_cap` failed.
With `core_check.py#judge` comparing the whole file,
`Test_judge::test_accepts_the_body_below_the_frontmatter_and_refuses_the_whole_file`
failed. Each mutation was made with the `Edit` tool in this round's clone
and undone the same way. `git status` was clean after.

confirms: none
Nothing of A1 that A5 retires stands outside the records (executed,
*Probes*). A `git grep` for the preset block, `preset-setup`, `install.sh`,
`uninstall.sh`, `claude-md-block`, the `@` line, `/memory`, the
marketplace clone and `@skills/core` found these hits outside `seal/`, and
nothing else:

- the update step that takes the block out (`skills/update/SKILL.md:122-200`);
- the README's sentences on that step, both editions;
- the template's own test module, which asserts the three files are gone;
- `payload_meter.py`'s import rows, which plan D1 keeps;
- `README.md:266`, which says `/memory` does not list the core;
- one historical comment, `tests/behaviour/test_first_setup_asks_once.py:788`.

Every *Removes* row's file is gone or changed in the diff stat. The four
`from:` texts of *Rule changes* are found in their documents with the
whitespace normalised (executed), so the settle can apply them. No file
under `docs/` changes in the branch.

confirms: none
Update step 4 matches *Scope* item 4 (read `skills/update/SKILL.md:122-200`).
It handles both marker pairs. It backs up to `CLAUDE.md.bak` before
writing. A start marker with no end marker exits 1 and changes nothing. A
project's `CLAUDE.md` is named under *Needs action* and not edited. The
user's file is `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md`. Its output
table states the two facts the step opens with. The meter's session table
matches *Scope* item 6 as folded at `f0c4aff2`. A tree with no core gets a
0-byte `missing` row, and every session figure is labelled estimated (read
`skills/verify/scripts/payload_meter.py` `session_composition` and
`_session_lines`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `f0c4aff2`. Contract rule 2 keeps them from this round, and the stale `trail/gate.md` and `guarantee.md` are the orchestrator's to re-run | the tree | the orchestrator, through `seal gate` |
| The Windows leg on `72c1a3ee`'s fix. No `tests` run has read the branch since `df5ba5f1`. The two new cases are platform-independent, but the six that failed have not run on Windows against the fix | `tests/skills/test_core_check.py` | the orchestrator, from the next CI run on the pushed branch |
| S11 for the proofer and the crafter, which did not run by the owner's decision of 2026-10-30, and whether the core caused the framer's rise in tokens read under rule 5. This round's reading is the S12 stand-in the decision names. It cannot say what a suite would have measured | `seal/threads/1793273065-the-core-reaches-no-users-repository/gaps.md` *Not verified* | the orchestrator, on #1038 as `gaps.md` names |
| `frame/questions.md` Q2 (an interactive session on an installed 0.25.0 holds the core once, and `/agentic:update` from 0.24.2 leaves an empty pair) and Q3 (`seal core` under `--bare`) | `frame/questions.md` | the owner after the release (Q2); anyone with an `ANTHROPIC_API_KEY` (Q3) |
| Whether findings 1 to 3, if fixed, need S11 run again. Each changes a sentence of the core after the commit S11's two runs read | `skills/core/SKILL.md` | the orchestrator |
| Round 1's carried row on the three-fix stop for an orchestrating session, which the core still does not state. Round 1's rows on the symlinked user `CLAUDE.md` and on update under `CLAUDE_CONFIG_DIR` concerned the A1 line and the block's install; step 4 now reads `CLAUDE_CONFIG_DIR`, while steps 1 to 3 still read `~/.claude/plugins/` (`skills/update/SKILL.md:46`, `:61`, `:81`) | `skills/update/SKILL.md` | the owner at #1148 (the three-fix stop); the orchestrator (the update paths) |
| This round's spawn context held a `CLAUDE.md` for this repository whose text is the A1 one, while the checkout at `f0c4aff2` holds the A5 text. That fits round 1's reading that a spawn receives the parent session's file as it stood at that session's start. It did not change what this round read, since this round opened the tree's files | the harness | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/hooks/test_core.py tests/hooks/test_core_start.py tests/skills/test_core_check.py tests/skills/test_payload_meter.py tests/behaviour/test_the_old_block_leaves_through_update.py tests/text/test_review_axes.py tests/text/test_every_agent_reads_the_contract.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_the_rules_claude_md_names_have_one_home.py tests/hooks/test_dispatch.py` at `f0c4aff2` | exit 0, 199 passed |
| `hooks/lib/core.py#output` edited to print the file whole, then `bin/test -q -p no:xdist tests/hooks/test_core.py tests/skills/test_core_check.py tests/hooks/test_core_start.py`; edit undone | exit 1, 2 failed: `test_accepts_the_header_then_the_files_body_under_its_digest`, `test_the_trees_core_stays_under_the_harness_cap` |
| `core_check.py#judge` edited to compare the file whole, then `bin/test -q -p no:xdist tests/skills/test_core_check.py`; edit undone | exit 1, 1 failed: `test_accepts_the_body_below_the_frontmatter_and_refuses_the_whole_file`; `git status` clean after |
| `gh run view 40989182473 --repo MichaelYcJo/AgenticSeal --log-failed`, the `FAILED` and summary lines | Windows group 3: 6 failed, 834 passed, 14 skipped; every `FAILED` line is in `tests/skills/test_core_check.py` (`Test_judge` four, `Test_main` one, `Test_module` one) |
| `python3 -I` matching each *Rule changes* `from:` text against its document with whitespace collapsed | all four found |
| `git grep -n -i` for "preset block", "preset-setup", "install.sh", "uninstall.sh", "claude-md-block", the `@` line, "/memory", "marketplace clone", "@skills/core", outside `seal/` | the hits *Confirmations* lists, and nothing else |
| `python3 -c` calling `censuses.real_identifiers` on `frame/design.md`; `git grep -n -E -- "-Users-[A-Za-z]"` | `[]`; one real slug at `frame/design.md:42`, every other hit the fixture user `x` |
