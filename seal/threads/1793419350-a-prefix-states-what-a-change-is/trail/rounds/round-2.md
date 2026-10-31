# Review round 2: 1793419350-a-prefix-states-what-a-change-is

target: faedeb6f, fixes 9e5b996b..faedeb6f

This verifying round reads the fix diff `9e5b996b..faedeb6f`: `9944919e`
(findings 1 to 3), `175f19d8` (finding 4), the answers in `c77c9ec1`, and
`faedeb6f`, the orchestrator's fold of the frame's table into a pointer,
read as a unit of its own. The range was re-established with `git log
--oneline`. Facts carried from round 1 and not re-established: the
coordinates of the release check (`judge_feat`, the early return, the step
in `hygiene.yml`), the phase record's five departures, and `seal layout
--pairs` reading 0 pairs for the test module. None of them is in the fix
diff. The fix diff adds no test; it changes the assertions of two existing
cases, so no new case is read against its group. The core sentence that the
release check's comment cites is on #1167's branch, and no finding counts
its absence. No `seal/parity.md` is declared, so the record names no
original commit.

The prompt asked whether the reordered table gives two writers one answer
for eight cases. Six hold, read at `skills/commit-pr-convention/SKILL.md:118-148`:
#1167 is not wholly any of the first four kinds and stops at `feat:` on
its Scope items 11 and 12; #1198 adds a record format, `feat:`; this work
adds a refusal on a rule it states, `feat:`; a test with the fix it pins
falls past `test:` to `fix:`; a dependency bump that tells no party to do
anything new is `chore:`; a commit of a work item's records alone is
`chore:`. Two do not: a speed-up, or a test change, that carries its work
item's records (finding 1), and a settle that rewrites a section its
judgments call for (finding 2).

## Findings

### 1. A speed-up or a test change that carries its work item's records falls past `perf:` and `test:`, so the first-row rule still sends it below them

severity: should
location: `skills/commit-pr-convention/SKILL.md:118-133`
evidence: executed `git show --name-only --format= 8cb58904`, `git show --name-only --format= 97e29b7a`, `git log origin/release/v0.26.0 --no-merges --format='%h %s'`
verdict: fixed 05b716f7
reopens: round-1#1

The close does not hold for the changes this repository titles. Round 1
found that the first-row rule sent every speed-up to `refactor:` and a
tests-only change to `fix:`. The fix put `test:`, `perf:`, `docs:` and
`chore:` first and gave each the words "and nothing else" or "only", and
the opening sentence now says "a change with any other part falls past
them" (`:120-121`). A pull request through the review chain always carries
its work item's records under `seal/threads/`, and the squash makes its
title the commit subject the release reads. So such a change is never
wholly tests or wholly faster. `8cb58904` is a `test:` squash whose files
are three test modules, `.test_durations` and one work item's records
(executed). Under the rewritten table it is not "tests only, and nothing
else", and not "only ... a work item's own records". It falls past all
four rows. The test it changes read files it should not have, so it fits
the `fix:` row's "behaviour existed and was wrong". A speed-up with the
case that pins it and its records falls past `perf:` and fits `refactor:`'s
"the same kinds of outcome, reached another way" (`:133`), which is round
1's defect unchanged. The last `perf:` squash on the release history,
`97e29b7a`, carried tests and work item records as well (executed). A
writer who reads the `test:` or `perf:` row gives one prefix. A writer who
applies `:120-121` gives another. A README edit with its changelog fragment
and a dependency bump with its records fall the same way, past `docs:` and
`chore:`. The answer to finding 1 checked a test with a fix and found it
falls to `fix:`, which is right. It did not check a whole change of one of
the first four kinds carrying its records.

The same boundary shows in one row the reorder did not touch. The `fix:`
row says "a check that starts refusing what its stated rule always refused
is here" (`:132`). In a repository whose checks include test cases, a
commit that adds only such a case is `test:` by the first-row rule and
`fix:` by that row's words. Round 1's finding 1, which the fix pass
answered "Holds", took it as `test:`.

```markdown
**A change takes the first row that fits, read from the top.** The first
four rows each fit only a change that is wholly of their kind, so they stand
first: the rows below them would otherwise take such a change, and a change
with any other part falls past them. A change's own tests, and the records
of the work item it belongs to, are never that other part: a speed-up with
the case that pins it and its work item's records is `perf:`, and a README
edit with its changelog fragment is `docs:`. A case added to the tests
alone is `test:` even where it refuses, and the `fix:` row's check is one
outside the tests. A change two rows fit takes the higher one, so a writer
who finds one part of the change that adds something stops at `feat:`.
```

answer: Routed by the orchestrator to the framer, not to a fix pass: the first-row rule was the mechanism the fixes chased. The reframe (fec2a3cc) replaced it with a per-part rule, and phase 2 built it at 05b716f7. Round 3 reopens this finding as its finding 2.

### 2. The new sentence says the settle writes only what the released frames decided, and the settle also rewrites guidance no frame decided

severity: should
location: `skills/commit-pr-convention/SKILL.md:142-145`
evidence: read `skills/commit-pr-convention/SKILL.md:139-148`, `skills/core/SKILL.md:72-77`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:30`
verdict: fixed 05b716f7
regression: round-1#2

The unit is the sentence `9944919e` added at `:142-145`, which names the
settle as one of the two cases where text a party acts on takes `chore:`
and gives the reason: the settle "writes into the policy documents what the
released work items' frames already decided". The frame (`frame/design.md`
*Scope* item 1, delivered by `frame/plan.md`'s phase 1 row) said such text
is never `chore:`. The fix named the settle as an exception and grounded it
in that description, which came from round 1's own paste-ready text. On
this base, `skills/core/SKILL.md:72-77` says the settle "rewrites the
guidance where a kind of judgment keeps costing more than it returns, and
writes a source where a judgment had none". No frame decided that rewrite.
#1167, which merges before this work, adds the step that does it to
`skills/settle/SKILL.md` (*The settling session's procedure*, step 3, read
with `git show` of its branch). A settle commit that rewrites such a section
is `chore:` by the row at `:130`, which names "the settle". By the sentence
at `:142-145` it falls outside the stated case, so it takes `feat:`, `fix:`
or `refactor:`. A writer gets one prefix from the row and another from the
sentence. The sentence also states something false about the settle to
every repository the skill ships to.

```markdown
**Text a party reads and acts on is behaviour.** A skill, an agent
definition, a template a party fills and a hook's message are such text, so
a change to one takes `feat:`, `fix:` or `refactor:`, and never `docs:`. It
takes `chore:` in two cases only, both named in the `chore:` row: a work
item's own records, which only that item's parties read and which leave with
it, and the settle, which is release preparation whatever it writes into
the policy documents: the rules the released work items decided, and a
section it rewrites where their recorded judgments kept costing more than
they returned.
```

answer: Routed with the other two to the framer's reframe (fec2a3cc). The settle is now *An effect is counted once, by the change that decided it*, built at 05b716f7. Round 3 confirms the close.

### 3. The frame's Scope item 1 still says text a party acts on is never `chore:`, and the fold says the frame's rule is unchanged

severity: should
location: `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:30`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:64`
evidence: executed `git grep -n -E "never .docs:. or .chore:.|.chore:. is never a change"`
verdict: fixed 05b716f7
regression: round-1#1

The unit is the paragraph `faedeb6f` wrote at `frame/design.md:64` in
place of the frame's copy of the table, after finding 1's answer asked the
orchestrator to fold the new order in. The frame drew the rule that text a
party acts on is never `docs:` or `chore:` (*Scope* item 1, `:30`, which
`frame/plan.md`'s phase 1 row delivers). The fix pass for finding 2 made
`chore:` take two such cases, and the fold's paragraph states that
exception and also says "The rule this frame drew is unchanged". The defect
came from the fold: it rewrote the classification section and left `:30`,
which still reads "never `docs:` or `chore:`" and "`chore:` is never a
change a party acts on". The search over the tree finds those words at
`:30` and nowhere else outside round records (executed). The sealer reads
*Scope* against the tree and the issue, and the settle reads the design. A
reader of `:30` checks the skill's two `chore:` cases against a frame that
forbids them, and the sentence at `:64` tells that reader nothing changed.
Contract rule 19 asks that the text the change amends be rewritten where it
stands.

```markdown
In `frame/design.md` *Scope* item 1, replace the two sentences
"Text a party reads ... never `docs:` or `chore:`. `chore:` is never a
change a party acts on, a check, a gate, a record's shape or a process step."
with:

Text a party reads and acts on, such as a skill, an agent definition, a
template a party fills or a hook's message, is behaviour, so a change to it
takes `feat:`, `fix:` or `refactor:`, never `docs:`, and `chore:` only as a
work item's own records or the settle. Apart from those two, `chore:` is
never a change a party acts on, a check, a gate, a record's shape or a
process step.

In *Data & interfaces*, *The classification*, replace "The rule this frame
drew is unchanged:" with:

The rule this frame drew stands with one change, made by round 1's finding
2, where the frame had said text a party acts on is never `chore:`:
```

answer: Routed with the other two to the framer's reframe (fec2a3cc). Scope item 1 was rewritten there and folded at 5b6dc48f. Round 3 reopens this finding as its finding 1.

## Confirmations

confirms: round-1#2
The contradiction round 1 named is gone. The `chore:` row names the settle
and a work item's own records (`skills/commit-pr-convention/SKILL.md:130`),
and the sentences under the table now name both as the only cases where
text a party acts on takes `chore:` (`:139-148`). The fix pass was right
that the paste-ready clause "whichever row above also fits them" would have
been false once `chore:` stood above `feat:`. The description the fix gives
the settle is finding 2 of this round. Read.

confirms: round-1#3
The two branch-name examples now read `fix/940-on-demand-files-state-the-current-rule`
and `docs/the-readme-says-how-to-install` (`skills/commit-pr-convention/SKILL.md:278-279`).
The first is a change that made text a party reads state the current rule,
which the `fix:` row takes. The second is text no party acts on. A search
under `skills/`, `agents/`, `templates/`, `docs/` and both READMEs for a
line opening `chore/` or `docs/` followed by a slug finds only the second
example (executed, `git grep`).

confirms: round-1#4
Both cases now pin the new words
(`tests/github/test_release_completeness_check.py:339-340`, `:360-363`).
In a scratch clone at `faedeb6f`, the warning's "That reading passes" put
back to "Passing" turned both cases red, 2 failed and 35 passed, and the
module was green before the edit, 37 passed. Executed (`## Probes`). The
crafter's second mutant, "the milestone" put back to "this run", fails the
assertion on "the milestone reading verified NOTHING" in both cases as
written. Read.

confirms: none
The changelog fragment states the new order and the two `chore:` cases
(`seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:7`),
in step with the skill at `faedeb6f`. What it says of the settle carries
finding 2's defect only through the words "the settle among it", which
make no claim about what the settle writes. Read.

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* still lists the
full suite, the repository-wide lint and the format at this branch's head
after `release/v0.26.0` is merged in, with the orchestrator answering. When
this round's three findings are answered, the next acts are the
orchestrator's broad run and then the sealer's spawn. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's ruff run and its count of 655 passed across six modules. This round ran the release check module and the six modules that read the skill, 37 and 189 passed, and did not run ruff | `skills/commit-pr-convention/SKILL.md`, `tests/github/test_release_completeness_check.py` | the orchestrator, by `seal gate` |
| The core sentence that the release check's comment on `FEAT` cites, and #1167's settle step 3 that finding 2 cites, both on #1167's branch | `.github/scripts/release_completeness_check.py:285-288`, `skills/settle/SKILL.md` | the orchestrator, at the merge of `release/v0.26.0` into this branch |
| The renamed step and its `::error::` line on a real release pull request into `main` | `.github/workflows/hygiene.yml:141` | the orchestrator, at the release pull request |

## Probes

| Command | Result |
|---|---|
| In a scratch clone at `faedeb6f`: `bin/test tests/github/test_release_completeness_check.py -q -p no:xdist` | exit 0, 37 passed |
| The same clone, the warning's "That reading passes" edited back to "Passing", then the same command | exit 1, 2 failed and 35 passed: both missing-milestone cases; the edit was reverted with `git checkout` |
| The same clone: `bin/test` over the six modules that name `commit-pr-convention`, with `tests/behaviour/test_docs_line_wrap.py` named twice, in the parallel form | exit 5, no tests ran |
| The same clone: `bin/test` over the same six modules, each once, `-q -p no:xdist` | exit 0, 189 passed |
| `git show --name-only --format= 8cb58904` and `97e29b7a` | each squash carries test files and one work item's records under `seal/` |
| `git grep -n -E "never .docs:. or .chore:.\|.chore:. is never a change"` | `frame/design.md:30`, the skill's `:147`, and two round-record lines |
