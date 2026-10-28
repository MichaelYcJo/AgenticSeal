# Questions for the planner: 1793169129-the-creation-row-still-says-retry-with-worktree-ok

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `frame/design.md` or
in `frame/plan.md`'s Alternatives table.

1. **Whether #903's decision extends to row 5's hints.** Yes. The owner
   answered (b) to
   `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/questions.md`
   Q1 on 2026-10-28, which names #920 as the fix to the two `[worktree-ok]`
   hints and keeps it in 0.24.0.
2. **Which hints.** Two, both at row 5 under the press: the confirmation
   sentence in `steer_to_switch`, and the quote note in `judge_creation`'s
   origin. `frame/design.md` *The class* checks every other site in the
   creation direction and finds no third.
3. **What replaces the confirmation sentence.** `press_sentence()` and
   `reissue_sentence()`, the shared strings every deny under the press
   carries, in both languages. No new sentence is written (`plan.md` A over
   B and D).
4. **Whether the steer to `git switch` stays under the press.** Yes. #903's
   frame relied on it, and the switch it names reaches no person
   (`plan.md` *Technical context*).
5. **Where the press is read.** Inside row 5, from the session's own root,
   with the reader rows 3 and 4 use. Nothing new is read.
6. **What the transcript costs.** At most two reads per creation, the bound
   #903 set. The S5 pin becomes `[1, 2, 2, 2]`.
7. **The attended path.** Byte-identical, both languages, with and without
   the quote note (S3).
8. **The policy documents and the READMEs.** The pull request does not edit
   `docs/`; `frame/design.md` *Rule changes* carries the two sentences the
   settle writes. Neither README describes row 5's text, so neither changes.
9. **Windows.** Row 5 is never reached there, because every tree reads
   detection unusable and takes row 4.
10. **The parallel work items.** #1058, #913 and #712 own no file this work
    edits (read, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:618`).
    #1096 edits `hooks/worktree-guard.py` after this work, and nothing here
    touches `tr` or the language reading.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| P1 | **Whether row 2, `[worktree-ok]` given, stops asking a person under the press in another clone.** After this work no reason in the creation direction names the token. A model can still write it from what it read elsewhere: `README.md:282` and `README.ko.md:274` document it, and row 2 then puts an `ask` to a person in a run that promised none. The tree cannot answer it: it is a verdict change, which #903 kept out on purpose (its S6, `test_the_token_still_reaches_its_own_row`) and which the owner left out of #920 by scoping it to the hint. What an unattended run does with a token a model wrote is a value somebody has to be accountable for | **a person**: the repository owner | **(a)** Unchanged: row 2 asks under the press as attended. The question stays reachable only by a model that writes the token unprompted. #1049 weighs it with the rest of the guard in 0.24.1. **(b)** Under the press in another clone, row 2 denies on every attempt with row 5's press text, so the token reaches no person. One arm more in `guard_worktree_creation`, S4 rewritten, and a third `## Rule changes` item for *Choice sites*. (b) blocks more and never allows more; what it costs is that a person who did ask for a worktree in another clone during an automation run cannot get one through the token | (a); the frame is built on it | open |
| W1 | **How row 5 reaches the switch command lines without the confirmation sentence.** `steer_to_switch` returns both in one `tr`. Either the three lines become a function of their own and `steer_to_switch` returns that function's text plus the sentence, or `steer_to_switch` takes a flag that leaves the sentence out. Both keep every caller's output unchanged | **the work**: phase 1 | **Own function:** one name for the command lines, which row 5's pressed arm and `steer_to_switch` both call. **Flag:** one function, and a parameter whose `True` arm only row 5 reaches. Either is pinned by S1 and S3, and the choice goes into `trail/phases/phase-1.md` | own function | answered 2026-10-28 by the crafter: own function, `switch_lines(git)` (`trail/phases/phase-1.md`) |
