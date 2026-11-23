# Phase 2: 1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite

## What this phase found

**The frame holds against the tree at `5d0a4758d` for *Scope* item 5.**
Phase 1 changed no line of `HEX_REF`, `sealed_names`, `ref_is_commit`,
`SHORTEST_SHA` or `_same_commit` (executed, `git diff ee8a72583 HEAD --
skills/verify/scripts/seal_stamp.py`, whose hunks end in `build`). Each of
those lines stood one line below the coordinate `frame/design.md` G11 gives
at `ee8a72583`, because phase 1 added a line to the module docstring (read).

**The comment above `HEX_REF` went with it, where *Scope* item 5 says it
cites the rule.** That comment said what `HEX_REF` matched, and once
`HEX_REF` goes no statement stands under it. Judged against
`skills/core/SKILL.md` *The rule a mechanism is kept against*, whose rule
is that a change removes what stood on the old fact in the same commit. The
rule's other citations are where the item puts them: `sealed_names`'
docstring and `ref_is_commit`'s docstring name `_same_commit`, and the
comment above `SHORTEST_SHA` names `_same_commit` as its reader.

**The hex check and the ceiling of forty stand in one pattern built from
`SHORTEST_SHA`.** `SHA_SPELLING`, beside `SHORTEST_SHA`, fully matches a
lower-case hex spelling of `SHORTEST_SHA` to forty characters. `_same_commit`
lower-cases both spellings, holds each to that pattern, and keeps its one
prefix comparison. So the floor of seven is written once, and the pattern's
source holds no `{4,40}`. `ref_is_commit` answers True for `None` and `""`
and otherwise returns `_same_commit(str(ref), str(base))`. The `str` keeps
the old reading of a `base` of `None`, which matched no ref then and matches
none now.

**The S3 case was seen red against `ee8a72583`'s rules at the pair `bbb2`
and `bbb2222`.** `Test_ref_is_commit.test_answers_as_a_refusal_record_is_matched`
was written first and run with the code unchanged (executed, `bin/test -q
-p no:xdist`). The `bbb2` row failed on `assert stamp.ref_is_commit(ref,
commit) is same`, where `ref_is_commit('bbb2', 'bbb2222')` returned True.
The rows `bbb222`, `cafe`, `BBB2222` and `zzzzzzz` failed as well. The two
existing cases failed at their moved values, `bbb2` refused and `BBB2222`
accepted. The case asserts each rule's answer against the expected value,
so two rules that agree on a wrong answer still fail it.

**The case gained a row for a 41-character spelling after the code was
written, because no case held the ceiling.** That row's ref is
`bbb2222` with 34 zeros. Under `ee8a72583`'s rules the two answers differed
there, because `HEX_REF` stopped at forty and `_same_commit` had no ceiling
(read). The row was committed at `3bc7d5968` and shown red by the mutant
that drops the ceiling, on that row alone (executed, below).

**Each unit that adds behaviour was mutated after its commit, and every
mutant was red.** The call was one `seal mutate` over
`skills/verify/scripts/seal_stamp.py` with six pairs, run under
`bin/test tests/skills/test_seal_stamp.py -q -k Test_ref_is_commit -p no:xdist`
(executed: `6 mutants, 6 red, 0 SURVIVED`). `git status --short` printed
nothing after it.

- `SHORTEST_SHA = 7` made 4: red, the floor.
- `SHA_SPELLING`'s `,40` dropped: red, on the 41-character row alone, read
  from a second run of that mutant with `-rf`.
- The hex check made the old length check: red, the `zzzzzzz` row.
- The two `.lower()` calls dropped: red, the `BBB2222` rows.
- `ref is None or ref == ""` made `ref is None`: red, the `""` row.
- `ref_is_commit`'s return made `str(base).startswith(str(ref))`: red.

**`seal layout --pairs` names no pair this phase made** (executed, exit 0;
its lines for `tests/skills/test_seal_stamp.py` are the four phase 1
reviewed, in `Test_read_sprite` and `Test_main`).

**The phase boundary set passed in one command** (executed, `bin/test -q`
over `tests/skills/test_seal_stamp.py`, `tests/skills/test_broad_gate.py`,
`tests/github/test_release_seal.py`, `tests/lib/test_optin.py`,
`tests/skills/test_agentic_pytest_record.py`, `tests/skills/test_seal.py`,
`tests/text` and `tests/behaviour`, at `3bc7d5968`: exit 0, 2022 passed, 10
skipped). The four files beyond the two modules load `seal_stamp.py` or
`broad_gate.py`, which loads it. The two tree-wide failures phase 1 named
pass here, after its closing commit wrote `gaps.md` and `5d0a4758d` folded
the citation in `frame/plan.md` *Operational impact*.

**The plan row's searches print what it asks at `3bc7d5968`** (executed).
`git grep -n -E 'startswith\((base|ref|one|other)\)' -- skills/verify/scripts/seal_stamp.py`
prints one line, `:1152`, in `_same_commit`.
`git grep -n -F '{4,40}' -- skills/verify/scripts/seal_stamp.py` prints
nothing and exits 1.

**The other places that state the rule were searched, and the list is a
sample.** The method was `git grep -n -i` for the rule's words, `prefix of
the other`, `ref is the commit`, `spelled in hex`, `four characters`,
`seven characters`, `a bare SHA`, `resolves to itself`, `HEX_REF` and
`SHORTEST_SHA`, over `docs`, `skills`, `agents`, `templates`, `hooks`,
`lib`, `evals`, `.github`, both READMEs, `CONTRIBUTING.md` and `tests`.
`docs/checks/the-stamp.md:75-77` states the refusal record's rule as a
prefix match of at least seven characters. It still holds for every
spelling that reaches it, because a record's target and the SHA it is
matched with are `lib/fields.py`'s `COMMIT`, lower-case hex of 7 to 40
characters, as `frame/design.md` G12 and G13 read it. The hits in
`docs/checks/the-pull-request-check.md` are `chain_check.py`'s rule, which
*Scope*, *Out* leaves. `broad_gate.py#resolve_base`'s docstring says a bare
SHA resolves to itself, which holds. The search did not reach prose that
states the rule in other words.
