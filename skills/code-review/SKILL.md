---
name: code-review
description: |
  Two-stage review methodology (compliance, then quality) with comparison axes,
  cross-session review records, and re-review inheritance.
  Use when: reviewing a PR or diff, re-reviewing after fixes, orchestrating reviewer agents.
  NOT for: implementing fixes (use `implement`), style-only linting a formatter
  can do, or a plain bug-and-cleanup sweep of a diff — Claude Code's built-in
  `/code-review` covers that. This one judges compliance before quality and
  carries earlier rounds' coordinates across sessions.
---

# code-review — compliance first, then quality

Assume the code has defects, and look for them. A pass with no grounds is
forbidden: where you are unsure, write a question, not a pass. A session
orchestrating a review run reads `skills/code-review/orchestration.md` before
round 1.

## Two stages, in order

1. **Compliance**: the code against the documents that outrank it, the
   `docs/` policies first and then the work item's SDD set under
   `seal/threads/`. Look
   for behaviour that is missing and for behaviour nobody asked for. Read the
   code, not the implementer's report of it.
2. **Quality**, only after stage 1: correctness, error handling, security,
   performance, test quality.

The work item's `gaps.md` arrives in the diff and is the implementer's
account, so stage 1 governs it. Its divergences, its `## Not verified` rows
and the clauses it fed back into the design are claims to check, and an
account citing a clause it added is citing itself. Settle what you can; what
only a person can answer stays a question. Do not edit it.

Review beyond the changed files: new code that calls into untouched files
puts their conditions and boundaries into effect for the first time, so
follow every call the change introduces.
check: evals/behaviour/proofer/rule-proofer-one-finding/

## Comparison axes

Fix the axes before starting and cover all of them.

| Axis | Compare |
|---|---|
| Inputs | names, types, required/optional, defaults, accepted ranges |
| Authorization | who acts/queries as whom; self/admin/other branches |
| Query scope | which set is targeted: period, ownership, status filters |
| Exclusions & boundaries | excluded states, overlap conditions, **boundary values** (rarely written down — most frequent divergence point) |
| Deliberate non-exclusions | what the policy or the design intentionally does *not* filter; new code tends to "clean it up" |
| Ordering, dedup, response shape | sort keys, tie-breaking, dedup basis, included/excluded fields |
| Error paths | failure conditions, codes, messages; failure vs. empty result. Count **new failure paths the change introduces** separately — someone must classify each as fix or regression |
| State transitions | against the state machine the policy or the design states, if one exists |
| Concurrency & atomicity | what can change between the read that decides and the write that acts: state held across an external call or `await`, transaction boundary against lock scope, whether a retry executes twice |
| Security | who can reach this path and as whom; the trust of every input that crosses an OS or process boundary; whether each failure fails open or closed; what a crafted name, path, or payload reaches |

The last two rows are not settled by following one request end to end: one
asks what a second actor does while the first is mid-flight, the other what
an input nobody sends in good faith does.

### The table is a floor, not a ceiling

An axis nobody wrote down leaves no trace when it is skipped. So
name this change's own axes before starting: money and rounding, time zones,
resource lifetime, migration ordering, pagination while writes land, whatever
the diff touches. Walk them like the rest. An axis you could not judge is a
row of `## Not judged`, never a silent pass.
check: tests/text/test_review_axes.py

## Probes and regression tests

| | What | Handling |
|---|---|---|
| Probe | a temporary test that settles what reading cannot | you write it, run it once and delete it, named `test_tmp_*` — and everything else it made goes with it; what it settled goes into the record's `## Probes` |
| Regression test | a test that should exist and does not | you do not write it: it is a `should` finding whose `location:` names the file it belongs in |

Contract rule 7 is about leavings, not files: a worktree, a branch, a clone or a
virtual environment a probe made for itself goes too. Batch the probe cases
into one file and run it once. Never probe what reading answers: a schema
constraint, an enum or a default settles whether a state can exist. Leave a
`test_tmp_*` file another session made alone.

A fixture chain is `&&`, never `|`: a pipe feeds one command's output to the
next instead of ordering them, and the chain can sit waiting on stdin with
nothing arriving. Give any call that could run long a timeout you chose
rather than one you assumed.
check: tests/behaviour/test_a_probe_that_commits_says_so.py tests/text/test_a_probe_does_not_outlive_its_round.py

## Earlier rounds

Read the work item's earlier `trail/rounds/round-*.md` before starting. What
carries is **where to look, not what was concluded**: open the coordinates
an earlier round names instead of searching again, and reach your own
verdict on the code as it stands, since a fix made for round 2 can break an
axis round 1 found clean. Every finding the round before closed
`fixed <commit>` or `rejected` is answered this round, by a `confirms:` line
where the close holds, and where it does not by a finding naming it on a
`reopens:` line, or on a `regression:` line where a fix pass's commit
introduced the defect. Where you weigh an earlier finding, re-run its
`evidence: executed` line rather than re-deriving the claim; a probe it names
is written again from its `## Probes` row. A record written before the
`evidence:` row lacks the line, and that is no finding.
check: tests/text/test_review_axes.py tests/text/test_the_rules_have_one_owner.py

## The record

A round writes `seal/threads/<work-item-id>/trail/rounds/round-N.md` from
`templates/records/sdd-round.md`. Every labelled line and heading follows its row of
the grammar table in `docs/the-review-record.md` *The round record*, which
the check reads; that section is the grammar's one statement. The prose follows
`Record language` in the `seal/` root's `config.md`, English where the row
is absent; field names, headings and vocabulary words stay English
(`templates/setup/config.md` *What no row governs*).

- A finding is a defect. `must` is a compliance violation or a defect to fix
  before merge; `should` is a defect the release would ship, a tool doing
  something wrong or telling a person something wrong, to fix or say why
  not. A wrong sentence an agent reads and acts on is `should`; a sentence
  that only reads badly is no finding.
- `location:` names every place the defect shows, and the path the fix
  changes where that is elsewhere, because a `fixed` commit must touch one.
- Each finding carries one line of each row the table places in a finding
  as `one`: `severity:`, `location:`, `evidence:`, `verdict: open` and
  `answer:`, the last left empty for the fix pass. The check refuses a
  finding missing any.
- `evidence:` names what the claim rests on, in the forms its row gives. A
  claim that something is absent rests on a search, so its line is
  `executed`. The check cannot tell such a claim from another; the round
  reading the record does.
- Each finding gives why it matters and its grounds, then the paste-ready
  fix in a fenced block, then its `answer:` line. The grounds open with why
  the earlier close does not hold where `reopens:` stands.
- What this round confirmed holds is a `confirms:` entry, and what it could
  not judge a row of `## Not judged` naming who answers it; neither is a
  finding.
- The record is written in words: no emoji anywhere in it, and no summary
  block under it. A mark quoted from the code under review is written as its
  code point (`U+1F7E1`) or in words, never as the character.

check: tests/skills/test_chain_check.py tests/text/test_the_record_is_written_in_words.py evals/behaviour/proofer/rule-proofer-one-finding/

**Paste-ready means the snippet cannot mislead on its own.** Mark a name the
tree does not have at the line that uses it:

```python
if requester != order["paid_by"]:   # NAME NOT IN TREE — no order schema found
    raise PermissionError(...)
```

Where too many names are missing, describe the change in sentences and say
which document would have to exist. A fix touching an OS boundary — path
resolution, file modes, symlinks, a subprocess's working directory, encoding
— states the precondition it assumes beside the line, or says it has none.

**A finding is not closed too early.**

- An enumeration over an unbounded domain, of keywords, spellings or
  constructs, narrows a finding and does not close it; the verdict says so,
  and the limit goes to the skill's Known limits or a `deferred <home>`.
- A mutation score licenses *tested*, never *safe*: say so where the number
  is reported.
- A claim a fix writes into a document closes when a test pins the document,
  not when the sentence lands.

check: none reader: the next round
