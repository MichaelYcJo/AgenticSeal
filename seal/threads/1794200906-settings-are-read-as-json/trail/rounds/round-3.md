# Review round 3: 1794200906-settings-are-read-as-json

```seal
target: 64315ab6, fixes dc3bcba7..64315ab6
```

This is a verifying round over the fix pass for round 2. The range holds four commits. `4b99e2d3` rewrites plan row A9. `66b462d7` adds twelve operations to design *Rule changes* and one sentence to `gaps.md`. `1b04534c` adds one case to `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py`. `64315ab6` appends round 2's close blocks. The code this round reviewed is that range and nothing outside it. Beside that bound, it read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `64315ab6`. No `pr.<lang>.md` stands, and both language keys of `seal/config.json` read `English`, so none is owed. Every `seal` and `bin/test` command this round ran is the clone's own at `64315ab6`, never the installed 0.36.0 plugin.

Facts carried from round 2 and not established again: `changelog.md`, `pr.md`, `routing.md`, `frame/questions.md` and the code outside the one test file are unchanged in the range (executed `git diff --stat dc3bcba7..64315ab6`). So round 2's substring check of the nine `pr.md` quotes against `changelog.md` still holds, and it was not run again. Also carried: phase 4's claim that the 25 moved walker units equal the base's by `ast`, which round 1 left to the sealer, and the five commands that refuse an unconverted `config.md`, which round 2 established. This round re-read one of the five, `seal pact`, at `skills/verify/scripts/pact_check.py:688-694`. It returns 2 where `config.config_pairs` gives a refusal.

## Findings

None. All three round-2 findings hold as closed, and the range adds no defect this round found.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the A9 Verdict cell at `frame/plan.md:25` is round 2's snippet, byte for byte (executed: a `diff` of the snippet line against the cell). It names `seal gate`, `seal pr-body`, `seal fold`, `seal pact` and `seal mode --check` as the commands that refuse. `changelog.md:10`, `:15` and `frame/plan.md:11` and `:54` name the same five (read). The close claimed that no other line of the work item's records says every reader or every command refuses. This round's whole read of the seven records found none (read). One limit stands, and it is no finding. The cell cites "design Scope item 2 and S3", and `frame/design.md:37` and `:61` name four of the five commands between them. Neither names `seal pact`. The code refuses there anyway (`pact_check.py:688-694`, read), so the cell states what the tree does.

```seal
confirms: round-2#2
```
What holds: the twelve operations at `frame/design.md:645-719` and the `gaps.md:15` sentence are round 2's snippet, byte for byte (executed: a `diff` of each against the round-2 record). The fix pass claimed that a draft placed 112 of 113 operations. This round ran `bin/seal settle --draft --released-at HEAD` in the clone at `64315ab6`, and it printed "placed 112 of 113 operations in docs/". The one not placed is `seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md:226`, and its reason is that "the `from` text is not in section `The checks`" (executed). Each of the twelve `to:` texts stands once in the drafted `docs/`, at `docs/checks/the-pull-request-check.md:183-184` and `:213-216`, `docs/forms/the-guarantee.md:34`, `:36` and `:58`, `docs/layout/one-root-by-lifetime.md:232` and `:251`, `docs/layout/the-record-layout.md:117`, `:118` and `:125`, `docs/running/the-run.md:66` and `docs/running/what-a-script-gates.md:78` (executed `git grep -n -F` of a phrase from each). In the drafted `docs/`, `config.md` stands only in this item's converter sentences, at `docs/layout/one-root-by-lifetime.md:269` and `docs/layout/one-root-by-lifetime.ko.md:246`. The added lines that hold "row" or "행" name `routing.md` rows, among them the `Automation` row at `docs/running/the-run.md:57`, or the pact anchor's rows (executed `git grep` and `git diff -U0 -- docs` filtered, each hit read). The `gaps.md:15` sentence states the unplaced operation as the draft gives it, and that operation's `to:` names "`config.md`'s two language rows" (read `seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md:226-230`). The drafted `docs/` was restored with `git checkout -- docs` in the clone.

```seal
confirms: round-2#3
```
What holds: the case at `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py:452-467` is round 2's snippet, byte for byte (executed: a `diff`). At `64315ab6` the module and `tests/skills/test_chain_check.py` pass, 242 cases (executed). With `chain_check.py:1611` changed by the Edit tool to `f"{routing.optin.HOME}/{routing.optin.OLD_PARITY_CONFIG}"`, the new case alone fails, at `(line,) = refused`, with "not enough values to unpack (expected 1, got 0)". The other 241 pass (executed). So the case holds the line, and no other case of its group does. The line was then restored, and `git status` in the clone was clean (executed). `bin/seal layout --pairs` over the module reads "1 files read, 0 pairs", and `bin/seal layout --check` over it exits 0 (executed). The docstring claims a refusal at the old file's path under the root's own name, naming the file to write. The two asserts pin exactly that.

What matched: the range raises no new notice from `chain_check.py`. Run over the worktree before this record was written, it printed the same twelve test-pin notices at `frame/design.md:358` and `:477` that round 2 weighed, and none at `:645-719` (executed). Quoted, one of them: "a test pins text this operation takes out of `docs/checks/the-fold.md`: `tests/skills/test_broad_gate.py:1965` holds "a fence nobody closed", and the `to` does not". These are the notices round 2 read, and none is a finding. It also named round-2 finding 3 and commit `1b04534c` as owed a verifying round, which this record is.

The settling session should know one thing, and it is no finding of this range. The drafted `docs/running/what-a-script-gates.md` *The checks* holds table rows written across several lines: the `seal pr-body --check` row at `:76-80`, which 1794187229's operation (`seal/threads/1794187229-the-body-carries-the-seal-mark/frame/design.md:293-296`) writes over four lines, the `chain_check.py` row at `:56-64` and the `seal rules --check` row at `:68-70` (executed: the draft, then read). In GitHub's table grammar, each line of such a row renders as a row of its own. The twelfth operation of this range swaps one of those lines for two, inside a row that already renders broken. The settle's step 4 reads every section the draft wrote, and it is there that the rows are joined.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The whole suite, the repository-wide lint and the format check at `64315ab6` (`unverified`); this round ran only the two modules in *Probes* | the branch at `64315ab6` | the orchestrator, through this worktree's own `bin/seal gate` |
| Whether the 25 moved walker units equal the base's by `ast`, as phase 4 claims (carried from round 1, not re-run) | `lib/tables.py` | the sealer, where it samples the crafter's claims |
| Whether `frame/questions.md` Q1's default (no converter for `parity.md`, the signer table and `pact-paths.md`) is the owner's answer | `seal/threads/1794200906-settings-are-read-as-json/frame/questions.md` Q1 | the owner |

## Probes

| Command | Result |
|---|---|
| `diff` of round 2's three snippets and the A9 cell against `frame/design.md:645-719`, `gaps.md:15`, the test file's lines 452-467 and `frame/plan.md:25` | all four identical |
| `bin/seal settle --draft --released-at HEAD` in the clone at `64315ab6`, then `git checkout -- docs` | exit 0; "placed 112 of 113 operations in docs/"; not placed: `1794188289-the-body-reads-in-the-teams-language/frame/design.md:226`; `docs/` restored |
| `bin/test -q tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py tests/skills/test_chain_check.py` in the clone at `64315ab6` | exit 0, 242 passed |
| the same, with `chain_check.py:1611` read at `optin.HOME`; the line restored by the Edit tool after | exit 1; only `test_s3_an_earlier_releases_parity_md_under_agentic_seal_is_refused_there` fails, at line 465; 241 passed |
| `bin/seal layout --pairs` and `bin/seal layout --check` over the test file | "1 files read, 0 pairs"; check exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.37.0 --root <worktree> --worktree`, before this record | exit 0; twelve test-pin notices at `frame/design.md:358` and `:477`; round-2 finding 3 and `1b04534c` owed a verifying round; no gate record and no guarantee yet |
