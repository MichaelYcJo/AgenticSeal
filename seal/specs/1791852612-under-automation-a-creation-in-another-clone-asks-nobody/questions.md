# 1791852612-under-automation-a-creation-in-another-clone-asks-nobody — questions for the planner

<!-- seal/specs/1791852612-under-automation-a-creation-in-another-clone-asks-nobody/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here.
Framed by `specseal:framer` on Fable 5.1 for #903. Nobody answers mid-run:
every row carries a default and the plan is built on it. -->

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `spec.md` or in
`plan.md`'s Alternatives table.

1. **Whether the rows change at all.** Yes: the owner decided it on
   2026-10-13 (the issue's comment, `routing.md` §*Why this way*), and the
   frame carries it out (`plan.md` A).
2. **Where the press is read for the two rows.** Through
   `hooks/worktree-guard.py#automation_pressed` against
   `repo_paths(cwd)[0]`, the session's own root, the reader the switch rows
   and the stop use; nothing new, no fallback, no `routing.md`
   (`spec.md` In 1; #894 In 1 and its `plan.md` A–D hold the refusals).
3. **Why the rows are reachable under the press.** Only in a clone the press
   does not consent to (`automation_answered` condition 4) where this
   session holds no record (`granted`); row 0 answers every other creation
   (`spec.md` §*The class*, row 0).
4. **What the deny names as the way on.** Nothing: the split is the creation
   being refused, `[worktree-ok]` reaches an `ask`, and the shared tree is
   the call the row exists to hand a person (#896 P1 (b)). The sentence is
   the switch deny's other-clone sentence where the act is the same
   (`spec.md` In 1; `plan.md` B over C and D).
5. **Whether the deny writes the choice marker or a consent record.**
   Neither: no question was put, and no creation ran (`spec.md` In 1).
6. **Whether either token's reading changes.** No. `[worktree-ok]`'s row is
   above these and is an `ask` by design; `[shared-tree-ok]` is a switch
   token the creation ladder never reads. S6 pins the first.
7. **Whether row 4 is treated differently from row 3.** No, as #896's
   `plan.md` F: a wrong allow where nothing can be read is the worst case.
8. **Where the new cases live.** A new file named for the creation rows,
   importing the two sibling files' helpers (`plan.md` E).
9. **The attended path.** Byte-identical, both rows, both attempts, both
   languages (S3).
10. **The Agent/Task path.** Untouched: its worktree lands under the
    session's own repository, where the press is consent.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| P1 | **Whether row 1 — an ACTIVE session in the other clone — also stops asking under the press.** The owner's decision names §B's two choice rows. Row 1 is a different row with a different reason (*separation justified, creation still needs a human*), and under the press in another clone it is still a question to a person, one the model cannot answer in their place. It is outside what was decided, and the frame does not widen a policy decision on the owner's behalf. The cost of leaving it: a run that reaches another clone's tree while a session is active there stops once, attended | **a person**: the repository owner. What an unattended run does about a tree somebody else is working in, in a clone it was not answered for, is a value somebody has to be accountable for | **(a)** unchanged: row 1 asks, as today; `spec.md` §*The class* says so and nothing pins it beyond the existing `test_worktree_add_active_session_asks`. **(b)** under the press in another clone, row 1 denies on every attempt with In 1's other-clone sentence after the ACTIVE situation, one case more in the new file and one sentence more in §B and §*Creation consent*. (b) blocks more and never allows more; what it costs is that a run can no longer be stopped by a person at that row | (a); the frame is built on it, and (b) is one sentence of text and one case away | ⬜ |
| M1 | **On the Windows CI leg, is a creation in another clone under the press row 4's deny with no stub?** Every case stubs `sessions_in_tree`; the claim that Windows reads *detection unusable* on every creation is read from `ps` not taking `-o` there, and from #896's switch-side Windows case, never from a creation under the press | **a measurement**: S11, one case with the real `sessions_in_tree`, marked to run on Windows only, run by the test workflow's Windows shards at the pull request | **Deny on Windows:** the Known-limits bullet's creation half is a measured fact and the case stays. **Not a deny:** the Windows reading is wrong in a way that helps — some creations there are judged — and the bullet is corrected in this item | the reading stands and is labelled read | ⬜ |
| M2 | **Does a model loop on the deny, and does any run reach another clone at all?** At the next `automation` run after this ships: how many row 3 and row 4 creation denies each session met, how many were the same creation re-issued unchanged, and how many guard `ask`s of any creation row reached a person | **a measurement**: taken by the orchestrator of that run from its own transcript, by the method `spec.md` §*What was measured* of `1790644505` used, posted to the open flow-measurement log as the segment ends | **None, or none repeated:** the reason's text is enough. **Repeats:** the text is reworded first; `plan.md` C is the next frame and carries `CONTRIBUTING.md`'s four requirements. **An ask under the press:** its row is a site `spec.md` §*The class* missed, or P1's row, and is named | the reason's text bounds it | ⬜ |
| W1 | **Where the press sentence and the re-issue sentence live.** Today both are locals of `main` (`press`, `reissue`). In 1 reuses them byte for byte in `guard_worktree_creation`. (a) Move both to module-level functions returning `tr(en, ko)` — functions, not constants, because `tr` reads the language at call time — and have `main` and `guard_worktree_creation` call them; `main`'s hash moves and this item's `Re-read ·` rows cover it. (b) A second copy in `guard_worktree_creation` with a comment naming the first | **the work**: phase 1 | One text pinned by S1 and S2 in both languages, with #896's `test_under_the_press_a_choice_row_denies_every_attempt` still green on the switch side; the choice recorded in `phases/phase-1.md` | (a) | ✅ (a), at `7fd83e55`; `phases/phase-1.md` |
| W2 | **The `Reads:` line for `guard_worktree_creation`.** The unit reads the consent this session holds for the creation's clone through `worktree_consent.consent` (the record, then the answer), the session count through `sessions_in_tree`, the token its caller read, and now the press for the session's own root at rows 3 and 4. Which class and direction the registry's grammar gives that — `docs/the-reader-registry.md` §*The four classes* and the line `main` carries, *guess — … the press in this session's transcript; unknown mixed*, are the models | **the work**: phase 1 | `bin/test tests/test_a_reader_declares_its_input_class.py` green with the census line removed; the line's wording is the warden's to argue at review (§*What neither check can read*, item 1) | — | ✅ `observed`, `refused`, at `7fd83e55`; `phases/phase-1.md` |

**`Who can answer` takes one of three values and nothing else.**

- **a person** — what the product should be, or a value somebody has to be
  accountable for. The only kind of row that blocks the build, and under this
  run's `automation` answer P1 does not block: it is built on its default,
  which `routing.md`'s *Why this way* says is the run's shape.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records it in its `phases/phase-N.md`.

**The framer opens rows and does not own their answers.** The `Status` column
is ticked by whoever answered, never by whoever asked.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
