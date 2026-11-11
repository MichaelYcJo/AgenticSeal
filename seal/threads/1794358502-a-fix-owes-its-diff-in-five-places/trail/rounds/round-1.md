# Review round 1: 1794358502-a-fix-owes-its-diff-in-five-places

```seal
target: 1ea4a8eb0 against release/v0.37.3
```

This is the first round, so no earlier record carries a coordinate and every
fact below was established here. The diff was read from `0b55462b2` to
`1ea4a8eb0`. `routing.md`, the three frame files, `gaps.md`, `changelog.md`
and `pr.md` were each read whole at `1ea4a8eb0`. No `pr.<lang>.md` stands,
and none is owed, because `seal/config.json` names English for both
language keys. No `seal/parity.json` is declared, and `seal/config.json`
has no `Pact` key. The definitions this round was spawned with are the
installed 0.37.2 plugin's. The diff was read against the tree's texts at
`1ea4a8eb0`, and the tree's `skills/code-review/SKILL.md` is the same file
as the installed one (executed: `diff -q`).

## Findings

### 1. The proofer's new sentence on a fix's account reaches `pr.md` and `pr.<lang>.md`, which the implementer's reading never covers

```seal
severity: should
location: `agents/proofer.md:138-142`, `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/frame/design.md:101`, `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/changelog.md:5`
evidence: read `agents/proofer.md:30-35`, `agents/proofer.md:122-142`, `agents/crafter.md:178-201`; executed `git grep -n -F "pr.md" 1ea4a8eb0 -- agents/crafter.md skills/implement/fix-pass.md`, which printed nothing, exit 1
```

Why it matters: T5 tells every proofer that a statement the implementer's
reading held and its account missed is a finding on the method. The
sentence names that reading as "its own reading of its diff and of these
records", and "these records" in that rule are the files step 3 reads whole
(`agents/proofer.md:123-124`, as T4 now words it). Step 3 lists eight
files, `pr.md` and `pr.<lang>.md` among them (`agents/proofer.md:30-32`).
The crafter's rule lists six: `routing.md`, the three frame files,
`gaps.md` and `changelog.md` (`agents/crafter.md:182-183`). Neither
`agents/crafter.md` nor `skills/implement/fix-pass.md` names `pr.md` at
all (the search above). The orchestrator writes `pr.md`, as it did here at
`1ea4a8eb0`. So a stale quote in `pr.md` after a fix pass is, by T5 as
written, a finding on the crafter's method. The crafter was never asked to
read that file, and the finding belongs to `pr.md` alone, which the rule's
own sentence on a quote of `pr.md` already makes (`agents/proofer.md:131-132`).

The claim and what the tree holds: `frame/design.md` *Scope* item 4 and
`trail/phases/phase-1.md` say T5 is "the proofer's half of R11". The old
R11 read "a statement the closed set held", and the old R5 defined that set
in general words, "each file of the work item's directory that states the
present". That wording left the same gap open to a reader's choice. T5
replaces the general words with a reference to the proofer's own list, so
the wider reading is now the only one. This is new work in a build phase,
so the finding takes neither a `regression:` nor a `reopens:` line.

The fix reaches three statements. The sentence in `agents/proofer.md` is
the repair. `changelog.md:5` quotes T5 word for word, so the fix pass owes
that quote too. `frame/design.md:101` holds T5 in *Data & interfaces*,
which the fix pass does not write, so its hand-back names it for the
orchestrator to fold. The case
`tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_proofer_finds_a_missed_statement_on_the_method_of_a_fix`
pins only the clause after the colon, which the fix leaves as it is.

```markdown
the sealer, the first reader of each sentence in them. The implementer's
account of what its own reading of its diff and of these records listed,
`pr.md` and `pr.<lang>.md` aside, is a claim you verify on your own: a
statement that reading held and the account missed, or a sample handed back
as a whole list, is a finding on the method, even where every instance on
the list was fixed.
```

```seal
verdict: fixed a085980ed
answer: The finding holds: "these records" in T5 are the files the proofer's step 3 reads whole, `pr.md` and `pr.<lang>.md` among them, and the crafter's rule names neither. The paste-ready words, which the frame's T5 holds since its fold at `112f5faf4`, now stand in `agents/proofer.md` *Every round reads the work item's records that state the present, whole, against its target*, and `changelog.md` quotes them. `wc -c agents/proofer.md` prints 10,999, 253 B more than 10,746 at `0b55462b2`, and the changelog now says 253 bytes. The case on the sentence pins the clause after the colon and passes unchanged.
```

### 2. The changelog says only the crafter and the proofer act on the sentences rule 12 lost, and the framer's and the orchestrator's folds cited one of them

```seal
severity: should
location: `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/changelog.md:3`, `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/changelog.md:12`
evidence: read `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/frame/design.md:18`, `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/frame/plan.md:19`, `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/frame/plan.md:26`; executed `git show 0b55462b2:<file> | perl -0777 -ne 'print if /asks\s+of\s+the\s+party\s+that\s+fixes/'` for `skills/implement/orchestration.md`, `skills/implement/fold-and-reframe.md` and `skills/code-review/orchestration.md`, which matched all three
```

Why it matters: the fragment becomes the release note, and the settle reads
its *Process changes* row for what the rule change was for. Both say the
moved sentences were acted on by the crafter and the proofer alone:
"only the crafter and the proofer act on those sentences" (`changelog.md:3`)
and "about 0.8 KB that only the crafter and the proofer act on"
(`changelog.md:12`). The first of those sentences is the one saying which
files a fix reads whole. At `0b55462b2`, `skills/implement/fold-and-reframe.md:22-24`
told a framer folding a decision to read each of its three files whole "as
contract rule 12 asks of the party that fixes", and
`skills/implement/orchestration.md:91-94` told the orchestrator the same
after its own fold commit. `frame/design.md` G8 (`:18`) reads both as
citing "a reading of whole files, which only R5 states", and this diff had
to re-point both for that reason. `frame/plan.md` *Alternatives considered*
row 2 (`:26`) is careful to name only "a tracer, a sealer and a first-frame
framer" as agents that act on none of it. `frame/plan.md` *Technical
context* (`:19`) names two more parties that fix and relied on that
sentence, and `frame/questions.md` Q1 and the second `gaps.md` row exist
to measure them. The fragment's claim contradicts all three.

The fix states the claim the frame makes. It covers both statements in the
fragment. No other file states it: `trail/phases/phase-1.md` and `pr.md`
make no claim about who acts on the sentences.

```markdown
- **Contract rule 12 no longer defines what a fixing party reads whole, and no longer addresses the proofer, so every agent preloads 822 bytes less (#1472).** Every agent spawn preloads `skills/agent-contract/SKILL.md`. Rule 12 also said which files a fix reads whole, why that list is never a sample, what is not the proofer's share, and how the proofer reads the fixing party's account. A tracer, a sealer and a framer writing a first frame act on none of those sentences. The framer's and the orchestrator's folds cited the first of them, and now cite rule 12's second method. The rule now keeps the class, the three methods that make a list whole, and where a list stays a sample. It still says what a hand-back names: the method and what it listed, a sample called a sample, where the part it did not reach stands, and what was not finished. The contract holds 12,364 bytes, where it held 13,186.
```

```markdown
| 2026-11-11 | Contract rule 12 keeps the class, the three methods and the sample. The closed set a fix reads whole is defined in `agents/crafter.md` *Before you hand back, your range and the work item's records are read whole against HEAD* alone, the proofer's sentence on a fix's account stands in `agents/proofer.md` *Every round reads the work item's records that state the present, whole, against its target*, and `skills/implement/orchestration.md` and `skills/implement/fold-and-reframe.md` cite rule 12's second method | Every spawn of every agent preloaded about 0.8 KB that a tracer, a sealer and a first-frame framer act on none of, and the closed set was defined both in the contract and in the crafter's rule | https://github.com/MichaelYcJo/AgenticSeal/issues/1472 |
```

```seal
verdict: fixed a085980ed
answer: The finding holds: at `0b55462b2` the framer's fold and the orchestrator's fold each cited rule 12 for the reading of whole files, so the crafter and the proofer were not the only parties acting on it. `changelog.md:3` and its *Process changes* row now hold the round's paste-ready text word for word, which states the claim `frame/plan.md` *Alternatives considered* row 2 makes.
```

## Confirmations

What matched: the five texts went in as `frame/design.md` *Data &
interfaces* gives them. T1 and T2 stand at
`skills/agent-contract/SKILL.md:149-154` and `:202`, T3a and T3b at
`agents/crafter.md:193-194` and `:200-201`, and T4 and T5 at
`agents/proofer.md:123-124` and `:138-142`, each compared word for word
with the frame (read).

What matched: S1 holds. `wc -c` printed 12,364 for the contract, 11,411 for
`agents/crafter.md` and 10,964 for `agents/proofer.md`, against 13,186,
11,299 and 10,746 at `0b55462b2`, so the changes are 822 B less, 112 B more
and 218 B more, as G11, `trail/phases/phase-1.md` and `changelog.md` state
(executed).

What matched: S2 holds. `git grep -n -e 'closed set' -e 'states the present' -e "proofer's share" -e 'finding on the method' -- skills/agent-contract/SKILL.md`
printed nothing, exit 1 (executed). Rule 12 holds R1 to R4 and T1, and
rule 19 holds T2 (read).

What matched: S3 holds. T1 lets a list stay a sample only where no method
makes it whole, and no sentence of rule 12 lets a list a method could make
whole be handed on (read).

What matched: S4 holds. `git grep -n 'states the present' -- skills/core skills/agent-contract agents`
printed `agents/crafter.md:182` and `:186` alone (executed).

What matched: S6 holds. A search with whitespace collapsed for
`asks\s+of\s+the\s+party\s+that\s+fixes` over every tracked file outside
`seal/` names `skills/code-review/orchestration.md:73` alone at
`1ea4a8eb0`, and at `0b55462b2` it names both skill files as well
(executed).

What matched: S8 holds. `git diff --stat 0b55462b2...1ea4a8eb0 -- ':!seal/'`
lists the five files of *Scope* items 1 to 6 and the two test files of item
7, and no other (executed).

What matched: S7 holds. The seven modules S7 names passed through
`bin/test`, 390 passed, exit 0 (executed). `uvx ruff check` and
`uvx ruff format --check` over the two changed test files exited 0
(executed).

What matched: the new case reads its clause inside the proofer's rule
alone, from its lead to the lead of *A verifying round answers the closed
findings*, so deleting the sentence or moving it out of the rule fails its
last assertion. The crafter's two new clauses are asserted against the
crafter's rule paragraph the same way. This round read the red account in
`trail/phases/phase-1.md` against the assertions and did not re-run
`seal mutate` (read). No other case pins the proofer's rule on the records
(executed: `git grep -n -E "Every round reads|records that state the present|first reader of each sentence|alike open" -- tests evals`
printed only the new case's lead), so the case covers a fact its group does
not.

What matched: the phase record's sample of the other statements is a
sample, and called one. This round made its own list of citations of rule
12 by number, a line search and a search across wrapped lines over every
tracked file outside `seal/` (executed). That list is whole for citations
that use the number. Each hit cites rule 12 for the class, the three
methods or what a hand-back names, which R1 to R4 and T1 still state. Two
hits were weighed and hold. `skills/code-review/orchestration.md:68-74`
cites rule 12 for a hand-back carrying "the method of its read", which T1's
"names the method and what it listed" still asks, and `frame/design.md`
*Scope* item 11 keeps it. The docstring at
`tests/text/test_a_moved_rule_leaves_its_definition.py:568` cites rule 12
for the reading of the range and the records, which reading whole as the
second method still covers. A phrase search with whitespace collapsed for
"proofer's share", "finding on the method", "closed set", "states the
present", "never a sample", "reach of your own", "each part's method" and
"verifies it on its own" found no statement of R5 to R11 left outside the
lines this diff wrote (executed). `agents/crafter.md:69-70` step 10's "each
part's method" is the crafter's own wording of its read and its search, and
cites no rule 12. A paraphrase in other words is outside what any search
here reaches.

What matched: the crafter case's docstring says "the one party that reads
the set holds" (`tests/text/test_a_moved_rule_leaves_its_definition.py:496-497`).
That holds by `frame/plan.md` *Alternatives considered* row 5, which says
the orchestrator and the framer each read a set of their own. It is not the
claim of finding 2, which concerns who acted on the contract's sentences.

What matched: T4's "the files step 3 reads whole" has one referent. Step 3
attaches "each whole at the target" to its list of eight files and reads
`trail/phases/` and the earlier rounds after it, for their coordinates
(`agents/proofer.md:30-35`, read).

What matched: the two frame statements phase 1 named were folded at
`2a918188d`. G12 now places `test_no_definition_carries_a_sections_own_sentences`
and `test_the_proofer_checks_its_record_in_the_branch_worktree` in
`tests/text/test_a_moved_rule_leaves_its_definition.py` (`:161` and `:349`
at `ebe6ceed3`), and S6 now searches with whitespace collapsed (read).

What matched: each of the five quotes in `pr.md` stands word for word at
the source its coordinate names: rows 1, 3 and 6 of `frame/plan.md`
*Alternatives considered* and both rows of *Judgments of the run* (read).
`changelog.md` lines 4 to 6 state what the diff does, and their byte counts
match the measured ones (read; executed `wc -c`). `gaps.md` is new in this
range, so no row left it. Its two `## Not verified` rows name their
answerers (read).

What matched: the crafter's rule paragraph after the reflow keeps a short
line, "removed, by `git grep` on its words" (`agents/crafter.md:196`). It
reads the same and passes `tests/behaviour/test_docs_line_wrap.py`, so it
is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at `1ea4a8eb0`: the full suite, the repository-wide lint and the typecheck. `gaps.md` labels it `unverified`, which this round confirms is honest: the phase ran a boundary set and this round ran S7's modules alone | `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/gaps.md:7` | the orchestrator, by `seal gate --record` after the rounds settle |
| Whether a party that fixes without the crafter's definition still reads its diff and the work item's records whole under the new rule 12. This is the conduct of sessions under the released text, which no read or run here shows | `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/frame/questions.md:17` | a measurement, as Q1 states |
| The red runs of contract rule 15 at `fdb208fed` and `3acdc8065`. This round read the assertions and did not re-run `seal mutate` | `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/trail/phases/phase-1.md:18-26` | the sealer, whose sample of the crafter's claims may take one |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the seven modules S7 names | 390 passed, 2 warnings, exit 0. The warnings name `docs/running/the-review-and-parity-arms.md:56` and another work item's pending rule change |
| `uvx ruff check` and `uvx ruff format --check` over the two changed test files | exit 0 each |
| `wc -c` of the contract, `agents/crafter.md` and `agents/proofer.md` at `1ea4a8eb0`, and of the same files by `git show 0b55462b2:<file> \| wc -c` | 12,364, 11,411, 10,964; 13,186, 11,299, 10,746 |
| `git grep -n -F "pr.md" 1ea4a8eb0 -- agents/crafter.md skills/implement/fix-pass.md` | no line, exit 1 |
