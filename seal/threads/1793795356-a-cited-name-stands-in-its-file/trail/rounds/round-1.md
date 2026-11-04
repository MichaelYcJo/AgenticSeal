# Review round 1: 1793795356-a-cited-name-stands-in-its-file

```seal
target: 66c9c245e against release/v0.32.0
```

The target is `git diff 479a79d15...66c9c245e`. `release/v0.32.0` and `origin/main` both stand at `479a79d15` (executed: `git rev-parse`). It was read in a `git clone --no-local` of the branch worktree, checked out at `66c9c245e`, under the round's scratch directory. This is the first round, so no fact was carried from an earlier one, and every coordinate below was opened this round. `seal/parity.md` is not declared, so no `original:` line is owed. `seal/config.md` has no `Record language` row, so the record is in English. The request was read whole with `gh issue view 1256 --json title,body,comments`: the body and its one comment, which corrects the measure commits in place (executed). The owner's decision behind the frame's first proposal was read in #1355's body (executed: `gh issue view 1355`).

The axes walked were Inputs (the token shape and the look-behind), Query scope (the corpus, the top-level test, A3's reading of an untracked path), Exclusions and boundaries (records, a token at a commit, a path inside a longer path, a file that does not parse), Deliberate non-exclusions (method and nested-function names), Error paths (the not-read warning), and Security (a cited path holding `..`). Two more axes are this change's own. One is the excuse a pending rule change gives a name citation. The other is whether each rewritten sentence still gives its reader what it needs.

## Findings

### 1. A pending rename that lengthens a cited name is refused, and a `from` holding a longer token excuses a citation it does not correct

```seal
severity: should
location: `tests/behaviour/test_a_cited_section_stands_in_its_file.py:184-197`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:332`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:815-913`, `seal/threads/1793795356-a-cited-name-stands-in-its-file/gaps.md:12-18`
evidence: executed `bin/test tests/behaviour/test_tmp_round1_probe.py -q -s -p no:xdist` (the probe below, since deleted); read `tests/behaviour/test_a_cited_section_stands_in_its_file.py:184-197`, `skills/settle/scripts/rule_changes.py:569-586`
```

Why it matters: `frame/design.md` *Scope* item 1 says a dangling citation in a file of the policy root is excused where a pending rule change corrects it. `frame/plan.md` A9 gives the reason. A work item whose subject is the code may rename a function that `docs/` cites, and it must be able to pass its own suite until the settle. `excuser` decides "corrects" by substring tests at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:193-195`. The `from` must hold the cited text and the `to` must not. For a section the cited text is `*<section>*`, and its asterisks bound it. A `path#name` token has no closing delimiter, and no opening one either, so a substring test reads a different token as the same one in two ways.

- **A rename that lengthens the name is refused.** A `change` whose `from` is "See `manual/b.py#gone`." and whose `to` is "See `manual/b.py#gone_all`." corrects the citation. But `manual/b.py#gone` is a substring of `manual/b.py#gone_all`, so `cited not in` the `to` is false. The probe printed `Found(read=1, dangling=[('docs/a.md', 11, 'manual/b.py', 'manual/b.py#gone')], excused=[])` (executed). A rename such as `load` to `load_all`, or `read` to `read_text`, is the ordinary case A9 was built for. That work item's suite goes red, and its author is pushed to edit the policy root directly, which A9 rejects. The same holds where the `to` moves the path under a longer one, as `lib/x.py#y` to `hooks/lib/x.py#y`.
- **A `from` holding a longer token excuses a citation it does not correct.** A `change` whose `from` is "See `manual/b.py#gone_more`." and whose `to` is "See `manual/b.py#kept`." excuses the citation of `manual/b.py#gone` at line 11, and the warning says a pending rule change in `seal/threads/1-x/` corrects it. The probe printed `('docs/a.md', 11, 'manual/b.py', 'manual/b.py#gone', 'seal/threads/1-x/')` among `excused` (executed). The settle does not touch line 11, so the citation turns red after the settle, on a branch that did not make it.

The account names half of this. `gaps.md:14-18` *Not done* and `trail/phases/phase-1.md:84-88` describe only the second direction, and leave it because "no record shows the case". Neither names the first direction, which is the more likely of the two. The crafter's reason for leaving it, "bounding the token's end adds a rule for one shape only", also does not hold for the fix below. The fix reads the `from` and the `to` with the reader this module already has for the shape, `NAME_TOKEN`. That is a parser's answer, which `skills/core/SKILL.md` *The rule a mechanism is kept against* asks for over a substring.

The fix, with no OS-boundary precondition, replaces `excuser` at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:184-197`. `NAME_TOKEN` is defined lower in the module and is read when the function is called:

```python
def holds(field, cited):
    """FIELD, an item's `from` or `to` with its whitespace collapsed, holds
    the citation CITED whole: a `*section*` as written, which its asterisks
    bound, or a `path#name` token as `NAME_TOKEN` reads one, so neither
    `manual/b.py#gone_all` nor `lib/manual/b.py#gone` holds
    `manual/b.py#gone`."""
    flat = " ".join((field or "").split())
    if cited.startswith("*"):
        return cited in flat
    return cited in {m.group(0) for m in NAME_TOKEN.finditer(flat)}


def excuser(rel, line, cited, text, pending):
    """The work item directory of the PENDING item that corrects the citation
    CITED, as written, at LINE of REL, whose text is TEXT, or None. An item
    whose `from` holds the citation whole (`holds`) and whose `to` does not
    corrects it, and so does a `remove` with no `from` whose section holds
    the line (`rule_changes.removed_by`). `parse` reads an item's `file`
    only as a file of the policy root or of one of its groups."""
    for o, item in pending:
        if o.file == rel and o.old is not None:
            if holds(o.old, cited) and not holds(o.new, cited):
                return item
    return rules.removed_by(pending, rel, text, line)
```

Two entries, one in each S9 table, hold the two directions. Each should be seen red against `66c9c245e` before it is planted (contract rule 15). The probe saw both outcomes there, but it was not run as these cases.

```python
# In EXCUSING, after "a change whose from holds a name":
    "a change that renames the name to a longer one": (
        "docs/a.md",
        op("change", "Old section", NAME_OLD, "See `manual/b.py#gone_all`."),
        None,
        "name",
    ),
# In REFUSING, after "a to that keeps the name":
    "a from that holds a longer name": (
        "docs/a.md",
        op("change", "Old section", "See `manual/b.py#gone_more`.", NAME_NEW),
        "name",
    ),
```

The snippet does not reach every statement of the fact. The fix pass owes these too. `gaps.md:12-18` *Not done* goes, since the limit it records is gone. `trail/phases/phase-1.md:84-88` states the module at the commit that record names, so it stands, and the fix pass's own record says what changed. `frame/design.md:85`, the `excuser` bullet of *Data & interfaces*, stays true, since `excuser` still takes the cited text as written. The section reader's behaviour is unchanged, because `holds` keeps the substring test for a `*section*`.

```seal
verdict: fixed 2b1db715b
answer: The finding holds at its coordinate: `excuser` tested the token by substring against both the `from` and the `to`. I first added the two S9 entries, and both were red against the substring test (executed): the lengthening rename left `docs/a.md:11` dangling, and the longer `from` raised nothing. I read the paste-ready `holds` against `frame/design.md` *Data & interfaces* and *Scope* item 1. `excuser` still takes the cited text as written. The section shape keeps its substring test, which its asterisks bound. A token is read from the `from` and the `to` by `NAME_TOKEN`, the module's own reader of the shape. So I applied it as given. With `holds` cut back to a substring, `bin/seal mutate` turned both entries red (executed). The citation module passed 53 cases, and the plan row's six modules passed 598 (executed, at `2b1db715b`). `gaps.md` *Not done* now reads `nothing`. The changelog fragment says what a correcting change has to hold, and calls the five places names that no tracked file binds. `23f27bbc8` closes the `gaps.md` look-behind row that this round's *Confirmations* answered. `trail/phases/phase-1.md` states the module at `6b04007c1`, so it stands.
```

## Confirmations

What matched: A3, the breadth the orchestrator asked about (`frame/plan.md:19`). The issue says "a `path#name` whose path is a tracked `.py` file". The reader at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:308-344` also makes a citation dangling where its path, under a tracked top-level entry, names no tracked file. This round reads A3 as within the issue rather than past it. The issue's *Done when* asks that "the tree's `path#name` citations resolve", and a citation of a file that is not there does not resolve. The issue's phrase names the shape the case reads. It does not exempt a cited file that left. Taken literally, it would also let a renamed file pass with every citation of it unread, which is the failure A3's row names. The breadth earned its keep on the first run. One of the four real instances, `tests/skills/test_settle.py:3236`, cited `skills/code-review/scripts/round_record.py#load`, a file `8350c5788` deleted. Under the issue's literal reading that citation would have stayed unread. The cost is that a fixture writer cannot write a top-level path to a file that does not exist as a literal. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:491-492` paid that cost once at HEAD. The design states it, and the refusal names the citing line. This is read for compliance, not for whether the trade is right, which `frame/plan.md` A3 and the orchestrator's confirmation decided.

What matched: the tree case. With HEAD's reader run over a clone at `479a79d15`, `names` read 280 citations and named exactly the five citing lines `frame/design.md` *Data & interfaces* lists. At `66c9c245e` it read 275 citations, with nothing dangling and nothing excused (executed, the second probe below). This confirms the phase record's "red at the phase's start" claim at `trail/phases/phase-1.md:25-34` by an independent run. The module passed whole: 51 cases (executed: `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -rw -p no:xdist`, exit 0, no warning). So did `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` with `tests/text/test_a_cited_commit_outlives_the_squash.py` (21 passed), and the cases of the other three edited modules that the rewritten docstrings sit on (34 passed, selected with `-k`; executed).

What matched: the four rewritten sentences, read for whether their reader still gets what they need. No sentence cites a commit, and none keeps a path to a gone name (read: the diff). `tests/hooks/test_config.py:1110-1113` loses only the history after the dash, and the reader still learns why the reader tells the two cases apart. `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:635-637` still says what `config_base` reproduces, which is what a caller needs. `tests/skills/test_settle.py:3236-3238` now says what the case holds, and `settle.load` stands at `skills/settle/scripts/settle.py:239`. The case at `tests/skills/test_settle.py:3240-3252` asserts exit 2, the path and the purpose on stderr, so the docstring's new claim is the case's own (read). `.github/scripts/release_seal.py:126-128` keeps the grounds of 23 with #832 and no path, as `frame/design.md` *Scope* item 4 asks. Its facts hold. The gate's value is 41 at `skills/verify/scripts/seal_stamp.py:532`, and `tests/github/test_release_seal.py:428-429` holds 23 below it (read). This comment was the one sentence whose old text named where the other number lived, though by then the name was stale. The rewrite names neither the gate's constant nor the case. A person changing 23 now has to search for both. `skills/verify/scripts/seal_stamp.py#PANEL_VALUE_WIDTH` would be a present citation that the new case holds. This round names that as a gap in the reader's path, not a defect, since the build does what the frame's item 4 asked.

What matched: the look-behind members the crafter left unpinned (`gaps.md:9`, `trail/phases/phase-1.md:55-64`). The crafter's account holds. This round compared `NAME_TOKEN` with the look-behind cut to `(?<![/:])` on six strings (executed, the first probe). The two differ only on back-to-back tokens, `x.py#a.tests/y.py#b` and `x.py#a-tests/y.py#b`, and on an empty segment, `a//btests/x.py#n`. A URL and an ordinary backticked token read the same either way, because the `/` member and the top-level test already hold them. A case that pinned `\w`, `.` and `-` would pin text no writer produces. No case is owed: `frame/design.md` *Scope* item 3 names only the `:` and `/` guards and the top-level test as guards to show red. The three members cost a few characters, and the module docstring and the comment at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:244-246` state them truly.

What matched: each case of *Scope* item 3, read against the break the phase record names at `trail/phases/phase-1.md:41-53`. Each break, applied alone, makes its case's named assertion fail for the reason given. The `if True` break leaves N2's dangling list empty. The `ast.walk` break binds N3's `local`. Without the tracked-file test, N4's untracked `manual/loose.py` is read and resolves. Each N5 guard alone admits one of the three unread tokens. Either N6 branch returning `set()` turns the not-read file into one that is read. The `RECORDS` filter, the `excuser` call and the `to` test each hold their S9 or S8 entry. This was read, not re-run. N5 builds its commit token from the fixture's own commit, whose `manual/b.py` lacks `gone`. A reader that opened the commit would therefore count the token and fail N5, so the acceptance row "nothing opens the commit" is held, not only claimed. Each new N case covers a branch of `names` or `bound` that no S case reaches, so none duplicates its group. The module declares no `TARGET` (executed: `grep -n "^TARGET"`).

What matched: the module docstring's other statements, the sample `gaps.md:10` names. This round listed every file of the tree that names the module, which is a command that lists each holder of that property (executed: `git grep -n test_a_cited_section_stands_in_its_file -- ':!seal/threads'`). Three describe it. `skills/settle/scripts/rule_changes.py:17-20` says `removed_by` serves two readers, the rules script and this module, which is still true. `tests/text/test_a_cited_commit_outlives_the_squash.py:12` and `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:89` name `#corpus`, which still stands and still reads the same files. `skills/writing-style/SKILL.md:267` names the module on a `check:` line. A sentence that describes the module's reach without its path is outside this list, as the crafter said.

Remarks outside `## Findings`, none a defect the release would ship:

- `bound` at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:275-305` binds what *Scope* item 1 lists. A module-level `for` target, a `with ... as` name and an `except ... as` name are not in that list, and a citation of one would be refused. The kinds of binding are an open set. No tree citation meets one (the tree case is green), and contract rule 18 has a refusal reported when one does.
- A GitHub line anchor such as `hooks/x.py#L10` reads as a name and would be refused as a name the file lacks. The tree holds none in the corpus. The message would point to the line, though "names what its file lacks" describes a line anchor loosely.
- `changelog.md:3` says "Five places in the tree cited a name their file no longer binds". One of the five, the planted `tests/test_tmp_seventh.py#sweep`, names a file that never existed. The next sentences of the entry say so.
- `trail/phases/phase-1.md:110-114` says the five rewrites went through a shell script, not the `Edit` tool, against contract rule 9, with each substitution asserted. The diff matches what the frame asked at each place (read), so the deviation left no defect in the tree.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. `gaps.md:7` labels them for the orchestrator, and the label is honest: the phase record names a scoped run and not the broad gate | `gaps.md:7` | the orchestrator, at the broad gate |
| The `path#name` tokens #1254's and #1255's branches write, which this case reads once they merge beside this one | `gaps.md:8`, `frame/plan.md:47` | the orchestrator, at the broad gate on the release branch after the merges |
| The two `add` items of `## Rule changes` land where `frame/design.md:26` says the framer saw them land, applied with `apply_op` from a scratch clone. This round did not re-apply them | `frame/design.md:26`, `frame/design.md:98-107` | the settle, by `seal rules --check` after it |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_round1_probe.py -q -s -p no:xdist`, a probe holding three cases: a pending `change` from `manual/b.py#gone` to `manual/b.py#gone_all`, a pending `change` whose `from` holds `manual/b.py#gone_more`, and `NAME_TOKEN` against the look-behind cut to `(?<![/:])` on six strings | 3 passed. The rename left `manual/b.py#gone` dangling at line 11 with nothing excused. The longer `from` excused line 11. The cut look-behind differed only on `x.py#a.tests/y.py#b`, `x.py#a-tests/y.py#b` and `a//btests/x.py#n`, and on the URL it read the token from the host's second letter on, whose first segment is no top-level entry. The file was deleted after the run |
| `bin/test tests/behaviour/test_tmp_round1_base.py -q -s -p no:xdist`, a probe that ran HEAD's `names` over a `git clone --no-local` of the review clone checked out at `479a79d15`, and over the clone at `66c9c245e` | 1 passed. At the base: read 280, five dangling, at `.github/scripts/release_seal.py:126`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:491`, `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:637`, `tests/hooks/test_config.py:1113` and `tests/skills/test_settle.py:3236`. At HEAD: read 275, none dangling, none excused. The probe file and the base clone were deleted after the run |
