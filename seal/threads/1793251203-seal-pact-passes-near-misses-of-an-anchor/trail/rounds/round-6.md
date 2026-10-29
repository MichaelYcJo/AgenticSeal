# Review round 6: 1793251203-seal-pact-passes-near-misses-of-an-anchor

target: a2e1f67e9, fixes c472a1dc7..a2e1f67e9

## Findings

None. The three closes of round 5 hold. The changelog sentence `a2e1f67e9`
rewrote states what the skill now says. The fix diff changes no Python file,
so no code phase 1 to 4 built is reviewed again here.

## Confirmations

confirms: round-5#1
`skills/code-review/SKILL.md:35-43` at `a2e1f67e9` holds round 5's
paste-ready text word for word; the diff of `12fb615c` was compared line by
line. The qualifier "of a pact that row declares" is gone. "Whatever remote
its `Pact` cell names" now covers the row S11 and probe P5 describe, a remote
one letter off under `| Pact | Clause | Hashes |`. So *Scope* item 7 and
#1132's third *Done when* bullet, as `frame/design.md:150-159` and
`:175-179` state them, are now what the text asks. The fix pass claimed that
no other live text holds the qualifier. A `git grep` for its words at
`a2e1f67e9` finds it in this work item's records and in one refusal sentence,
`skills/verify/scripts/pact_check.py:239` with its copy at
`tests/skills/test_pact_check.py:88`. There "that row" is the signer's `Pact`
row in the `UNDECLARED` sentence, not the removed qualifier. The fix pass
also claimed the skill's readers pass. This round ran them again, every
module `git grep -l "code-review/SKILL.md" tests/` lists among them: 861
passed, exit 0. In the last example, "a pact that row declares" stands
nearest to "a row outside the anchor table". The operative sentence says
"whatever remote", so either reading reaches the same finding, and that
example reads badly at most. Executed and read.

confirms: round-5#2
`gaps.md:34-37` now cites "`CLAUDE.md`, its section on where judgment is
spent, which spends it where meaning is the question". The source the
orchestrator names is `CLAUDE.md` on `origin/release/v0.24.2`, now
`4a2cf8790`. There the sentence "Judgment is spent where meaning is the
question" stands at `CLAUDE.md:15`, under *The first value: efficient
development through the workflow*. At `10942072d`, the revision round 5
read, it stands at `CLAUDE.md:54` under *The rules steer judgment, and a few
invariants hold the chain*. At `a2e1f67e9` the search prints nothing, exit
1, because the branch base `8d8d63903` predates #1168. That base is an
ancestor of `4a2cf8790`, so the section reaches the tree this memo merges
into. Round 5's finding was true at `10942072d`. #1169 has since added the
very heading the memo first cited. A citation by subject resolves across
both wordings, which is why the fix pass's choice over the record's italic
heading holds. Executed.

confirms: round-5#3
`gaps.md:19` is the record's second form, with "the line predates this
work" added to its grounds. Each part was checked. The S10 search at
`a2e1f67e9` prints `skills/verify/scripts/unverified_check.py:413`, exit 0.
`git blame` gives that line to `56ade5c8c`, an ancestor of the base
`8d8d63903` (exit 0), so "predates this work" holds. The bold heading the
row cites stands at `trail/phases/phase-3.md:20`. `seal unverified` over
`gaps.md` exited 0. `frame/design.md:216` is unchanged, as the orchestrator
directed, and the row records the divergence where the sealer reads it.
Executed and read.

confirms: none
`changelog.md:7`, the sentence `a2e1f67e9` rewrote, matches
`skills/code-review/SKILL.md:35-43`. "A signer's work item" is the text's
`Pact` row condition. "Whatever remote it names" is the operative clause.
The three shapes are the text's examples, and the remote one letter off under
`| Pact | Clause | Hashes |` is its fourth. "No script refuses it" holds,
since the fix diff leaves `pact_check.py` unchanged. One clause parses two
ways on a first read: "a line written as an anchor that `seal pact` does not
read as a finding" can join "does not read" to "as a finding". The clause
after the colon settles it, and a person reads these notes. By *The record*
in `skills/code-review/SKILL.md`, a sentence that only reads badly is no
finding. A rewording that removes the second parse puts "as a finding"
straight after "raise": "to raise as a finding a line written as an anchor
that `seal pact` does not read, whatever remote it names". Read.

confirms: none
`trail/phases/phase-4.md:28-35` stands as history. The record names its
commit, `6303f97f`, in its field table, and its quote is what that commit
built. `CLAUDE.md` *The rule a mechanism is kept against* sends history to
the work record. Round 5 finding 1 and its `fixed 12fb615c` line link the
change. The phase's present-tense claims still hold for the new text. The
text stands under *Two stages, in order*, after the paragraph on `gaps.md`
and before *Review beyond the changed files*. It is three sentences, so
`gaps.md`'s row on the proofer's text stays true. Its examples name only
shapes outside what the docstring states as read, and the fourth combines
the first three. Contract rule 19 reaches a sentence stating the old fact as
current, and this quote states what one commit built. Read.

confirms: none
The handoff's label is honest. `gaps.md` *Not verified* names the full
suite, the repository-wide ruff runs and the typecheck, with the
orchestrator answering through `seal gate`. This round ran none of the
three (contract rule 2). The fix diff adds no test, so no new case is read
against its group. Executed and read.

Carried, not re-established: round 5's probes P1 to P8, its red-first run
against `a5533a3d` and its `{1,4}` mutant. The fix diff changes no Python
file (`git diff --stat c472a1dc7..a2e1f67e9 -- '*.py'` printed nothing), so
the code those probes read is the code at `a2e1f67e9`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck, which stay `unverified`; this round ran none of them (contract rule 2) | the branch at `a2e1f67e9` | the orchestrator, by the broad gate |
| Phase 3's seven `seal mutate` mutants and the phase boundary counts; carried from round 5, not re-run | `trail/phases/phase-3.md`, `trail/phases/phase-4.md` | the sealer, by its sample |
| Whether the issue `gaps.md` *Not done* and the design's *Out* row assign for the walker's over-refusal exists; carried from rounds 3 to 5 | `hooks/lib/config.py#gfm_table` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_review_axes.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py tests/text/test_every_agent_reads_the_contract.py tests/skills/test_chain_check.py tests/evals/test_noninferiority.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/test_censuses.py tests/behaviour/test_unverified_rows_close.py -q` in a `git clone --no-local` at `a2e1f67e9`, unmodified | 861 passed, exit 0 |
| `git grep -n -i "pact that row declares\|anchor of a pact\|written as an anchor\|written as a pact anchor" a2e1f67e9 -- .` | hits only in this work item's records, `skills/code-review/SKILL.md:38` and `:43`, and the `UNDECLARED` sentence at `skills/verify/scripts/pact_check.py:239` and `tests/skills/test_pact_check.py:88` |
| `git grep -n "Judgment is spent where meaning is the question" <rev> -- CLAUDE.md` for `4a2cf8790`, `10942072d` and `a2e1f67e9` | `CLAUDE.md:15`, `CLAUDE.md:54`, and nothing with exit 1 |
| `git merge-base --is-ancestor 8d8d63903 4a2cf8790` | exit 0 |
| `git grep -n -i "no anchor table holds\|misses twice\|four columns" a2e1f67e9 -- skills/verify/scripts/ tests/skills/` | `skills/verify/scripts/unverified_check.py:413`, exit 0 |
| `git blame -L 413,413` on that file, then `git merge-base --is-ancestor 56ade5c8c 8d8d63903` | `56ade5c8c`, 2026-10-08; exit 0 |
| `bin/seal unverified seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/gaps.md` | exit 0 |
| `bin/seal rules --check` | exit 0, 17 excused in 268 check lines of 55 rule files |
| `git diff --stat c472a1dc7..a2e1f67e9 -- '*.py'` | nothing printed |

The clone was removed before hand-back, and no probe file was written.
