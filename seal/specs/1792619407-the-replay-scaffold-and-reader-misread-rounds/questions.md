# Questions for the planner: the seeded scaffold hides the shipped rounds, and the harness reader miscounts findings (#986)

## Decided from the tree, so nobody reopens them

- **Which cases defect 1 is in.** The seeded cases, not the replay cases.
  No replay scaffold runs `git rm`, and all 8 artefact rows #971 classed are
  seeded cases (`spec.md` *What the issue's facts stand on, opened*).
- **How the seeded case is fixed.** It is built at round 1's target, not on
  the squash commit with its rounds kept. Keeping the rounds makes the case
  owe round N a reference and leaves the unmutated build one diff away
  (`plan.md` *Alternatives considered*, S2 and S3). The chosen design leaves
  a narrower leak through `HEAD^`, which is Q5.
- **Whether the reflog leak is in scope.** Yes. It is in the scaffold this
  work rewrites, and a later fix would cost a second new suite and a second
  baseline.
- **What a finding is, for the harness.** A `### <n>.` section of the one
  `## Findings` section, split by `chain_check.py#finding_spans` over the
  shared reader's lines (`docs/the-review-record.md` *The round record*). A
  section the check refuses is still one false row (`plan.md` R2 and R3).
- **The "verdict table" of the issue.** The shape before #1000. No table of
  today's record holds a finding, and a record writing findings anywhere
  but a section fails the `shape-findings` grader.
- **Where recall is read.** From the same rows as the false count, for a
  `truth-` grader whose target is a round record
  (`noninferiority.py#reads_record`); a `truth-` grader over another file,
  as the sealer suite's over `guarantee.md`, keeps the eval's result
  (`plan.md` T2).
- **What happens to the committed sides.** They are refused by `compare` and
  `regrade`, not converted: they keep no text a reader can read again.
- **The stated point.** The squash commit that lands this work on
  `release/v0.22.3`, written in the changelog fragment, on the precedent of
  #971's own suite change.
- **The case names.** Kept as the squash commit's first 8 hex (`plan.md`
  S5).
- **The six recurred truths of two seeded cases.** They go; their
  coordinates were read at squash commits (`spec.md` *Removes*).
- **`## Rule changes`.** Nothing: no file of `docs/` states the harness
  reader or the seeded scaffold.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Is a paid warden side run under the new suite and reader in this work? The issue's *Done when* asks for a paid baseline taken under them. The tree cannot weigh the spend, and the owner's precedent (#941 Q1, #940 Q1) is no paid run unless it is the only way to read the fact a change needs. The facts this change needs, that a fenced line is no row and that the seeded clone cites nothing it lacks and keeps no copy of the target's original commit, are read by free cases and free scaffold runs (`spec.md` S1 to S12). Price, read from the committed records: a warden side is about 40 USD and about 2 hours of run time pooled over its 18 runs (#971's record: 36.04 and 36.67 USD, 5780 and 6808 seconds; #985's record: 41.74 and 39.79 USD, 7587 and 6960 seconds) | a person | (a) **One side now**: the orchestrator runs `noninferiority.py run --agent warden --rev <this work's head>` after phase 2, about 40 USD. It gives the first figures under the new suite and reader, and serves as a later change's baseline only where that change's merge base carries the same warden preload. (b) **Not run**: the next work item that compares a warden side runs its baseline at its own merge base, as `evals/README.md`'s commands already do, and that side is the first paid baseline under the new suite. Nothing in this work waits on a side | (b). The build proceeds without the run. A run not made can still be ordered at the pull request and made before the merge; a run made cannot be taken back. The pull request body names this departure from the issue's *Done when* | open |
| Q2 | Does every regenerated seeded scaffold fetch its round 1 target and base from the repository's GitHub remote, and run to exit 0? **Why the tree cannot answer:** whether GitHub serves a commit reachable only from a pull request's head ref is a fact of the remote, read only by fetching it | a measurement | The smith runs each regenerated `scaffold.sh` once in an empty scratch directory (spec S10). Exit 0 with every check of S10 holding: recorded. A fetch that fails: Q3 applies to that case | The smith runs it in phase 2 and records each case's line in `phases/phase-2.md`. The build does not wait on it | answered 2026-10-22 by the work, phase 2 (`phases/phase-2.md`, S10, executed): each of the four regenerated scaffolds, `sh scaffold.sh` in an empty scratch directory fetching from the GitHub remote, exited 0, and every check of S10 held |
| Q3 | Which shipped commit replaces a committed seeded case that cannot be built at round 1's target? **Why the tree cannot answer:** a case fails only when the generator meets it: no readable round 1 record, no seedable line in `base..target`, a seed window that would accept a truth's line, or a fetch that fails (Q2) | the work | Replace it with the next smallest shipped commit `seed_defects.py --list` names that builds, and remove the old case directory; or keep three cases. Both keep the suite generated | Replaced by the next smallest that builds, named with its reason in `phases/phase-2.md` and in a divergence row of `overview.md` | answered 2026-10-22 by the work, phase 2 (`phases/phase-2.md`, `overview.md`), applied twice: `seeded-8a100e13` replaces `seeded-4d316179`, which takes no seed at its round 1 target `44c67f9f`; `seeded-f1c9932d` replaces `seeded-9b644676`, two of whose round 1 truths accept one `location:` line. The generator now leaves out such a commit (`seed_defects.py#shared_line`) |
| Q4 | How is a kept record masked where `tests/test_no_real_identifiers.py` would refuse a committed side? **Why the tree cannot answer:** whether any printed record holds a user path or a real host is known only from a run's output, and how the scan's pattern reaches `annotate` without a second copy of it is a choice the code meets | the work | `annotate` replaces what the scan's own patterns match, a user path by `/Users/x/` and a host by `example.com`, loading the patterns from their one home; a `location:` path never starts with `/` (`docs/the-review-record.md` *The round record*, the `location:` row), so no finding row changes. Or no masking, and a side holding one is not committable until the orchestrator edits it | Masked, with the pattern taken from its one home and never copied; the phase 1 record says how it is loaded, and a case shows a masked text gives the same rows | answered 2026-10-22 by the work, phase 1 (`phases/phase-1.md`, `overview.md`): masked. `noninferiority.py#identifier_scan` loads `tests/test_no_real_identifiers.py` without its `conftest` import; the scan's allow logic moved into `refused_domains` and `refused_user_paths` there, which both its walks and `noninferiority.py#masked` call, so no pattern is copied. A side writes the record as one JSON string, so the mask also reads that form: `noninferiority.py#apart` scans the text's JSON form with the scan's own `refused_domains` and `refused_user_paths`, and sets one space beside each escape a refused match takes in, after the character where the match starts inside the escape and before it where the match runs into it (round 1 finding 3, fixed at 0cc8be41). `test_a_kept_record_is_masked_where_the_identifier_scan_refuses_it` scans the written side |
| Q5 | Does the seeded clone's narrower leak stand? The amend rewrites only the target commit, so the commits before it still hold the seeded line unmutated, and `git diff --stat HEAD^ HEAD` shows the seeded file changed by one line inside a commit that otherwise touches records, in all four clones (executed by the smith, `phases/phase-2.md`). `plan.md`'s first summary said nothing in the clone held the build without the seed, which was false. **Why the tree cannot answer:** keeping every cited commit resolvable and leaving no unmutated copy of the seeded line conflict wherever the line existed before the target commit, and choosing between the leak, the old scaffold's dangling citations and another design is a value only the owner can set; whether a warden uses `HEAD^` is read only by Q1's paid run | a person | (a) **Accept the narrower leak.** The old scaffold's alternative was citations to records and commits the clone did not hold, which #971 classed as 8 false rows; the leak needs a warden to diff `HEAD^`, and only Q1's paid run could measure whether one does. (b) **Seed only a line the target commit itself added.** No commit before the target then holds the line, so `HEAD^` shows nothing; none of the four targets' last commits adds a Python line, so all four cases change again and the generator selects only targets whose last commit adds code in a Python unit | (a). The build proceeds; the owner can overturn it at the pull request | open |

**`Who can answer` takes one of three values and nothing else.**

- **a person**: what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement**: a probe, a command or a count settles it, so a person is
  the wrong instrument, and queueing the row behind one wastes a round trip.
- **the work**: unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing, and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way also keeps the batch short
enough to answer in one sitting: two of the three kinds never need a person.

The orchestrator carries each answered row into `spec.md`'s `## Rule
changes` (a policy clause or an open-questions section) when it drains the
work item's rows, at the moment `skills/implement/SKILL.md` *6. Drain the
rows before the broad run, and keep the records* names.
