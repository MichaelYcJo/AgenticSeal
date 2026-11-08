# Phase 1: 1794142459-parity-reads-original-forward

## What this phase found

**The frame holds for this phase, with three coordinates that do not.**
Every section, clause and case `frame/design.md` *Grounding* reads for
items 1, 2, 3, 4 and 6 stood at `377e21a3f` as the row says. The three
*no*s, judged against the tree before the first edit:

- `frame/plan.md` *Phases* row 1's Verified by cell names
  `tests/text/test_docs_line_wrap.py` and
  `tests/text/test_a_cited_section_stands_in_its_file.py`. Neither exists
  (`ls` executed). Both modules are under `tests/behaviour/`, and this
  phase ran them there. `frame/design.md` *Grounding* names the first at
  `tests/behaviour/` and the second at `tests/text/`, and the scenario
  *Nothing else moves* names both at `tests/text/`.
- The same cell expects `git grep -n "Start every comparison there"` to
  print nothing. At HEAD it prints four lines, all in this work item's
  own frame: `frame/design.md:10`, `frame/design.md:36` and
  `frame/design.md:83`, each quoting the sentence as it stood at
  `9e758b0b0`, and `frame/plan.md:48`, the row that holds the pattern. Outside
  `seal/threads/` it prints nothing (executed:
  `git grep -n "Start every comparison there" -- ':!seal/threads'`).
- Folding these is the framer's and the orchestrator's; this phase leaves
  the frame's lines as they are.

**Two edits stand outside the sentences *Scope* names, each on a section
item 1 or item 2 rewrites.**

- *The original's coordinates* ends with
  `check: tests/text/test_review_axes.py`. *Scope* item 2 asks for a
  check line under *Parity review* only. `skills/implement/SKILL.md` *2.
  Implement test-first, and let each rule name its test* says a rule the
  work changes ends with a check line naming its case, and the first case
  below holds this section's rule. `seal rules --check` reads it (all 219
  check lines in 68 rule files hold, executed).
- *Parity review*'s opening sentence said stage 1 compares against the
  original "through the coordinates the design cites". The new paragraph
  says the walk starts at the original's entry point. Left alone, the two
  would stand side by side for the reader to choose between, which
  contract rule 19 refuses. The sentence now reads "from its entry point
  and through the coordinates the design cites". The section's heading,
  its block of four words and the block's check line stand as they were.

**The new paragraph of *Parity review* names the proofer as the party
that walks.** *Scope* item 2 writes "Stage 1 walks the list". Stage 1 is
the proofer's under `through the review chain`, and the paragraph's last
sentence gives the sealer's walk under `straight to the PR`. The grounds
are `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
읽히게 쓴다*, which asks each instruction to name the party that acts.
The walk is stated over the original's output surface, with the design's
list opened at each item. Read as "walks the list", it would start at the
list, and an item the list lacks would be met by nobody, which is the
defect item 1 removes.

**The four cases stand in `tests/text/test_review_axes.py`, as *Scope*
item 6 places them.** Before writing them I read the group each one
covers, as the crafter's rule *A new test starts from its group* asks:

- The tracer's existing case,
  `tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_tracer_opens_the_parity_skill_and_returns_original_not_found`,
  pins step 1 and the guessed-original rule from #970. Nothing pins step
  6.
- No case reads `agents/framer.md` step 4 (`grep` over `tests/` for the
  definition's readers, executed).
- `seal layout --pairs` exits 0 (executed).

So none of the four duplicates a case. They join the module that already
holds the skill's half of the parity method, the module the two new
check lines name. The module docstring now names what it holds. Two
helpers, `prose` and `step`, read a section without its fences and check
lines, and one numbered step of `## Order of work`. The module imports
`PARITY_REVIEW`, `PARITY_WORDS` and `section` from
`tests/text/test_the_record_is_written_in_words.py`, as
`tests/text/test_a_moved_rule_leaves_its_definition.py` imports from its
neighbour, so the four words have one home.

**What each case pins, weighed under `docs/running/what-a-script-gates.md`
*The checks*.** Each guard is a fact a reader acts on, and none was
dropped:

- the list's home, the path and heading `` `frame/design.md` *Grounding* ``;
- the list's writer, `framer writes the list`. The section names the
  framer a second time, in "does not resolve for the framer", so the
  party alone stays green with the writer removed. The first draft
  asserted `framer` alone, and `58158cea7` widened it before any
  mutation run;
- the framer's citation of `skills/legacy-parity/SKILL.md` *The original's
  coordinates* at step 4;
- the verdict an absent item takes: `differs` among the backticked words
  of *Parity review*'s prose outside the block that `PARITY_WORDS` holds;
- the walk's home: `round record` and `` `## Confirmations` `` in that
  prose;
- the tracer's step 6: `output surface`, the list's name in the skill,
  and `lacks`.

**Seen red, before the text was edited.** At `377e21a3f`, with the four
cases written and no other file changed, `bin/test
tests/text/test_review_axes.py -q -p no:xdist` gave 4 failed and 5 passed
(executed). Each failed on its own first guard:

- *names no home for the list*;
- *does not send the framer to the list*;
- *gives an absent item no verdict*;
- *step 6 lost 'output surface'*.

**Mutation runs**, `seal mutate` over `58158cea7`, one guard at a time,
each with `--tests "bin/test tests/text/test_review_axes.py -q -p
no:xdist -k <case>"`. All eight were red, exit 0, and each failed on the
assertion of the guard it broke (executed):

1. `skills/legacy-parity/SKILL.md`: `` `frame/design.md` *Grounding*: each ``
   was replaced with `the design: each`, and the run failed on *names no
   home*.
2. Same file: `The framer writes the` was replaced with `Someone writes
   the`, and the run failed on *names no writer*.
3. `agents/framer.md`: ``and with it `skills/legacy-parity/SKILL.md` ``
   was replaced with `and with it the parity skill`, and the run failed
   on *does not send the framer*.
4. `skills/legacy-parity/SKILL.md`: ``is `differs` by default`` was
   replaced with `is a finding by default`, and the run failed on *gives
   an absent item no verdict*.
5. Same file: `stands in the round` was replaced with `stands in the`, and
   the run failed on *'round record'*.
6. Same file: ``of its `## Confirmations` naming`` was replaced with `of
   it naming`, and the run failed on *'`## Confirmations`'*.
7. `agents/tracer.md`: `output surface the design` was replaced with
   `surface the design`, and the run failed on *'output surface'*.
8. Same file: `list lacks, with` was replaced with `list misses, with`,
   and the run failed on *'lacks'*.

`93d4b9683` changed only the four docstrings, which had numbered the
design's scenarios S1 to S4. The scenario table numbers none, so each
docstring now names its scenario by name. `24e9aee1e` corrected one
comment over the verdict guard, which had said the proofer writes the word
at the start of a finding's line; the round record's form names no such
line. No assertion changed after the mutation runs.

**What `agents/tracer.md` step 3 leaves for a reader.** Step 3 still
reads "search the original only for the axes they leave". Step 6 now
asks for each item of the surface the design's list lacks. An item on an
axis the design does cite is reached by step 4, which traces each axis
to what the original sends. So the two steps do not contradict each
other, and step 3 stands, as *Scope* item 3 changes step 6 alone. A
proofer that reads step 3 as excusing the tracer from walking the
surface of a cited axis has a finding to raise against this reading.

**The phase's scoped run.** One command over the phase's 80 test
modules, `bin/test <80 modules> -q`. The plan row's eight modules are
among them, at their real paths. The other 72 are every module under
`tests/` whose source names a path this phase changed (`legacy-parity`,
`tracer.md`, `framer.md`, `test_review_axes`, `gaps.md`, `plan.md`,
`phase-`, `threads`), or that lists or walks the tree (`ls-files`,
`os.walk`, `glob(`, `rglob`, `listdir`). The list comes from one `grep
-l` over `tests/`, with `conftest.py` and `tests/censuses.py` left out,
since neither is a test module. The census still runs, through
`tests/test_censuses.py`. It ran over `93d4b9683` with this record,
`gaps.md` and the Status cell in the working tree, which is the content of
the commit that adds them, less this sentence. It gave 4591 passed and 9
skipped, exit 0 (executed). `seal rules --check` and `seal layout --pairs`
both exit 0, and `uvx ruff check` and `uvx ruff format --check` pass over
`tests/text/test_review_axes.py` (executed).
