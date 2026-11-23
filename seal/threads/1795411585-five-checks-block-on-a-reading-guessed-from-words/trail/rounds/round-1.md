# Review round 1: 1795411585-five-checks-block-on-a-reading-guessed-from-words

```seal
target: 525374339 against origin/release/v0.38.6
```

This is the first round, so no earlier round carries a coordinate or a close. The round read issue #1572, `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `525374339`, the four phase records, and the diff `origin/release/v0.38.6...HEAD` whole. The work item holds no `pr.<lang>.md`, and `seal/config.json` names English for both language keys, so none is owed. The repository declares no `seal/parity.json`.

Facts carried from the frame and not re-established here: the shape of what `gh api -i` prints for a missing and a present release or issue, and for a host that does not resolve (`frame/design.md` G10, the framer's probe with gh 2.92.0); that `7da1a77e9` is first tagged `v0.24.0` (G4); that G9's search lists every line of shipped `.py` code that reads `stderr`. The round re-ran no network call against GitHub.

## Findings

### 1. `skills/verify/SKILL.md` still tells the agent that a disagreement with CI is no permission to keep the row, which the rewritten paragraph above it now grants

```seal
severity: should
location: `skills/verify/SKILL.md:237-240`
evidence: read `skills/verify/SKILL.md:205-240`, `skills/verify/scripts/deferral_check.py:24-27`, `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/frame/design.md:32`; executed `git grep -n -e "permission to keep the row" -- ':!seal/threads'`, which printed `skills/verify/SKILL.md:240` alone
```

Why it matters: the section is what a session reads before it writes an `unverified; CI covers it` row, and its two paragraphs now give opposite instructions for the case the issue names. *Scope* item 4 rewrote `:229-235` to say that a kind with no matching line "is not a finding that nothing runs it, so open the CI files and read what they run". The next paragraph, `:237-240`, was left as it stood at the base: "a runner reached through a composite action, a reusable workflow, or a script it cannot see reads as absent. Disagreement with what CI really does is a finding about this tool, not permission to keep the row." That sentence stood on the old exit 1, which `:227-228` at the base read as "the row about to be written is not true". Under the new paragraph, an agent that opens the CI files and finds `./run-suite` running the suite may keep the row; under the old sentence it may not. `deferral_check.py:24-27` now says the same as `:229-235`: "a kind no line matched is no finding that nothing runs the check: the agent writing the row opens the CI files for what they run". `frame/design.md` G2 asks the change to remove what stood on the old fact in the same commit.

The build's account names no search for other statements of `seal deferrals`' exit-1 verdict beyond the frame's search 5, which is keyed to the words the build removed (`trail/phases/phase-2.md:136`). This sentence is in the section the diff rewrote. The round's own list was made by `git grep -n -i "seal deferrals\|deferrals\b" -- ':!seal/threads' ':!tests' ':!evals'`, which lists every place that names the command. It printed this section, `README.md:407`, `README.ko.md:404` (finding 2), `docs/running/what-a-script-gates.md:65`, which the design's `## Rule changes` rewrites at the settle, and `skills/implement/scripts/seal.py:136-139`. A statement of the fact that does not name the command is outside that list.

The fix replaces the paragraph's last sentence. No case pins either wording (executed: the `git grep` above).

```markdown
It reads command text rather than a YAML graph, so a runner reached through a
composite action, a reusable workflow, or a script it cannot see reads as
absent. Where the CI files run the check by a path the words miss, the row
stands on what the agent read in them, and the miss is a finding about this
tool.
```

```seal
verdict: fixed 031807642
answer: The finding holds: the sentence stood on the old exit 1 and refused the row the paragraph above it now lets stand. The paste-ready sentence replaces it as given, after a read against `frame/design.md` *Scope* item 4 and `deferral_check.py`'s docstring, which say the same; the trigger paragraph above still binds a file the agent reads. `git grep -n "permission to keep the row" -- ':!seal/threads'` now prints nothing, and no case pinned either wording.
```

### 2. Both READMEs still say `seal deferrals` tells whether anything runs the check, and the frame keeps them out of scope on the claim that they state no verdict

```seal
severity: should
location: `README.md:407`, `README.ko.md:404`, `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/frame/design.md:41`
evidence: read `README.md:405-407`, `README.ko.md:402-404`, `skills/verify/scripts/deferral_check.py:207-214`, `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/frame/design.md:41`; executed `git grep -n -e "says whether anything here runs" -e "돌리는 것이 있는지" -- ':!seal/threads'`, which printed the two README rows alone
```

Why it matters: the commands table is where a person learns what a command answers. `README.md:407` says the command "says whether anything here runs the check an `unverified` row defers, and names each CI file that does". `README.ko.md:404` says the same. The new `headline` in `deferral_check.py:207-214` has the docstring "what its words matched, and never whether anything runs the check", and the command now exits 0 on every reading. A person who reads the README row and then sees `tests: no CI or hook line matched a runner word` reads it as "nothing runs the suite here", which is the reading the issue removes.

The frame rules the two rows out of scope at `frame/design.md:41`: "Neither states an exit code or a verdict, and the issue names neither." The first half does not hold at the target. "says whether anything here runs the check" is the verdict that `deferral_check.py:24-27` and `skills/verify/SKILL.md:229-232` now say the command does not give. The issue does not name the README, but its *Direction* is that the reading is reported and not used to decide, and G2's clause asks the change to remove what stood on the old fact.

`skills/implement/scripts/seal.py:138` and `deferral_check.py:2` describe the command as "resolve the answerer named in an `unverified` row". `skills/verify/SKILL.md:213` uses the same verb for the agent's own act ("Resolve the answerer before writing the row"), so the round does not count them in this finding. The fix pass may weigh them with it.

The fix rewrites both rows and turns the out-of-scope bullet into a *Scope* sentence. No case pins either row (executed: the `git grep` above).

```markdown
| `seal deferrals . [--kind all]` | names each CI file and hook line a runner word matches for the check an `unverified` row defers, and exits 0 whatever it matched; whether anything runs the check is read in the files it names (`skills/verify/SKILL.md` *The answerer has to exist*) |
```

```markdown
| `seal deferrals . [--kind all]` | `unverified` 행이 미뤄 둔 검사의 실행기 단어에 맞는 CI 파일과 훅의 줄을 하나씩 짚고, 무엇이 맞든 0 으로 끝난다. 그 검사를 실제로 돌리는지는 짚은 파일을 열어 읽는다 (`skills/verify/SKILL.md` *The answerer has to exist*) |
```

In `frame/design.md`, the bullet at `:41` goes, and *Scope* item 4 gains a closing sentence:

```markdown
`README.md` and `README.ko.md` say in their commands tables what the command names and that it exits 0, and neither says whether anything runs the check.
```

```seal
verdict: fixed d68add798
location: `README.md:407`, `README.ko.md:404`, `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/changelog.md`
answer: The finding holds, and its frame half went at 4b04fa3d6. Both README rows now say what the command names and that it exits 0. The paste-ready rows ended on whether anything runs the check being read in the files the command names, which misses the finding's own case: a suite run through a script leaves no file named. So each row sends the reader to the CI files themselves, in my words. The changelog's `### Fixed` entry for `seal deferrals` names the two rows and the `skills/verify/SKILL.md` sentence of finding 1, because the fragment is what the release note shows. `skills/implement/scripts/seal.py:138` and `deferral_check.py:2` and `:220` are left as they stand: "resolve the answerer named in an `unverified` row" names the act the command serves, the verb `skills/verify/SKILL.md:213` gives the agent, and claims no verdict. No case pinned either row.
```

### 3. `frame/design.md` *Scope* item 2 says the headline and the closing sentence name the composite action, the reusable workflow and the script, and neither does

```seal
severity: should
location: `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/frame/design.md:30`
evidence: read `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/frame/design.md:30`, `skills/verify/scripts/deferral_check.py:96-101`, `skills/verify/scripts/deferral_check.py:207-253`, `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/trail/phases/phase-2.md:52-64`, `tests/skills/test_deferral_check.py:70-73`
```

Why it matters: the sealer reads the frame's *Scope* against the tree, and a sentence there that says what the work does and that the target contradicts sends it to look for output that is not there. `frame/design.md:30` says: "The headline for a kind with no matching line and the closing sentence say that no CI or hook line matched a runner word for that kind, and that a runner reached through a composite action, a reusable workflow or a script reads as absent." At the target, the headline says `no CI or hook line matched a runner word`, or `no CI line matched a runner word` where only the hook matched (`deferral_check.py:207-214`). The closing sentence says `No CI line matched a runner word for <kinds>. Open the CI files and read what they run before deferring <kinds> to CI.` (`:247-252`, pinned at `tests/skills/test_deferral_check.py:70-73`). Neither names the composite action, the reusable workflow or the script. The `limit:` line does, from `KNOWN_LIMITS` at `:96-101`, which every run prints. `trail/phases/phase-2.md:52-64` records this choice ("the closing sentence and the `limit:` line ... carry the rest"), and the `frame:` commit `2c0c21552` that folded phase 2 left the *Scope* sentence as the framer wrote it.

The fix touches the work item's records alone.

```markdown
2. **`seal deferrals` reports and exits 0 on what it read.** `deferral_check.py#main` exits 0 whenever it read the path, and 2 only where the path or the arguments are unusable. The `nothing runs it` line goes. The headline for a kind with no matching line says that no CI or hook line matched a runner word for that kind, or that no CI line did where only the pre-commit hook matched. The closing sentence says that no CI line matched for the kinds it names and asks the reader to open the CI files and read what they run. The `limit:` line, printed under every run, says that a runner reached through a composite action, a reusable workflow or a script it cannot see reads as absent. None of them says nothing runs the check. The module docstring's outcomes and exit codes say the same. The cases of `tests/skills/test_deferral_check.py` that assert exit 1 assert exit 0 and the new lines (contract rule 14).
```

```seal
verdict: fixed 4b04fa3d6
answer: The finding holds. *Scope* item 2 now says what the headline and the closing sentence print, and that the `limit:` line printed under every run names the composite action, the reusable workflow and the script, in the words the finding gave. The fix touches the work item's records alone, so the sealer reads it.
```

## Confirmations

What matched: each of *The five* in issue #1572 now reads an exact fact or reports. `release_exists` and `_issue_api` decide on the status `lib/gitcmd.py#http_answer` reads from `gh api -i` (`.github/scripts/publish_release_note.py:445-451`, `.github/scripts/close_issues_on_release.py:143-149`, `lib/gitcmd.py:214-230`), and no line of shipped code decides on stderr's words (executed: search 4 printed nothing). `seal deferrals` returns 0 after every reading and 2 only from its usage refusals (read: `deferral_check.py:217-253`). `seal pact` holds no token loop (read: `pact_check.py:778-792`). The near-miss sweep warns and passes (read: `tests/behaviour/test_a_cited_section_stands_in_its_file.py:1326-1342`). The batch sweep is gone (executed: search 3 printed nothing; at `22803718e` it printed 19 lines, as `frame/design.md:65` says).

What matched: `frame/design.md` S10, S11 and S12 hold at the target (executed: search 1 printed `docs/layout/the-pact.md:110` alone, search 2 printed `docs/layout/the-pact.md:102` and `:109` alone, searches 4 and 5 printed nothing).

What matched: the phase records' red and mutation claims, re-run for two units in a `git clone --no-local` at `525374339` (executed). With the `status is None or` guard of `release_exists` turned into `status is not None and`, `Test_release_exists::test_refuses_any_other_status_and_no_status_by_exiting[no-http-answer]` failed. With `deferral_check.py#main`'s last `return 0` turned into `return 1 if unmatched else 0`, six cases of `tests/skills/test_deferral_check.py` failed. These are phase 1's and phase 2's claims at `trail/phases/phase-1.md:80-82` and `trail/phases/phase-2.md:119-120`.

What matched: the union in `deferral_check.py#RUNNERS` holds every command the old `session_cost.py#FAMILIES` `test` and `lint/type` patterns matched (read: the two lists at the base and at the target). Each old anchor, the start of the line or one of `\s`, `.`, `/` and `\`, is a place where `\b` holds before a word character, and every word of the old patterns has a fragment of its own or one of the two merged groups. So `trail/phases/phase-2.md:44-46`'s claim that neither reader loses a match holds.

What matched: `pr.md`'s two quotes stand word for word in `frame/plan.md:68` and `:69`, the cells its coordinates name (read). `changelog.md`'s statements match the target: the two headlines and the closing sentence it quotes are the strings at `deferral_check.py:207-252`; `pylint src` and `go vet` fell to `other` at the base, since no family's pattern held either word (read: `FAMILIES` at `origin/release/v0.38.6`); and the batch sweep's `BATCH_PHRASE` and `ASKING_WINDOW = 140` at the base are the phrase and the window the entry describes (read: `git show origin/release/v0.38.6:tests/behaviour/test_chain_hooks_hardening.py`).

What matched: the new cases read against their groups. `bin/seal layout --pairs` named one pair among the changed files, `Test_release_exists`'s two cases, whose class docstring says the world differs between them (executed). `tests/skills/test_deferral_check.py#Test_main.test_reports_a_suite_run_through_a_script_as_no_match_and_exits_0` prints the same lines as `test_reports_a_tree_with_no_ci_and_exits_0`, and its group's `test_workflows_that_run_no_tests_are_not_named` and `test_lint_matches_while_tests_do_not` hold most of what it asserts. It is the one case that pins the whole output for a tree whose workflow runs its suite through a script, which is the frame's S5, so the round opens no finding for it.

What matched: `gaps.md` labels the broad gate `unverified` and names the orchestrator, and names the repository owner for the CI runner's `gh` status line. Both labels are honest: no phase record claims the full suite, and no party here ran `gh` on the release workflow's runner.

`deferral_check.py:24-27` says a runner reached through "a script" reads as absent, where `RUNNERS` now holds `bin/test`, `scripts/test` and `test.sh`. The printed `limit:` line says "a script this cannot see", so what a session reads at run time is exact, and the docstring is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check over the tree at HEAD (contract rule 2) | `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/gaps.md:7` | the orchestrator, at the broad run after the rounds settle |
| Whether `gh api -i` on the release workflow's runner prints its status line as gh 2.92.0 did; this round carried the framer's probe and called no GitHub endpoint | `seal/threads/1795411585-five-checks-block-on-a-reading-guessed-from-words/gaps.md:8` | the repository owner, reading the publish job's log at the v0.38.6 tag |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/lib/test_gitcmd.py tests/github/test_publish_release_note.py tests/github/test_close_issues_on_release.py tests/skills/test_deferral_check.py tests/skills/test_session_cost.py tests/skills/test_pact_check.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_chain_hooks_hardening.py` | exit 0; 679 passed, 5 warnings, each a citation another work item's pending rule change excuses, and no near-miss warning |
| `bin/test -q tests/github/ tests/skills/test_payload_meter.py tests/skills/test_coordinates.py tests/skills/test_seal.py tests/behaviour/test_waiver_decided_at_start.py tests/test_censuses.py` | exit 0; 1170 passed |
| `uvx ruff check` and `uvx ruff format --check` over the 14 `.py` files the diff changes | exit 0 and exit 0 |
| `bin/seal mutate .github/scripts/publish_release_note.py`, the `status is None or` guard turned into `status is not None and`, `-k release_exists`, in the clone | red: the `no-http-answer` case failed |
| `bin/seal mutate skills/verify/scripts/deferral_check.py`, the last `return 0` turned into `return 1 if unmatched else 0`, in the clone | red: 6 failed, 27 passed |
| `bin/seal layout --pairs` over the seven changed test files that add cases | one pair, in `Test_release_exists` |
| `frame/design.md`'s searches 1 to 5 at HEAD, and search 3 at `22803718e` piped to `wc -l` | as S10, S11 and S12 state; 19 lines at `22803718e` |
| `bin/seal pr-body --body <scratch>/body.md` on the work item | exit 0; the body opens with `pr.md` and carries the changelog's three sections |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.6 --root <the branch worktree> --worktree`, before the record was written, with the installed plugin's script and with the tree's | exit 0 from each; it named the missing round record, `trail/gate.md` and `guarantee.md`, and printed no notice at a line of `frame/design.md` |
