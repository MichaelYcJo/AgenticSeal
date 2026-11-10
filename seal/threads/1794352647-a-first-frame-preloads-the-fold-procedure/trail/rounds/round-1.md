# Review round 1: 1794352647-a-first-frame-preloads-the-fold-procedure

```seal
target: 493553094 against release/v0.37.3
```

The branch was read against `release/v0.37.3` at `7c2801838` over its
eight commits, `5d16bcd4d` to `493553094`. This is the first round, so no
coordinate or verdict was carried from an earlier one, and every fact
below was established here. `seal/parity.json` is not declared, so no
parity comparison was owed. The work item's records were each read whole
at `493553094`: `routing.md`, the three frame files, `gaps.md`,
`changelog.md`, `pr.md` and `trail/phases/phase-1.md`. No `pr.<lang>.md`
stands, and `seal/config.json` names English for both language keys, so
none is owed.

## Findings

### 1. The sentence the build adds leaves "It corrects its row" naming the framer as its nearest antecedent

```seal
severity: should
location: `skills/implement/orchestration.md:107-112`, `tests/text/test_the_rules_have_one_owner.py:511-512`
evidence: read `skills/implement/orchestration.md:96-112`, `7c2801838:skills/implement/orchestration.md:104-109`, `tests/text/test_the_rules_have_one_owner.py:511-512`, `seal/threads/1794289596-implement-orchestration-grew-back/frame/design.md:83`; executed `git grep -n "corrects its row"`
```

Why it matters: at the base, the paragraph of *Orchestrator: the order
inside a ticket* read "The orchestrator resumes the work item's framer
... and otherwise spawns a fresh framer and hands it the decisions and
the commit at which the frame was last written. It corrects its row where
the framer's hand-back names a defect in it, then commits the frame files
the framer changed and its own rows in one commit"
(`7c2801838:skills/implement/orchestration.md:104-109`). The sentence
before "It" had the orchestrator as its subject. *Scope* item 4 of
`frame/design.md` places the new sentence after "the commit at which the
frame was last written.", and the build put it there
(`skills/implement/orchestration.md:107-110`). The new sentence's subject
is "The message ... and the prompt", and it ends "for the framer to open
before it answers." So the "It" of "It corrects its row" now follows a
sentence whose last singular actor, and whose last "it", is the framer.
The reader learns that "It" is the orchestrator only from the rest of the
sentence, where "the framer's hand-back" is named apart. The text tells
the orchestrator what to do after a fold, and a framer sent there by the
new file's citation of the same section reads it too.
`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
읽히게 쓴다* asks that a sentence telling a party what to do name that
party, and that text an agent reads have one reading. The row this
sentence carries out, row 8 of D1 in
`seal/threads/1794289596-implement-orchestration-grew-back/frame/design.md:83`,
names the actor: "The orchestrator corrects its row where the framer's
hand-back names a defect in it." The order case pins the sentence by its
first words, row 8 at `tests/text/test_the_rules_have_one_owner.py:512`,
so the fix changes that pin with it. `git grep -n "corrects its row"`
finds no other statement outside `seal/threads/`.

```markdown
at which the frame was last written. The message that resumes the framer,
and the prompt that spawns a fresh one, each name
`skills/implement/fold-and-reframe.md` for the framer to open before it
answers. The orchestrator corrects its row where the framer's
hand-back names a defect in it, then commits the frame files the framer
changed and its own rows in one commit, before the spawn that reads them.
```

```python
        # 8, round 2 of #1442.
        (
            8,
            "The orchestrator corrects its row where the framer's hand-back "
            "names a defect in it,",
        ),
```

The changed pin is seen red with the old wording of the sentence restored
in `skills/implement/orchestration.md` (contract rule 15).

## Confirmations

What matched: *Scope* item 1's word-for-word move holds. The base's
`agents/framer.md:256-289` and the new file's `:8-40`, split one word per
line and compared with `diff`, differ in the fold half only at the four
citations `frame/design.md` G11 lists. The two that resolved inside the
definition now name `agents/framer.md`, and "*What the tree can answer,
you answer*" and "rule 12" now read "contract rule 5" and "contract rule
12". The rest of the diff is the reframe half, which *Scope* item 1
rewrites as a citation (executed). The phase record's account of S6
(`trail/phases/phase-1.md:9`) agrees with that diff.

What matched: the reframe half cites both owners as `frame/design.md` G6
and *Scope* item 1 say. The row *The framer* of
`skills/code-review/orchestration.md:245` states the rewrite of
`plan.md` with new phase rows, a closed phase keeping its commit, and of
`frame/design.md`, and the `Reframed` line under the `Framed` line.
`docs/running/the-run.md:14-22` states the `Reframed` line under the mark,
written by that framer. The new file's
`skills/implement/fold-and-reframe.md:34-39` names both, and ends
"`docs/running/the-run.md` *The run* owns that rule", the words rule 16 of
`RULES` reads (read). The dropped "never in its place" is restated by
nothing lost: both owners say "under" (read).

What matched: the pointer at `agents/framer.md:254-255` is *Scope* item 2's
text word for word, and the rule keeps no `check:` line. The mark rule at
`agents/framer.md:233-236` keeps its bold lead and the mark's shape, and
`git grep -n "git dir" agents/framer.md` exits 1 (S2, executed). The
docstring of `tests/behaviour/test_waiver_decided_at_start.py#test_the_framer_leaves_a_mark_in_the_tree`
loses both sentences *Scope* item 6 names, and its assertions are
unchanged (read).

What matched: S1 holds. `wc -c` gives `agents/framer.md` 14,946 B, against
17,298 B at `7c2801838`, and `skills/core/SKILL.md` 9,322 B and
`skills/agent-contract/SKILL.md` 13,186 B, 37,454 B in all. The diff from
the base touches neither skill (executed). These are the figures
`changelog.md:3` and `gaps.md:8` state.

What matched: `changelog.md:3` says no `frame/design.md` at v0.32.0,
v0.34.0, v0.36.0, v0.37.0, v0.37.1 or v0.37.2 carries a `Reframed` line.
`git grep -l '^Reframed ' <tag> -- 'seal/threads/*/frame/design.md'`
lists no file at any of the six tags (executed). `changelog.md:9` says no
hook, library or script writes a framer mark and that `hooks/hooks.json`
registers only `Stop` and `SessionStart`. The file's `hooks` keys are those
two, and `git grep -n -i framer -- hooks lib bin 'skills/*/scripts'`
finds no line that also names a mark or git (executed).

What matched: the tests re-pointed by *Scope* items 5 and 7 hold what the
frame says. Rule 16 of `RULES` lists `FOLD` in place of `FRAMER` with the
same words. The fold case asserts that `agents/framer.md` names the
`FOLD` path and slices the new file from the same lead, and pins all four
re-pointed citations; the phase record says why it pins four where the
item could be read as two (`trail/phases/phase-1.md:15`). Row 4 of the
order case pins the citation in its new words, row 25 pins the sentence
*Scope* item 4 adds, and the comment at
`tests/text/test_the_rules_have_one_owner.py:541-542` names the new file.
`tests/behaviour/test_docs_line_wrap.py:159-161` adds the file after
`skills/implement/merge-order.md` with the comment *Scope* item 7 gives.
No test function is added, so no new test is read against a group. The
six modules ran green (executed, `## Probes`).

What matched: the census of the moved rule's old spellings is whole
outside `seal/threads/`. `git grep` for "two routes back", "states the
fold", "`agents/framer.md` *Rules*", "framer mark" and "git dir's mark"
finds only the new file, the re-pointed citation and the test module's
lead and comment; the one other hit,
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:90`,
is about another rule of `agents/framer.md`. Every citation of
`agents/framer.md` in `skills`, `docs`, `templates`, `README.md`,
`CONTRIBUTING.md` and `agents` names a part that stays in the definition
(executed).

What matched: the records state the target. The dated sections of
`frame/design.md` and `frame/plan.md` state `5d16bcd4d`, and every
sentence saying what the work does reads true at `493553094`, the *Removes*
row the orchestrator's fold rewrote among them. `frame/plan.md:37` now
cites `7c2801838:agents/framer.md`, and
`tests/text/test_a_cited_commit_outlives_the_squash.py` passes (executed).
Each of the six quotes in `pr.md` stands word for word at the coordinate
it names in `frame/plan.md`, and `pr.md` quotes no sentence of
`changelog.md` (read). The title row's grounds hold: no test function,
gate, check or hook is added or removed, and the order and fold cases
gain pins inside existing cases (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at `493553094`. This round ran six modules narrow, and the suite stays `unverified`. | `Broad gate` in `seal/config.json` | the orchestrator, by `seal gate --record` |
| `release_report.py`'s `preloads` row for the framer, which the issue's *Done when* names. This round measured the branch only. | `.github/scripts/release_report.py#preloads` | the orchestrator, at the release's pull request into `main`, as `gaps.md:8` says |
| Whether a resumed framer opens the new file before it answers a fold. No case can read it; `frame/plan.md:15` names the signal, a fold hand-back that skips a clause the file states. | `skills/implement/orchestration.md:107-110`, `agents/framer.md:254-255` | the orchestrator, reading the framer's hand-back on the next fold |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_waiver_decided_at_start.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/github/test_rules.py -q` | exit 0, 263 passed, 2 warnings, both on another work item's pending rule change |
| `bin/seal rules --check` | exit 0 |
| `git show 7c2801838:agents/framer.md`, lines 256 to 289, and `skills/implement/fold-and-reframe.md`, lines 8 to 40, one word per line, through `diff` | the fold half differs only at the four G11 citations; the rest is the reframe half |
| `wc -c agents/framer.md skills/core/SKILL.md skills/agent-contract/SKILL.md`, and the same on `7c2801838:agents/framer.md` | 14,946 B, 9,322 B, 13,186 B, 37,454 B in all; 17,298 B at the base |
| `git grep -l '^Reframed ' <tag> -- 'seal/threads/*/frame/design.md'` at the six tags `changelog.md:3` names | no file at any tag |
