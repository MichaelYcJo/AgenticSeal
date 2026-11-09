# Review round 2: 1794200906-settings-are-read-as-json

```seal
target: fda842b8, fixes 4a58c4ba..fda842b8
```

This round reads three things in that range. The first is the fix pass `4a58c4ba..f775882b`, whose nine commits include the orchestrator's `10a1e66e`. The second is the take-in of `origin/release/v0.37.0` at `a9cbb7f7`, read as its resolution through `git show --remerge-diff a9cbb7f7` and not as #1059's whole diff. The third is the two follow-on commits `3edba430` and `fda842b8`. It also read `routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md` whole at `fda842b8`. No `pr.<lang>.md` stands, and both language keys of `seal/config.json` read `English`, so none is owed. Every `seal` command this round ran is the clone's own `bin/seal` at `fda842b8`, never the installed 0.36.0 one.

Facts carried from round 1 and not established again: `lib/config.py#policy_root` and `#reference_roots` drop `declared_value`'s refusal and read their defaults. Round 1's `seal rules --check` probe showed it, and this round read the docstring again (`lib/config.py:292-325`). Also carried: the phase records' account of what each phase built, and phase 4's claim that the 25 moved walker units equal the base's by `ast`, which round 1 left to the sealer. Re-established this round: S8 at the target. The only `gfm_table(` calls outside `tests/` are `skills/implement/scripts/seal.py:1576` (the converter), `skills/settle/scripts/settle.py:1090` and `skills/verify/scripts/pact_check.py:364`, and `lib/config.py:48-50` imports `json`, `os` and `re` alone (executed: `git grep -n 'gfm_table('`).

## Findings

### 1. `frame/plan.md` A9 still says every reader refuses an unconverted `config.md`

```seal
severity: should
location: `seal/threads/1794200906-settings-are-read-as-json/frame/plan.md:25`
evidence: executed `git grep -n -i 'every reader\|every command\|every script that reads\|every `seal`'` over the tree outside the other items' threads, then read each hit; read `seal/threads/1794200906-settings-are-read-as-json/frame/plan.md:25`, `lib/config.py:292-325`
reopens: round-1#1
```

Why it matters: round 1's finding 1 was closed `fixed f8d33094`. The close said `git grep` found three more statements of the claim, and that each was fixed. The class is a closed set: this item's diff and each of its records that states the present, read whole (contract rule 12). `frame/plan.md` *Alternatives considered* row A9 is in that set. It says the alternative was "rejected: `seal mode` converts, and every reader refuses an unconverted file (design Scope item 2)". The target does not do that. `lib/config.py#reference_roots` (`:313-325`) and `#policy_root` (`:370`) read their defaults on any refusal, and the changelog and template sentences the fix pass rewrote now say so. The plan's *Alternatives considered* section names no commit it was read at, so it states the present. The sealer reads this row, and it contradicts `changelog.md:4`. Only the A9 cell changes.

```markdown
frame/plan.md:25, the Verdict cell of row A9:
rejected: `seal mode` converts, and `seal gate`, `seal pr-body`, `seal fold`, `seal pact` and `seal mode --check` refuse an unconverted file (design Scope item 2 and S3)
```

```seal
verdict: fixed 4b99e2d3
answer: Applied the A9 cell as given. Before committing it I read the work item's records for every other statement of the claim. The method was a grep of `routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md` for "every reader", "every command", "every script", "refuses an unconverted", "exits 2" and the Korean "모든 ... 거절" forms, and I read each hit. No other line says every reader or every command refuses. `frame/plan.md:11` and `:54`, `changelog.md:10` and `pr.md:8` name the five commands that stop and the three that read defaults. `frame/design.md:37` and S3 (`:61`) name `seal mode --check` and the four commands. The two design `to:` values at `:260` and `:327` say a `config.md` "is refused by every reader that refuses a file it cannot read, and read as no file by the readers of `Policy root` and `Reference specs`", which holds at HEAD. `frame/design.md:38` (Scope item 3) says every script that reads a setting reads it through the one reader, which is a different claim and holds.
```

### 2. *Rule changes* misses twelve `docs/` sentences that the settle writes from earlier items and that name `seal/config.md` or call a setting a row

```seal
severity: should
location: `seal/threads/1794200906-settings-are-read-as-json/frame/design.md:640-644`, `seal/threads/1794200906-settings-are-read-as-json/gaps.md:13`
evidence: executed `bin/seal settle --draft --released-at HEAD` in a scratch worktree at `fda842b8`, then `git diff -U0 -- docs` filtered to added lines holding `row`, `config.md` or `행`, and each hit read; executed the same draft at a scratch commit holding the operations below; read `seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md:121-230`, `seal/threads/1794187229-the-body-carries-the-seal-mark/frame/design.md:225`, `:295`
```

Why it matters: the settle writes `docs/` in merge order. It applies the 0.36.0 items' operations first and then this item's. Two of those earlier items, 1794187229 (#1452, the seal mark) and 1794188289 (#1453, the team's language), are still under `seal/threads/` at the target. Their `to:` values put new sentences into `docs/` that name `seal/config.md` or call a setting a row. None of those sentences stands in `docs/` at HEAD, so round 1's search of `docs/` could not see them. The draft shows each one. `seal settle --draft --released-at HEAD` at `fda842b8` placed 100 of 101 operations. The drafted policy root then holds these sentences, and no operation of this item reaches them:

- `docs/checks/the-pull-request-check.md` *What the check reads at the pull request*: "the `Pull request seal mark` row reads `yes`" (from 1794187229 `frame/design.md:225`); "Where `seal/config.md`'s two language rows differ ... where either row is absent the check refuses on `seal/config.md`" (1794188289 `:222-225`).
- `docs/forms/the-guarantee.md` *The guarantee*: "`seal/config.md`'s `Commit and pull request language` and `Record language` rows name different languages", "either language row is absent" and "where the rows differ" (1794188289 `:129-130`, `:147`, `:155`).
- `docs/layout/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read*: "The two language rows are required" and "Where the two rows differ" (1794188289 `:194`, `:207`).
- `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*: the `pr.md` and `pr.<lang>.md` rows and the paragraph on what leaves with the directory, three times (1794188289 `:166`, `:160`, `:173`).
- `docs/running/the-run.md` *The run*: "where the two language rows differ" (1794188289 `:217`).
- `docs/running/what-a-script-gates.md` *The checks*: "the mark the row and the guarantee at HEAD give" (1794187229 `:295`).

Without operations for them, the settled 0.37.0 policy root names a file that no reader opens and calls the language and seal-mark settings rows. Design G1 asks that every sentence stating the table shape be rewritten. Round 1's finding 3 owed the same kind of operation for lines already in `docs/`. The twelve operations below go after the last entry, at `frame/design.md:644`. A second draft at a scratch commit holding them placed 112 of 113 operations, all twelve among them. Its drafted `docs/` then held no `seal/config.md` and no setting called a row, except this item's own sentences on converting the old `config.md` (executed).

One more operation of 1794188289 is not placed by either draft (`frame/design.md:226-230`, the `seal pr-body` row of `docs/running/what-a-script-gates.md` *The checks*). Its `from:` expects the row as it stood before 1794187229 rewrote it, and its `to:` names "`config.md`'s two language rows". No `from:` of this item can name text that the settling session will write by hand, so the snippet's last part is a sentence for `gaps.md` *Not done*, where the settle reads it. The orchestrator asked about the six `config.md` mentions at HEAD, at `docs/checks/the-fold.md:112`, `:117`, `:147`, `docs/forms/the-guarantee.md:43` and `docs/layout/one-root-by-lifetime.ko.md:121`, `:199`. Each already has an operation (`frame/design.md:346-354`, `:355-367`, `:378-383`, `:428-432`, `:155-175`, `:264-273`), and the first draft rewrote each one. So none of the six owes a new operation.

```markdown
frame/design.md, after the last entry at :640-644:
- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: the seal mark where the `Pull request seal mark`
    row reads `yes` and the work item is sealed at HEAD,
  to: the seal mark where the `Pull request seal mark`
    key reads `yes` and the work item is sealed at HEAD,
- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: Where `seal/config.md`'s two language rows differ, the body the check
    compares opens with the work item's `pr.<lang>.md` and then `pr.md`, as
    `seal pr-body` composes it, and where either row is absent the check
    refuses on `seal/config.md`, as `seal pr-body` does.
  to: Where `seal/config.json`'s two language keys differ, the body the
    check compares opens with the work item's `pr.<lang>.md` and then
    `pr.md`, as `seal pr-body` composes it, and where either key is absent
    the check refuses on `seal/config.json`, as `seal pr-body` does.
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: `pr.<lang>.md`, where `seal/config.md`'s
    `Commit and pull request language` and `Record language` rows name
    different languages,
  to: `pr.<lang>.md`, where `seal/config.json`'s
    `Commit and pull request language` and `Record language` keys name
    different languages,
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: `seal pr-body` refuses where either language row is absent,
  to: `seal pr-body` refuses where either language key is absent,
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: where the rows differ, `pr.<lang>.md` give,
  to: where the keys differ, `pr.<lang>.md` give,
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: The two language rows are required:
  to: The two language keys are required:
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: Where the two rows differ,
    the pull request body opens with `pr.<lang>.md`,
  to: Where the two keys differ,
    the pull request body opens with `pr.<lang>.md`,
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: `pr.<lang>.md` where the two language rows differ: the `Closes` lines
  to: `pr.<lang>.md` where the two language keys differ: the `Closes` lines
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: where that row and `Record language` name different languages;
  to: where that key and `Record language` name different languages;
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: where the two language rows differ) go with the directory, whole,
  to: where the two language keys differ) go with the directory, whole,
- change
  file: docs/running/the-run.md
  section: The run
  from: `pr.<lang>.md` where the two language rows differ, where the owner can
  to: `pr.<lang>.md` where the two language keys differ, where the owner can
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: the records and the mark the row and the guarantee at HEAD give |
  to: the records and the mark the `Pull request seal mark` key and the
    guarantee at HEAD give |

gaps.md, Not done, after the paragraph at :13:
`seal settle --draft` does not place the operation at `seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md:226`, because 1794187229's operation rewrites the `seal pr-body --check` row of `docs/running/what-a-script-gates.md` *The checks* before it. Its `to:` names `config.md`'s two language rows. The settling session that places it by hand writes `config.json`'s two language keys and calls each a key.
```

```seal
verdict: fixed 66b462d7
answer: Added the twelve operations after the last entry of *Rule changes*, and added the gaps.md sentence after the paragraph at :13, in one commit. Before applying them I read the unplaced operation at `seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md:226-230` and the `seal pr-body --check` row at `docs/running/what-a-script-gates.md:66`, and the gaps.md sentence states both as they stand. I ran `chain_check.py --baseline origin/release/v0.37.0 --worktree` after applying the operations. It printed the same twelve test-pin notices at `frame/design.md:358` and `:477` that this round weighed, and none at the new operations (executed). I then ran the tree's `bin/seal settle --draft --released-at HEAD` in a scratch worktree at `66b462d7`. It placed 112 of 113 operations, and the one not placed is 1794188289's at `:226` (executed). Each of the twelve `to:` texts stands once in the drafted `docs/` (executed: `git grep -F` of each). The drafted `docs/` names `config.md` only in this item's two converter sentences, `docs/layout/one-root-by-lifetime.md:269` and its Korean edition at `:246`. Its other added lines holding "row" name `routing.md` rows, the pact anchor's rows or a plan's row (read). The scratch worktree was then removed with `git worktree remove`.
```

The fix pass runs `chain_check.py --worktree` after applying the operations, and weighs any test-pin or copy notice they raise.

### 3. No case holds the take-in's reading of an unconverted `parity.md` under `agentic-seal/`

```seal
severity: should
location: `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py:429-449`, `skills/code-review/scripts/chain_check.py:1611`
evidence: executed `bin/test -q tests/behaviour/test_tmp_agentic_parity_md.py tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py tests/skills/test_chain_check.py` with `chain_check.py:1611` changed to the `optin.HOME` spelling `f775882b` had, then with it spelt `"seal/"`, then restored
```

Why it matters: the merge at `a9cbb7f7` wrote a line that neither side held. `old = f"{home}/{routing.optin.OLD_PARITY_CONFIG}"` (`chain_check.py:1611`) reads an earlier release's `parity.md` under the root's own name. So a repository whose root is `agentic-seal/` is told to write `agentic-seal/parity.json`. The behaviour is right at the target. The probe's first run showed the refusal `agentic-seal/parity.md:0  is the migration config an earlier release read, ... write agentic-seal/parity.json from templates/setup/parity.json ...`. But nothing in the suite holds it. With the line put back to the `f775882b` side of the conflict, `f"{routing.optin.HOME}/..."`, the probe failed, and `test_a_foreign_seal_dir_keeps_the_records_shared.py` and `test_chain_check.py` passed whole (241 passed). With the line spelt `"seal/"`, `test_chain_check.py::test_census` failed on its `root_name` rule. So the census catches a literal spelling and does not catch the constant. Design *Scope* item 4 states the refusal "wherever the arm would read the config", and #1059 has the arm read the config under `agentic-seal/` (`test_s3_a_change_to_the_package_reaches_outside_the_document_roots`). The one case the take-in owes sits beside that one (`skills/code-review/SKILL.md` *Regression test*). The fix pass shows the case red against the `optin.HOME` line before it commits it (contract rule 15).

```python
# tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py,
# after test_s3_a_change_to_the_package_reaches_outside_the_document_roots
def test_s3_an_earlier_releases_parity_md_under_agentic_seal_is_refused_there(
    declared, capsys
):
    """#1454 beside #1059: an `agentic-seal/parity.md` git carries with no
    `agentic-seal/parity.json` beside it is refused once, at its path under
    the root's own name, naming the file to write, where a change reaches
    the package. Red with `chain_check.py#originals_of` reading the old
    file at `optin.HOME`."""
    write(declared, "agentic-seal/parity.md", "# Migration config\n")
    write(declared, "seal/__init__.py", "VERSION = 2\n")
    commit_everything_as_e(declared, "the change")
    _code, out = checked(capsys, declared)
    refused = [ln for ln in out.splitlines() if ln.startswith("agentic-seal/parity")]
    (line,) = refused
    assert line.startswith("agentic-seal/parity.md:0  "), line
    assert "agentic-seal/parity.json" in line, line
```

```seal
verdict: fixed 1b04534c2
answer: Added the case as given, after `test_s3_a_change_to_the_package_reaches_outside_the_document_roots`. `bin/seal layout --pairs` over the module names no pair (executed: "1 files read, 0 pairs"). I showed it red with `bin/seal mutate skills/code-review/scripts/chain_check.py`, replacing `old = f"{home}/{routing.optin.OLD_PARITY_CONFIG}"` with `old = f"{routing.optin.HOME}/{routing.optin.OLD_PARITY_CONFIG}"`. The new case failed at `(line,) = refused` with "not enough values to unpack (expected 1, got 0)", because no refusal names a path under `agentic-seal/` once the old file is read under `seal/` (executed). `seal mutate` restored the file, and `chain_check.py:1611` reads `{home}` again (read). The case then passed, with the rest of its module and `tests/skills/test_chain_check.py`: 242 passed (executed).
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: `b5715ae5` rewrites the four lines the finding named to "key" (`agents/sealer.md:153`, `skills/code-review/SKILL.md:63`, `skills/writing-style/outside-the-review.md:34`, `skills/settle/SKILL.md:296`). It also rewrites one more, `agents/sealer.md:84`, and three test docstrings and a comment (read `git diff 4a58c4ba f775882b`). The close calls its Python list a sample, and finding 2 above found no shipped sentence the sample left (read).

```seal
confirms: round-1#3
```
What holds: `97b56c17` adds the five operations at `frame/design.md:484-516` and removes the third *Not done* paragraph of `gaps.md` (read). The draft at `fda842b8` placed all five: after it, `docs/running/the-broad-gate.md` holds no "row" meaning the command, and `docs/checks/the-fold.md` reads "no configuration key names such a" (executed).

```seal
confirms: round-1#4
```
What holds: `README.md:101-114` and `README.ko.md:105-117` name the three hand-written files and the target of each, in the finding's text, after finding 1's sentence (read).

```seal
confirms: round-1#5
```
What holds: `lib/config.py#BOM` is `chr(0xFEFF)`, and `baseline_commit` (`lib/config.py:606`) and `pact_check.py#path_map` (`:397-399`) take it off before they parse (read). The two new cases, `tests/lib/test_config.py#Test_baseline_commit::test_reads_past_a_byte_order_mark_an_editor_wrote` and `tests/skills/test_pact_check.py#Test_path_map::test_reads_past_a_byte_order_mark_an_editor_wrote`, pass in this round's run of both modules (executed). `seal layout --pairs` names no pair for either case (executed).

```seal
confirms: round-1#6
```
What holds: `changelog.md:7` opens "The table walker lives in `lib/tables.py`, and no setting is read through it", and `pr.md:6` quotes it. `lib/tables.py:6-14` says its callers read records and policy documents, and `frame/plan.md` A12 says the same (read). All nine quotes of `pr.md` stand word for word in `changelog.md` once runs of whitespace are collapsed (executed: a substring check of each quote).

What matched: `10a1e66e`, judged as a fix. `hooks/hooks.json` registers a `Stop` hook and a `SessionStart` hook and no other (read). Only `seal.py`'s `mode` reads the `Mode` key, through `lib/config.py#declared_mode` (`seal.py:1476`; executed `git grep -n 'declared_mode\|MODE_KEY'`). `seal mode --check` returns 0 where the key is absent (`seal.py:2278-2279`, read). So the template's new paragraph at `templates/setup/config.md:21-25` holds. `seal.py:1423-1426` says every script that reads a setting imports `lib/config.py` and never imports this command. `broad_gate.py:150` runs `seal.py` as a subprocess and imports nothing of it (read). No other text names a denied Bash call or a `PreToolUse` gate (executed `git grep -n -i 'first Bash call\|PreToolUse'`). The new case `tests/text/test_the_mode_is_a_row_and_a_command.py#test_the_template_says_an_absent_mode_key_stops_nothing` would fail on the template at `4a58c4ba`, which held "first Bash call" (read in the diff), and it passes at the target (executed).

What matched: the take-in keeps both items' behaviour. `lib/config.py#inside_the_root` and `#reference_roots` take #1059's NAME and read `config.json` (`:283-325`). `chain_check.py#originals_of` reads `parity.json` and the old `parity.md` under HOME (`:1610-1611`); finding 3 is the case it owes. `pact_check.py#check` names the pact repository's config under its root's own name and each signer's under that signer's root (`:699-702`, `:751-754`). `release_report.py#documents` reads `Policy root` under `optin.home_name` (`:217-218`). `unverified_check.py#references_at` returns #1059's triple (`:969-982`). `seal.py`'s move guard reads `f"{name}/{CONFIG}"` with `CONFIG` now `config.json` (`:1691`), so dropping `CONFIG_PATHSPEC` left no caller (read; executed `git grep -n CONFIG_PATHSPEC` at `f775882b`, `961fe52b` and HEAD). The test modules of the conflicted scripts and of the two follow-on commits pass, and so do those of `seal.py`, `pr_body.py`, `unverified_check.py`, `fold_check.py`, `rules.py` and `release_seal.py` (executed, *Probes*). `3edba430` passes `originals_of` the root name its new signature takes. `fda842b8` writes `config.json`, `parity.json` and a `Pact signers` key in #1059's cases, and the S5 pact case now asserts the refusal at `agentic-seal/config.json` (read).

What matched: the shipped code and texts outside `docs/` name `config.md`, `parity.md` and the old tables only as the earlier release's files that `seal mode` converts or the refusals name (executed `git grep` for `config\.md`, `parity\.md`, `Signer |`, `PACT_ROW`, `BASELINE_ROW` and `pact_signers` over `lib`, `skills`, `.github`, `hooks`, `bin`, `agents`, `templates` and the READMEs, each hit read).

What matched: `chain_check.py --baseline origin/release/v0.37.0 --root <worktree> --worktree`, run before this record was written, prints twelve test-pin notices at `frame/design.md:358` and `:477`. These are the two `remove` operations round 1 weighed. Quoted: "a test pins text this operation takes out of `docs/checks/the-fold.md`: `tests/skills/test_broad_gate.py:1965` holds "a fence nobody closed", and the `to` does not". So do `tests/skills/test_chain_check.py:2915` and `tests/skills/test_payload_meter.py:1321`. Six more name `tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:57`, `:203`, `tests/block_shapes.py:58` and `tests/lib/test_tables.py:441`, `:472`, `:562`, and three repeat the `| Item | Value |` pins at `:477`. Each pin is a case id, a commit message or a fixture header that shares words with the removed paragraph. None holds the rule's wording, so none is a finding (read each line).

The orchestrator named #1059's records at `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/design.md:55` and `frame/plan.md:47`. They state `config.md` where the tree has `config.json`. They are #1059's, read at its settle, and this round raises nothing on them.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The whole suite, the repository-wide lint and the format check at `fda842b8` (`unverified`); this round ran only the module sets in *Probes* | the branch at `fda842b8` | the orchestrator, through this worktree's own `bin/seal gate` |
| Whether the 25 moved walker units equal the base's by `ast`, as phase 4 claims (carried from round 1, not re-run) | `lib/tables.py` | the sealer, where it samples the crafter's claims |
| Whether `frame/questions.md` Q1's default (no converter for `parity.md`, the signer table and `pact-paths.md`) is the owner's answer | `seal/threads/1794200906-settings-are-read-as-json/frame/questions.md` Q1 | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/lib/test_config.py tests/skills/test_chain_check.py tests/skills/test_pact_check.py tests/skills/test_broad_gate.py tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py tests/github/test_release_report.py tests/text/test_the_mode_is_a_row_and_a_command.py` in the clone at `fda842b8` | exit 0, 783 passed, 1 skipped |
| `bin/test -q tests/skills/test_seal.py tests/skills/test_pr_body.py tests/skills/test_unverified_check.py tests/skills/test_fold_check.py tests/github/test_rules.py tests/github/test_release_seal.py` in the clone | exit 0, 937 passed |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.37.0 --root <worktree> --worktree`, before this record | exit 0; twelve test-pin notices at `frame/design.md:358` and `:477`; six close blocks of round 1 owed a verifying round |
| `bin/seal settle --draft --released-at HEAD` in a scratch worktree at `fda842b8` | placed 100 of 101; not placed: `1794188289-the-body-reads-in-the-teams-language/frame/design.md:226`; drafted `docs/` holds the twelve sentences of finding 2 |
| the same draft at a scratch commit adding finding 2's twelve operations to this item's design (the commit stayed in the scratch worktree, which was removed) | placed 112 of 113, the same one not placed; no `seal/config.md` and no setting called a row in the drafted `docs/` outside this item's converter sentences |
| `bin/test -q tests/behaviour/test_tmp_agentic_parity_md.py` at the target, then with `chain_check.py:1611` spelt `"seal/"` and with it read at `optin.HOME`, each beside `test_a_foreign_seal_dir_keeps_the_records_shared.py` and `test_chain_check.py`; the line restored and the file deleted | at the target the refusal reads at `agentic-seal/parity.md:0` and names `agentic-seal/parity.json` (the first run's own filter also matched the pytest path, and its output shows the line); `"seal/"`: the probe and `test_census` fail; `optin.HOME`: only the probe fails, 241 passed |
| `bin/seal layout --pairs` over the three test files the fix pass changed, and `--check` over the six test files the range changed | no pair names a new case; check exit 0 |
| `git grep -n 'gfm_table('` outside `tests/` | three callers, as the opening paragraph gives |
