# Feature Specification: the hooks read the session, the waiver and a creation one way (#868, #856)

<!-- seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate.
Issues #868 and #856, for release 0.21.0. Coordinates are at 5623d728
(0.20.0 as shipped) unless a commit is named. Reframed after round 3 (the
brace rule widened) and again on 2026-10-12 after round 5, by the owner's
decision: the brace machinery leaves the tree. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Between two readers that catch the same defect, the one that stops to ask is the more expensive. Every design here is weighed for a run that verifies unattended |
| #834 §*What the table says* (`seal/specs/1791382684-…/spec.md`, read with `git show`), and its `handoff.md` §*Review of the run* and §*What the owner decided* (branch `chore/834-every-reader-and-record-is-inventoried`, read with `git show`) | What converged read an owned format or an observed fact and refused the unknown; what reopened guessed from text it does not control. The owner's judgment of 2026-10-12: every reader is observed, forces a format, or is deleted, and the brace rule, after six rounds, still imitates bash. This work names the fate of every reader it touched |
| `docs/worktree-guard-spec.md` §*A. Branch switch*, *The stop for an unrecognised shape* | The question §A asks is *is this command known to leave the branch where it is?*, read off the frozen reading's words. A word the shell builds before git runs is not among those words, and since the second reframe the guard says so as a limit rather than guessing where one stands |
| `docs/worktree-guard-spec.md` §*Which tree, when the command walks to it* | The guard and the consent writer read every command through `hooks/cmdline_base.py`, frozen; §A reads the command's text on every git, permanently, because no git refuses a switch before its tree has moved (#692's M1). The second reframe re-measured that and it holds |
| `docs/the-commit-gate-inside-git.md` §*The convergence argument is claimed for commits alone* | On 2.34–2.43 a switch reaches `reference-transaction` with no line; on 2.50.1 the `HEAD` line arrives after the index and working tree hold the new branch, so a refusal there is a broken tree, not a prevented switch. Pinned by `tests/test_the_hook_surface_git_offers.py::test_no_git_refuses_a_switch_before_the_tree_moves`, executed by this frame on 2026-10-12 (In 5). This is the clause that decides the owner's direction |
| `docs/worktree-guard-spec.md` §*Known limits*, the first bullet, the hidden-spelling bullet and the fallback bullet | Neither a switch nor a creation is judged by git; a creation only a hidden spelling holds is silent in a clean single-stream tree; a tree the guard cannot place falls back to the session's own. In 5 adds the brace to the shapes these bullets already let through, as one sentence naming the class, beside #886's four |
| `docs/worktree-guard-spec.md` §*Unknowns resolve conservatively* | A wrong deny costs one prompt; a wrong allow breaks another session's tree; and a deny that fires on every command in an environment is an outage. The second reframe prices the format rule by this paragraph (In 5, the count) |
| `docs/worktree-guard-spec.md` §*Creation consent*, *The record* | The record stands for *this session may split this clone into worktrees*, under the common git directory of the clone the creation acted on. In 1 makes the clone the writer files under the one the guard judged, by one rule |
| `docs/the-commit-gate-inside-git.md` §*A commit with no Claude session behind it is a person's own* | The session is `CLAUDE_CODE_SESSION_ID`, else the lease whose recorded pid is the hook's nearest ancestor named `claude`. The writer of that pid and its reader must find the same process (In 2) |
| `docs/the-commit-gate-inside-git.md` §*The arms, the marks and the declaration*, and §*Known limits*, *The old spelling waives only where the hook can find the call's shell* | The old bare word is read out of the Bash call by `hooks/answer-write.py` through `hooks/tokens.py#given`; the match through `ps` is a named limit and stays (Out) |
| `docs/commit-review-gate-spec.md`, the consent-read paragraph under §*commit-review-gate (PreToolUse, Bash)* | A token counts only where the command as written carries it, so a consent read can refuse a waiver and never grant one. In 3 removes the one read that grants where the command does not split |
| `docs/the-review-and-parity-arms.md` §*Parity arm* | *The change* is every path the commit would carry. A diff git could not take carries no paths and is not a change confined to `docs/` and `seal/`; In 4 makes the arm ask there |
| `skills/agent-contract/SKILL.md` §13 | A defence resting on a platform guarantee is verified with it removed. `CLAUDE_PID` (In 2) is one, so the `ps` walk stays as the route under it |
| `skills/agent-contract/SKILL.md` §15 | Every case In 1–4 added was seen red at 5623d728 before it was planted. The second reframe plants one new case and rewrites one, and each is seen red at 52c72bbe, the commit the reframe starts from, before it is committed |
| `skills/code-review/SKILL.md` §*Verdicts that close too early* | An enumeration over an unbounded domain is a recorded limit, not a closed finding. Rounds 1–5 of this run enumerated what bash makes of a brace five times, and each round found the next shape. The second reframe records the limit (In 5) |
| `skills/code-review/orchestration.md` §*A fix of a fix twice sends the work item back to its framer* | Why this file carries two `Reframed` lines and `plan.md` new phase rows with every closed phase keeping its commit. The second reframe is the owner's decision of 2026-10-12, not a fix-of-a-fix count |

## Scope

### In

Six items. Four are #868's disagreements, closed in phases 2, 4 and 5 and
held through every round; the fifth is #856, reframed twice; the sixth is
the list of what leaves the tree, which #834's direction asks every 0.21.0
frame to name.

1. **A creation is placed by one rule, and the rule is the guard's.**
   `hooks/worktree-guard.py#main` places a segment at `wheres[0]` and
   `judgeable` falls back to the session's own directory where that entry is
   `Unresolved` or holds no repository (wg:598-636, 2998). `hooks/worktree_consent.py#creation_directory`
   takes the first entry that is not `Unresolved` (wc:448-451). Executed by
   this frame, through `hooks/cmdline_base.py`'s walk (a deleted probe,
   2026-10-07): the two agree on the three `BASE_TREE_CHAINS` of
   `tests/test_guard_resolves_the_tree_it_judges.py`, and disagree on the
   inventory's shape and on one more:

   | Command, from `S` | `wheres` | guard | writer |
   |---|---|---|---|
   | `eval x ; cd /tmp/a \|\| git worktree add ../wt f` (part 1 row 127) | `(Unresolved(S), /tmp/a)` | `S` | `/tmp/a` |
   | `cd <missing> ; git worktree add ../wt f` | `(<missing>, S)` | `S` | `<missing>`, so no record at all |

   bash runs the `\|\|` segment only where the `cd` failed, in the directory
   the shell was already in, and `/tmp/a` is the branch it skipped; and
   `;` runs its segment in the session's directory when the `cd` fails. The
   guard's answer is where bash runs the command in both, so the writer
   takes it. One function places a segment — `wheres[0]`, the `Unresolved`
   and no-repository fallbacks, the segment's own `-C` composed — and both
   `main` and `creation_directory` call it; the Windows backslash doubling
   the guard's `_tokenize_with_separators` does and the writer does not
   (part 1 row 90) goes through the same one adapter. The function lives in
   `hooks/worktree_consent.py`, which the guard already imports and which
   already reads through `cmdline_base`, so
   `tests/test_the_frozen_reading_never_grows.py#test_only_the_two_fallback_arms_read_it`
   keeps its list of importers. Input class: guess (the frozen walk's
   directories), unknown refused to the session's own directory, as
   §*Known limits* already says of a switch. Closed in phase 2 (e1cca725).

2. **The session's process is found by one reader, and it reads an observed
   value first.** `hooks/hooksession.py` owns it:
   - `is_claude(comm)`: `os.path.basename(comm) == "claude"`, the test
     `hooksession.claude_ancestor` (hs:59), `call_args` (hs:95) and the
     guard's `sessions_in_tree` (wg:1228) already use. `hooks/session-lease.py#owner_pid`'s — NAME NOT IN TREE since phase 4 removed it
     `"claude" in comm` at depth 15 (sl:78) goes: the lease it writes is read
     back by `claude_ancestor` at depth 20 with the stricter test, and a pid
     only the looser test finds is a lease no reader matches, which
     `from_lease` answers with no session and the commit is not judged
     (hs:136, 148). Read, not run: no process named that way was built.
   - `claude_pid(environ=None)`: `CLAUDE_PID`
     where the environment carries it, else `claude_ancestor()`. Measured by this frame on 2026-10-07 in a
     Bash child of this harness: `CLAUDE_PID` is exported beside
     `CLAUDE_CODE_SESSION_ID`, and it equals the pid `ps -o ppid=,comm=`
     names as the `claude` ancestor of the shell (10196 on both sides, read
     off the process table). Whether a hook process the harness spawns sees
     it is `questions.md` M1; the `ps` walk stays either way (§13).
     `session-lease.py#main` records `claude_pid()`;
     `hooksession.session`'s lease route asks `from_lease(common, claude_pid(environ))`.
   - `SESSION_VARIABLE = "CLAUDE_CODE_SESSION_ID"`, the one name. `hooks/githooks.py#_P2`
     is formatted from it, and `$CLAUDECODE` leaves the stub: `hooksession.session`
     never reads it (hs:142), so a stub that starts Python on it alone
     starts an interpreter that answers no session unless a lease stands, and
     a lease starts it anyway. `hooks/tokens.py#steps_around_hooks` compares
     the one name (tk:127); the word `CLAUDECODE` leaves its list, because
     unsetting a variable the stub no longer reads leaves the stub its
     session. The verdict is the same in every state (plan.md Alternatives).
   `commitgate._process` is the `git commit` process, not the session's, and
   is untouched. `worktree-guard.py#host_app` labels the host application
   for the stop's text and is display only; its substring labels stay.
   Closed in phase 4 (8f056802).

3. **The waiver token has one reader, and it refuses what does not split.**
   `hooks/tokens.py#given` is the reader (tk:83): bare words through `shlex`
   with the punctuation characters, parentheses stripped, comments kept,
   read in the command as written AND in `without_bodies`, nothing where the
   command does not split. `hooks/commit-review-gate.py#has_marker`
   (crg:657) and `hooks/worktree-guard.py#has_token` (wg:381) become
   `token in tokens.given(command)`; `crg#_reads_marker` with its substring
   fallback (crg:691-697) and the guard's `carries` closure and
   `_without_bodies` (wg:442) go. `tokens.without_bodies` takes the fallback
   the guard's `_without_bodies` carried: where `hooks/cmdline.py` fails to
   load or the read raises, the frozen reader's `drop_heredoc_bodies` finds
   the bodies, so a broken reader leaves the single-stream creation deny a
   way past (released row T1 of `seal/releases/0.18.3.md`). What changes for
   a person: a command that does not split and carries `[no-review]` or
   `[no-parity]` as a substring waived its arm in the PreToolUse reading
   (crg:695) and now does not; the refusal names
   `git -c specseal.waive=review`, the spelling the hook reads with no text
   read at all. `hooks/answers.py#given` is untouched (Out). Closed in phase
   5 (077c0bc6); `overview.md`'s divergence rows say where the build landed.

4. **A failed git call is a failure the caller sees, and the parity arm asks
   on it.** `hooks/gate.py#git` is the one runner; `hooks/commit-review-gate.py#git`
   (crg:571) goes. The runner answers `None` on a non-zero exit, an
   `OSError` or a timeout, and `""` for an empty answer. Every caller that
   reads a non-zero exit as an ordinary *no* keeps that reading at its own
   line, explicitly (`rev-parse --verify --quiet HEAD` on an unborn branch,
   `config --get-all specseal.waive` with no key, `symbolic-ref -q HEAD`
   when detached, `rev-parse --git-dir` outside a repository). The path
   readers — `commitgate.pre_commit`'s `diff --cached --name-only` (cg:229),
   `_paths_between` (cg:266), `crg.changed_paths` (crg:616) — hand
   `arms_missing` `None` where git failed, and `gate.touches_code(None)` is
   True: a change git could not list is not a change confined to the
   document roots, and the parity arm asks. Read, not run, as #868 says of
   it; S10 runs it. The mark readers already refuse on `""` and are
   unchanged. Closed in phase 5 (077c0bc6).

5. **#856: a brace expansion is a word the shell builds, and the guard does
   not read it. The limit is named, and the reader that guessed at it
   leaves.** This is the second reframe's one decision, and it reverses In
   5 as the first reframe wrote it. The grounds, in the order they were
   weighed:

   **What the owner asked to weigh: observe the act.** git's
   `reference-transaction` hook, which this plugin already installs
   (`hooks/githooks.py#HOOKS`), runs for every ref update, `HEAD` included,
   and a non-zero exit at `prepared` aborts the update whatever spelled the
   command. **Executed by this frame on 2026-10-12** in a scratch repository
   driven from Python (agent contract §8), git 2.50.1 (Apple Git-155), a
   hook that logs its state and stdin and reads the working tree, then
   refuses at `prepared`:

   | Command, from `main` with `other` differing in `marker.txt` and `b.txt` | What `prepared` is handed, and what the tree holds at that moment | After the refusal |
   |---|---|---|
   | `git switch other` | one line, `0000… ref:refs/heads/other HEAD`; `marker.txt` already reads `other`, `b.txt` already exists, the index already holds both | exit 128 `fatal: ref updates aborted by hook`; `HEAD` on `main`, the working tree and index on `other`: `git status` shows `A b.txt`, `M marker.txt` |
   | `git switch --detach other` | `0000… <oid> HEAD`, the tree already moved | the same broken state |
   | `git rebase main other` | `0000… <oid> refs/heads/other`, the tree already on `other` | the same broken state |
   | `git switch other` with a conflicting local edit | the hook never runs: git refuses the switch itself before any hook, as it always did | unchanged |
   | `git stash branch x` | `0000… <oid> refs/heads/x` first, the tree not yet moved | refused cleanly: `HEAD` on `main`, the tree unchanged, no branch `x` |
   | `git switch -c newb` | `0000… <oid> refs/heads/newb`, no tree change | refused cleanly |
   | `git worktree add <dir> -b wb` | `0000… <oid> refs/heads/wb` first, from the main worktree | refused cleanly: no `<dir>`, no branch `wb` |
   | `git worktree add <dir> other` | `0000… ref:refs/heads/other HEAD`, the new worktree's `HEAD`, handed with the hook's working directory in the MAIN worktree | refused cleanly: no `<dir>`, `git worktree list` shows the main worktree alone |

   So the hook observes a switch, and a branch-naming rebase, only after
   the index and working tree hold the new branch, and refusing it there
   leaves `HEAD` lying about the tree, which is a worse state than the
   switch. On 2.34–2.43 it observes no switch at all. This is #692's M1,
   pinned by `test_no_git_refuses_a_switch_before_the_tree_moves` on four
   gits in CI, and the reason the owner answered P4 of that work item with
   *the frozen text reading, on every git, permanently* on 2026-10-01. The
   direction cannot refuse the act #856 is about. What it CAN refuse
   cleanly on 2.50.1 — a branch creation and a worktree creation, before
   any checkout — is the creation arm, decided by #692's P6 and not
   reopened here (Out; `questions.md` P3 hands the measured fact to the
   owner).

   **Force a format.** A brace rule that imitates nothing is a character
   test: a `{` or a `}` anywhere in the judgment text, heredoc bodies taken
   out by the frozen reader, makes the command the brace shape where the
   tree matters. Nothing bash expands lacks the character, so there is no
   next spelling to find (`$''{g..g}it`, `{git,$(: x)}` and `\${a,b}` each
   hold one). Counted by this frame on 2026-10-12 over the recorded corpus
   by phase 1's method, tree-blind (every Bash `tool_use` in every `*.jsonl`
   under `~/.claude/projects/*SpecSeal*/`, recursive, distinct (command,
   cwd) pairs): **2,486 of 33,526 pairs**, 7.4%; 561 of them hold only
   `${…}` parameter expansions, and the other 1,926 hold `awk '{…}'`,
   `jq '{…}'`, `{ …; }` groups, `find -exec {} \;` and the like. Exempting
   a bare `${` reads one bash fact and misses `\${a,b}`, which bash makes
   `$a $b` (round 4, executed), so the honest format is the 2,486. Round
   5's rule stops 42 of 33,287 (0.13%); the #826 stop for every
   unrecognised shape cost 315 of 31,193 (1%) and was accepted. A rule
   sixty times that, taken in every dirty tree, is the outage §*Unknowns
   resolve conservatively* refuses, not a prompt. Offered to the owner as
   `questions.md` P2's alternative with its count, and not the default.

   **Delete.** The guard reads the words the frozen reading splits, and a
   word the shell builds before git runs — a brace expansion, a
   substitution that spells `git`, a here-string handed to a shell, `g""it`
   in a line the splitter cannot close — is not among them. #886 already
   holds the other four as one undecided class, each silent in an ACTIVE
   tree at 5623d728, deferred by round 4 and the orchestrator rather than
   widened into this redesign. The brace is the fifth, and the one this
   run spent five rounds and a reframe closing on its own while the other
   four stayed open. Deleting the brace reader puts the five back in one
   class, named once in §*Known limits* and decided once, in #886, by the
   owner. **This is the second reframe's default, and the build ships on
   it under `Automation | yes`.** What it costs: `git rebase
   {main,feature/x}`, `git rebase --ro{,} feature/x`, `git stash {branch,}
   x` and `git worktree {add,} ../wt f` are listed to the guard and silent
   in every tree, as at 0.20.0; over 33,287 recorded pairs one git segment
   held a brace, a `git add` of a `{plan,questions}` path, and none of the
   four forms was ever recorded. The Premise's protection against a
   shell-built word is already incomplete by #886's four, so the brace's
   silence is a limit the tree already has, named rather than guessed at.

   **What stays.** Everything §A built before this work item: the three
   shapes, `LEAVES_THE_TREE`, the switch and creation rules, the
   unrecognised-shape stop where the tree matters, the trees a cut group
   and a wider-read git are judged in. `_rebase_names_a_branch`'s docstring
   as phase 3 corrected it (S14). The git-binding case
   `test_no_listed_form_moves_head_under_git` keeps running the four brace
   forms through bash: it pins that bash moves HEAD on three and adds a
   worktree on the fourth AND that the guard reads each as listed, which is
   the limit stated as a fact the way M1's case states its own — the day a
   change to the frozen words makes the guard read one, the case says so.

6. **What leaves the tree.** From phases 2, 4 and 5, closed:
   `worktree_consent.py#creation_directory`'s placement loop; the body of
   the guard's `judgeable` and its tokenizing adapter's doubling line (one
   home each); `session-lease.py#owner_pid`'s walk; the guard's basename
   test in `sessions_in_tree`; `commit-review-gate.py#git`;
   `commit-review-gate.py#_reads_marker` and the body of `has_marker`; the
   guard's `has_token` body and `_without_bodies`; the word `CLAUDECODE`
   from `githooks._P2` and from `tokens.steps_around_hooks`; two of the
   three `(…)` strips.

   From the second reframe, phase 11. The list is fenced because every name
   in it is one the tree will not have once the phase closes (the record
   checker reads a fence as a quotation):

   ```
   hooks/worktree-guard.py
     _BRACE and the comment above it; _unquoted_brace
     the `braced` parameter of _git_finding, _segment_finding, shape_of,
       _merged_findings and _first_finding_in
     the brace arm of _git_finding and of _segment_finding
     the brace half of _command_findings' untokenizable arm
     the command-level brace finding in _first_finding_in and in main
     _finding_trees (the union of -C trees was built for brace segments
       alone; _finding_tree stays and main calls it)
     _described's `brace` branch, both languages
     main's `braced` read
   tests/test_worktree_guard.py
     BRACE_SHAPES, BRACE_EN, BRACE_KO
     test_a_brace_expansion_in_a_git_word_is_unrecognised
     test_a_brace_that_makes_the_command_word_is_unrecognised
     test_a_brace_in_any_word_is_the_brace_shape
     test_a_brace_command_word_is_judged_in_the_tree_its_c_names
     test_a_brace_segment_composes_its_c_values_as_git_does
     test_a_brace_in_a_command_that_will_not_split_stops
     test_a_c_a_brace_hides_is_the_named_limit
     test_a_brace_in_a_body_or_a_cut_group_is_unrecognised
     test_a_broken_token_reader_reads_every_brace_as_unquoted
     test_the_brace_stop_reads_in_korean
     test_a_quoted_brace_in_a_git_word_stays_listed
     test_a_quoted_brace_beside_an_unquoted_one_stops_on_both
     test_what_the_shell_does_not_expand_stays_silent
   tests/test_guard_resolves_the_tree_it_judges.py
     test_the_guard_policy_names_the_brace_shape_and_its_costs
     test_the_guard_policy_names_a_brace_hidden_c_among_the_known_limits
       (both replaced by the one pin S27 names)
   docs/worktree-guard-spec.md
     §A's four brace paragraphs, from "A brace expansion is unrecognised
       (#856)" to "A creation is §B's and is read as it was"
     the brace sentence of "The failure direction"
     the brace-hidden -C sentence of the `sh -c` bullet in Known limits
     every `Enforced by:` entry naming a removed case
   ```

   `questions.md` P1 is withdrawn, not answered. The build names each in
   `phases/phase-11.md`.

### Out

- **`hooks/answers.py#given`'s match by `ps args=` text** (#868 item 3's
  last sentence). Two parallel calls with the same command text cannot be
  told apart, and `docs/the-commit-gate-inside-git.md` §*Known limits*
  already says so. Measured by this frame: the harness exports no per-call
  id to a Bash child (`env` on 2026-10-07 shows `CLAUDE_CODE_SESSION_ID`,
  `CLAUDECODE`, `CLAUDE_PID`, `CLAUDE_CODE_CHILD_SESSION` and nothing
  naming a tool use), so there is no owned input to read instead. Stays.
- **The other copies #868 lists for scope** — `WRAPPERS` ×4, the git-dir
  resolvers ×6, the once-per-session markers ×6, the `automation_answered`
  wrappers ×3. No measured disagreement; #835's registry names them.
- **The guard's enumeration of other sessions by `ps -axo comm`** against
  the lease records (part 1 row 184). That is the guard's activity model,
  not the session's identity; In 2 gives it the one predicate and nothing
  else.
- **The writer recording a creation whose exit status it never reads**
  (part 1 row 134). `test_a_failed_creation_still_records_the_approval`
  pins it as intended: the approval is the fact recorded.
- **`hooks/cmdline_base.py`.** Unchanged; nothing here needs it reopened.
- **A switch arm inside git** — `reference-transaction` refusing a `HEAD`
  move in a tree another session is in. Weighed as the owner asked and
  rejected on the executed table of In 5: the hook sees the switch after
  the tree moved (2.50.1) or not at all (2.34–2.43), so a refusal breaks
  the tree and a report protects nothing. The four costs the owner named
  were weighed too and are smaller than this one: a foreign hooks slot
  would keep the text guard beside the hook, two readers of one act; a hook
  cannot ask, so §A's choice and tracked-changes rows would become denies
  with text; the session (`hooksession.session`) and the press
  (`commitgate.pressed`) ARE readable from a hook process since #692 and
  #868, so context is not the blocker, the order of git's operations is.
  `plan.md` Alternatives holds the rows.
- **A creation arm inside git.** The executed table shows 2.50.1 refusing a
  worktree creation cleanly at `prepared`, before any checkout, which
  `post-checkout` could not (P6 of #692). It is not built here: the
  creation is a consent question a hook cannot put, P6 (a) is the owner's
  answer, and #868's placement fact (In 1) held through every round. The
  fact goes to the owner as `questions.md` P3, with no code behind it.
- **Reading where a brace stands, what it spells, or whether it is quoted**
  — everything rounds 1–5 built. A finding that asks for one more shape of
  it is answered from In 5, not fixed.
- **#856's answer (a)**, expanding braces in the guard; **the character
  format** (In 5, P2's alternative); **report-only** after the tree moved
  (P4 (c) of #692, declined on 2026-10-01); **a `git` function or `PATH`
  shim in the Bash tool's shell**, which would observe git's argv but is
  not an input this plugin owns and is stepped around by a path-qualified
  `git`, `command`, `exec` and `env`. Each in `plan.md` Alternatives.
- **#886's four shapes.** The owner's issue; the brace joins it as the
  fifth by a comment the orchestrating session posts (no agent posts).
- **Windows.** In 1's adapter and In 2's `ps`-less route are read, not run;
  `questions.md` names the answerer.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a session at `S` with a clone, when `eval x ; cd <A> \|\| git worktree add ../wt f` reaches the guard and then the writer, then the guard judges `S`'s clone and the record is written under `S`'s clone | a case red at 5623d728 (the writer files under `<A>`'s clone there) |
| S2 | Given `cd <missing> ; git worktree add ../wt f`, when the writer runs, then it records under the session's clone | a case red at 5623d728 (no record there) |
| S3 | For every chain of `BASE_TREE_CHAINS`, the inventory's shape and S2's, the writer's directory is the guard's `judgeable` target | a property case over the list; the three existing writer cases stay green |
| S4 | Given a process tree whose nearest ancestor's comm is `/x/bin/claude`, both `session-lease.py#owner_pid` and `hooksession.claude_ancestor` name it; given one whose comm is `claude-host`, neither does and the lease omits `pid` | cases against a fixture tree, through the one reader |
| S5 | Given `CLAUDE_PID` in the environment, the lease records it and the hook's lease route reads it, with no `ps` run; with it absent, the `ps` walk answers as today | cases; `test_s9_an_emptied_environment_is_still_judged_through_the_lease` stays green |
| S6 | The stub's text carries `CLAUDE_CODE_SESSION_ID` and no `CLAUDECODE`; `CLAUDECODE= git commit -m x` is plain (`is_plain`) and stands aside where git decides; `CLAUDE_CODE_SESSION_ID= git commit -m x` is judged by the reading | cases; the `CLAUDECODE` fixtures of `test_the_commit_gate_decides_at_the_commit.py` rewritten to the one name, one of them flipped to plain |
| S7 | Given `git commit -m 'x [no-review]` (an unclosed quote), when the PreToolUse reading judges it in an opted-in, undeclared clone, then the review arm is missing and the refusal names `git -c specseal.waive=review` | a case red at 5623d728 (waived through the substring fallback there) |
| S8 | For every command in the three consent-token corpora (`test_the_old_spellings_reach_the_hook.py`, `test_one_heredoc_shape_is_data_to_the_commit_gate.py`, the guard's `BODY_TOKENS`/`TYPED_BESIDE_A_BODY`), `has_marker` and `has_token` answer what `tokens.given` answers | a property case over the corpora; T1's and W1's cases stay green |
| S9 | `[worktree-ok]` in a comment, in parentheses and beside a body is read as today; a token only a body carries is not | the existing guard cases, unchanged |
| S10 | Given a repository declaring `seal/parity.md` and a `git` whose `diff` exits non-zero, when `pre-commit` and the PreToolUse reading judge a code commit, then the parity arm is among the arms missing | a case red at 5623d728 (silent there) |
| S14 | `_rebase_names_a_branch`'s docstring says the words are read once their redirections are off | the docstring; a `Corrected ·` row for R1 in the fragment |
| S15 | `docs/worktree-guard-spec.md` §*Known limits* adds the brace creation to the hidden-spelling bullet, §*Creation consent* says the record's clone is the one the guard judged; `docs/the-commit-gate-inside-git.md` names `CLAUDE_PID`, the one predicate and the one variable; `docs/commit-review-gate-spec.md`'s consent-read paragraph says a command that does not split carries no token; `docs/the-review-and-parity-arms.md` §*Parity arm* says a diff git could not take is asked about | the policy pin cases, each sentence with its `Enforced by:` line. The §A brace clause this row carried before the second reframe is S27's now |
| S16 | The stop cost of In 5 as first framed and the waiver cost of In 3 are counted over the recorded corpus by the method of 1791270162's phase 1 | `phases/phase-1.md`; the probe deleted |
| S23 | `test_a_pid_beside_no_session_id_on_either_side_is_not_recorded` builds both absences: the environment variable removed or empty, the payload key absent or empty, four parameters; `test_a_pid_exported_for_another_session_is_not_recorded`'s `outer=None` removes the variable; `run_main_in_process` leaves `session_id` out of the payload for `None` | the four parameters green at a8f86f44; `[None-None]` and `[-]` red with `hooks/session-lease.py` at e0c5a191, shown in `phases/phase-8.md` as round 3's ⬜ 4 executed it |
| S25 | Every name In 6 lists for phase 11 is absent from `hooks/worktree-guard.py` and the two test modules, no `braced` parameter is threaded anywhere, `_finding_tree` is what `main` calls for every unrecognised shape, and nothing imports or names them | `phases/phase-11.md`'s removal table; `uvx ruff check hooks/ tests/`; `grep -n 'brace\|_BRACE' hooks/worktree-guard.py` finding only the limit's comment |
| S26 | `git rebase {main,feature/x}`, `git rebase --ro{,} feature/x`, `git stash {branch,} y` and `git worktree {add,} ../wt feature/x` are listed to the guard and silent in an ACTIVE tree, and under bash the first three move HEAD and the fourth adds a worktree; `git commit -m '{a,b}'`, `git log --format='{%h}'`, `cat {a,b}` and `echo {a,b}` are silent in every tree | `test_no_listed_form_moves_head_under_git`'s `BRACED` half, its assertion inverted from *the guard reads none of the four as listed* to *the guard reads each as listed*, and one case `test_a_shell_built_word_is_the_named_limit` in `tests/test_worktree_guard.py` over the eight forms in an ACTIVE tree; the inverted assertion and the new case red at 52c72bbe (the guard stops the four there), executed in `phases/phase-11.md`; the new case's name is NAME NOT IN TREE until phase 11 plants it |
| S27 | `docs/worktree-guard-spec.md` §A holds no brace paragraph and names no brace cost or count; §*Known limits*' first bullet, or a bullet beside it, says in one sentence that a word the shell builds before git runs is not read — a brace expansion, a substitution that spells `git`, a here-string or heredoc handed to a shell, a git spelled past the splitter — names the four #856 forms as silent, and points at #886 as where the class is decided; the hidden-spelling bullet keeps its `{add,}` example; the `sh -c` bullet names no brace-hidden `-C`; `docs/the-commit-gate-inside-git.md` §*The convergence argument is claimed for commits alone* gains one sentence: a branch-naming rebase reaches `reference-transaction` the same way a switch does (executed by the reframe on 2.50.1) | one policy pin in `tests/test_guard_resolves_the_tree_it_judges.py`, `test_the_guard_policy_names_the_shell_built_word_limit`, replacing the two brace pins and red at 52c72bbe, its name NAME NOT IN TREE until phase 11 plants it; the commit-gate policy pin extended by the sentence |
| S28 | `tests/test_the_hook_surface_git_offers.py::test_no_git_refuses_a_switch_before_the_tree_moves` runs the branch-naming rebase (`git rebase main other`) beside `switch` and `checkout`, and reads the same two branches: a `HEAD` or `refs/heads/other` line after the tree moved, or no line | the parameter added; green on 2.50.1 as the reframe executed it, and the CI floor leg |
| S29 | The records say what the tree has: ledger rows S11, S11a–S11e, S12, S13, S13a, S15b, S17–S22, S24, S24a and S20a leave the unreleased fragment or are rewritten against S25–S28; the changelog's brace paragraph says the brace reader was built and taken out inside this release and names the limit; `overview.md`'s Not done names #856 closed as a limit and the brace handed to #886; `questions.md` P1 reads withdrawn, P2 and P3 stand; `plan.md`'s Status column closes 11 and 12 | `bin/evidence-check . --strict`, `bin/correction-check`, `survivor-check --range origin/release/v0.21.0...HEAD`, the eight suite-wide guard modules, exit codes read directly |

### Scenarios the second reframe retires

Kept so that rounds 1–5 and phases 3, 7 and 9 still resolve; none is
acceptance any more. S11, S12 and S13 asked for the brace shape in a git
word, its quoted forms and the git-binding half (phase 3, b5ceec40); S17–S21
for the rule on every word, its union of trees and the removed command-word
units (phase 9, 6e5e02bf); S22 for the over-stop count, 42 of 33,287 as
round 5 left it (phase 7, 452cf167, corrected in rounds 4 and 5); S24 for
§A's text of all that. S13's bash half survives inside S26; the rest is
history in `phases/phase-3.md`, `phase-7.md`, `phase-9.md` and the round
records.

## Data & interfaces

- `hooks/hooksession.py`: `SESSION_VARIABLE`, `is_claude(comm)`,
  `claude_pid(environ=None)`; `session` and `from_lease` keep their
  signatures (phase 4).
- `hooks/githooks.py#_P2` formatted from `hooksession.SESSION_VARIABLE`; the
  stub's bytes change, so the installer rewrites every opted-in clone's
  stubs at the next session, as §*The hooks are stubs* says it does.
- `hooks/tokens.py`: `given` unchanged in signature; `without_bodies` with
  the frozen fallback; `steps_around_hooks` reading the one name.
- `hooks/gate.py#git(args, cwd) -> str | None`; `touches_code(None) is True`;
  `arms_missing`'s `paths()` may answer `None`.
- `hooks/worktree_consent.py`: the one tokenizing adapter and the one
  placement function; `creation_directory` through them.
- `hooks/worktree-guard.py` after phase 11: `_git_finding(tokens, parsed)`,
  `_segment_finding(tokens)`, `shape_of(tokens)`, `_merged_findings(items)`,
  `_command_findings(text, clean, depth)`, `_first_finding_in(body, depth)`
  and `_finding_tree(tokens, wheres, cwd)` as they stood at 5623d728 in
  shape; `_described` without a `brace` kind; no `_BRACE` (NAME NOT IN TREE), no
  `_unquoted_brace`, no `_finding_trees` — NAME NOT IN TREE once phase 11 closes.
- `hooks/commit-review-gate.py`: `git` → `gate.git`; `has_marker` →
  `tokens.given`; `changed_paths` answers `None` on a failed diff.
- Policy: the documents S15 and S27 name, with `Enforced by:` lines.
- Ledger: `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md`,
  with `Re-read ·` or `Corrected ·` rows for G3 and G6
  (`seal/releases/0.17.0.md`), W1 (`0.18.2.md`), T1 (`0.18.3.md`), F3 and
  R1 (`0.20.0.md`), as `docs/the-evidence-ledger.md` §*A released row is
  read again in the branch's fragment* says; the brace rows retired or
  rewritten in place, the fragment being unreleased (S29).

## Rule changes

- nothing
  why: written: one session reader, one waiver reader and one placement, in
    docs/the-commit-gate-inside-git.md and docs/worktree-guard-spec.md *Creation consent*;
    overturned: the brace reader, taken out in its own release, now a known limit.

## Open questions → questions.md

`questions.md` holds the judgments each frame made from the tree, the
measurements that answered, and the rows a person owns.

Since the second reframe: P1 (the wide brace rule) is withdrawn, because the
rule leaves the tree. P2 is the owner's: the default is the deletion In 5
describes, and the alternative is the character format with its measured
count; the build ships on the default under `Automation | yes`. P3 hands
the owner one executed fact with no code behind it: 2.50.1 refuses a
worktree creation cleanly at `prepared`, which #692's P6 believed no hook
could. W5 is the work's: which brace cases retire and which one is
rewritten, recorded in `phases/phase-11.md`.

Framed 2026-10-07 by framer, before the build.
Reframed 2026-10-08 by framer, after round 3.
Reframed 2026-10-12 by framer, after round 5.
