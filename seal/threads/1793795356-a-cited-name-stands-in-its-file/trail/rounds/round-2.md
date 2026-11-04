# Review round 2: 1793795356-a-cited-name-stands-in-its-file

```seal
target: 6b442e66f, fixes d9bce5d49..6b442e66f
```

This is a verifying round. Its target is `git diff d9bce5d49..6b442e66f`: the fix commit `2b1db715b`, the closing memo's row closed at `23f27bbc8`, and round 1's close block at `6b442e66f`. It was read in a `git clone --no-local` of the branch worktree, checked out at `6b442e66f`, under the round's scratch directory. `seal/parity.md` is not declared, so no `original:` line is owed. `seal/config.md` has no `Record language` row, so the record is in English. The round stays inside the fix diff, and the one new unit in it is `holds`.

Carried from round 1 as coordinates, not re-established: `rules.pending` and `rules.removed_by` in `skills/settle/scripts/rule_changes.py`, which round 1 read at lines 569-586 and which the fix diff does not touch; `NAME_TOKEN` and its look-behind at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:254-257`, which round 1 compared on six strings and the fix diff does not touch; and the S9 fixture `POLICY_CITING` and `pending` at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:782-822`, which the new entries reuse. Round 1's verdicts on the four rewritten sentences, on A3 and on the tree case stand outside this diff, so this round does not repeat them. It re-derived the tree case by running the module whole.

The axes walked were Inputs (what `holds` reads from a `from` and a `to`, including `None`), Exclusions and boundaries (a token whose name runs on, a token under a longer path, a token at a commit, a token followed by `.` or `/`), and Test quality (whether each direction `holds` now decides is held by a case). One axis is this change's own: whether the release note's sentences about the fix and about the five places say what the tree shows.

## Findings

### 1. No case holds the path side of `holds`, so a reader bounding only the name's end keeps all 53 cases green

```seal
severity: should
location: `tests/behaviour/test_a_cited_section_stands_in_its_file.py:184-193`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:825-862`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:885-934`
evidence: executed `bin/test tests/behaviour/test_tmp_round2_probe.py -q -s -p no:xdist` (the probe below, since deleted), and `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist` with line 193 replaced by an end-only bound, 53 passed, the line restored after; read `tests/behaviour/test_a_cited_section_stands_in_its_file.py:184-205`
regression: round-1#1
```

The unit is `holds`, at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:184-193`, added by `2b1db715b`. `frame/design.md` *Scope* item 1 excuses a citation that a pending rule change corrects, and item 3 holds that excuse by entries in S9's tables. The fix reads a token whole at both ends but adds entries for the name's end only. So the defect comes from round 1's paste-ready entries, applied as given, which covered the suffix direction while round 1's own grounds also named the path direction ("as `lib/x.py#y` to `hooks/lib/x.py#y`").

Why it matters: `holds` now decides two more directions than the substring test did, and the module holds neither. The probe ran four versions of `holds` over the module's four name entries and four more inputs (executed):

- A `to` that moves the cited path under a longer one, from "See `manual/b.py#gone`." to "See `lib/manual/b.py#gone`.", corrects the citation. HEAD's `holds` excuses it. The substring test refused it.
- A `from` holding "See `lib/manual/b.py#gone`." does not hold the citation of `manual/b.py#gone`. HEAD's `holds` leaves line 11 dangling. The substring test excused it.
- A version that bounds only the name's end, `re.search(re.escape(cited) + r"(?!\w)", flat)`, gets all four of the module's name entries right and both directions above wrong. With that line in place at line 193, the module passed 53 of 53 (executed). The next edit that simplifies `holds` to a regular expression would bring back half of round 1's finding with the suite green.

The fix pass's hand-back says this was left unverified: no case pins `holds`' docstring claim that `lib/manual/b.py#gone` does not hold `manual/b.py#gone`. That label is honest, and the probe confirms the claim is true at HEAD and unpinned. `gaps.md` does not carry it, so the claim reaches no later reader. Under `skills/code-review/SKILL.md` *The record*, this is a behaviour the diff changed that no case then holds, so it is a `should` and not a gap named in prose.

The fix adds one entry to each S9 table. Both were red against the end-only version and against the substring test in the probe, which is how contract rule 15 has them seen before they are planted:

```python
# In EXCUSING, after "a change that renames the name to a longer one":
    "a change that moves the name's file under a longer path": (
        "docs/a.md",
        op("change", "Old section", NAME_OLD, "See `lib/manual/b.py#gone`."),
        None,
        "name",
    ),
# In REFUSING, after "a from that holds a longer name":
    "a from that holds the name under a longer path": (
        "docs/a.md",
        op("change", "Old section", "See `lib/manual/b.py#gone`.", NAME_NEW),
        "name",
    ),
```

The snippet reaches every statement of the fact this round found. The `holds` docstring already states both directions. The changelog sentence at `seal/threads/1793795356-a-cited-name-stands-in-its-file/changelog.md:3` gives only the rename example and stays true. A third input changed with the fix as well: a `to` that rewrites the citation as `abc1234:manual/b.py#gone` is now excused, where the substring test refused it (executed). No entry is proposed for it, since `frame/design.md` *Out* leaves every `<commit>:<path>` to #1355.

```seal
verdict: fixed f9a92629c
answer: The finding holds. `holds` read the token whole, but no case held the path side, which `frame/design.md` *Data & interfaces* ("`excuser` takes the cited text as written") asks for as part of the whole token. I added the round's two entries as given. "a change that moves the name's file under a longer path" goes in `EXCUSING`, and "a from that holds the name under a longer path" goes in `REFUSING`. Against `f9a92629c`, `bin/seal mutate` replaced the last line of `holds` with each of the two alternatives, and both runs came back `red` with the tree clean after the restore (executed). With the substring test, all four entries that bound a name failed. With the end-only `re.search(re.escape(cited) + r"(?!\w)", flat)`, exactly the two new path-side entries failed. The citation module passed 55 cases, and the plan row's six modules passed with two record readers (executed). The `<commit>:<path>` input the round names stays unpinned, as `frame/design.md` *Out* leaves it to #1355.
```

### 2. The release note says no tracked file binds the five cited names, and two of them are bound in the tree

```seal
severity: should
location: `seal/threads/1793795356-a-cited-name-stands-in-its-file/changelog.md:3`
evidence: executed `git grep -nwE "(def|class) <name>|<name> =" -- '*.py'` for each of the five names, `git grep -nwE "def load" -- '*.py'`, and `git ls-files --error-unmatch` on each cited file; read `seal/threads/1793795356-a-cited-name-stands-in-its-file/frame/design.md:89-95`
regression: round-1#1
```

The unit is the changelog fragment's entry, which `2b1db715b` changed. `frame/design.md` *Data & interfaces* gives each of the five a different reason, in its "Why it does not resolve" column: three names left a file that is still tracked, one file was deleted, and one planted key names a file that never existed. The fix rewrote "a name their file no longer binds" as "a name that no tracked file binds". The defect came from answering round 1's remark about the planted key: the new wording fixes the planted key and breaks two of the other four.

Why it matters: the fragment becomes the release note, which a person reads as the record of what changed. The plain reading of "a name that no tracked file binds" is that the name is bound nowhere in the tree. That is false for two of the five. `PANEL_VALUE_WIDTH` is bound at `.github/scripts/release_seal.py:129`, the file whose comment cited it, and at `skills/verify/scripts/seal_stamp.py:532`. `load` is bound at `skills/settle/scripts/settle.py:239`, one of 15 `def load` lines in the tracked `.py` files (executed: `git grep -nwE "def load" -- '*.py'`). The other reading, "a `path#name` that no tracked file binds", is the one the fix pass meant, but the sentence does not have one reading. The old sentence was false only for the planted key, which round 1 named as no defect.

The fix replaces the one sentence:

```markdown
Five places in the tree cited a name their cited file does not bind: three files had lost the name, one cited file had been deleted, and one planted key named a file that never existed.
```

The sentence after it, "Four sentences about a name the past held are rewritten without it, and one keeps the issue number its value's grounds hang on", stays true, and the snippet leaves it. No other statement of the five's reasons changed in the fix diff.

```seal
verdict: fixed f9a92629c
answer: The finding holds. `PANEL_VALUE_WIDTH` and `load` are bound in tracked files, so "a name that no tracked file binds" was false for two of the five. `git ls-files --error-unmatch` shows `broad_gate.py`, `test_unverified_rows_close.py` and `mode-gate.py` tracked, and `round_record.py` and `tests/test_tmp_seventh.py` not (executed). That matches the round's sentence and `frame/design.md` *Data & interfaces*. I replaced the sentence with the round's text. The sentence after it stays. In the same commit `gaps.md` closes its search-sample row, which round 1 *Confirmations* answered by listing every file that names the module.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: round 1's finding is fixed at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:184-205`. The fix pass claimed that `excuser` now reads the token whole in the `from` and the `to` with `NAME_TOKEN`, and that both new entries were red against the substring test. `holds` at line 193 builds the set of tokens `NAME_TOKEN` reads in the collapsed field and asks whether the cited token is one of them. `excuser` at line 205 calls it for the `from` and the `to` (read). The probe put the substring test back in place of `holds` and ran the module's own entries. "a change that renames the name to a longer one" went from excused to dangling, and "a from that holds a longer name" went from dangling to excused (executed). So each new entry fails against the code round 1 reviewed, which confirms the `seen red` claim by an independent run. The section shape keeps its substring test at line 192, since its asterisks bound it, so the section entries are unchanged: every section entry of the two tables passed in the module's run. A `to` of `None` reads as an empty field, as the old `(o.new or "")` did (executed: `holds(None, ...)` is false). The module passed whole, 53 cases, the tree case among them, with no warning (executed). That matches the fix pass's count. The fix pass's account of the six modules' run, 598 passed, was not re-run: the fix diff changes no other module.

What matched: the closed `gaps.md` row at `seal/threads/1793795356-a-cited-name-stands-in-its-file/gaps.md:9`. It opens with the word `closed`, the form `skills/verify/scripts/unverified_check.py:136` reads, and keeps the item's text. Its second cell cites round 1's look-behind confirmation, whose content it states truly (read: `trail/rounds/round-1.md`, the look-behind entry). `gaps.md` *Not done* now reads `nothing`, and the limit it recorded is gone at line 193 (read).

What matched: the changelog's new sentence, "The change has to hold the cited token whole in its `from` and not hold it in its `to`, so a rename from `#load` to `#load_all` corrects the citation", says what `holds` and `excuser` do (executed, the probe's rename entry). `frame/design.md:85`, the `excuser` bullet, stays true: `excuser` still takes the cited text as written, and its docstring at lines 197-202 names `holds` (read).

Remarks outside `## Findings`, none a defect the release would ship:

- `gaps.md:10`, the row on the sample search for the module docstring's other statements, stays open with "the proofer at review" as its answerer. Round 1 answered it under *Confirmations* with a command that lists every file naming the module. `23f27bbc8` closed the look-behind row that round 1 answered and left this one. The fix pass or the sealer may close it the same way.
- `trail/phases/phase-1.md:84-88` still describes the substring test. That record states the module at `6b04007c1`, which it names, so it stands, as round 1 said.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. `gaps.md:7` labels them for the orchestrator, and the label is honest: the fix pass names scoped runs and not the broad gate | `gaps.md:7` | the orchestrator, at the broad gate |
| The `path#name` tokens #1254's and #1255's branches write, which this case reads once they merge beside this one | `gaps.md:8` | the orchestrator, at the broad gate on the release branch after the merges |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_round2_probe.py -q -s -p no:xdist`, a probe that called `holds` on seven fields and then ran four versions of it (HEAD's, the substring test, an end-only bound and a start-only bound) over the module's four name entries in S9 and four more inputs: a `to` under `lib/`, a `from` under `lib/`, a `to` at a commit, and a `to` that drops the citation | 2 passed. HEAD's `holds` returned true for "See `manual/b.py#gone`." and false for `#gone_all`, for `lib/manual/b.py#gone`, for `abc1234:manual/b.py#gone` and for `None`, and got all eight inputs right. The substring test got five wrong, both new entries among them. The end-only bound got the four module entries right and the three extra inputs wrong. The start-only bound got the two new entries wrong. The probe file was deleted after the run |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist`, with line 193 replaced by `return re.search(re.escape(cited) + r"(?!\w)", flat) is not None` through the `Edit` tool | 53 passed. Line 193 was restored through the `Edit` tool, and `git diff --quiet` in the clone exited 0 after |
