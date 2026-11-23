# Review round 2: 1795411585-five-checks-block-on-a-reading-guessed-from-words

```seal
target: 70d02bd7a, fixes 525374339..70d02bd7a
```

This is the verifying round over round 1's fixes. The code read is the diff `525374339..70d02bd7a`. It holds the frame repair `4b04fa3d6`, the close of finding 3 `45da4dec2`, the crafter's two fixes `031807642` and `d68add798`, the fix pass's close blocks `afb8a4217`, and the frame fold `70d02bd7a`. It changes `skills/verify/SKILL.md`, `README.md`, `README.ko.md`, and the work item's `frame/design.md`, `changelog.md` and `trail/rounds/round-1.md`, and no `.py` file. Outside that bound, the work item's records were each read whole at `70d02bd7a`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, the four phase records and `trail/rounds/round-1.md`. No `pr.<lang>.md` stands, and `seal/config.json` names English for both language keys, so none is owed. The repository declares no `seal/parity.json`.

Carried from round 1 as coordinates and not re-established here, since the fix diff touches no code: the shape of what `gh api -i` prints (`frame/design.md` G10, the framer's probe), the tag `v0.24.0` as the first to hold `7da1a77e9` (G4), G9's list of every `stderr` read in shipped `.py` code, round 1's two `seal mutate` runs, and its reading that `deferral_check.py#RUNNERS` holds every command the old `session_cost.py#FAMILIES` patterns matched. Re-established here: each of round 1's three closes, the statements of `seal deferrals` across the tree, every `pr.md` quote, searches 1 to 5 of `frame/design.md`, and the narrow cases that read the documents the fix diff changes.

## Findings

None. Each close of round 1 holds. No unit the fix pass touched carries a new defect. No sentence of the work item's records is contradicted by `70d02bd7a`.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the last sentence of `skills/verify/SKILL.md` *The answerer has to exist* no longer refuses the row the paragraph above it lets stand. At `skills/verify/SKILL.md:237-241` it now reads "Where the CI files run the check by a path the words miss, the row stands on what the agent read in them, and the miss is a finding about this tool." That is round 1's paste-ready sentence word for word, as the close claimed. It agrees with `:229-235`, which sends the agent to the CI files, and with `deferral_check.py:24-27` (read). `git grep -n "permission to keep the row" -- ':!seal/threads'` prints nothing (executed). The paragraph still names the composite action, the reusable workflow and the script, which `KNOWN_LIMITS` at `deferral_check.py:96-101` prints under every run (read). `frame/design.md:32`, folded at `70d02bd7a`, says the section's last sentence "says what the reader does with what the CI files run", and it does. `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` pass over the rewrapped paragraph (executed).

```seal
confirms: round-1#2
```
What holds: neither README row says that the command tells whether anything runs the check. `README.md:407` now says the command "names each CI file and hook line a runner word matches for the check an `unverified` row defers, and exits 0 whatever it matched; whether anything runs the check is read in the CI files themselves". `README.ko.md:404` says the same in Korean: the lines of CI files and hooks that match a runner word, exit 0 whatever matched, and whether the check really runs is read by opening the CI files directly (read). The close claimed the rows depart from round 1's paste-ready text, which sent the reader to "the files it names". The departure holds: for a suite run through a script, `inspect` names no CI file (`deferral_check.py:184-204`, read), so the paste-ready row would have sent the reader to an empty list. The frame half is in place: the out-of-scope bullet that named the two rows is gone, and `frame/design.md:32` gains the sentence round 1 gave (read at `4b04fa3d6` and at the target). The changelog's `### Fixed` entry now names the two rows and the answerer section's last sentence, and each statement matches the tree (read: `changelog.md:4` against `README.md:407`, `README.ko.md:404` and `skills/verify/SKILL.md:237-241`). The close left `skills/implement/scripts/seal.py:138` and `deferral_check.py:2` and `:220` as they stand. Each says "resolve the answerer named in an `unverified` row", which names the act the command serves and claims no verdict (read). `tests/behaviour/test_both_editions_carry_the_same_folds.py` and `tests/behaviour/test_docs_line_wrap.py` pass over both editions (executed).

```seal
confirms: round-1#3
```
What holds: `frame/design.md` *Scope* item 2 now says what the target prints. The headline for a kind with no matching line is `no CI or hook line matched a runner word`, or `no CI line matched a runner word` where only the hook matched (`deferral_check.py:207-214`). The closing sentence names the kinds and asks the reader to open the CI files and read what they run (`:247-252`). The `limit:` line, printed under every run at `:246`, names the composite action, the reusable workflow and the script (`:96-101`). Each statement of `frame/design.md:30` was read against those lines at the target. The fix touched the work item's records alone, and the close says so.

What matched: the statements of `seal deferrals` across the tree agree with what it does. `git grep -n -i "seal deferrals\|deferrals\b" -- ':!seal/threads' ':!tests' ':!evals'` prints the two README rows, `docs/running/what-a-script-gates.md:65`, `skills/implement/scripts/seal.py:136`, `skills/verify/SKILL.md:216-217`, three lines of `deferral_check.py` and two comments of `session_cost.py` (executed). The row at `what-a-script-gates.md:65` is the one `frame/design.md` `## Rule changes` rewrites at the settle, and its `to` cell agrees with the new answerer section. A wider search, `git grep -n -i -e "CI covers it" -e "answerer has to exist" -e "runner word" -- ':!seal/threads' ':!tests' ':!evals'`, adds `skills/implement/orchestration.md:247` and `skills/verify/SKILL.md:323` (executed). Neither stands on the old exit 1 (read). A statement of the fact that names neither the command nor those words is outside both lists.

What matched: `frame/design.md` S10, S11 and S12 still hold at the target (executed: search 1 printed `docs/layout/the-pact.md:110` alone, search 2 printed `docs/layout/the-pact.md:102` and `:109` alone, searches 3, 4 and 5 printed nothing).

What matched: `pr.md`'s two quotes stand word for word at `frame/plan.md:68` and `:69`, the cells its coordinates name (executed: `grep -n -F` of each quote). `frame/plan.md` is unchanged since round 1's target. `seal pr-body` composes the body from `pr.md`, the changelog's three sections and the round records (executed).

What matched: `gaps.md` labels the broad gate `unverified` and names the orchestrator, and names the repository owner for the CI runner's `gh` status line. Both labels stay honest after the fix pass. The fix pass ran no case, and its close answers claim only a `git grep`, which this round re-ran.

`frame/plan.md:45` says phase 2 delivers *Scope* items 2, 3 and 4 and names `f167beb29`. The two sentences `4b04fa3d6` and `70d02bd7a` added to item 4 were delivered by `031807642` and `d68add798`, which round 1's close blocks name. The table states what each phase was built to deliver, and no reader acts on it to find the later commits, so the round opens no finding for it. In the same way, `frame/design.md` `## Removes` names `skills/verify/SKILL.md` and not the two README rows among the sentences that read the exit 1 as a verdict. The rows were rewritten rather than removed, and the changelog names them, so the pull request states the change.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check over the tree at HEAD (contract rule 2) | `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/gaps.md:7` | the orchestrator, at the broad run after the rounds settle |
| Whether `gh api -i` on the release workflow's runner prints its status line as gh 2.92.0 did; this round carried the framer's probe and called no GitHub endpoint | `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/gaps.md:8` | the repository owner, reading the publish job's log at the v0.38.6 tag |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/skills/test_deferral_check.py tests/text/test_a_document_has_room_for_the_next_fold.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_no_document_names_the_old_roots.py tests/skills/test_passages.py`, in a `git clone --no-local` at `70d02bd7a` | exit 0; 217 passed, 5 warnings, each a citation another work item's pending rule change excuses, and no near-miss warning |
| `frame/design.md`'s searches 1 to 5 at `70d02bd7a` | as S10, S11 and S12 state |
| `git grep -n -i "seal deferrals\|deferrals\b" -- ':!seal/threads' ':!tests' ':!evals'`, and the wider search under *Confirmations* | the lines listed there |
| `git grep -n "permission to keep the row" -- ':!seal/threads'` | nothing printed |
| `bin/seal pr-body --body <scratch>/body.md` on the work item, in the clone | exit 0; the body opens with `pr.md` and carries the changelog's three sections |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.6 --root <the branch worktree> --worktree`, with the installed plugin's script, before the record was written | exit 0; it named findings 1 and 2 as owing a verifying round, the missing `trail/gate.md` and `guarantee.md`, and printed no notice at a line of `frame/design.md` |
