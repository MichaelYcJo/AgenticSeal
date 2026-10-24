# 1792459424-docs-states-the-current-rule-in-one-read — phase 6

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | 813031e9 |

## What this phase was asked

The review and records group rewritten to the current rule, once:
`docs/the-review-record.md`, `docs/the-record-layout.md`,
`docs/the-reader-registry.md` and `docs/the-agent-set.md`. The group's
backlog specs read, what they decided and `docs/` lacked written in, their
rows closed by the closers of `spec.md` *Data & interfaces*, and a no-change
block added. At the boundary the six checks of phase 4, every test file
naming a rewritten document, the seven meta modules, `bin/rules --check`,
`bin/fold-check` and ruff.

## What this phase found

- **Three of the four documents were already written as the current rule,
  so they were edited in place, not rewritten.** The review record and the
  record layout were written anew in #923 and since, and 23 test modules pin
  their sentences; what they still held was issue history, a release's story
  and section signs. `chain_check.py` loads the review record's grammar table
  by its heading and header row, so both stand byte for byte, the `nowhere`
  rows' dash cell included, which is a value the loader reads. The agent set
  was rewritten whole. The reader registry already states one rule with its
  check line and is unchanged.
- **The paste ratchet refused the agent set's numbering rule**, which restated
  the contract's preamble word for word once its history was gone. The agent
  set now points at the contract.
- **A stale citation found beside the rewrite.** `unverified_check.py`'s
  docstring cited `docs/the-record-layout.md` *A marker counts only on a live
  line*, a statement the document did not hold at ac83bdf3 either. It now cites
  *Whether a line is live is asked by what the line does*, the statement that
  says it. `gather_changelog.py`'s same words are its own bold opening, not a
  citation.
- **The census.** Each change, and where the rule lives now.

  | Old text | New home |
  |---|---|
  | The review record: "as #941's will" beside the loader's path | *The round record*, reworded to "a change that moves this heading or the table" |
  | The review record: `skills/agent-contract/SKILL.md` §7; `deferred #956`; §*The round record*; §*One act, one owner*; §*Measure the segment, and feed the flow log* | the same sentences: "the agent contract's probe rule", `deferred #<issue>`, and the italic heading without the sign |
  | The review record: "(#975)", "since #853", "the class #975 accepts" | *The stamp*, the same rules without the issues; the budget pin in `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` follows "and no scale either" |
  | The record layout: the title's dash and "a dozen kinds of record" | the title *The record layout*, and "every kind of record" |
  | The record layout: 0.18.2's three false fragments and #795 | gone as history; the rule *A commit after the build brings its changelog fragment along* stands |
  | The record layout: "(#517)" twice and "(#602)" | gone; the rules stand |
  | The record layout: seven section signs, and §3's table | the italic heading without the sign, `skills/implement/SKILL.md` *3. The SDD file set* |
  | The record layout: "work item 1790645290 was bound to miss no row" | "the walk may miss no row the older reading saw" |
  | The record layout: "`settle` exited 2 on its own finished work" | the same grounds as a condition, "would exit 2" |
  | The agent set: the title's dash; "It is a policy document, with the standing `docs/README.md` gives one" | the title *The agent set*; the index says what a `docs/` document is |
  | The agent set: one rule arriving at round 2 and another at round 3 | the grounds in one clause |
  | The agent set: #957's renumbering of the contract and the edition's rule | *The contract's section numbers are stable*, pointing at the contract's preamble |
  | The agent set: two consequences of the split | the same paragraph |
  | The agent set: the phase that moved a rule to an interim home | gone as history; the rule and its divergence stand |
  | The agent set: the 0.15.0 run's four chains (#544) | gone as history; the naming rule stands |
  | The agent set: the measured preload of an orchestrator's procedure | one sentence |
  | New | *No case runs the scribe*, the limit that closes `1792368013`'s row |

- **S14.** The two renamed headings are the titles of the record layout and
  the agent set. `git grep -F` outside `seal/` and `changelog/` finds no
  citation of either; `docs/README.md`'s row for the record layout uses the
  same words to say what the document answers, which is no citation. Every
  section heading of the four documents stands, so every `§*…*` citation of
  them in `skills/`, `agents/`, hooks and tests still resolves, as
  `citations.py` over the tree reported (one false hit in a split string
  aside).
- **The backlog of this group: 30 specs**, 25 by count and five by title
  (`1791384154`, `1791384155`, `1791384160` and `1790993138` from ties, and
  `1791382684` naming no test file a rule names). The four by count that
  `spec.md` *Scope* 8 removes, `1790260563`, `1790263216`, `1792126889` and
  `1792368014`, are phase 9's, which removes them, and gained no block here.
  Each of the 30 gained a no-change block naming what was written and where,
  what was overturned and by which commit, or what is internal to a test.
  Their rows: 78 closed, 19 open in 10 directories.
- **The closers used.** The item's own merged pull request for a suite row,
  each read with `gh pr view` as green on lint and all three pytest legs
  (#593, #608, #631, #648, #672, #675, #700, #736, #767, #786, #802, #828,
  #878, #879, #880, #882, #890, #895, #901, #917, #918 and #919), and #965 for
  a row about its own legs and the hygiene job. #959 merged with red pytest
  and release jobs, and #961, the 0.22.0 release, had its pytest legs
  cancelled, so `1791933022`'s suite row cites #997, the green release that
  carries the work. #997's legs and its `release-report` job closed the
  platform rows and the release table. 8350c578 closed rows whose subject it
  removed (`docs/review-chain-spec.md`, `round_record.py`, the generator's
  `notes` and `close`), and 5b1f6fae those of the ledger (its readers, the
  survivor sweep, `frozen_changes`, `ledger_kind` and the case past the
  ceiling). Three limit sentences closed rows: the in-flight record and the
  local-mode stamp already in the review record, and the new scribe limit.
- **Q4 for this group: 19 rows no closer closes, keeping 10 directories.**
  `1790381329`'s `cmd.exe` scan after an undefined name; `1790645290`'s
  no-break space after a closing fence, a divergence from CommonMark that
  the shared rule still holds; `1790815614`'s session-start hook in a real
  joined project, whose limit would belong to a skill or template, not
  `docs/`; `1791240747`'s reframe end to end, which its own round 3 mostly
  ran; `1791384158`'s Q-M2 comparison and the `seal` job's suite step on a
  tag, a run no pull request leg makes; `1791852610`'s routing question on
  screen, whose owning document is a skill; `1792368015`'s cost of a
  line-bounded search; and eight of `1791933022`'s, each a measurement of
  #957's or an owner's confirmation. Three rows have their owning document
  in phase 7's group and can close there with a limit sentence:
  `1791384161`'s two (the directory search inside Claude and the Console
  page, `docs/release-checklist.md`) and `1792367880`'s GitHub event
  behaviour (`docs/branch-and-release.md`).
- **The checks at the boundary (executed):** `bin/fold-check` exit 0, no
  group document past the ceiling; `bin/rules --check` exit 0, 240 lines; the
  S7 comparison at d8fb2ee8 names the same 24 paths before and after;
  `unverified_check.py` over the 30 directories, 19 open and 78 closed;
  `bin/settle --released-at HEAD` lists 20 of them as nothing to apply and
  holds 10 for their rows; the 37 modules naming a group document or its
  check targets, with the meta modules, 1896 passed; ruff clean over the two
  changed Python files. The rewritten stamp pin is absent from the old text.
  After the backlog and the records, the 46 modules that name any document
  phases 4 to 6 rewrote, with the meta and record modules, ran together: 2733
  passed, 2 skipped, exit 0.
