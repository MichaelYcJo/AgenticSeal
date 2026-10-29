# Feature Specification: 1793169129-the-creation-row-still-says-retry-with-worktree-ok

Issue #920. Under the `automation` press, a `git worktree add` in another
clone, where this session's is the only live stream, meets the creation
ladder's row 5 (single stream), whose deny still tells the model to get the
user's confirmation and to retry with `[worktree-ok]`. A model that follows
it meets row 2's `ask`, a question to a person in a run that promised none.
This work makes row 5's deny under the press name no `[worktree-ok]` and ask
for no confirmation, and leaves its verdict, its attended text and every other
row as they are.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | Verification through an automated workflow is the first goal. A hint that leads an unattended run to a person's prompt spends that goal for nothing |
| `skills/implement/SKILL.md` *1. Read the spec before the code* | Once the routing batch is answered, the session runs to the pull request and nothing comes back mid-run. A guard's reason that tells the model to get the user's confirmation contradicts that under `Automation` `yes` |
| `docs/worktree-guard-spec.md` *B. Worktree creation* | The single-stream row reads *deny, steering to `git switch`; `[worktree-ok]` in a retry reaches the row above*. The row's verdict stays a deny. What the row says under the press is a rule change below |
| `docs/worktree-guard-spec.md` *Choice sites*, the paragraph *Under the press* | Under the press no choice-site reason names a question tool, `[worktree-ok]` or `[shared-tree-ok]`, and each says re-issuing the command unchanged meets the same refusal. Row 5 is not a choice site, so that sentence does not reach it today; this work extends the same register to row 5 under the press |
| `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/questions.md` Q1 | Answered 2026-10-28 by the owner, (b): #920, *the fix to two `[worktree-ok]` hints of `hooks/worktree-guard.py#steer_to_switch`*, stays in 0.24.0 and is fixed before #1049 decides whether the guard stays, narrows or goes. This is the answer to the issue's *What to decide*: yes, the decision on #903 extends to row 5's hints (read) |
| `v0.21.1:seal/specs/1791852612-under-automation-a-creation-in-another-clone-asks-nobody/spec.md` *The class* | #903's frame kept row 5 *unchanged*, relying on its steer to `git switch` as the way on in another clone's single-stream tree. This work keeps that steer and changes only what follows it (read) |
| `v0.21.1:seal/specs/1791852612-under-automation-a-creation-in-another-clone-asks-nobody/rounds/round-2.md` | Row 5's hints were deferred to #920 by that round, out of its scope (read, `:22` and `:76`) |
| `CONTRIBUTING.md` *What a change to a gate must carry* | A test seen red, a failure direction, a prompt budget, platform honesty and what the work removes. Each is answered under *Scope* and `## Removes` |
| `docs/the-reader-registry.md` *A frame names what its work removes* | The `## Removes` table below |
| `skills/agent-contract/SKILL.md` rules 12, 14, 15 and 19 | The class is enumerated under *Scope*; the text a model reads is pinned in both languages; each new case is seen red at the base `977b6613`; every comment stating the old fact is rewritten in place |

## Scope

### In

**Under the press, row 5's deny names no `[worktree-ok]` and asks for no
confirmation, on every attempt, in both languages.** The verdict stays
`deny`. The reason is built from four parts in this order:

1. `plain_origin`, the origin without `judge_creation`'s quote note, as rows
   3 and 4 already open under the press. The note tells the model to append
   `[worktree-ok]` or re-issue once the quote is closed, so it goes under the
   press whether or not the command parses.
2. The single-stream situation as it reads attended: *No other session is
   working in this tree (= single-stream). Rule: ...* in English, and its
   Korean text, unchanged.
3. The three switch command lines `steer_to_switch` prints today, with the
   same `git` or `git -C <top>` command word (`git_at`), unchanged.
4. `press_sentence()` followed by `reissue_sentence()`, the two shared
   strings every deny under the press already carries. They stand where the
   attended text has *If this genuinely is concurrent work needing
   separation, state why and get the user's confirmation first (if the user
   already asked for a worktree, retry with [worktree-ok] in the command).*

The English reason, for a creation `git -C <other> worktree add ../wt f` issued
from the session's own clone, reads exactly:

```
Attempting to create a worktree with `git worktree add`.
No other session is working in this tree (= single-stream). Rule: for single-stream work, don't create a worktree — just switch branches in the shared tree. Everything stays visible in one editor window, and half-used worktree folders don't pile up.

  git -C <other> fetch origin
  git -C <other> switch -c <branch> origin/main   # new branch
  git -C <other> switch <branch>                  # existing branch

This session's person pressed `automation` on the routing question, so this guard puts no question to them, and none is to be put to them in its place.

Re-issuing this command unchanged meets this same refusal.
```

The Korean reason is the same four parts from their existing Korean strings.
No new sentence is written in either language.

**The press is read inside row 5, from the session's own root**, with
`automation_pressed(repo_paths(cwd)[0], session_id, transcript_path)`, the
reader rows 3 and 4 use, and only once rows 1 to 4 have not fired. Row 0
reads the press as consent in the clone it was given in, so under the press
row 5 is reached only in another clone where this session holds no record,
exactly as rows 3 and 4 are.

**Attended, row 5 is byte-identical to the base**, the quote note and the
confirmation sentence included.

**Every comment and docstring that states the old fact is rewritten in
place** (contract rule 19): the module docstring's creation ladder and its
*Under the press* paragraph (`hooks/worktree-guard.py:67-72`, `:91-104`), the
comment above `elsewhere` (`:1819-1835`), the comment above row 5's deny
(`:1926-1927`), the comment above `plain_origin` (`:2013-2016`), and the
docstrings of `test_an_unbalanced_quote_under_the_press_names_no_token` and
`test_the_transcript_is_read_at_most_twice_per_creation` in
`tests/hooks/test_worktree_guard.py`.

### The class (contract rule 12)

Every text a model reads in the creation direction under the press, checked
against `hooks/worktree-guard.py` at `977b6613` (read; the token's string
sites found with `grep -n "worktree-ok"`, executed):

| Site | Names `[worktree-ok]` under the press today | This work |
|---|---|---|
| Row 0, consent | never reached as a deny: allow or silent | unchanged |
| Row 1, ACTIVE session, `ask` (`:1753-1773`) | no; its text names no token | unchanged; it is still a question to a person, #903's P1, out of scope below |
| Row 2, `[worktree-ok]` given, `ask` (`:1788-1817`) | yes, through `steer_to_switch` at `:1815`, but only after the model wrote the token itself; it is the prompt the hints lead to, not a hint | unchanged; P1 of `frame/questions.md` |
| Rows 3 and 4, `choose` (`:1857-1924`) | no, since #903: `plain_origin` and `elsewhere`; the fallback with `steer_to_switch` at `:1889` is never reached under the press | unchanged |
| Row 5, single stream, the steer (`:1928-1944`, `steer_to_switch` at `:1382-1395`) | **yes**, the sentence at `:1387-1389` and `:1393-1394` | **replaced under the press** by `press_sentence` and `reissue_sentence` |
| Row 5, the origin's quote note (`judge_creation`, `:2017-2028`) | **yes**, where the command does not parse cleanly | **dropped under the press**: row 5 opens with `plain_origin` |
| The Agent or Task path | no token; silent under the press in the session's own clone | unchanged |
| Every other entry to the ladder: `judge_creation`'s five call sites in `main` (`:3123`, `:3163`, `:3169`, `:3340`, `:3488`) | all reach row 5 through `guard_worktree_creation` | covered by the one change |

The switch direction's options name `[worktree-ok]` at `:3316-3325`, and
`choose` returns before reading them under the press (`:1558-1559`); the
switch steer `split` names none. The switch direction is outside #920 and
holds no instance.

### Failure direction, prompt budget, platform

- **Failure direction: neither.** The verdict at row 5 is `deny` before and
  after, in every state. Only the reason's text changes, and only under the
  press.
- **Prompt budget.** Under the press, row 5 stops pointing at a path that
  ends in a person's prompt: a model that followed either hint met row 2's
  `ask` once per retry, and after this work no reason in the creation
  direction names the token. Attended, unchanged. Nothing is added.
- **What the transcript costs.** A creation that reaches row 5 now reads the
  transcript twice, once at row 0 for the creation's clone and once at row 5
  for the session's own root, the bound rows 3 and 4 already hold. S5 counts
  it.
- **Platform.** On Windows every tree reads *detection unusable* and takes
  row 4 (`docs/worktree-guard-spec.md` *Known limits*), so row 5 and this
  change are never reached there. The new cases stub `sessions_in_tree` and
  run on every platform.

### Out, each with why

- **Row 2's `ask` under the press.** A model can still write `[worktree-ok]`
  from what it read elsewhere, the READMEs included, and row 2 then asks a
  person. Changing that is a verdict change, not a hint; the owner scoped
  #920 to the hint, and the guard's future is #1049's. P1 of
  `frame/questions.md`, default unchanged.
- **Row 1's `ask` under the press in another clone.** #903's P1, still open
  in `v0.21.1:seal/specs/1791852612-under-automation-a-creation-in-another-clone-asks-nobody/questions.md`;
  its text names no token, so #920's class does not hold it.
- **The attended texts.** The token is the attended single-stream deny's
  documented way past (`README.md:282`, `README.ko.md:274`); removing it
  there changes what a person at the keyboard can do, which #920 does not ask.
- **Whether the guard stays, narrows or goes.** #1049, in 0.24.1.
- **`README.md` and `README.ko.md`.** Neither describes row 5's text, and
  each sentence about it stays true: row 5 under the press was a deny before
  and is one after. #1102 rewrites both later in this release.
- **The language reading in `hooks/worktree-guard.py`.** #1096, after this
  work, edits the same file; nothing here touches `tr` or `SPECSEAL_LANG`.

## User scenarios & acceptance *(mandatory)*

Every case lives in `tests/hooks/test_worktree_guard.py`, beside #903's
creation cases, and uses that file's `judge`, `other`, `creation`, `wko`,
`write_transcript`, `ask_entries`, `assert_names_nobody`, `no_create_marker`
and `no_record` helpers. *Single stream* is the session count
`([], [], True)`.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1, row 5 under the press | Given this session's press in its own clone and a single-stream tree in another clone where it holds no record, when `creation(other)` is judged three times in each language, then each attempt is `deny` with the reason *In* gives word for word, `assert_names_nobody` holds, and neither a choice marker nor a consent record is written | a new case; seen red at `977b6613`, where the reason ends with the sentence naming `[worktree-ok]` |
| S2, an unbalanced quote under the press | Given S1's state, when `creation(other, "  # don't")` is judged twice in each language, then each attempt is S1's reason word for word, with no quote note | a new case, or S1 parametrised over the two commands; seen red at `977b6613`, where the first line names `[worktree-ok]` |
| S3, attended row 5 unchanged | Given no press, when `creation(other)` and `creation(other, "  # don't")` are judged in each language, then the reason is the base's: the origin, the quote note on the second command only, the situation, and `steer_to_switch`'s text ending with the sentence naming `[worktree-ok]` | a new case pinning the attended text in both languages; green at `977b6613` by design, and seen red by forcing the pressed arm on for every session |
| S4, the token still reaches its own row | Given S1's state, when `creation(other, "  # [worktree-ok]")` is judged, then the decision is row 2's `ask` | the existing `test_the_token_still_reaches_its_own_row`, unchanged and green |
| S5, the transcript is read at most twice | Given the four states of the existing case, when each creation is judged, then the reads are `[1, 2, 2, 2]`: the third state, row 5 in the other clone under the press, now reads the press | `test_the_transcript_is_read_at_most_twice_per_creation`, its pin and docstring rewritten; red at `977b6613`, which reads `[1, 2, 1, 2]` |
| S6, the press's own clone | Given the press in the creation's own clone, when a single-stream creation is judged, then row 0 allows it and row 5 is never reached | the existing `test_the_press_for_a_creation_is_read_from_the_sessions_own_root` and #903's own-clone cases, unchanged and green |

## Data & interfaces

- `hooks/worktree-guard.py#guard_worktree_creation`, row 5: reads `pressed`
  as rows 3 and 4 do, sets `lead = plain_origin if pressed else origin`, and
  ends the reason with the switch command lines, then `"\n\n"`, then
  `press_sentence() + reissue_sentence()` where pressed, or with
  `steer_to_switch(git)` where not. No parameter of the function changes.
- `hooks/worktree-guard.py#steer_to_switch`: its output for every caller is
  unchanged. The three command lines become reachable without the
  confirmation sentence; how is W1 of `frame/questions.md`.
- `hooks/worktree-guard.py#judge_creation`: no change to its code; the
  comment above `plain_origin` names row 5 beside rows 3 and 4.
- No new file, no new reader of any input, no change to
  `hooks/worktree_consent.py`, `hooks/hooks.json` or any template.

## Rule changes

- change
  file: docs/worktree-guard-spec.md
  section: B. Worktree creation
  from: deny, steering to `git switch`; `[worktree-ok]` in a retry reaches the row above
  to: deny, steering to `git switch`; `[worktree-ok]` in a retry reaches the row above.
    Under the press this row is reached only in a clone the press was not
    given in and this session has created no worktree in, and there its
    reason names no `[worktree-ok]` and asks for no confirmation
    (*Choice sites*, *Under the press*)
- change
  file: docs/worktree-guard-spec.md
  section: Choice sites
  from: `[shared-tree-ok]` still turns the switch rows silent and `[worktree-ok]` still reaches its `ask` above the creation rows. Without the press all four rows are as above.
  to: `[shared-tree-ok]` still turns the switch rows silent and `[worktree-ok]` still reaches its `ask` above the creation rows.
    The creation's single-stream row is reached under the press only in
    that same other clone, and keeps its deny and its steer to `git switch`
    there. Its reason opens with the origin without the quote note.
    Attended, it ends by asking for the user's confirmation and naming
    `[worktree-ok]`; under the press it ends with the press sentence and the
    re-issue sentence instead, so no reason in the creation direction names
    `[worktree-ok]` under the press. Without the press the four choice rows
    and the single-stream row are as above.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sentence asking for the user's confirmation and naming `[worktree-ok]`, from row 5's deny under the press | `hooks/worktree-guard.py#guard_worktree_creation` | Attended, `steer_to_switch` keeps it. Under the press `press_sentence` and `reissue_sentence` stand in its place, because nobody is at the keyboard to confirm and the retry it names reaches row 2's `ask` |
| The quote note naming `[worktree-ok]`, from row 5's origin under the press | `hooks/worktree-guard.py#judge_creation` | Attended, the origin keeps it. Under the press row 5 opens with `plain_origin`, as rows 3 and 4 do since #903 |
| The pin `[1, 2, 1, 2]` | `tests/hooks/test_worktree_guard.py#test_the_transcript_is_read_at_most_twice_per_creation` | Rewritten as `[1, 2, 2, 2]`: row 5 now reads the press, and the bound of two reads per creation that the case names still holds |
| The comments and docstrings saying only rows 3 and 4 name no token under the press | `hooks/worktree-guard.py#judge_creation`, `hooks/worktree-guard.py#guard_worktree_creation`, the module docstring, and `tests/hooks/test_worktree_guard.py#test_an_unbalanced_quote_under_the_press_names_no_token` | Rewritten in place to name row 5 as well (contract rule 19) |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.
