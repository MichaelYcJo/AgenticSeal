# Review round 1: 1793171930-no-check-reads-a-citation-of-most-files

target: 5b7ab394 against c825fd2c

## Findings

### 1. The check line S10 extended is pinned by a second module, which fails at the branch head

severity: must
location: `tests/text/test_a_language_section_of_writing_style_opens_alone.py:43-50`, `skills/writing-style/SKILL.md:268`
evidence: executed `bin/test tests/text/test_a_language_section_of_writing_style_opens_alone.py -q`
verdict: open

The broad gate runs this module, so the branch cannot pass `seal gate` as it
stands. Phase 2 appended `tests/behaviour/test_a_cited_section_stands_in_its_file.py`
to the `check:` line at `skills/writing-style/SKILL.md:268`. The module
`tests/text/test_a_language_section_of_writing_style_opens_alone.py` holds
that line's old value in `WRITING_RULE_CHECKS` (`:43-50`) and compares the
section's check lines with it at `:155`. Run alone at `5b7ab394` it ends
`1 failed, 1 passed`, exit 1, on
`test_the_rules_for_text_an_agent_or_a_check_reads_reach_both_languages`.

The crafter's phase 2 record says S10 was verified by
`bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/github/test_rules.py -q`
and `bin/seal rules --check`. Both pass (executed), and neither reads this
pin. A `git grep` of `writing-style` across `tests/` names this module, so
the plan's run list missed a reader of the edited file. Contract rule 19
asks that the same commit correct what stood on the old fact.

```python
WRITING_RULE_CHECKS = (
    "check: tests/github/test_rules.py"
    " tests/skills/test_rule_changes.py"
    " tests/test_censuses.py"
    " tests/text/test_the_agent_contract_holds_the_universal_rules.py"
    " tests/behaviour/test_a_cited_section_stands_in_its_file.py",
    "check: tests/behaviour/test_one_word_one_meaning.py",
    "check: none reader: the proofer at review",
)
```

answer:

### 2. A citation in the `skill's` spelling is not read when the named skill is gone, though a path citation of a gone file is refused

severity: should
location: `tests/behaviour/test_a_cited_section_stands_in_its_file.py:55`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:93-97`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:348-392`
evidence: read `tests/behaviour/test_a_cited_section_stands_in_its_file.py:55`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:93-97`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:199-204`
verdict: open

On this input the reader fails open where it could refuse. `cited_in`
keeps a name citation only where `skills/<name>/SKILL.md` is tracked
(`:96`). This filter is right for the bare form `` `<name>` *X* ``, because
any backticked word can stand before italic text. The form
`` the `<name>` skill's *X* `` is different: the word `skill's` already
says a skill is meant. When the skill is removed or renamed, every citation
of it in that form silently drops out of the corpus, and the suite stays
green. A path citation of a removed file goes the other way. Its first
segment is still a tracked top-level entry, so it is read and refused
(`:199-204`, and S7). `frame/questions.md` judgment 4 grounds that refusal
in one sentence: a file that moved leaves its citations dangling, as a
renamed heading does. A removed skill is the same case in the other
spelling.

This is not hypothetical. `e391ea04` (#1099) removed eight skills from
`skills/`. Today the tree holds the `skill's` spelling only for tracked
skills (executed: a `git grep` of that spelling outside the records names
`implement` and `verify` alone, plus the fixture's `drafting`). So refusing
the untracked case breaks no current citation. The frame's grammar table
says "where that file is tracked" for both name forms. Its table of what
the reader does with input it cannot read has no row for this case, and
#956 starts its audit from that table. If the fix is taken, `gaps.md` owes
a divergence row against the grammar table.

```python
NAME_CITED = re.compile(r"`([a-z0-9][a-z0-9-]*)`( skill's)?\s+\*([^*]+)\*")

    found += [
        (m.start(), f"skills/{m.group(1)}/SKILL.md", m.group(3))
        for m in NAME_CITED.finditer(flow)
        # The bare name is read only where the skill is tracked, since any
        # backticked word can stand before italics; the word `skill's`
        # names a skill, so a removed one leaves its citation dangling.
        if m.group(1) in skills or m.group(2)
    ]
```

In S5's fixture, append a blank line and then the line
``the `unlisted` skill's *Gone six*`` to `SPELLINGS`, so it stands at line 20. Raise `found.read` to 10. Add
`("a.md", 20, "skills/unlisted/SKILL.md", "*Gone six*")` as the last
expected dangling entry. The bare `` `unlisted` *Gone five* `` stays unread.

answer:

## Confirmations

confirms: none
The three corrections of *Scope* item 2 hold. `f6ae6db6` is an ancestor of
the head, and line 117 of `docs/the-broad-gate.md` at that commit is
`## Where the stamp is drawn` (executed: `git merge-base --is-ancestor`,
`git show`). `docs/the-record-layout.md:140` opens the bold lead
*Whether a line is live is asked by what the line does* (read).
`agents/crafter.md` opens *Commit before you mutate* (read: `frame/design.md`
cites `:105`, and S1 resolves it). The new module passes alone, 25 passed,
exit 0 (executed).

confirms: none
Everything *Removes* names is gone. A `git grep` outside the records for
`SKILL_NAMED`, `CITED_TITLE`, `NOT_CITATIONS`, `implement_headings`,
`dangling_implement_citations`, `cited_files`, `MISSING_STEP` and the two
removed case names finds nothing (executed). The three `.test_durations`
keys are removed (read in the diff). The two extra imports the crafter
removed, `os` and `ROOT`, are unused in what remains
(`tests/behaviour/test_the_set_a_work_item_always_has.py:30-32`, read), so
`gaps.md`'s second row holds.

confirms: none
The replacement loses nothing the old case read. A probe ran the removed
regex over whitespace-collapsed text of the same corpus. It found 26
citations of `implement`, and every one is among the new reader's
citations of `skills/implement/SKILL.md` (executed, `## Probes`).

confirms: none
The new reader's "not read" branch for an untracked first segment hides
nothing today. Of the 76 citations it skips, two name a repository file
through `$CLAUDE_PLUGIN_ROOT/templates/setup/config.md`
(`skills/config/SKILL.md:143`, `:148`), and both resolve against that file.
None names a file relative to the citing file's directory (executed,
`## Probes`).

confirms: none
`gaps.md`'s fourth row, a bold lead read only on a list item, the first
line, or after a blank line, changes no citation in the tree. No tracked
`.md` file outside the records has a line opening `**` directly under a
heading or a fence line (executed, `## Probes`). That reading refuses
rather than passes a lead in that place, so it fails closed.

confirms: none
The census row `gaps.md` names holds:
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:89-91` names
`#citations`, and that module passes (executed, in the module run below).
The comment edit in `tests/behaviour/test_one_word_one_meaning.py` touches
line 461 alone (read in the diff), as phase 1 was asked.

confirms: none
`bin/seal layout --check` exits 0 with 0 refused, and `bin/seal rules --check`
exits 0 on 266 check lines (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's red runs: S1 red at the three coordinates before the corrections, and S9 red against a reader that excused nothing. They are claimed in the phase records, and this round did not re-run them against the old tree. | `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/trail/phases/phase-1.md:18-27`, `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/trail/phases/phase-2.md:36-39` | the sealer, which re-runs a sample of the crafter's claims |
| The mutation counts, 29 in phase 1 and 14 in S9, all red in the end. Not re-run. A score licenses *tested*, never *safe*. | `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/trail/phases/phase-1.md:29-34`, `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/trail/phases/phase-2.md:61` | the sealer |
| Whether S9's warning stands in the output `seal gate` keeps | `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/gaps.md:22` | the orchestrator, at `seal gate` |
| The full suite, the repository-wide lint and the typecheck. The suite is labelled `unverified` in `gaps.md`, and that label is honest, since finding 1 fails a module the gate runs. | `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/gaps.md:20` | the orchestrator, at `seal gate` |
| Whether a sibling branch landing in `release/v0.24.0` changes what S1 meets (Q2) | `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/frame/questions.md:42` | the orchestrator, at the rebase |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 39 modules that `git grep -l` names for each changed file's path or name under `tests/`, `-q`, in a clone at `5b7ab394` | exit 1: 1 failed, 1816 passed, 4 skipped. The one failure is finding 1. |
| `bin/test tests/text/test_a_language_section_of_writing_style_opens_alone.py -q` | exit 1, 1 failed, 1 passed |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | exit 0, 25 passed |
| `bin/seal layout --check` | exit 0, 160 files read, 0 refused |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `tests/behaviour/test_tmp_round1_probe.py`, one file run once and deleted. It imports the new module, runs the removed `implement` regex over the corpus, lists the citations skipped for an untracked first segment, searches for a name citation wrapped before `skill's`, and searches for a bold lead directly under a heading or fence. | exit 0. Old reader 26 citations, none missing from the new reader. 76 skipped, 2 naming a repository file, both resolving. No wrapped `skill's` citation. No lead under a heading or fence. |
| `git grep` of the `skill's` spelling outside the records | names `implement`, `verify` and the fixture's `drafting`, all tracked |
| `git merge-base --is-ancestor f6ae6db6 HEAD`, `git show f6ae6db6:docs/the-broad-gate.md` | exit 0; line 117 is `## Where the stamp is drawn` |
