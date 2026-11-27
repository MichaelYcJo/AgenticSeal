# Phase 2: 1795742080-a-session-is-bound-by-the-crafters-rules

## What this phase found

**The frame holds for this phase, with four places where the tree differs from what it states.** The paragraphs *Scope* items 2 to 7 move or rewrite stood where `frame/design.md` G1, G2, G4, G9, G11, G15 and G16 put them (read at `1c045ac40`). The four places:

- *Scope* item 8 has `MOVED_OUT_OF_CRAFTER` name each moved rule "by a code span only its paragraph held". The paragraph **The frame is judged before it is built to** in `agents/crafter.md` held only the paths `trail/phases/phase-N.md` and `## What this phase found`, and both also stand in the *Job* or in step 5. So the entry names the lead with its bold marks, which step 3's citation in italics does not contain. The *Never* line "Build beyond the request" held no code span either, so its entry names the words "no TODO stub in a core path".
- `frame/questions.md` Q2 asks whether a case the G14 search missed holds a moved sentence. One case did. `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py#test_crafter_cites_the_handoff_for_the_narrow_form` read `docs/running/the-run.md` *The handoff* anywhere in `agents/crafter.md`. After the move it would have passed on the citation in **A handoff's claim is measured where the handoff says**, a rule that stays in the definition. It was green and pinned nothing. The case now reads the **Find the runner, and type the narrow form** paragraph of `skills/implement/SKILL.md`. No case failed on a size. The byte counts went from 9219 to 5815 for `agents/crafter.md`, from 22290 to 28907 for `skills/implement/SKILL.md`, and from 9404 to 8808 for `skills/implement/fix-pass.md` (executed: `git show <commit>:<path> | wc -c` at `1c045ac40` and at `d48344a1f`).
- *Scope* item 5 adds a sentence to *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*. The section's first bold lead still said that each phase is built by a fresh `crafter` spawn, which would contradict the new sentence. The lead now opens "Where a crafter builds".
- *Scope* item 6 rewrites step 1 and the frame-read lead of `skills/implement/orchestration.md`. Step 2 also said that the orchestrator "spawns the crafter", which contradicts a session's build in the same way. It now adds "or builds itself where `routing.md` answers `Implementation` with `the session`".

**Decisions settled while writing the text.** Each was judged against `frame/design.md` *Scope* unless the entry names another document.

- The builder paragraph says that each rule of `skills/agent-contract/SKILL.md` binds both builders, as item 2 asks. Contract rule 2 and contract rule 6 withhold acts from every agent, among them the broad gate, which the orchestrator's own procedure gives it. Read as written, the paragraph would withhold the broad gate from the orchestrator. One clause says that such a rule withholds the act from the crafter and leaves the orchestrator the acts its procedure gives it. The grounds are `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*.
- The rule on the read gives the command `seal range <item> --from <commit> --out <file>` as an inline code span, not as a fenced block. `tests/text/test_a_moved_rule_leaves_its_definition.py#lead_paragraph` reads a rule as the text up to its first blank line. A fenced block would end the paragraph before the rule's other facts.
- Item 6 has step 1 name rules 4, 5, 19 and 21 in one sentence, and then state rules 21, 19, 4 and 5 again one by one. Both sentences said the same thing, so a case that pins "contract rule 4" stayed green with either removed. Step 1 keeps the three sentences that each say what one rule asks, and the list sentence is removed (`c6e231e5f`). The grounds are `skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has one source.
- The intro of `skills/implement/fix-pass.md` restated who makes the pass. It now cites the builder paragraph, as item 4 removes the mapping from the section below it.
- Item 4 names the commit the pass's range starts after as the one in "the sealer's block" where the pass fixes a sealer's verdict. `docs/forms/the-guarantee.md` calls that block a verdict block of `guarantee.md`, which holds a `target:` line, so the paragraph says "the newest `guarantee.md` block's `target:`".

**What building found in `seal range`.** The S11 case, `tests/skills/test_range_read.py#test_accepts_a_hunk_inside_a_docstring_widened_to_its_paragraph`, went red against the phase-1 script. `git diff -W` alone printed the docstring paragraph from its third line (executed). `c5979ac4d` unions each `-U0` hunk's paragraph bound with the `-W` hunk that holds its first changed line. A joined span equal to one `-W` hunk prints as git printed it, function line included. Any other span prints under a header in git's form with no function line.

The first `seal mutate` round over that unit left six mutants alive. They were the end of the `-W` span, the verbatim branch, both containment bounds, the key of the kept spans, and a `break` after the first holding `-W` hunk. The old `-W` case changed one line in a function with no blank line, so a print by either bound passed it. `9989e60e0` and `a61e578a5` rebuilt it over three paths:

- a function whose body holds blank lines on either side of the change, under an `import`, so that the header carries a function line;
- a change to a function's first line;
- a change to the last line of a file that ends in a function.

Each path asserts its whole `git diff -W` print. The `break` was removed, since no fixture tells it apart: two `-W` hunks never hold one line. The no-op `wide or printed` was removed too. An emptied path prints the same hunk under `-W` and `-U0` (executed: both prints on a fixture). The second round read `red` for 11 of 11 mutants (executed).

**Seen red.** Each case of *Scope* item 8, and each case a moved rule took with it, was run by `seal mutate` with only the sentence or span it pins removed. Each read `red` (executed):

- each phrase of `MOVED_OUT_OF_CRAFTER` this phase added, pasted back into `agents/crafter.md`;
- the facts of `BUILDERS_RULES`;
- the facts of the rule on the read, and step 10's citation of it;
- the facts of the account's rule, and step 10's citation of it;
- the facts of the builder paragraph;
- the facts of *The narrow set, then the read of the range*, and the citation in `skills/implement/fix-pass.md` of the rule on the read;
- the frame rule in `tests/behaviour/test_chain_hooks_hardening.py`;
- the command line, `-p no:xdist` and the 300 s bound in `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`;
- the handoff citation in the **Find the runner** paragraph;
- *Scope* item 5's sentence;
- step 1's "contract rule 4" and "contract rule 5".

**The searches of `frame/design.md` G18, at `b6816d2b0`.** V1, V3 and V4 printed nothing. V2 printed `skills/implement/SKILL.md` alone, at lines 167, 192, 201, 244 and 249 (executed, with the commands G18 gives).

**The phase boundary.** `bin/test tests/text tests/behaviour tests/skills/test_range_read.py tests/skills/test_seal.py tests/skills/test_mutation_check.py tests/test_censuses.py -q` exited 0 at `b6816d2b0`: 1602 passed, 10 skipped. Its 9 warnings name no path this phase changed (executed). `d48344a1f` rewraps three lines of prose after that run. The cases that read the two files, `tests/behaviour/test_docs_line_wrap.py` among them, passed again after it (executed).
