# 1792459424-docs-states-the-current-rule-in-one-read — review round 1

target: 75ac6203 against release/v0.22.3

## Findings

### 1. The durations case fails at the target: 373 of 7284 collected cases have no price in `.test_durations`

severity: must
location: `.test_durations`, `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:344`
evidence: executed `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite`
verdict: open

The suite is red at 75ac6203 on every leg that collects the whole suite.
`test_the_durations_file_prices_the_suite` allows 5% of the collected cases
to carry no price. Run in the round's clone at 75ac6203, it fails with "373
of the 7284 collected cases (5.1%) have no price in .test_durations". The
branch is the cause. It retires
`tests/test_a_folded_statement_names_what_enforces_it.py` and the marker and
shape cases, rewrites the rules command's module, and adds parametrized cases
to the settle and fold modules. Every new node id is unpriced until the file
is refreshed. The orchestrator relayed the same failure from CI run
39368250047 at ebcb4257, on ubuntu, one macOS split and one Windows split. A
refresh, 0398a18b, landed after this target. The fix pass names it once the
next round has read it.

```sh
gh run download 39368250047 -n test-durations -D /tmp/x/durations
mv /tmp/x/durations/.test_durations .test_durations
git -C <the branch worktree> commit -m "chore: .test_durations prices the cases #941 added (#941)" -- .test_durations
```

answer:

### 2. A `## Rule changes` holding `- nothing` twice passes, and the second item is never read

severity: should
location: `skills/settle/scripts/rule_changes.py:139-175`, `tests/test_settle_applies_rule_changes_in_place.py:235`
evidence: executed `python3 -I -c "rule_changes.parse('## Rule changes\n\n- nothing\n  why: a\n- nothing\n  bogus: x\n', 'docs')"`
verdict: open

`skills/settle/SKILL.md:56` says the `nothing` item "stands alone in the
section", and the changelog fragment says the block "stands alone in its
section". The parser refuses `- nothing` beside an operation (line 139), but
it does not refuse a second `- nothing`. The loop at line 148 returns at
line 175 on the first `nothing` item, so a second one is never checked. With
a second `- nothing` carrying an unknown field `bogus:`, `parse` returns
`Parsed(ops=[], nothing='a', errors=[])`. That is a block the reader cannot
read, passed in silence: the same class as the beside-an-operation case the
branch refuses, and no case pins it.

```python
    blocks = [item for item in ops if item["kind"] == NO_CHANGE]
    if blocks and len(ops) > 1:
        extra = next(item for item in ops if item is not blocks[0])
        return Parsed(
            [],
            None,
            [(extra["line"], f"`- {NO_CHANGE}` is the section's one item")],
        )
```

This replaces lines 139 to 145. The case goes into the parametrized refusal
list beside "the block beside an operation":

```python
        (
            "- nothing\n  why: a reason.\n- nothing\n  why: another.",
            "- nothing",
            "`- nothing` is the section's one item",
        ),
```

with the id `"the block twice"`. The `bad` line is the second `- nothing`,
so the case finds it by its line number and not by its text.

answer:

### 3. The rewritten one-root document says a round record carries `Target SHA`, a spelling the round grammar refuses

severity: should
location: `docs/one-root-by-lifetime.md:33`, `docs/one-root-by-lifetime.md:48`, `docs/one-root-by-lifetime.ko.md:33`, `docs/one-root-by-lifetime.ko.md:46`
evidence: read `docs/one-root-by-lifetime.md:33`, `docs/one-root-by-lifetime.md:48`, `docs/one-root-by-lifetime.ko.md:33`, `docs/one-root-by-lifetime.ko.md:46`, `docs/the-review-record.md:41`, `docs/the-review-record.md:53`
verdict: open

Scope 4 says every rewritten document states the current rule. The
dependency rule names "a round record's `Target SHA`" twice in each edition.
In `docs/the-review-record.md:41` a round record carries a `target:` line.
Row 53 lists `Target SHA:` as `nowhere`, "the old spelling of `target:`".
The rewrite carried the old name over from the base text
(`docs/one-root-by-lifetime.md` at ac83bdf3, lines 174 and 206). An agent
reading the rule looks for a field the record no longer holds.
`Target SHA` stays correct where it names the guarantee's row
(`docs/the-commit-gate-inside-git.md:96`, `docs/the-review-record.md:324`).
No other `docs/` file names it for a round record (`git grep -n 'Target SHA'`
over `docs`).

```markdown
treats it as already gone. A round record's `target:` line is read only while
...
record's `target:` line, read while its pull request is open and gone with the
```

```markdown
없는 것으로 취급합니다. 라운드 기록의 `target:` 줄은 그 PR 이 열려 있는
...
무엇이든 같은 식으로 깨집니다. 남은 묶임은 라운드 기록의 `target:` 줄 하나이고,
```

Both editions are re-wrapped in place. The outline is unchanged, so
`tests/test_both_editions_carry_the_same_folds.py` is unaffected.

answer:

### 4. The check-line reader neither reads nor refuses a check line behind an ordered-list or blockquote marker, and it accepts extra spaces after `reader:`

severity: should
location: `.github/scripts/rules.py:60-62`, `.github/scripts/rules.py:146-154`, `tests/test_the_rules_command_reads_each_rule_off_its_test.py:399`
evidence: executed `python3 -I -c "rules.NEAR.match(c); rules.line_problems('.', c)" over 18 spellings`
verdict: open

The owner's direction is that no spelling a near miss could pass. The
branch's own S5 refuses a bullet in front (`- check:`). The same class, a
block marker in front of the label, is not covered. `1. check:
tests/nope.py` and `> check: tests/nope.py` do not match `NEAR`. They are
not read and not refused, so a rule written that way carries a target
nobody resolves. Separately, `parse` strips the reader (line 147), so
`check: none reader:  x` with two spaces passes. `skills/settle/SKILL.md:85`
says the no-target form is "written exactly" and that targets are separated
by single spaces, and two spaces between targets are already refused (line
157). Against the tree, the widened pattern below matches no shown line of
any rule file that the current one misses, so it refuses nothing standing
today (the probe's second command).

```python
NEAR = re.compile(
    r"^\s*(?:(?:[-+*]|[0-9]{1,9}[.)]|>)\s*)*[*_]*\s*(?:checks?|enforced\s+by)\s*[*_]*\s*:",
    re.IGNORECASE,
)
```

```python
    if value == "none" or value.startswith("none "):
        reader = value[len(NO_TARGET) :]
        if not value.startswith(NO_TARGET) or not reader or reader != reader.strip():
```

The cases to add to `test_every_other_spelling_is_refused_at_its_line`:
`1. check: tests/test_x.py`, `> check: tests/test_x.py`, and
`check: none reader:  review`. Each needs to be seen red against the
current code first.

answer:

### 5. Two worked-example issue numbers stay in a rewritten document, though Scope 4 says they leave

severity: should
location: `docs/issues-and-milestones.md:301`, `docs/issues-and-milestones.md:303`
evidence: executed `git grep -nE '#[0-9]+' HEAD -- 'docs/*.md' ':!docs/experiments'`
verdict: open

Scope 4 says issue numbers that a sentence can stand without leave the
document. Phase 7's record says its three documents dropped their issue
numbers, but two remain in `docs/issues-and-milestones.md`. "#136 is the
worked example." is a sentence with no content except the number. "#30 is
the worked example: ..." carries a rule that stands without it. `#51` at
line 305 names the live log that the rule describes, so it stays. The
`Closes #88` and `Closes #153 and #150` lines are examples of the syntax,
so they stay too. Phase 7's census has no row for either sentence.

```markdown
- **Consolidate the body**, once the design is settled. The comments stay and
  are still part of the issue; what goes away is the need to cross-check four
  places to learn what the ticket asks for.
- **Leave the body and open it with `> **Update <date>.**`**, naming what has
  moved since it was written: the original design is preserved and the block
  says which things below it have changed.
```

answer:

## Confirmations

confirms: none
S7, the census, holds (executed, the round's census probe). The base had
243 label lines in the rule files, not the frame's 240. `git grep -E '^\s*'`
misses the three lines indented under list items at
`docs/the-record-layout.md` lines 181, 201 and 208 of ac83bdf3, and
`[[:space:]]` counts 243. `overview.md`'s first divergence row says the
same. The head has 240 check lines, the count `bin/rules --check` reports.
Every target path a base line named is still named by a check line or by a
marker's carrier, except three that `## Removes` names:
`skills/settle/scripts/fold_check.py`,
`tests/test_a_folded_statement_names_what_enforces_it.py`, and
`tests/test_docs_line_wrap.py`, whose one base rule was the fold-marker
exemption. Each marker in `docs/the-review-record.md` is carried by exactly
the base's `::name` tests (`rules.markers` read against the base lines).

confirms: none
`bin/rules --check` exits 0, with "all 240 check lines in 61 rule files
hold". `bin/fold-check` exits 0, holding 17 documents, none past 25000, and
the index names every one (S9). No fold marker line, section sign, arrow
or symbol heading is left under `docs/` outside `docs/experiments/` (S8,
executed grep).

confirms: none
S11 and S12 hold, and the held count reconciles (executed). `bin/settle
--released-at HEAD` holds 35 directories: 33 backlog, plus #953's and this
item's. That set equals the set of directories that
`unverified_check.py --baseline origin/main seal/specs/` reports with an
open row. The per-phase counts 4, 2, 10, 2, 13 and 5 sum to 36. Phase 6's
ten include `1791384161` and `1792367880`, which phase 7 closed with limit
sentences in its own documents. Phase 8's thirteen include `1791876666`,
which phase 9 closed on the durations refresh. 36 - 3 = 33, and every one
of the 33 is named in a phase record.

confirms: none
S13 holds (executed). `unverified_check.py --baseline
origin/release/v0.22.3 seal/specs/` and `--baseline origin/main` both exit
0, and each names seven removed overviews as settled. `origin/main` is
adac0891 and `origin/release/v0.22.3` is ac83bdf3, both checked with
`git ls-remote`. The only file outside `seal/` that still names a removed id
is a docstring pointer (`tests/test_a_declared_label_reaches_the_tracker.py:42`).

confirms: none
The reframe at 75ac6203 describes the build and does not bend the frame.
S11 and S12 now allow directories held for a row that no closer closes.
The frame already said so at 98a0efa2: "A row none of these closes stays
open, and its directory stays, named in the phase record" (`spec.md:177` at
98a0efa2). The original S11 and S12 contradicted that clause, and the
revision resolves the contradiction toward it. The S13 change states a fact:
`1791019421` held no `overview.md`.

confirms: none
The sampled closers are facts a reader can open (executed). #589, #608, #683,
#937, #972 and #997 are merged pull requests (`gh pr view`). 8350c578,
149ca9ec, af9c924b, aadf2efb, 5b1f6fae and f1c9932d are ancestors of the
target. The limit sentence that three rows close on stands in
`docs/commit-review-gate-spec.md` *Registration* (read, lines 20 to 32). No
typecheck is configured (`seal/config.md` `Broad gate` row), so "the
repository configures no typecheck" is true.

confirms: none
S14 holds (executed). None of the 38 base heading texts that were removed or
renamed appears as a citation outside `seal/` and `changelog/`. The
`hooks/root-migrate.py` citation was moved to *What first setup asks*. A
resolver over every `docs/<file>.md` plus italic-heading citation in the
tree finds no unresolved citation this branch made. The ones it does find
fail the same way at ac83bdf3.

confirms: none
The sampled rewrites keep their rules. In `docs/commit-review-gate-spec.md`,
the unresolvable-`cd` table, the reserved-word, wrapper and substitution
readings, and the heredoc shape stand with their check lines (read, lines
34 to 191). The worktree guard's Agent path keeps "counts no session, asks
once, and reads no token" (`docs/worktree-guard-spec.md:167`). The one-root
document keeps the dependency rule, the opt-in signal, first setup and the
config rows.

confirms: none
The reader modules pass: `tests/test_the_rules_command_reads_each_rule_off_its_test.py`,
`tests/test_settle_applies_rule_changes_in_place.py`,
`tests/test_a_document_has_room_for_the_next_fold.py`,
`tests/test_both_editions_carry_the_same_folds.py`,
`tests/test_docs_line_wrap.py` and
`tests/test_a_unit_is_bounded_where_a_parser_decides.py`, 242 passed
(executed). `ruff check` over `rules.py`, the settle scripts,
`coordinates.py`, `unverified_check.py`, `tests/conftest.py` and the rules
test module finds nothing. The em-dash form, a missing `why:` and an empty
`why:` are each refused at their line (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether "two hook processes racing for one record, run for real" is behaviour the tree cannot observe, which is what the closing rule requires before a limit sentence may close a row. A case could spawn two processes, and the row was closed on the limit sentence in *Registration* | the backlog overview row closed on `docs/commit-review-gate-spec.md` *Registration*, `spec.md` *Closing a backlog row* | the framer, through the orchestrator |
| Whether any rule an agent needs was lost from the 17 rewritten documents outside the three sections sampled above. Not every document was read whole against its base | `docs/` | the next round's warden |
| The 51 modules that read `seal/specs`, over the corpus without the eight directories. Phase 9 claims 3085 passed; this round did not run them | `seal/specs/1792459424-docs-states-the-current-rule-in-one-read/phases/phase-9.md` | the orchestrator, at `broad-gate` |
| The full suite, the repository-wide lint and the typecheck: `unverified` | the branch | the orchestrator, at `broad-gate` once the rounds settle |
| `rules --check` and the marker walk on Windows. The orchestrator relayed that run 39368250047 passed every leg except the durations case; this round did not read that run | `overview.md` *Not verified* | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `python3 -I probe/census.py <clone>` (base label lines against head check lines, marker carriers resolved) | 243 base lines, 240 head lines; dropped targets were only `fold_check.py`, `test_a_folded_statement_names_what_enforces_it.py` and `test_docs_line_wrap.py` |
| `python3 -I probe/markers_vs_base.py <clone>` | each marker's carriers equal the base's `::name` tests for the paired lines |
| `python3 -I -c "rules.NEAR.match(c); rules.line_problems('.', c)"` over 18 spellings | `1. check:` and `> check:` not read; `check: none reader:  x` passes; the rest refused or held as S5 states |
| the widened `NEAR` pattern over every shown line of the rule files | no line it matches that the current pattern misses |
| `python3 -I -c "rule_changes.parse(...)"` over 9 bodies | a second `- nothing` with a `bogus:` field returns `nothing='a'` and no error; the others refused or read as documented |
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` | exit 1: 373 of the 7284 collected cases (5.1%) unpriced |
| `bin/test` over the six reader modules | 242 passed |
| `bin/settle --released-at HEAD`; `unverified_check.py --baseline origin/release/v0.22.3` and `--baseline origin/main` over `seal/specs/` | exit 0 each; 35 held, 7 settled |
| `python3 -I probe/citations.py <clone>`; `git grep -F` of 38 removed heading texts | no stale citation this branch made |
