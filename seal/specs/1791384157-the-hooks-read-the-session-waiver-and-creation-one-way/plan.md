# Implementation Plan: the hooks read the session, the waiver and a creation one way (#868, #856)

<!-- seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-08 by the repository owner, when `smith` was spawned.
Approved 2026-10-08 by the orchestrating session under the owner's `automation` answer, for the redesign after round 3, when `smith` was spawned; `questions.md` P1 is built on its default (yes).
Approved 2026-10-12 by the orchestrating session under the owner's `automation` answer and the owner's reframe decision, for the redesign after round 5, when `smith` was spawned; `questions.md` P2 is built on its default (delete) and is flagged to the owner, since it reverses the owner's confirmed (c) for #856.

<!-- The line above is the record that the gate happened. Fill it in at the
spawn: reading this plan and spawning the builder IS the approval, so nothing
extra is being asked for here — only that the approval stop living in a
transcript. The second reframe's approval is the line the orchestrating
session adds when it spawns phase 11. -->

## Summary

Four facts every gate depends on are read in more than one place, and the
readings disagree (#868): where a creation lands, which process is the
session, whether a waiver token was typed, and what a failed git call means.
Each gets one reader the hooks import, chosen so the reader refuses what it
does not recognise, and each copy that disagreed leaves the tree. Those four
closed in phases 2, 4 and 5 and held through five review rounds.

#856's brace expansion was answered twice from §A of
`docs/worktree-guard-spec.md` — a word bash expands before git reads it is a
shape the guard does not recognise, so it stops where the tree matters — and
each answer was a reader of bash's expansion rules that the next round found a
hole in. **Reframed a second time on 2026-10-12, by the owner's decision.**
The owner read the run against 0.21.0's theme — every reader is observed,
forces a format, or is deleted — and judged the brace rule a patch on a
prediction, and asked this frame to weigh observing the act through git's
`reference-transaction` hook instead. Weighed and executed (`spec.md` In 5):
the hook sees a switch only after the tree has moved, so it cannot refuse
one, which is #692's M1 and the owner's P4 answer of 2026-10-01. A format that
imitates nothing costs 2,486 of 33,526 recorded pairs. So the reader is
deleted: the brace machinery leaves the tree, the limit is named once beside
#886's four shapes, and `questions.md` P2 offers the owner the format with
its count. Phases 11–12 are that work. Phases 1–10 keep their commits; what 9
built, 11 removes, and the records say so.

`spec.md` In 1–6 is the contract; this file is the order the work arrives in
and why each design was chosen over its alternative.

## Technical context

Coordinates at 5623d728 (`seal/specs/1791382684-…/inventory/1-hooks-shell.md`
and `2-hooks-rest.md` are the inventory's; the line numbers below were read
again by the framer on 2026-10-07).

**Placement (In 1).** `hooks/worktree-guard.py:2998` takes `wheres[0]`;
`judgeable` (wg:596-636) falls back twice; `_tokenize_with_separators`
(wg:232-276) doubles backslashes on Windows. `hooks/worktree_consent.py:419-453`
(`creation_directory`) walks the same `cmdline_base.walk_directories` and
takes the first entry that is not `Unresolved`, with no doubling. The frozen
walk's `wheres` is the failure branch first, then the skipped live shells
(`hooks/cmdline_base.py:1950-2020`), which is why `wheres[0]` is the
directory bash runs a `||` segment in. `tests/test_the_frozen_reading_never_grows.py#test_only_the_two_fallback_arms_read_it`
pins which modules import `cmdline_base`; the one placement function goes
into `worktree_consent.py`, an importer already, so that case is untouched.
The guard already imports `worktree_consent` (wg:188).

**Session (In 2).** `hooks/hooksession.py:40-65` (`claude_ancestor`, basename
test, depth 20), `:81-102` (`call_args`, the same test), `:139-148`
(`session`, `CLAUDE_CODE_SESSION_ID` only). `hooks/session-lease.py:57-85`
(`owner_pid`, substring test, depth 15 — NAME NOT IN TREE since phase 4). `hooks/worktree-guard.py:1213-1229`
(`sessions_in_tree`, basename test over `ps -axo`). `hooks/githooks.py:117-125`
(`_P2`, two variable names). `hooks/tokens.py:117-128` (`steps_around_hooks`,
the same two names). Measured by the framer in a Bash child on 2026-10-07:
`CLAUDE_PID` is exported and equals the `claude` ancestor's pid; the `claude`
process's own environment could not be read with `ps -E`, so whether a hook
process sees the variable is `questions.md` M1.

**Waiver (In 3).** `hooks/tokens.py:44-88` (`words`, `without_bodies`,
`_bare`, `given`); `hooks/commit-review-gate.py:657-697` (`has_marker`,
`_reads_marker` with the substring fallback at :695), callers at :1122 and
:1418; `hooks/worktree-guard.py:381-440` (`has_token`), `:442-459`
(`_without_bodies`, the frozen fallback), callers at :1974 and :3119;
`hooks/answer-write.py:29` reads `tokens.given`. The substring fallback's
own argument (crg:663-665) was made when the PreToolUse reading was the only
gate; since #692 the refusal names `git -c specseal.waive=review`
(`docs/the-commit-gate-inside-git.md` §*The arms*), and `hooks/tokens.py`'s
docstring already records the choice to refuse (*an unbalanced quote reads
nothing*).

**Failed git (In 4).** `hooks/gate.py:65-79` (`git`, `""` on failure),
`:93-95` (`touches_code`), `:98-131` (`arms_missing`, `paths()` asked only
for the parity arm); `hooks/commit-review-gate.py:571-583` (`git`, the copy),
`:598-636` (`changed_paths`); `hooks/commitgate.py:71` (`config --get-all`),
`:224-229` (`pre_commit`), `:241` (`symbolic-ref -q`), `:258-266`
(`_paths_between`). A hook that raises is a non-zero exit with a traceback,
and a PreToolUse gate that raises reaches `hooks/dispatch.py:134-170` as a
pending failure record and the call goes ahead, so the failure has to be an
answer the caller handles, not an exception.

**Brace (In 5), as first framed and as reframed after round 3.** The
coordinates the first two frames read are in the round records and in
`phases/phase-3.md`, `phase-7.md` and `phase-9.md`; the units they name are
NAME NOT IN TREE once phase 11 closes, and this plan reads the tree as the
second reframe found it instead.

**Brace, as the tree stands at 52c72bbe (the second reframe's coordinates,
read by the framer on 2026-10-12).** Fenced, because most of the names below
leave the tree in phase 11:

```
hooks/worktree-guard.py
  :2003-2045  _BRACE, the comment above it, _unquoted_brace (the text test
              with quoted spans and escapes as spaces and the ${ exception,
              round 5's reading)
  :2194-2234  _git_finding: the `braced` parameter, the brace arm at :2211
              after the creation and switch checks
  :2286-2320  _segment_finding (brace arm at :2301), shape_of
  :2323-2399  _merged_findings, `braced` threaded through
  :2401-2431  _command_findings, the brace half of the untokenizable arm :2429
  :2434-2460  _first_finding_in: `braced` read at :2446, the command-level
              brace finding at :2456
  :2463-2487  _finding_tree — stays
  :2490-2518  _finding_trees, the -C union for brace segments — leaves
  _described's `brace` branch, both languages
  :3013-3053  main: `braced` read once at :3016, threaded into
              _segment_finding and _merged_findings; the command-level brace
              finding at :3050
tests/test_worktree_guard.py
  :1870-2290  the brace cases; BRACE_SHAPES, BRACE_EN, BRACE_KO
  :2396-2510  BRACED and test_no_listed_form_moves_head_under_git — the bash
              half stays, the guard half inverts (S26)
tests/test_guard_resolves_the_tree_it_judges.py
  :828-900    the two brace policy pins
docs/worktree-guard-spec.md
  :63-140     §A's four brace paragraphs
  :190-202    "The failure direction" with the brace sentence, and the
              Enforced by: line naming thirteen brace cases
  :917-921    the hidden-spelling bullet — its {add,} example stays
  :932-940    the sh -c bullet with the brace-hidden -C sentence
changelog.md   the brace bullet, "A command holding an unquoted brace …"
the ledger fragment   rows S11–S13a, S15b, S17–S22, S24, S24a, S20a
```

**The hook direction, executed by the framer on 2026-10-12.** git 2.50.1
(Apple Git-155), a scratch repository driven from Python, a
`reference-transaction` hook logging its state, stdin and the working tree,
refusing at `prepared`. The table is `spec.md` In 5's. What it settles: a
switch, a detached switch and a branch-naming rebase hand the hook their
`HEAD` or branch line after the index and working tree hold the new branch,
and a refusal leaves `HEAD` on the old branch with the new branch staged
(`git status`: `A b.txt`, `M marker.txt`); a conflicting local edit makes
git refuse the switch itself before any hook; a branch creation (`switch
-c`, `stash branch`) and a worktree creation, with `-b` or onto an existing
branch, are refused cleanly before anything is written. `commitgate.pressed`
and `hooksession.session` already give a hook the press and the session, so
the four costs the owner named are not what decides it; M1 is.

**The character format's count, executed by the framer on 2026-10-12.** Phase
1's method, tree-blind: every Bash `tool_use` in every `*.jsonl` under
`~/.claude/projects/*SpecSeal*/`, recursive, distinct (command, cwd) pairs:
33,526. Holding a `{` or `}` anywhere: 3,990. Outside heredoc bodies, taken
out by `cmdline_base.drop_heredoc_bodies`: 2,486, of which 561 hold only
`${…}` parameter expansions and 1,926 something else, 570 of those beside the
word `git`. The probe was deleted (§7); the figures are the framer's,
`executed`, and S29's records may carry them with this paragraph as the
method.

**The failure scenario of the chosen approach.** In six months a session
types `git rebase {main,feature/x}` in a tree another session is working in,
and the guard says nothing, as it said nothing at 0.20.0. The limit is
named in §*Known limits* with the four forms and the pointer to #886, and
`test_no_listed_form_moves_head_under_git` keeps running the four through
bash, so the day the limit is closed — in #886, by the owner, for the whole
class — the case is the one that has to change. What cannot happen is the
round-1-to-5 class: no reader of bash's expansion rules is left in the guard
for a round to find a hole in. The other failure is the one #835's registry
exists for: a fifth hook writes its own walk beside the one reader, and the
registry row for each reader this work added names its input class (the
table below).

**Input class of every reader this work adds, changes or removes**, in
#834's words:

| Reader | Reads | Class | Unknown |
|---|---|---|---|
| the one placement function (`worktree_consent.place`) | the frozen walk's `wheres` and the segment's `-C` | guess | refused to the session's own tree |
| `hooksession.is_claude`, `claude_ancestor` | `ps -o ppid=,comm=` | guess | passed (no `claude` is no session, a person's own commit) |
| `hooksession.claude_pid` | env `CLAUDE_PID`, else the walk | observed, then guess | as above |
| `githooks._P2`, `tokens.steps_around_hooks` | the one session variable name | owned | — |
| `tokens.given` (now the only token reader) | bare words of the command and of `without_bodies` | guess | refused (no split, no token) |
| `gate.git` (now the only runner) | git's exit code and stdout | observed | refused (`None`, and the parity arm asks) |
| the brace reader, rounds 1–5 (`_unquoted_brace`, `_BRACE`, the arms, `_finding_trees`) — NAME NOT IN TREE once phase 11 closes | the command's text with quoted spans as spaces, every segment's words | guess, an imitation of bash's expansion rules | **deleted** by the second reframe: the fate #834 gives a reader that neither observes nor forces a format |

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| #856 (a): expand braces in the guard, so `{main,feature/x}` becomes two words before the shape is read | a shell-prediction rule in the one family that did not converge after its redesign (#834 part 8: 6 issues, 4 reopenings, two filed after #850). The next spelling reopens it, and each expansion the guard performs is one more place its words are not the frozen reading's | rejected |
| #856 (c), first frame: a word holding an unquoted brace expansion in a git segment is unrecognised | round 1 found `{git,} rebase …`, a segment the frozen reading reads as no git | rejected by round 1; phase 3's commit stands |
| #856 (c), first reframe: a brace in any word of any segment, no position read | rounds 4 and 5 found the quoting read incomplete (`\${a,b}`, `$''{g..g}it`, `{git,$(: x)}`), each fix widened the text test, and the owner judged the result a patch on a prediction (handoff of #834, §*Review of the run*) | rejected by the owner on 2026-10-12; phases 7–10's commits stand |
| Keep round 5's rule as it stands (42 of 33,287) and run round 6 | the rule still imitates bash's quoting, escapes and `${`; six rounds found a hole each time, and nothing says the seventh would not. The owner's judgment names it a cover-up | rejected |
| **Observe the act**: `reference-transaction` at `prepared` refuses a `HEAD` move in a tree another session is in, however the command was spelled (the owner's direction) | executed on 2.50.1 (`spec.md` In 5): the `HEAD` line arrives after the index and working tree hold the new branch, so the refusal leaves `HEAD` on `main` and the tree on `other` — a broken tree in the very tree the Premise protects, worse than the switch; on 2.34–2.43 no line arrives at all (#692's M1, pinned on four gits). A foreign hooks slot would keep the text guard beside it, two readers of one act. A hook cannot ask, so §A's two choice rows and the tracked-changes row would be denies with text. The session and the press ARE readable from a hook (`hooksession.session`, `commitgate.pressed`), so context is not what fails; git's order of operations is | rejected, on executed evidence |
| Observe and report: let the switch through and write a notice for the model to switch back | P4 (c) of #692, declined by the owner on 2026-10-01; protects nothing, and the window it leaves is in another session's tree | rejected |
| A `git` shell function or `PATH` shim in the Bash tool's shell, observing git's argv after every expansion | not an input this plugin owns (the harness's shell environment), and stepped around by `/usr/bin/git`, `command git`, `exec git`, `env git`, a `PATH=` assignment — a list again, the class the memory of #692 refuses; no measurement exists | rejected |
| **Force a format**: a `{` or `}` anywhere in the judgment text, heredoc bodies out, is the brace shape where the tree matters; no quoting, escape or `${` read | converges (no brace expansion lacks the character) and costs 2,486 of 33,526 recorded pairs tree-blind, 7.4%, sixty times round 5's rule and seven times the whole #826 stop; `awk '{…}'`, `jq`, `{ …; }` groups and `${VAR}` each stop in every dirty tree, a deny the model rewrites under the press and an `ask` otherwise. §*Unknowns resolve conservatively* calls a deny that fires like that an outage. Exempting a bare `${` misses `\${a,b}` (round 4, executed) | **the owner's alternative**, `questions.md` P2; not the default |
| **Delete**: the brace machinery leaves, the limit is named once beside #886's four shell-built-word shapes, `test_no_listed_form_moves_head_under_git` pins the limit as a fact | `git rebase {main,feature/x}` and three forms are silent in an ACTIVE tree, as at 0.20.0; none was ever recorded in 33,287 pairs, and the Premise's protection against a shell-built word is already incomplete by #886's four. The class is decided once, by the owner, in #886 | **chosen** |
| A creation arm inside git: `reference-transaction` refuses a worktree creation at `prepared`, which the executed table shows 2.50.1 doing cleanly before any checkout, for `-b` and for an existing branch | a creation is a consent question a hook cannot put; P6 (a) of #692 is the owner's answer; `-B`, `--no-checkout`, `--orphan`, `--lock` and git below 2.46 are unmeasured; and In 1's placement held through every round. Reopening the arm is another work item | not reopened; the fact goes to the owner as `questions.md` P3 |
| In 1: unify placement on the writer's rule (first resolved entry) | wrong for `cd X \|\| …`, where the resolved entry is the branch bash skipped, and for `cd <missing> ; …`, where it names a directory that holds nothing; measured by the framer's probe | rejected |
| In 1: unify on the guard's rule, in `worktree_consent.py` | the guard's answer is the base's on the three pinned chains (probe) and bash's on the two that disagreed; no new importer of `cmdline_base` | **chosen** |
| In 1: a new module `hooks/placement.py` | a new file, and a new importer of the frozen reader that `test_only_the_two_fallback_arms_read_it` would have to learn | rejected |
| In 2: align the predicate only, keep three walks | three readers of one fact, each guessing; the registry would list three rows for one question | rejected |
| In 2: one reader, `CLAUDE_PID` first, the walk under it | an observed value where the harness exports it; where it does not, today's walk; §13 is why the walk stays | **chosen** |
| In 2: keep `$CLAUDECODE` in the stub and in `steps_around_hooks` | not wrong, but two names for one fact in two places, and the second exists only because of the first. With it gone the verdict is unchanged in every state | rejected |
| In 3: keep `has_marker`'s substring fallback | a waiver read where the command did not split, which is reading loosely in the one direction that waives with nobody asked | rejected |
| In 3: three readers through one `tokens.given` | one splitter, one body rule, one parenthesis rule; the only behaviour change is on a command that does not split, where the refusal already names the way on | **chosen** |
| In 4: `gate.git` raises on failure | in a git hook, a traceback and a refused commit with no reason text; in a PreToolUse gate, a pending failure record and the call goes ahead (`dispatch.py:161-170`), which is silence | rejected |
| In 4: `gate.git` answers `None` on failure, `""` on an empty answer, and the parity path reader turns `None` into *asks* | each caller says at its own line which exit is an ordinary *no*; the parity arm asks where it was silent; nothing else changes | **chosen** |

## Phases

Vertical slices — each phase ends with something runnable and verified.
Every new case is seen red first (§15) — at 5623d728 for phases 1–6, at
a8f86f44 for 7–10, at 52c72bbe for 11 — and each phase record says how. No
phase runs the broad gate; the sealer does (§2).

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **Measure before building; nothing in the tree but the record.** A deleted `test_tmp_*` probe by the method of 1791270162's phase 1 over the recorded corpus, tree-blind: M2, M3 and the self-check. `phases/phase-1.md` with the tables, user paths rewritten to `/Users/x/`; the probe, its result files and every scratch directory gone (§7) | the record's tables; the self-check line; `ls` of the scratchpad showing no `test_tmp_*` of this phase | 84535260 |
| 2 | **One placement (In 1).** The adapter and the placement function in `hooks/worktree_consent.py`; `creation_directory`, the guard's `judgeable` and `_tokenize_with_separators` through them; S1–S3 planted red at 5623d728 first; the `Creation consent` sentence of `docs/worktree-guard-spec.md` with its pin | `uv run --frozen pytest -q -p no:cacheprovider tests/test_guard_resolves_the_tree_it_judges.py tests/test_the_guard_asks_once_per_session.py tests/test_the_frozen_reading_never_grows.py`, exit code read directly (§1); the red run of each new case in `phases/phase-2.md` | e1cca725 |
| 3 | **The brace shape (In 5, first frame).** `_git_finding`'s `brace` arm; `_described`'s text; S11–S13 red first; `_rebase_names_a_branch`'s docstring; §A's brace sentence and costs. Superseded by phase 9, then removed by phase 11; the docstring (S14) stands | the modules the phase named; the git-binding case executed under bash | b5ceec40 |
| 4 | **One session reader (In 2).** `hooksession.is_claude`, `claude_pid`, `SESSION_VARIABLE`; `session-lease.py#owner_pid` and `sessions_in_tree` through them; `_P2` formatted from the one name; `steps_around_hooks` reading it; S4–S6 red first; `docs/the-commit-gate-inside-git.md` pinned — `owner_pid` is NAME NOT IN TREE since this phase removed it | `uv run --frozen pytest -q -p no:cacheprovider tests/test_lease_liveness.py tests/test_the_commit_gate_decides_at_the_commit.py tests/test_the_hooks_are_installed_where_git_runs_them.py tests/test_worktree_guard.py`; `test_s9_*` green; the stub text asserted free of `CLAUDECODE` | 8f056802 |
| 5 | **One waiver reader and one runner (In 3, In 4).** `tokens.without_bodies` with the frozen fallback; `has_marker` and `has_token` through `tokens.given`; `gate.git` answering `None`, `crg.git` gone, each caller's ordinary-*no* line explicit, `touches_code(None)` True; S7–S10 red first; the three policy documents pinned | `uv run --frozen pytest -q -p no:cacheprovider tests/test_the_old_spellings_reach_the_hook.py tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py tests/test_gate_judges_the_repo_it_commits_to.py tests/test_chain_hooks_hardening.py tests/test_the_commit_gate_decides_at_the_commit.py tests/test_guard_resolves_the_tree_it_judges.py tests/test_a_gate_that_fails_says_so.py`; `uvx ruff check hooks/` for the dead imports | 077c0bc6 |
| 6 | **The fragments and the closures.** The ledger fragment with a row per scenario and the `Re-read ·`/`Corrected ·` rows; `changelog.md`; `overview.md`; `plan.md`'s Status column closed | `bin/evidence-check . --strict`, `bin/correction-check`, and the five text-hygiene modules, exit codes read directly | efb73268 |
| 7 | **Measure the reframed rule before building it (first reframe; S22).** A deleted probe by phase 1's method; M4, M5; `phases/phase-7.md`. Its figure, corrected in rounds 4 and 5 to 42 of 33,287, is history since the second reframe | the record's tables; the self-check line | 452cf167 |
| 8 | **The lease case that can fail (round 3's ⬜ 4; S23).** `test_a_pid_beside_no_session_id_on_either_side_is_not_recorded` over both absences on both sides; seen red with `hooks/session-lease.py` at e0c5a191 in a scratch clone | `uv run --frozen pytest -q -p no:cacheprovider tests/test_lease_liveness.py`; the red run in `phases/phase-8.md` | 27793ce1 |
| 9 | **A brace in any word of any segment is the brace shape (first reframe; S17–S21, S24).** `_segment_finding`'s brace arm, `_finding_trees`, the command-word units removed, §A rewritten. Removed by phase 11, after which `_finding_trees` is NAME NOT IN TREE | the modules the phase named; `bin/mutation-check`; the git-binding case under bash | 6e5e02bf |
| 10 | **The fragments and the closures, again.** Ledger rows for S17–S24; `overview.md`; `changelog.md`; `plan.md`'s Status column for 7–10 | `bin/evidence-check . --strict`, `bin/correction-check`, and the five text-hygiene modules | bee729a8 |
| 11 | **The brace reader leaves the tree, and the limit is named (second reframe; S25–S28, In 6).** Every unit `spec.md` In 6 lists for this phase removed from `hooks/worktree-guard.py`, `_finding_tree` restored as the one tree lookup `main` calls, `_described` without a `brace` kind, no `braced` parameter anywhere; the thirteen brace cases and the three constants removed from `tests/test_worktree_guard.py`, the two brace policy pins removed from `tests/test_guard_resolves_the_tree_it_judges.py`; `test_no_listed_form_moves_head_under_git`'s `BRACED` half inverted to assert the guard reads each of the four as listed while bash moves HEAD or adds the worktree, and `test_a_shell_built_word_is_the_named_limit` over the eight S26 forms in an ACTIVE tree, both red at 52c72bbe first (the guard stops the four there), shown in `phases/phase-11.md`; `docs/worktree-guard-spec.md` §A's four brace paragraphs and the brace sentence of *The failure direction* gone, §*Known limits*' first bullet gaining the one sentence S27 states with the four forms and the pointer to #886, the `sh -c` bullet's brace-hidden `-C` sentence gone, every `Enforced by:` entry naming a removed case gone, `test_the_guard_policy_names_the_shell_built_word_limit` pinning the sentence and red at 52c72bbe; `docs/the-commit-gate-inside-git.md` §*The convergence argument is claimed for commits alone* gaining the rebase sentence with its pin, and `test_no_git_refuses_a_switch_before_the_tree_moves` gaining the `rebase main other` parameter (S28); the changelog fragment's brace bullet rewritten to say the reader was built and taken out inside this release and what the limit is; `phases/phase-11.md` with the removal table, W5's answer, and the red runs; the two new case names are NAME NOT IN TREE until this phase plants them | `bin/test tests/test_worktree_guard.py tests/test_guard_resolves_the_tree_it_judges.py tests/test_the_guard_asks_once_per_session.py tests/test_the_hook_surface_git_offers.py tests/test_the_commit_gate_decides_at_the_commit.py`, exit codes read directly (§1); `uvx ruff check hooks/ tests/`; the git-binding case and S28's parameter executed under bash and git; `grep -n 'brace\|_BRACE\|braced' hooks/worktree-guard.py` showing only the limit's comment | 63a518a8 |
| 12 | **The records say what the tree has (S29).** Ledger rows S11, S11a–S11e, S12, S13, S13a, S15b, S17–S22, S24, S24a and S20a retired or rewritten against S25–S28 in the unreleased fragment, S14 and S15 re-hashed, rows for S25–S28 added, the `Re-read ·` rows for every released row phase 11's edits drift (`evidence-check --reverify --into`); `overview.md`'s divergence rows for phase 11, its Not done naming #856 closed as a limit and the brace handed to #886 by the orchestrating session's comment, its Not verified table as before; `questions.md` P1 withdrawn, P2 and P3 standing, W5 answered; `plan.md`'s Status column for 11–12; `survivors.md` re-read for the places the removal leaves | `bin/evidence-check . --strict`, `bin/correction-check`, `survivor-check --range origin/release/v0.21.0...HEAD`, and the eight suite-wide guard modules, exit codes read directly | 8e231b70 |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it: where feature branches squash, these
commits stop resolving at the merge, and a rebase during the work does the
same thing earlier and more quietly. Re-read the column after any rebase.

## Seams with the 0.21.0 siblings

None of the brief's siblings names a unit this plan changes
(`hooks/worktree-guard.py`, `worktree_consent.py`, `hooksession.py`,
`session-lease.py`, `githooks.py`, `tokens.py`, `gate.py`,
`commit-review-gate.py`, `commitgate.py`, and the policy documents of S15
and S27). #835's registry reads #834's table, and the input-class table in
*Technical context* is what that frame reads, its last row saying the brace
reader was deleted. #867 reads `seal/config.md` and the coordinate grammar,
which the fragment uses as every fragment does. Before any seal, the release
branch is merged in: it has moved since this branch last merged it
(`handoff.md`).

## Operational impact

- The stub's bytes change (one variable name), so `hooks/hook-install.py`
  rewrites every opted-in clone's three stubs at the next session or Bash
  call, silently, as it does for a plugin move.
- `CLAUDECODE= git commit -m x` and `env -u CLAUDECODE git commit -m x` are
  judged by the reading as before (`overview.md`'s divergence row);
  `CLAUDE_CODE_SESSION_ID=` forms are judged by the reading as today.
- A command that does not split and carries `[no-review]` or `[no-parity]`
  as a substring meets the refusal; the way on is the waiver typed in
  front, which the refusal names.
- In a repository declaring `seal/parity.md`, a commit whose `git diff`
  fails meets the parity question where it met silence.
- Since the second reframe, the guard's stop has no `brace` kind. A command
  holding a brace expansion is read as its frozen words, as at 0.20.0:
  `cat {a,b}`, `ls x/{a,b}.md`, `A={a,b} ls`, `echo {a, b}` and `git diff
  HEAD@{1}..HEAD@{0}` are silent in every tree, and `git rebase
  {main,feature/x}`, `git rebase --ro{,} feature/x`, `git stash {branch,} x`
  and `git worktree {add,} ../wt f` are silent too, which is the named limit.
  Nothing a person met at 0.20.0 changes; what the rounds added inside this
  release is taken back before it ships.
- A lease may record a pid for a session whose process is not named
  `claude`, where the harness exports `CLAUDE_PID` to its hooks (M1).
- No migration, no new dependency, no new environment variable the plugin
  sets.
