# 1792459424-docs-states-the-current-rule-in-one-read — phase 8

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | 71ca8949 |

## What this phase was asked

The runs, broad gate and pact group rewritten to the current rule, once:
`docs/measuring-a-run.md`, `docs/the-broad-gate.md` and `docs/the-pact.md`.
The group's backlog specs read, what they decided and `docs/` lacked written
in, their rows closed by the closers of `spec.md` *Data & interfaces*, and a
no-change block added. At the boundary the six checks of phase 4, every test
file naming a rewritten document, the meta modules, `bin/rules --check`,
`bin/fold-check`, `bin/unverified-check --baseline origin/main seal/specs/`,
`bin/settle --released-at HEAD` and ruff.

## What this phase found

- **The three documents went from 26,851 bytes to 24,910, and no pin
  moved.** They were already rules with grounds and check lines; what went
  was the dashed titles, the sentence calling each a policy document, the
  section signs, the issue numbers, and the incidents and one-run
  measurements the rules were written from. The 21 modules naming the three
  documents or their check targets passed unchanged, 1368 passed and 2
  skipped. The S7 comparison at d1f0dd94 names the same 18 paths before and
  after. No heading below a title was renamed, and no citation names a title,
  so S14 has nothing to follow; `citations.py` reports no stale citation.
- **The census.** Each change, and where the rule lives now.

  | Old text | New home |
  |---|---|
  | The three titles' dashed subtitles | the opening paragraph of each, which already said the same |
  | "It is a policy document, with the standing `docs/README.md` gives one" (three times) | gone; the index says what a `docs/` document is |
  | Run: a span of zero ending the report after "four divisions" | the rule as a condition: the meter survives both readings |
  | Run: "Three defects in one meter put a wrong row into every reading" | the rule: correcting a meter does not correct its readings |
  | Run: "both used to be the same silence"; "the procedure a session used to reconstruct from prose", "a day of measurements nobody took" | the rules as they stand, one clause each |
  | Run: "No case reads yet" | "No case reads", a standing limit |
  | Gate: "A run inside an agent was a second run" | the same grounds as a condition |
  | Gate: section signs on *The guarantee* and *The stamp*; (#666) twice | the italic headings; the issue gone |
  | Gate: four steps and two skipped by count | "some steps", which the case holds by name |
  | Gate: seven arms against five, the 0.13.0 copy, #475; "older than #666"; "said the same thing and was read by nobody" | the rule and its grounds as conditions; "an installed copy that names none" |
  | Gate: 55 to 58 seconds on seventeen calls | gone as a measurement; the rule stands |
  | Gate: (#337), the 0.15.0 run's six sealer runs | gone; the three meanings of one command stand as the grounds |
  | Gate: "Three were not" and the three checks | one sentence of the repair's shape |
  | Pact: the owner's names given in #647 on 2026-10-03 and #822 on 2026-10-06 | "The three names are the owner's" |
  | Pact: (#647, decision 5) and (#647, decision 2) | gone; the rules stand |
  | Pact: the section sign on the orchestration citation | the italic heading |

- **The backlog of this group: 35 specs**, 24 by count and 11 by title from
  ties: `1790635412`, `1790297086`, `1790823441`, `1791076830`, `1791180640`,
  `1791076832`, `1792311781`, `1791270165`, `1790815610`, `1790815612` and
  `1791163980`, whose titles name the broad gate, a run's measurement or
  neither group, which phases 4 to 7 left to the later phase. Each gained a
  no-change block.

  | Work item | What it decided, and where it is | Rows |
  |---|---|---|
  | `1790550714` | internal: the family after `cd`, `tests/test_session_cost.py` | 2 closed |
  | `1790562540` | written: a segment's own transcript; internal: the slice | 1 closed |
  | `1790562541` | internal: the read family | 1 closed, 2 open |
  | `1790690762` | written: arms enumerated and mutated; internal: the node tables | 2 closed, 1 open |
  | `1790815611` | internal: the preflight's record arms; overturned: the ledger arm, `round_record.py` | 4 closed |
  | `1790815615` | written: what the run prints and counts; overturned: the values file, at f1c9932d | 2 closed |
  | `1790835050` | internal: the delegated note | 2 closed |
  | `1790835051` | internal: the preflight's asked lines; overturned: `round_record.py seal` | 3 closed |
  | `1790913304` | overturned: the letter and its sheet, at 149ca9ec | 3 closed |
  | `1790993137` | written: the pact, its signers, the anchor and `pact-check` | 1 closed |
  | `1791076833` | overturned: the reverify writer, at 5b1f6fae | 3 closed |
  | `1791090130` | overturned: `evidence-check`'s families and `--into`, at 5b1f6fae | 1 closed |
  | `1791119069` | internal: a row's failing file measured under its directory | 2 closed, 1 open |
  | `1791128260` | written: one reader of the `Pact` row | 2 closed |
  | `1791239490` | written: the pact's repository is a signer; the old header reads | 1 closed |
  | `1791240748` | overturned: `--reverify`, at 5b1f6fae | 3 closed |
  | `1791270161` | internal: the gate reads its plugin's record | 3 closed, 3 open |
  | `1791270163` | internal: the pact-policy sweep; written: the old header quoted | 2 closed |
  | `1791270164` | written: the release seal from the SVG, and the 28-cell stamp | 6 closed |
  | `1791384162` | internal: the macOS shards | 2 closed |
  | `1791852613` | internal: the durations file and its refresh | 2 closed |
  | `1791876666` | internal: the suite's budgets | 1 open |
  | `1792251842` | written outside `docs/`: `agents/smith.md`; the split, in `docs/the-agent-set.md` | 1 closed, 1 open |
  | `1792252400` | written: the orchestrator runs the gate, the sealer reads its record | 1 closed, 1 open |
  | `1790635412` | overturned: `evidence-check`'s cell count, at 5b1f6fae | 4 closed |
  | `1790297086` | written: every CI step mirrored or excluded; internal: the `cmd.exe` handoff | 2 closed |
  | `1790823441` | internal: `arm-check` runs the original first | 2 closed |
  | `1791076830` | internal: every file names its encoding | 2 closed, 1 open |
  | `1791180640` | internal: the base run collects only its files | 2 closed, 1 open |
  | `1791076832` | internal: the base re-run takes the test part of the row | 2 closed, 1 open |
  | `1792311781` | written: the gate draws nothing, the stamp follows the sealer's verdict | 3 closed |
  | `1791270165` | internal: the Windows leg's shards and cuts | 1 closed, 3 open |
  | `1790815610` | internal: `mutation-check`'s bytecode and bound; written outside `docs/`: `agents/smith.md` | 2 closed, 2 open |
  | `1790815612` | written: the per-segment bars, and the framer's opening in `agents/framer.md` | 1 closed, 2 open |
  | `1791163980` | overturned: `--reverify`, at 5b1f6fae | 1 closed |

  The closers used: the item's own merged pull request for a suite row and
  its platform legs (#607, #635, #649, #651, #659, #685, #696, #697, #698,
  #699, #707, #711, #714, #735, #756, #757, #758, #771, #787, #793, #801,
  #814, #827, #829, #843, #845, #846, #859, #876, #924, #974 and #977, each
  read with `gh pr view` as green on lint and all three pytest legs, and #685
  and #707 on both `arm-check-grammar` legs); #997 for `1792252400`'s CI row,
  because #973's Windows leg carries a red run beside its green one;
  5b1f6fae, 8350c578, 4b363e68, f1c9932d and 149ca9ec for subjects they
  removed; run 39332461097, the `seal` job at `v0.22.2`, for the install and
  the drawing; and the limit sentences of `docs/the-review-record.md` *The
  stamp* (a screen, a background, a person's session) and
  `docs/branch-and-release.md` *Cutting a release* (a browser).
  `1790550714`'s re-derivation of published readings closed on the rule in
  `docs/measuring-a-run.md` that a correction names the readings it affects
  and re-deriving them is its own work, because the transcripts sit on the
  owner's machine. `#924`'s and `#876`'s jobs carry their budgets in their
  names, which is the closest reading of "GitHub reads the timeout" a green
  run gives.
- **Q4 for this group: twenty rows no closer closes, keeping thirteen
  directories.** A Linux bash and bash 5.3 nobody ran (`1790562541`); the
  whole suite on 3.14, which no CI leg runs (`1790690762`); this
  repository's lint-first row through a real failing gate, which no run has
  met (`1791119069`, `1791076832`); pytest below 6.1 or 8.1, a third-party
  plugin and an unreachable branch, each "nobody" in its own row
  (`1791270161`, `1791180640`); the phase-1 file's Windows seconds
  (`1791876666`); `CLAUDE.md`'s *a seal block*, the owner's
  (`1792251842`); a paid side for `rule-sealer-stale-gate`, which Q1 does
  not buy (`1792252400`); a non-ASCII notice under an ASCII console
  (`1791076830`); the twins case's lookup, 4b's Windows gain and the sealer's
  10 to 15 seconds (`1791270165`); `proc.kill()` on Windows and the
  harness's own bound (`1790815610`); and two flow-log readings, a warden row
  and a framer's tools per turn (`1790815612`). `bin/settle --released-at
  HEAD` lists the other 22 as nothing to apply and as removed by `--apply`.
- **The checks at the boundary (executed):** `bin/fold-check` exit 0, no
  group document past the ceiling; `bin/rules --check` exit 0, 240 lines; the
  S7 comparison; `unverified_check.py` over the 35 directories, 20 open, 100
  closed, none unreadable once one row written with three cells was
  repaired; `bin/unverified-check --baseline origin/main seal/specs/` exit 0;
  the 21 group modules, 1368 passed and 2 skipped; the meta and record
  modules, 455 passed. No Python file changed.
