# 1792624592-the-release-seal-is-drawn-from-the-stamps-cells — review round 2

target: 478da5c6, fixes 736062fe..478da5c6

This round verifies the fixes. It read the diff from 736062fe to 478da5c6:
the smith's fix at b4772c74, the changelog fragment at d9dad63b, the
framer's lines in `spec.md` and `plan.md` at 478da5c6, and the two answer
lines per finding in `rounds/round-1.md` at 6170385c. The work happened in a
`git clone --no-local` of the branch at 478da5c6, under the round's scratch
directory. From round 1 it carried only coordinates: the line ranges of
`draw`, `seal_release` and the `seal` job, and the probe shapes in round 1's
`## Probes`. It rewrote those probes and ran them again rather than taking
round 1's results.

## Findings

None. Each of round 1's three findings is confirmed below. Every line the
four commits changed was read for a regression, and none was found.

## Confirmations

confirms: round-1#1
S2's case now replaces `CHART` and `LIGHT` on the stamp module that
`release_seal.py` loaded and on the one the case loads by path. It asserts
that cell (14, 14) carries the new colour
(`tests/test_the_release_seal_is_drawn.py:122-152`). In the clone, `draw`
was changed so that any colour outside a literal copy of the nine colours
was painted as the copy's `LIGHT`. S2 failed against that draw, and S1
still passed, as the smith's answer says S1 does. The draw was then
restored with `git checkout`. Both cases passed on the tree as it stands
(`bin/test tests/test_the_release_seal_is_drawn.py -q`: exit 0, 48 passed).
Executed.

confirms: round-1#2
S2 now imports Pillow at its top and uses it in its last assertion. With
`sys.modules["PIL"]` set to None, both S1 and S2 raised
`builtins.ModuleNotFoundError: import of PIL halted; None in sys.modules`,
and neither raised `Refused`. So the sentence in
`.github/scripts/run_tests.py:334-338` and its pin at
`tests/test_the_suite_has_a_command_that_is_cheap_twice.py:919` are now true
without being edited, as the answer says. Executed.

confirms: round-1#3
The `draw` docstring (`release_seal.py:429-437`) and the workflow comment
(`publish-release.yml:98-100`) now say the suite fails before the draw. The
smith's answer says this does not depend on pip, and that holds. In the
job, the suite step fails, and `seal_release` refuses on `SUITE_OUTCOME` at
`release_seal.py:479-481`. On the hand-drawn route, which sets no
`SUITE_OUTCOME`, `suite_counts` refuses with "the suite at the tag did not
pass" (`release_seal.py:285-286`). Both refusals come before `draw` at
line 501. The docstring's last sentence names the remaining case, a draw
under a Python the suite did not use. Read.

The docstring says "its pixel cases and stamp cases need both of the first
two". This holds when read of the cases together. Read case by case, it
would say the stamp cases need Pillow, which they do not
(`test_the_stamp_module_imports_with_pillow_blocked`). This is no finding,
because the rule on text with one reading covers skills, agent definitions,
templates and frames, and a code docstring is none of them. It is noted for
whoever next edits the paragraph.

A `git grep` at 478da5c6 for "lands here", "the draw's `::warning::` says so"
and "names Pillow not" outside the round records matched no sentence about
the seal. So the class of false sentences has no member left. Executed.

confirms: none
The framer's `spec.md` changes at 478da5c6 hold. The new *Data & interfaces*
sentence, that in the `seal` job neither a missing Pillow nor an unloadable
stamp module reaches `draw`, matches the read above. The checklist `to:`
line is now "the seal could not be drawn or written,". `rule_changes.parse`
returned three `change` items with no error. Each `apply_op` applied once.
The applied box reads "the suite at the tag did not pass, the seal could not
be drawn or written, a `gh` call failed, or the glance table ...". The
checklist pin's assertions do not touch that clause. Executed.

confirms: none
`plan.md` *The window* now says that a hand-drawn run without Pillow fails
at the suite: the pixel cases fail with a `ModuleNotFoundError` naming
`PIL`, and the script then refuses because the suite did not pass. The
probe for round-1#2 shows the first half. `suite_counts` at
`release_seal.py:285-286` gives the second half. Read and executed.

confirms: none
The changelog fragment at d9dad63b now says that where Pillow is missing or
the stamp's module will not load, the suite at the tag fails first, and the
warning names the suite's outcome. This matches the confirmation of
round-1#3. The fragment has no line starting `## `. Read.

confirms: none
The fix pass changed only the `verdict:` and `answer:` lines of
`rounds/round-1.md` (`git diff 2d7daefa..6170385c`). Each `fixed b4772c74`
touches a path the finding's `location:` names: the test module for
findings 1 and 2, and `release_seal.py` and `publish-release.yml` for
finding 3. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| CI run 39697436778 at 478da5c6 | CI | the orchestrator, which started it and has not read it yet |
| The full suite, the repository-wide lint and the typecheck at 478da5c6 | the branch | the orchestrator's `broad-gate` run, now due, since this round leaves nothing open |
| The `seal` job at a real tag push | `.github/workflows/publish-release.yml` | the owner, at the v0.22.3 release run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_the_release_seal_is_drawn.py -q` in the clone at 478da5c6 | exit 0, 48 passed |
| `bin/test tests/test_a_release_publishes_its_note.py -q` in the clone | exit 0, 32 passed |
| `test_tmp_round2.py` running S1 and S2 with `sys.modules["PIL"]` set to None | both raised `ModuleNotFoundError`, and neither raised `Refused` |
| S1 and S2 with `draw` painting any colour outside a literal copy of the nine as the copy's `LIGHT` (edited in the clone, then restored with `git checkout`) | S2 failed and S1 passed |
| `rule_changes.parse` and `apply_op` over `spec.md` and the two `docs/` files, in memory | three `change` items, no error, each applied once |
