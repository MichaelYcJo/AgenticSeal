# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 5a

| Field | Value |
|---|---|
| Phase | 5a |
| Commit | 4632eeea, the last build commit; this record's commit follows it |

## What this phase was asked

`plan.md`'s row 5a, the repair after round 2 and part A's last phase, in
three parts, adding no mechanism. (i) `chain_check.py#open_findings` reads
one fact per row: the `Verdict` cell is a word of `CLOSED_WORDS`, `deferred`
with a home, or the row fails a ready pull request, whatever its `#` cell,
which only names the row in the refusal. `severity_of`, `NOT_FINDINGS`,
`FINDING_CLOSES` and the `ID_COLUMN` lookup leave; `FINDINGS`, `BLOCKING`
and `SHOULD` stay as vocabulary. `TestOpenFindings` rewritten test-first to
T19 and T20, each seen red on 2f0b4460's `open_findings`. Every sentence
stating the severity-keyed rule rewritten in place, the class found by the
row's `git grep`. (ii) `.test_durations` pruned to the ids
`pytest --collect-only -q` collects, by a script run once with 1b875efc's
round-trip guard and deleted, nothing re-measured and nothing new in the
tree; `overview.md`'s S12 row, round 1's 🟡 5 account and the changelog's
suite figure recounted. (iii) `tests/test_one_word_one_meaning.py:472`, five
`.py` members to four. Then this record and the fragment's line counts.
`rounds/round-2.md` is not edited, and part B is out of scope.

## What this phase found

**The frame held at its coordinates.** `chain_check.py` and
`tests/test_chain_check.py` were unchanged since 2f0b4460, so the red run
below is a run against round 2's `open_findings`. Each coordinate the row
lists for a sentence held the severity-keyed rule as round 2 quoted it.

**T19 and T20, red then green** (`executed`, `bin/test` on
`tests/test_chain_check.py -k TestOpenFindings`):

| Run | Exit | What it printed |
|---|---|---|
| before the fix, the new cases over 93903107's `chain_check.py` | 1 | T19: `At index 2 diff: ('4', 'open') != ('🟢', 'open')`, three more items expected — the 🟢, ❓ and ⬜ rows were skipped. T20: `[(11, '🔴 1', 'confirmed'), (12, '🟡 2', 'out of verified scope')] != []` |
| after the fix, at fad5be2d | 0 | the module's 32 cases passed, `TestMain::test_a_record_written_by_the_old_generator_reads` among them |

That last case reads every `round-N.md` in the tree, 37 now with round 2's
own, through the new reading and finds no row open in any of them. It is the
executed form of `spec.md` S3's "the 36 records in the tree read with no
refusal".

**Four breaks of the new `open_findings`, each `red`** through
`mutation-check` on the two cases: `confirmed` dropped from the closing set
(T20 red), the `the row` fallback dropped (T19), a ⬜ row skipped (T19), and
a word outside the set skipped (T19).

**The row's `git grep` cannot come back empty, and what it still finds
states no check rule.** After the rewrite, its four patterns outside
`seal/specs/` find two kinds of line. The released `changelog/0.*.md` files
are history, which nothing rewrites. The rest are the warden's writing
rules: where the severity goes and which rows take an integer id, in
`agents/warden.md:154` and `:268`, `skills/code-review/SKILL.md:217` and
`:221`, and `templates/sdd-round.md:28`. They are true of the record the
warden writes. They say nothing about what the check reads, and part B
writes both files anew. The class was also searched past the four patterns,
for `closes no finding`, `is no finding` and `open finding`. That search
found the comments over the constants, which are rewritten, and the refusal
message `… which closes no finding: a fix pass writes …`, which is left. That
message is pinned at `tests/test_chain_check.py:569`. Most rows it names are
🔴 or 🟡 rows, and for those the fix pass's words it lists are the right
ones; whether a 🟢 row left at `open` needs other words is the next round's
to judge.

**The prune** (`executed`, the one-shot script, deleted with the scratch
directory): 7,574 cases collected; the file went from 7,649 entries to
7,348; 301 dropped, 345.3 s, as round 2 measured. 3,371.9 s are kept, 0
entries are uncollected afterwards, and 226 collected cases are unpriced.
The guard held: the file round-tripped before the write, and every kept line
is the old line in its old order. `git diff --numstat` shows 0 added and 301
deleted. `bin/test tests -q -k test_the_durations_file_prices_the_suite`
then passed, run rather than skipped. A passing run of that case prints no
count, so the plan row's "its output naming 0 entries gone" is the prune
script's own line, which re-read the written file against the collection.

**What was recounted, and what had no figure to recount.** `overview.md`'s
S12 row reads 1,144.7 s over the 42 modules naming `chain_check` or
`broad_gate`, from 1,482 s. Round 1's 🟡 5 account is read as `overview.md`'s
S10-spellings row, the one place outside the round records that tells it.
That row now names both prunes and the 3,371.9 s the file sums to.
`rounds/round-1.md`'s Grounds cell stays as the record at its target, and
round 2's 🟡 2 is what answers it. The changelog fragment carries no suite
seconds: round 2's paste names a "suite-fall sentence" the fragment never
held. So no suite figure was recounted there, and none was added. Its line
counts were recounted: `chain_check.py` 1,110, `templates/sdd-round.md` 46,
`docs/the-review-record.md` 230, tests 31,996 deleted against 3,076 added.

**The checks** (`executed`, at 101343c1, before the count commit and this
record):

| Check | Exit |
|---|---|
| `bin/test` over `test_chain_check.py`, `test_the_pull_request_language_is_the_repositorys.py`, `test_one_word_one_meaning.py`, `test_the_release_table_reads_two_trees_and_fails_nothing.py` (`-q -rs`) | 0, 157 passed, none skipped |
| `chain_check.py --baseline origin/release/v0.22.0 --root <worktree>` | 0. The pull request's state was unknown, so nothing was judged as ready. It printed no row refusal. It printed three lines that are owed later: round 2's `Target SHA` is behind fad5be2d, so a verifying round is owed, and there is no `broad-gate.md` and no `guarantee.md` yet, which are the sealer's |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` | 0, 1 passed |
| `bin/rules --check --root <worktree>` | 0, all 400 `Enforced by:` targets in 60 rule files resolve |
| `ruff check` and `ruff format --check` on the three touched `.py` files | 0 and 0 |
| the full suite | not run: `unverified`, the sealer's |
