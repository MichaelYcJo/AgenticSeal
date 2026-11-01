# Review round 1: 1793457437-readers-state-the-shapes-they-pass

```seal
target: 71a85927 against origin/release/v0.27.1
```

The frame is `frame/design.md`, `frame/plan.md` and `frame/questions.md` at `081cb6b5`. There is no earlier round, so no fact is carried; every fact below was established this round. Neither `seal/parity.md` nor a `Reference specs` row exists, so no behaviour is compared with an original and no reference root is read.

## Findings

### 1. The marker sentence says every gate is then silent, but the gates read the root under the git directory where one opens with the marker

```seal
severity: should
location: `templates/setup/seal-README.md:60-62`, `seal/README.md:60-62`, `seal/threads/1793457437-readers-state-the-shapes-they-pass/changelog.md:3`
evidence: executed `bin/test`, `pytest tests/hooks/test_tmp_round1.py -q -s`
```

Why it matters: the claim is that a broken first line makes every gate silent (*Scope* item 1, and the sentence at `templates/setup/seal-README.md:60-62`). `hooks/lib/optin.py:252-255` (`home_at`) reads `<root>/seal/` and then `<git-common-dir>/seal/`, and returns the first whose `README.md` opens with the marker. So a `seal/README.md` with a space after the marker is passed over, and the gates read the root under the git directory wherever that one is marked. The probe built a repository holding both roots and wrote the shared README with a trailing space: `home_at` gave `.git/seal`, and gave `""` only once the local root was removed. With that root in force the gates are not silent. `hooks/lib/routing.py:375-377` reads the routing declarations from it, so `hooks/routing-edit-gate.py:253-258` refuses an edit on a branch whose declaration stands in the tree's `seal/threads/` and not under the git directory (read). The paragraph's own earlier sentence says first setup meeting an unmarked `seal/` keeps the root under the git directory, and that is how such a root comes to stand. A clone with both roots is the state `seal import` and `seal mode` refuse (`skills/implement/scripts/seal.py:1050`, `skills/implement/scripts/seal.py:2415`), and that refusal is not the gates' silence. The person editing the README reads this sentence, and the changelog fragment repeats it to every reader of the release note.

The fix replaces the sentence in both files, which `tests/behaviour/test_first_setup_asks_once.py` keeps byte-identical, and the clause in the changelog fragment. The precondition is the one `home_at` already has: the two places are read in that order, and the opt-out file `.git/agentic-scratch` is not present.

```markdown
The line is compared whole, with only its line end taken off, so a space
after it, a byte order mark before it or a blank line above it makes it
another line. The gates then read the root under the git directory where
its `README.md` opens with the marker, and are silent where none does.
Leave the line as it is.
```

```seal
verdict: fixed fd549f8e
answer: The finding holds at `hooks/lib/optin.py#home_at`, which passes over an unmarked `<root>/seal/` and returns `<git-common-dir>/seal/` where that one is marked. The sentence in both READMEs now says the gates then read the root under the git directory where its `README.md` opens with the marker, and read the repository as one that never opted in where none does; the changelog clause says the same. The paste-ready text was not applied as written: its `are silent where none does` would drop the words `never opted in`, which `tests/behaviour/test_first_setup_asks_once.py#test_the_seal_readme_says_its_first_line_is_the_marker` pins in that paragraph, and the next paragraph states the opt-out in those words. By contract rule 12 the paragraph's opening sentence, which said every gate reads an unmarked `seal/` as a repository that never opted in, made the same claim and now says every gate passes over such a `seal/`. The two files stay byte-identical (`cmp`, exit 0).
```

### 2. The `evals/README.md` sentence says a count cell spaced otherwise reads as 0, but a value cell with extra spaces is read

```seal
severity: should
location: `evals/README.md:62-65`, `tests/evals/test_noninferiority.py:1905-1909`, `seal/threads/1793457437-readers-state-the-shapes-they-pass/changelog.md:3`
evidence: executed `bin/test`, `pytest tests/hooks/test_tmp_round1.py -q -s`
```

Why it matters: the sentence at `evals/README.md:62-65` says `check` reads each count "only in the spacing `compare` writes", and that "a count cell spaced otherwise reads as 0". `evals/scripts/noninferiority.py:1058-1063` (`header_field`) matches `^\| <name> \| (?P<v>[^|]*) \|$` and strips the value. The pattern fixes one space on each side of the name, needs at least one space on each side of the value, and allows nothing after the last pipe. The probe read `| New false rows |  15 |`, `| New false rows | 15  |` and `| New false rows |   15   |` as `15`. It read `|  New false rows | 15 |`, `| New false rows |15 |` and `| New false rows | 15|` as None, which `evals/scripts/noninferiority.py:1077-1080` turns into 0. So a count cell padded with extra spaces is read, and the sentence states a limit wider than the reader's. The new case at `tests/evals/test_noninferiority.py:1905-1918` pins the name cell, which holds; its docstring repeats the wider claim, and so does the changelog fragment. Contract rule 12 asks for the class: the four counts are the only `header_field` reads that `parse_record` turns into 0 (`evals/scripts/noninferiority.py:1077-1080`), so the class is those four lines.

The fix replaces the sentence after `Nothing in the tree makes a later edit owe a run.`, the matching clause of the changelog fragment, and the first sentence of the case's docstring:

```markdown
`check` finds each of the record's four row counts only on a line spelt
`| <name> | <value> |`, with one space on each side of the name, at least
one on each side of the value, and nothing after the last pipe. A row
spelt otherwise is not found and its count reads as 0, so a record edited
by hand can pass `check` on a count it never read.
```

```seal
verdict: fixed b5a4d754
answer: The finding holds at `evals/scripts/noninferiority.py#header_field`. The `evals/README.md` sentence, the changelog clause and the case's docstring now state the row spelling the reader finds. The paste-ready text was applied with one clause added, `nothing before the first pipe`, because the pattern opens with `^`. The case is renamed `test_a_count_row_spelt_otherwise_is_read_as_naught` and parametrized over four spellings that read as 0: the name spaced otherwise, no space before the value, no space after it, and a space after the last pipe. A new case, `test_a_count_padded_with_more_spaces_is_read`, holds the other half of the sentence. Each was seen red with `seal mutate` on `header_field` before the commit: a pattern that allows any spacing turned the four ids red, and a value read as `\S*` turned the padded case red.
```

## Confirmations

```seal
confirms: none
```
What matched: *Scope* item 1's placement. The sentence stands before `Leave the line as it is.` in `templates/setup/seal-README.md:60-62`, and `seal/README.md` is byte-identical to it (executed, `cmp`, exit 0). The two ids at `tests/hooks/test_optin.py:290-291` write a trailing space and U+FEFF, and `readme_at` encodes U+FEFF as its three UTF-8 bytes (read `tests/hooks/test_optin.py:261-266`). The trailing-space id covers what `a longer line` does not: under the plan's mutation `first.strip() == MARKER`, `{marker} of a fork` stays refused and `{marker} ` does not (read `hooks/lib/optin.py:208-212`).

```seal
confirms: none
```
What matched: the first departure the crafter reports. The claim is that `str.strip` leaves U+FEFF, so the plan's mutation cannot turn the byte-order-mark id red. The probe gave `'﻿x'.strip() == '﻿x'` True (executed). A `utf-8-sig` decode drops a leading U+FEFF, so `marked` would then read the marker and the id goes red (read `hooks/lib/optin.py:208-212`). The departure meets contract rule 15 better than the plan's cell did. That the run went red is the crafter's claim (`trail/phases/phase-1.md`); this round did not repeat the mutation.

```seal
confirms: none
```
What matched: the second departure, items 2 and 3 written as several sentences. The text at `templates/setup/config.md:15-18` and `evals/README.md:62-65` carries every clause of *Scope* items 2 and 3, at the place each item names (read). Finding 2 concerns what item 3's sentence says, not how many sentences it takes.

```seal
confirms: none
```
What matched: *Scope* item 2 holds for every item of `seal/config.md`, as its alternatives row claims. The list was made by listing every caller of `config_table`, `config_rows` and `value_of` outside the tests (executed, `git grep`): `hooks/lib/config.py:529-536`, `skills/implement/scripts/seal.py:1539-1540`, `skills/implement/scripts/seal.py:1583-1586`, `skills/implement/scripts/seal.py:1667`, `skills/verify/scripts/broad_gate.py:724-725` and `skills/settle/scripts/fold_check.py:296-300`. Each compares the item with `==` (read). `gaps.md` *Not done* says the fold reads through `value_of`, and `skills/settle/scripts/fold_check.py:300` shows it.

```seal
confirms: none
```
What matched: *Scope* item 4. `.github/scripts/rules.py#markers` lists `a-release-is-judged-under-its-two-names` on `Test_main.test_refuses_a_head_that_is_not_a_release_branch_with_a_reason` and `Test_main.test_a_milestone_that_does_not_exist_says_it_verified_nothing` and nothing else (executed). The `add` in `## Rule changes` matches `.github/scripts/release_completeness_check.py:355-390`: a head no release pattern matches prints `nothing to judge` and returns 0 before `subjects_since`, and a missing milestone prints the warning and returns the `feat:` reading's result (read). The `change` item's `from` matches `docs/the-record-layout.md:183-193` word for word (read).

```seal
confirms: none
```
What matched: no reader changed, as *Data & interfaces* says. `git diff --stat origin/release/v0.27.1...HEAD` touches no file under `hooks/`, `skills/`, `evals/scripts/` or `.github/scripts/` (executed).

```seal
confirms: none
```
What matched: each new case against its group. `bin/seal layout --pairs` over the four changed test modules names two pairs, both between cases the diff does not touch (executed). Read against `Test_config_value`, `Test_marked` and `Test_check_record`, each new case covers a shape no other case of its group covers.

```seal
confirms: none
```
What matched: the suite's label. `gaps.md` *Not verified* names the full suite, the lint and the format check as not run, names the orchestrator as their answerer, and calls the 57-module set a sample. The narrow run this round passed (executed, `bin/test` over `tests/hooks/test_optin.py`, `tests/hooks/test_config.py`, `tests/evals/test_noninferiority.py`, `tests/github/test_release_completeness_check.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/github/test_rules.py`: 760 passed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the branch head | the whole tree | the orchestrator, by `seal gate` under the `Broad gate` row of `seal/config.md` |
| Whether the four seen-red runs went red as `trail/phases/phase-1.md` reports; this round read each mutation against its reader and did not run them again | `trail/phases/phase-1.md` | the sealer, which re-runs a sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the seven modules named under the last confirmation | 760 passed, exit 0 |
| `pytest tests/hooks/test_tmp_round1.py -q -s` in a scratch clone at `71a85927`, through the worktree's `.venv` | `header_field` gave `15` for the name spaced as written with the value padded by one, two or three extra spaces on either side, and None for the name cell spaced otherwise, for `\|15 \|` and for `\| 15\|`. `'﻿x'.strip()` kept U+FEFF. `home_at` gave `seal` with both roots marked, `.git/seal` once the shared README had a trailing space, and `""` once the local root was removed. 3 passed; the file and the clone were deleted after the one run |
| `bin/seal layout --pairs` over the four changed test modules | 4 files read, 2 pairs, both on unchanged cases, exit 0 |
| `cmp seal/README.md templates/setup/seal-README.md` | exit 0 |
