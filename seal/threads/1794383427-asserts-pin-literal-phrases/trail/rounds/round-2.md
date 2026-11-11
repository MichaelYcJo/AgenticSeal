# Review round 2: 1794383427-asserts-pin-literal-phrases

```seal
target: 21ca6ecff, fixes ea1328097..21ca6ecff
```

This is a verifying round. Its code bound is the diff from `ea1328097`, the
commit of round 1's record, to `21ca6ecff`. That range holds the framer's
fold `d664a9194`, the fix pass's commits `3368a3111`, `4864f032d`,
`e94c791e9` and `e1375088c`, and the orchestrator's records commit
`21ca6ecff`. Ten test modules changed in it. The base is `dbed1d5ff`, the
merge base of HEAD and `origin/release/v0.37.4`.

What was read whole at `21ca6ecff`: `routing.md`, the three frame files,
`gaps.md`, `changelog.md`, `pr.md` and round 1's record. No `pr.<lang>.md`
stands, since `Commit and pull request language` is English. Every hunk of
the ten modules in the range was read. The phase records were read only at
the coordinates round 1 and the frame name; none of them changed in the
range.

Carried from round 1, not re-established: the counts at `18a7e18fb`, the
per-phase ledgers, S3 for the phases' diff, and the kept absence asserts
outside the listing (`AskUserQuestion`, the `Planning` row). Re-taken here:
the counts at HEAD, the narrow run, the lint of the ten modules, `seal rules
--check`, the parse of `## Rule changes`, and the mutants the close blocks
claim.

Two things in the fix diff are named here and are not findings:

- `3368a3111` also removed `assert not stale`, the absence of a concrete
  `release/v<n>.<n>.<n>` in the `::error::` line, at
  `test_the_release_check_watches_what_ships.py:207-212` at `ea1328097`.
  Neither round 1's close of finding 2 nor the commit message names it. Its
  removal follows design *The criterion*: `.github/workflows/hygiene.yml`
  holds no rule that forbids a concrete branch in that line, so its absence
  has no rule of that text to cite. The gaps row of fix pass 1 covers it,
  since its case was open.
- The section comment the fix pass wrote at
  `test_the_release_check_watches_what_ships.py:159-168` ends "Its sentences
  are the proofer's to read". Yet `test_the_refusal_asserts_neither_case` at
  `:214-222` still counts the phrase `If this is` twice. That case holds no
  listed assert, so it is *Out*, and the comment claims slightly more than
  the module does.

## Findings

### 1. The fold left three statements of the absence rules that give the answer it rejected

```seal
severity: should
location: `seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md:157`, `seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md:238`, `seal/threads/1794383427-asserts-pin-literal-phrases/frame/plan.md:24`
evidence: read `frame/design.md:157`, `:159`, `:161`, `:238`, `frame/plan.md:24`, `agents/sealer.md:85-87`, `skills/implement/orchestration.md:81`; executed design *The listing* at HEAD, which lists `'/tmp/run.txt' not in text`, `` '`.git/seal/`' not in bootstrap() `` and `'seal stamp --from' not in text` among 21 absence asserts, and `git log -S"/tmp/run.txt" -- skills/verify/SKILL.md`, which names `1404b3a7` as the commit that removed it
reopens: round-1#1
```

Why it matters: round 1's close of finding 1 holds for the tree. The fold
`d664a9194` added the precedence paragraph at `frame/design.md:161`, and the
fix pass ruled by it. It kept `seal stamp --from`, restored `/tmp/run.txt`
and `` `.git/seal/` ``, and removed the `copied` absence. The close does not
hold for the frame. The finding was that the frame states the two absence
rules without saying which rules where both apply. The fold added the
answer but left three older statements that still give another answer:

- `frame/design.md:157` ends "Every release up to v0.37.3 has shipped, so
  every such assert at the base goes." Three such asserts stand at HEAD.
  Each is an absence of text a shipped release removed. `/tmp/run.txt`, for
  example, left `skills/verify/SKILL.md` with `1404b3a7` (#549).
- The first row of `## Removes`, at `frame/design.md:238`, removes "each
  absence assert of what a shipped release removed", and says it lands
  "nowhere". `agents/sealer.md:85-87` has the sealer check every `## Removes`
  row and "confirm nothing of it stands in the tree". Read as written, the
  row names three asserts that stand, and the sealer must either withhold or
  read past the row.
- The chosen approach in `frame/plan.md:24` still keeps "the absence a rule
  in force forbids". The fold narrowed that to a rule of that text itself,
  and rejected the wider reading as A14 at `frame/plan.md:37`.

`skills/implement/orchestration.md:81` states the rule the fold missed:
"One fold reaches every statement of the fact it changes." Round 1's
paste-ready fix named only the paragraph and the `to:` line, so these three
statements were outside it.

The frame is the framer's, so the orchestrator sends this as a fold. Each
statement takes the exception in place:

In `frame/design.md:157`, the second sentence becomes:

```markdown
Every release up to v0.37.3 has shipped, so every such assert at the base goes, except where a rule of that text itself forbids the literal (the precedence paragraph below).
```

In `frame/design.md:238`, the first cell of the first row of `## Removes`
becomes:

```markdown
| each assert on a file's text ruled wording, and each absence assert of what a shipped release removed that no rule of that text itself forbids |
```

In `frame/plan.md:24`, the clause of the A1 cell becomes:

```markdown
remove the absence of what a shipped release removed, keep the absence a rule of that text itself forbids
```

The changelog fragment already states the folded rule
(`changelog.md:3`), and so does the `to:` line at `frame/design.md:206`, so
neither needs a change.

```seal
verdict: fixed 5416a887c
answer: The finding holds. The framer's fold at `5416a887c` gives design *The criterion*'s removal paragraph (`:157`) and the first `## Removes` row (`:238`) the exception for a literal a rule of that text itself forbids, and narrows plan A1 to that reading, so none of the three answers the overlap the old way. Reading every frame sentence on absences, it also brought S2, G1 and the #1482, #1484 and #1485 rows of *Overlap with the release* to the same reading. The tests already held it, as this round confirms.
```

### 2. One fold row of Judgments of the run still cites the framer's fold file, which the orchestrator does not act from

```seal
severity: should
location: `seal/threads/1794383427-asserts-pin-literal-phrases/frame/plan.md:82`
evidence: read `frame/plan.md:82`, `:85`, `:87`, `skills/implement/fold-and-reframe.md:3-6`, `skills/implement/orchestration.md:67-68`, `:81-84`; executed `git show 21ca6ecff -- seal/threads/1794383427-asserts-pin-literal-phrases/frame/plan.md`
```

Why it matters: `21ca6ecff` changed the *Judged against* cell of two rows in
`frame/plan.md` *Judgments of the run*. One is the orchestrator folding phase
5's statements itself (`:85`), and the other is round 1's findings going to
the framer as one fold (`:87`). Both moved from
`skills/implement/fold-and-reframe.md` to `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket*. The grounds hold:
`fold-and-reframe.md:3-6` says the framer opens that file and "No other
party acts from it". The row at `:82` is the same kind of judgment. In it,
the orchestrator sent the `docs/` check lines and phase 4's statements to
the framer in one fold. It still cites `skills/implement/fold-and-reframe.md`.
The rule that row applies is `orchestration.md:81-84`, which says the
orchestrator sends every pending decision to the framer in one message. The
settle reads each row against the guidance it names (`skills/core/SKILL.md`
*A judgment stands on a source document, and is written down with both*).
Left as it is, the settle would charge this judgment to a file only the
framer acts from. The commit fixed two of the three rows of the class.

```markdown
| 2026-11-11 | The `docs/` check lines phases 1, 3 and 4 named, and the frame statements phase 4's hand-back names, went to the framer in the one fold after phase 4 | The plan's opening line holds the fold to after phase 4, so the framer reads every such line once | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
```

```seal
verdict: fixed 65407e62a
answer: The finding holds. The row of the fold after phase 4 now cites `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, as the two rows `21ca6ecff` moved do.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: the fold states at `frame/design.md:138` that a printed line read
from its file is a file's text, and plan A15 at `frame/plan.md:38` rejects
the separate kind. `3368a3111` rules the seven listed asserts by *The
criterion*. `release/vX.Y.Z`, `plugin.json` and `CONTRIBUTING.md` stay, each
with a comment naming the fact and its reader
(`test_the_release_check_watches_what_ships.py:195-197`, `:208-209`,
`:230-231`).
The `base` word, the `Change the base rather than plugin.json` sentence, the
skip sentence, its `moves` absence, the order assert and the skip line's
count go. Two cases went and two were renamed. The close claims each kept
assert is red under a mutant of `hygiene.yml`, and that holds (executed).
With the three literals taken out of the `::error::` line, the three cases
fail on their own assert lines and the module's other cases pass. Its account
leaves out the `stale` absence, named above.

```seal
confirms: round-1#3
```
What holds: `e94c791e9` gives the six cases the names round 1 wrote, and
rewrites the docstring of `test_the_reviewer_points_at_the_edit_rule`
(`tests/text/test_edits_go_through_the_edit_tool.py:78-81`). The first-setup
section comment drops "once" (`tests/behaviour/test_first_setup_asks_once.py:274`).
The last case is `test_the_chain_check_loads_the_one_reader`
(`tests/behaviour/test_release_hygiene.py:1305`), since the `split_row`
absence stays removed under the fold. `git grep` on each old name outside
`seal/threads/` finds nothing (executed). The other name it finds,
`..._restates_none_of_it`, belongs to an unrelated case in
`test_first_setup_asks_once.py:580`.

What matched: the fix pass's call to keep the `rm -rf` absence removed. The
case asserted `rm -rf` absent from the contract and every agent definition.
Contract rule 17 forbids an agent to remove the scratchpad, a scratch
directory or a file in one. That is a rule about the target, not the
command. The same text has rule 7, which requires a probe's leavings outside
the scratch directory to be gone, and rule 21, which says how an `rm` is
written. So the contract expects removals, and the literal `rm -rf` hands its
reader no act rule 17 forbids as such. No agent definition's *Never* forbids
a removal command (executed: `grep -n -i "rm\|remov\|delet"` over
`skills/agent-contract/SKILL.md` and `agents/*.md`). Under design *The
criterion* at `frame/design.md:159`, no rule of that text forbids the
literal, so the removal holds.

What matched: the two restored absences. Each comment cites a rule of the
text the assert reads. `/tmp/run.txt` cites `skills/verify/SKILL.md`
*Capture once, filter locally.*, whose quoted words stand at
`skills/verify/SKILL.md:283-284`. `` `.git/seal/` `` cites
`skills/implement/bootstrap.md` *Orchestrator: Bootstrap*, whose **local**
option says the path is spelled through the common git directory rather
than `.git` (`:70-73`). The `.git/seal/` assert now reads that section
(`bootstrap()`, `test_first_setup_asks_once.py:56-57`) where it read three
files at `18a7e18fb` (`both_halves()`), as `gaps.md:64-67` says (read). Each
is red under its mutant, failing on its own line (executed).

What matched: the `copied` absence goes with `_block_keys`, which nothing
else uses (executed, `git grep`). The case is renamed
`test_the_exclusion_list_points_at_the_block_grammar`, its docstring says
what it holds, and the `_literal_strings` docstring names the new name
(`test_the_pull_request_language_is_the_repositorys.py:1083-1085`, `:1126`).

What matched: the absences the build removed and the fix pass left removed,
which `gaps.md:21` hands to this round. All 141 removed lines holding
`not in` in `git diff dbed1d5ff ea1328097 -- tests/text tests/behaviour`
were read by their literal and message (executed). Twelve were opened in
their case at `dbed1d5ff`, chosen because a rule of their own text could
plausibly forbid the literal. They were `"hooks"` in `plugin.json`,
`disable-model-invocation` and `seal stamp --` in skill texts, `refs/pull/`
in the hygiene template, `git reset -- :/seal` in the READMEs, `SEALED` in
the stamp section, `<!--` in `skills/verify/orchestration.md`, `bin/test`
in two definitions, `mv ` in the README's first block, `/Users/` in a
shipped skill, `${CLAUDE_PLUGIN_DATA}/stamp.py` and `--preflight`. None
cites or has a rule of its own text that forbids the literal. Each is
removed text, wording, a one-source rule, or a premise guard of its own
module. The twelve are a sample chosen by judgment. The other 129 were
weighed on the line alone.

What matched: the counts. Design *The listing* at HEAD gives comparisons
455, asserts 434, absence asserts 21, cases 263, modules 66. The two
`git grep -E` forms give 287 and 16. These are the after-build column of
`changelog.md:11-14` (executed). The ledger moves from 315 kept, 237 removed,
113 unchanged to 320, 239, 106. That matches the seven newly ruled asserts
(3 kept, 4 removed) and the two restored absences, and still sums to 665.
`59 cases` is the 57 before the pass and the two the pass removed (read).

What matched: the records. `pr.md`'s five quotes stand word for word at
`frame/design.md:159`, `:161` and `frame/plan.md:81`, `:83`, `:84` (read).
The `gaps.md` row of phase 4 drops the printed lines, and a `closed` row
carries that item, so no row left without `closed` (read, `git show
e1375088c`). The two new fix-pass rows label the suite beyond the ten
modules `unverified`, with the orchestrator's broad gate answering. That is
honest, because the pass claims no wider run. The `docs/` check lines that
name the ten modules each keep a case reading their rule. For example,
`docs/releasing/release-checklist.md:250` is still read by
`test_the_refusal_names_the_branch_a_contribution_goes_to` (read).

What matched: S4, S8 and S9 for the range. `bin/seal rules --check` prints
"all 177 check lines in 69 rule files hold." `rule_changes.parse` returns
six operations, no error and nothing unread. Each `from` stands once in its
section (the pact line once in *When there is a pact at all*, at
`docs/layout/the-pact.md:39`). `bin/test` over the ten modules and
`tests/github/test_rules.py` passes, 323 cases. `uvx ruff check` and `uvx
ruff format --check` over the ten modules exit 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond the ten modules and `tests/github/test_rules.py`, the repository-wide lint and the typecheck | the whole tree at `21ca6ecff` | the orchestrator's broad gate |
| The 129 removed absences weighed on their line alone, for a rule of their own text that this round did not open | `git diff dbed1d5ff ea1328097 -- tests/text tests/behaviour`, the removed `not in` lines | the sealer, where it samples the removals the changelog names |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the ten modules the range changed and `tests/github/test_rules.py`, in a `git clone --no-local` at `21ca6ecff` | exit 0, 323 passed |
| `uvx ruff check` and `uvx ruff format --check` over the ten modules | exit 0 and exit 0 |
| `bin/seal rules --check` | "all 177 check lines in 69 rule files hold." |
| design *The listing* at HEAD | comparisons 455, asserts 434, absence asserts 21, cases 263, modules 66 |
| `git grep -E` the two forms of *The counts* at HEAD | 287 and 16 |
| `test_tmp_parse.py`: `rule_changes.parse(design, "docs")` and the count of each `from` | six operations, no error, nothing unread; each `from` once in its section |
| mutants, applied with `Edit` in the clone and restored with `git checkout`: `plugin.json`, `release/vX.Y.Z` and `CONTRIBUTING.md` taken out of the `::error::` line of `.github/workflows/hygiene.yml`; `` `.git/seal/` `` written into the **local** option of `skills/implement/bootstrap.md`; `/tmp/run.txt` written into *Capture once, filter locally.* of `skills/verify/SKILL.md`; then `bin/test -q` over the three modules | 5 failed, 75 passed; each failure is the named case on its own assert line |
| removed lines holding `not in` in `git diff dbed1d5ff ea1328097 -- tests/text tests/behaviour` | 141 lines |
