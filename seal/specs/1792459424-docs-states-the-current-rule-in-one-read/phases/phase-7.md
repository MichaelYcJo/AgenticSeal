# 1792459424-docs-states-the-current-rule-in-one-read — phase 7

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | d8ad9cbd |

## What this phase was asked

The release and tracker group rewritten to the current rule, once:
`docs/branch-and-release.md`, `docs/release-checklist.md` and
`docs/issues-and-milestones.md`. The group's backlog specs read, what they
decided and `docs/` lacked written in, their rows closed by the closers of
`spec.md` *Data & interfaces*, and a no-change block added. Three open rows
phase 6 named close here with a limit sentence: `1791384161`'s directory
search and Console page in `docs/release-checklist.md`, and `1792367880`'s
GitHub event behaviour in `docs/branch-and-release.md`. At the boundary the
six checks of phase 4, every test file naming a rewritten document, the meta
modules, `bin/rules --check`, `bin/fold-check`, `bin/unverified-check
--baseline origin/main seal/specs/`, `bin/settle --released-at HEAD` and ruff.

## What this phase found

- **The three documents went from 65,311 bytes to 55,699.** They were
  already written as rules with grounds; what they held beside them was the
  incidents each rule was written from, dated measurements, issue numbers and
  section signs. Every check line kept its targets: the S7 comparison at
  9782dd03 names the same 16 paths before and after.
- **Two headings renamed, no citation moved.** *2b. Settle what earlier
  releases left behind* and *3. Verify before committing* lost their dashed
  tails. The numbers stay, because `skills/`, `.github/scripts/` and tests cite
  the checklist by step number (`§5`, `§6`, `§*2b*`), which Q2 leaves to #940.
  `git grep -F` for both old texts outside `seal/` and `changelog/` finds only
  a test id in `.test_durations`; `citations.py` over the three documents
  reports no stale citation.
- **The em dash in the release title stays.** `publish_release_note.py#title_line_re`
  matches `release: X.Y.Z — <symptoms>` with the dash, so the dash is a value
  the workflow reads, and the sentence says so.
- **Pins that held history.** Eight pins followed a rewritten sentence: the
  hotfix grounds (`tests/test_the_rules_claude_md_names_have_one_home.py`),
  the review record citation without its sign
  (`tests/test_the_rules_have_one_owner.py`), the settle citation
  (`tests/test_settle_reads_before_it_removes.py`), the accumulation section
  (`tests/test_the_changelog_is_gathered_at_release.py`), the release
  descriptions (`tests/test_a_release_is_sized_by_a_criterion.py`), the third
  reader, the checklist step and the two bold leads bounding the squash rule
  (`tests/test_the_release_tail_does_not_end_at_the_tag.py`), and the seal
  bullet without its issue numbers (`tests/test_the_release_seal_is_drawn.py`).
  One assertion retired with the history it pinned: the three pull request
  numbers the closing-keyword rule was written from
  (`tests/test_release_hygiene.py`). Each new pin is absent from the old
  text, and four were mutated with `mutation-check` and went red.
- **The census.** Each change, and where the rule lives now.

  | Old text | New home |
  |---|---|
  | Branching: "Split out of `CONTRIBUTING.md` because" | the opening, as a reason the document stands alone |
  | Branching: the release that shipped untagged | gone as history; the rule and its grounds stand in *Cutting a release* |
  | Branching: three acts once assigned to a person, the note missed three releases running | gone as history; "a step a person can skip is a step that gets skipped" stands |
  | Branching: (#572), (#718), (#832) in the note bullet | gone; the rules stand |
  | Branching: "states the design and not the tracker's state" | one sentence, `gh label list` |
  | New | the browser limit in the note bullet, which closes `1790993139`'s release page row |
  | New | the limit on which run GitHub starts or cancels, which closes `1792367880`'s row |
  | Branching: "A hotfix was squashed in once" | the same grounds as a condition |
  | Branching: "measured", and the squash whose round records survived | gone as history |
  | Branching: the 2026-09-22 count of 310 entries, its work item and marker | one clause: an entry with a `ref` usually names `main` or `master` |
  | Branching: "This is enforced, and it was not always"; the preparation commit that "used to be" pushed | *Two rulesets enforce the merge methods*; the preparation commit's branch and squash as the current rule |
  | Branching: the release branch two commits behind | gone as history |
  | Branching: three branches on 2026-09-01; which file a change writes | `docs/the-record-layout.md` *A change writes fragments, never a shared file*, by citation |
  | Branching: (#728), (#586), (#584); the two refusals in two paragraphs | one paragraph: the gather refuses either fragment, naming it |
  | Branching: "There is no accumulation section any more" | `CHANGELOG.md` holds no section entries accumulate under |
  | Branching: #37, #38 and #39 | gone as history; the hygiene test's docstring keeps the incident |
  | Branching: "Three releases show what remembering is worth" | gone |
  | Branching: the run that died on its first refusal, before #536 | gone as history; the rule *One issue the tracker refuses does not leave the rest open* stands |
  | Checklist: the paragraph on the old footing and its quadratic cost (#272, #351) | gone as history; the never-rebase rule stands |
  | Checklist: `docs/flow.md` and (#351) in the milestone box | gone |
  | Checklist: the IDE pull "once" | the same rule as a condition |
  | Checklist: "Every line here was bought by a release that re-learned it" | gone |
  | Checklist: (#728), (#289) | gone; the rules stand |
  | Checklist: "the class #517 settled for the fold" | gone |
  | Checklist: (#179), (#363) and the three releases in the table row | the row says what the check finds and what is history to it |
  | Checklist: "This section used to stop here, and that is what #386 measured"; "until 2026-09-16" | one sentence: two acts come after the tag |
  | Checklist: (#718), (#832), (#536); "This paragraph said the opposite of both halves until #359" | gone; the box rules stand |
  | New | the limit on the directory search and the Console page, which closes `1791384161`'s two rows |
  | Tracker: "Every other mechanism … The tracker had none" | one sentence naming the three owners |
  | Tracker: 0.8.3 shipped three of eight | gone as history |
  | Tracker: *The two releases above are named rather than numbered on purpose* paragraph | one sentence: both are named so the description reads the same on every release |
  | Tracker: "It used to be two" and (#351); "It named a real unshipped release here for three of them (#179)" | gone |
  | Tracker: the 2026-09-22 share of `from-review` (89 issues, 48%) | gone as a measurement; the rule to quote the date stands |
  | Tracker: (#198), (#363), #155 and "written before that convention" | the rules as conditions; the older title form named by what it means |
  | Tracker: "A bare `now` was the name proposed" | one clause on why a bare `now` is not the name |
  | Tracker: "until #450 nothing acted on it" | gone as history |
  | Tracker: "This section said *nothing automated reads a milestone* until #359" | gone as history |
  | Tracker: PR #162 and the 0.8.0 release's one close | gone as history; the keyword rule stands |
  | Tracker: "The closer used to mask … (#266)" | gone as history; what is masked and why stands |
  | Tracker: "That is how the tickets here have actually been used" | gone |

- **The backlog of this group: 9 specs**, 7 by count, `1790993139` by title
  from a tie with phases 4 and 8, and `1790635414` from a tie with phase 6
  whose title names neither group, which phase 6 left to the later phase.
  Each gained a no-change block.

  | Work item | What it decided, and where it is | Rows |
  |---|---|---|
  | `1790260565` | overturned: the ledger and its cell count, at 5b1f6fae; `docs/round-record-spec.md`, at 8350c578 | 1 closed |
  | `1790297085` | written: the gather refuses a fragment's section line; internal: a loader's exit 2; overturned: `settle --retire`, at ac83bdf3 | 1 closed |
  | `1790297087` | overturned: `MALFORMED` left with `evidence-check` at 5b1f6fae | 1 closed |
  | `1790635413` | internal: one fence rule, `hooks/blocks.py`; written: the gather refuses an unclosed block | 2 closed |
  | `1790683267` | overturned: the rider check, at af9c924b | 2 closed |
  | `1791076834` | written: the release's own file and the index | 3 closed, 1 open |
  | `1791940762` | written: a rule names the test that holds it | 2 closed, 2 open |
  | `1790635414` | overturned: `evidence-check`'s follow-up reading and re-read dates, at 5b1f6fae | 3 closed |
  | `1790993139` | written: the seal job; overturned: the pixel drawing, by 149ca9ec | 3 closed |

  Beside them, `1791384161`'s two rows and `1792367880`'s one closed against
  the limit sentences above. The closers used: the item's own merged pull
  request for a suite row (#588, #605, #606, #663, #668, #683, #770 and #950,
  each read with `gh pr view` as green on lint and all three pytest legs);
  #997 for `1790993139`'s suite row, because #731's macOS leg carries a red
  run beside its green one; the same pull requests' legs for a platform row;
  5b1f6fae, af9c924b and 149ca9ec for subjects they removed; run 39332461097,
  the `seal` job at the `v0.22.2` tag, whose log reads "attached seal.png to
  v0.22.2 and put it in the note"; and the limit sentences.
- **One closer outside the list's letter.** `1791076834`'s row about the real
  gather and note at 0.18.1 closed on `changelog/0.18.1.md` in the tree and
  the `v0.18.1` release that `publish-release.yml` published from it, with
  `seal.png` attached. That is a CI run of the release's own workflow, not a
  pull request leg; the overview records it.
- **Q4 for this group: three rows no closer closes, keeping two
  directories.** `1791076834`'s update into 0.18.1 by 0.18.0's update skill,
  a person's run whose owning text is a skill; and `1791940762`'s
  `bin/rules.cmd` and `bin/pact-check.cmd` on Windows, which no case runs:
  `tests/test_pact_check.py` skips its wrapper case on Windows, and no case
  runs `bin/rules.cmd`. `bin/settle --released-at HEAD` lists the other nine
  as nothing to apply and as removed by `--apply`, and holds these two.
- **The checks at the boundary (executed):** `bin/fold-check` exit 0, no
  group document past the ceiling, `docs/one-root-by-lifetime.ko.md` still
  the one past it; `bin/rules --check` exit 0, 240 lines; the S7 comparison;
  `unverified_check.py` over the 11 directories, 3 open and 22 closed;
  `bin/unverified-check --baseline origin/main seal/specs/` exit 0; the 29
  modules naming a group document or its check targets, 945 passed and 9
  skipped; the meta and record modules, 633 passed; ruff clean over the eight
  changed test files.
