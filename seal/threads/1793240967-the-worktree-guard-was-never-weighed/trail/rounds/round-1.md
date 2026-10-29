# Review round 1: 1793240967-the-worktree-guard-was-never-weighed

target: 3c49c7cd against origin/release/v0.24.1

This is the work item's first round, so no earlier round has coordinates to
carry, and every fact below was established this round. The diff read is
`1e82fd0a..3c49c7cd`, since 1e82fd0a is the merge base with
`origin/release/v0.24.1`. The implementer's account (the four phase
records, `gaps.md`, the frame's executed claims, the commit messages and the
spawn prompt) was read as claims, and each claim below says what was
claimed and what was found. `seal/parity.md` is not declared, so this round
writes no `original:` line. `seal/config.md` holds no `Record language` row,
so the record is in English.

## Findings

### 1. The pull request deletes a policy document against the layout rule, and one of the two checks the frame says force it does not

severity: must
location: `docs/worktree-guard-spec.md`, `docs/README.md`, `.github/scripts/rules.py:291-303`, `tests/github/test_rules.py:522-529`, `tests/behaviour/test_release_hygiene.py:124-131`, `seal/threads/1793240967-the-worktree-guard-was-never-weighed/frame/design.md:17`, `seal/threads/1793240967-the-worktree-guard-was-never-weighed/frame/plan.md:50-60`, `skills/implement/SKILL.md:75`
evidence: executed `python3 .github/scripts/rules.py --check --root clone`, `python3 skills/settle/scripts/fold_check.py --root clone`
verdict: fixed 2bfa6459

`skills/implement/SKILL.md:75` states the layout rule with no exception:
the policy root "is the baseline, and a pull request does not edit it". The
policy in force is the baseline plus the latest decision of the unsettled
designs' `## Rule changes`. `tests/text/test_settle_reads_before_it_removes.py:221`
pins that sentence. Phase 2 (f528f7a1) deletes `docs/worktree-guard-spec.md`
and its row in `docs/README.md` in this pull request anyway, and the frame's
design also states both removals in `## Rule changes`.

The frame claimed two suite cases force the deletion
(`frame/design.md:17`, `frame/plan.md:50-60`). Only one does. In a scratch
clone at 3c49c7cd with the document and its index row restored from
1e82fd0a, `seal rules --check` exits 1 with 17 refusals, each a `check:`
line naming a test file this work deletes. The fold check exits 0 and
prints "the index docs/README.md names every document". The fold check
refuses an index row only once the document is gone, so that half of the
grounds rests on the deletion it is offered to justify.

The frame also claimed "the suite reads the policy root as it stands". That
is not true of the whole suite.
`tests/behaviour/test_a_cited_section_stands_in_its_file.py:143-176`
already reads the policy in force. It excuses, with a warning, a citation in
the policy root that a pending rule change corrects (its S9, `corrections`
and `excuser`). `.github/scripts/rules.py#unresolved` reads the rule files
as they stand and nothing else. So the conflict is between the layout rule
and one check that does not read the policy in force, and the frame adapted
to the check. `CLAUDE.md` *The rule a mechanism is kept against* asks first
whether the structure should change. The precedent the frame cites,
e391ea04, edited 17 policy documents in its pull request (read,
`git show --stat`). That is an earlier act, not an exception any rule
states. The sibling work item merged at 8de879bc left
`docs/the-routing-check.md` *At the pull request* for its settle, as the
layout rule says.

The fix restores the document, its index row and the exemption
`("docs/worktree-guard-spec.md", "2.50.1")` of
`tests/behaviour/test_release_hygiene.py#VERSIONS_OF_ANOTHER_PRODUCT`. The
check then reads each rule file as the policy in force reads it: a `check:`
line inside a section a pending `remove` takes out at the settle is excused
and named as excused, the way S9 excuses a citation. A case in
`tests/github/test_rules.py` plants a rule file whose `check:` line names a
missing test. With a design under `seal/threads/*/frame/design.md` whose
`remove` names that section, the check exits 0 and names the line excused.
Without that design, the check exits 1. The case is seen red against the
check as it stands. The frame's grounding row, *Scope* In 6, the *Removes*
row and `frame/plan.md` *Why phase 2 deletes a policy document* are
rewritten to the restored document. The README links to the document may
stay removed, since the READMEs are not the policy root.

```python
# .github/scripts/rules.py
# Precondition: a `seal/threads/*/frame/design.md` is read as UTF-8 text, and
# one that does not parse excuses nothing.
RULE_CHANGES = os.path.join(ROOT, "skills", "settle", "scripts", "rule_changes.py")


def pending_removals(root):  # NAME NOT IN TREE -- the reader this fix adds
    """`{path: [(first, last), ...]}`: the line span of every section a
    pending `remove` takes out at the settle. Each design is read through
    `rule_changes.parse` against the policy root
    `hooks/lib/config.py#policy_root` names, and each span through
    `rule_changes.section_lines`, as
    `tests/behaviour/test_a_cited_section_stands_in_its_file.py#corrections`
    reads them."""


def unresolved(root):
    """`(failures, files, lines)`: each refusal in the rule files at `root`,
    as `path:line: heading: why`, and how many rule files and check lines
    were read. A line inside a section a pending `remove` takes out is
    read, and not refused."""
    found, read, files = [], 0, rule_files(root)
    removed = pending_removals(root)
    for path, text in files.items():
        for number, heading, line in check_lines(text):
            read += 1
            if any(a <= number <= b for a, b in removed.get(path, ())):
                continue  # the settle removes this section; `check` names it excused
            for problem in line_problems(root, line):
                found.append(f"{path}:{number}: {heading}: {problem}")
    return found, len(files), read
```

The fix pass may instead weigh the check change as costlier than an
exception to the layout rule. In that case the exception is written into
`skills/implement/SKILL.md:75` beside the sentence it qualifies, and it
names the one check that forces it. The frame's grounding then names one
check, not two. Either way, the layout rule and the tree stop disagreeing.

answer: Holds; the round's fix was taken, not the exception, with one reader rather than a second. The fact that a pending `remove` takes a section out of the policy in force was already read by `tests/behaviour/test_a_cited_section_stands_in_its_file.py#corrections` and the `remove` arm of `#excuser`, inside a test module. 2bfa6459 moves that reading into `skills/settle/scripts/rule_changes.py#pending` and `#removed_by`. The citation case's `corrections` and `excuser` now call them, and so does `.github/scripts/rules.py#unresolved`. So the S9 excuser and the rules check read one fact through one reader. An exception written into `skills/implement/SKILL.md:75` would have added a rule to keep a second reading alive; this change removes the disagreement at its cause. A refused `check:` line inside a section a pending `remove` with no `from` takes out is printed as `seal rules: excused: <path>:<line>: <heading>: <why>; <work item> removes this section at the settle`, and is no refusal. `docs/worktree-guard-spec.md` (`cmp` with 1e82fd0a's bytes, exit 0), its `docs/README.md` row and the `2.50.1` exemption of `tests/behaviour/test_release_hygiene.py#VERSIONS_OF_ANOTHER_PRODUCT` are restored. `bin/seal rules --check` exits 0 with 17 excused in 266 check lines (executed). `tests/github/test_rules.py#Test_main::test_a_refusal_in_a_section_a_pending_remove_takes_out_is_excused_and_named` was red against the check as it stood (executed, exit 1, `assert 1 == 0`). fddec67a adds its `remove` with a `from` arm after `seal mutate` dropping that guard survived; it is red under that mutant now (executed, exit 0, verdict red). `#test_every_check_line_in_the_tree_holds` copies the pending designs into its scratch tree and plants no defect in a file a pending `remove` names. `skills/settle/SKILL.md`, both READMEs' command tables and the `rules.py` docstring state the excuse. The frame lines that still say the pull request deletes the document are the orchestrator's to fold.

### 2. `hooks/lib/cmdline.py` keeps four outputs no reader reads, and the rider on one of them stands only because a check requires a rider in the file

severity: should
location: `hooks/lib/cmdline.py:541-600`, `hooks/lib/cmdline.py:718-813`, `hooks/lib/cmdline.py:815-915`, `tests/hooks/test_cmdline.py:24-60`, `tests/hooks/test_cmdline.py:144-300`, `tests/hooks/test_cmdline.py:349-363`, `tests/text/test_a_rider_reaches_its_file.py:112-117`
evidence: executed `git grep -n -E "command_word\(|strip_subshell\(|_git_options\(|chdirs|split_segments_with_separators" -- hooks skills tests`
verdict: fixed a82da960

`frame/design.md` *Scope* In 3 prunes `hooks/lib/cmdline.py` to what
`hooks/implementer-notice.py` reaches. The prune was name-based, so the
values the guard read inside the kept functions stayed.
`hooks/implementer-notice.py:112-116` reads `parse_git(tokens)[0]` and
nothing else. The search above finds no other caller of these four outputs:

- `parse_git` returns `chdirs`, built by `_git_options` from the `-C`
  positions (`hooks/lib/cmdline.py:851-867`, `:902`, `:915`).
- `command_word` returns whether a segment's directory is `unplaced`.
  Its one caller, `parse_git`, binds it to `_unplaced` (`:891`, `:893`).
- `strip_subshell` returns `opened`. Its one caller, `command_word`, binds
  it to `_opened` (`:738`, `:760`).
- `split_segments_with_separators` keeps the joining operator, and its one
  caller, `split_segments`, drops it (`:560-561`). Its own docstring says no
  caller reads the operator.

`gaps.md` *Not done* claimed three of these and left them "for the review
to weigh". This round weighs them as removals. The guard was their reader,
and `CLAUDE.md` *The rule a mechanism is kept against* has a change remove,
in the same commit, what stood on the old fact. The cases pin behaviour
nobody reads. `Test_split_segments_with_separators` asserts the operators,
`WRAPPED` carries an `UNRESOLVED` or `HERE` placement per runner that
no case now asserts against, and two `Test_parse_git` cases assert an empty
`chdirs`. Two of those cases name the frozen reader's commit 86256492 as
the model.

The rider at `:824-833` describes a gap in `chdirs`, and its own text
says no reader follows `chdirs`. It stays because
`tests/text/test_a_rider_reaches_its_file.py:112-117` asserts a
`# RIDER:` in the file. That file's docstring says "a rider kept after its
fix is the cost this file names", and `hooks/dispatch.py` left the same
tuple when its rider was resolved. Keeping a comment so that a check passes
is the shape contract rule 18 refuses.

The fix removes each output with its cases, the rider with it, and
`hooks/lib/cmdline.py` from the rider tuple. `parse_git` returns
`(subcommand, args)`. `_git_options` returns the index alone. `command_word`
returns the segment alone. `strip_subshell` returns the tokens alone.
`split_segments` holds the scan that `split_segments_with_separators`
holds now, with no operator kept. `WRAPPED` maps a name to its command. The
two cases at `tests/hooks/test_cmdline.py:349-363` assert two-element
tuples and drop the frozen commit from their docstrings.
`tests/hooks/test_cmdline.py`, `tests/hooks/test_implementer_notice.py` and
`tests/hooks/test_dispatch.py` (its `cmdline` parameter) are the narrow
runs.

```python
# hooks/lib/cmdline.py, the tail of parse_git
    word = command_word(tokens)
    if not word or os.path.basename(word[0]) != "git":
        word = command_word(tokens, redirections=True)
        if not word or os.path.basename(word[0]) != "git":
            return None
    rest = word[1:]
    at = _git_options(rest)
    if redirection_width(rest, at):
        again = _git_options(rest, redirections=True)
        if again < len(rest):
            at = again
    if at >= len(rest):
        return None
    subcommand = rest[at].rstrip(")")
    return (subcommand, rest[at + 1 :]) if subcommand else None
```

```python
# tests/text/test_a_rider_reaches_its_file.py
    for rel in (
        "hooks/lib/optin.py",
        "hooks/review-skill-gate.py",
    ):
        assert "# RIDER:" in read(os.path.join(ROOT, rel)), rel
```

answer: Holds. a82da960 makes the four functions return only what `hooks/implementer-notice.py` reads: `parse_git` returns `(subcommand, args)`, `_git_options` the index, `command_word` the segment and `strip_subshell` the tokens. `split_segments` now holds the scan, keeps no operator, and `split_segments_with_separators` is gone. The rider on `chdirs` goes with `chdirs`. `WRAPPED` maps a name to its command, and `Test_split_segments_with_separators` goes with its four `.test_durations` entries. The two `parse_git` cases assert two-element tuples and no longer cite 86256492. The three heredoc cases and the case-pattern case read `split_segments`. Under contract rule 18 the rider check holds: it pins that a file a row named still carries its rider. A file whose rider's gap is gone leaves its list, as `hooks/dispatch.py` did. So `hooks/lib/cmdline.py` leaves the tuple, and the docstring says why. `UNPLACED`'s and `RUNNERS`' comments stop speaking of an unplaced directory. `hooks/lib/cmdline.py` is 844 lines (`wc -l`). `tests/hooks/test_cmdline.py` 19 passed, `tests/hooks/test_implementer_notice.py` 26, `tests/hooks/test_dispatch.py` 49 and `tests/text/test_a_rider_reaches_its_file.py` 8 (executed, each exit 0). A `seal mutate` that drops a segment in the rewritten split is red (executed, exit 0, verdict red). The changelog fragment's line count is corrected.

## Confirmations

confirms: none
The `automation` press reads as before. The spawn prompt asked whether
`hooks/question-gate.py` and `hooks/routing-edit-gate.py` behave as before
against `hooks/lib/press.py`. All 14 definitions in `hooks/lib/press.py`
have the same AST as the same names in `hooks/worktree_consent.py` at
1e82fd0a once docstrings are set aside (executed, an `ast.dump` comparison,
14 of 14 `same`). Each gate calls the same function it called before:
`press.is_routing_question` and `press.last_routing_answer` at
`hooks/question-gate.py:88` and `:108`, and `press.automation_answered` at
`hooks/routing-edit-gate.py:266`. The docstring of `last_routing_answer`
dropped the sentence on `consent`'s catch-all. Neither gate called through
`consent` at 1e82fd0a (read, the diff of both gates), so no catch was lost.
`ruff check --select F` over the two gates, `press.py`, `cmdline.py`,
`implementer-notice.py`, `dispatch.py` and `hooksession.py` finds no
undefined name (executed, exit 0).

confirms: none
Nothing reads a removed module, file or variable. A search for the removed
modules, `session-lease`, the process walk's names, `CLAUDE_PID`,
`CLAUDE_PLUGIN_OPTION`, `SPECSEAL_LANG`, `WORKTREE_GUARD`,
`worktree_guard_language`, `agentic-leases`, `agentic-worktree`,
`worktree-guard`, `tokens.py` and `post-agent` outside the records and the
replay eval prints six lines (executed, `git grep`). They are
`docs/the-routing-check.md:81`, which `## Rule changes` corrects at the
settle, and the generic option reader in
`tests/behaviour/test_chain_hooks_hardening.py:151,166`.
`tests/conftest.py:504` scrubs `CLAUDE_PID` as a variable a session
exports, which stays true. `tests/hooks/test_dispatch.py:1157` asserts
`post-agent` is gone, and `tests/hooks/test_root_migrate.py:927` is
`gaps.md`'s kept rename. `.test_durations` holds no key for any file or
case this work removed. Its one key for a missing file,
`tests/behaviour/test_a_unit_is_bounded_where_a_parser_decides.py`, is
already in 1e82fd0a's copy (executed).

confirms: none
`hooks/dispatch.py:80-101` holds the groups `frame/design.md` *Data &
interfaces* states, and `hooks/hooks.json` lost only the `PostToolUse`
entry for `Agent|Task` (read). The narrow modules pass at 3c49c7cd
(executed, each exit 0). `tests/hooks/test_press.py`,
`tests/hooks/test_question_gate.py` and
`tests/hooks/test_routing_edit_gate.py` give 79 passed.
`tests/hooks/test_dispatch.py`, `tests/hooks/test_cmdline.py` and
`tests/hooks/test_implementer_notice.py` give 98 passed.
`tests/behaviour/test_chain_hooks_hardening.py`, `tests/github/test_rules.py`,
`tests/skills/test_fold_check.py`,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` and
`tests/text/test_a_rider_reaches_its_file.py` give 148 passed.

confirms: none
`gaps.md`'s first divergence row holds. The two moved cases that lost
their `consent` assertions dropped exactly those, 7 to 4 and 5 to 3. Every
other moved case keeps its assertion count. The 25 moved cases and the
labels case are all in `tests/hooks/test_press.py` (executed, an `ast` walk
of both files).

confirms: none
`gaps.md`'s last divergence row holds. `hooks/root-migrate.py:103-121`
keeps `leases`, `worktree-choice` and `worktree-consent` in `STATE_NAMES`.
For a person upgrading from before the rename, that rename turns the
`specseal-` directories into the three `agentic-` paths the changelog
fragment names. The fragment's list therefore stays complete (read).

confirms: none
The frame's claim on the settle holds. `skills/settle/SKILL.md:155-172`
shows a group whose heading is not there and refuses nothing in the dry
run, so the pending rule changes of work item 1793169129 on
`docs/worktree-guard-spec.md` meet a removed file without stopping the
settle (read).

confirms: none
The branch merges onto `origin/release/v0.24.1` without conflict, with
8de879bc's edits to `tests/censuses.py#KEPT_OLD_NAMES` and
`.claude-plugin/plugin.json` included (executed, `git merge-tree
--write-tree`, exit 0).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over 3c49c7cd: unverified | the whole tree | the orchestrator, at the broad gate |
| Whether `.test_durations`, with 29 unpriced cases (`gaps.md` *Not done*), stays under `test_the_durations_file_prices_the_suite`'s shares: unverified, that case is part of the broad run | `.test_durations` | the orchestrator, at the broad gate |
| Whether `test_every_job_that_runs_pytest_has_the_whole_history` still earns its place now that no case skips at depth 1 (`gaps.md` *Not done*) | `tests/text/test_ci_gives_the_checks_what_they_need.py:515-528` | the repository owner |
| Whether work item 1793169129's `frame/questions.md` P1 closes with this removal (`frame/questions.md` P1, default (a)) | `seal/threads/1793169129-the-creation-row-still-says-retry-with-worktree-ok/frame/questions.md` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `python3 -` comparing `ast.dump` of each top-level definition of `hooks/lib/press.py` with `git show 1e82fd0a:hooks/worktree_consent.py`, docstrings set aside | exit 0, 14 of 14 `same` |
| `python3 -` counting `assert` nodes per case in `tests/hooks/test_press.py` against `git show 1e82fd0a:tests/hooks/test_worktree_consent.py` | 26 cases, 25 matched by name; two differ, 7 to 4 and 5 to 3 |
| `git grep -n -E` for the removed modules, files and variables outside `seal/threads` and the replay eval | exit 0, six lines, each accounted for in the confirmations |
| `uvx ruff check --select F` over the two gates, `press.py`, `cmdline.py`, `implementer-notice.py`, `dispatch.py`, `hooksession.py` | exit 0 |
| `bin/test tests/hooks/test_press.py tests/hooks/test_question_gate.py tests/hooks/test_routing_edit_gate.py -q` | exit 0, 79 passed |
| `bin/test tests/hooks/test_dispatch.py tests/hooks/test_cmdline.py tests/hooks/test_implementer_notice.py -q` | exit 0, 98 passed |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/github/test_rules.py tests/skills/test_fold_check.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_rider_reaches_its_file.py -q` | exit 0, 148 passed |
| `git merge-tree --write-tree --name-only HEAD origin/release/v0.24.1` | exit 0, no conflicted path |
| In a `git clone --no-local` at 3c49c7cd with `docs/worktree-guard-spec.md` and `docs/README.md` restored from 1e82fd0a: `python3 .github/scripts/rules.py --check --root clone` | exit 1, 17 refused in 266 check lines of 55 rule files, each naming a test file this work deletes |
| The same clone: `python3 skills/settle/scripts/fold_check.py --root clone` | exit 0, "the index docs/README.md names every document" |
