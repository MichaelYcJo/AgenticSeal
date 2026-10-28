# Review round 2: 1793171929-the-suite-tells-the-agent-it-is-evaluated

target: f6ac4ff5, fixes 4e9d61ca..f6ac4ff5

## Findings

This round opens nothing.

## Confirmations

confirms: round-1#1
The close `fixed efa93f62` holds. The fix range is three commits:
`efa93f62` changes the text case, `bc5388dc` rewrites the `gaps.md`
clause, and `f6ac4ff5` writes round 1's verdict and answer.

What the code does now (read
`tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:114-153`).
`copied_spans` returns `None` only where no rendering of the generator
matches the file (`:122`). A rendering that matches and holds no copied
slot still returns `[]`, so a matched file is not reported as stale. Where
`hits` receives `None`, it appends `STALE` at line 0 (`:142-144`), masks
nothing and scans every line, as before. A case name takes at most one of
the two prefixes, so a file can take at most one `STALE` hit.

Round 1's executed evidence, run again. The same drift as round 1 was
applied to a copy of `replay-1791382684-r2/prompt.md`: "commit nothing
yourself." became "commit nothing.". `hits` now returns the `STALE` hit at
line 0 first, then `judge` at line 5 (executed). Over HEAD's suite it
returns no hit (executed), so no committed replay or seeded case is stale.

The answer's claim of red holds. With `:122` set back to `return []` in the
scratch clone, `bin/test tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`
exited 1. The S5 case's third reading got `(1, 'judged')` where it expected
the `STALE` hit (executed). The line was restored and the clone's diff read
empty. The answer's mutant count was not run again.

The fix makes one consequence that the finding's fix block also had. A
replay or seeded case its generator no longer writes is now refused even
when it holds no refused word. `frame/design.md` S4 names refused words
only. The refusal enforces `evals/README.md:104`, "The cases are
generated, never edited by hand". The hit names the remedy, `--case NAME`.
This round judges it no defect.

`gaps.md:27` now states the behaviour as built (read). The answer leaves
`trail/phases/phase-1.md:40`, "A file that holds none keeps no exemption",
as it is. That sentence is still true of the code, so nothing contradicts
it.

confirms: none
The modules that read the files the fix range changed pass, and so does
the layout check (executed). `git grep -l` over `tests/` for each changed
path and name chose the modules. Six that read records, docs or the test
layout were added: `test_rule_cases.py`, `test_docs_line_wrap.py`,
`test_the_record_is_written_in_words.py`, `test_one_word_one_meaning.py`,
`test_no_document_names_the_old_roots.py` and `test_test_layout.py`. The
38 modules ran in one `bin/test` call: exit 0, 3577 passed, 4 skipped. `bin/seal layout --check` exited 0, with 160 files
read and 0 refused.

Carried from round 1 and not re-derived: the generators' outputs equal the
committed cases, S2, S4's red at the base and S6's red. The fix range
touches none of `evals/` or `tests/evals/`, so the check behind each fact
did not change.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `f6ac4ff5`. Not run here (contract rule 2), and labelled `unverified` | the branch at `f6ac4ff5` | the orchestrator, through `seal gate` |
| The two `seal mutate` mutants the answer reports. Not run again; the red of the `return []` mutant was reproduced by hand above | `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:122`, `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:142-144` | the sealer, if it samples the claim |
| Round 1's other two rows: whether a directory `claude plugin eval` makes holds a refused word, and the odds of `mkdtemp`'s random characters spelling a stem. Outside this fix range | `evals/scripts/noninferiority.py:611-632` | the orchestrator, with `questions.md` Q2 |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 38 modules that read the changed files, `-q` | exit 0, 3577 passed, 4 skipped |
| `bin/seal layout --check` | exit 0, 160 files read, 0 refused |
| `python -c` calling `hits` over a drifted copy of `replay-1791382684-r2` and over HEAD's suite | the `STALE` hit at line 0, then `judge` at line 5; no hit |
| `return []` set at `:122` in the scratch clone, `bin/test tests/text/test_no_case_tells_the_agent_it_is_evaluated.py -q -p no:xdist`, then restored | exit 1, the third reading missing the `STALE` hit; clone diff empty after the restore |
