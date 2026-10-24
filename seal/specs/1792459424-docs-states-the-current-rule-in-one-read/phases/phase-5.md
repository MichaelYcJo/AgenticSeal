# 1792459424-docs-states-the-current-rule-in-one-read — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 86723699 |

## What this phase was asked

`docs/worktree-guard-spec.md` rewritten to the current rule, once, and split
along its own `##` headings only if still past 25000 estimated tokens after
the rewrite, each new file on a `docs/README.md` row. The guard group's
backlog specs read, what they decided and `docs/` lacked written in, their
rows closed by the closers of `spec.md` *Data & interfaces*, and a no-change
block added. At the boundary the six checks of phase 4, S14 for every moved
section's citations in `skills/`, `agents/` and tests, every test file naming
the document, the seven meta modules, `bin/rules --check`, `bin/fold-check`
and ruff.

## What this phase found

- **No split.** The rewrite took the document from 67,274 bytes to 42,849,
  about 21,400 estimated tokens, so it stays one file and `docs/README.md`
  gains no row. Every check line kept its targets: the S7 comparison at
  930ee5e9 names the same eight paths before and after.
- **Pins that carried an issue reference.** Four pins in
  `tests/test_guard_resolves_the_tree_it_judges.py` held a sentence with
  "since #826", "since #780", "the class is decided in #886" or "the guard
  stops more than it did". Three were rewritten to the new sentence and one,
  `left with #826`, was retired with the history it pinned. Each new pin is
  absent from the old text, and two were mutated with `mutation-check` and
  went red. One test docstring cited the old heading *Which tree, when the
  command walks to it* and now cites *Which tree*.
- **The census.** Each rule the old text stated, and where it lives now.

  | Old rule | New home |
  |---|---|
  | Premise | the document, unchanged |
  | *A*'s table, `[shared-tree-ok]`'s lead | *A*; "a blanket deny locked out extension hosts" becomes "locks some hosts out" |
  | The tracked-changes row's two readers (#894) | *A*; the issue gone |
  | Why the row's sentences predict nothing; three review rounds of 1791779434; sixteen setups | *A*, one paragraph; the rounds and the setups gone |
  | The two failure directions | *A*; the stop's "stops more than it did" reworded without the comparison, and the 31,193, 315 and 55 counts gone to 1791270162's records |
  | The three shapes (#826); the stop for an unrecognised shape; its two readers; the trees | *A*; the issue gone |
  | *B*'s table | *B*, cells shortened |
  | The Agent path counts nothing, asks once, reads no token (#8); the two token attempts that failed | *B*, one bold paragraph; the attempts gone |
  | The first creation is the question (#237's six creations) | *Creation consent*; the measurement one clause |
  | The token and record table; the four-column table (#604) | *Creation consent*, one four-column table; "measured twice" gone |
  | "*Creating a worktree always takes one confirmation* becomes *the first creation takes one*" | gone as history |
  | What is read, five rules | *Creation consent*; rule 5's round and the owner's settlement gone |
  | The record's six properties (#868's before and after) | *Creation consent*, six bullets; the before and after gone |
  | Why the allow is bounded; a segment is more than its command word (round 1's eleven shapes); exact equality (round 2's basenames) | *Creation consent*, one paragraph; the rounds gone, one example kept |
  | The command-word groups; `nice` before #670; #674, #689 and #826 | *Creation consent*, two groups; the history gone |
  | A creation the guard never judged used to mint the record; reading row 2 twice; the other order (#620) | *So the creation is judged between the ladder's two halves*, with its table; the executions and issues gone |
  | The `if not top` exit; the property; the Agent path's silence; what does not change; the prompt budget (re-measured after round 2) | *Creation consent*; the round gone, the deny-then-five-allows reading kept |
  | Decided before git runs (#692, its round 1, P6); recorded from the command that ran | *Decided before git runs*; the references and "as 0.16.0 judged it" gone |
  | Choice sites, the two branches, once per session per direction, the marker, unwritable counts as asked | *Choice sites*; "(measured)" and the review-skill-gate cross-reference gone |
  | Under the press (#896, #903) | *Choice sites*, *Under the press*; the issues gone |
  | Retry tokens as bare words; the substring and per-segment histories; the unquoted residual | *Choice sites*; the histories gone, the residual kept |
  | Where the token is read from (#780, #773) | *Choice sites*; the issues gone |
  | The token table; the check before the choice sites; each choice hands back the other token | *Choice sites*; the measured cost of the missing half gone |
  | What `[shared-tree-ok]` cannot reach, and the standing of a token (stated twice) | *Choice sites*, once |
  | Declared work streams; the activity table (2026-05-06); five minutes against the earlier sixty; passive events (observed live); identification (the Cursor misattribution, #896); unknowns | the same sections; the dates, observations and earlier design gone |
  | Which tree: the tracked row until round 1 of 1790550712; read as `86256492` read it (#674, #689, #826, #780); one answer where the gate takes all; the cost (round 2 of 1790660768); a broken reader costs a stop | *Which tree*, naming `hooks/cmdline_base.py` and the case that pins it; the history gone |
  | Candidate C (#678) and the option and lookup readings (#764, #738, #790) left with #826 | gone as history |
  | #692 decided this reading on the owner's answers of 2026-10-01; M1 | *Decided before git runs* and the first known limit |
  | The advice follows the tree; two fallbacks; a `-C` naming no repository; the gate stops instead | *Which tree* |
  | Known limits: judged by no git (M1, P6); the shell-built word (#856, #886, the brace reader's five rounds); the switch into a new worktree; the unplaceable tree (#686, the 2026-10-03 count, #854); `LEAVES_THE_TREE` (P1); a hidden-spelling creation (#678); `rebase`; a body; a string; an unloaded reader; quotes; Windows (CI run 36978391812); the press (#894's measurement); the loop (M1, P1 (c)); per project; tty atime | *Known limits*; the issues, dates, run numbers and measurements gone, "9 of 395" kept as the count behind the fallback |
  | New limits | *Known limits*: a `/clear` and the harness's transcript shape, a subagent's payload, what a model does after a deny, a live concurrent session, counts from one machine, and the isolation spawn |

- **S14, the renamed headings.** The H1, *A*'s and *B*'s parenthesised
  headings, *Why the Agent path counts nothing*, *Creation consent*'s dash,
  *Decided before git runs (#692)*, *Declared work streams*' dash, the
  activity heading, *What a blocking prompt must show (identification)* and
  *Which tree, when the command walks to it*: `git grep -F` outside `seal/`
  and `changelog/` finds one citation, in
  `tests/test_the_guard_asks_once_per_session.py`, now *Which tree*, and one
  phrase in `hooks/worktree-guard.py`'s docstring that summarises the code
  and cites no heading. Every other citation names *A*, *B*, *Premise*,
  *Creation consent*, *Choice sites*, *Unknowns resolve conservatively*,
  *Which tree* or *Known limits*, which stand.
- **The backlog of this group: 13 specs**, 10 by count and three by title
  (`1791019475` and `1791119071` from ties with phase 4, `1791334956` with no
  test file a rule names). Each gained a no-change block.

  | Work item | What it decided, and where it is | Rows |
  |---|---|---|
  | `1790381327` | written: the press as second consent, the Agent path | 4 closed |
  | `1790550712` | written: the switch after a creation, the sidechain refusal | 4 closed |
  | `1790745049` | written: the frozen reader | 2 closed, 1 open |
  | `1791019475` | overturned by the three shapes; internal: env's grammars | 1 closed, 1 open |
  | `1791089705` | overturned by the three shapes | 1 closed |
  | `1791119071` | overturned by the three shapes | 2 closed |
  | `1791163981` | written: a body token is not read; overturned: the lookup and message search | 3 closed |
  | `1791270162` | written: the three shapes and the stop | 6 closed |
  | `1791334956` | written: `rebase`'s words | 2 closed |
  | `1791384157` | written: one session reader and one placement; overturned: the brace reader | 3 closed |
  | `1791779434` | written: the tracked-changes row's readers | 5 closed |
  | `1791781864` | written: the choice rows under the press | 3 closed |
  | `1791852612` | written: a creation in another clone | 2 closed |

  Beside them, `1790815613`'s M5 closed against the isolation limit, as
  phase 4 said it would. The closers used: the item's own merged pull
  request for a suite row (#622, #633, #691, #745, #765, #788, #803, #850,
  #855, #881, #897, #902 and #916, each read with `gh pr view` as green on
  lint and all three pytest legs); #997's legs for a platform row whose cases
  still exist; 3d78c220 for the message search, the name lookup, the option
  table and the hidden-creation reading it removed; 5ed2966b for the counts
  it took out of the document; ce448bbe for the stale durations, where none
  of the 383 guard entries naming no case at 3d78c220 remains; 5b1f6fae for
  the ledger; and the limit sentences above.
- **Q4 for this group: two rows no closer closes, keeping two directories.**
  `1790745049`'s real shell for its cases' shapes, and `1791019475`'s GNU
  `env` that its grammar model was never run against. Each is a run nobody
  owes, and the model is still in `hooks/cmdline.py`. With phase 4's, eight
  backlog directories now stay for an open row.
- **A stale exemption, not this phase's.**
  `tests/test_release_hygiene.py#VERSIONS_OF_ANOTHER_PRODUCT` exempts git
  2.54.0 in `docs/worktree-guard-spec.md`, which the document stopped naming
  before this phase, with the option table at 3d78c220. Nothing fails; the
  hand-back names it.
- **The checks at the boundary (executed):** `bin/fold-check` exit 0, one
  document past the ceiling, `docs/one-root-by-lifetime.ko.md`, which is
  phase 9's; `bin/rules --check` exit 0, 240 lines; the S7 comparison;
  `unverified_check.py` over the 13 directories, 2 open; `bin/settle
  --released-at HEAD` lists 11 of them as nothing to apply and holds two for
  their rows; the 13 modules naming the document or its check targets 557
  passed and 3 skipped, and the meta and record modules passed; ruff clean
  over the two changed test files.
