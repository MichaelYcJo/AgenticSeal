# 1791781864-the-idle-session-rows-ask-nobody — questions for the planner

<!-- seal/specs/1791781864-the-idle-session-rows-ask-nobody/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here.
Framed by `specseal:framer` on Fable 5.1 for #896. Nobody answers mid-run:
every row carries a default and the plan is built on it. -->

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `spec.md` or in
`plan.md`'s Alternatives table.

1. **What the line prints.** `<kind> <age>` and nothing after it — *lease
   declaration 4.7h ago* — not *last seen <age>* (`plan.md` A). The kind
   already names the measurement, and §*What a blocking prompt must show*
   says the line is the signals.
2. **Whether the clause goes from the active list too.** Yes. The function
   cannot tell which list it prints, every header already carries the
   judgment, and an unidentified entry is active because its age is under
   the window, which is what the line says (`spec.md` In 1, `plan.md` B).
3. **Where the press is read for the two rows.** Through
   `hooks/worktree-guard.py#automation_pressed` against the session's own
   root, the stop's reader, and nowhere new; no fallback, no `routing.md`,
   no payload-shape guess (`spec.md` §*Out of scope*; #894 In 1 and its
   `plan.md` A–D hold the refusals).
4. **Whether the deny writes the choice marker.** No. The marker means *the
   question was put*; under the press none is, and a later `per axis` in the
   same clone then meets the attended first attempt (`spec.md` In 2).
5. **Whether the deny names `[worktree-ok]`.** No. The press is consent and
   is read before every creation row, so the split is a plain `git worktree
   add` (§*Creation consent*).
6. **Whether the creation direction's choice rows change.** No; they sit
   below the consent row and never run under the press (`spec.md` §*The
   class*).
7. **Whether row 2 is treated differently from row 1-b.** No (`plan.md` F):
   a wrong allow where nothing can be read is the worst case, and on Windows
   it would silence every switch.
8. **Where the flag lives.** In `choose`, so one function holds a site's
   three verdicts (`plan.md` G).
9. **Where the new cases live.** A new file, so the merge after the review
   rounds does not meet #894's append (`plan.md` H).
10. **The attended path.** Byte-identical, both rows, both attempts, both
    languages (S5).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| P1 | **What the deny names as the way on, under the press.** `spec.md` In 2 denies both rows on every attempt and names the worktree split. Whether it also names `[shared-tree-ok]`, which would let the model switch in the shared tree on its own judgment that the idle session is a forgotten tab, is the product decision #894's P1 handed here. On Windows the choice decides every switch: under (b) the model works in a worktree per branch and never switches; under (c) it may press the token and switch in place, with nobody having judged the tab | **a person**: the repository owner. It is what an unattended run does about a session it cannot show to be working, and somebody has to be accountable for it | **(b)** deny on every attempt; the reason names the split (`git worktree add <wt_root>/<name> -b <branch> origin/main`, then `git -C`), never the token. **(c)** (b), but the reason also names `git switch <branch>  # [shared-tree-ok]`, leaving the judgment to the model. (c) is the lever if (b)'s Windows cost — a worktree per branch, every time — turns out wrong | (b); the frame is built on it, and (c) is one sentence of text and one assertion away | ⬜ |
| P2 | **Whether `[shared-tree-ok]` keeps its standing under the press.** Today the token turns the two rows silent, and nothing verifies who put it there (§*Choice sites*). In 2 leaves that reading as it is: the deny does not name the token, and a model that appends it anyway has read it in the README or the policy, which the command line records. The alternative makes the token inert where the press is read, so the split is the only way on | **a person**: the repository owner. Whether an audit trail is enough where nobody reads it in time is a value somebody has to be accountable for | **(a)** unchanged: S6 pins that the token still silences the rows under the press. **(b)** under the press the token is not read at rows 1-b and 2; the deny says so; S6 inverts; §*Choice sites*' token table gains a row. (b) blocks more and adds a reader clause the ticket did not ask for | (a) | ⬜ |
| M1 | **Does the deny loop, and does a Windows run split twice?** At the next `automation` run after this ships: how many row 1-b and row 2 denies each session met, how many were the same switch re-issued unchanged, how many were a `git switch` inside a worktree already on the branch (the six-months scenario in `plan.md`), and how many guard `ask`s of any row reached a person | **a measurement**: taken by the orchestrator of that run from its own transcript, by the method `spec.md` §*What was measured* of `1790644505` used, posted to the open flow-measurement log as the segment ends | **None repeated, no second split, zero asks:** the reason's text is enough. **Repeats or a second split:** the text is reworded first; a mechanism is a new work item carrying `CONTRIBUTING.md`'s four requirements. **An ask under the press:** its row is a site `spec.md` §*The class* missed, and is named | the reason's text bounds it | ⬜ |
| M2 | **On the Windows CI leg, is a switch under the press row 2's deny with no stub?** Every case stubs `sessions_in_tree`; the claim that Windows reads *detection unusable* on every switch is read from `ps` not taking `-o` there, and from #692's Windows pass, never from a case under the press | **a measurement**: phase 2, one case with the real `sessions_in_tree`, marked to run on Windows only, run by the test workflow's four Windows shards at the pull request; or the reading stays read and the Known-limits bullet says so | **Deny on Windows:** the bullet's sentence is a measured fact and the case stays. **Not a deny:** the Windows reading of §*Known limits* is wrong in a way that helps — some switches there are judged — and the bullet is corrected in this item | the reading stands and is labelled read | ⬜ |
| W1 | **The deny's exact text**, English and Korean, and where it is composed: the row's situation as today, the press sentence (#894's register: *This session's person pressed `automation` on the routing question, so this guard puts no question to them, and none is to be put to them in its place*), the split as two commands with `<wt_root>` filled from `repo_paths` and the command word from `git_at`, the sentence that a worktree already on the branch needs no switch, working there by path with `git -C`, no question tool, the re-issue sentence. Composed in `main` from `steer` and handed to `choose`, or composed inside `choose` from the pieces it is given | **the work**: phase 2 | One text pinned by S3 and S4 in both languages, the Korean half by `skills/writing-style`; the composition recorded in `phases/phase-2.md` | — | ⬜ |
| W2 | **How the press is read lazily at the two rows** so a command reads the transcript at most once (S10): a closure evaluated inside each row's `if`, or a value computed once above the rows only where `idle or not reliable` and `not shared_ok`. `automation_pressed` is read against `repo_paths(cwd)[0]`, the session's own root, as the stop's and #894's calls are | **the work**: phase 2 | S10's counts hold either way; `test_the_tree_is_read_once_for_both_kinds`'s standing holds | — | ⬜ |
| W3 | **S7's fixture.** `repo` has no `origin`; the way on names `-b <branch> origin/main`. Either the case adds a remote and a `main` to the fixture repository so the named command runs as written, or it runs `git worktree add ../wt -b feature/x` and the handover says the start point was omitted | **the work**: phase 2 | The command the case runs is the one the deny names, or the difference is recorded in `phases/phase-2.md` | — | ⬜ |

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
