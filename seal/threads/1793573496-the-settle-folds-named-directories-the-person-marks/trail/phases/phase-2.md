# Phase 2: 1793573496-the-settle-folds-named-directories-the-person-marks

## What this phase found

**The frame holds, and design A9's search cannot see the sentence it was
written for.** At `a3634eeb0`, `skills/settle/SKILL.md` has 419 lines, the
`seal settle [--apply]` rows stand at `README.md:265` and `README.ko.md:259`,
and the readers named in `plan.md` *Technical context* pin what the plan
says they pin. The intro's "**It asks nobody at any step**" is wrapped
after "asks", so A9's `git grep -n -i 'asks nobody\|asking nobody\|묻지 않'`
never printed it, at the base or here. At the close the search was run as
the design writes it, and again over each changed file with its line breaks
folded. Neither found a sentence that says the settle asks nobody. Judged
against `agents/crafter.md` *The frame is judged before it is built to*.

**Decisions settled while writing the text**, each against design *Scope*
items 4 to 8 and D5:

- The rules of items 4 to 7 are in one new section, *Directories a person
  names*, after *The settling session's procedure*, and the procedure's
  steps link it. That is the plan's *Technical context*. The procedure
  gains three steps: step 1 asks the first question, step 2 passes
  `--from`, and step 3 writes the proposal rows and asks the second
  question. The old steps 2 to 9 are now 4 to 11. The two cross-references
  inside the procedure moved with them, "as step 4 writes a group's" and
  "step 10 runs every one". A `git grep` for a step number cited with the
  procedure's name found no citation outside the skill.
- The listing is not a proposal because each of the skill's three
  descriptions of it says so, as D5 asks. *What the dry run shows* gives
  the listing's facts as phase 1 built them, and ends by saying no line of
  it is a proposal. The new section's paragraph *The listing is not a
  proposal* says what a line does not tell, and whose the proposal and the
  mark are. Step 3 of the procedure says the row is the session's to
  write.
- The listing is described as phase 1 built it, not as the design's *Data
  & interfaces* drew it. A working-tree change is what `git diff HEAD`
  names (phase 1's departure). A file staged and never committed reads
  `no commit adds it`, as an untracked one does. A file two directories
  hold is listed under the first one named.
- The first question states the limit folded at `a3634eeb0` in one
  sentence. The proposal's `skip` cases name "a file of the `seal/` root"
  beside the design's three, so the sentence and the grounds agree.
- "Its last change is a commit that settle's merge commit reaches" is given
  its command, `git merge-base --is-ancestor <last change> <merge commit>`
  exiting 0. The design states the fact as reachability, and that command
  answers it from its exit code (`skills/core/SKILL.md` *Judgment is spent
  where meaning is the question, and a script answers the rest*).
- Step 11 names, besides the rows with their marks, the directories the
  first answer named. Where the answer was "none", it says whether the
  session took that answer because it had no way to ask. Design *Scope*
  item 4 asks the body to say so.
- The reference-root paragraph is rewritten where it stands, in *What
  `--apply` does* (contract rule 19). It keeps every fact
  `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`'s
  `READERS` reads, and gains that the settle reads a reference root only
  where a person names it, and does not read the row. No settle script
  reads `Reference specs`: `grep -rni reference skills/settle/scripts/`
  printed nothing.

**Two readers' shapes set where words could go.**

- `READERS` takes the paragraph around the first occurrence of
  `` `templates/setup/config.md` *Reference specs* `` in the skill. The new
  section comes before *What `--apply` does*, so its promote paragraph
  cites the reference-root paragraph by place and does not write that
  citation. Written there, it would have become the first occurrence, and
  the case would have read the wrong paragraph.
- `tests/text/test_settle_reads_before_it_removes.py#test_the_cheat_sheets_name_the_design_file_the_settle_reads`
  asserts that each README edition, its whitespace folded, names
  `` `frame/design.md` `` within the first 900 characters after the cell
  `` `seal settle [--apply]` ``. The first English draft of the row put
  that path at character 917 of the folded text, measured with a
  `python3 -c` count and not run as the case. The row was shortened to
  878. "asks the person, before its first edit," became "first asks the
  person", and the clause "`--apply` refuses `--from`" was dropped. The
  row still links the procedure, which states both. The window is the
  case's, not a fact a reader acts on. It is reported here and in the
  hand-back (contract rule 18), and the case is unchanged.
  `test_the_skill_states_the_settling_sessions_procedure` cuts the
  procedure at the first "## " after its heading, so no step before the
  `seal/follow-up.md` row writes a heading's name with its hashes.

**No case is new, and no unit was mutated.** The phase changes prose a
session reads. Under `questions.md` Q1's default (a), no case drives a
settling session, and `skills/verify/SKILL.md` *The narrow command still
has to be able to fail*'s *Prose only* row gives the readers that parse
these files as what can fail. No code unit adds behaviour, so `seal mutate`
owes no run.

**The phase-boundary set ran green in one command**, exit 0, 3,320 passed
and 9 skipped. It ran over the working tree that `7868ee56f` then committed
unchanged: 77 modules through `bin/test`, the plan's three among them. The
list is every `tests/**/test_*.py` that a `grep -rlE` names for
`settle/SKILL.md`, `setup/config.md`, either README, a `SKILL.md` glob, or
a walk of the tracked files (`ls-files`, `rglob`, a `.md` glob). The
pattern matches more modules than read the four files, and it is still a
sample of the readers: the broad gate is the whole. `seal rules --check`
was not run, because the phase writes no `check:` line.

**The census of the sentences this phase rewrote**, by `git grep -i`
outside `seal/threads/` for "asks nobody", "asking nobody", "ask nobody",
"asks no one", "asking no one" and "묻지 않", and for "never input",
"history, never input" and "decides from the tree". It is a search for
wordings, so it is a sample (contract rule 12). It found the skill's intro
and reference-root paragraph and the two README rows, all rewritten here,
and `docs/release-checklist.md` *2b*, which the design's rule changes
rewrite at the settle. Every other hit is about another party. The
framer's "asks nobody anything" and the orchestration rows that cite it
are about the framer. `templates/setup/config.md:228` is about `seal
gate`. The other hits in `README.ko.md` are the tagline, the migration
question and the mode question. The tagline, with `README.md`'s "without
asking anyone", speaks of the whole workflow, and the routing question
already did not fit it before this work. It is left as it stands.
