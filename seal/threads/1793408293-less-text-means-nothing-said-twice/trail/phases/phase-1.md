# Phase 1: 1793408293-less-text-means-nothing-said-twice

## What this phase found

**The frame holds against the tree.** The anchor sentence ends on line 106 of `skills/core/SKILL.md`, as `frame/plan.md` *Technical context* says. `origin/release/v0.25.2` is `13dc7c63`, the merge base of this branch, and `.claude-plugin/plugin.json` read `0.25.1` before the build (executed). The enumeration command of `frame/design.md` *Data & interfaces* listed the fifteen recorded lines at `01d09c18` (executed).

**`tests/behaviour/test_docs_line_wrap.py` covers the core.** `COVERED` names `skills/core/SKILL.md` at line 170 of the module, and `LIMIT` is 88 display columns (read). Line 106 was 86 columns before the build, a sentence spliced in without a re-wrap. The new sentence starts on that line after the anchor, and the old tail of line 106 moves to a new line. The paragraph keeps its band, with no line past 77 columns, and lines 107 onward of the old text are unchanged: the diff changes one line and adds three.

**The sentence is *Scope* item 1's text, word for word.** No rewording was needed.

**S1's grep gives line 106, the anchor's own last line.** The plan's *Verified by* cell says the line after the anchor. The sentence follows the anchor on the line where the anchor ends, so `git grep -n -F 'Less text means nothing said twice' -- skills/core/SKILL.md` returns one line, `106` (executed).

**S3 lists seventeen lines, not sixteen.** The enumeration at `af0bdaff` lists the fifteen recorded lines unchanged and both of the sentence's first two lines: line 106 matches `fewer lines`, and line 107 matches `(change).{0,10}grows` on "a change that grows" (executed). Both are the new sentence, and neither holds a change's net line count as a criterion. The frame counted one match for the sentence because it matched only `fewer lines`. Wrapping keeps `fewer lines` and `Less text means nothing said twice` each on one line, so both greps still find the sentence.

**The hook's output is 6,523 characters with the sentence, against `CAP` 10,000.** `hooks/lib/core.py#output` was measured in this clone at the build (executed). P1's 6,653 was measured in a clone at a different path, and the 130-character difference was not traced; `tests/hooks/test_core.py` passed (executed).

**No case is written new, and no `seal mutate` runs.** The phase changes prose and one version string. `skills/verify/SKILL.md` *The narrow command still has to be able to fail* gives prose only what parses it, and no unit adds behaviour. `frame/plan.md` *Alternatives considered* rows B to D reject a pin and a sweep.

**The narrow run.** The plan's six modules and every other test module that names the core, globs `skills/`, reads `.claude-plugin/plugin.json`, reads a changelog fragment, or reads the tree's own `seal/threads/` records: 45 modules through `bin/test`. Before the records were written it gave 2,908 passed, 9 skipped and one failure, `test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, which asks for this work item's `gaps.md` (executed). The same 45 modules with this record, `gaps.md` and the Status cell in the working tree gave 2,909 passed and 9 skipped, exit 0 (executed).

**The fragment's *Changed* entry says #1148's issue wrote the count.** The owner's comment that the row cites says the issue's last *Done when* read "the change removes more lines than it adds", and `frame/questions.md` Q2 of #1148 quotes it (read). The entry names the issue as where the count was written, and the review finding and the question as what followed.
