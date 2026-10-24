# 1792449518-settle-squashes-specs-into-docs-in-place — review round 1

target: a8bd7772 against release/v0.22.3

No earlier round exists for this work item, so no fact is carried and every
verdict below was reached at a8bd7772. The frame read is `spec.md`,
`plan.md` and `questions.md` as they stand at a8bd7772. The owner's two
answers that bind this round are Q1 (no symbol or constant a reader can trip
on, and a grammar or value stated once) and Q6 (a document past `Document
token ceiling` is reported, and the run exits 0). `overview.md` and
`phases/` were read as the smith's account and checked against the code.
Findings 1 to 4 are the four cases the orchestrator relayed from the
`tests` workflow run 39346594309. This round opened each coordinate and
re-ran the four cases narrowly in its clone, where all four fail.

## Findings

### 1. The sealer's refusal of an old verdict word now prints the settle sentence

severity: must
location: `skills/code-review/scripts/chain_check.py:91`, `skills/code-review/scripts/chain_check.py:1687`, `skills/code-review/scripts/chain_check.py:1770-1773`, `skills/code-review/scripts/chain_check.py:1861`
evidence: executed `bin/test tests/test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists tests/test_the_sealer_guarantees.py::test_the_old_words_are_refused_by_line tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py tests/test_a_script_says_which_interpreter_it_needs.py::test_what_runs_before_any_floor_needs_nothing_its_python3_lacks -q -p no:randomly`
verdict: fixed a69a1c6e

The build added a second module-level `RETIRED_SAYS` at line 1770. Line 91
already defines `RETIRED_SAYS` as the sentence a `guarantee.md` gets when it
still reads `sound`, `not sound` or `undecidable`. The new binding replaces
the old one when the module loads. So line 1687 now tells a person whose
guarantee reads `sound` that it was "retired: a settle — nothing open at the
merge base". That sentence comes from code the build wrote, not from a
fixture. The failing line in the case is `guarantee.md:18 the sealer's
verdict reads `sound`: `sound` retired: a settle — …`. The case fails on
ubuntu, macOS and Windows, and it failed here too. An AST scan for
top-level names bound twice in every `.py` file this diff touches found this
pair and no other. The fix gives the settle sentence its own name.

```python
# skills/code-review/scripts/chain_check.py, line 1770
SETTLE_SAYS = (
    "retired: a settle — nothing open at the merge base, and the policy root "
    "holds every rule change its spec states"
)

# line 1861, in main
                notices.append((rel, 0, SETTLE_SAYS))
```

answer: The settle sentence is now `SETTLE_SAYS`, and line 91's `RETIRED_SAYS` is bound once again. `tests/test_the_sealer_guarantees.py::test_the_old_words_are_refused_by_line` passes.

### 2. Two new pins cite an `implement` heading by half its title

severity: must
location: `tests/test_settle_reads_before_it_removes.py:814`, `tests/test_waiver_decided_at_start.py:713`
evidence: executed `bin/test tests/test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists tests/test_the_sealer_guarantees.py::test_the_old_words_are_refused_by_line tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py tests/test_a_script_says_which_interpreter_it_needs.py::test_what_runs_before_any_floor_needs_nothing_its_python3_lacks -q -p no:randomly`
verdict: fixed 4e28cb9c

`tests/test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists`
reads every `§*...` citation of `skills/implement/SKILL.md`, test sources
included. Both new pins assert the prefix `§*Document layout`, and the
heading at `skills/implement/SKILL.md:68` is `Document layout — two roots,
three lifetimes`. The citation check reads the prefix as a heading that
does not exist, and it refuses it. The prefix was likely chosen because the
carriers wrap the heading across lines. Collapsing whitespace before the
assertion lets each pin name the whole heading.

```python
# tests/test_settle_reads_before_it_removes.py, line 814
    flat = " ".join(text.split())
    assert (
        "`skills/implement/SKILL.md` §*Document layout — two roots, three lifetimes*"
        in flat
    ), "/".join(parts)

# tests/test_waiver_decided_at_start.py, lines 712-714
    assert (
        "the policy in force as `skills/implement/SKILL.md` §*Document layout — "
        "two roots, three lifetimes*" in " ".join(framer.split())
    )
```

answer: Both pins name the whole heading in one string literal. The citation scan reads the source, so a literal split across two lines failed it a second time; one literal on one line passes. The helpers already collapse whitespace.

### 3. A new fixture helper runs git in the locale's encoding

severity: must
location: `tests/test_settle_applies_rule_changes_in_place.py:375`
evidence: executed `bin/test tests/test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists tests/test_the_sealer_guarantees.py::test_the_old_words_are_refused_by_line tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py tests/test_a_script_says_which_interpreter_it_needs.py::test_what_runs_before_any_floor_needs_nothing_its_python3_lacks -q -p no:randomly`
verdict: fixed a3f37ed8

The helper `git` calls `subprocess.run(..., text=True)` without
`encoding="utf-8"`. Python then decodes git's output as cp1252 on the
Windows leg. `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`
refuses it at that line. A search of the diff's added lines for
`text=True` found this call and no other.

```python
def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
    ).stdout
```

answer: The helper passes `encoding="utf-8"` in place of `text=True`, and the encoding case passes.

### 4. `rule_changes.py` now runs before any interpreter floor and is not linted at 3.9

severity: must
location: `ruff.toml:43-48`, `skills/verify/scripts/unverified_check.py:1247-1258`
evidence: executed `bin/test tests/test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists tests/test_the_sealer_guarantees.py::test_the_old_words_are_refused_by_line tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py tests/test_a_script_says_which_interpreter_it_needs.py::test_what_runs_before_any_floor_needs_nothing_its_python3_lacks -q -p no:randomly`
verdict: fixed 641ae5bb

`unverified_check.py#rule_changes` loads `skills/settle/scripts/rule_changes.py`
by path. `unverified_check.py` is linted at `py39` because it runs on
whatever `python3` starts it, before the launcher checks any floor. So
`rule_changes.py` now runs there too, and the case refuses a file of that
set with no `per-file-target-version` entry. Reading `rule_changes.py`
found no construct newer than 3.9 (no `match`, no `zip(strict=)`, no
`datetime.UTC`). The entry is the whole fix.

```toml
"skills/verify/scripts/unverified_check.py" = "py39"
"skills/settle/scripts/rule_changes.py" = "py39"
```

answer: `ruff.toml` lists `skills/settle/scripts/rule_changes.py` at `py39`, and the interpreter case passes. `fold_check.py` is not in that set: `settle.py` loads it, and `settle.py` runs only after the launcher has checked the floor.

### 5. A `file:` field is matched as a string, never as a path, so a Windows separator or a second case of one name escapes it

severity: should
location: `skills/settle/scripts/rule_changes.py:157-161`, `skills/settle/scripts/settle.py:79-81`, `skills/settle/scripts/settle.py:272-302`, `skills/settle/scripts/settle.py:574-579`
evidence: executed `python3 tests/test_tmp_round1_probe.py`
verdict: fixed 5ccef9cc

`parse` accepts any `file` matching `docs/[^/]+\.md`. A backslash and a
drive colon both pass. `settle.py#under` then joins the value with
`os.path.join`, which is `ntpath.join` on Windows. The probe parsed four
such values, and each came back as an operation with no refusal:

- `docs/..\..\evil.md` joins to the drive root.
- `docs/C:\x\evil.md` joins to `C:\x\evil.md`, because a drive in a later
  part resets the join.
- `docs/\evil.md` joins to the drive root.
- `docs/sub\b.md` lands below the top level, and `apply` creates `sub`.

An `add` with no `section` then writes outside the repository on the
owner's machine at `settle --apply`. The CI predicate later refuses the
removal, but by then the write has already happened. `hooks/config.py#policy_root`
does normalise `\` and refuse `..` for the config row. The field that names
the file inside that root gets neither check.

The same cause has a second instance. Two specs naming `docs/a.md` and
`docs/A.md` are two places to `replay`, which the probe confirmed: both
applied, under two keys. On a case-insensitive disk (APFS and NTFS by
default) both keys are one file. `apply` writes them in turn, so the second
write erases the first spec's change. That spec's directory is still
removed, and the run exits 0.

```python
# skills/settle/scripts/rule_changes.py, parse: no separator or drive in a name
        if not re.fullmatch(re.escape(policy_root) + r"/[^/\\:]+\.md", file):
            errors.append(
                (item["line"], f"`{file}` is not a top-level {policy_root}/ file")
            )

# skills/settle/scripts/settle.py, rule_plan, after `held = {... if p.errors}`.
# Precondition: os.listdir returns each name as stored, which APFS and NTFS do.
    top = under(root, policy)
    listed = os.listdir(top) if os.path.isdir(top) else []
    for work_item_id, found in parsed.items():
        for op in found.ops or []:
            name = op.file.split("/", 1)[1]
            if name not in listed and any(
                n.casefold() == name.casefold() for n in listed
            ):
                held.setdefault(work_item_id, []).append(
                    (op.line, f"{op.file} names an existing document in another case")
                )
```

A case in `tests/test_settle_applies_rule_changes_in_place.py` for each
spelling, run through `parse` and through `rule_plan`, pins it.

answer: `parse` refuses a `file` holding `\` or `:`. `rule_plan` holds a spec whose `file` differs only in case from another name, whether that name is a document on disk or another spec's `file`. Four rows of `test_a_block_that_does_not_match_whole_is_refused_at_its_line` and `test_a_name_that_differs_only_in_case_is_held` pin both. The skill's `file` bullet states the rule.

### 6. A spec at a nested heading neither waits on nor conflicts with one at its parent

severity: should
location: `skills/settle/scripts/rule_changes.py:268-269`, `skills/settle/scripts/rule_changes.py:282-301`, `skills/settle/scripts/rule_changes.py:347-359`, `skills/settle/SKILL.md:107-114`
evidence: executed `python3 tests/test_tmp_round1_probe.py`
verdict: fixed 56220680

`place(op)` is the literal pair `(file, section)`. A `change` reads its
`from` across the whole section, sub-sections included (line 227). So a
section `X` and its sub-section `Y` overlap but count as two places. The
probe built this case. Spec A, earlier and held by an open row, changes
`old sentence.` under `X`. Spec B, later, changes the same sentence under
`Y`. B applied, and A stayed refused. In merge order A applies first and B
is refused. So the later spec landed under the earlier one, which
`skills/settle/SKILL.md` lines 107-114 say cannot happen ("A later spec at
one of its places waits with it"). When A is released later it is refused,
because its `from` is gone. `conflicts` has the same gap for parallel specs.
Both failures are loud at a later run, and neither is guessed. But the
order the skill promises does not hold.

The narrowest fix that holds the promise makes the document the place. It
costs waits and conflicts between specs in one file that never overlap, and
each of those is printed. A per-heading-range reading avoids that cost but
needs the document's heading ranges inside `replay`.

```python
def place(op):
    """A document is one place: a section's range holds its sub-sections,
    so two headings of one file can name one text."""
    return (op.file, None)
```

The skill sentence then reads: "A later spec naming a document a refused
one names waits with it."

answer: Fixed by the heading-range reading, not by making the document one place. With the document as the place, two release branches that each add a rule to different sections of one document become a conflict, and every later spec in that document waits on any refusal. `rule_changes.overlapping` reads each section's lineage from the document as it stood before the replay. Two places overlap when they are in one file and one section holds the other, or when either is the whole document. `replay` waits and `conflicts` refuses on that overlap. `test_a_spec_at_a_section_holding_or_held_by_a_refused_ones_waits` and the `S child` row of the parallel-branch conflict case were both red before the fix. The skill sentence now says a section and a sub-section it holds are one place.

### 7. The `nothing — <why>` sentinel is spelled a second time, and a near miss is refused with a sentence that does not name it

severity: should
location: `skills/settle/scripts/rule_changes.py:27`, `skills/settle/scripts/rule_changes.py:101-110`, `skills/settle/scripts/fold_check.py:96`, `skills/verify/scripts/unverified_check.py:94`
evidence: executed `python3 tests/test_tmp_round1_probe.py`, `git grep -nE "\"nothing —|'nothing —|nothing — \"|NOTHING" -- '*.py'`
verdict: fixed 5ccef9cc

`rule_changes.py:27` defines `NOTHING = "nothing — "` beside
`fold_check.py:96`'s identical constant. Under the owner's Q1 answer a
value stated twice is the defect: the next edit to one leaves the other
behind. The sentinel also carries an em dash (U+2014). A person writing on
a keyboard types a hyphen, and Q1 names a symbol a reader trips on as a
defect. The probe parsed `nothing - x`, `nothing -- x`, `nothing: x` and
`Nothing — x`. Each was refused as "a line outside an item", which tells
the author nothing about the dash. The sentinel predates this item
(`Enforced by: nothing — <why>`). Keeping it is consistent with the rest of
the tree, so the fix keeps it, names it once, and names it in the refusal.
Both modules already load `unverified_check.py`, which is the one place
both can read it from.

```python
# skills/verify/scripts/unverified_check.py, beside FOLD_MARKER
# A section or a line that states nothing, with its reason after the dash
# (U+2014). `fold_check.py` and `rule_changes.py` read it here.
NOTHING = "nothing — "

# skills/settle/scripts/rule_changes.py, parse, before `if first.startswith(...)`
    nothing = r.NOTHING.strip()
    if first.lower().startswith("nothing") and not first.startswith(nothing):
        return Parsed(
            [], None,
            [(first_no, "a spec that changes no rule writes `nothing — <why>`, "
              "with an em dash (U+2014)")],
        )  # fmt: skip
```

`fold_check.py` reads `reader().NOTHING`, and its own constant goes. A row
of `test_a_block_that_does_not_match_whole_is_refused_at_its_line` pins
the new sentence.

answer: `NOTHING` is defined once, in `unverified_check.py`. `rule_changes.py` and `fold_check.py` read it from there, and both of their own copies are gone. A first line that opens with `nothing` in any case, but not with the sentinel, is refused with "writes `nothing — <why>`, with an em dash (U+2014)". The `nothing-with-a-hyphen` and `nothing-capitalised` rows pin it. The two `.github/scripts/rules.py` mentions are prose that names the shape, and no other constant spells it.

### 8. `--apply` reports `0 refused or kept` while it keeps every spec with no `## Rule changes`

severity: should
location: `skills/settle/scripts/settle.py:590-596`, `skills/settle/SKILL.md:117-124`
evidence: read `skills/settle/scripts/settle.py:590-596`, `skills/settle/SKILL.md:117-124`, `tests/test_settle_reads_before_it_removes.py:988-997`
verdict: fixed 6789ec70

The overview says a spec with no section is "kept, exit 0" on purpose. The
grounds are in the account and in the pin at
`tests/test_settle_reads_before_it_removes.py:988`, which no policy
document states. The code does what the account says. But the skill says
"It exits 0 when nothing was refused or kept, 1 when something was" (line
123), six lines after it says such a spec "is named and stays". The summary
line counts only `refused`, `kept` and `base_kept`. Until #941 settles the
backlog, every run in this repository prints `0 refused or kept` while it
leaves 100 or more directories behind. The line is the one a person reads
to decide whether the settle is finished.

```python
    held = len(plan["refused"]) + len(kept) + len(base_kept)
    left = len(plan["premodel"])
    out.write(
        f"\napplied {applied} spec{plural(applied)} and removed {removed} "
        f"director{plural(removed, 'ies', 'y')}; {held} refused or kept"
        + (f"; {left} with no `## Rule changes`, left in place" if left else "")
        + "\n"
    )
```

```markdown
It exits 0 when nothing was refused or held by an open row, a spec with no
`## Rule changes` included, 1 when something was, and 2 when the arguments
or the tree are unusable.
```

The existing pin's substring `0 refused or kept` still holds. A new
assertion on the `left in place` clause pins the count.

answer: The last line now adds `; <n> with no `## Rule changes`, left in place`. The skill's exit sentence and `settle.py`'s exit-code docstring both say such a spec is counted and is not refused. `test_an_apply_with_nothing_to_do_is_no_refusal` pins the count of 3.

### 9. Both READMEs still describe `fold-check` as a line ceiling with frozen markers

severity: should
location: `README.md:264`, `README.ko.md:254`
evidence: executed `git grep -nE "줄 수 상한|표시 개수|two rules|두 규칙" -- ':!seal/specs' ':!changelog' ':!CHANGELOG.md'`
verdict: fixed 072f60bd

The cheat-sheet row says "no document grows past the ceiling unless it is
listed with its fold markers frozen" and calls the listing a
`seal/config.md` row. The Korean edition says "문서는 줄 수 상한을 넘지
않아야 하고, 넘은 문서는 fold 표시 개수를 고정한 채 목록에 올라 있어야
합니다". This item removed `Over the ceiling` and the freeze. It made the
ceiling a token estimate that fails nothing, and it added the index arm.
The `settle` row beside it was rewritten, and this one was not. A person
choosing whether to run the command reads a check that no longer exists.

```markdown
| `fold-check [--shape-from <id>] [--ceiling <n>]` | holds the top level of the policy root (`docs/` unless `Policy root` names another) to three checks. Every bound statement from the cutoff on opens with a bold rule sentence and carries one `Enforced by:` line whose targets exist. Each document past the token ceiling is named as one to split, which fails nothing. Where `<policy root>/README.md` exists, it names every other document on exactly one row. The cutoff and the ceiling are `seal/config.md` rows the repository writes; a row it leaves out is a check that does not run, and the output says so. A flag replaces its row for one run, so `--shape-from 0` lists every statement still missing the shape |
```

```markdown
| `fold-check [--shape-from <id>] [--ceiling <n>]` | 정책 루트(`Policy root` 가 따로 정하지 않으면 `docs/`) 최상위를 세 가지로 확인합니다. 기준 id 이후의 문장은 굵은 규칙 문장으로 시작하고, 가리키는 대상이 실제로 있는 `Enforced by:` 줄을 하나 가져야 합니다. 토큰 상한을 넘은 문서는 나눌 문서로 이름만 찍고 실패시키지 않습니다. `<policy root>/README.md` 가 있으면 다른 문서마다 정확히 한 행이 그 문서를 가리켜야 합니다. 기준 id 와 상한은 레포가 `seal/config.md` 에 적는 행이며, 적지 않은 행의 검사는 돌지 않고 출력이 그렇다고 알려 줍니다. 플래그는 그 실행에서만 행을 대신하므로, `--shape-from 0` 이면 아직 형식을 갖추지 못한 문장을 전부 찍습니다 |
```

answer: Per the owner's direction, both rows point to the checks' one statement (`fold_check.py` and `templates/config.md` §*The fold's values*) instead of restating the three checks. `test_both_cheat_sheets_point_to_the_checks_home` was red against the old rows.

### 10. The release checklist orders a split in the same pull request, against Q6 and the skill

severity: should
location: `docs/release-checklist.md:115-117`, `templates/config.md:452-455`, `docs/the-record-layout.md:25-29`
evidence: read `docs/release-checklist.md:115-117`, `skills/settle/SKILL.md:176-182`, `templates/config.md:452-455`
verdict: fixed e9879bbd

The checklist says "a document past its ceiling is split along its
headings in the same pull request". `skills/settle/SKILL.md` §*A document
past its ceiling is split, never trimmed* says "in that pull request or a
later one". Q6 makes the ceiling a report, and the spec leaves this
repository's two documents past it to #941. A session following the
checklist at the next settle would be told to split
`docs/worktree-guard-spec.md` and `docs/one-root-by-lifetime.ko.md` there
and then. The report rule is stated in four places: the skill,
`templates/config.md`, `docs/the-record-layout.md` and the checklist. The
copy that drifted shows why Q1 asks for one statement. The skill section is
the procedure, so the other prose points there.

```markdown
documents the second wrote, and names each one past its ceiling as one to
split (`skills/settle/SKILL.md` §*A document past its ceiling is split, never
trimmed*).
```

In `templates/config.md`, the sentence from "A document past the ceiling
is reported" to "read in more calls." becomes the same pointer.

answer: The checklist, `templates/config.md` and the third copy, `docs/the-record-layout.md` §*The size a reader takes whole*, each point to the skill's section, so the skill is the one statement of what a document past the ceiling owes. `test_the_release_checklist_carries_the_by_hand_step` was red against the old checklist sentence.

## Confirmations

confirms: none
Q6 holds in `fold-check`. `skills/settle/scripts/fold_check.py:573-587`
adds the past-ceiling lines to the output and never to `problems`, so a
document past the ceiling exits 0. `settle.py#write_after` prints the same
lines after the writes and changes no exit code. Read.

confirms: none
The settled predicate loosens a gate only as far as Q2's default (a).
`skills/verify/scripts/unverified_check.py:1266-1321` accepts four kinds of
directory without a replay: one that never wrote a `spec.md`, which
`retired_by_rule` also accepted; one whose `spec.md` has no
`## Rule changes`, which is Q2's case; one that says `nothing — <why>`; and
in every case only with nothing open at the merge base. A section that does
not parse, an operation the base cannot place and a count HEAD does not
match all keep the removal refused. The open-row check is new for spec'd
directories, so the gate is tighter there than the marker was. Read.

confirms: none
`settle --apply` writes every document before it removes any directory
(`skills/settle/scripts/settle.py:574-585`), and a spec is applied whole or
not at all in memory (`rule_changes.py:290-304`). A spec whose adding
commit is unknown is held before `conflicts` runs (`settle.py:292-303`), so
no `None` commit reaches `git merge-base`. A run cut short between two
writes keeps every directory, and a rerun applies an `add` a second time.
The settled predicate then counts the text twice against the replay's once
and refuses the removal in CI, so the duplicate cannot merge. Read.

confirms: none
Claimed by the smith: the suite is `unverified` and the broad gate is the
orchestrator's. Found: `overview.md` `## Not verified` names the full
suite, the lint and the typecheck with the orchestrator as answerer. The
label is honest, and the four red cases above are the reason it is not a
pass. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Q2 is still `open`, and the settled predicate and `tests/test_unverified_rows_close.py:1619` ("Q2's answer (a)") rest on its default. `CONTRIBUTING.md` §*What a change to a gate must carry* makes a gate's failure direction the owner's call | `seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/questions.md` Q2 | the owner, through the orchestrator |
| Q3 is still `open`: nothing gates a pull request that edits the policy root | `seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/questions.md` Q3 | the owner, through the orchestrator |
| `spec.md`'s `## Removes` row for the marker freeze still reads "a document over a ceiling is refused" and "this repository declares `none`", which Q6 and the 25000 row overturned. The frame is the framer's to write, not the fix pass's | `seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/spec.md:204` | the orchestrator, for the framer |
| Finding 5's Windows joins were shown with `ntpath` on macOS, not on a Windows host | `skills/settle/scripts/settle.py:79-81` | the orchestrator, from the Windows leg of the `tests` workflow once a case is planted |
| Q4: whether bytes halved overestimates dense Hangul | `skills/settle/scripts/fold_check.py:316-318` | a measurement, as the frame says |
| The full suite, the repository-wide lint and the typecheck. The smith's report of ruff exit 0 over the changed files was not re-run here | the whole branch | the orchestrator, at `broad-gate` |

When the fix pass closes these ten findings and a verifying round leaves
nothing open, what comes due is the orchestrator's broad run and then the
sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `python3 tests/test_tmp_round1_probe.py` | exit 0, deleted afterwards. The four near misses of `nothing — ` were each refused as "a line outside an item". The four Windows-shaped `file:` values each parsed with no refusal, and `ntpath` joined three of them outside the repository. With the earlier spec held, the nested-heading spec applied; with both free, the earlier one applied and the later one was refused. `docs/a.md` and `docs/A.md` both applied, under two keys |
| `bin/test` over the four relayed cases, `-q -p no:randomly` | exit 1: 4 failed, 150 passed in 3.11s. Each failure line matches the relayed one |
| AST scan of each `.py` file the diff touches for a top-level name bound twice | one hit, `RETIRED_SAYS` in `skills/code-review/scripts/chain_check.py` at lines 91 and 1770 |
| `git grep` over the tree outside `seal/specs/` and `changelog/` for `retire-process`, `settle --retire`, `folded_items`, `retired_by_rule`, `Over the ceiling`, `Document line ceiling`, `frozen at` and `one writer that does` | no live carrier outside the tests that assert the words absent and `.test_durations`, except the `fold-check` rows of finding 9 |
