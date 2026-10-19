# 1792366315-the-wardens-real-false-finding-rate-is-unknown — review round 1

target: ef237bf4 against release/v0.22.2

## Findings

The four findings are in cause order. Finding 1 is a defect in the suite
this work adds, and it moves a committed figure. Finding 2 is the generator
path that lets the next entry of the same input file go wrong in two more
ways. Findings 3 and 4 are each a sentence or a field that tells its reader
something false. This round read the branch as `git diff 8a100e13..ef237bf4`,
8a100e13 being where it was cut from `release/v0.22.2`. It is round 1, so no
fact was carried from an earlier round, and every fact below was
re-established here.

### 1. Two replay-1791382684-r5 truths accept every line of a 17-line changelog, so one finding is counted as two

severity: must
location: `evals/scripts/recurred_truths.json:90-130`, `evals/behaviour/warden/replay-1791382684-r5/graders/truth-changelog-history.md`, `evals/behaviour/warden/replay-1791382684-r5/graders/truth-old-phrase-kept.md`, `evals/scripts/replay_targets.py:372-393`, `evals/scripts/replay_targets.py:416-451`, `tests/test_a_rewritten_definition_proved_non_inferior.py`, `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/false-rows.md:183-185`, `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/971-warden-phase-3-864798a4.md:55`, `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/changelog.md:42-43`, `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/overview.md:18-24`
verdict: fixed 11ebe8f4

Why it matters. `spec.md` §*Scope*, *Decided here*, makes a different defect
its own grader so that one find is never counted as another. A truth is
also meant to credit only the defect it names, the first of the risks this
round was asked to look at. Here two truths that the classing keeps apart
cannot be told apart by any `location:` line. The suite this work adds will
decide warden comparisons from the release after 0.22.2. Any run that names
any line of that changelog will be credited with both defects.

Grounds, executed:

- The file both truths point into is 17 lines long at the case's target
  (`git show 97c910d5:seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md | wc -l`
  gave 17). Its first bullet is lines 3-10 and its second lines 12-17.
- `truth_pattern`'s window of 15 lines gives truth-changelog-history
  (`changelog.md:12`) lines 1-27, and the changelog half of
  truth-old-phrase-kept (`changelog.md:7`) lines 1-22. These are the
  committed `pattern:` lines of the two grader files. Both truths therefore
  accept every line of the file.
- The round's probe built one `location:` line for every line each truth
  of each of the nine warden cases at ef237bf4 accepts, then tested it
  against every other truth of the same case. This pair is the only pair
  that shares a line, and it shares 44 of them. The class has this one
  instance.
- The probe then listed every credit that the regrade onto 864798a4 adds,
  with the rows behind it. Phase 3's replay-1791382684-r5 run 0 is credited
  with truth-old-phrase-kept by its row 1 alone, the line that names
  `…/changelog.md:11-16`. `evals/false-rows.md` classes that
  row as r0.F2, the second-bullet finding, and the entry's `from` does not
  list it. No row of that run names `changelog.md:7` or
  `tests/test_a_reader_declares_its_input_class.py`.
- So phase 3's recall under 864798a4, 41/54 in `false-rows.md:185`, the
  changelog fragment's table and `971-warden-phase-3-864798a4.md:55`
  (`truth-old-phrase-kept`, 2 of 2), holds one find the run did not report.
  By the classing the figure is 40/54, with truth-old-phrase-kept at 1 of 2.
  The baseline's 39/54 is unaffected: each of its two runs names
  `changelog.md:7`.

Grounds, read. The account is in `phases/phase-3.md`, under *What the ±15
window does to two truths of replay-1791382684-r5*. It says that a run that
named only the first-bullet defect is credited with both, that every row
involved is `real`, and that S5 therefore holds. It also says a narrower
window would change every truth the generators write. Checked against the
code, neither of the last two settles this. S5's join tests a row's class,
never which defect the class was given for, so it passes over this credit.
A window chosen per entry changes only the entries that carry one, so no
committed case is rewritten. `overview.md` §*Where spec and implementation
diverged* has no row for the choice. It is a conflict between two clauses
of the frame: *locations through `truth_pattern`* in §*Data & interfaces*,
and *a different defect is its own grader*. The account settled it on its
own and recorded it only in the phase file.

The fix gives an entry an optional `window`, narrows the two r5 entries to
it, and adds a test for the class across every warden case. It also
records the field in `overview.md` §*Fed back into the spec*, beside
`widens`.

```python
# evals/scripts/replay_targets.py
def truth_option(location, target, window=WINDOW):
    """`truth_pattern`'s alternative for LOCATION, without the `location:`
    line around it: a line within WINDOW of the one LOCATION names, or of
    the unit's span.

    A location naming no backticked path gives None."""
    m = LOCATION.search(location)
    if not m:
        return None
    path = m["path"]
    lines = None
    if m["line"]:
        line = int(m["line"])
        lines = (line - window, line + window)
    if m["unit"] and path.endswith(".py"):
        source = git("show", f"{target}:{path}", check=False)
        span = unit_span(source, m["unit"]) if source else None
        if span:
            lines = (span[0] - window, span[1] + window)
    if lines:
        numbers = "|".join(str(n) for n in range(max(1, lines[0]), lines[1] + 1))
        return f"{behaviour.js_escape(path)}:(?:{numbers})(?!\\d)"
    return f"{behaviour.js_escape(path)}(?![\\w./#-])"

# in truths_with, the one call that builds an entry's options:
            options.append(truth_option(f"`{location}`", target, e.get("window", WINDOW)))
```

```json
    "grader": "truth-changelog-history",
    "window": 2,

    "grader": "truth-old-phrase-kept",
    "window": 2,
```

With a window of 2, truth-changelog-history accepts `changelog.md:10-14` and
truth-old-phrase-kept accepts `changelog.md:5-9` and the test's lines 4-8
(read, not run). Every row classed for either defect still matches its own
truth. Old-phrase-kept keeps three runs, so it still recurs. Phase 3's run
0 loses the credit above. After regenerating the case, re-run the S5 join,
the regrade of both sides, `compare` and the figures check. Then rewrite
`false-rows.md:185`, the changelog fragment's table, `phases/phase-4.md`'s
figures and the record from what those print.

```python
# tests/test_a_rewritten_definition_proved_non_inferior.py
# What a truth's alternative looks like in its pattern: an escaped path with
# a line list, or a bare escaped path.
OPTION = re.compile(
    r"((?:[\w-]|\\[./-])+):\(\?:([\d|]+)\)\(\?!\\d\)|((?:[\w-]|\\[./-])+)\(\?!\["
)


def test_no_two_truths_of_a_warden_case_accept_one_location():
    """Guards #971 round 1 finding 1: a `location:` line one truth of a
    warden case accepts is accepted by no other truth of that case, so one
    finding is never counted as two."""
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evals", "behaviour", "warden")
    shared = []
    for case in sorted(os.listdir(root)):
        graders = os.path.join(root, case, "graders")
        truths = {}
        for f in sorted(os.listdir(graders)):
            if f.startswith("truth-"):
                with open(os.path.join(graders, f), encoding="utf-8") as h:
                    pattern = ni.grader_from(f"graders/{f}", h.read())["config"]["pattern"]
                truths[f] = re.compile(pattern, re.M)
        for name, found in truths.items():
            for m in OPTION.finditer(found.pattern):
                path = (m[1] or m[3]).replace("\\", "")
                for n in m[2].split("|") if m[2] else [None]:
                    row = f"location: `{path}:{n}`" if n else f"location: `{path}`"
                    others = [o for o, g in truths.items() if o != name and g.search(row)]
                    if others:
                        shared.append((case, name, row, others))
    assert not shared, shared[:3]
```

answer: Fixed as the round proposed, test first. At 11ebe8f4, `truth_option` takes a `window` and `truths_with` reads an entry's `window` (15 where it names none). truth-changelog-history now reads `changelog.md:12-17` and truth-old-phrase-kept `changelog.md:7` and the test's `:6`, each with window 2. Only those two grader files of replay-1791382684-r5 changed (`git diff --name-only 864798a4 11ebe8f4 -- evals/behaviour`, executed). `test_no_two_truths_of_a_warden_case_accept_one_location` was red at f9f53f3c, naming this pair, and is green at 11ebe8f4; `test_an_entry_window_narrows_the_lines_its_truth_accepts` pins the field, and `test_an_entry_the_case_cannot_take_stops_the_generator[a-window-that-is-no-count]` (05715164) its refusal, seen red by mutation. In 4116d2a5 both sides were regraded onto 11ebe8f4 and `compare` wrote `971-warden-phase-3-11ebe8f4.md`: truth-old-phrase-kept passes 1 of 2 new runs, `check` exits 0. Phase 3's recall is 40/54 in `false-rows.md`, the changelog fragment's table and `phases/phase-4.md`; the 864798a4 sides and record were removed. The S5 join, the figures check and the phase 1 join exit 0 as written. `overview.md` carries the divergence row and the `window` clause under Fed back into the spec, marked inferred during implementation. The S5 join and the figures check in `phases/phase-3.md` and `phases/phase-4.md` now name 11ebe8f4, and those records say why.

### 2. An input-file entry with no locations becomes a truth every row matches, and a range keeps only its first line

severity: should
location: `evals/scripts/replay_targets.py:416-451`, `tests/test_a_rewritten_definition_proved_non_inferior.py:1758-1775`
verdict: fixed 11ebe8f4

Why it matters. The input file is where the next truth will be added by
hand, and `truths_with` is the only check between that file and the suite.
`spec.md` §*Data & interfaces* says an entry takes `path`, `path:line` or
`path:first-last`. The docstring of `truths_with` says any other location
stops the run. Two entries pass that check and still write a wrong truth,
with no message.

Grounds, executed. The round's probe called `truths_with` for
rule-warden-one-finding with a temporary input file:

- `"locations": []` gave the pattern `^location: .*(?:)`, which matched a
  row naming `anything/else.md:3`. A truth like that turns every row of
  its case to found, `wrong` rows included.
- `"locations": ["src/x.py:10-100"]` gave `src/x.py` lines 1-25, which
  matched neither a row naming `src/x.py:60` nor one naming
  `src/x.py:100`. The range was accepted and silently narrowed to the
  window around its first line.

Grounds, read. No entry of `recurred_truths.json` has either shape today,
so no committed truth is wrong. The stale-entry cases at
`tests/test_a_rewritten_definition_proved_non_inferior.py:1758-1775` cover
neither shape.

```python
# evals/scripts/replay_targets.py, in truths_with, replacing the loop over
# e["locations"]; `re` and `behaviour` are already imported in this module.
        options = []
        for location in e["locations"]:
            m = LOCATION.fullmatch(f"`{location}`")
            if not m or m["unit"]:
                raise SystemExit(
                    f"{case}: {e['grader']} names `{location}`, no coordinate"
                )
            last = re.search(r"[-\N{EN DASH}](\d+)$", location) if m["line"] else None
            if last:
                lines = range(max(1, int(m["line"]) - WINDOW), int(last[1]) + WINDOW + 1)
                numbers = "|".join(str(n) for n in lines)
                options.append(f"{behaviour.js_escape(m['path'])}:(?:{numbers})(?!\\d)")
            else:
                options.append(truth_option(f"`{location}`", target))
        if not options:
            raise SystemExit(f"{case}: {e['grader']} names no location")
```

Where finding 1's `window` field is taken, the range branch reads it in
place of `WINDOW`. The parametrized stale-entry test gains one row, with
the id `no-location`:

```python
        ({"locations": []}, "names no location"),
```

A case of its own pins a range entry whose truth matches the range's
last line:

```python
def test_an_entry_range_is_read_to_its_last_line(tmp_path, monkeypatch):
    """Guards #971 round 1 finding 2: a `path:first-last` location credits
    a row at its last line, not only around its first."""
    truths = rule_truths(tmp_path, monkeypatch, entry(locations=["src/x.py:10-100"]))
    found = truth_regex("truth-no-case.md", truths["truth-no-case.md"])
    assert found.search("location: `src/x.py:100`")
    assert not found.search("location: `src/x.py:200`")
```

answer: Fixed test first at 11ebe8f4. `truths_with` refuses an entry with no location, exit 1 with `names no location`. A `path:first-last` location accepts every line of its range and the window either side, through the new `lines_option`, which `truth_option` uses too, so no committed truth's bytes moved. The stale-entry test gained the `no-location` row, and `test_an_entry_range_is_read_to_its_last_line` pins the range at lines 60, 115 and not 116 of `src/x.py:10-100`. Both were red at f9f53f3c and green at 11ebe8f4 (executed). The docstrings of `recurred_truths` and `truths_with` and the README's paragraph state both.

### 3. A side regraded twice says it ran the suite it was first regraded onto

severity: should
location: `evals/scripts/noninferiority.py:1324-1329`, `tests/test_a_rewritten_definition_proved_non_inferior.py:1228-1252`
verdict: fixed 11ebe8f4

Why it matters. `specseal.regraded_from` is how a regraded side is kept
from passing for a side that ran the suite it now names. `overview.md:84`
says so, and the changelog fragment (`changelog.md:8`) says it names the
suite the side ran. From the release after 0.22.2, the next suite change
will regrade the sides this work commits, as this work regraded #957's.
Each of those sides then states that its runs answered 864798a4, a suite
they never ran.

Grounds, executed. `noninferiority.py regrade --side
seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/warden-phase-3-864798a4.json
--suite-rev 864798a4` exited 0. The committed side holds `regraded_from`
af9c924b; the side written holds 864798a4.

Grounds, read. `regrade` sets `regraded_from=own`, and `own` is the side's
`suite_rev`, which a previous regrade has already replaced.

```python
    out["specseal"] = dict(
        out.get("specseal", {}),
        suite_rev=target,
        suite_tree=suite_tree(target, agent),
        # The suite the runs answered, kept through any number of regrades.
        regraded_from=meta.get("regraded_from") or own,
    )
```

```python
# at the end of test_a_side_regraded_onto_a_wider_truth_counts_the_row_it_now_matches
    again = tmp_path / "again.json"
    assert regrade(str(out), commits["wide"], again) == 0
    second = json.loads(again.read_text(encoding="utf-8"))
    assert second["specseal"]["regraded_from"] == commits["own"]
```

answer: Fixed test first at 11ebe8f4: `regrade` writes `regraded_from=meta.get("regraded_from") or own`, with a comment saying why. The second regrade the round proposed closes `test_a_side_regraded_onto_a_wider_truth_counts_the_row_it_now_matches`, red at f9f53f3c and green at 11ebe8f4 (executed). Both committed sides at 11ebe8f4 hold `regraded_from` af9c924b (executed). The README's `regrade` paragraph, the changelog fragment and `overview.md`'s clause now say the first suite is kept.

### 4. The changelog fragment says one of 0.22.2's comparisons passes --suite-rev af9c924b, where two do

severity: should
location: `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/changelog.md:45-51`
verdict: fixed 4116d2a5

Why it matters. The paragraph tells a release reader which of 0.22.2's
comparisons the new suite cannot reach. It names four, then says "One of
them passes `--suite-rev af9c924b` and is unaffected". A reader takes that
to mean the other three are exposed to the refusal described in the next
sentence.

Grounds, executed. `gh issue view 968` and `gh issue view 970` each hold, at
body line 11, "The suite stays af9c924b's (`--suite-rev af9c924b`) for every
issue". `gh issue view 985`, at body line 19, measures "on af9c924b's
suite". Grounds, read: `plan.md` §*Operational impact* already says "#968
and #970 name `--suite-rev af9c924b` in their bodies".

```markdown
- **The new suite is the one a warden comparison uses from the release
  after 0.22.2, and 0.22.2 decides nothing on it.** By the owner's
  decision in #971, 0.22.2's comparisons stay on af9c924b's suite: #968,
  #970, #985 and the milestone's closing verdict. #968's and #970's bodies
  pass `--suite-rev af9c924b`, and #985's measures on af9c924b's suite, so
  each is unaffected. A comparison against an af9c924b baseline that
  passes the default `HEAD` meets the new suite, and `compare` refuses it.
```

answer: Fixed at 4116d2a5 with the round's sentence: #968's and #970's bodies pass `--suite-rev af9c924b`, and #985's measures on af9c924b's suite, so each is unaffected (`gh issue view 968`, `970` and `985`, executed: line 11, line 11 and line 19). No other text of the branch says one of them does (`git grep -n -i -e "one of them passes"` exits 1, executed).

## Confirmations

confirms: none
S1 holds. The phase 1 join, run as written in `phases/phase-1.md` in a clone
at ef237bf4, exited 0 (executed). It checks the 74 rows one to one against
the rows recomputed from both committed sides, and the totals.

confirms: none
S5 holds as the frame states it. The phase 3 join, run as written, exited 0
and printed `problems: 0` (executed). Every entry's grader passed in at
least two runs: truth-cutoff-in-docs, truth-host-prefix,
truth-manifest-not-object and truth-docstring-pipeline in two, the rest in
three or four. Finding 1 is what this condition cannot see.

confirms: none
S3 and the committed sides hold. In-process `regrade` onto af9c924b gave
55 rows with 43 false, and 47 with 31 false, both exit 0. Onto 864798a4 it
wrote files byte for byte equal to the committed
`baseline-warden-864798a4.json` and `warden-phase-3-864798a4.json`
(executed).

confirms: none
S4's suite refusal holds against a real tree. A commit in the clone
changing `rule-warden-one-finding/prompt.md` made `regrade` of the baseline
side onto it exit 2, naming the case, with nothing written (executed). The
module's thirteen parametrized refusals cover the rest, and
`bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q`
passed 98 (executed).

confirms: none
S6 holds. `replay_targets.py --case` for the four replay cases, in a
`--shared` clone where their targets resolve, `seed_defects.py --case` for
the four seeded cases and `rule_cases.py` all exited 0. Afterwards
`git status --porcelain` was empty (executed).

confirms: none
S7 holds. The framer's, smith's and sealer's suite trees are the same hash
at 8a100e13 and ef237bf4. Every path under `evals/behaviour/` that the
branch changes is a `graders/truth-*` file (executed).

confirms: none
The account says `verdict` is unchanged. An AST comparison of every
top-level function of `noninferiority.py` at 8a100e13 and ef237bf4 shows
`main` as the only existing function changed (executed). The thirteen
added ones are `regrade`'s.

confirms: none
The figures check of `phases/phase-4.md` exited 0, and `noninferiority.py
check` over `971-warden-phase-3-864798a4.md` exited 0 (executed). Both
recompute what is committed, finding 1's credit included.

confirms: none
S2 holds for every `wrong` and `unclear` row and for a sample of the
`real` rows that became truths. Each named command, re-run, gave what its
row says (executed):

- phase 3's `wrong` row: `git cat-file -e 7ef6abbf:docs/the-review-record.md`
  exits 128, and `TARGET = "Target SHA"` is at chain_check.py:379.
- the baseline's `wrong` row: at ad447367, the module
  `tests/test_a_range_owns_what_git_lists_for_it.py` passed 7 of 7, and
  failed 7 of 7 with the scaffold's seed applied at chain_check.py:4647.
- the baseline's `unclear` row: :23 and plan.md:56.
- `real` rows: `now defines` at :13, `rest.startswith` at :76-77,
  `except (OSError` at :297, cmdline.py's two `Refused:` paragraphs and two
  `isabs` checks, `NOTES_FROM = 1791384163` against `1791384154` in
  spec.md:92 and :161 and plan.md:114, `git diff --quiet 7608d82c` exiting
  1 at 97c910d5 and 0 at ef8fb33c, and `inspect`'s two calls at :197 and
  :203.

confirms: none
The two widenings come from the historical record. The fix block of round
2's should 1 (`git show b914a1c7^:` that record, lines 40-95) lists every
unit truth-1 gains, by coordinate and name. Each name is the unit defined
at that line at 7ef6abbf (executed). The same block lists
`unverified_check.py:767 parse_section` and gives its class to should 2,
which is truth-2.

confirms: none
Each new test was read against its group in
`tests/test_a_rewritten_definition_proved_non_inferior.py`. The regrade
cases cover the new subcommand, which no earlier case reaches. The
generator cases cover `truths_with`, beside the earlier `truth_pattern`
cases they call into. None covers only what an earlier case already does
(read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The finding wording behind every class. The commands of each re-checked row agree with its class, but what each finding said survives only in #971's first comment | `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/false-rows.md` | the repository owner, who wrote the comment |
| Five credits under 864798a4 rest on rows no entry's `from` names: the baseline's replay-1791382684-r2 run 1 truth-step-refused (row 0), phase 3's replay-1791382684-r2 runs 0 and 1 truth-2 (rows 0 and 2, and row 0), and phase 3's seeded-9b644676 runs 0 and 1 truth-no-commit-unpinned (row 0 of each, the seeded finding citing the test at :200). S5 tests only rows that turn from false to found, and these rows were already found or were classed for another defect. Whether each names that truth's defect rests on wording that is gone, so the frame decides whether a credit must be tied to a `from` row | `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/phases/phase-3.md` | the repository owner |
| truth-direction-unplaced rests on the comment's reading of the inventory rows, and its own row calls it "the weakest candidate" | `evals/scripts/recurred_truths.json` | the repository owner |
| The full suite, the repository-wide lint and the typecheck over this branch. This round ran one module and no broad run | the branch | the orchestrator, through `broad-gate` |
| What `release/v0.22.2` gained after 8a100e13 (#978, assets). This round read the branch against 8a100e13 | `release/v0.22.2` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `test_tmp_round1.py`, one file at a `--no-local` clone's root at ef237bf4, run once and deleted | The three documented joins each exited 0. Regrading onto af9c924b gave 55/43 and 47/31, and onto 864798a4 gave files byte-equal to the committed sides. The new-credit listing named phase 3's r5 run 0 truth-old-phrase-kept from row 1 alone (finding 1), and five credits from rows no `from` names. The overlap scan of nine cases found one shared pair, 44 lines (finding 1). `truths_with` on `[]` gave `(?:)`, and on a range gave its first line's window (finding 2). A prompt change refused with exit 2. Only `main` changed among existing functions. The other agents' suite trees were unchanged |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q` | 98 passed |
| `seed_defects.py --case` for the four seeded cases, and `rule_cases.py`, in the `--no-local` clone; `replay_targets.py --case` for the four replay cases, in a `--shared` clone, since their target commits are unreachable in a `--no-local` one | All exited 0; `git status --porcelain` was empty after each |
| `noninferiority.py regrade --side …/warden-phase-3-864798a4.json --suite-rev 864798a4` | exit 0; `regraded_from` 864798a4, where the committed side holds af9c924b (finding 3) |
| `noninferiority.py check …/971-warden-phase-3-864798a4.md` | exit 0 |
| `python -m pytest -p no:xdist tests/test_a_range_owns_what_git_lists_for_it.py` at ad447367 in the `--shared` clone, unseeded and then with the seed made through the Edit tool and restored | 7 passed; 7 failed |
| The S2 `git grep`, `git cat-file` and `git diff --quiet` commands listed under the confirmation of S2 | Each gave what its row says |
