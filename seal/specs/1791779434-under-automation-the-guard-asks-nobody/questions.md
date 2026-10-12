# 1791779434-under-automation-the-guard-asks-nobody — questions for the planner

<!-- seal/specs/1791779434-under-automation-the-guard-asks-nobody/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here.
Framed by `specseal:framer` on Fable 5.1 for #894. Nobody answers mid-run:
every row carries a default and the plan is built on it. -->

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `spec.md` or in
`plan.md`'s Alternatives table.

1. **Where an `automation` press is read from once the session is gone.**
   Nowhere new. Nothing exists that survives a machine move and that the
   model cannot forge: the transcript and the git directory are machine-local,
   and everything that travels is in the tree, which the model writes
   (`spec.md` In 1; `docs/worktree-guard-spec.md` §*Creation consent*'s table
   of five sources). The remedy is procedural: a resumed run presses again
   through the tool (In 3, `plan.md` G), which is a recorded fact the existing
   reader reads.
2. **Whether the dirty-tree row denies under the press.** Yes, to the model,
   naming commit-first and stash each as a command of its own, and no question
   tool — the shape `docs/commit-review-gate-spec.md` §*Where the person said
   nobody would be answering* gives every stop (`spec.md` In 2, `plan.md` F).
   Attended, the row is unchanged.
3. **Whether the commit gate has the same gap.** Yes, by construction: its
   `automation_pressed` wraps the same `automation_answered`. It is fixed by
   In 3 alone and no line of it changes (`spec.md` S8). Where the plugin's git
   hooks run, a commit stop is text to the model already.
4. **Whether `[shared-tree-ok]` reaches the dirty row under the press.** No,
   as today: it answers a different question (§*Choice sites*). Carrying the
   changes along is reachable through the stash sequence, so nothing is lost.
5. **Whether #21's attended choice site is built here.** No. It changes the
   prompt a person sees and spends the switch direction's budget; In 2 reuses
   its table of destinations so a later #21 inherits the words (`plan.md` E).
6. **Whether a subagent's command is treated differently.** No (`plan.md` D):
   that predicts a payload shape, and attended the person can answer.
7. **Why the ways on are commands of their own.** The guard reads the tree
   before the command runs, so `git stash && git switch x` in a dirty tree
   meets the same deny; S5 pins it so the text cannot send the model into a
   loop.

Judgments the reframe after round 3 made, from the round records and the
tree (`spec.md` §*Why the deny predicts nothing*, `plan.md` I–L):

8. **Whether round 3's two findings get a third fix.** No. Each of three
   rounds found the next switch form the recipe was wrong for, with no fact
   the guard reads to tell a right cell from a wrong one; that is the class
   the repository has judged not to converge, and the chain's own rule spends
   the stop on a redesign (`plan.md` I).
9. **Whether the guard should read HEAD's state, the target branch or the
   stash to get the recipe right.** No: a new reader the switch arm is pinned
   not to gain, and a pop's outcome is git's merge, which no reader short of
   running it knows (`plan.md` J).
10. **What the deny says instead.** What it read and what it is: the changes,
    the press, that it stops a switch while they are present and says nothing
    once they are not, that `git commit` and `git stash` are listed shapes
    that pass it alone, that a compound meets the same row, that a re-issue
    meets the same refusal. No sentence about what git does for any form
    (`plan.md` K; S12 pins one text for every form).
11. **Whether the press sentence changes.** No: #896 copies it verbatim, and
    the reframe moves nothing in it.
12. **Whether the deny names `git stash pop` or any step after the one
    command.** No. Naming the next step is where every round's finding lived,
    the attended `ask` names *commit/stash first* and nothing after, and the
    commit gate's `AUTOMATION_WAYS` names acts and never outcomes. A model
    under the press knows git; the guard tells it what it read.
13. **Whether the attended `ask`'s *They will follow you onto the target
    branch* is corrected too.** No: it is the base's text, false for the
    discarding forms, pinned byte-identical by S2 and owned by #21's attended
    site. The reframe changes the pressed reader only.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| P1 | **The two `choose` rows under the press — in scope?** §A rows 1-b (only IDLE sessions) and 2 (detection unusable) deny once per session per direction with a reason that tells the model to call `AskUserQuestion`, then `ask` on every attempt after. Under the press both are a person's prompt, one step removed. They are the same class as #894's two stops (`spec.md` §*The class*), but what needs nobody there is a product decision: splitting into a worktree is always available (consent is read first for a creation), while pressing `[shared-tree-ok]` on the model's own judgment is the call the row exists to hand a person. Not measured in #894; on Windows every switch takes row 2 | **a person**: the repository owner. It is what an unattended run does about sessions it cannot show to be working, and somebody has to be accountable for it | **(a)** out of scope here: `spec.md` §*Out of scope* names it, §*Known limits* carries one sentence, and the orchestrator files it as an issue. **(b)** in scope as a third phase: under the press both rows deny on every attempt and name the worktree split as the way on, never the token. **(c)** (b), but the deny names `[shared-tree-ok]` too, leaving the judgment to the model | (a); the frame is built on it, and (b) is reversible as a later item | ⬜ |
| P2 | **A same-machine fallback to an earlier session's press — wanted?** `plan.md` A refuses reading the other main transcripts of this machine for the latest routing answer in this clone, because of cross-talk between an automation run and an interactive session in one clone, the scan cost on every stop, and because it would not have changed #894. The owner's runs do span several sessions on one machine between machine moves (`questions.md` of `1791270162`: *asked by the next session on another machine*), so the trade is one click per resumed session against that fallback | **a person**: the repository owner | **(a)** no; a resumed run presses again (In 3). **(b)** yes, with this ordering: this session's own transcript decides where it holds any routing answer, and the latest answer from this clone across the other main transcripts of this machine decides only where it holds none; the scan is bounded to files modified in the last N days, N named by the owner. Each is a new reader clause and a new `Enforced by:` set in §*Creation consent* | (a) | ⬜ |
| M1 | **Does the diagnosis hold on this machine?** For the session in which the two stops happened, does `worktree_consent.automation_answered(<root of the main checkout>, <that session id>, "")` return False, and does that transcript hold any `AskUserQuestion` result whose options are the three routing labels? The ticket asserts both (*This session's transcript holds no click*); nobody has run the call | **a measurement**: phase 1, one call outside the suite, as `1790644505` Q1 was taken; no case may read a real transcript (`tests/conftest.py#_no_real_transcripts`) | **False and no routing result:** the ticket's reading stands and In 3 is the fix for stop 1. **True:** the reader found a press and stop 1 asked for another reason; phase 1 finds which condition before building on In 3 and records a divergence row in `overview.md` | the ticket's claim stands | ✅ executed 2026-10-12: False, replayed up to stop 1, and no routing result before it; the one press is at 04:59:51Z, after both stops (`phases/phase-1.md`) |
| M2 | **Which events change the session id?** Does `claude --resume` keep the session id and append to the same transcript file, and does auto-compaction? `/clear` and a new `claude` start are assumed to issue a new id. This decides the wording of §*Known limits* and of In 3's paragraph (*a new session — a new day, a `/clear`, another machine*) | **a measurement**: phase 2, read off two transcripts on the building machine (a resumed one and a compacted one), by their file names and the session ids inside; or the harness documentation where it states it | **Both keep the id:** the wording stands and names only `/clear`, a new start and another machine. **Either issues a new id:** the paragraph names it too, and that event becomes a moment a person has to press again, which is a cost worth stating | both keep the id; the paragraph is written hedged until read | ✅ executed 2026-10-12: both keep the id, so the wording names a `/clear`, a new start and another machine; that those two issue a new id stays assumed (`phases/phase-2.md`, `overview.md`) |
| M3 | **Does the deny loop?** At the next `automation` run after this ships, how many dirty-row denies does each session meet, how many were the same switch re-issued unchanged, and how many guard `ask`s of any row reached a person | **a measurement**: taken by the orchestrator of that run from its own transcript, by the method `spec.md` §*What was measured* of `1790644505` used; posted to the open flow-measurement log as the segment ends | **None repeated, zero asks under the press:** the reason's text is enough. **Repeats:** the text is reworded first; a mechanism (a count of refusals naming the command) is a new work item carrying `CONTRIBUTING.md`'s four requirements. **An ask under the press:** its row is P1's or a site this enumeration missed, and is named | the reason's text bounds it | ⬜ |
| W1 | **The deny's exact text**, English and Korean: the changes listed as today, then the ways on — commit here first (as its own command; on a declared branch the commit gate is silent for it), or `git stash`, the switch, `git stash pop` as three commands with the note that `pop` applies to whatever is checked out — then no question tool and the re-issue sentence. And how a detached HEAD is handled: stop 2 ran from one, where a commit lands on no branch. Either the guard reads HEAD's state (one more git spawn, against `test_the_repository_lookup_cannot_hang_the_gate`'s spawn budget) or the text tells the model the one-line check (`git branch --show-current` prints nothing) | **the work**: phase 1 | One text pinned by S1 and S3 in both languages, following `skills/writing-style` for the Korean half; the detached-HEAD handling is recorded in `phases/phase-1.md` | — | ✅ phase 1: one `tr(en, ko)` text pinned whole by S1 and S3; a detached HEAD is a check the model runs, not a spawn (`phases/phase-1.md`) |
| W2 | **Where the press is read in `main` for the dirty row**, and whether it is cached beside `seen` so a command holding an unrecognised shape in a dirty tree and a switch reads the transcript once; `automation_pressed` is read against `repo_paths(cwd)[0]`, the session's own root, as the stop's call is | **the work**: phase 1 | A read in the `if entries:` block, or a value computed once above the ladder and handed to both; `test_the_tree_is_read_once_for_both_kinds`'s standing holds either way | — | ✅ phase 1: read in the `if entries:` block, uncached, because the stop exits whenever it fires; the own root pinned by `test_the_press_is_read_from_the_sessions_own_root` (`phases/phase-1.md`) |
| P3 | **(reframe) Should the deny name `git stash` beside `git commit`?** The reframed deny names the two plain commands that leave a tree with no uncommitted tracked change and promises nothing about what follows. A stash is the lighter act and the one the attended `ask` names first (*commit/stash first is recommended*), but a model that stashes and does not restore leaves the change in `git stash list` of a tree nobody opens again, on the guard's word. A commit on a declared branch is silent at the commit gate and keeps the change in history, where a squash or a later commit finds it. The tree answers neither way: the base names both attended, and no run has measured an unattended model's stash discipline | **a person**: the repository owner. It is what an unattended run is told to do with changes that are not ready to commit, and somebody has to be accountable for a change that waits in a stash | **(a)** both, as the attended `ask` does; the model chooses (`plan.md` K). **(b)** `git commit` only; the text says a stash is the model's own act and the guard names none (`plan.md` L). **(c)** both, plus one fact: *what `git stash` set aside is listed by `git stash list`* — a sentence about git's state, not its outcome | (a); the frame is built on it, and (c) is one sentence if M4 counts stashes left behind | ⬜ |
| M4 | **(reframe) Does a model told less finish what it started?** At the next `automation` run after this ships: of the dirty-row denies each session met, how many were followed by `git stash` with no `git stash pop` or `apply` later in that session's transcript, how many by a commit on a detached HEAD with no `git branch <name>` after, and how many by the same switch re-issued unchanged (M3's count, kept) | **a measurement**: taken by the orchestrator of that run from its own transcript, by the method M3 names; posted to the open flow-measurement log as the segment ends | **No stash left, no commit stranded:** the text is enough and P3 stays at (a). **Stashes left:** P3's (c) sentence, or (b) on the owner's answer; never a recipe, which is what three rounds measured not converging. **A switch re-issued unchanged:** M3's answer applies | the reason's text bounds it, as M3 assumed | ⬜ |
| W3 | **(reframe) The deny's exact text**, English and Korean, with the shape In 2 lists and nothing keyed on a form: the lead, listing and note as today; the press sentence byte-identical to the first frame's; the row's meaning in the guard's terms; `git commit` and `git stash` as listed shapes issued alone, the choice and what follows left to the model and git's output; the *Issue each command on its own* sentence; the re-issue sentence. The Korean half follows `skills/writing-style`; the premise sentence of 8c1db4bd (*a switch that keeps them carries them*) is a prediction and goes | **the work**: phase 3 | One `tr(en, ko)` text pinned whole by S1 in both languages, identical across S12's forms; the block's comment rewritten with it | — | ⬜ |
| W4 | **(reframe) What becomes of the three recipe cases of rounds 1–2** (`test_a_creating_switch_under_the_press_takes_the_stash_way`, `test_an_orphan_switch_under_the_press_takes_the_commit_way`, `test_the_deny_does_not_say_a_discarding_switch_carries_the_changes`) and of S4's outcome assertions: removed with the sentences they pin, or folded into S12's parametrisation as forms whose reason is the same bytes. And which option words S12's negative check lists, given that `{git}` is `git -C <path>` in W2's case and `-C` is also a switch option | **the work**: phase 3 | The removals and the word list recorded in `phases/phase-3.md`, with the `Enforced by:` line of the policy paragraph following in phase 4 | — | ⬜ |

**`Who can answer` takes one of three values and nothing else.**

- **a person** — what the product should be, or a value somebody has to be
  accountable for. The only kind of row that blocks the build, and under this
  run's `automation` answer neither P-row blocks: each is built on its
  default, which `routing.md`'s *Why this way* says is the run's shape.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records it in its `phases/phase-N.md`.

**The framer opens rows and does not own their answers.** The `Status` column
is ticked by whoever answered, never by whoever asked.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
