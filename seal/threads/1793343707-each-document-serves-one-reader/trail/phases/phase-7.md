# Phase 7: 1793343707-each-document-serves-one-reader

## What this phase found

**The frame held against the tree.** Step 7 of `skills/settle/SKILL.md`
*The settling session's procedure* read `7. Run \`seal settle --apply\`.`
at the base `fba13ab2`. Only two commits of the range changed it or its
pin, `0a15911b` and `634e8b26`. Between them they touched the skill, the
pin's module and this work item's `changelog.md`, and nothing else
(executed, `git show --stat`). After this phase,
`git diff fba13ab2 -- skills/settle/SKILL.md tests/text/test_settle_reads_before_it_removes.py`
prints nothing (executed). Both files are byte for byte the base's. The
`add` to `docs/release-checklist.md` *2b. Settle what earlier releases
left behind* stands in `frame/design.md` `## Rule changes`, and that
section stands in the checklist at the base (read). The settle writes it.

**The row named the step's entries and the comment at `:150-151`, and the
case's docstring also stated the measure.** Its last sentence said step 7
counts the review cost and posts the counts where a log is kept. This
phase reverted it with the rest, because the plan says every sentence
that states the measure in the settle procedure goes. That docstring
sentence was one.

**The fragment's `### Changed` entry held no sentence on the measure or
on step 7** (read). `frame/design.md` `## Removes` names "the measure's
sentences in the changelog fragment's entry and process row". Only the
process row held such a sentence, and only the row changed. The entry
was left as it stands, an assumption under `automation`. The frame's
*Operational impact* says the measure reaches no user, and a sentence in
the user's entry about a step the user never meets would contradict
that. The row now says this repository's release checklist takes the
four counts at the settle, before the records are removed, and posts
them to the `flow-baseline` log; it also says the plugin's settle
procedure is unchanged.

**The fix-pass sentence names the root as `either \`seal/\` root (contract
rule 11)`.** *Scope* item 13 says "a procedure step in every root and
under every condition its file names". In an agent definition the bare
word "root" has more than one reading: the policy root, a reference root,
the `seal/` root. Round 3's finding 2 was a `seal/` root in local mode.
So the sentence names that root and cites the rule that places it, an
assumption under `automation`. The rule's `check:` line is unchanged, so
no new target was added. The sentence stands after the clause on
`answer:`, because a pass reads the fix before it writes either line.

**The pin was added to its group.** Four clauses of the new sentence went
into the tuple of
`tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_crafters_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded`,
which is the one case that reads this paragraph. No case function is
new.

**Red, then green, then the mutants.**

- The reverted procedure case, against step 7 as it stood at
  `3c25478b`: exit 1, `AssertionError: ['Run \`seal settle --apply\`.']`.
  Green after the step was reverted (executed).
- The fix-pass case, with the four clauses added and the sentence not yet
  written: exit 1, on "the fix-pass rule lost \"A paste-ready fix is the
  proofer's claim and not the fix.\"" (executed). Green after the
  sentence (executed).
- `seal mutate agents/crafter.md`, with the sentence "Where that reading
  fails, write the fix in your own words and say so in `answer:`."
  deleted, against the fix-pass case: red, exit 1 (executed).
- `seal mutate skills/settle/SKILL.md`, with `7. Run` changed to
  `7. Then run`, against the procedure case: red, exit 1 (executed).
- `git status --short` printed nothing after both runs (executed).

**The measure's four commands, as `frame/design.md` *The measure's
command* gives them with `<root>` as `seal`, over
`seal/threads/1793273065-the-core-reaches-no-users-repository/` at
`7489d13e`** (executed, the third command's three stages exit `0 0 0` by
zsh's `pipestatus`):

```
$ grep -h '^### [1-9]' seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-*.md | wc -l
      10
$ grep -h '^regression: \|^reopens: ' seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-*.md | wc -l
       3
$ grep -h '^location: ' seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-*.md | sed 's/`seal\/threads\/[^`]*`//g' | grep -vc '`'
1
$ ls seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/ | wc -l
       8
```

They read 10, 3, 1 and 8, as scenario S9 states. Each prints one
number, where phase 6's `git grep -c` printed one line per file.

**Nothing under `skills/`, `agents/` or `templates/` names the counts.**
`git grep -n 'four numbers\|four counts' -- skills agents templates`
printed nothing and exited 1 (executed). The same search over the whole
tree outside `seal/threads/`, with `` flow-baseline` log `` added, finds
two lines. One is `skills/verify/orchestration.md:169`, the flow log's
own section. The other is `tests/skills/test_session_cost.py:3691`, a
docstring on `seal cost`'s numbers. Both stand at `fba13ab2` (executed),
and neither states the settle's measure.

**The phase-boundary set is 86 modules, run as one command.** It holds
the seven modules row 7 names. It also holds every test module whose text
names `crafter.md`, `agents/`, `settle/SKILL`, `"settle"`,
`seal/threads`, `"threads"` or `changelog.md`. It gave exit 0, with
`4558 passed, 9 skipped` at `7489d13e` (executed). The seven named
modules alone gave exit 0, with `456 passed` (executed). `ruff check` and
`ruff format --check` over the two test files this phase changed each
exited 0 (executed).

**`gaps.md` gains no row.** What the new sentence makes a fix pass do is
held only by the behaviour suite over `agents/crafter.md`. The row for
that suite already stands, with the owner as its answerer
(`frame/questions.md` Q1).
