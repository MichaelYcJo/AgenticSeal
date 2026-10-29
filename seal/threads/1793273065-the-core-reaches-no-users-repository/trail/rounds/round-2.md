# Review round 2: 1793273065-the-core-reaches-no-users-repository

target: 3418f1a3, fixes 007d9cb9..3418f1a3

## Findings

### 1. The core's new routing sentence puts "that batch" before the clause about the question, so it can read as saying the hook holds the first edit until the whole batch is answered

severity: should
location: `skills/core/SKILL.md:82-86`, `tests/text/test_review_axes.py:100-125`, `seal/threads/1793273065-the-core-reaches-no-users-repository/frame/design.md:49-54`
evidence: read `skills/core/SKILL.md:77-86`, `hooks/routing-edit-gate.py:2-35`, `skills/implement/orchestration.md:95-103`, `skills/implement/SKILL.md:171-175`
verdict: fixed 3c43b42e
regression: round-1#1

The unit is the sentence `1562e058` wrote into *Asking a person is the most
expensive judgment* (`skills/core/SKILL.md:82-86`). The frame (`frame/plan.md`
phase 1, and `frame/design.md` *Scope* item 1 as it stood at `007d9cb9`)
made the routing question the subject, "asked by the session that spawns the
work, as ... states, and `hooks/routing-edit-gate.py` refuses the first edit
until it is answered", so every clause had one referent. The fix took round
1's paste-ready text word for word. That text set "that batch" between the
routing question and the two clauses that follow, so the defect came from
round 1's own proposed fix.

The sentence now reads: "The routing question is one of that batch, which
the orchestrating session puts as `skills/implement/orchestration.md`
*Orchestrator: how the work is routed* states, and
`hooks/routing-edit-gate.py` refuses the first edit until it is answered."
The nearest noun to "which" is "that batch", and so is the nearest noun to
"it". Read that way, the cited section states how the whole batch is put,
and the hook holds the first edit until the whole batch is answered. Both
are false. The section states the routing question and only places it in
the batch (`skills/implement/orchestration.md:97-99`). The batch is
`skills/implement/SKILL.md` *1.*'s, and it holds a decision, an approval, a
credential and a permission (`:171-175`). The hook refuses an edit only
while no routing declaration names the branch (`hooks/routing-edit-gate.py:2-8`).
It knows nothing of a credential or an approval.

This matters because the core is what every session and every agent holds
before anything else, and it ranks above the skills. A session that takes
the second reading can treat the hook letting its first edit through as
proof that the batch is done. The credential it never asked for then stops
the run mid-way, which is the cost the paragraph exists to prevent.
`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
읽히게 쓴다* names this class, a clause that attaches to something other
than the noun the writer meant. The core's own first section requires the
same of every sentence an agent reads.

The case the fix added pins the first clause only. Nothing pins which
question the hook waits on. The frame's fold carries the same attachment:
`frame/design.md:50-54` reads "the routing question is one of that batch,
asked by the session that spawns the work, ... until it is answered", and
in the design "that batch" also has no antecedent of its own.

```markdown
<!-- skills/core/SKILL.md:79-86 -->
and the difference has to be argued rather than assumed. Whatever needs a
person is asked once, together, before the first edit, and nothing comes
back mid-run; `skills/implement/SKILL.md` *1. Read the documents that
outrank the code first* holds that rule with its reasoning. The routing
question is one of that batch, and the orchestrating session puts the
routing question as `skills/implement/orchestration.md` *Orchestrator: how
the work is routed* states; `hooks/routing-edit-gate.py` refuses the first
edit until the routing question is answered.
```

It stays one sentence, so the frame's "one sentence" of *Scope* item 1,
*Removes* row 2 and plan phase 1 still hold.

```python
# tests/text/test_review_axes.py, in test_the_core_names_where_the_routing_question_is,
# after the assertion on "The routing question is one of that batch"
    assert (
        "refuses the first edit until the routing question is answered"
        in paragraph
    ), (
        "the core does not say which question the hook waits on, so its "
        "last clause can be read as the whole batch"
    )
```

```markdown
<!-- frame/design.md, Scope item 1, the sentence on the added sentence -->
   issue, milestone 69 and `routing.md` use for it. One sentence is added to
   the paragraph *Asking a person is the most expensive judgment*: the routing
   question is one of the batch that paragraph says is asked before the first
   edit, and the session that spawns the work puts the routing question as
   `skills/implement/orchestration.md` *Orchestrator: how the work is routed*
   states; `hooks/routing-edit-gate.py` refuses the first edit until the
   routing question is answered. That sentence is what the block's routing bullet
```

The new assertion is red against `3418f1a3`'s core and green after the core
edit above, which is how the fix pass shows it (contract rule 15). The
design's fold is the orchestrator's.

answer: The finding holds. `hooks/routing-edit-gate.py:2-8` refuses an edit only while no routing declaration names the branch, so the hook waits on the routing question and not on the whole batch. The core's sentence is now the one the finding proposes: "The routing question is one of that batch, and the orchestrating session puts the routing question as `skills/implement/orchestration.md` *Orchestrator: how the work is routed* states; `hooks/routing-edit-gate.py` refuses the first edit until the routing question is answered." It is still one sentence. `test_the_core_names_where_the_routing_question_is` now also asserts "refuses the first edit until the routing question is answered". That assertion was seen red against the core at `3418f1a3` and green after the edit (`bin/test -q -p no:xdist tests/text/test_review_axes.py -k test_the_core_names_where_the_routing_question_is`, exit 1 then exit 0). Both changes are inside `location:`. `git grep` on "first edit until", "one of that batch" and "one of the batch" finds the same attachment only in `frame/design.md:50-54`, *Scope* item 1 ("one of that batch, asked by the session that spawns the work, ... until it is answered"). That is the frame's, and the orchestrator folds it.

### 2. The memo and the release note give the core as 6,711 B and the session's share as 6,810 B, but round 1's first fix made the core 6,716 B

severity: should
location: `seal/threads/1793273065-the-core-reaches-no-users-repository/gaps.md:26`, `seal/threads/1793273065-the-core-reaches-no-users-repository/changelog.md:3`, `tests/skills/test_payload_meter.py:316-323`
evidence: executed `git show 007d9cb9:skills/core/SKILL.md | wc -c`, `git show 1562e058:skills/core/SKILL.md | wc -c`, `git show HEAD:templates/setup/claude-md-block.md | wc -c`, `env -u CLAUDE_CONFIG_DIR HOME=<scratch>/home-007d9cb9 python3 <scratch>/home-007d9cb9/.claude/plugins/marketplaces/agenticseal/skills/verify/scripts/payload_meter.py --root <scratch>/home-007d9cb9/.claude/plugins/marketplaces/agenticseal`, `env -u CLAUDE_CONFIG_DIR HOME=<scratch>/home-3418f1a3 python3 <scratch>/home-3418f1a3/.claude/plugins/marketplaces/agenticseal/skills/verify/scripts/payload_meter.py --root <scratch>/home-3418f1a3/.claude/plugins/marketplaces/agenticseal`
verdict: fixed c8dfc556
regression: round-1#3

The unit is the memo's second sentence, which `85edcd81` rewrote
(`gaps.md:26`). The frame (`frame/plan.md` phase 3, `frame/design.md`
*Scope* item 5) has the meter measure the core's cost at a commit and the
phase record keep that number. The fix wrote phase 3's 6,711 B, measured at
`a7329570`, as the core's present size. But `1562e058`, committed before it,
had already added 5 B to the core, and that is where the defect came from.

The core is 6,711 B at `007d9cb9` and 6,716 B at `1562e058` and at HEAD
(executed). The meter, run against a scratch home holding each tree and its
block, gives these figures (executed, *Probes*):

| What | At `007d9cb9` | At `3418f1a3` |
|---|---|---|
| The core | 6,711 B | 6,716 B |
| `~/.claude/CLAUDE.md` with its import: the pair less this repository's 856 B `CLAUDE.md`, which is the block's 99 B plus the core | 6,810 B | 6,815 B |
| Crafter's prefix (phase 3's before: 29,711 B) | 36,507 B, +6,796 | 36,517 B, +6,806 |

`gaps.md:26` now says "the core's 6,711 B a second time ... inside a
per-agent growth of 6,796 B". At HEAD both are 5 B and 10 B short.
`changelog.md:3` says the share "goes from 1,786 B to 6,810 B", and the
release ships 6,815 B. The fragment is the release note a user reads, and
the memo is the account the sealer reads against the tree. Both now state a
measurement the tree no longer gives. The token figures hold at 3.2 B/token:
6,716 B is about 2,099 tokens and +5,029 B is about 1,571.

The class is every stated byte size of the core, and of what holds it, that
was written before `1562e058` or carried past it. `git grep` on "6,711",
"6,796" and "6,810" (executed) finds `gaps.md:26` and `changelog.md:3`
outside the phase records. `trail/phases/phase-1.md:110`,
`trail/phases/phase-3.md:112-132` and `trail/phases/phase-4.md:37-38` are
measurements at the commit each phase names, and they stay. One instance is
outside the tree: the orchestrator's comment on #1183 (read with `gh api`,
updated 2026-10-29T14:30:06Z) says "the core's 6,711 B per spawn ... inside
the payload's net growth of +6,796 B per agent". Its edit is the
orchestrator's.

```markdown
<!-- gaps.md:26, the second sentence -->
That is the core's 6,716 B a second time, about 2,100 tokens at 3.2 B/token, inside a per-agent growth of 6,806 B (`seal payload` at `3418f1a3`; `trail/phases/phase-3.md` measured 6,711 B and 6,796 B at `a7329570`, before round 1's fix added 5 B to the core).

<!-- changelog.md:3, the sentence on `seal payload` -->
`seal payload` follows the `@` lines of the two `CLAUDE.md` files and counts each imported file, so the core's cost is measured: the share a session in a plugin user's repository reads from `~/.claude/CLAUDE.md` goes from 1,786 B to 6,815 B, about 1,570 tokens more.
```

A later edit to the core moves these figures again. Where the fix pass
weighs that against the house rule that no count is kept beside the tree,
giving the tokens alone and citing phase 3 for the bytes is the other form
of the same fix, and its answer says which it took.

answer: The finding holds. I took the other form, the one the orchestrator set as the prevention home on #1177: give the tokens alone, and cite phase 3 for the bytes. A new number would go stale again at the next edit to the core. `gaps.md:26` now says the second read costs about 2,100 tokens per agent spawn at 3.2 B/token. It names `trail/phases/phase-3.md` as where the exact bytes live, measured at its commit, and the pull request body as where they are given at the broad gate's HEAD. The fragment's `seal payload` sentence now says only that the share grows by about 1,570 tokens. Both are in `c8dfc556`. Both token figures hold at 6,716 B (6,716 / 3.2 is about 2,099, and +5,029 / 3.2 is about 1,571). The class was enumerated by a search over every file this branch changes outside `trail/`, for byte figures and for the token figures. One more instance was found, outside `location:`: `tests/skills/test_payload_meter.py:316-323`, a docstring I wrote in phase 3, said "the core's 6,700". It now copies no figure (`88cef629`), and that coordinate is appended to `location:`. The figures that stay are records of their time. `trail/phases/phase-3.md` holds the measurements at its commit. `trail/phases/phase-4.md:37-38` gives 1,786 B and 6,810 B as phase 3's figures, names phase 3 as their source, and is a phase record this pass does not rewrite. The round-1 record's lines are history. `skills/verify/scripts/payload_meter.py:55-56` and `:787` give earlier measurements of other files. The orchestrator's comment on #1183 still gives 6,711 B and +6,796 B, and its edit is the orchestrator's.

## Confirmations

confirms: round-1#2
All five shipped texts now give the true reason the project scope is gone:
the block's relative line names a `plugins/` directory inside the project
that is not there, and only a line rewritten to reach the clone would be
external (read `install.sh:22-26`, `README.md:302-306`,
`README.ko.md:297-300`, `changelog.md:3`,
`tests/behaviour/test_the_installer_writes_the_block_from_its_template.py:271-277`).
`install.sh:99` still computes `CORE="$(dirname "$TARGET")/$IMPORT"`, so the
installer's warning and its header now agree (read). The class was
enumerated again with `git grep` on "outside the working directory", "import
is external", "resolves outside", "reach outside", "points outside", "point
outside" and "is external" (executed). Every hit outside the round and phase
records gives the new reason: the four texts above, the test docstring, and
the orchestrator's fold at `frame/design.md:28`, `:244`, `frame/plan.md:62`
and `frame/questions.md:21`. The two `chain_check.py` hits are about document
roots. Carried rather than re-established: the docs sentence that a relative
import resolves against the file that holds it, quoted at
`frame/design.md:32`, and probe d's result, both from round 1's coordinates.

confirms: none
Round 1 finding 1's reading is gone from the tree, and finding 1 above is a
new defect in the same unit, not this one coming back. `git grep -i` on "one
ask is", "the one question", "only question" and "that one ask" (executed)
finds six lines, none about asking a person (`docs/the-record-layout.md:5`,
`skills/verify/scripts/broad_gate.py:852`,
`skills/verify/scripts/unverified_check.py:324`, `:542`,
`tests/behaviour/test_first_setup_asks_once.py:10`,
`tests/skills/test_arm_check.py:1388`). The new assertion in
`test_the_core_names_where_the_routing_question_is` is absent from the old
core (executed: the whitespace-joined core at `007d9cb9` holds "The routing
question is one of that batch" 0 times) and passes at HEAD (executed,
*Probes*). That is consistent with the red-then-green the fix pass reported.
The diff of the old `CLAUDE.md` against the core still prints the one added
sentence and nothing else (executed, *Probes*).

confirms: none
Round 1 finding 3's home half, which the fix pass answered without a commit,
holds. The comment on #1183 (read with `gh api`, updated
2026-10-29T14:30:06Z) names the agents' double read through `skills:` and
the import, its cost per spawn, and the unverified question whether a
`SessionStart` hook reaches a subagent. `docs/issues-and-milestones.md:287`
*An issue is its body and its comments together* makes that comment part of
the issue (read). The body's search still finds no subagent or spawn
(executed, *Probes*), so the home is the comment alone. The memo's sentence
now has the right structure: the second read is the core, inside the
per-agent growth, as `trail/phases/phase-3.md:125-130` breaks it down. Its
figures are finding 2.

confirms: none
The fix pass's labels are honest about scope. It reported 95 modules passing
and labelled no broad gate as run. This round did not re-run the 95; it ran
round 1's four modules again (executed, *Probes*). The orchestrator's 246
passes after the fold are its own report and were not re-run here.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `3418f1a3` | the tree | the orchestrator, through `seal gate` |
| The fix pass's 95 modules (4,280 passed, 10 skipped) and the orchestrator's 246 passes after the fold, which this round did not re-run | the tree at `5694cdbc` and `3418f1a3` | the orchestrator, through `seal gate` |
| The #1183 comment's byte figures, outside the tree (finding 2) | #1183, comment 6498975932 | the orchestrator |
| Round 1's *Not judged* rows on the symlinked `~/.claude/CLAUDE.md`, `/agentic:update` under `CLAUDE_CONFIG_DIR`, the three-fix stop for an orchestrating session, and Q2. They are carried, outside this fix diff, and were not re-examined | `seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-1.md` | as round 1 names each: the orchestrator, the owner at #1148 |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/behaviour/test_the_installer_writes_the_block_from_its_template.py tests/skills/test_payload_meter.py tests/text/test_every_agent_reads_the_contract.py tests/text/test_review_axes.py` | exit 0, 89 passed |
| `diff <(git show origin/release/v0.25.0:CLAUDE.md \| sed -n '3,$p') <(sed -n '/^## The first value/,$p' skills/core/SKILL.md)` | one hunk at old line 65: the routing sentence added, nothing else |
| `gh issue view 1183 --json body --jq .body \| grep -n -i "subagent\|spawn\|twice\|skills:"` | lines 20 and 28, both about a session; no subagent, spawn or `skills:` |
| `git show 007d9cb9:skills/core/SKILL.md \| tr -s ' \n' '  ' \| grep -c "The routing question is one of that batch"` | 0 |
| `git show <rev>:skills/core/SKILL.md \| wc -c` for `007d9cb9`, `1562e058`, HEAD | 6711, 6716, 6716 |
| `payload_meter.py --root <home>/.claude/plugins/marketplaces/agenticseal` with `HOME=<home>`, where `<home>` under `<scratch>` holds `git archive <rev>` at that path and the rev's block as `.claude/CLAUDE.md`, for `007d9cb9` and `3418f1a3`; the scratch homes were removed after | `007d9cb9`: core 6,711 B, pair 7,666 B, crafter 36,507 B. `3418f1a3`: core 6,716 B, pair 7,671 B, crafter 36,517 B, framer 39,179 B, proofer 36,110 B |
