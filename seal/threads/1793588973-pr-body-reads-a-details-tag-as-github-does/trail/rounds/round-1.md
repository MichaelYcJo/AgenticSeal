# Review round 1: 1793588973-pr-body-reads-a-details-tag-as-github-does

```seal
target: 02c740e95 against release/v0.28.0
```

The diff is `02c740e95` against its merge base with `origin/release/v0.28.0`, `30ba21373`. No earlier round exists, so no fact is carried into this one from a round. Two facts are carried from the frame and not re-established here: how GitHub renders each line of the frame's probe (`frame/design.md:17`, executed by the framer on 2026-11-02), and the issue's measurement of its four lines (`frame/design.md:16`). No `seal/parity.md` is declared, so the round block holds no `original:` line.

## Findings

### 1. No case pins the refusal's repair, and the case for a line ending in `<details` pins no tag name

```seal
severity: should
location: `tests/skills/test_pr_body.py:373`, `tests/skills/test_pr_body.py:402`, `skills/code-review/scripts/pr_body.py:474-478`
evidence: executed `bin/seal mutate skills/code-review/scripts/pr_body.py --replace '; write it in a code span"' '"' --tests "bin/test tests/skills/test_pr_body.py -q -p no:xdist"`
```

Why it matters: the refusal sentence is what the orchestrator acts on when a record line is refused, and its last clause, "write it in a code span", is the repair. Contract rule 14 asks that a changed message be pinned in the same commit. No case pins that clause. With the clause removed from `pr_body.py:477`, all 31 cases of `tests/skills/test_pr_body.py` still pass (executed, *Probes*). No other module of `tests` or `evals` holds the words "write it in a code span" (executed, `git grep -n "in a code span" -- tests evals`).

The phase record claims that "The new parameters' `said` values hold the tag in backticks, so each case pins the name the sentence gives" (`trail/phases/phase-1.md:23`). For one case that does not hold. The case at `test_pr_body.py:373` copies `a sentence <details` and asserts that the sentence holds `` `<details` `` (`:402`). Every refusal sentence ends with `` `{FOLD}` ``, which is `` `<details>` `` (`pr_body.py:477`), and that string holds `` `<details` `` itself. So the case passes whatever tag the sentence names (read). The existing case at `:355`, `said` `<details>`, matches the same fixed tail, but it predates this branch and its `said` was never claimed to pin a name.

The fix makes that one parameter assert the whole sentence. It then pins the tag name, the claim about the fold and the repair, and it goes red against the mutant above. The `said` is the sentence as `pr_body.py:474-478` composes it for this line (read):

```python
            (
                "changelog.md",
                CHANGELOG + "a sentence <details\n",
                3,
                "holds `<details`, a `details` tag GitHub would read as a second "
                "fold or as the end of the copy's one `<details>`; write it in a "
                "code span",
            ),
```

```seal
verdict: fixed 662bca509
answer: The paste-ready parameter was read against `pr_body.py:474-478` and is the sentence that code composes for the line `a sentence <details`, so it was applied as given at `tests/skills/test_pr_body.py:373`. Under the round's mutant alone, which removes the repair clause, `bin/seal mutate` printed red: that one parameter failed, its assertion reading the whole sentence against the sentence without "; write it in a code span". `tests/skills/test_pr_body.py` passes 31 cases, and `bin/seal layout --check tests`, `uvx ruff check` and `uvx ruff format --check` exit 0. Every other new parameter's `said` value was compared with the fixed tail every refusal ends with, the backticked `<details>`: none is a substring of it, so each still pins its tag name.
```

## Confirmations

```seal
confirms: none
```
What matched: the reading refuses a fact it reads exactly, under `skills/core/SKILL.md` *The rule a mechanism is kept against*. `TAG` (`skills/code-review/scripts/pr_body.py:135`) is one compiled pattern applied at `:470` to the record's own line. Fences are blanked first by `unverified_check.py#readable` (`skills/verify/scripts/unverified_check.py:603`), and code spans next by `close_issues_on_release.py#SPAN` (`.github/scripts/close_issues_on_release.py:123`), the same blanking `_claims` uses for a closing keyword. The pattern holds no list of writer spellings: its four arms after the tag name (whitespace, `/`, `>`, the line's end) and its case flag are the edges of an HTML tag name, and a near miss adds no arm. It decides nothing on what the writer meant. It refuses a character sequence and names the one spelling that always passes, a code span. That spelling is the form the refusal holds, and the form's one statement is the script itself (`pr_body.py:26-30`, `:124-134`). It refuses a superset of what GitHub reads as a tag, and that over-refusal is not a guess about meaning: each over-refused line is a bare tag outside a code span, which the form does not allow, and its cost is one record commit by the orchestrator. The core rule's "reported, never used to block" covers a reading that judges whether a line meant a label, which this reading does not do. One part of the sentence does guess, and it is weighed under *Edges weighed and not opened*, edge 1. The frame cites `docs/what-a-script-gates.md` *Which gate a script holds* for "its absence is refused" (`frame/design.md:9`). That clause is about a required line that is missing, and the clause that fits a forbidden spelling is the same section's "a line of a form the plugin defines, spelt as that form spells it" (`docs/what-a-script-gates.md:16`). The verdict does not change (read).

```seal
confirms: none
```
What matched: a record line that names a `details` tag in prose now meets a refusal that names its path, its line and the tag as read, and says what to do. For `a sentence with </details> inside it` the cause is the record's path and line 3, and its sentence opens "holds `` `</details>` ``" and ends "write it in a code span" (`pr_body.py:470-478`, read; the six new parameters at `tests/skills/test_pr_body.py:363-373` executed green). The instruction is right for every line the reading refuses except one shape, edge 1 below.

```seal
confirms: none
```
What matched: the claim that the six new cases and the two old equality cases are refused at their line, and that a backticked `` `</details>` `` passes and stands in the fold as written. `bin/test tests/skills/test_pr_body.py -q -p no:xdist` passed 31 cases at `02c740e95` (executed). The crafter's seven mutants were not re-run. Reading the pattern settles each: without `re.IGNORECASE` the upper-case line is not matched, `TAG.match` misses a tag after the first character, and each removed lookahead arm misses its one case (read, `pr_body.py:135`, `:470`).

```seal
confirms: none
```
What matched: S5, this work item's records compose with no refusal. `bin/seal pr-body seal/threads/1793588973-pr-body-reads-a-details-tag-as-github-does --body <scratch>/pr-body.md` exited 0 at `02c740e95` (executed, before this record was written), and exited 0 again over the worktree with this record in it (executed). This record writes every `details` tag in a code span.

```seal
confirms: none
```
What matched: no other text states the equality test, under contract rule 19. `git grep` for `FOLD` and `FOLD_END` in Python outside `pr_body.py`, and for a `pr-body` refusal beside a fold or a `details` tag under `docs`, `skills`, `agents`, `templates`, `CONTRIBUTING.md` and `README.md`, found no statement of it (executed). `docs/the-review-record.md:270` states the rule this work holds and needs no change, as `## Rule changes` says. Like the crafter's, this search goes by wording, so the list is a sample.

```seal
confirms: none
```
What matched: each new test was read against its group. The six refused cases are parameters of the existing refusal test. `test_accepts_a_details_tag_in_a_code_span` (`tests/skills/test_pr_body.py:404`) covers the code-span blanking of the tag reading, which no other case in `Test_compose` covers: the case at `:376-381` puts its tag in a fence and its keyword in a span (read). The crafter reports that `bin/seal layout --pairs tests` names no pair in the file (read, `trail/phases/phase-1.md`, not re-run).

```seal
confirms: none
```
What matched: the module docstring's *Limits* (`pr_body.py:48-53`) states both edges of the reading as the frame's probe found them: over-refusal in a table cell, after a backslash, in an indented code block and in an HTML comment, and under-refusal between two backticks GitHub does not read as a span (read, against `frame/design.md:17`). Rule 12's class, the release note's fold in `.github/scripts/publish_release_note.py#release_body`, holds changelog fragments that each pass this refusal at their own pull request (read, `frame/design.md:20`).

```seal
confirms: none
```
What matched: the broad gate's label is honest. `gaps.md` *Not verified* names the full suite, the lint and the typecheck at the last commit, with the orchestrator's `seal gate` as the one to answer them, and the phase record names only its narrow command and checks as run (read).

## Edges weighed and not opened

The owner asked that the review not be overdone. Each edge below was weighed and not opened as a finding, with its grounds.

1. **The sentence says GitHub would read the tag, and for the over-refused spellings GitHub does not.** The *Limits* list names those spellings: a table cell, after a backslash, an indented code block, an HTML comment. The repair the sentence gives is still right for a table cell and a backslash. A record carries no HTML comment, and its reader refuses a line that opens one (`unverified_check.py:614`). Only inside an indented code block would a code span show its backticks. No copied record line at HEAD holds a bare tag (executed, *Probes*), and the frame found none from `v0.25.1` to `HEAD`. A reader who doubts the claim reaches the same repair, so the cost is one look at the docstring.
2. **A code span that a record wraps across two lines.** `SPAN` reads one line at a time (`pr_body.py:470`). A tag inside such a span is refused although GitHub shows it as code, and the writer, told to use a code span, has to join the span onto one line. In the other direction, the closing backtick of the wrapped span and the opening one of a later span on the next line pair up around a bare tag. Such a line passes, though GitHub reads the tag. That falls under the *Limits* sentence on two backticks GitHub does not read as a span, and `_claims` carries the same limit for a closing keyword. It needs a wrapped span and a bare tag on the next line, and no record line shows it.
3. **The name runs to the line's end where no `>` follows.** `[^>]*` names `a sentence <details and more` as "`` `<details and more` ``". The refused set is unchanged, as the phase record says, and the name is the text GitHub would read as the tag's attributes.
4. **Plan A1's verdict cell says GitHub's reading is a subset of the reading** (`frame/plan.md:15`). The escaped-backtick limit qualifies it. The same plan's *Technical context* and the docstring both name the limit, and the copy of the plan in the body is `## Phases` alone.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `02c740e95` | the whole tree | the orchestrator's broad run, `seal gate`, after the rounds settle |
| How GitHub renders each line in the reading and in *Limits*; not probed again this round | `frame/design.md:16-18` | carried from the framer's executed probe; the orchestrator, should a later change alter the reading |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py -q -p no:xdist`, in a `git clone --no-local` at `02c740e95` | exit 0, 31 passed |
| `bin/seal mutate skills/code-review/scripts/pr_body.py --replace '; write it in a code span"' '"' --tests "bin/test tests/skills/test_pr_body.py -q -p no:xdist"`, in the same clone | exit 1, `SURVIVED`: 31 passed against the mutant; the file was restored and the clone's status was clean |
| `bin/seal pr-body seal/threads/1793588973-pr-body-reads-a-details-tag-as-github-does --body <scratch>/pr-body.md`, in the same clone | exit 0, the body written |
| `git grep -n "in a code span" -- tests evals`, in the worktree | no hit in a test of the refusal sentence |
| `git grep -n -i -E` with the reading's pattern over every work item's `changelog.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `trail/rounds/` and `trail/gate.md` at HEAD, keeping only lines with no backticked tag | no line |
