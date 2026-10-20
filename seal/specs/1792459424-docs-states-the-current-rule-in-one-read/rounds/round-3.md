# 1792459424-docs-states-the-current-rule-in-one-read — review round 3

target: 5ddc6b61, fixes 93671fc2..5ddc6b61

## Findings

### 1. `NEAR` takes time exponential in a run of `#`, so a shown line of about 30 hashes stalls `rules --check` instead of answering

severity: should
location: `.github/scripts/rules.py:60`, `tests/test_the_rules_command_reads_each_rule_off_its_test.py:425`
evidence: executed `python3 -I probe/near_time.py <clone>`, `python3 -I probe/near_fix.py <clone>`
verdict: open
regression: round-2#1

The unit is `BLOCK_MARK` at `.github/scripts/rules.py:60`, which 3b01852d
added, read through `NEAR` at line 65. The frame says every line out of
grammar is refused with exit 1 at `<path>:<line>` (`spec.md`, *Data and
interfaces*, the `Refused` clause; `plan.md` phase 1). The fix made the
answer for a run of `#` take time exponential in the run's length. The
defect comes from the `#{1,6}` alternative inside the starred group
`(?:\s|{BLOCK_MARK})*`. A run of n hashes can be split into pieces of one
to six in exponentially many ways, and on a line that holds no label the
engine tries every split before it fails.

Measured on the pattern at 5ddc6b61, each case in a child process with a
10-second timeout, for a line of hashes followed by ` x`:

- 12 hashes: 0.0006 s
- 18 hashes: 0.034 s
- 22 hashes: 0.52 s
- 26 hashes: 8.1 s
- 30 hashes and 60 hashes: past 10 s

Runs of `-`, `*`, `>`, `|` or `1. ` of the same or greater length answer
in under a millisecond, because each of those alternatives matches one
fixed shape. Spaces are quadratic: 5000 spaces take 0.18 s. Only a shown
line is matched (`check_lines` asks `visible` first), so a run of hashes
inside a fence is safe. A shown line of hashes is still ordinary Markdown,
for example a separator a consuming repository writes in `docs/`. On such a
line `rules --check` and `rules <doc>` never answer, and this repository's
case `test_every_check_line_in_the_tree_holds` runs until the suite's
ceiling stops it. Neither is a refusal at the line.

A single `#` in the alternative removes the ambiguity, because the star
already repeats it. On the probe it answers 30, 60 and 5000 hashes in under
a millisecond. It gives the same answer as 5ddc6b61's pattern on every shown
line of the 61 rule files (0 differ). It still refuses every markup spelling
the module's cases name, `####### check:` and `#check:` included. Its
comment says "a heading's `#` run" already, so the comment stands.

```python
BLOCK_MARK = r"(?:#|[-+*]|[0-9]{1,9}[.)]|\[[ xX]\]|>|\|)"
```

The case goes beside `test_a_label_behind_block_markup_is_refused_at_its_line`.
It must be seen red against 3b01852d's pattern, where it times out:

```python
@pytest.mark.parametrize("mark", ["#", "-", "*", ">", "|", "1. ", " "])
def test_a_long_run_of_markup_with_no_label_is_answered_at_once(mark):
    """A run of one mark is matched in one way, so a shown line of markup
    that holds no label is answered in time linear in its length, never in
    time exponential in it."""
    child = (
        "import importlib.util, sys\n"
        "spec = importlib.util.spec_from_file_location('r', sys.argv[1])\n"
        "r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)\n"
        "assert r.NEAR.match(sys.argv[2] * 64 + ' x') is None\n"
    )
    done = subprocess.run(
        [sys.executable, "-c", child, SCRIPT, mark],
        capture_output=True, text=True, timeout=10,
    )
    assert done.returncode == 0, done.stderr
```

`sys` joins the module's imports. The child process holds the timeout, so a
pattern that backtracks fails this one case at 10 seconds and does not stall
the run. Precondition: none beyond the interpreter the suite runs on, since
the child is `sys.executable`.

answer:

## Confirmations

confirms: round-2#1
The close at 3b01852d holds for the class it was asked about (executed,
`probe/near_fix.py` on the pattern at 5ddc6b61). `## check:`,
`- [ ] check:`, `| check:`, `1. check:`, `> check:`, `####### check:` and
`#check:` are all read and refused. The bare `check:` line and the indented
`check:` line still read as check lines. `BLOCK_MARK` holds the markup once.
`skills/settle/SKILL.md:93-95` states the class in one sentence, and the
changelog fragment follows it. `bin/rules --check` reads 240 lines and
exits 0, so no line in the tree is newly refused.
`test_a_label_behind_block_markup_is_refused_at_its_line` pins each of the
five marks at its own line (read,
`tests/test_the_rules_command_reads_each_rule_off_its_test.py:414-436`). The
module passes, 54 passed, and ruff check and format pass on both files
(executed). The backtracking that the same commit brought in is finding 1
above, on its own `regression:` line.

confirms: none
The lines the class now refuses are ones the frame asks it to refuse. A
heading or a table row whose text opens with `Check:`, `Checks:` or
`Enforced by:` is refused at its line in any rule file. `spec.md` *Data and
interfaces* refuses any near miss of the label in any case, and the owner's
direction is that no near miss passes. None stands in this tree (executed,
`bin/rules --check`). A consuming repository with such a heading meets one
refusal that names the line and the spelling it expected. That is the loud
direction, so it is no finding.

confirms: none
The markup the constant still does not list is outside Markdown's block
markup, or is read already. HTML block tags (`<li>`), footnote and
link-reference definitions (`[^1]:`) and a definition list's `:` are not
GFM block markers. An indented code block's line is read as a shown line
and resolved, which is the reading at 75ac6203 as well, so it is not this
fix's. `skills/settle/SKILL.md:93` says "Markdown block markup" without
listing it, and the one list is `BLOCK_MARK`, so no second copy can drift
(read, `.github/scripts/rules.py:58-60`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 5ddc6b61: `unverified` | the branch | the orchestrator, at `broad-gate` once the rounds settle |
| Whether "two hook processes racing for one record" is behaviour the tree cannot observe, carried from round 1 unanswered | `docs/commit-review-gate-spec.md`, the backlog row closed on *Registration* | the framer, through the orchestrator |

## Probes

| Command | Result |
|---|---|
| `python3 -I probe/near_time.py <clone>` (the pattern at 5ddc6b61, each line in a child with a 10 s timeout) | 22 hashes 0.52 s, 26 hashes 8.1 s, 30 and 60 hashes timed out; 60 of `-`, `*` and 2000 of `> `, `\| `, `1. ` under 1 ms; 5000 spaces 0.18 s |
| `python3 -I probe/near_fix.py <clone>` (a single `#` in the alternative) | 30, 60 and 5000 hashes under 1 ms; 0 shown lines of the rule files answered differently; every markup case answered as at 5ddc6b61 |
| `bin/rules --check` | exit 0, all 240 check lines in 61 rule files hold |
| `bin/test tests/test_the_rules_command_reads_each_rule_off_its_test.py -q` | 54 passed |
| `uvx ruff check` and `uvx ruff format --check` over `rules.py` and the rules test module | all checks passed, 2 files already formatted |
