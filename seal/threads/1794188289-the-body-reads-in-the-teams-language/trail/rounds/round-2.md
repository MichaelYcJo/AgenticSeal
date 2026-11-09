# Review round 2: 1794188289-the-body-reads-in-the-teams-language

```seal
target: f2b29c48, fixes 1677d096..f2b29c48
```

This is the verifying round over round 1's fix pass. The fix diff
`1677d096..f2b29c48` was read whole: `78f083c8`, `f71c31ba`, `a98be282`,
`614769a7` (round 1's close blocks) and `f2b29c48`. The work item's
`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`
were read whole at `f2b29c48`. Of those, only `frame/design.md` changed in
the range. The other six stand as round 1 read them, and nothing in the fix
diff contradicts a sentence of theirs. No `pr.<lang>.md` is owed: both
language rows of `seal/config.md` read `English`.

Carried from round 1, not re-established: the coordinates of the four
sentences of finding 2, of `lib/config.py:557-558` for finding 3 and of
`frame/design.md:127-132` for finding 1. `pr_body.py#first_part` is not in
the fix diff, so round 1's reading of where it lives was carried. Its order
for each case was read again at `skills/code-review/scripts/pr_body.py:472-482`,
because finding 1 below rests on it. Every verdict below was reached this
round.

No `seal/parity.md` is declared. The fix diff adds no test case. It changes
two comments and one docstring of existing cases, so no new test is read
against its group.

## Findings

### 1. The `pr.md` line of the two README trees puts `pr.md` after any `pr.<lang>.md` that stands, which the composer does only where the rows differ

```seal
severity: should
location: `seal/README.md:99-100`, `templates/setup/seal-README.md:99-100`
evidence: read `seal/README.md:99-102`, `templates/setup/seal-README.md:99-102`, `skills/code-review/scripts/pr_body.py:429-482`, `tests/skills/test_pr_body.py:1113-1123`, `frame/design.md:42`, `frame/design.md:92`; executed `git diff 1677d096 f2b29c48 -- seal/README.md templates/setup/seal-README.md`
regression: round-1#2
```

The unit is the `pr.md` line of the work item's tree in `seal/README.md`
and in its template `templates/setup/seal-README.md`, which `f71c31ba`
rewrote. `frame/design.md` *Scope* item 3, which `frame/plan.md` *Phases*
row 2 delivers, says "Where the two values are the same, `pr.md` leads and
one `pr.*.md`, where present, follows it", and *Data & interfaces*
(`frame/design.md:92`) says the same. The fix wrote "the pull request
body's first part, after pr.<lang>.md where one stands", so the defect came
from conditioning the order on the file being present rather than on the
two rows differing, as every other statement the same commit rewrote does.

Why it matters: in a repository whose two rows name one language and whose
work item holds a `pr.*.md`, the composer writes `pr.md` first and the file
after it (`pr_body.py:477-478`), and the case labelled "one language and a
pr.en.md" pins that order as "`pr.md` then `pr.en.md`"
(`tests/skills/test_pr_body.py:1115-1123`). The README line says the
reverse. The line two below it, the `pr.<lang>.md` line, states the
condition correctly ("opening the first part where the two language rows
differ"), so the tree gives two orders for the same case. A
reader of the root's README who finds a stray `pr.*.md` in a one-language
repository reads it as opening the body, which `seal pr-body` does not do.
Round 1's close of finding 2 names this line among the statements its census
rewrote, so the class search reached it, and the rewrite is where the defect
came in.

In both `seal/README.md` and `templates/setup/seal-README.md`, which the
suite holds equal, replace lines 99-100 with:

```text
    ├── pr.md              the pull request body's first part, after
    │                      pr.<lang>.md where the two language rows differ;
    │                      read by every round
```

The snippet covers both statements of this fact. The other sentences that
say "where one stands" do not state an order: `agents/sealer.md` in its
`description` and step 2, and `skills/code-review/orchestration.md:468-470`.
They need no change.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `frame/design.md:127-133` now opens and closes each code span
on one line. `chain_check.py --baseline origin/release/v0.36.0 --worktree`
over the branch worktree printed no line at `frame/design.md`, so
`## Rule changes` parses, and no test pin or copy notice stands behind it
(executed). The operation's `from:` and `to:` are otherwise as round 1 read
them (read: `git diff 1677d096 f2b29c48`).

```seal
confirms: round-1#2
```
What holds: each of the four sentences round 1 located now names
`pr.<lang>.md`, or stops calling `pr.md` the whole first part, in the
sentence that states it. At `skills/code-review/orchestration.md:402-405`
the bold lead names both files and points to the paragraph at line 428. At
`skills/commit-pr-convention/SKILL.md:237-239` the first part is "`pr.md`,
opened by its mirror where the two rows name different languages (below)",
and line 267 agrees. At `templates/setup/config.md:92-96` the sentence now
says only that `pr.md` stands in the first part. At `lib/optin.py:58-60`
the comment names `pr.<lang>.md` where the rows differ (read). The fix pass
claimed a census over more wordings. This round's own search, `git grep -i`
for "first part", "above the line", "body opens", "opens the body", "opens
with `pr", "above the heading", "orchestrator's part" and "앞부분" over `skills`,
`agents`, `templates`, `lib`, `hooks`, `bin`, `.github`, `evals/scripts`,
`tests`, the root documents and `seal/README.md`, found no other statement
of the first part as `pr.md` alone outside a one-language fixture's own
comment (executed). Some sentences say `pr.md` is the first part of a case
that has one language only, and they hold: `evals/scripts/rule_cases.py:124-125`
and `:830`, and the docstrings of S8 and S9 at `tests/skills/test_pr_body.py:905` and
`:929`.
`skills/implement/SKILL.md:284`
and the two Korean sentences `a98be282` rewrote in
`skills/writing-style/outside-the-review.md:22-28` and `:72` state the order
and condition `pr_body.py#first_part` gives (read). The one statement the
rewrite got wrong is finding 1.

```seal
confirms: round-1#3
```
What holds: `lib/config.py:557-561` now reads "An item with a default
falls back to what every repository got before the row existed", which no
longer contradicts the module docstring's four rows without a default
(`lib/config.py:3-10`) or `templates/setup/config.md:11-18` (read). `git
grep -i` for "row existed", "every other item" and "every other row" over
`lib`, `skills`, `agents`, `templates`, `hooks` and `bin` found the other
hits naming one row each, `lib/config.py:611`, `:628` and `:679`, or the
template's opening, which names the four exceptions (executed).

What matched: the two `## Removes` rows `f2b29c48` added
(`frame/design.md:249-250`) name coordinates the fix diff rewrote, each
read at its path: the bold lead of `skills/code-review/orchestration.md`,
`skills/commit-pr-convention/SKILL.md` *Pull request bodies*,
`templates/setup/config.md`, the `PR` comment of `lib/optin.py`, the
`pr.md` lines of both README trees, the `pr.md` row of
`skills/implement/SKILL.md`, the two Korean sentences, and the
`declared_mode` docstring. The removed wordings, "Every other item in
`config.md` falls back to" and "the pull request body's first part, read by
every round", return nothing outside `seal/threads/` and
`tests/text/test_the_chain_section_has_one_shape.py:4`. That module
docstring tells the history up to #1415 and states no present rule
(executed: `git grep`).

What matched: every quote of `pr.md`, twelve in all, stands word for word,
with runs of whitespace collapsed, at the record its coordinate names
(executed: `## Probes`). Each coordinate names the item or row that holds
the quote (read: `changelog.md:3-8`, `frame/plan.md:108`, `gaps.md:8`).

What matched: the narrow run over the twelve modules that cover the files
the fix diff changes passed, 719 cases. The modules are the cases of `pr.md`
and the body, of the language rows, of the README trees, of `lib/optin.py`
and `lib/config.py`, of the line wrap, of the writing-style sections and of
the rule-changes parser (executed). The suite as a whole is `unverified`,
as `## Not judged` says.

The fix pass's text edits to test comments and a docstring
(`tests/skills/test_pr_body.py:243-245`, `:589-593`,
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:256-257`)
change no assertion, so they hold no fact a case did not already hold, and
no case gap follows from them.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite as a whole, the repository-wide lint and the typecheck: `unverified`, since contract rule 2 leaves the broad gate to the orchestrator | the `Broad gate` row of `seal/config.md` | the orchestrator, at `seal gate --record` once the rounds settle |
| Round 1's other three rows of `## Not judged`, the two `gaps.md` *Not verified* rows and whether the settle owes `docs/layout/one-root-by-lifetime.ko.md` the added sentences: the fix diff touches none of their coordinates, so they stand as round 1 wrote them | `trail/rounds/round-1.md` *Not judged* | the repository owner and the settling session, as round 1 names them |

## Probes

| Command | Result |
|---|---|
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.36.0 --root <worktree> --worktree`, before this record was written | exit 0; no line at `frame/design.md`; lines owing a verifying round for round 1's findings 2 and 3 and for `f71c31ba` past the last target, and the gate record and the guarantee not yet in git |
| `bin/test tests/skills/test_pr_body.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/lib/test_optin.py tests/lib/test_config.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_records_can_be_carried_out_and_in.py tests/text/test_a_language_section_of_writing_style_opens_alone.py tests/text/test_the_chain_section_has_one_shape.py tests/skills/test_rule_changes.py -q`, in a `git clone --no-local` at `f2b29c48` under `<scratchpad>/1453-r2/clone` | exit 0, 719 passed |
| `python3 -I <scratchpad>/1453-r2/test_tmp_quotes.py <the clone's work item directory>`, a script comparing each quote of `pr.md` with its source file, runs of whitespace collapsed | exit 0, 12 of 12 found |
