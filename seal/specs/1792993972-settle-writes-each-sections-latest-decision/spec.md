# Feature Specification: settle writes each section's latest decision

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | The settle asks nobody. The session running it decides from the tree, takes a written default where the tree does not decide, and the owner reviews the settle's pull request |
| `CLAUDE.md` *The rule a mechanism is kept against* | "A check gates only a fact it reads; a noisy reading, or one guessed from words, is a report." Once the settling session writes a section in its own words, no reader can count a spec's `to` text in `docs/`, so the predicate keeps only the facts it can read (the whole directory left, and it stood at the base) and the `to` comparison becomes a printed report |
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion* | Holds the three rules this work rewrites: what tells a settle from a deletion, when a released directory leaves, and how a spec's rule changes reach `docs/`. It also holds the stale "waived one command at a time" sentence this work corrects in the same section |
| `docs/release-checklist.md` *2b. Settle what earlier releases left behind* | The settle runs when the owner calls it, on the preparation branch cut from `release/vX.Y.Z`, and released means present at `--released-at` (default `origin/main`). This work keeps that and rewrites what the two commands do |
| `skills/settle/SKILL.md` *A settle is not a work item* | A settle opens no directory under `seal/specs/`, commits as `no work item`, and is reviewed at its pull request. Kept: so this work item ships the mechanism and does not run the settle |
| `docs/the-review-record.md` *What the check reads at the pull request* | `chain-check` parses each `## Rule changes` with `rule_changes.py#parse` and refuses a section that does not parse. Kept, with the sentence on what `settle` then does rewritten |
| `docs/the-review-and-parity-arms.md` *The declaration, and where the check went* | A declaration whose directory a settle removed is asked `unverified_check.py#settled` at the merge base. Kept, with the sentence on what a retirement is rewritten |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | Defines the policy in force as the baseline plus every unsettled spec's rule changes in merge order. Rewritten to the latest decision at each section |
| `CONTRIBUTING.md` *What a change to a gate must carry* | The pull request states the failure direction (the predicate allows more: any whole removal of a directory that stood at the base), a prompt budget of zero, and what it removes |
| `.github/workflows/hygiene.yml` lines 157 to 195 | CI runs `unverified_check.py --baseline origin/<base_ref> seal/specs/` and `chain_check.py --baseline origin/<base_ref>` from the tree. On the release pull request the base is `main`, where the 41 held records still hold open rows (executed: `git ls-tree origin/main seal/specs/` lists all 41), so any predicate that reads rows at the base keeps the release pull request red after a settle that decided them |

## Scope

**The design in one paragraph.** The specs are a timeline. `settle`, the
script, reads it: it groups the released specs whose rule changes name one
section, orders each group by merge, shows each group's history beside the
section as it stands, lists every open row of every released record, and
removes what the settle leaves. It writes no policy document. The session the
owner runs the settle in, the settling session below, does the judging: for
each group it writes the section as the latest decision states it, checked
against the code, and it decides every open row from the tree. It asks
nobody. Its pull request body states each judgement with its grounds and
lists the defaults it took, and the owner reviews that pull request. The
sentence "The spec decides; the command applies. The step moves and does not
verify" is replaced by: "The specs say what was decided and in what order,
the code says what holds now, and the settling session writes each section as
the latest decision the code bears out. The script reads and removes; it
neither writes `docs/` nor judges."

### In

1. **`settle` (the dry run) shows the timeline.** `skills/settle/scripts/settle.py`
   prints, for the work items released at `--released-at`:
   - each group: the specs whose operations name one place, a place being a
     file and a section, two places one group where `rule_changes.py#overlapping`
     says they can name one text. Its specs are listed in merge order
     (`rule_changes.py#order`), each operation with its kind, its spec's
     coordinate (`seal/specs/<id>/spec.md:<line>`), and two facts read from the
     working tree: whether its `from` is found in the section and whether its
     `to` is. The section's own coordinate (`<file>:<first>-<last>`) heads the
     group, or the words saying the heading is not there. Two specs whose
     adding commits no ancestry orders are marked as such inside their group,
     for the settling session to order by content; they are not a refusal.
   - each released spec to read whole: one whose `## Rule changes` does not
     parse, with the reader's reason, and one with no such section.
   - every open `## Not verified` row of every released record
     (`unverified_check.py#open_record_rows`, asked of the working tree), each
     with the backticked paths it names and whether each path is in the working
     tree. This is a report the settling session reads, not a verdict.
   - the readers of `seal/specs` under `tests/` and the citations into what
     `--apply` would remove, as today (`settle.py#citations`).
   Nothing is refused or held in the dry run for a stale `from`, a parse error,
   an unordered pair or an open row.
2. **`settle --apply` removes, and only that.** It removes every released work
   item directory whose record holds no open row in the working tree, a
   directory with a `spec.md` and one without alike, and keeps one that still
   holds a row, naming each open row. It prints, for each directory it
   removed, the rows its record closed with what closed each, so the settle's
   pull request body can copy them. It then prints `fold-check`'s lines over
   the policy root, as today (`settle.py#write_after`). It exits 0 when it kept
   nothing, 1 when it kept a directory, and 2 when the arguments or the tree
   are unusable, as today. It no longer asks the merge base of `--released-at`
   and `HEAD` anything: a row closed in the working tree is closed.
3. **`skills/settle/SKILL.md` states the settling session's procedure**, in
   order: run the dry run; for each group, read every operation in merge order,
   the section as it stands and the code the rule names (its `check:` targets
   first), and write the section as the latest decision states it, the code
   winning where it has moved past that decision; settle each superseded
   operation with its group, unapplied; read each spec listed to read whole and
   write any rule it states the same way; decide each open row as moot (it
   names a unit the tree no longer holds), answered (another record or a later
   run answered it, named), or a measurement nobody has taken (re-homed as an
   issue, `gh issue create`, or as a `seal/follow-up.md` row where the
   repository has no tracker), and close it in the record with `closed` and
   what closed it; where the tree does not decide, take a default and write it
   down; run the documents' checks over what it wrote and change whatever the
   written sections leave standing on an old fact (a pin under `tests/`, a
   README copy), naming each in the pull request body; run `settle --apply`;
   run the repository's `Broad gate` row once; open the pull request whose body
   lists, per group, the decision and its grounds, the superseded operations,
   the rows by kind with what closed each, the defaults under the decisions it
   leaves open, the answers for the checks that read the corpus, and how it
   was checked. It asks nobody at any step.
4. **The CI predicate reads only what it can read.**
   `unverified_check.py#settled` holds a directory as settled when the
   directory stood at the merge base and is gone whole. The condition that
   nothing in its record was open at the base goes, and so does the replay
   that counted each applied operation's texts in `docs/`. Its two readers,
   `unverified_check.py --baseline` and `chain_check.py#retired`, keep calling
   it. A pull request that removes an `overview.md` from a directory that
   stays is still a deletion, and so is one that drops rows from a table.
5. **The messages a person reads say the new fact, each pinned by a case.**
   `chain_check.py#SETTLE_SAYS` ("nothing open at the merge base, and the
   policy root holds every rule change its spec states"), the `settled:` notice
   of `unverified_check.py --baseline` (`unverified_check.py` near line 1751),
   its `--baseline` help text and its module docstring (lines 25 to 27), and
   `chain_check.py#RULE_CHANGES_SAYS` ("and `settle` applies nothing from this
   spec"), which becomes a statement that `settle` cannot group the spec.
6. **The `## Rule changes` grammar does not change.** `rule_changes.py#parse`,
   `GRAMMAR`, the no-change block and the pull request's parse stay as they
   are. What changes is what `from` means: the text as the spec's framer read
   it, which locates the change for the settling session and for a reviewer,
   and is not a precondition. `skills/settle/SKILL.md` *Rule changes* says so.
7. **The places that state the present behaviour are rewritten**, each in the
   same commit as the code it describes: `skills/settle/SKILL.md` (whole: the
   description, the opening, *The index*, *What `--apply` does*, *A released
   work item with no `spec.md`*, *What this does not do*), `README.md` lines
   116 and 262 and `README.ko.md` lines 112 and 252, `seal/README.md` lines 5
   to 9 and `templates/seal-README.md`, which is the same text,
   `templates/config.md` line 436, `skills/config/SKILL.md` line 43, and
   `skills/implement/SKILL.md` line 75. The policy root changes only through
   `## Rule changes` below.

### Out

- **Running the settle.** This work item ships the mechanism. The owner runs
  the 0.22.4 release settle (`docs/release-checklist.md` *2b. Settle what
  earlier releases left behind*) after this merges into `release/v0.22.4` and
  before the release pull request, with the tree's script, as `plan.md`
  *Operational impact* says. A settle is not a work item, and its 41
  directories and their row decisions would enlarge this work item's review
  rounds with judgements the frame cannot state in advance.
- **`1792935671-the-routing-check-moves-to-the-sessions-tools`.** It is not
  present at `origin/main` (executed:
  `git ls-tree --name-only origin/main seal/specs/`), so the 0.22.4 settle does not count it released; it settles
  at the next release's settle, with every other 0.22.4 work item.
- **A new grammar for `## Rule changes`.** `questions.md` answered list, A1.
- **A pull-request check that applies a spec's `to` texts and runs the
  documents' checks over them.** `questions.md` answered list, A3.
- **Local mode (#955).** `settle` still refuses a root under the common git
  directory. #955 lands after this item on the same skill and will touch
  `settle.py#main` (the local-mode refusal), `settle.py#released` (a ref holds
  no local directory, so released needs another definition there),
  `skills/settle/SKILL.md` *It refuses to run in local mode*,
  `docs/the-review-record.md` *The stamp* ("since `settle` retires no
  local-mode work item"), the `settle` rows of both READMEs,
  `tests/test_settle.py::Test_main::test_refuses_local_mode_rather_than_reading_an_empty_repository`
  and `tests/test_settle_reads_before_it_removes.py::test_the_module_and_the_skill_both_say_local_mode_is_refused`.
  This item frames none of it.
- **`docs/one-root-by-lifetime.md` lines 17 and 45 and their Korean
  edition.** "lives until `settle` applies its spec and removes it" and
  "`settle` rewrites `docs/` and removes directories" stay true of a settle
  that writes the latest decision, so nothing there changes.
- **`agents/framer.md` lines 54 to 61 and 147.** "the unsettled specs'
  `## Rule changes`" and "at the settle that applies its spec" stay true; the
  definition of the policy in force they point to is rewritten at its one
  home, `skills/implement/SKILL.md` line 75.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 two specs on one sentence | Given two released specs, merged in order, each with a `change` to one sentence of one section, the later one's `from` quoting the sentence as the earlier left it and the earlier's `from` no longer matching. When `settle` runs, then both appear in one group in merge order, the earlier with its `from` not found, and nothing is refused; when both records hold no open row, `settle --apply` removes both directories and writes no document | a case in `tests/test_settle.py`, seen red against the current code, which refuses the pair |
| S2 a stale `from` | Given a released spec whose `from` matches nothing (the shape of `1792627930`). When `settle` runs, then its group lists the operation with `from` not found, and the spec is neither refused nor waited on | a case in `tests/test_settle.py`, seen red against the current refusal |
| S3 an open row keeps, a closed one goes | Given a released directory whose record holds one open row. When `settle --apply` runs, then the directory stays, the row is named and the exit is 1; when the row is closed in the working tree and not committed, a second `settle --apply` removes the directory, prints the row with what closed it, and exits 0 | cases in `tests/test_settle.py` replacing `test_an_uncommitted_closure_keeps_the_directory` and `test_a_closure_the_base_has_not_seen_keeps_the_directory`, each seen red |
| S4 a spec that joins no group | Given a released spec whose section does not parse, and one with no `## Rule changes`. When `settle` runs, then each is listed to read whole with its reason; when their records hold no open row, `--apply` removes both | cases in `tests/test_settle.py` replacing `test_a_section_that_does_not_parse_keeps_its_directory` and the case that keeps a spec with no section |
| S5 an unordered pair | Given two specs at one place whose adding commits no ancestry orders. When `settle` runs, then they are one group with the pair marked unordered, and nothing is refused | a case replacing `tests/test_settle.py::Test_main::test_two_specs_on_parallel_branches_at_one_place_are_a_conflict` |
| S6 the settle's pull request | Given a pull request that removes a whole released directory whose record held an open row at the base and whose spec's `to` text is not in `docs/`. When `unverified_check.py --baseline` and `chain_check.py --baseline` run, then the first prints the `settled:` notice and the second `retired: a settle`, and neither fails | cases marked `a-settle-is-no-deletion` in `tests/test_unverified_check.py`, and a case in `tests/test_chain_check.py::Test_retired`, each seen red against the current predicate |
| S7 the release pull request | Given a base that holds a directory with open rows, and a head where one squash commit removed it whole. When `unverified_check.py --baseline` runs against that base, then the directory is settled, not deleted | a case in `tests/test_unverified_check.py`, seen red against the current predicate |
| S8 a deletion stays a deletion | Given a pull request that removes `overview.md` from a directory that stays, or drops a row from a table. When `unverified_check.py --baseline` runs, then it fails as today | the existing cases in `tests/test_unverified_check.py` (`test_refuses_a_removal_no_settle_explains` and the fewer-rows cases), passing unchanged |
| S9 the parse message | Given a work item `spec.md` whose `## Rule changes` does not parse. When `chain_check.py` runs at the pull request, then it refuses at the reader's line with the new `RULE_CHANGES_SAYS` text | `tests/test_chain_check.py::Test_rule_changes_read`, its pinned text rewritten and seen red |
| S10 the real corpus | Given the tree at the build's head. When `python3 skills/settle/scripts/settle.py --released-at origin/main` runs, read-only, then it lists the groups of the six released specs that state rule changes, refuses none, and lists every open row of the 41 released records | executed by the smith, the counts and the group headings recorded in the phase record; no `--apply` |
| S11 the procedure is written | Given `skills/settle/SKILL.md`. Then it states the settling session's steps of *In* item 3, the replacement sentence of *The design in one paragraph*, and that nobody is asked; the sentence "The spec decides; the command applies" is gone | cases in `tests/test_settle_reads_before_it_removes.py` replacing `test_the_skill_says_the_spec_judges_and_the_command_applies`, `test_the_skill_says_the_directory_goes_with_the_rule_it_applied` and `test_the_skill_states_how_the_changes_land`, each seen red |
| S12 the rule changes parse | Given this `spec.md`. When `chain_check.py` reads it, then its `## Rule changes` parses | `rule_changes.py#parse` over this file, run by the smith |

## Data & interfaces

- **`bin/settle` and `settle.py`'s flags do not change**: `settle`,
  `settle --apply`, `--released-at REF` (default `origin/main`), `--root DIR`.
  The exit codes keep their meanings (*In* item 2). The dry run's headings and
  line shapes are the build's to choose and the cases' to pin; *In* item 1
  names what each holds.
- **`rule_changes.py` keeps** `parse`, `GRAMMAR`, `Op`, `Parsed`, `headings`,
  `heading_text`, `letters`, `pattern`, `place`, `where`, `overlapping` and
  `order`, and gains one function that groups ordered specs by `overlapping`
  places. It loses `replay`, `conflicts`, `_ancestor`, `apply_op` and `_cut`.
  Where the dry run needs a section's line range, the function that finds it
  lives here, reading headings through `headings` as `apply_op` did.
- **`settle.py` loses** `rule_plan`'s holds and replay, `apply`'s document
  writes and its creation of the policy root and index, `rule_arm`'s call of
  `unverified_check.py#settled`, the merge base it computed (`survey`'s
  `base`, `base_label`, `base_moved`), `RULE_BASE_HEADING`,
  `RULE_MOVED_HEADING`, `base_heading`, `NO_BASE_SAYS` and the refusal of a
  `--released-at` that shares no commit with `HEAD`. It keeps `released`,
  `citations`, `write_after`, `load` and `main`'s root and mode refusals.
- **`unverified_check.py#settled(root, ref, directories)`** returns the
  directories that hold a file at `ref`. Its callers pass only directories
  absent at the head side, as they do today. `here` and `wrote_a_spec` go
  where nothing else calls them.
- **`unverified_check.py#rule_changes`** stays as the loader; its docstring
  stops naming the replay.

## Rule changes

- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: **A removed work item directory is a settle, not a deletion, when
    replaying it gives what the tree holds.** Each directory a pull request
    removes whole is judged as it stood at the merge base: nothing in its
    record open, and either no rule to replay (it wrote no `spec.md`, or its
    spec has no `## Rule changes` or holds the no-change block) or the replay
    holds. The replay applies every removed spec's rule changes, in merge
    order, over the merge base's `docs/`, and each text an applied operation
    names must occur as often across `docs/` at HEAD as in the replay,
    whitespace collapsed. So a later spec may rewrite what an earlier one
    placed, and a split along headings in the same pull request passes. One
    predicate, `unverified_check.py#settled`, answers `settle`,
    `unverified-check --baseline` and `chain-check`, and a refusal keeps the
    directory, the cheaper mistake.
  to: **A work item directory a pull request removes whole is a settle, not
    a deletion, where the directory stood at the merge base.** A settle
    removes released directories whole, and no other step of the workflow
    removes another work item's directory, so the whole removal is the fact
    the readers read. What the settle wrote into `docs/` is not read here:
    the settling session writes each section in its own words, a reader
    could only guess at that from words, and the settle's pull request
    states each decision for the owner to review. A pull request that
    removes part of a directory, an `overview.md` from a directory that
    stays, or a row from a table is still a deletion. One predicate,
    `unverified_check.py#settled`, answers `unverified-check --baseline`
    and `chain-check`. A pull request outside a settle that removes a whole
    work item directory reads as a settle too; its diff shows the removal
    to its review.
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: **A released work item that wrote no `spec.md` states no rule, and
    it is retired by that rule, with no marker.** Such an item was below the
    SDD ladder: a release entry, a renumbering, a CI repair, a pull
    request's record. Those are records of a moment, and a moment states no
    rule, so nothing has to be carried out of one: `settle` prints these
    under their own heading and `settle --apply` removes them without
    writing into `docs/`. **One condition narrows it: nothing in the record
    may still be open.** An open `## Not verified` row is a claim with an
    answerer rather than a rule, so a directory holding one is kept and
    named with its rows, and closing each row — a row re-homed is closed
    too, `closed` naming where it went — in a pull request merged before
    the one that retires the directory is what lets the next retirement
    take it. The CI readers ask the rule of the merge base, so a closure in
    the same pull request as the removal is still open where they look.
    `settle` asks it at the merge base of `--released-at` and `HEAD`, which
    is where they look until the base moves past the fork and earlier
    after, and keeps a directory whose closure has reached the working
    branch and not that base. Whether the item wrote a `spec.md` is asked
    of its history, so a spec deleted in one commit, or in an earlier pull
    request, and the directory in the next is still a deletion. That
    condition is a judgment the repository owner may overturn. An item that
    did write a `spec.md` leaves when `settle --apply` applies its rule
    changes.
    check: tests/test_settle.py
  to: **A released work item leaves at the settle whatever it wrote, and
    the settling session decides every open row of its record before it
    goes.** An open `## Not verified` row is a claim with an answerer, and
    the rule it qualifies reached users in the code with the release, so
    holding the directory back stops nothing. The session reads each row
    against the tree. A row naming a unit the tree no longer holds is moot;
    a row another record or a later run already answered is answered, and
    the closure names that record; a row naming a measurement nobody has
    taken is re-homed as an issue. Each is closed in the record, `closed`
    with what closed it, and `settle --apply` removes a directory only once
    its record holds no open row in the working tree. The settle's pull
    request body carries every closure, an issue carries every re-homed
    row, and git keeps the record. A released work item that wrote no
    `spec.md` states no rule and goes the same way.
    check: tests/test_settle.py
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: **A released spec's rule changes are applied to `docs/` in place,
    and its directory goes with them, never before.** `settle --apply`
    replays each released spec's `## Rule changes` in merge order, writes
    what applies, and removes each applied directory whole; a spec it
    cannot place applies nothing and its directory stays. The judgment was
    made when the spec was written and reviewed, so applying it judges
    nothing, and no sentence is written by hand. No marker is written.
    check: tests/test_rule_changes.py tests/test_settle.py
  to: **The settle writes each section as the latest decision among the
    released specs states it, checked against the code.** The specs whose
    rule changes name one section, or a section holding it, are one group,
    and merge order sorts it, so a group is that rule's history. Within a
    group the latest spec that states a rule decides it, and an earlier
    operation it restates is superseded: it is settled with the group and
    not applied. Where the code has moved past the latest decision, the
    code is the later fact and the section states what the code does. The
    settling session writes the section; an operation's `from` locates the
    text its spec's framer read, and a `from` that no longer matches is
    history, not a refusal. The rest of the document stays as it was, and
    no marker is written. `settle` groups the specs, shows each group's
    history and removes the directories; it writes no policy document.
    check: tests/test_rule_changes.py tests/test_settle.py
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: Its commits are waived one command at a time and what it applied
    is reviewed at its pull request.
  to: Its commits carry the trailer `SpecSeal-Routing: no work item`, and
    what it wrote is reviewed at its pull request.
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: The first prints the rule changes the released specs state, in
    merge order, what it refuses and what the second would remove. The
    second applies them to `docs/` in place and removes each applied spec's
    directory whole, and each released directory with no `spec.md` and
    nothing open. A refused spec applies nothing and waits for a later
    settle. `fold-check` then reads the documents the second wrote, and
    names each one past its ceiling as one to split
    (`skills/settle/SKILL.md` *A document past its ceiling is split, never
    trimmed*).
  to: The first prints each group of released specs whose rule changes
    name one section, in merge order, and every open row of every released
    record. Between the first and the second, the session running the
    settle writes each section as its group's latest decision, checked
    against the code, and closes each open row with what closed it, asking
    nobody (`skills/settle/SKILL.md` is the procedure). The second removes
    every released work item directory whose record holds no open row, and
    names any it keeps. `fold-check` then reads the documents the settle
    wrote, and names each one past its ceiling as one to split
    (`skills/settle/SKILL.md` *A document past its ceiling is split, never
    trimmed*). The settle's pull request body states each decision with
    its grounds and lists the defaults it took, and the owner reviews it.
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: and the retirement is `settle --apply` removing a released work
    item's directory once `docs/` holds its rule changes.
  to: and the retirement is `settle --apply` removing a released work
    item's directory whole.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: `settle` reads the section after the release and applies nothing
    from a spec whose section does not parse, so a section first read there
    is a rule change that never lands, with no pull request left to fix it
    in.
  to: `settle` groups the released specs by the sections their rule
    changes name, and a spec whose section does not parse joins no group,
    so a section first read there is a rule change the settle can place
    only by reading the whole spec, with no pull request left to fix it in.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: A `spec.md` with no `## Rule changes` section is left alone, as
    `settle` leaves it.
  to: A `spec.md` with no `## Rule changes` section is left alone here, and
    the settle reads such a spec whole.
- change
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  from: stay until `settle --apply` applies the spec's rule changes,
    and then the directory goes whole
  to: stay until the settle: the settling session writes the spec's
    sections, and `settle --apply` removes the directory whole once its
    record holds no open row

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The literal, whole-or-nothing, merge-order apply | `skills/settle/scripts/rule_changes.py#replay` | the settling session writes each section (`skills/settle/SKILL.md`); the grouping it read places with lives on in `rule_changes.py#overlapping` and the new grouping function |
| The conflict class of #1025 | `skills/settle/scripts/rule_changes.py#conflicts`, `rule_changes.py#_ancestor` | two specs at one place are one group, and a pair no ancestry orders is marked inside it for the settling session |
| Writing a policy document from a script | `skills/settle/scripts/rule_changes.py#apply_op`, `rule_changes.py#_cut`, `skills/settle/scripts/settle.py#apply`'s document writes and its creation of the policy root and `INDEX` | the settling session writes `docs/`; where it creates the policy root it writes the index with it, as `skills/settle/SKILL.md` *The index* will say |
| The hold on an open `## Not verified` row, at the plan | `skills/settle/scripts/settle.py#rule_plan` | `settle --apply` keeps a directory whose record holds an open row in the working tree, and the settling session closes every row first |
| The closure-must-reach-the-base rule (#602) | `settle.py#RULE_BASE_HEADING`, `settle.py#RULE_MOVED_HEADING`, `settle.py#base_heading`, `settle.py#NO_BASE_SAYS`, `settle.py#survey`'s merge base and the refusal of a `--released-at` sharing no commit with `HEAD`; `skills/settle/SKILL.md` *A released work item with no `spec.md`* paragraphs "Close it in a pull request of its own" and "Merged first means merged"; `README.md` line 262 and `README.ko.md` line 252, their last sentences | the CI readers no longer ask rows at the base, so a closure in the working tree is the fact; nothing lands in their place |
| The open-row and replay conditions of the predicate | `skills/verify/scripts/unverified_check.py#settled`; `unverified_check.py#wrote_a_spec` where nothing else calls it | the predicate reads the whole removal of a directory that stood at the base (`docs/the-record-layout.md` *The fold, and what tells it from a deletion*, rewritten above) |
| "The spec decides; the command applies. The step moves and does not verify", and *What this does not do* "It does not verify" | `skills/settle/SKILL.md` *settle — apply what released specs decided* and *What this does not do* | the replacement sentence in *Scope*, written into the skill |
| *What `--apply` does*, its four bullets (merge order wins, whole or not at all, in place, a directory goes only with what it applied) | `skills/settle/SKILL.md` *What `--apply` does* | rewritten in place to *In* items 1 and 2 |
| The cases that pin the replay, the holds, the conflict and the base rule | `tests/test_rule_changes.py::Test_replay` (all eleven cases); in `tests/test_settle.py`, `Test_apply::test_an_open_memo_row_keeps_a_spec_less_directory`, `test_a_closure_the_base_has_not_seen_keeps_the_directory`, `test_an_uncommitted_closure_keeps_the_directory`, `test_a_closure_the_base_has_seen_lets_the_directory_go`, `test_a_base_that_moved_past_the_fork_names_the_merge_that_moves_it`, `test_refuses_a_survey_with_no_base` (both), `test_the_predicate_is_what_settle_asks`, `Test_main::test_two_specs_on_parallel_branches_at_one_place_are_a_conflict`, `test_apply_rewrites_in_place_and_removes_the_directory`, `test_apply_follows_merge_order`, `test_what_apply_removed_is_settled_for_the_readers`, `test_apply_deletes_a_document_its_removal_leaves_empty`, `test_a_rule_change_half_applied_is_not_settled`, `test_apply_refuses_a_conflict_and_keeps_both`, `test_apply_writes_nothing_of_a_refused_spec`, `test_an_open_record_row_holds_its_spec`, `test_a_section_that_does_not_parse_keeps_its_directory`, `test_the_text_applied_is_the_spec_as_released`, `test_a_spec_no_commit_adds_is_held`, `test_apply_creates_the_policy_root_the_config_names`, `test_a_name_that_differs_only_in_case_is_held`, `test_a_shallow_clone_is_not_told_the_refs_share_no_commit`, `test_no_merge_base_is_refused_and_nothing_is_removed`, `Test_module::test_the_base_heading_says_where_the_closure_has_to_go`, `test_the_predicate_asks_every_condition_itself`, `test_every_reader_of_a_retirement_calls_the_one_predicate`; in `tests/test_settle_reads_before_it_removes.py`, `test_a_closed_row_is_told_to_merge_before_its_directory_goes`, `test_the_documents_say_the_closure_has_to_reach_the_base`, `test_the_skill_says_the_spec_judges_and_the_command_applies`, `test_the_skill_says_the_directory_goes_with_the_rule_it_applied`, `test_the_skill_states_how_the_changes_land`; in `tests/test_unverified_check.py`, the `Test_settled` cases and the two `a-settle-is-no-deletion` cases that pin the rows and the replay, and `Test_rule_changes::test_accepts_the_one_reader_of_a_specs_rule_changes`'s `replay` assertion | each is retired with the behaviour it pins, or rewritten to S1 to S11, which replace them; a case kept where its behaviour stays (the readers, the citations, the local-mode refusal, the settled root, the case-insensitive name where the dry run still reports it) is the build's to keep, and the phase record names which |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-26 by framer, before the build.
