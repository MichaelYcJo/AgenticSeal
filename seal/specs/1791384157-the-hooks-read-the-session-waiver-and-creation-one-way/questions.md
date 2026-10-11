# 1791384157-the-hooks-read-the-session-waiver-and-creation-one-way — questions for the planner

<!-- seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**Judgments the tickets left open that the tree answered.** Listed so nobody
reopens them; each has its grounds in `spec.md` In or `plan.md` Alternatives.

- **#856's choice between (a) expanding braces and (b) a known limit.** The
  first frame gave a third answer, (c): `docs/worktree-guard-spec.md` §A
  stops a shape the guard does not recognise where the tree matters, and a
  word bash expands before git reads it is one. **Confirmed by the
  repository owner on 2026-10-08** as *an unquoted brace expansion in a git
  word*. **Reversed by the second reframe on 2026-10-12**, on the owner's
  review of the run: (c) was built three times and each round found the
  next hole in its reading of bash, so the reader is deleted and the answer
  is (b), the limit named once beside #886's shapes (`spec.md` In 5, the
  judgment below, P2).
- **How far the consolidation goes** (#868's last paragraph). The four facts
  with a measured or traced disagreement, and the copies a change to one of
  them touches (`crg.git`); the listed-for-scope copies stay (`spec.md`
  Out).
- **Whether `hooks/cmdline_base.py` is reopened.** No. Nothing below the
  rider changes.
- **Which placement rule is the one.** The guard's, because it is where bash
  runs the segment on both shapes that disagreed (the framer's probe,
  `spec.md` In 1) and the base's on the three pinned chains.
- **Whether `$CLAUDECODE` stays in the stub.** No; the verdict is unchanged
  in every state (`plan.md` Alternatives), and the name exists in
  `steps_around_hooks` only because the stub read it.
- **Whether `answers.given`'s match by `ps` text is in scope.** No; a named
  limit with no owned input to replace it (`spec.md` Out, measured).

**Judgments the first reframe made from the records (2026-10-08, after round
3).** Each stands as the record of why phases 7–10 were built; the rule they
built leaves the tree in phase 11.

- **Whether the command-word reading gets a third fix.** No (`plan.md`
  Alternatives).
- **What a brace anywhere means.** A word holding an unquoted brace
  expansion, in any segment, is the brace shape (phase 9; removed by phase 11).
- **Whether an assignment word is exempt** (round 3's ⬜ 5). No (moot since
  the second reframe).
- **Which tree a non-git brace segment is judged in** (round 2's 🟡 2). The
  union of `place`'s tree and every `-C <dir>` pair (phase 9; removed by
  phase 11).
- **Whether the 34,775 figure is trusted.** Not as the figure for the
  reframed rule; phase 7 measured it, corrected in rounds 4 and 5 to 42 of
  33,287. History since the second reframe.
- **Whether the lease case is the redesign's** (round 3's ⬜ 4). Yes, as
  phase 8; it stands.

**Judgments the second reframe made from the records and from git
(2026-10-12, after round 5, by the owner's decision).**

- **Whether the owner's direction, observing the act through
  `reference-transaction`, can refuse a switch.** No. Executed by the framer
  on git 2.50.1 (`spec.md` In 5's table): a switch, a detached switch and a
  branch-naming rebase hand the hook their line after the index and working
  tree hold the new branch, and a refusal leaves `HEAD` on the old branch
  with the new branch staged; on 2.34–2.43 no line arrives. This is #692's
  M1, pinned on four gits, and the owner's P4 answer of 2026-10-01. The
  four costs the owner asked to weigh were weighed and are not what decides
  it (`plan.md` Alternatives, the observe row).
- **Whether a format that imitates nothing is the default.** No. A `{` or `}`
  anywhere in the judgment text costs 2,486 of 33,526 recorded pairs
  tree-blind (executed, `plan.md` Technical context), sixty times round 5's
  rule, in every dirty tree. Offered as P2's alternative with its count.
- **What the fate of the brace reader is.** Deleted, the third of #834's
  three fates. The limit is named once, beside #886's four shapes, and
  pinned as a fact by `test_no_listed_form_moves_head_under_git`'s bash half
  (`spec.md` In 5, S26, S27).
- **What the PreToolUse guard keeps.** Everything of §A and §B as at
  0.20.0, and #868's four facts (In 1–4, phases 2, 4, 5). Nothing of the
  brace.
- **Whether the creation arm is reopened on the new fact** (2.50.1 refuses a
  worktree creation cleanly at `prepared`). No: a creation is a consent
  question a hook cannot put, P6 (a) of #692 is the owner's, and In 1 held
  through every round. The fact is P3's, for the owner, with no code here.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| M1 | Does a hook process the harness spawns (`session-lease.py` at PostToolUse, the three git stubs' Python through a Bash child's git) see `CLAUDE_PID` in its environment? Measured in a Bash child it is exported and equals the `claude` ancestor's pid; `ps -E` on the session's own `claude` process showed no `CLAUDE_*` variable, so the hook side is unread | a measurement | **yes**: the lease records an observed pid for every session, extension hosts included, and `from_lease` matches it with no `ps` run. **no**: the lease side keeps the walk and only the git-hook side reads the variable (git inherits the Bash child's environment). Either answer builds the same code, because the walk stays under the variable (§13); the answer decides only which route S5 exercises live | **no** is assumed; phase 1 measures it where it can (a Bash child's `env`, read; a hook's environment, by a lease written after phase 4 compared with the walk's answer on a host whose process is not named `claude`, or left `unverified` with the repository owner named) | ⬜ The Bash-child half answered by phase 1 (executed: exported, and equal to the `claude` ancestor's pid); the hook half stays open, `unverified` in `overview.md` with the repository owner named, because no hook of a session can be made to print its environment without changing the installed configuration |
| M2 | How many recorded (command, cwd) pairs hold a git segment with an unquoted brace expansion, by subcommand — In 5's new stop class as first framed, tree-blind? | a measurement | a count. It goes into §A's failure-direction paragraph and the changelog; it changes no code | none needed; phase 1 counts it by 1791270162 phase 1's method, with the self-check first | ✅ one: `git add` of a path holding `{plan,questions}`, from a 2026-09-23 transcript, under `add`, which is not one of the three. Phase 1 answered zero of 32,431 pairs after a self-check that found all four S11 forms and none of the three S12 forms (`phases/phase-1.md`); round 4 found the pair its count missed (`phases/phase-7.md`, corrected in round 4). History since the second reframe: §A carries no figure |
| M3 | How many recorded pairs do not split and carry `[no-review]` or `[no-parity]` as a substring — In 3's cost, the commands that waived through `has_marker`'s fallback and will meet the refusal? | a measurement | a count, for the changelog. It changes no code: the refusal names the git-native spelling either way | none needed; phase 1 counts it in the same probe | ✅ six pairs under the framed rule, four of them the guard's comment form with an apostrophe after the token; one pair under the rule phase 5 builds, the words read before the split fails (`phases/phase-1.md`, `overview.md`'s divergence row) |
| W1 | How does S10 make `git diff --name-only --cached` fail in a test: a `git` shim first on `PATH` that exits 128 for `diff` and execs the real git otherwise, or an index git cannot read? | the work | the shim is portable and names the failure; a broken index depends on the git version's message. Either way the case is red at 5623d728 | the shim; phase 5 records which | ✅ the shim, a POSIX script exiting 128 for any `diff`; the cases skip on Windows (`phases/phase-5.md`) |
| W2 | Which cases retire with the guard's `has_token` body and `_without_bodies`, and which are rewritten against `tokens.given`? | the work | a case whose subject is the removed splitter retires; one that pins the token rule moves to the one reader | phase 5 names each in `phases/phase-5.md` | ✅ none retired; T1's four cases pass unchanged through the one reader, and `test_s6_neither_read_honours_a_token_the_base_did_not` compares against both base reads together (`phases/phase-5.md`) |
| P1 | On 2026-10-08 the owner confirmed #856's (c) as *an unquoted brace expansion in a git word is an unrecognised shape*. The first reframe widened the word to every word of every segment, so `cat {.gitignore,README.md}` and `for f in x/{a,b}.md` stopped where the tree matters. Did the owner take the wide rule and its over-stop? | a person | **yes**: phases 7–10 as written. **no**: the frame reopens | **yes**; built on it in phase 9 under `Automation \| yes` | **Withdrawn by the second reframe, 2026-10-12.** The rule leaves the tree in phase 11 (P2), so there is no wide rule to take. Built on its default in phase 9; the over-stop was 42 of 33,287 recorded pairs as round 5 left it (`phases/phase-7.md`). Not answered by the owner, and no longer asked |
| M4 | How many recorded (command, cwd) pairs does the first reframe's rule stop tree-blind? | a measurement | a count for §A, the changelog and ledger row S11b | phase 7 counts it by phase 1's method | ✅ 42 of 33,287 pairs under the rule as round 5 left it, 41 a segment that is not git and one a git segment; corrected in rounds 4 and 5 (`phases/phase-7.md`). History since the second reframe: the rule is gone and §A carries no figure |
| M5 | Do bash and zsh expand a brace in an assignment word (`A={a,b}`)? | a measurement | **neither does**: the assignment cost was a stop on a word the shell leaves alone. **zsh does**: the cost sentence says so | the bash manual's reading is assumed for both; phase 7 runs both | ✅ neither does: executed in a scratch directory, bash and zsh each printed `{a,b}`, exit 0 (`phases/phase-7.md`). Moot since the second reframe |
| W3 | How does a finding carry more than one tree for S20's union? | the work | one finding per tree, or a tree list on the finding | one finding per tree; phase 9 records which | ✅ one finding, several trees (`_finding_trees`, NAME NOT IN TREE once phase 11 closes), each looked up once and the shape named once (`phases/phase-9.md`). Removed by phase 11 |
| W4 | Which brace cases keep their names and gain parameters, and which are rewritten, in phase 9? | the work | a case whose claim inverts is rewritten under a name that says the new claim; a case whose claim widens keeps its name | S18's name for the inverted case; phase 9 names each | ✅ the inverted case is `test_a_brace_in_any_word_is_the_brace_shape`; the other two keep their names and gain parameters; two cases are new (`phases/phase-9.md`). All of them leave in phase 11 (W5), after which each is NAME NOT IN TREE |
| P2 | **The fate of the brace reader.** The owner asked the frame to weigh observing the act through `reference-transaction`; executed on 2.50.1, the hook sees a switch and a branch-naming rebase only after the tree has moved, so it cannot refuse either (`spec.md` In 5's table). Two fates are left for the reader. **Delete**: the brace machinery leaves, and `git rebase {main,feature/x}`, `git rebase --ro{,} feature/x`, `git stash {branch,} x` and `git worktree {add,} ../wt f` are silent in an ACTIVE tree as at 0.20.0, a limit named once in §*Known limits* beside #886's four shell-built-word shapes and decided for the whole class in #886; none of the four was recorded in 33,287 pairs. **Force a format**: a `{` or `}` anywhere in the command's text outside heredoc bodies is the brace shape where the tree matters, with no quoting, escape or `${` read, so no next spelling exists; it stops 2,486 of 33,526 recorded pairs tree-blind (7.4%, executed by the frame on 2026-10-12), sixty times round 5's rule, `awk '{…}'`, `jq`, `{ …; }` groups and `${VAR}` included, a deny the model rewrites under the press and an `ask` otherwise, in every dirty tree. Which does the owner take? The tree could not answer it: both converge, and the choice is a price somebody has to be accountable for | a person | **delete**: phases 11–12 as written; #856 closes as the named limit, the brace joins #886 by the orchestrating session's comment, and the class is decided there. **format**: phase 11 replaces the brace machinery with the character test instead of removing it, §A names the rule and the 2,486 count with this frame's method, and the thirteen brace cases collapse to one over the character; phase 12 as written. **neither, keep round 5's rule**: the frame is wrong and goes back to the owner, because the owner's own judgment of 2026-10-12 is what refuses it | **delete**; the build ships on it under `Automation \| yes`. The grounds: §*Unknowns resolve conservatively* prices a deny that fires on 7% of commands in every dirty tree as an outage, not a prompt; the Premise's protection against a shell-built word is already incomplete by #886's four, so deleting the fifth names a limit the tree already has; and #834's theme gives a reader that neither observes nor forces a format one fate | ⬜ |
| P3 | **Does the creation arm get a hook, in a later work item?** Executed by the frame on git 2.50.1 (`spec.md` In 5's table): `git worktree add <dir> -b wb` and `git worktree add <dir> other` are each refused cleanly by `reference-transaction` at `prepared`, before any checkout — no directory, no branch — which `post-checkout`'s take-back could not do (P6 of #692, round 1's `-B` finding). Unmeasured: `-B`, `--no-checkout`, `--orphan`, `--lock`, and git below 2.46, which hands the hook no symref line. A hook still cannot put the consent question §B asks, and In 1's placement held through every round. The tree could not answer it: whether to spend a work item on it is the owner's | a person | **yes**: a new issue, framed on its own, measuring the five unmeasured shapes first. **no**: §B stays a text reading on every git, as P6 (a) says. Neither answer changes this work item | **no**, nothing is built here; this row exists so the executed fact is not lost in a transcript | ⬜ not blocking |
| W5 | Which brace cases retire in phase 11, and which is the one rewritten? `spec.md` In 6 names thirteen cases and three constants in `tests/test_worktree_guard.py` and two pins in `tests/test_guard_resolves_the_tree_it_judges.py`; `test_no_listed_form_moves_head_under_git`'s `BRACED` half inverts rather than retires (S26); S26's `test_a_shell_built_word_is_the_named_limit` and S27's `test_the_guard_policy_names_the_shell_built_word_limit` are new | the work | a case whose subject is the removed reader retires; one that pins the limit as a fact stays with its claim inverted; the policy pin follows the sentence | In 6's list; phase 11 names each in `phases/phase-11.md`, with the red run of the inverted half and of the two new cases at 52c72bbe; the two new names are NAME NOT IN TREE until phase 11 plants them | ⬜ |

**`Who can answer` takes one of three values and nothing else.**

- **a person** — what the product should be, or a value somebody has to be
  accountable for. The only kind of row that blocks the build. P2 is one,
  with a default the build ships on under `Automation | yes`; P3 is one that
  blocks nothing here.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument. The second reframe's two measurements, the
  hook table and the format's count, are the framer's and `executed`
  (`spec.md` In 5, `plan.md` Technical context), so they take no row.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer.

**The framer opens rows and does not own their answers.** The `Status`
column is ticked by whoever answered, never by whoever asked. A withdrawn
row says so in its own words and is not an answer.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
