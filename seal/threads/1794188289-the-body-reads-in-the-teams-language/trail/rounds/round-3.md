# Review round 3: 1794188289-the-body-reads-in-the-teams-language

```seal
target: e4b4d22f, fixes f2b29c48..e4b4d22f
```

This is the verifying round over round 2's fix pass. The fix diff
`f2b29c48..e4b4d22f` was read whole: `bbcf246a` (round 2's record),
`847ab81e` (the two README trees) and `e4b4d22f` (round 2's close block).
It changes three files: `seal/README.md`, `templates/setup/seal-README.md`
and `trail/rounds/round-2.md` (executed: `git diff --stat f2b29c48
e4b4d22f`). The work item's `routing.md`, the three frame files, `gaps.md`,
`changelog.md` and `pr.md` were read whole at `e4b4d22f`. None of the seven
changed in the range, and nothing in the fix diff contradicts a sentence of
theirs. The *Removes* row on the first part (`frame/design.md:249`) names
the `pr.md` lines of both trees as rewritten to "the first part is
`pr.<lang>.md` and then `pr.md` where the rows differ", which is what the
two lines now say. No `pr.<lang>.md` is owed: both language rows of
`seal/config.md` read `English` (`seal/config.md:9-10`). The phase records
name no coordinate in the fix diff.

Carried from round 2, not re-established: the coordinates of finding 1,
`seal/README.md:99-100` and `templates/setup/seal-README.md:99-100`, and
the list of modules that cover the README trees, which this round widened
by a search of `tests/` for the two paths. Re-established this round: the
order `pr_body.py#first_part` gives each case, read at
`skills/code-review/scripts/pr_body.py:472-480`, and every verdict below.

The quotes of `pr.md` were not compared again by script. `pr.md`,
`changelog.md`, `frame/plan.md` and `gaps.md` are byte for byte as they
stood at `f2b29c48`, where round 2's probe found all twelve quotes at
their sources (executed: `git diff --stat f2b29c48 e4b4d22f` names none of
the four).

No `seal/parity.md` is declared. The fix diff adds no test case, so no new
test is read against its group.

## Findings

None. The fix diff holds no defect this round found.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `seal/README.md:99-101` and `templates/setup/seal-README.md:99-101`
now read "the pull request body's first part, after pr.<lang>.md where the
two language rows differ; read by every round". That is the order
`pr_body.py#first_part` composes. Where the rows name one language,
`pr.md` comes first and any `pr.*.md` follows it (`pr_body.py:473-474`).
Where they differ, the one translated file comes first and `pr.md` after
it (`pr_body.py:475-480`). The line two below it, the `pr.<lang>.md` line
at `:102-103`, states the same condition, so the tree now gives one order
for each case (read). The two files are identical (executed: `cmp`), and
the narrow run over the modules that read either tree passed (executed:
`## Probes`).

The fix pass claimed that the other statements of the order condition it
on the rows. That holds at each coordinate it named, read this round:
`skills/code-review/orchestration.md:436-437` and `:455-457`,
`skills/commit-pr-convention/SKILL.md:267-268` and `:322-324`,
`templates/setup/config.md:179-182`, and the `pr_body.py` module docstring
at lines 2-3 and 37-40. The fix pass also claimed that the "where one
stands" lines list what is read and state no order. This round's own
search for presence wordings ("where one stands", "where present", "where
one is present", "where one was written", "if one stands") outside
`seal/threads` found six lines. Each lists a read or a rerun and states no
order: `agents/proofer.md:32` and `:123`, `agents/sealer.md:9` and `:83`,
and `skills/code-review/orchestration.md:115` and `:470` (executed:
`git grep`). A second search found lines naming `pr.<lang>.md` or `pr.*.md`
beside an order word, after dropping those that name the rows' condition.
It found no order conditioned on a file's presence. `orchestration.md:465`
says "as the rows ask for them". `tests/skills/test_chain_check.py:3486`
and `tests/skills/test_pr_body.py:1131` both stand in a docstring whose
sentence opens "Where the rows differ" or "Where the rows name different
languages" (executed: `git grep`; read). Both searches are a sample of
wordings, as the fix pass said of its own. The class is every statement of
the order across the tree, which is open.

No test pins the wording of the rewritten line (executed: `git grep` over
`tests` and `evals` for its words). None is owed:
`docs/running/what-a-script-gates.md:67` says a case pins a fact a reader
acts on, and one that pins wording goes. The suite holds the fact that the
two trees are one text.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite as a whole, the repository-wide lint and the typecheck: `unverified`, since contract rule 2 leaves the broad gate to the orchestrator | the `Broad gate` row of `seal/config.md` | the orchestrator, at `seal gate --record` once the rounds settle |
| Round 1's other three rows of `## Not judged`: the two `gaps.md` *Not verified* rows, and whether the settle owes `docs/layout/one-root-by-lifetime.ko.md` the added sentences. The fix diff touches none of their coordinates, so they stand as round 1 wrote them | `trail/rounds/round-1.md` *Not judged* | the repository owner and the settling session, as round 1 names them |

This round leaves no finding open. What comes due is the orchestrator's
broad run and then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.36.0 --root <worktree> --worktree`, before this record was written | exit 0. It printed no line at `frame/design.md`, so no test pin or copy notice stands. It printed the lines owing this round for round 2's finding 1 and for `847ab81e` past the last target, and the gate record and the guarantee not yet in git |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_no_document_names_the_old_roots.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/lib/test_optin.py tests/skills/test_seal.py tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_records_can_be_carried_out_and_in.py tests/behaviour/test_docs_line_wrap.py -q`, in a `git clone --no-local` at `e4b4d22f` under `<scratchpad>/1453-r3/clone` | exit 0, 854 passed |
| `cmp seal/README.md templates/setup/seal-README.md` at `e4b4d22f` | exit 0, identical |
