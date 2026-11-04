# Implementation Plan: the census reads every entry point (#1255)

## Technical context

`tests/censuses.py#entry_point` reads a file
only where `_python(rel, root, ("hooks/",))` returns its text. It flags each
module-level block `is_main_guard` matches whose first statement
`opens_with_to_utf8` does not accept, and hands the flags to `_held`, which
applies the exemptions and refuses an exemption that excuses nothing
(`tests/censuses.py#_held`). `tests/test_censuses.py` sweeps every tracked
file no module file declares as its `TARGET`, and each module file runs
every census over its own target through `census_case`, so both the sweep
and the module files of the repaired scripts judge the tree.

The census keeps its form. It widens its corpus, reads a loop as an answer,
and compares the answer with `STREAMS` parsed from
`hooks/lib/console.py`. The tree is then repaired file by file, in the four
groups of `frame/design.md` *Scope* item 5.

The chosen approach's failure scenario, six months on: a contributor writes
a correct answer in a third spelling, such as `import console as c` with
`c.to_utf8()`, or `for n, e in console.STREAMS:`. The census refuses it,
and its message names the two forms it reads. A contributor who bends the
code to the census pays one rewrite, and contract rule 18 asks a party that
meets a correct spelling refused to report it, so the third form becomes a
row rather than a habit. A second scenario: an entry point that has to ask
the console before the loop moves it, like `broad_gate.py`, gets an
exemption above its first statement. That exemption excuses only the order.
The answer's pairs and its presence are still read (design *Scope* item 3).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. The corpus is every tracked `.py` | A fixture under `evals/behaviour/` or `tests/` that plants a script with a `__main__` block is refused, and carries an exemption that says it is a fixture. None exists at HEAD (design *Grounding*, the `ast` probe row) | chosen. The plugin ships from the repository root (`.github/scripts/run_tests.py:14-18`), so every tracked `.py` is shipped code, and the corpus needs no list kept beside the tree |
| A1'. The corpus is `tests/censuses.py#SHIPPED`, `hooks/`, `skills/` and `.github/scripts/` | The four entry points under `evals/scripts/` stay unread, and the measure counts them among the twelve without an answer. A new directory of scripts is unread until someone edits the tuple | rejected |
| A1''. A new list of directories, `SHIPPED` with `evals/scripts/` added | The same list kept beside the tree, which `skills/core/SKILL.md` *The rule a mechanism is kept against* refuses. At HEAD it reads the same 48 files as A1 | rejected |
| A2. Every entry point owes the answer, and only one that cannot give it carries its reason (Q1's default) | One more statement in twelve scripts that may never print a character a console cannot encode. Its cost is one line each, and `console.to_utf8()` is a no-op where the streams are UTF-8 already (`hooks/lib/console.py#to_utf8`) | chosen, as Q1's default |
| A2'. A script that runs only on CI's UTF-8 runner carries an exemption instead | The exemption states where the script runs, and no check reads that. Seven of the seventeen run only from a workflow, and the other ten do not: `bin/test` and `bin/test.cmd` run `run_tests.py` on a contributor's machine, `seal mutate` and `seal layout` run `mutation_check.py` and `test_layout.py`, and a person types `finding_counts.py`, `plugin_directory_check.py`, `tracker_labels.py --check` and the four under `evals/scripts/` (design *Grounding*, the row on where the 17 run). Each exemption costs the same line the answer costs, and states a fact that changes when a document starts telling a person to run the script | rejected |
| A3. Keep the inline loops, and read their answer | The census reads two forms of one answer, which costs one reader more than A3' | chosen. `hooks/lib/console.py`'s docstring gives reasons for the loops of `chain_check.py`, the three release scripts and `dispatch.py`. The census reads the answer, as "What must not diverge is the ANSWER" (`:64`) asks |
| A3'. Replace every loop with `console.to_utf8()`, and read the call alone | `chain_check.py`'s refusal, printed when a reader it loads is missing, meets the console's code page before the call can be made. `dispatch.py` depends on a module whose failure it reports. The release scripts lose the named result they give when a module will not load. All three are stated in `hooks/lib/console.py`'s docstring, and each breaks | rejected. The premise that keeps the loops is checked: each of those reasons stands in the docstring at HEAD |
| A4. A loop's pairs must equal `STREAMS`, and the five loops without `stdin` gain the `stdin` pair | Five scripts put a stream they never read into UTF-8, which is a no-op for them | chosen. Equality is read exactly |
| A4'. A loop may leave out `stdin` where the file reads no `stdin` | Whether a file reads `stdin` is a guess: `input()`, `fileinput`, `argparse.FileType("-")` and a library's read all reach it. `skills/core/SKILL.md` *The rule a mechanism is kept against* says a script holds a gate only on a fact it reads exactly | rejected |
| A5. The answer is the block's first statement; an answer out of order is refused at the block's first statement, and the exemption for it stands there | Two exemptions are added, in `broad_gate.py` and `seal_stamp.py`. Each excuses the order alone | chosen. The census keeps the order it reads at HEAD (`tests/test_censuses.py`, the `hooks/after.py` arm) |
| A5'. Accept the answer anywhere in the first block | A call after `main()` is accepted, and the gate prints before its streams are fixed. The `hooks/after.py` arm of the census's case is reversed | rejected |
| A5''. Refuse the order at the `if` line, or at the answer's line | At the `if` line, the exemption also excuses a block that loses its answer. At the answer's line, it also excuses drifted pairs, which is the class with a catch record | rejected |
| A6. Read the first module-level `__main__` block of a file and no later one | A later block's statements run after the first block's, so nothing is lost | chosen. `chain_check.py` and `pr_body.py` give the answer in their first block, before they load their readers |
| A6'. Read every module-level `__main__` block | `chain_check.py:2047` and `pr_body.py:784` are refused although their streams are already set, and each needs an exemption that says so | rejected |
| A7. The five scripts that call `console.to_utf8()` inside `main()` move the call to their `__main__` block | A test that calls `main()` in the same process no longer has its streams reconfigured, which is what `hooks/lib/console.py`'s docstring asks for | chosen. No file calls these scripts' `main()` from outside, and every workflow runs them as scripts (executed: `git grep` over the tree) |
| A7'. The census follows the block's call into `main()` and reads the call there | The census would trace calls through functions, which is no longer a fact read exactly. `main()` is also what the tests call in the same process | rejected |
| A8. Remove `tests/hooks/test_console.py#Test_module.test_a_release_script_run_on_its_own_gives_the_answer_streams_holds` | The census reads each loop's pairs and its `reconfigure` call, and no longer runs the scripts. A loop that the parser reads correctly but that fails at run time is no longer caught for these three. The loop form of design *Scope* item 2 names the call and its keywords, so the case catches nothing the census misses | chosen. The case's docstring gives its reason: those scripts spell the loop inline and no check read `.github/scripts/` |
| A8'. Keep the case | Two holders of one fact for three files, and none for the other fifteen loops | rejected |
| A9. The census parses `STREAMS` out of `hooks/lib/console.py` under `ROOT` | A case cannot plant another `STREAMS`. None needs one | chosen |
| A9'. A literal copy of `STREAMS` in `tests/censuses.py` | A copy kept beside the tree, which drifts when `STREAMS` changes | rejected |
| A10. A script that puts `hooks/lib/` on `sys.path` at import calls `console.to_utf8()`; any other spells the loop | The tree keeps two forms, which A3 already accepts | chosen. A script that loads nothing from `hooks/lib/` at import would add a load that can fail before the answer. That is the reason `hooks/lib/console.py`'s docstring gives for `chain_check.py` |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | design *Scope* items 1, 2, 3, 4 and 5, and the `## Removes` rows on the census's restriction, `dispatch.py`'s exemption, the run-time case, the `tests/x.py` arm and the calls inside `main()` | Each case of *Scope* item 4 seen red at `215ad6020` and with only its own guard removed, as the phase record states. The widened census run over the tree before *Scope* item 5's repairs prints the 25 lines of design *User scenarios & acceptance*, and after them it prints none. `bin/test -q tests/test_censuses.py tests/hooks/test_console.py tests/hooks/test_dispatch.py`, and the module file of each script the phase edits | 6b4471be6 |
| 2 | design *Scope* item 6, item 7's answer in `hooks/lib/console.py`'s docstring (its census docstring closed in phase 1), and the `## Removes` rows on that docstring's open question and the `CONTRIBUTING.md` clauses and pin | The text pin seen red against the old sentence. `bin/test -q tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py tests/hooks/test_console.py tests/test_censuses.py` | 4355ee989 |

## Operational impact

- No migration, environment variable or dependency. The census reads more
  files, at 0.51 s for one parse of each tracked `.py` (design *Grounding*,
  the cost row).
- **Files shared with the release's other work items.** #1254 edits
  `evals/scripts/noninferiority.py`, and phase 1 adds one statement as the
  first statement of that file's `__main__` block at `:1598`. The second of
  the two branches to merge into `release/v0.32.0` meets that hunk. Either
  branch also meets the other's new entry points: an entry point #1254 or
  #1256 adds without the answer is refused by this census once both stand
  on the release branch. The orchestrator that merges the second branch
  runs `tests/test_censuses.py` on the merged tree and gives each such entry
  point the answer. This work touches no file #1256 names.
- **What the pull request body carries**, by `CONTRIBUTING.md` *What a
  change to a gate must carry*:
  - The tests seen red: phase 1's and phase 2's records.
  - The failure direction: the census refuses more. A wrong refusal costs
    a contributor one rewrite into a form the message names. A wrong
    acceptance lets a script die with its stdout empty on a console that
    cannot encode what it prints.
  - The prompt budget: none. The census runs in the suite and asks nobody.
  - Platform honesty: the census reads source text and runs nothing, so it
    reads the same on every platform. The repaired scripts' behaviour under
    cp949, cp932 or cp936 was not run on Windows.
  - What it removes: design `## Removes`.
  - What it reads: the first module-level `__main__` block of each tracked
    `.py`, through `ast`. A statement in neither of the two forms is not
    read as an answer. The refusal at the `if` line and the refusal at the
    `for` line each say what the census did not read rather than that the
    file gives no answer, and the refusal at the block's first statement
    names the line of the answer it read.
    Whether an exempted entry point's reason holds is the proofer's to
    judge at review.
- The changelog fragment carries no `### Process changes` table (design
  *Grounding*, the release row).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-04 | The frame is folded to phase 1 as built: *Scope* items 2, 4 and 7, *Data & interfaces* and phase 2's row state what phase 1 did, Q2 records the crafter's answer, and the measures are cited at `569780eff` and `48d035aa6` | The crafter's hand-back named each statement HEAD contradicts, read whole against HEAD by the orchestrator; the measures' commits are reached by no `main` or release ref, so `tests/text/test_a_cited_commit_outlives_the_squash.py` refuses them, and `569780eff` (#1257) and `48d035aa6` (#1237), their squashes onto `main`, hold the same files byte for byte (executed: `git diff --quiet`). The same unreached citation stood in all three frames of the release, carried from the issue bodies, so the issue bodies of #1254, #1255 and #1256 are corrected in place as its prevention home | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-04 | The frame is folded to phase 2 as built: *Scope* items 5 and 7 and `## Removes` state what phase 2 did, and every line-number coordinate of `hooks/lib/console.py` and `tests/censuses.py` in *Technical context*, *Alternatives* and the phases table is replaced by the function or the docstring it named | The crafter's hand-back named each line number HEAD has moved; a line number is a coordinate kept beside the tree that drifts at the next edit with nothing to catch it, so it is replaced rather than renumbered | `skills/core/SKILL.md` *The rule a mechanism is kept against* ("Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate"); `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-04 | The frame is folded to round 1's fix pass: *Scope* item 4 lists the target case, item 6 states the bullet's loop form and the three facts its pin holds, and *Operational impact* states what a refusal says | The fix pass named each statement HEAD contradicts (round-1#1 and #2, closed `fixed` at `bc6d3387a` and `6c77082d6`), read whole against HEAD by the orchestrator | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-04 | *Operational impact* names which refusals say what the census did not read, as round-2#1 asks; the fragment's sentence goes to the crafter, and no verifying round follows, since the finding and both fixes stand in the work item's records alone | Round-2#1 located the defect in this plan's line and `changelog.md:3`; the order refusal at `tests/censuses.py#entry_point` names the answer the census read (read) | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* |
| 2026-11-04 | The loop form does not also require a `hasattr` guard, the question rounds 1 and 2 left to the orchestrator | No entry point at HEAD spells the loop without it (round 1's probe, `trail/rounds/round-1.md`), and a further shape the census refuses is one more grammar edge whose record of catches is none; a loop that raises on a missing stream is a defect a case running the script would show, not one the census exists to read | `skills/core/SKILL.md` *The rule a mechanism is kept against* |
