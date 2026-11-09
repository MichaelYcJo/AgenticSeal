# Review round 4: 1794200906-settings-are-read-as-json

```seal
target: b0d01da81, fixes eb03b4d7c..b0d01da81
```

This is a verifying round over the fix made after the sealer withheld at `18fec3619` (`guarantee.md:39`). The range holds one commit, `b0d01da81`. It rewrites the exit code of `seal pr-body` in `changelog.md:4` and `:10`, the quote at `pr.md:8`, `README.md:105-109`, `README.ko.md:108-112`, `templates/setup/config.md:46-51`, `frame/plan.md:11` and `:54`, `frame/design.md:61` (S3) and the `lib/config.py` docstrings at `:41-42` and `:125-127` (executed `git diff eb03b4d7c..b0d01da81`). Round 3 recorded no finding, so no closed finding is owed a `confirms:` line here. The code this round reviewed is that range. Beside that bound, it read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `b0d01da81`. No `pr.<lang>.md` stands, and both language keys of `seal/config.json` read `English`, so none is owed. Every `seal` and `bin/test` command this round ran is the clone's own at `b0d01da81`, never the installed 0.36.0 plugin.

No exit code is carried from an earlier round. Rounds 1 to 3 carried the five-command list without running `seal pr-body` (`round-1.md:265`, `round-3.md:9`), so this round ran every command whose exit a text states. One fact is carried: the weighing in rounds 1 and 3 of the twelve test-pin notices at `frame/design.md:358` and `:477`. Those two operations are unchanged in the range, since the range touches `frame/design.md` at line 61 alone (executed `git diff`).

## Findings

None. Every exit code the rewritten texts state matches what the tree's `bin/seal` does, no text in the tree still groups `seal pr-body` with exit 2, and the places the fix left alone are true.

## Confirmations

What matched: the exits on an unconverted `config.md` (executed). The probe repository's `seal/` held a README opening with the marker, a `config.md` table with `Policy root` `policies` and `Reference specs` `refs`, a `pact.md` and a work item with `pr.md` and `gaps.md`. `seal gate --base HEAD`, `seal fold`, `seal pact` and `seal mode --check` each exited 2 and printed `lib/config.py#unconverted_config`'s sentence, which ends "run `seal mode` once, which writes config.json from that table and removes config.md". `seal pr-body <item> --body <file>` exited 1, with and without `--check`. Each printed that same sentence after `refused: seal/config.json:` and wrote no body. `seal rules --check` exited 0 with "all 0 check lines in 0 rule files hold", although `policies/a.md` holds a `check:` line whose target is absent. After bare `seal mode` converted the table and exited 0, the same command exited 1 naming `policies/a.md:6`. So it had read the default policy root before the conversion. `seal settle --released-at HEAD` and `seal unverified` exited 0 and refused nothing. `lib/config.py#policy_root` (`:364-379`) and `#reference_roots` (`:294-337`) read a refusal as the default (read).

What matched: the exits on a `config.json` that will not parse (executed). In the same repository, `seal/config.json` was rewritten with a trailing comma. `seal gate`, `seal fold`, `seal pact`, `seal mode --check` and bare `seal mode` each exited 2. Each named "line 6 column 28", which is what `frame/plan.md:11` says they name. `seal pr-body` exited 1 with and without `--check`, printing the same sentence. `seal rules --check` exited 0 reading 0 rule files, and `seal settle --released-at HEAD` and `seal unverified` exited 0.

What matched: each sentence the range rewrote states what those runs gave. These are `changelog.md:4` and `:10`, `pr.md:8`, `README.md:105-109`, `README.ko.md:109-112` ("종료 코드 2 로 멈추고", then "`seal pr-body` 는 같은 문장으로 거절하고 종료 코드 1 로 끝납니다"), `templates/setup/config.md:46-51`, `frame/plan.md:11` and `:54`, and `frame/design.md:61` (read against the runs above). The S3 case pins exit 1 for all three unreadable shapes (`tests/skills/test_pr_body.py:1095-1114`, read). `lib/config.py:41-42` says `seal pr-body` "exits 1 on every refusal". This was weighed against `skills/code-review/scripts/pr_body.py:101-107`. That *Exit* section names exit 1 "refused and nothing written", and exit 2 "the arguments are unusable, `<item>` is not a directory". So the docstring states the script's own contract. A case name, `test_refuses_an_item_that_is_not_a_directory_at_exit_2` (`tests/skills/test_pr_body.py:1354`), calls the second exit a refusal. That name is read by whoever next edits the case and by no party at a step, so it is no finding.

What matched: no text groups `seal pr-body` with exit 2 (executed). The search split every file `git ls-files` lists into paragraphs. It listed each paragraph that holds `pr-body` together with "exit 2", "exits 2", "exit code 2", "exit status 2" or "코드 2". Other work items' records were left out, since each states its own commit, and so were this item's round records and `guarantee.md`, which state their targets. Each hit was read. Two kinds name exit 2 for another command: `seal gate` on an absent `Broad gate` key (`lib/config.py:6-7`, `templates/setup/config.md:28`, `skills/config/SKILL.md:65`), and `seal pact` (`frame/plan.md:30`, `docs/running/what-a-script-gates.md:64`). The other kind is the rewritten sentences above. The method covered every tracked file. The spellings it searched for are a sample, and a statement worded another way, such as "exits with status two", is beyond what it reached.

What matched: the places the fix left alone are true. `templates/setup/config.md:57-60` names `seal fold`, `seal gate`, `seal mode`, `seal pact` and `seal pr-body` as refusing an unconverted `config.md` and naming `seal mode`. Each printed the sentence that names it (executed, above). Bare `seal mode` converts rather than refuses, and the paragraph's next sentence says so at `:60-62`. A switch, `seal mode local` or `seal mode shared`, refuses through `skills/implement/scripts/seal.py#mode_refusal` (`:2188-2198`, `:2365-2368`, read). `skills/implement/bootstrap.md:122-123` says `seal gate`, `seal pr-body` and every other command that refuses an unreadable config refuses one that no longer parses. It names no exit code, and the second probe bears it out. `skills/config/SKILL.md:107-111` sends the reader to `templates/setup/config.md` for which commands print and stop and which read defaults, and `:46-51` there now says it truly. `frame/plan.md:25` (A9) says five commands refuse an unconverted file, and each did. The *Rule changes* `to:` texts at `frame/design.md:260-263` and `:327-330` say every reader that refuses an unreadable file refuses a lone `config.md`, and that the readers of `Policy root` and `Reference specs` read it as no file. Both runs bear that out.

What matched: `pr.md`'s nine quotes each stand in `changelog.md`, word for word with runs of whitespace collapsed. That includes the rewritten quote at `pr.md:8` of `changelog.md:10` (executed: a substring check, 9 of 9 found).

What matched: the whole read of the seven records against `b0d01da81` found no other sentence the target contradicts (read). `gaps.md` keeps its one `## Not verified` row open, and the range does not touch it.

What matched: the modules that read the rewritten texts pass at `b0d01da81`: `bin/test -q tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/lib/test_config.py tests/skills/test_pr_body.py`, exit 0, 312 passed and 7 skipped (executed). This is a probe of six modules, not the suite.

What matched: `chain_check.py` over the worktree, before this record, prints the same twelve test-pin notices at `frame/design.md:358` and `:477` that rounds 1 to 3 weighed, and no new one (executed). Quoted, one of them: "a test pins text this operation takes out of `docs/running/the-broad-gate.md`: `tests/lib/test_tables.py:441` holds "| Item | Value |", and the `to` does not". Round 1 weighed these pins as walker fixtures and corpus shape names, not a rule's wording (`round-1.md:277`). That weighing is carried, and none of the twelve is a finding. The run also says a verifying round is owed for `b0d01da8`, which this record is. It says the gate record and the guarantee are behind HEAD.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The whole suite, the repository-wide lint and the format check at `b0d01da81` (`unverified`); this round ran only the six modules in *Probes* | the branch at `b0d01da81` | the orchestrator, through this worktree's own `bin/seal gate`, then the sealer's new spawn |
| Whether `frame/questions.md` Q1's default (no converter for `parity.md`, the signer table and `pact-paths.md`) is the owner's answer | `seal/threads/1794200906-settings-are-read-as-json/frame/questions.md` Q1 | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/seal gate --base HEAD`, `fold`, `pact`, `mode --check` in a scratch repository whose `seal/` holds an unconverted `config.md`, `pact.md` and an origin remote | each exit 2, printing the sentence that names `seal mode` |
| `bin/seal pr-body seal/threads/1-x --body <file>`, with and without `--check`, in the same repository | each exit 1, "refused: seal/config.json: is not there, and the config.md beside it ..."; no body written |
| `bin/seal rules --check`, `settle --released-at HEAD`, `unverified` in the same repository; then bare `bin/seal mode`, then `rules --check` again | exit 0 ("all 0 check lines in 0 rule files hold"), 0, 0; `mode` exit 0, `config.json` written, `config.md` removed; `rules --check` exit 1 naming `policies/a.md:6` |
| `bin/seal gate --base HEAD`, `fold`, `pact`, `mode --check`, `mode` with `seal/config.json` ending in a trailing comma | each exit 2, naming "line 6 column 28" |
| `bin/seal pr-body`, with and without `--check`, `rules --check`, `settle --released-at HEAD`, `unverified` on the same file | `pr-body` exit 1 both ways, with the same sentence; `rules` exit 0 reading 0 rule files; `settle` and `unverified` exit 0 |
| a paragraph search of every `git ls-files` path for `pr-body` with an exit-2 spelling | no paragraph groups `pr-body` with exit 2 |
| a whitespace-collapsed substring check of `pr.md`'s quotes against `changelog.md` | 9 of 9 found |
| `bin/test -q` over the six modules named above, in the clone | exit 0, 312 passed, 7 skipped |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.37.0 --worktree` in the worktree, before this record | exit 0; the twelve notices at `frame/design.md:358` and `:477`; a verifying round owed for `b0d01da8`; the gate record and the guarantee behind HEAD |
