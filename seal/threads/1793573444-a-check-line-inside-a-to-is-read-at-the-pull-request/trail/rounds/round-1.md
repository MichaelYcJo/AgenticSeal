# Review round 1: 1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request

```seal
target: 7e5561f4d against origin/release/v0.28.0
```

No earlier round exists, so no fact is carried into this one: every coordinate below was opened in this round. No `seal/parity.md` is declared, so the round block holds no `original:` line. `seal/config.md` has no `Record language` row and no `Pact` row, so the record is English and no pact anchor was read.

The review read the frame at f76018851, the build commits 92e04b7b9, 88e4a5880 and b520cbf52, the phase-2 commit ff6e32dd6, and the record commits 42c442642 and 7e5561f4d, against the design's *Scope*, *User scenarios*, *Data & interfaces* and *Rule changes*, and against the earlier decisions the design names as G17 to G20 (#1214, #1167, #1198). The axes walked were the table's floor plus this change's own: line-number mapping between a value and its design, the scope edges of the read (`add`, `change`, `from`), the reader's load path in a user's CI clone, and what the new message tells a person.

## Findings

### 1. No case reads the `to` of an `add`, so dropping `add` from the read passes every test that runs chain-check

```seal
severity: should
location: `tests/skills/test_chain_check.py:1902`, `skills/code-review/scripts/chain_check.py:1058`
evidence: executed `bin/test tests/skills/test_chain_check.py -q -p no:xdist`, `bin/test $(git grep -l -e chain_check -- "tests/**/test_*.py" | grep -v test_chain_check.py) -q`, `bin/test tests/skills/test_chain_check.py -q -p no:xdist -k test_tmp_reads_the_to_of_an_add`
```

Why it matters: the arm reads the `to` of the two kinds named in `WRITES_A_TO = ("add", "change")` (`skills/code-review/scripts/chain_check.py:1058`). Every case of `Test_check_lines_in_a_to` builds its design with `change_to` (`tests/skills/test_chain_check.py:1794-1800`), so each one exercises a `change`. No case puts a check line in the `to` of an `add`. The `add` cases elsewhere in the module carry no check line in their `to` (`tests/skills/test_chain_check.py:1422`, `tests/skills/test_chain_check.py:3641`), so they pass whether the `add` is read or not.

This round ran the mutant. `WRITES_A_TO` was set to `("change",)` in a scratch clone at 7e5561f4d. `tests/skills/test_chain_check.py` then gave 173 passed. The 25 other test modules that name `chain_check` gave 1858 passed and 9 skipped. No case went red.

The `add` is the kind the issue is about. The design's own rule change is an `add` (`frame/design.md:74-86`), and the 0.27.1 settle wrote its six refused lines from `add` and `change` values alike (G17). Design G19 builds on #1167's rule that each edge of the scope where a gate reads a form carries a case. The phase-1 record names the `change`'s and the `remove`'s `from` as the edges it covered. It names no case for the `add`.

A dropped `add` would go unnoticed by the suite, and every rule a design adds would reach the settle unread again. The check would still pass every case.

The case below was run in the scratch clone. It passed at 7e5561f4d and failed under the `("change",)` mutant (*Probes*). It goes into `Test_check_lines_in_a_to`, above `test_reads_no_check_line_in_a_from`:

```python
    def test_reads_the_to_of_an_add_as_of_a_change(self, branch, ready, capsys):
        """S1 for an `add`: the settle writes an `add`'s `to` into the policy
        root as it writes a `change`'s, so the comma line is refused at its
        line. Seen red under the mutation that reads a `change` alone."""
        root, _code = branch
        text = spec_with(
            f"- add\n  file: docs/policy.md\n  to: new words.\n    {COMMA}\n"
        )
        put_spec(root, text)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out) == [
            check_line_refusal(text, f"    {COMMA}", reason(root, COMMA))
        ], out
```

### 2. The refusal says `seal rules --check` refuses the line in the file the settle writes, and that reader never reads a file outside `docs/`

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1052-1056`, `tests/skills/test_chain_check.py:1786-1790`, `seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request/frame/design.md:77-86`
evidence: read `.github/scripts/rules.py:71-79`, `.github/scripts/rules.py:211-221`, `skills/settle/scripts/rule_changes.py:206-213`, `hooks/lib/config.py:683-695`, `skills/code-review/scripts/chain_check.py:1052-1056`, `seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request/frame/plan.md:24`
```

Why it matters: `CHECK_LINE_SAYS` tells the author that the settle writes the line into `{file}`, "where that reader refuses it with no pull request left to fix it in" (`skills/code-review/scripts/chain_check.py:1052-1056`). The reader is `seal rules --check`. It reads only the files `RULE_FILES` names, and the one policy entry there is the fixed glob `docs/*.md` (`.github/scripts/rules.py:71-79`, `.github/scripts/rules.py:211-221`). `rule_changes.parse` accepts any `file` that is a top-level file of the configured `Policy root` (`skills/settle/scripts/rule_changes.py:206-213`). That root is any repository-relative directory `seal/config.md` names (`hooks/lib/config.py:683-695`).

So in a repository whose `Policy root` is, say, `policy`, the arm refuses a line in a `to` with `file: policy/rules.md`. It then says `seal rules --check` refuses that line in `policy/rules.md`. That reader never opens that file. The plan knew this when it rejected reading only `RULE_FILES` (`frame/plan.md:24`, row 6: "In a repository whose `Policy root` is not `docs`, no `to` is read"). The arm reads every policy root, as the design chose, and that choice stands. The sentence printed to the author is the defect.

The design's own `add` states the same fact as policy: "The settle writes each `to` into the policy root, where `seal rules --check` first reads it" (`frame/design.md:80-82`). The settle would write that sentence into `docs/the-review-record.md`. A repository with another root would then carry the same false claim in its policy.

The refusal stands on the reader's reason alone, so the message can drop the claimed consequence. `skills/code-review/scripts/chain_check.py:1052-1056`, and the copy pinned at `tests/skills/test_chain_check.py:1786-1790`, both become:

```python
CHECK_LINE_SAYS = (
    "`.github/scripts/rules.py`, the reader `seal rules --check` uses, refuses "
    "this check line, which the settle writes into `{file}` as it stands: {why}"
)
```

The design's `to`, `frame/design.md:77-86`, rewritten with the value's indent:

```markdown
  to: **Each check line inside an `add` or `change` `to` of a design whose
    `## Rule changes` the check parses is read by `.github/scripts/rules.py`,
    the reader `seal rules --check` uses, and a line that reader refuses is a
    refusal at its line in the design, carrying the reader's reason.** The
    settle writes each `to` into the policy root as it stands. Where that
    root is `docs`, `seal rules --check` first reads the line there, and a
    line refused there has no pull request left to fix it in. A line that
    opens like a check line and is not one is named at its line as not read
    and refuses nothing. A `from` is read for no check line, since the
    settle writes none into the policy root.
    check: a-check-line-in-a-to-is-read-at-the-pull-request
```

## Confirmations

```seal
confirms: none
```
What matched: `seal rules --check` prints at this branch what it printed at the base (design S7, the `gaps.md` row the crafter left to round 1). The crafter claimed one run at phase 1's commit, exit 0, with no base run. This round ran the base's `rules.py` over the base tree, the head's `rules.py` over the head tree, and the base's `rules.py` over the head tree. Each exited 0 and printed `seal rules: all 283 check lines in 55 rule files hold.`. The outputs of the base code and the head code over the same tree are identical (`diff` exit 0, executed). The tree holds no refused or excused line, so that run does not reach the rewritten branch of `unresolved` (`.github/scripts/rules.py:366-374`). Read against the old loop, the rewrite keeps the count (`len(check_lines(text))`), the order of the refusals, and the one `removed_by` answer per line. `tests/github/test_rules.py` at HEAD holds every base case unchanged and passed (executed, the narrow run).

```seal
confirms: none
```
What matched: `chain_check.py` loads `.github/scripts/rules.py` from a plugin clone outside the repository it checks (design G9, the second `gaps.md` row left to round 1). `templates/setup/hygiene.yml:63-78` clones the plugin whole with `git clone --depth 1 --branch v<version>` into `$RUNNER_TEMP/agentic`, outside the workspace, and runs `chain_check.py` from that clone (read). `git ls-tree v0.27.3 -- .github/scripts/rules.py` shows the file in a release tag (executed). This round ran the head's `chain_check.py` from a scratch clone against the main checkout with `--root` and `--worktree`. It exited 0. It printed no line for this work item's design, whose `add` names the marker `a-check-line-in-a-to-is-read-at-the-pull-request`. The design holds an `add`, so the arm loaded `rules.py` from the clone, and a load failure would have ended at exit 2 (executed). Because the clone sits outside the root, the marker walk of `rules.py#markers` reads only the checked repository's tests.

```seal
confirms: none
```
What matched: the arm refuses the defect the issue names. Run in-process over `v0.27.0:seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md`, `check_lines_in` refused lines 211, 236, 241 and 313, each for the comma (executed). Design G6 names the same four lines.

```seal
confirms: none
```
What matched: the new read fails no pending design (design G8). Run over the eight `frame/design.md` files under `seal/threads/` at 7e5561f4d, `rule_changes_read` returned no refusal and no notice. Their `add` and `change` `to` values hold five check lines, this design's own among them (executed).

```seal
confirms: none
```
What matched: `Op.lines` equals the value `field_values` builds (design *Scope* item 1). `value_lines` drops leading parts equal to `""`, trailing blank parts, and the last part's trailing spaces (`skills/settle/scripts/rule_changes.py:233-247`, read). That matches `"\n".join(parts).strip("\n").rstrip()` (`skills/verify/scripts/unverified_check.py:676`, read), including a whitespace-only leading part, which neither side drops. Each part is one entry of `body` in order, because `items` appends one part per body line (`skills/verify/scripts/unverified_check.py:643-661`, read). So `numbers[at : at + len(parts)]` gives each part its design line even where a fenced line was skipped. `Op` is built only in `parse` (`git grep -n 'Op('`, executed), and no caller unpacks it by position (`git grep` on `kind, file, section`, executed, no match).

```seal
confirms: none
```
What matched: the build keeps the earlier decisions the design names. G18, #1167: the arm refuses only what `rules.py#refused_lines` refuses and adds no grammar of its own (`skills/code-review/scripts/chain_check.py:1082-1114`, read). G20, the one departure from #1198: a near line goes only to the notices, and `test_names_a_near_line_as_not_read_at_its_line_and_passes` pins exit 0 inside and outside CI (read, and passed in the narrow run). G19: the `from` of a `change` and of a `remove` read nothing (`test_reads_no_check_line_in_a_from`, passed). The `add` edge is finding 1. G17, #1214: the settle's `seal rules --check` run stays, and nothing in the diff removes it (read).

```seal
confirms: none
```
What matched: the phase-2 departure holds. The crafter claimed that no other fragment opens with a `<!-- specs/... -->` marker and that the release note writes it. Each of the seven other `seal/threads/*/changelog.md` files opens with a `###` heading (executed, `head -1` over each). `.github/scripts/publish_release_note.py:292` writes `<!-- specs/{item} -->` above each fragment (read). `.claude-plugin/plugin.json` reads `0.28.0`, and `git grep -n '0\.27\.3' -- ':!seal/threads'` printed nothing (executed).

```seal
confirms: none
```
What matched: the three touched test modules pass at 7e5561f4d. `bin/test tests/skills/test_rule_changes.py tests/github/test_rules.py tests/skills/test_chain_check.py -q` gave 308 passed, exit 0 (executed). This is a narrow run and no seal of the suite.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond the narrow runs above, the repository-wide lint and the format check: `unverified` | the whole tree at 7e5561f4d | the orchestrator's broad gate, `seal gate --base origin/release/v0.28.0 --record seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request` |
| That the release note shows this fragment under its `<!-- specs/... -->` marker once | `.github/scripts/publish_release_note.py:292` | the tag's workflow at the 0.28.0 release, and the orchestrator reading the published note |
| The new cases on the Windows leg of `.github/workflows/test.yml` | `tests/skills/test_chain_check.py:1782-1947` | the pull request's `tests` run |
| Whether each new case was seen red as `trail/phases/phase-1.md` states: this round re-ran only the `add` mutant of finding 1 | `seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request/trail/phases/phase-1.md:15-27` | the sealer, which re-runs a sample of the crafter's claims |

## Probes

Every probe ran in a `git clone --no-local` of the repository under the session's scratch directory, at `<work item>/round-1/`. That holds a clone at 7e5561f4d and one at the base 57d6665b5. Both clones are removed before the hand-back.

| Command | Result |
|---|---|
| `python3 base/.github/scripts/rules.py --check --root base`, `python3 clone/.github/scripts/rules.py --check --root clone`, `python3 base/.github/scripts/rules.py --check --root clone`, then `diff` of the last two outputs | each exit 0, `all 283 check lines in 55 rule files hold.`; `diff` exit 0 |
| `WRITES_A_TO` set to `("change",)` in the head clone; `bin/test tests/skills/test_chain_check.py -q -p no:xdist`, then `bin/test` over the 25 other test modules `git grep -l chain_check` lists under `tests/` | 173 passed; 1858 passed, 9 skipped; no case red |
| finding 1's case added to the head clone as `test_tmp_reads_the_to_of_an_add_as_of_a_change`; `bin/test tests/skills/test_chain_check.py -q -p no:xdist -k test_tmp_reads_the_to_of_an_add` at head, then under the `("change",)` mutant | 1 passed at head; 1 failed under the mutant |
| `python3 -I clone/skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.0 --root` the main checkout `--worktree` | exit 0; no line for this work item's design; three notices for the round, gate and guarantee records the chain owes later |
| `python3 -I -c` loading the head clone's `chain_check.py` and calling `rule_changes_read` over each `seal/threads/*/frame/design.md` | eight designs, five check lines in `add` or `change` `to` values, no refusal, no notice |
| `git show v0.27.0:seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md` into a scratch file, then `python3 -I -c` calling `check_lines_in` over its operations | refusals at lines 211, 236, 241 and 313, each for the comma; scratch file removed |
