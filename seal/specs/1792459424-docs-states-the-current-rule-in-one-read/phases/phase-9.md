# 1792459424-docs-states-the-current-rule-in-one-read — phase 9

| Field | Value |
|---|---|
| Phase | 9 |
| Commit | 63e088b3 |

## What this phase was asked

`docs/one-root-by-lifetime.md` and its `.ko.md` edition rewritten to what
still rules, both editions alike, split along their own `##` headings only if
the Korean edition is still past 25000 estimated tokens after the rewrite.
Every backlog spec no group took read and given a no-change block, including
`1790260563`, `1790263216`, `1792126889` and `1792368014`, which phase 6 left
for this phase. The 8 removable directories removed, with each check that
reads `seal/specs` answered. `docs/README.md`'s rows made final. S16's
`wc -c` of the preloads, `agents/*.md` plus each agent's `skills:`, at
ac83bdf3 against this phase's commit (the owner's Q1: no paid evaluation).
`tests/test_release_hygiene.py#VERSIONS_OF_ANOTHER_PRODUCT`'s git 2.54.0 entry
for `docs/worktree-guard-spec.md`, which the document stopped naming at
3d78c220, removed. At the boundary the six checks of phase 4, S13's two
`--baseline` runs, S15, S11 over the backlog, the meta modules,
`bin/rules --check`, `bin/fold-check`, `bin/unverified-check --baseline
origin/main seal/specs/`, `bin/settle --released-at HEAD` and ruff.

## What this phase found

- **The one-root document went from 45,284 bytes to 13,668, and its Korean
  edition from 55,649 to 16,754, so neither splits.** The Korean edition is
  about 8,400 estimated tokens by halved bytes and about 7,800 at 2.15 bytes
  a token, so Q5's question no longer moves the answer either way. Both
  editions carry the same outline, eight headings at levels 1, 2, 2, 2, 2,
  3, 2, 2. The S7 comparison at 99e1577b names the same 8 paths before and
  after, on 9 check lines.
- **What still rules, and where it lives.** The document kept six rules of its
  own: the root and its three lifetimes, the dependency rule, the opt-in, the
  first-setup question with shared or local, naming, and the config rows. The
  layout table, the reference root and the root's path a session types were
  stated elsewhere and are cited instead.
- **The census.** Each removed or moved text, and where the rule lives now.

  | Old text | New home |
  |---|---|
  | The opening: the design 0.4.0 started from, issue #74's thread, the numbers re-measured at `5685029` | gone as history; the opening says what the document answers |
  | *The change in four lines*, its before-and-after diagram | *The root and its lifetimes*, one rule; the before-and-after gone with the move it described |
  | *The problem, as measured*, and *Where the line between the SDD set and the process record runs* | gone as measurements; what each file answers is `docs/the-record-layout.md` *seal/specs/<work-item-id>/* |
  | *The proposed tree* and the lifetime table | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* and `docs/the-record-layout.md`, cited; one sentence of lifetimes kept |
  | *What happens at a release* and the guard | `skills/settle/SKILL.md`, which owns the procedure; the guard is the settled predicate in `docs/the-record-layout.md` *The fold, and what tells it from a deletion* |
  | *The dependency rule*: its three groups, the two readers that had to change | the rule and its wider rule kept; the readers answered at a settle, `skills/settle/SKILL.md` *Answer every check that reads the corpus* |
  | *What keeps settle light* | `skills/settle/SKILL.md`, which now states "moves and does not verify" itself instead of quoting this section |
  | *What spec means after this* | gone: the judgment order and the place of `docs/` are `skills/implement/SKILL.md`'s |
  | *The opt-in signal*'s before-and-after table and the thread's key candidates | one table of the two modes; the candidates one clause |
  | *What first setup asks* and the row *The first-setup question's shape* | *What first setup asks*, with the installed workflow, the old layout told and not asked, and the migration hook's stamp |
  | *Shared or local*: the owner's summary, "the owner hit exactly this" | the same section, as conditions |
  | *Retention: measured, and answered by settle* | gone as a measurement; settle's procedure owns removal |
  | *Naming*: the three-name table with *Why not*, and the cost of a rename | *Naming*, the chosen names and one sentence each; a rename's cost is `docs/branch-and-release.md`'s fixed-name rule |
  | *What happens to the existing directories at the switch*, *What it touches in this repository*, *What does not change*, *Order* | gone as history of the 0.4.0 move; the hook's one-time move is in *What first setup asks* |
  | *Out of scope* | gone with the release it scoped |
  | *Decided after the thread*: the scratch opt-out, the migration stamp, how a session finds the root | the scratch file in *The opt-in signal*, the stamp in *What first setup asks*, the root's path in the agent contract's root section, cited |
  | *Decisions left open*: the three names | answered; *Naming* |
  | The four dated sections of 2026-09-22, 2026-09-23, 2026-10-01 and 2026-10-04 | `skills/settle/SKILL.md` for what settle is and that a settle is no work item; `docs/the-record-layout.md` for the settled predicate and when a directory leaves; `templates/config.md` *Reference specs* for a project's own `specs/`; `skills/implement/orchestration.md` for the old layout the bootstrap tells |

- **Pins that held the dated sections retire with them, and two pins follow
  the rules where they now stand.** `tests/test_settle_reads_before_it_removes.py`
  lost `test_the_design_record_takes_the_later_decision_as_a_dated_section`,
  `test_the_design_record_takes_d1_as_a_dated_section`,
  `test_both_editions_took_the_same_decisions` and their constant and helper;
  the editions' outline arm holds the pairing instead.
  `tests/test_unverified_rows_close.py` lost the two one-root rows of
  `test_the_documents_state_the_merge_base_footing`, because the document no
  longer describes `--baseline`. In `tests/test_first_setup_asks_once.py`
  two cases reading *Decided after the thread* became
  `test_the_design_record_states_the_setup_rules_where_they_rule`, and the
  settle skill's floor case pins its rewritten sentence. Each new pin is
  absent from the old text, and three were mutated with `mutation-check` and
  went red: the English stamp sentence, the Korean scratch file, and the
  skill's sentence.
- **Two exemptions had nothing left to exempt, and a third had not since
  3d78c220.** The one-root editions were exempt from the old-root sweep
  (`tests/test_no_document_names_the_old_roots.py#DESIGN_RECORD`) and from the
  version-timer sweep (`tests/test_release_hygiene.py#RECORDS_OF_A_MOMENT`) as
  records of a moment; rewritten, they name no old root and no version, so
  both entries went and the sweeps read them like any document. Git 2.54.0's
  entry for `docs/worktree-guard-spec.md` went the same way, and the
  `broad_gate.py` entry that called it "the row above" now stands alone. No
  case was added for these: the sweeps pass over the files with the entries
  gone, which is the check that they were not needed. Each is a removal
  `## Removes` did not name, recorded in the overview.
- **S14, the renamed headings.** The title, and *The opt-in signal is the
  root itself, wherever the mode put it*, now *The opt-in signal is the root
  itself*, in both editions. `git grep -F` outside `seal/` and `changelog/`
  finds no citation of either long form; the citations that name the short
  form (`hooks/optin.py`, `hooks/config.py`, `skills/implement/scripts/seal.py`)
  still resolve. Three citations named sections the rewrite removed and were
  rewritten: `skills/settle/SKILL.md` twice (*What keeps settle light*,
  *The dependency rule*'s two readers) and `hooks/root-migrate.py`'s docstring
  (*What happens to the existing directories at the switch*, now *What first
  setup asks*). `docs/README.md`'s row says what the document answers now, and
  its section sign went.
- **The backlog no group took: 18 specs**, 16 naming no test file a rule
  names, `1791852616` by count, and `1790659274` from a four-way tie whose
  title names none of the groups. Each gained a no-change block.

  | Work item | What it decided, and where it is | Rows |
  |---|---|---|
  | `1790260564` | overturned: the survivor sweep, at 5b1f6fae | 3 closed |
  | `1790260567` | internal: the `cmd.exe` path and the logged-out `gh` | 3 closed, 1 open |
  | `1790297084` | overturned: the survivor sweep, at 5b1f6fae | 2 closed |
  | `1790381328` | overturned: `MALFORMED`, at 5b1f6fae | 2 closed |
  | `1790562543` | written: the stamp, in `docs/the-review-record.md`; overturned: the gate's signal, at f1c9932d | 3 closed |
  | `1790666894` | internal: the oracle's dropped lines | 1 closed |
  | `1791019476` | overturned: `--reverify`, at 5b1f6fae | 2 closed |
  | `1791076835` | written: the directory's paths and when it leaves; overturned: `--retire-process`, at ac83bdf3 | 3 closed |
  | `1791119068` | internal: the encoding walker's openers | 1 closed |
  | `1791327652` | internal: an unended base session; written outside `docs/`: `new?` | 3 closed, 2 open |
  | `1791384153` | overturned: the ledger, at 5b1f6fae | 5 closed |
  | `1791384159` | overturned: `evidence-check` and the unit reader | 2 closed |
  | `1791876665` | overturned: the budget mechanism, at 8350c578 | 8 closed |
  | `1791876667` | internal: the Windows shards measure the durations | 1 closed |
  | `1792363189` | internal: rule 3 | 1 open |
  | `1792366315` | internal: the false-row classes | 1 open |
  | `1790659274` | internal: inline HTML leaves a piece uncertain | 2 closed |
  | `1791852616` | internal: one walker reads the config table | 2 closed, 1 open |

  Beside them: the four directories with no spec that stay, `1791090072`,
  `1791852617`, `1791867522` and `1792365855`, closed their five rows, so the
  dry run retires all four by the rule; and `1791876666`'s last row closed on
  the durations refresh. The closers used: the item's own merged pull request
  (#589, #595, #609, #621, #650, #676, #681, #743, #766, #768, #782, #851,
  #887, #889, #912, #925, #927, #937 and #938, each read with `gh pr view` as
  green on lint and all three pytest legs, and #938 on its `budgets` job);
  5b1f6fae, 8350c578, ac83bdf3 and f1c9932d for subjects they removed; the
  durations refresh #972 committed, which #937 made the Windows shards
  measure; and the stamp's limit sentence for a screen.
- **Q4 for this phase: six rows no closer closes, keeping five
  directories.** A `gh` login in an OS keyring, on a machine nobody here has
  (`1790260567`); a replacement xdist worker and a recorder stopped by a full
  disk, neither provoked (`1791327652`); the owner's question on the
  `model` aggregation (`1792363189`); the 74 findings' wording, held only by
  an issue comment (`1792366315`); and a refusal naming the wrong cause in a
  reader outside the item (`1791852616`). Across the nine phases, 33 backlog
  directories stay for an open row; the dry run's refused list is those 33
  with #953's and this item's own.
- **The eight directories left.** `git rm -r` removed `1788177600`,
  `1788395377`, `1790134781`, `1791019421`, `1790260563`, `1790263216`,
  `1792126889` and `1792368014`. Their specs decided nothing `docs/` lacks:
  the fold checks and the enforcement lines became this item's `check:`
  grammar, and the agents' and the framer's rewrites live in `agents/` and
  `docs/the-agent-set.md`. Every check that reads `seal/specs` was answered
  by running it: the 51 modules the dry run lists passed over the smaller
  corpus, 3085 passed, so none needed retiring, re-pointing or declining. A
  path still citing a removed id is a record or a docstring naming it, a
  pointer git history resolves.
- **S13 (executed).** `unverified_check.py --baseline origin/release/v0.22.3
  seal/specs/` and `--baseline origin/main` both exit 0 and name seven
  removed overviews as settled. The eighth, `1791019421`, held no
  `overview.md`, so there is no record for either run to name; the overview
  records the difference. `chain_check.py --baseline origin/main` exits 0.
- **S11 (executed).** `bin/settle --released-at HEAD`: 115 released specs,
  none listed as having no `## Rule changes`; 80 with nothing to apply and
  removed by `--apply`; 35 held for an open row, 33 of them backlog; the four
  directories with no spec retired by the rule, none kept.
- **S16 (executed), the preload is smaller.** `wc -c` of each agent's
  definition plus the skills its `skills:` list injects, read from git:

  | Agent | At ac83bdf3 | At this phase |
  |---|---|---|
  | framer | 27,248 | 25,255 |
  | scribe | 19,922 | 18,545 |
  | sealer | 24,505 | 23,122 |
  | smith | 26,879 | 24,746 |
  | warden | 27,168 | 25,109 |
  | total | 125,722 | 116,777 |

  Every agent preloads `agent-contract` alone, which went from 16,603 bytes
  to 15,537.
- **The checks at the boundary (executed):** `bin/fold-check` exit 0, 17
  documents and none past the ceiling, the index naming every document;
  `bin/rules --check` exit 0, 240 lines; S15 through
  `tests/test_both_editions_carry_the_same_folds.py`; the 16 modules naming the
  one-root editions or their targets, 1055 passed; the modules reading the
  settle skill, the migration hook and the index, 658 passed; the 51 corpus
  modules, 3085 passed; `bin/unverified-check --baseline origin/main
  seal/specs/` exit 0; ruff clean over the six changed Python files.
