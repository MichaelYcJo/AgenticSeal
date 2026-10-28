# Phase 1: 1793188383-rule-5-judges-tokens-per-tool-call

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | c6e47cfe |

## What this phase was asked

Build phase 1 of `frame/plan.md` against the frame at `cf8127eb`, under the
owner's automation answer, with `frame/questions.md` Q1, Q2 and Q3 on their
defaults: `TOKEN_MARGIN = 0.07`, rule 5 alone, and the margin sized from the
6.8-point figure. Before the first edit, extract each of the 17 records of
`frame/design.md` *Data & interfaces* with `git show` into a directory
outside the tree, run `noninferiority.py check` on each at the base, and keep
each verdict and rule 5 line here. Then write the cases of *Data &
interfaces*, each seen red as its scenario row says. Then add
`TOKEN_MARGIN`, rewrite rule 5 of `#verdict` with the new reason line, and
rewrite in place the module, `#tool_calls`, `#verdict` and `#cost_rows`
docstrings and `evals/README.md` item 5 and the sentence after the list. No
paid run is made.

## What this phase found

**The frame holds against the tree (read, at `cf8127eb`).** Every coordinate
of `frame/plan.md` *Technical context* resolves to the text it names:
`FALSE_MARGIN` at `noninferiority.py:102`, rule 5's cross-multiplied
comparison at `:888` to `:899`, the four docstrings, `evals/README.md` item 5
at `:47` to `:50` and the sentence after it at `:52` to `:53`, and the four
rule 5 entries of `VERDICTS` at `:1537` to `:1552`. The plan's grep printed
the five lines it predicts at the base (executed).

**The defaults this phase built on.** Q1: `TOKEN_MARGIN = 0.07`. Q3: the
margin is sized from the 6.8-point spread of tokens per tool call and applied
to both figures, and the comment above the constant names that source. Q2
does not touch phase 1; `gaps.md` *Not done* carries it.

**The 17 records at the base (executed).** Each record was written with
`git show <commit>:<path>` to a scratch directory outside the tree, and
`python3 evals/scripts/noninferiority.py check <record>` ran on each with
the code of `cf8127eb`, its exit code read directly. The rule 5 verdicts
agree with the frame's *Rule 5 today* column on all 17 records.

| Name | Recorded verdict | Exit | Verdict at the base | Rules failing at the base |
|---|---|---|---|---|
| 957-framer-p3 | fail | 1 | fail | 5 |
| 957-sealer-p3 | fail | 1 | fail | 3, 5 |
| 957-smith-p3 | pass | 0 | pass | none |
| 957-warden-p2-run-1 | fail | 1 | fail | 3 |
| 957-warden-p2 | fail | 1 | pass | none; `check` prints "it says `fail` and its numbers give `pass`" |
| 957-warden-p3 | pass | 0 | pass | none |
| 967-framer-p4 | fail | 1 | fail | 5 |
| 967-smith-p4 | pass | 0 | pass | none |
| 967-warden-p4 | fail | 1 | fail | 5 |
| 969-sealer-p4 | pass | 0 | pass | none |
| 969-sealer-model | fail | 1 | fail | 3, 4, 5 |
| 975-sealer-p4 | pass | 0 | pass | none |
| 976-sealer-p5 | pass | 0 | pass | none |
| 943-sealer-p3 | fail | 1 | fail | 4 |
| 943-sealer-p3b | fail | 1 | fail | 5 |
| 968-framer-p2 | pass | 0 | pass | none |
| 985-warden-p3 | fail | 1 | fail | 1, 2 |

The rule 5 line `check` printed at the base, for each of the six records
rule 5 failed:

- 957-framer-p3: `the new side read 33595.1 tokens across every model per tool call (4736908 over 141), not below the baseline's 28253.1 (3164345 over 112) (rule 5)`
- 957-sealer-p3: `the new side read 36861.5 tokens across every model per tool call (3096365 over 84), not below the baseline's 34268.9 (3324087 over 97) (rule 5)`
- 967-framer-p4: `the new side read 29894.6 tokens across every model per tool call (3258508 over 109), not below the baseline's 27296.7 (3275602 over 120) (rule 5)`
- 967-warden-p4: `the new side read 87862.4 tokens across every model per tool call (82590654 over 940), not below the baseline's 87197.6 (81616964 over 936) (rule 5)`
- 969-sealer-model: `the new side read 34719.4 tokens across every model per tool call (1909566 over 55), not below the baseline's 33386.8 (2303686 over 69) (rule 5)`
- 943-sealer-p3b: `the new side read 35906.3 tokens across every model per tool call (2585256 over 72), not below the baseline's 35600.6 (2883649 over 81) (rule 5)`

`957-warden-p2` was recorded as `fail` on rule 3 before #966 changed rule 3,
and the base code gives it `pass`. This is the case the frame's base column
exists for.

**`check`'s exit code does not carry the verdict for such a record.** A
record whose recorded verdict differs from its computed one exits 1 whatever
the computed verdict is, as `957-warden-p2` does above. `frame/plan.md`'s
phase 2 *Verified by* cell expects "0 for `pass` and 1 for `fail`". That
holds only where the recorded and the computed verdicts agree. Phase 2 reads
the computed verdict from the line `check` prints, and reads the exit code
beside it.

**How each case was seen red (executed, `bin/test
tests/evals/test_noninferiority.py -q -p no:xdist -k "Test_verdict or
Test_check_record"`).**

1. With the cases written and the code at the base, the module refused to
   collect, exit 2: `AttributeError: module 'noninferiority_under_test' has
   no attribute 'TOKEN_MARGIN'`, raised by S5's entry.
2. With only `TOKEN_MARGIN = 0.07` added and rule 5 still the base's, exit 1
   with five cases red on their own assertions: S1 "fewer calls and a
   smaller total, though each call read more", S4 "the total and tokens per
   tool call both within the margin", S5 "both figures exactly at the
   margin", S6 "tokens per tool call equal to the baseline's", and S3's
   `test_refuses_with_a_line_for_each_other_rule`. S7 and S8 passed at the
   base, as the frame predicts.
3. With rule 5 rewritten, the whole module passed, 253 cases, exit 0.
4. S7 and S8 were seen red with rule 5's comparison removed. After commit
   `c6e47cfe`, `seal mutate` replaced the comparison with `if False:`, and
   `-rA` showed both cases red: `test_refuses_a_side_a_rule_fails_or_numbers_that_give_no_result[rule
   5: both figures past the margin]` and
   `Test_check_record::test_refuses_an_edited_cell_the_verdict_does_not_follow`.
   `agents/crafter.md` orders the commit before the mutation, so this red
   was shown after the cases were committed and not before.

**Each unit added has a case behind it (executed, `seal mutate` over
`evals/scripts/noninferiority.py` at `c6e47cfe`).** The batch of five
mutants over `Test_verdict` and `Test_check_record` ended with "5 mutants, 5
red, 0 SURVIVED", exit 0. Each mutant was then run on its scenario's case
alone, exit 0 and red each time:

| Mutant | Case it turned red |
|---|---|
| the whole comparison replaced by `if False:` | S7, S8 |
| the total's half of the comparison removed | S1 |
| the per-call half of the comparison removed | S2, S6 |
| `+ 1e-9` in the margin's bar turned to `- 1e-9` | S5 |
| `TOKEN_MARGIN = 0.07` turned to 0.12 | S3 |

`git status` was clean after each run.

**A choice made while writing the comparison.** The comparison is written as
`new_t > old_t * bar and new_t * old_c > old_t * new_c * bar`, with `bar = 1
+ TOKEN_MARGIN + 1e-9`. It stays cross-multiplied, as the base's was. The
no-result check above it refuses a side whose calls are none and does not
refuse a baseline of zero tokens, and a ratio would divide by that zero.
The `1e-9` scales with the baseline, so a figure exactly at the margin
passes at any token count. The reason line formats the margin with `:.0%`,
so a change of Q1's answer changes the line with it.

**The old rule's sentences are gone (executed).** `git grep -n -i -e "tool
call below" -e "total tokens, tokens per true find" -e "tool call are
fewer" -- evals tests` printed nothing at `c6e47cfe`, exit 1. At the base
it printed these five lines:

```
evals/README.md:48:   tool call are fewer than the baseline's. The rewrite controls the context
evals/README.md:52:Total tokens, tokens per true find, spend and wall seconds are written in
evals/scripts/noninferiority.py:52:tool call below the baseline's. Total tokens, tokens per true find, spend and wall seconds are
evals/scripts/noninferiority.py:775:    across every model per tool call below the baseline's (`tool_calls` says
evals/scripts/noninferiority.py:780:    total tokens, tokens per true find, spend and wall seconds are never
```

**Sentences read and left standing (read).** Three more sentences in the
test module name rule 5 or the per-call figure, and each stays true under
the new rule. The `#test_refuses_a_short_model_usage_as_no_figure`
docstring says a count read as zero makes a run look cheaper and rule 5
then passes it, and a smaller total still passes. The `numbers()`
docstring describes a new side with a tenth fewer tokens over as many
calls. The `written()` docstring calls the new side cheaper per call. A
`git grep -i "rule 5"` outside `seal/`, `changelog/` and `CHANGELOG.md`
finds no other statement of the rule. `.test_durations` names the three
renamed case identifiers, and the frame leaves that file to CI.

**The group check (executed).** `bin/seal layout --pairs` exited 0 and named
no pair in `tests/evals/test_noninferiority.py`. The two new `VERDICTS`
entries sit in the group the other rule 5 entries are in.
