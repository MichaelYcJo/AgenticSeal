# 1792459424-docs-states-the-current-rule-in-one-read — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 091f4ef6 |

## What this phase was asked

The commit gate group rewritten to the current rule, once:
`docs/commit-review-gate-spec.md`, `docs/the-commit-gate-inside-git.md` and
`docs/the-review-and-parity-arms.md`. Narrated history, dated decisions and
"this used to" paragraphs go; a sentence stays only where an agent not editing
the gate would decide wrongly without it; internal mechanics go to the test
that holds them; no symbol a reader can trip on as syntax, no value stated
twice, split along existing headings only. The group's backlog specs read,
what they decided and `docs/` lacked written in, their rows closed by the
closers of `spec.md` *Data & interfaces*, and a no-change block added. At the
boundary the six checks of `plan.md`'s phase 4 row, every test file naming a
rewritten document, the seven meta modules, `bin/rules --check`,
`bin/fold-check` and ruff, with the census below and S14's grep.

## What this phase found

- **The three documents went from 74,607 bytes to 38,546 by the rewrite.**
  Every check line kept its targets, and two rules gained a line: the waiver
  typed in front names `tests/test_the_waiver_can_be_typed.py`, and the
  unresolved target names `tests/test_what_the_reader_understands.py`
  beside its old module. The parity arm's failed diff, which named its module
  in prose, now names it on a check line. Two pins followed a renamed heading
  and sentence (`tests/test_a_gate_that_fails_says_so.py`,
  `tests/test_edits_go_through_the_edit_tool.py`); each new pin is absent
  from the old text, and each was mutated with `mutation-check` and went red.
- **A copy the paste ratchet caught.** The first draft restated the routing
  template's sentence about the `no work item` answer, and
  `tests/test_no_passage_is_pasted_into_a_second_file.py` refused the pair.
  The arms document now points at the template instead.
- **The census.** Each rule the old text stated, and where it lives now.

  | Old rule | New home |
  |---|---|
  | Gates run in groups; strictest wins; every reason kept; a raising gate is skipped | the document, *Registration* |
  | A failing gate is said once at turn end | the document, *Registration*; "a load-time `SystemExit` used to end the group" and "before this, a skipped gate read like an allow" gone as history |
  | The reading judges only where git cannot (0.16.0, #692) | the document, *The PreToolUse reading of a commit*; the release and issue gone |
  | Two opt-ins evaluated independently; declared together since the migration config moved into `seal/` at 0.10 | the arms document, *The two arms of the commit gate*; the 0.10 story and the pre-0.10 address gone |
  | The decision table; a deny addresses the model, an ask the user | the document, same section |
  | The repository judged is the one committed into; `-C` composes; the operator table | the document, *Which repository*; the measured defect's narrative gone; each operator held by `tests/test_gate_judges_the_repo_it_commits_to.py` (`test_or_reaches_the_directory_the_cd_did_not_leave`, `test_a_pipeline_does_not_move_the_shell_that_commits`, `test_a_branch_that_skips_a_cd_keeps_the_directory_it_skipped_from`) |
  | An operator at a line end binds; a backslash continuation | `tests/test_gate_judges_the_repo_it_commits_to.py` (`test_an_operator_at_the_end_of_a_line_is_still_that_operator`, `test_the_first_operator_after_a_segment_is_the_one_that_binds`) |
  | A heredoc body is data for where; a herestring opens none; an unterminated body runs to the end; `$((1<<2))` is a shift | the rule: *Only what the shell would execute*; the cases: `tests/test_gate_judges_the_repo_it_commits_to.py` and `tests/test_what_the_reader_understands.py` |
  | The consent read keeps comments and skips bodies; an unsplit command carries no token past its failure | the document, same paragraph; the substring fallback's history gone |
  | A file edit goes through the `Edit` tool; the one heredoc shape, slot by slot | the document, every slot kept; #34, #75, #670, #739, #760 and #763 gone, and "exactly as before" with them |
  | A failure branch waits for its operator; `;` consumes both branches | the table rows `cd X ; git commit` and `cd X && make \|\| git commit`; `tests/test_gate_judges_the_repo_it_commits_to.py::test_a_semicolon_carries_the_commit_to_both` |
  | The reader enumerates what it understands, and anything else is unreadable | the document, the unresolved table's last row; the measurement of seven commands gone |
  | Exclusive branches are not walked as one; the bound past 16 branches | `tests/test_gate_judges_the_repo_it_commits_to.py` (the `build/dist` case) and `hooks/cmdline.py#STATE_CAP` |
  | The common `cd src && git commit` costs what it cost | the document, *Which repository*, its first paragraph |
  | A variable `-C` resolves to no repository; the release session whose commits passed a gate that looked at nothing | the rule: the unresolved table; the story gone |
  | An unresolved target stops where the session's own repository opted in; the ways on, path first | the document, the bold rule and the sentence under the unresolved table |
  | The worktree guard reads a command the same way and keeps judging its own tree | `docs/worktree-guard-spec.md` *Which tree*, phase 5's |
  | A commit behind a reserved word (#669); a case arm's stand-in; `!` and `time`; `for`, `select`, `case`, `in` | the rule: *A commit is read wherever the shell would run one*; the positions: `tests/test_a_commit_behind_a_reserved_word_is_judged.py` |
  | A commit behind a runner, in a string or a substitution (#670); `parallel`; positional parameters | the rule: same paragraph; the lists: `hooks/cmdline.py#RUNNERS` and `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py` |
  | A script or remote runner stays unread | the document, same paragraph |
  | `NESTING_READ`, 32 levels | the rule: same paragraph; the number: `hooks/cmdline.py` and `tests/test_no_shape_the_base_stops_reads_silent.py` |
  | A program word read past a redirection, a glued redirection, the split operators' view, zsh's precommands, headers by position, a host glued to `(` (#674); `sudo -s` and `-i` are no string hosts | the rule: same paragraph; the positions: `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py` and `tests/test_no_shape_the_base_stops_reads_silent.py` |
  | "The reading can only have gained stops" (three times); the 11,393 and 6,033 command corpora | *A change to the reading adds stops and never removes one*; the corpora gone as measurements |
  | `STATE_CAP`, the base's own thread, the order of directories | `tests/test_no_shape_the_base_stops_reads_silent.py` and `hooks/cmdline.py#STATE_CAP` |
  | The guard and the consent writer read a frozen copy of `86256492`'s reader | `docs/the-commit-gate-inside-git.md` *The convergence argument*, naming `hooks/cmdline_base.py` |
  | Why a deny; the record path; an unwritable record counts as asked | the document, *The first stop is a deny* |
  | Under the `automation` press every stop is a deny, and what its reason names | the document, *Where the person pressed automation*; the milestone-49 measurement gone, its grounds kept as one clause |
  | The press is read once a stop is decided; `per axis` and the `Automation` row unread; the last answer stands; the attended answer on any failure; the reason's text is the only bound | the document, same paragraph |
  | Two readings that prompted that run stay; 1790635415's narrowing; Q1 of 1791089603 | *A change to the reading adds stops and never removes one*; the history gone |
  | Both arms, one call | the document |
  | The implementer mark and notice | the document, *The implementer mark and notice*; "until these two hooks existed" gone |
  | Judged inside the commit; M6's figures over 413 commands | the rule: `docs/the-commit-gate-inside-git.md`; the figures gone |
  | The stubs, the marker line, a foreign clone (P1) | the same document; the question reference gone |
  | A person's own commit, the session variable, the lease, `CLAUDE_PID`, `is_claude` (P2, #868) | the same document; the references gone |
  | How a stop is put; the git-native waiver; the old spelling's per-call answer (P3, #773, #868) | the same document; the references gone |
  | The guarantee refusal | the same document, unchanged |
  | `--no-verify` is met at `reference-transaction` (M12) | the same document, with the four gits it was measured on; M12 gone |
  | Git's own sequencer commits are not judged (rounds 1 and 2 of #692) | the same document; the history gone |
  | The PreToolUse reading stands aside where git decides; the plain rule (P5, P7) | the same document; "three review rounds each found spellings a list missed" becomes "such a list is never finished" |
  | The convergence argument; the owner's answers of 2026-10-01 | the same document; the date gone |
  | Known limits: an unreached clone (M8's count gone), an unplaced construct, `rm` and `chmod` (the rounds gone), `commit-tree` and `am`, a sequencer-state commit, Windows (two bullets made one, the CI run numbers gone), the old spelling, latency (#975's figures gone, the latest kept) | the same document, *Known limits of the commit gate inside git* |
  | Where each state of a repository stands | the same document; "as 0.16.0" becomes "the PreToolUse reading" |
  | The review arm's table | `docs/the-review-and-parity-arms.md` *Review arm*; a missing mark "contributes a stop" |
  | Why the review arm has no document-root line (#518's and #514's counts) | the same section; the counts gone |
  | The marker is decided when the work starts; the incentive ran backwards | gone: the introduction of the declaration; the rule is *There is no standing waiver* |
  | Where the marker goes; the three-shell table | *The waiver goes in front of the command*, on a check line naming `tests/test_the_waiver_can_be_typed.py`, whose cases hold the table |
  | The declaration table; two answers, not three (#241) | the arms document, *The declaration, and where the check went* |
  | A retired or renamed declaration; a settle tells it from a deletion; the first fold's 88 | the same section; the count gone |
  | Records read as git carries them at `HEAD`; `--worktree` | the same section |
  | A failed lookup resolves to asking | the same section, *There is no standing waiver* |
  | "This is a reversal, and of this document" | gone as history; the rule is *There is no standing waiver* |
  | What the declaration costs | the same section |
  | The parity arm's table; the change is every path the commit carries | the arms document, *Parity arm* |
  | A diff git could not take is asked about (#868) | the same section, on a check line naming `tests/test_chain_hooks_hardening.py` |
  | The parity mark says a comparison was recorded | the same section |
  | Ask chosen over deny; the old-worry table | gone: deny once and then ask is `docs/commit-review-gate-spec.md` *The first stop is a deny* |

- **S14, the renamed headings.** `git grep -F` outside `seal/` and
  `changelog/` for each old heading text (*Registration — gates run in
  groups*, *commit-review-gate (PreToolUse*, *and what happens when it cannot
  be read*, *A `cd` the gate cannot read*, *Why a deny*, *implementer-mark ·*,
  *reference-transaction · post-commit*, both arms' *opt-in:* headings,
  *Where the marker goes*, *where the check went instead*, and the three H1s)
  finds no citation. *the gate cannot read* matches the refusal text in
  `hooks/commit-review-gate.py` and two tests, which quote the message, not
  the heading. The citations that remain, *Registration*, *Review arm*,
  *Parity arm*, *The commit gate inside git* and *Known limits of the commit
  gate inside git*, name headings that stand.
- **The backlog of this group.** The assignment rule of `spec.md` leaves a tie
  open; a tie went to the group the spec's title is about, and to the later
  phase where the title names neither (overview). This phase took 8 specs:
  7 by count and `1790644505` by title from a tie with phase 5.

  | Work item | What it decided, and where it is | Rows |
  |---|---|---|
  | `1790635415` | written: *Registration*; internal: the record and the draw | 4 closed |
  | `1790644505` | written: the deny under the press, and the commit naming its repository (agent contract) | 3 closed |
  | `1790660768` | written: the reading's positions and the adds-stops rule; internal: the merged view and the bounds | 2 closed |
  | `1790815613` | written: the commit judged inside git; overturned: the `post-checkout` half, by its own P6 | 11 closed, 2 open |
  | `1790993140` | written: the guard's half, in `docs/worktree-guard-spec.md`; internal: the reader's spaced options and `env -S` | 1 closed, 1 open |
  | `1791019477` | internal: a cut along headings, no rule | 1 closed |
  | `1791089603` | written: the one heredoc shape; internal: its clause-by-clause grounds | 4 closed, 1 open |
  | `1791119070` | written: the waiver counts only in front of the call's own command; internal: the case table | 2 open |

  The closers used: the work item's own merged pull request for a suite row,
  each of #660, #671, #679, #705, #744 and #769 read with `gh pr view` as
  green on lint and all three pytest legs; #997's legs, all green, for a
  platform row whose cases still exist; aadf2efb for the `Over the ceiling`
  freeze it removed; and four limit sentences now in the documents (the
  report on screen, the race, the live harness, and the model that re-issues
  a command). A green leg means each case passed or skipped by its own
  condition. The suite rows name a typecheck the repository does not
  configure, and each closing cell says so.
- **Q4 for this group: six rows no closer closes, keeping four directories.**
  `1790815613`'s "at least 3 denies" provenance and its M5, the isolation
  spawn, which phase 5 closes with a limit in `docs/worktree-guard-spec.md`;
  `1790993140`'s stub under `env -S` with a lease; `1791089603`'s count of
  I10's corpus; and `1791119070`'s two cases no test pins (a body token
  carried to a real hook, and the splitter's over-drop). Each is a case or a
  count nobody owes, and none is a screen, a harness or a removed subject.
  `bin/settle --released-at HEAD` lists the other four as nothing to apply
  and as removed by `--apply`, and holds these four for those rows.
- **The checks at the boundary (executed):** `bin/fold-check` exit 0, no
  group document past 25000; `bin/rules --check` exit 0, 240 lines; the S7
  comparison over the three documents at 876d865b and now names no path lost
  and two gained; `unverified_check.py` over the eight directories, 6 open and
  26 closed; the 20 modules (every test file naming a rewritten document, the
  settle and record modules, and the seven meta modules) 1252 passed; ruff
  clean over the two changed test files.
