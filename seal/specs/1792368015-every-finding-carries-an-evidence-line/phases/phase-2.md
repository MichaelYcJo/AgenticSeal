# 1792368015-every-finding-carries-an-evidence-line — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | ee05f824 |


## What this phase was asked

Phase 2 is the instructions. In `agents/warden.md`, step 7 names the line,
and the coverage-probe sentence is rewritten into the absence rule. In
`skills/code-review/SKILL.md`, §*The record* lists the line and
§*Earlier rounds* tells a later round to re-run an `executed` line. The
`PROBE["warden.md"]` pin moves to the new text, and the changelog fragment is
written. Rule 4 binds the warden's preload, `agents/warden.md` plus
`skills/agent-contract/SKILL.md`, to 27,172 bytes or fewer, counted with
`wc -c` before and after. `agents/sealer.md`, `.github/workflows/` and the
orchestration files #943 changed are not touched.

## What this phase found

**The preload went from 27,173 to 27,168 bytes** (executed: `wc -c
agents/warden.md skills/agent-contract/SKILL.md`, at bc0e181b and at
bf6af66b). Step 7 gained 13 bytes for `` `evidence:`, ``. The probe sentence
lost 18, at 215 bytes where it stood at 233. A wording that added "never a
reading" cost 240 bytes and would have broken rule 4, so it was not used
(executed, a byte count of both drafts). `questions.md` Q3 is answered by
this count.

**The skill's absence bullet could not repeat the template's words.**
`tests/test_no_passage_is_pasted_into_a_second_file.py` refused the first
draft of the `evidence:` bullet in §*The record*. It shared 21 runs of 15
words with `templates/sdd-round.md`'s comment (executed). The bullet now says
the line takes the forms its row gives, says a claim of absence rests on a
search, and leaves the shapes to the table. `tests/test_docs_line_wrap.py`
refused one line of step 7 at 90 columns. The step was rewrapped at the same
byte count.

**A pin on the two lists reads the table, not a copy of it.**
`tests/test_chain_check.py::TestGrammar::test_the_warden_and_the_review_skill_name_every_line_a_finding_needs`
takes every row the table places in a finding as `one`, and asserts that
step 7 and the skill's list name each. At first it read all of §*The record*.
`mutation-check` then removed `evidence:` from the list, and the case stayed
green on the bullet below it (executed, exit 1). The case was narrowed to the
list alone in ee05f824, and the same mutation then went red (executed, exit
0).

**How each new pin was shown red.** The moved `PROBE["warden.md"]` pin, the
drift case and the skill sentence added to
`tests/test_review_axes.py::test_a_later_round_re_runs_an_executed_line` were
each run before their text existed, and each failed on the missing text
(executed). After the commit, `mutation-check` broke each unit once, and a
case went red every time (executed, exit 0 each):

- `evidence:` removed from step 7;
- `evidence:` removed from the skill's list, after the narrowing;
- the probe sentence's `evidence: executed` clause removed;
- the re-run sentence's verb changed to "read".

**The §19 sweep found no other statement of the rewritten sentences.**
`git grep` for "labelled apart" and "is not that run" outside `seal/` and
the changelogs finds nothing (executed). `agents/smith.md` keeps its own
coverage-probe sentence and its own `PROBE` entry. That is the smith's rule
and not a copy of the warden's.

**Narrow runs at the phase boundary** (executed): every module under
`tests/` that names `warden.md`, the review skill, `sdd-round`, the record
document or `changelog.md` ran, one module per command, 53 modules. 51
passed. The two that failed are the passage check and the line-wrap check
above, and both pass after the fix. `bin/rules --check` exits 0. The suite is
`unverified` here, and the orchestrator's broad run answers it.

**What phase 3 needs from this one.** The warden side runs at bf6af66b or
later. ee05f824 changed a test only, so the warden's preload and the files it
opens are the same at both. This branch's wardens run from the 0.22.1 cache,
which knows no `evidence:` line. Their spawn prompts must name the line and
point step 7 at the tree's `skills/code-review/scripts/chain_check.py`
(`plan.md` §*Operational impact*).
