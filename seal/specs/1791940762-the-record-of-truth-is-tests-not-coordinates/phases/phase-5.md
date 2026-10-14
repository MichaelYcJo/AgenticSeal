# 1791940762-the-record-of-truth-is-tests-not-coordinates — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 33fc9835 |
| Ran by | smith on Opus 5.5, as the attribution line in the spawn prompt names it |

## What this phase was asked

The last phase, under Q1's answer that the plugin stops shipping the ledger:
the product surface (`plugin.json`'s description and its `evidence-ledger`
and `drift-detection` keywords, both READMEs together with the ledger section
and the demo GIF, `skills/evidence-check/SKILL.md`, `skills/evidence-ci/`,
`templates/ledger.md`, `templates/evidence-check.yml`, any wrapper left
behind); phase 4's leftovers (the docstrings of `rider_check.py#reverify` and
`#migrate`, `chain_check.py#fix_range`, `pact_check.py#shown` and
`config.py#pact_declaration`, with their census entries, and
`round_record.py#RECORD_COMMENT_NEVER_CLOSED`, which named `evidence-check`);
the owner's principle written into `CLAUDE.md` §*The rule a mechanism is kept
against* in place, *a fact has one source*, under the `preload:claude-md`
ceiling; the ledger and `evidence-check` wording of the other prose files
(framer, scribe, legacy-parity, the parity and SDD templates, the round-record
spec, the design record, the pact docs) toward S9's zero; the changelog
fragment with the deletion table, `overview.md` closed and the answered
questions ticked. Q2 stays at its default. Narrow verification with census
and registry after every commit, `budget_check.py` on the tree and against
the base, `fold-check`, `enforced-unresolved` at 0, no ledger rows.

## What this phase found

**The frame holds, except S9's grep, which cannot reach zero as written.** It
greps for `evidence-check` and `survivor`. `plan.md` alternative G keeps the
kernel at `skills/evidence-check/scripts/`, so nine lines that name that path
match, and fifteen lines in `arm_check.py`, `round_record.py` and
`skills/verify/SKILL.md` say *survivor* for a mutation no case killed.
Executed at the phase's tip: 24 hits, 9 of them the kernel's path and 15 the
mutation word, and none of anything else. `overview.md` carries the row.

**What left, by commit.**

| Commit | What |
|---|---|
| 72b936d8 | the manifest's description and two keywords, `marketplace.json`'s two descriptions, both READMEs (headline, the records section, the skills count from 24 to 22, two cheat-sheet rows, the first-run and import passages, the limits bullet, the contributor line), `SECURITY.md`'s checker paragraph, the two skills, the two templates and `assets/demo.gif`; one case (`test_ci_wiring_never_asks_for_the_plugin_path`) whose whole subject left, the rider list's template entry, seven passage-baseline pairs, two section pins and three `unenforced` rows |
| f6c0f749 | the never-closed-comment refusal names `unverified-check`; the docstrings of the five census units and of the kernel's other readers stop describing the ledger as live |
| 99121307 | the tenet, rewritten in place; the whose-rule section's history paragraph shortened to its pointer |
| 33fc9835 | framer, scribe, legacy-parity and parity-setup; the parity, plan, spec, pact and config templates; the pact orchestration, the round-record spec, the reader registry, `agent-contract` §11, `commit-pr-convention`, `config`, `gap-analysis`, the pull request template; `docs/one-root-by-lifetime.md` and its Korean edition; `seal/follow-up.md` |

**The census refuses a re-hash, so the five units declare instead.** A unit on
`tests/undeclared_readers.txt` whose hash moves is the finding *declare it and
remove its census line*. `rider_check.py#reverify` and `#migrate` read
`guess` (rider comments, refused when unanchored), `chain_check.py#fix_range`
`guess`, mixed (a malformed range refused, unresolvable ends a notice),
`pact_check.py#shown` `owned` (it splits path strings, and `re.split` is a
K1 call, so `nothing` was refused, executed), and `unverified_check.py#annotate`
`observed` (`GITHUB_ACTIONS`). `config.py#pact_declaration` already declared.

**The printed message is pinned and was seen red.**
`test_a_flag_carrying_an_open_comment_writes_no_record` now asserts the
refusal names `` `unverified-check` ``. `mutation-check` putting
`` `evidence-check` `` back in `round_record.py` turned it red (executed,
exit 1 in 1.6 s, the file restored by hash).

**`CLAUDE.md` is 9,027 bytes.** The tenet gained 89 bytes and the whose-rule
section lost 188, the account of how `seal` came to need the rule, which the
check's own module keeps in a comment. `preload:claude-md` is lowered from
9,126 to 9,027.

**The design record says it is not rewritten, and it is rewritten here.**
`docs/one-root-by-lifetime.md` keeps its 2026-09-02 text as a record and
appends dated decisions. Its ledger statements were rewritten in place in
both editions under the owner's rule of 2026-10-13 that a document states the
latest: the tree, the lifetime table, the fold step of *What happens at a
release* (step 2 became step 1, and the decision row that cited step 2
follows), the guard (it now names `overview.md`'s `## Not verified` rows,
which `settle` reads, where it named `evidence-todo.md`), and two decision
rows: settle's grouping by ledger coordinates and the anchored-rows guard,
both removed from the code in phases 2 and 3. One rule paragraph and two
history lines left the English edition, one and one the Korean, and their
`unenforced` and `docs-history` rows are lowered to what is measured.

**`templates/config.md` linked a section phase 4 removed.** Its *Pact notify*
paragraph named `evidence-check --reverify` as a pact change's writer and
cited `docs/the-pact.md` §*A signer records a pact change*. It now says no
command writes a record and how `pact-check` reads one a signer holds, which
is Q2's default.

**Phase 4 left one module red.**
`tests/test_a_shrunken_corpus_declines_to_judge.py` still accounted for
`test_the_root_migrates_itself.py#test_the_re_pointed_ledgers_are_staged_with_the_move`,
which phase 4 deleted, and three of its cases failed (executed). The entry
is removed and the module is green.

**`preload:scribe` went over by 52 bytes** after the scribe and
legacy-parity rewrites, and is back under by shortening the new
legacy-parity paragraph; no ceiling was raised.

**Verification, executed at the phase's tip unless named.** The modules that
read the changed files, 81 of them (all but the ten round-record modules
whose pins the changed text does not reach, by `git grep` over `tests/`),
with the census, rider and shrunken-corpus modules: 6,056 passed, 12 skipped.
The 18 product-surface modules before 72b936d8: 757 passed, 7 skipped and
one red, a README line naming an old root; after the fix the three modules
it touched, 149 passed. The census module after each
commit. `budget_check.py` exit 0 on the tree and against
`origin/release/v0.22.0`; `fold-check` exit 0 (158 statements, 18
documents); `unverified-check --baseline origin/release/v0.22.0` exit 0;
`chain-check --baseline` exit 0, with the notice that no round record exists
yet; `settle` exit 0. `uvx ruff check` and `ruff format --check` on every
Python file changed. The full suite is the sealer's.
