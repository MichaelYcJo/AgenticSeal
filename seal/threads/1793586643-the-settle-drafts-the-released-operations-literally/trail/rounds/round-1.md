# Review round 1: 1793586643-the-settle-drafts-the-released-operations-literally

```seal
target: bee1ccacb against origin/release/v0.28.0
```

The target is the branch's diff against `origin/release/v0.28.0` at `30ba21373`, commits `d49bc246a` to `bee1ccacb`. This is round 1, so no earlier round hands over a coordinate or a verdict, and every fact below was opened this round. No `seal/parity.md` is declared, so no `original:` line is owed. Stage 1 read the code against `frame/design.md` (*Scope* items 1 to 6, *Data & interfaces*, *Where the script stops and the session's judgment starts*, D1 to D7) and `frame/plan.md` (A1 to A18, phase 1's *Verified by*). Stage 2 walked inputs, boundaries, ordering, error paths, line ends, file creation and deletion, and path safety.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: none
```
What matched: the restored applier is #953's function and adds only the table branch. Claimed in design G8 and *Scope* item 1: `apply_op` and `_cut` are restored from `91d570289^`. `git show 91d570289^:skills/settle/scripts/rule_changes.py` (executed) set beside `skills/settle/scripts/rule_changes.py:327-446` (read) shows `_cut` unchanged. `apply_op` is the same line for line, except for three things: the docstring, the `_last_row` call at `skills/settle/scripts/rule_changes.py:415-421`, and `_last_row` itself at `:346-367`. Each refusal in *Scope* item 1 stands at `:385-403` and `:436-442`, and each reason names the file and the section.

```seal
confirms: none
```
What matched: a table row is read through the oracle-held readers, as G9 asks. `_last_row` at `skills/settle/scripts/rule_changes.py:346-367` (read) takes a row through `config.py#table_cells` and a table's opener through `config.py#opens_table`, loaded lazily by `config()` at `:104-112`. `.github/scripts/rules.py` and `unverified_check.py` load this module, and the lazy load means neither of them now imports `config.py`. The phase's departure says a table opens only on a live line. That holds at `:356` and is grounded in GFM, which renders no table inside a fence. The probe (executed, `## Probes`) showed a table after an unpaired backtick in prose still opens, so the live-line reading does not miss an ordinary table.

```seal
confirms: none
```
What matched: `--draft` does what *Scope* item 3 and *Data & interfaces* state. `settle.py#draft` at `skills/settle/scripts/settle.py:1222-1258` (read) applies only `timeline`'s `specs`, built at `:799` from `parsed`. Designs read whole and designs with the no-change block never enter `parsed`, so they give no operation. It writes only an operation's `file`, which `rule_changes.py#parse` holds by `re.fullmatch` to a top-level `.md` of the policy root (`skills/settle/scripts/rule_changes.py:243-247`, read). It deletes a document a `remove` emptied and creates the policy root with `os.makedirs`. Its `not placed` line has the shape *Data & interfaces* gives. The refusals at `:1398-1403` come before anything is read. A settled root returns at `:1449-1456`, before `draft` is reached, and the `draft` id of `test_accepts_a_settled_root_and_says_so` pins that it writes nothing there.

```seal
confirms: none
```
What matched: S8, the record replays. Claimed in `trail/phases/phase-1.md` *S8*: 93 of 94 placed, and `docs/README.md` equal to the settled file. The built `settle.py --draft --released-at HEAD` ran over a `git clone --no-local` at `a92c358b8^` (executed, `## Probes`). It exited 0 and printed `placed 93 of 94 operations in docs/`. The one `not placed` line is `1793411151-judgment-where-meaning-is-the-question` at `frame/design.md:227`. `git status` named 14 changed documents and the new `docs/what-a-script-gates.md`, all under `docs/`. `git diff --quiet a92c358b8 -- docs/README.md` exited 0.

```seal
confirms: none
```
What matched: the phase's narrow modules pass at the target. `bin/test tests/skills/test_rule_changes.py tests/skills/test_settle.py -q` exited 0, with 237 passed. A second `bin/test` over `tests/hooks/test_launch.py`, `tests/text/test_settle_reads_before_it_removes.py`, `tests/behaviour/test_settle_applies_rule_changes_in_place.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` exited 0 (both executed, in the clone). These are probes of the slice, not a seal. The suite stays `unverified`, as `gaps.md` labels it, and the orchestrator's `seal gate` answers it. That label is honest: the phase record names its boundary run as 98 modules and does not call it the suite.

```seal
confirms: none
```
What matched: `gaps.md`'s Windows row has its answer. Claimed: the write without `newline=""` survived mutation on POSIX, and the Windows leg of `.github/workflows/test.yml` reads it. `gh run view 41381096626` (executed) shows head `bee1ccacb` on this branch, conclusion `success`, and all four `windows-latest` pytest groups `success`. No skip marker in `tests/skills/test_settle.py` covers `test_draft_creates_and_deletes_whole_documents` on `nt` (read: the only `os.name` branches are at `:352` and `:2554`, and both build fixtures). The case asserts the bytes of `docs/b.md`, so a translating write would have failed it there. The orchestrator reads that run as well and closes the row.

```seal
confirms: none
```
What matched: S9. The skill's text gives no reader the draft's output as a decided section, as `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* asks. Read at `skills/settle/SKILL.md`. The opening paragraph says the script writes "a starting text; it judges nothing". *What `--draft` writes* opens "no section it writes is settled" and closes "is decided no more than the dry run's groups are". Its second paragraph lists each question of meaning the session keeps, and the list matches the frame's *Where the script stops*. Step 4 makes the draft optional and has it committed alone. It reads every section the draft wrote against the code, writes each operation not placed by hand, and takes a superseded operation the draft wrote back out. Step 11 names each operation not placed in the body. The command's own last lines (`settle.py#DRAFTED`) say "This draft decides nothing" and send the session to step 4. The `README.md:265` and `README.ko.md:259` rows and `changelog.md` say the same.

```seal
confirms: none
```
What matched: the build stands with the earlier decisions the design names. #1035's three failures (D2) are each answered in the text. There is one writer, since the session runs the draft. Every written section is read against the code, at step 4. The draft is committed as its own diff. And the draft does not stop at an operation not placed: the `break` mutant the phase record names is pinned by C's second operation in `test_draft_writes_each_operation_in_merge_order_and_names_what_it_missed`. #1216's `copies` and `chain_check.py#pins_and_copies_in` are untouched: `git diff 30ba21373..bee1ccacb` (executed) changes no line of either. `--from` is refused beside `--draft` as #1054 refused it beside `--apply` (D7).

```seal
confirms: none
```
What matched: the contract rule 19 sweep is handed back as a sample, and a wider search found no sentence it missed that is now false. `trail/phases/phase-1.md` *Scope item 6* calls its four-wording list a sample. This round ran `git grep -i -E "settle[^.|]{0,120}(writ|judg)"` and `git grep -i -E "(script|settle\.py|seal settle)[^.]{0,80}(write|writ)"` over `docs`, `skills`, `agents`, `templates`, `hooks` and both READMEs (executed). That is also a sample, of two more wordings. The one sentence still saying the settle writes no policy document is `docs/the-record-layout.md` *The fold, and what tells it from a deletion*, and the design's `## Rule changes` carries that one.

```seal
confirms: none
```
What matched: the new tests each cover something their group does not. `Test_apply_op` is the first group for a new function. In `Test_main`, the five `--draft` cases split by behaviour: merge order with a miss, whole documents with CRLF bytes, the absent policy root, the two refusals, and local mode. None repeats `FROM_WITH_APPLY`'s case. `bin/seal layout --pairs` (executed) names no pair in either module.

## Edges weighed and not opened

The owner asked for edges not worth a finding to be recorded with their grounds. Each of these costs a reader less than the round trip a finding would cost.

- **A block directly under a table.** A table-row `add` whose section's last table runs straight into a paragraph, with no blank line, lands under that paragraph. GFM then renders the row as paragraph text (probe 1). `gaps.md` *Not done* states this. Probe 3 found no such table in `docs/`. The session reads every section the draft wrote, so the row is read before it ships.
- **"The last two lines".** `skills/settle/SKILL.md` *What `--draft` writes* says "The last two lines count the operations placed of all of them, and send the settling session to step 4". `settle.py#DRAFTED` is wrapped over three printed lines, so four lines follow the last `not placed` line. Nothing reads the output by line count, and the meaning (a count, then the pointer to step 4) is right.
- **"`copies` above".** `apply_op`'s docstring at `skills/settle/scripts/rule_changes.py:382` says "`copies` above". `copies` stands below it, at `:503`. The name is exact, and a search finds it. The module docstring at `:22-29` also names both appliers together.
- **`seal --help`'s settle line.** `skills/implement/scripts/seal.py:133-136` reads "show the released designs by section, and remove what a settle leaves". It names no flag (`--from` is also unnamed), so it is a summary that leaves `--draft` out, not a false sentence.
- **The reset command in a repository with no policy root at `HEAD`.** There, `git checkout HEAD -- <policy root>` fails on a pathspec that matches nothing. Only the case the crafter added `os.makedirs` for meets this. The session can see the error, and `git clean -f` alone returns that root.
- **No case pins that a design read whole gives the draft no operation.** `specs` is built from `parsed` (`settle.py:799`), the same dictionary the groups are built from. A design read whole could reach the draft only by also reaching the groups, which the dry run's cases already pin.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `bee1ccacb` (`gaps.md` *Not verified*, `frame/questions.md` Q1) | the whole tree | the orchestrator, at `seal gate` after the rounds settle |
| Whether the edge where the two appliers can differ (`plan.md` A3: a run spanning a placed `to`, or a `from` outside its section or twice in it) earns a follow-up issue | `skills/settle/scripts/rule_changes.py#copies`, `#apply_op` | the orchestrator, as `plan.md` A18 leaves it |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_rule_changes.py tests/skills/test_settle.py -q`, in a `git clone --no-local` at `bee1ccacb` under `<scratchpad>/1793586643-the-settle-drafts-the-released-operations-literally/round-1/clone` | exit 0, 237 passed |
| `bin/test tests/hooks/test_launch.py tests/text/test_settle_reads_before_it_removes.py tests/behaviour/test_settle_applies_rule_changes_in_place.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py -q`, same clone | exit 0 |
| `python3 <clone>/skills/settle/scripts/settle.py --root <s8> --released-at HEAD --draft`, where `<s8>` is a `git clone --no-local` checked out at `a92c358b8^` | exit 0; `placed 93 of 94 operations in docs/`; one `not placed` line, `1793411151-...` at `frame/design.md:227`; 14 documents changed and `docs/what-a-script-gates.md` new; `git diff --quiet a92c358b8 -- docs/README.md` exit 0 |
| `python3 test_tmp_draft_edges.py` in the clone, run once and deleted: `apply_op` over (1) a table whose last row a paragraph follows with no blank line, (2) a table after an unpaired backtick in prose, and (3) a walk of every live table in `docs/*.md` for a non-row line before the first blank | (1) the row lands after the paragraph; (2) the row lands as the table's last row; (3) 0 tables in `docs/` run into a non-row line |
| `bin/seal layout --pairs`, same clone | exit 0; no pair names `tests/skills/test_rule_changes.py` or `tests/skills/test_settle.py` |
| `gh run view 41381096626 --json headSha,conclusion,jobs` and `--log` | head `bee1ccacb`; conclusion `success`; the four `windows-latest` pytest groups `success` |
