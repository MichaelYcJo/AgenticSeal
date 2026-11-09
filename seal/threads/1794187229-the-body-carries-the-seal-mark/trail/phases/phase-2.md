# Phase 2: 1794187229-the-body-carries-the-seal-mark

## What this phase found

**The frame holds for this phase, except where the mark is composed by
two copies of the plugin.** Every coordinate of `chain_check.py` that
`frame/plan.md` *Technical context* gives stood where it says (read):
`main` at line 1867, `pull_request_state` at 536 and
`event_payload_present` at 530. The exception is the next paragraph.

**Finding for the orchestrator: the mark's address carries the version
of the plugin copy that composes it, and the body and the arm can be
composed by two copies.** `pr_body.py#MANIFEST` is the manifest beside
`pr_body.py`, and `_mark_line` builds `.../raw/v<version>/...` from it
(read). The orchestrator's `seal` on PATH resolves to the installed plugin,
0.35.1 in this session, while this tree's manifest reads 0.36.0 (executed:
`which seal`, `grep version .claude-plugin/plugin.json`). The body of #1446
carries `raw/v0.35.1` and the body of #1451 carries `raw/v0.36.0`
(executed: `gh pr view <N> --json body`). This repository's `hygiene.yml`
runs the tree's `chain_check.py`, so a body written by the installed `seal
pr-body` during a release whose tree has moved the version differs from
the arm's composition on the mark line. A user's workflow clones the plugin
at the tag it pinned at install, and the user's session runs the installed
plugin, so the two differ after any plugin update. Running `seal pr-body`
again writes the same body, so the repair the design's failure direction
names does not clear that refusal. The design's G11 and S2 hold only where
the two versions agree. The arm is built as framed. Whether the mark's
address should stop depending on the composing copy, or the orchestrator
should run the tree's `bin/seal pr-body` in this repository, is a decision
for the orchestrator or the framer. It is written in `gaps.md`
`## Not verified`.

**Decision on `frame/questions.md` Q1: a refusal in the body is annotated
on the work item's directory at line 0, and the message names the body's
line.** The printed line reads
`seal/threads/<id>:0  the pull request's body, line 3: lacks ...`. Option
(a), `pr.md` with the body's line, puts a line number on `pr.md` that is
past its end for every line of the copy, and the copy is most of the
body. GitHub shows an annotation it cannot place on a diff line on the run,
which is option (b)'s rendering whichever path it carries. Line 0 is how the
guarantee arm names a file as a whole, so the reader does not take the
number for a line of the path. The repair the refusal asks for never edits
the directory or `pr.md` by hand: it runs `seal pr-body` again and sends the
file, so the path only needs to name the work item. A cause `compared`
places at a record (`pr.md` missing, a round record that does not parse) is
annotated at that record's path under the work item and its line, as every
other arm annotates a record. Judged against `frame/questions.md` Q1's
three options and `chain_check.py#guarantee`'s line 0 for a whole file.

**Decision: which work item the body is compared for.** The design names
two shapes: one judged work item, and more than one holding `pr.md`. The
arm compares for the one work item holding `pr.md`, or for the lone judged
work item when it holds none, which `compared` then refuses at `pr.md`
(design G9). Several judged work items with no `pr.md` among them are named
as not read for each, as the two-holder shape is. A work item whose
declaration is retired or does not parse is not a candidate, since the
other arms do not judge it either. Judged against `frame/design.md`
*Scope* item 1 and *Out of scope*, "a shape outside it gets a limit
sentence and no guard".

**Decision: a payload whose `body` is not text is named as not read.**
The design names a missing field and `null`. A `body` of another JSON type
is not GitHub's shape, so the arm names it as not read with its type and
decides nothing. Judged against `skills/core/SKILL.md` *The rule a
mechanism is kept against*, "It names as not read a line or a file that
looks like one of its form's and is not one, and decides nothing on it".

**Decision: `seal_mark`'s sentence is a notice on the work item's
directory.** Where the row reads other than `yes`, or the seal cannot be
read against HEAD, the composition holds no mark and `seal pr-body` says
why on one line. The arm prints that sentence as a notice, so a refusal at
the mark's line comes with the reason the composition holds none.

**Departure: `ruff.toml` gains two rows that the frame did not name.**
`chain_check.py` runs before any floor is checked, and its arm loads
`pr_body.py`, which loads `.github/scripts/close_issues_on_release.py`.
`tests/behaviour/test_every_entry_point_runs_at_the_floor.py#test_what_runs_before_any_floor_is_linted_at_the_floor`
derives that set and failed on both files until they were added at `py39`
(executed). Both lint clean at 3.9 (executed: `uvx ruff check
--target-version py39`). Committed as `f950b269`.

**Departure: two `Test_main` cases read the `not read` lines with the body
arm's line left out.** The `ready` and `draft` payloads hold no body, so
the arm names the body as not read on every run of those fixtures.
`test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit` and
`test_names_no_line_inside_a_fence` asserted the whole list of `not read`
lines. They now read it through `unread_lines`, which leaves out the body
arm's lines and keeps every other line. Their subject is the round record's
fences, so what they assert of the record is unchanged.

**A run with no body prints one notice.** A run outside CI, `seal gate`'s
run under `--sealing` among them, prints `not read: the pull request's
body, since there is no pull-request event payload`. The design asks for
it (*Scope* item 1, S5). It changes no exit code.

**Seen red.** Ten of the eleven new cases were run against `95399efc`'s
parent, the tree with no arm, and failed (executed). Each failed on its own
assertion: the exit code where a refusal is owed, and the list of body
lines where a notice is owed. The two-work-item case also first failed on
its own expected order, which was wrong; the arm prints in the
declarations' sorted order, and the case was corrected. S2, the equal
body, passes with no arm, as an accepting case does; it was shown red by a
break that hands `compared` the body with one line appended. The row case,
added after the arm in `c529b990`, was shown red with the arm's call in
`main` removed, and with the notice of `seal_mark`'s sentence removed
(executed, `bin/seal mutate`).

**Mutations, all red** (executed, `bin/seal mutate` against `c529b990`,
each over `Test_body`):

- the arm's call in `main` replaced by no findings;
- `pull_request_body` reading `null` as no body;
- its check that `body` is text removed;
- its sentence for a missing field changed;
- `body` naming nothing where the text is None;
- the choice of the work item replaced by `if True`;
- the notice of `seal_mark`'s sentence removed;
- the body's line dropped from every message;
- `--sealing` reading the arm's findings as problems;
- `--worktree` reading the payload;
- the arm's notices dropped in `main`;
- the work item no longer added to the candidates.

The working tree was clean after every run (executed: `git status
--short`).

**No unit was renamed or moved,** so no census is owed. The phase removed
nothing.

**The phase-boundary run.** One `bin/test` command ran
`tests/skills/test_chain_check.py`, `tests/skills/test_pr_body.py`, the
files that load `chain_check.py` (`tests/lib/test_config.py`,
`tests/skills/test_broad_gate.py`, `tests/skills/test_seal_stamp.py`,
`tests/evals/test_replay_targets.py`, `tests/evals/test_rule_cases.py`),
`tests/text` and `tests/behaviour`. The first run failed the floor case
above alone. After `f950b269` the same command exited 0, with 2879 passed
and 9 skipped (executed). `tests/behaviour/test_this_repository_passes_its_own_checks.py`
is among them, so `seal rules --check` reads the design's check line
`body-is-what-pr-body-composes` against the marker the arm's cases carry.
Phase 3's edits were set aside under a stash entry of their own while this
ran, so the run measured phase 2's tree.
