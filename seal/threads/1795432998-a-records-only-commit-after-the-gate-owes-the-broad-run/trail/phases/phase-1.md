# Phase 1: 1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run

## What this phase found

**The frame holds against the tree at `e36796bb8`.** `chain_check.py#broad_gate`
calls `follows(root, sha, base, item)` with no `only`, and `#guarantee`
calls it with `only=CLOSING_RECORDS`, as `frame/design.md` G3 says (read).
`agents/sealer.md` step 1 goes on where the newest run is "At HEAD, or
followed only by paths under `seal/threads/<item>/`", as G5 says (read).
The paragraph on a conflict with the base stands in
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals*, where *Scope* item 3 places the new paragraph after
it (read). No file this phase changes had changed between `e5bdbff55`, the
commit the framer read, and `e36796bb8`, which adds the frame alone.

**The case was seen red twice, each time at the assertion it names, with
`chain_check.py` as `e36796bb8` holds it and the case as `3e1d1ec77`
commits it (executed).** Both runs were
`bin/seal mutate skills/code-review/scripts/chain_check.py --replace <old> <new> --tests "bin/test tests/skills/test_chain_check.py -q -k test_lets_the_records_follow_the_run -p no:xdist"`.

- With `broad_gate` calling `follows(root, sha, base, item, only=CLOSING_RECORDS)`:
  `red`, failing at `assert chain.broad_gate(str(root), ITEM, "main") == []`,
  the first assertion, on the refusal of the commit that touches
  `seal/threads/1791999999-a-work-item/changelog.md`.
- With `follows` reading `if False or (` in place of
  `if not path.startswith(f"{item}/") or (`, so that every path reads as
  inside the work item: `red`, failing at the last assertion, where the
  arm returned `[]` and the case expects the refusal naming `f.txt`.

`seal mutate` restored the file from its own copy each time. `git status`
afterwards listed only the uncommitted case. The case was green against the
tree as it stands, as `frame/design.md` G4 predicts, because the arm
already holds the rule. So the case takes its red from contract rule 15, by
removing the one guard each assertion names.

**No unit adds behaviour, so no `seal mutate` run is owed beyond the two
reds above.** The phase changes no code. `chain_check.py` keeps its bytes,
as `frame/design.md` *Data & interfaces* says (judged against
`skills/verify/SKILL.md` *The narrow command still has to be able to
fail*, the *Prose only* row, for the six text files).

**The case asserts the guarantee arm's refusal whole, naming
`changelog.md`.** One commit adds `pr.md` and `changelog.md`, and
`follows` refuses the first path that `touched` lists.
`chain_check.py#touched` reads `git diff-tree --name-only`, which lists
paths in git's sorted order, so `changelog.md` comes first. G4 reports the
same path. The case builds each expected sentence from
`chain.follows_reason` and copies no refusal string, as *Scope* item 8 asks.
It defines no `section`, `read` or `flat` helper, because #1580 rewrites
those (judged against `frame/plan.md` *Overlap with the release*).

**Departure: README.md does not use *Scope* item 6's words.** Item 6 says
the gate runs "at the commit the pull request will carry, or at one only
the work item's records follow". Those words hold the pattern
`the commit the pull request will carry`, so G15's command would still
print `README.md:286`, and the scenario *No sentence states the strict
rule* could not hold. README.md now says the gate runs "at the pull
request's head commit or at one that only the work item's records follow".
The meaning is item 6's (judged against `frame/design.md` *User scenarios
& acceptance*, the scenario *No sentence states the strict rule*).

**Departure: `README.ko.md` gains the same exemption, which the frame did
not name.** `README.ko.md:288` is the Korean edition of `README.md:286`,
and said that the session runs the broad gate once "pull request 가 담을
커밋에서". G14's search ran on English wordings and could not reach it. It
now reads "pull request 가 담을 커밋에서, 또는 뒤에 작업 항목의 기록만
이어지는 커밋에서" (judged against contract rule 19 and
`skills/core/SKILL.md` *The rule a mechanism is kept against*: a change
rewrites the text it amends in place, and every other statement of the
old fact with it). The first phase boundary run, at `b566ca252`, failed
`tests/behaviour/test_docs_line_wrap.py::test_prose_stays_within_the_wrap_limit[README.ko.md]`
on `README.ko.md:289`, 118 columns against a limit of 88, because the edit
had joined two lines (executed). The paragraph is rewrapped, and its words
are unchanged.

**The new paragraph says that both mechanisms read the rule over the
branch's own commits, so neither reads a merge.** `follows` lists commits
with `--no-merges` and leaves out the base's own commits with `^<base>`
(`chain_check.py#follows`, read). So a clean merge from the base after the
gate passes the arm. The paragraph on a conflict with the base still makes
the orchestrator run the gate again after any merge. Without that clause,
"read the same rule" would say that the arm refuses a merge, which it does
not. The clause names the paragraph above it as the rule for a merge, and
adds no exemption for one (judged against `frame/design.md` *Scope*, *Out*:
*A merge from the base after the gate*, which #1583 asks for).

**`gate-to-pull-request.md` cites the new paragraph and does not restate
it.** The clause "the record commits after the run leave it standing" now
reads "Whether the broad run is owed again for that commit is
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals*'s." The repair steps around it stay (judged against
`frame/design.md` *Scope* item 4 and `skills/core/SKILL.md` *The rule a
mechanism is kept against*: a fact has one source, and every other place
links to it).

**G15's command prints nothing at `3e1d1ec77` (executed).** It is
`git grep -n -F -e 'without the broad run at HEAD' -e 'withholds without' -e 'leave it standing' -e 'the commit the pull request will carry' -e 'No seal without the broad run at HEAD' -- ':!seal/threads'`.
Before the build the same command printed the four lines G15 names, so
the pattern finds lines that are there (executed at `e36796bb8`).

**The other statements of the rule were searched, and the search is a
sample.** It was `git grep -n -i -E` for `broad run at HEAD`,
`` gate\.md` at HEAD ``, `gate again`, `followed only by`, `touches only`,
`records alone`, `broad run is not at HEAD` and `run leave`, and then for
`(broad|gate).{0,60}HEAD` over every tracked `.md` file, outside
`seal/threads/`. It printed these, and each is left as it stands:

- `docs/releasing/branch-and-release.md:280`, which the settle rewrites
  through `frame/design.md` *Rule changes*;
- the verdict reason `no broad run at HEAD` at `agents/sealer.md:64` and
  `skills/code-review/gate-to-pull-request.md:94`, which `frame/design.md`
  G14 keeps;
- `chain_check.py`'s module docstring, its *broad gate* and *guarantee* rows,
  which already state the two sets;
- `evals/behaviour/sealer/rule-sealer-stale-gate/graders/truth-stale-gate.md:7`,
  which a code commit after the run makes true.

The search does not reach a paraphrase in other words, in English or in
Korean.
