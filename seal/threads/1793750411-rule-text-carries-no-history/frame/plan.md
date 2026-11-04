# Implementation Plan: rule text carries no history (#1317)

## Technical context

The work edits prose only. It touches 48 Markdown files, 595,984 bytes at
3bd60d29f (`frame/design.md` *Grounding*), plus the tests that pin a removed
sentence and `.claude-plugin/plugin.json`'s version. The constraints:

- `tests/text/test_no_passage_is_pasted_into_a_second_file.py` already
  fails on any 15-word run two rule documents share. A citation that
  replaces a copy must not create one.
- `tests/behaviour/test_docs_line_wrap.py` reads the wrap of `docs/`.
  `tests/behaviour/test_both_editions_carry_the_same_folds.py` reads
  `docs/layout/one-root-by-lifetime.md` against its `.ko.md` edition.
- `tests/behaviour/test_the_set_a_work_item_always_has.py` pins lines of
  `skills/implement/orchestration.md` through `KNOWN_PROSE`, and pins
  `issue #35`. Other modules pin other sentences, and no list of them exists
  before a removal. Each phase finds a pin by running the tests of each
  file it touched, narrow, and by `git grep` on the removed words (contract
  rule 19).
- Four sentences are quoted by pending `from` lines and are not edited
  (`frame/design.md` *Scope* O4).

Failure scenario of the chosen approach, six months on: a later work item
writes a new history sentence into one of these files, because nothing
checks for one. That cost is accepted. The class is a kind of claim with no
fixed spelling, so a check would block on a reading guessed from words,
which `skills/core/SKILL.md` *The rule a mechanism is kept against*
forbids. Review reads new text against the same rule, and the census
method in `frame/design.md` *D4 The census* can be run again by anyone.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Read each in-scope file whole and judge each sentence by D2 and D3. Use the two probes of D4 as the census before and after, and commit neither | The reading is long, about 89,000 words over three phases. A crafter that skims a file misses a sentence, and only review finds it | **chosen.** Rule 12's second method makes the list whole for each file, and the probes make the change visible in the pull request without adding a mechanism |
| A2. Commit a check: a history-marker lint, or a ten-word passage test over the scope | The marker probe lists 58 sentences, and about 41 of them are no history: coordinates, examples, version boundaries a reader needs. A ten-word window matches kept applications, whose longest measured run is 10 words (`tests/text/test_a_moved_rule_leaves_its_definition.py`). Either check refuses correct text, and neither has caught anything yet | rejected. It adds a mechanism with no record of a catch, and it blocks on a noisy reading |
| A3. Replace the paste check's structure: lower `skills/settle/scripts/passages.py#WINDOW` from 15 to 10, so that the existing test becomes the census and the gate | The test fails on the 264 shared runs at once. Many of them are shared wording such as "the commit subject and body, the pull request title and body". `test_the_window_sits_between_what_was_measured` pins 15 between 10 and 25 | rejected. The premise that keeps the structure was checked: the longest kept application measured is 10 words, and a window at 10 sits on it, not between it and a copy (read in that module's docstring) |
| A4. Remove only the sentences the marker grep lists | A grep matches a spelling, and history has none. `seal/follow-up.md`'s row on figures stated with no moment records that each such enumeration shipped short. The paraphrase copies would also stay | rejected. The grep is a sample, and it is used only as context (D4) |
| A5. Split the item by directory into several pull requests | Each pull request needs its own census, and the milestone runs one work item per issue before #506 starts | rejected. One work item, three phases on one branch |
| A6. Remove the copies on the `skills/implement/orchestration.md` side of each pair with `skills/implement/acts.md` now | #506 may remove the table or its enumeration, and the citation would then name a section that is gone | rejected. Both sides of each `acts.md` pair wait for #506 (O2) |
| A7. Move each removed sentence into a history section or into the changelog | It keeps the bytes in a file that some party opens. Git, the release notes and the work items' records already hold each sentence | rejected. The phase records list what went, with its grounds, which is this work's record |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2, 3 and 5 for `skills/implement/orchestration.md`, `skills/code-review/orchestration.md` and `skills/verify/orchestration.md`; item 4's base reading of both D4 probes, which must equal `frame/design.md` *Grounding* | each `## Removes` row for these files against the diff; the narrow tests of each touched file and of each pin; `tests/text/test_no_passage_is_pasted_into_a_second_file.py`; the phase record's lists | 19f0ceafe |
| 2 | *Scope* items 1, 2, 3 and 5 for every other in-scope file under `skills/`, without `skills/implement/acts.md` (O2) | the same checks, for these files | 1392479e2 |
| 3 | *Scope* items 1, 2, 3 and 5 for the in-scope files under `docs/`, with `docs/layout/one-root-by-lifetime.ko.md` following its English edition; item 4's HEAD reading of both probes; `changelog.md`, ending with its `### Process changes` table; item 6's version move to `0.31.1`, in the commit that adds `changelog.md` | the same checks, for these files, and `tests/behaviour/test_both_editions_carry_the_same_folds.py` and `tests/behaviour/test_docs_line_wrap.py`; *User scenarios* A1, A5, A6 and A8 | 930ac879c |

`docs/releasing/branch-and-release.md` *Cutting a release* names the
orchestrator as the party that moves the version in the commit that adds
the first fragment. Phase 3 writes the fragment, so the orchestrator's
spawn of phase 3 hands the crafter that write, and the commit that adds
`changelog.md` carries it. The same spawn hands the crafter the
`### Process changes` rows, which it writes with the fragment
(`docs/layout/the-record-layout.md` *A change to the way of working writes
its process row in its own fragment*).

Phases 1 and 2 hand the next phase their lists through their phase records.
A copy whose home is in a later phase's files is removed on the copying
side in the phase that holds that side, and the record names the home.

## Operational impact

No migration, no new environment variable, no new dependency. The plugin's
version moves to 0.31.1. No rule changes meaning. A user's session reads
shorter text in the orchestration files and the skills.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-04 | The orchestrator's spawn of phase 3 handed the crafter the `### Process changes` rows with the version move, and the paragraph under *Phases* now says so | One party writes the fragment whole in one commit, the version and the process rows with it; the crafter that writes the fragment has read the diff the rows describe | `docs/layout/the-record-layout.md` *A change to the way of working writes its process row in its own fragment*; `docs/releasing/branch-and-release.md` *Cutting a release* |
