# Guarantee: 1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite

Audited at `cd55daf7bfe7cefc150f74aa10f411d42132b2a4` against the base
`release/v0.38.6`, resolved as `seal gate` resolves it: `release/v0.38.6@{upstream}`
answers `f2a664eb85677c4a4656c76d2e01b7091b1609fe` (executed, `git rev-parse
--verify --quiet`). The re-runs below ran in a `git clone --no-local` of the
worktree at that HEAD, `<scratchpad>/1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite/at-base/repo`,
with the changed code restored from the base where a claim says `seen red`.
The tree under audit was not changed.

**The broad run is at HEAD** (executed). `trail/gate.md`'s last `seal` block
reads `run: 433ac25cf against f2a664eb8`. `433ac25cf` resolves and is an
ancestor of HEAD, and `git log --no-merges --name-only 433ac25cf..HEAD
^f2a664eb8` names one commit, `cd55daf7b`, touching only
`seal/threads/1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite/trail/gate.md`.
The run's log reads `BROAD GATE PASSED`, suite 5648 passed and 9 skipped,
chain exit 0, rounds 2 (read).

**The body's copy of the records holds** (executed). `seal pr-body
seal/threads/1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite
--body <scratchpad>/1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite/body.md
--check` exited 0. The part above `## From the records` is `pr.md`: one
quote of `frame/plan.md` *Judgments of the run* and `Closes #1582.`.
`Commit and pull request language` and `Record language` are both English,
so no `pr.<lang>.md` is owed and none stands (read).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1's case is red against the base's code: the gate beside a cut sprite exits 2 | `trail/phases/phase-1.md` *Each new case was seen red*, first bullet | in the clone, `broad_gate.py` and `seal_stamp.py` restored from `f2a664eb8`, then `bin/test -q -p no:xdist tests/skills/test_broad_gate.py::Test_main::test_a_malformed_sprite_leaves_the_verdict_and_the_report_as_they_were` | holds (executed): fails on `assert cut.returncode == 0` with `2 == 0`, stderr `... seal_stamp.py will not load, so nothing ran: seal stamp: the disc's mark sprite ... (1 lines). Nothing was drawn.`, the import-time read the case names |
| S2's `--from` case is red against the base's code: `--from` drew and claimed | `trail/phases/phase-1.md`, second bullet | the same clone and restore, `tests/skills/test_seal_stamp.py::Test_main::test_from_refuses_a_malformed_sprite_in_one_line_and_claims_nothing` | holds (executed): fails on `assert 0 == 2`, `main(["--from", ...])` returned 0 |
| S2's `--stop` case is red against the base's code: `--stop` printed a drawn stamp | `trail/phases/phase-1.md`, third bullet | the same clone and restore, `tests/skills/test_seal_stamp.py::Test_main::test_stop_draws_nothing_beside_a_malformed_sprite_and_claims_nothing` | holds (executed): fails on the `capsys` line, stdout `{"systemMessage": "SEALED feat/x @ aaa1111 ...` |
| S3's case is red against the base's rules at `bbb2` and `bbb2222`, and at `bbb222`, `cafe`, `BBB2222` and `zzzzzzz`; the two moved values fail too | `trail/phases/phase-2.md` *The S3 case was seen red* | the same clone and restore, `tests/skills/test_seal_stamp.py::Test_ref_is_commit` | holds (executed): `ref_is_commit('bbb2', 'bbb2222')` True where False is asserted, and the rows `bbb222`, `BBB2222`, the 41-character row, `cafe` and `zzzzzzz` fail; `[BBB2222]` and `[bbb2]` of the two older cases fail at their moved values. 11 failed, 10 passed over the four selections of this and the rows above |
| The 41-character row is red with the ceiling of forty alone removed, on that row alone | `trail/phases/phase-2.md` *The case gained a row for a 41-character spelling* and the mutant list | in the clone at HEAD's code, `SHA_SPELLING`'s `{SHORTEST_SHA},40` made `{SHORTEST_SHA},` (the `Edit` tool), then `bin/test -q -p no:xdist -rf tests/skills/test_seal_stamp.py::Test_ref_is_commit` | holds (executed): one failure, `test_answers_as_a_refusal_record_is_matched[bbb22220000000000000000000000000000000000-bbb2222-False]`, `assert True is False` |
| `rounds_rows`' `except (Exception, SystemExit)` is what holds `[raises]`: with `except SystemExit` alone it fails with `ValueError: planted` | `trail/phases/phase-1.md` *The deferred row's rule stays* and the mutant list | the same run, `rounds_rows`' arm made `except SystemExit:` (the `Edit` tool), `tests/skills/test_broad_gate.py::Test_rounds_rows::test_refuses_to_stop_a_run_where_the_check_will_not_load` | holds (executed): `[raises]` alone fails, `ValueError: planted`. 2 failed, 18 passed over both selections; the clone's code was restored with `git checkout HEAD --` after it |
| The two modules' cases pass at HEAD, `test_refuses_a_copy_without_the_git_helper_in_a_sentence` among them unchanged | `trail/phases/phase-2.md` *The phase boundary set passed*; `frame/design.md` S4 | in the clone at HEAD's code, `bin/test -q tests/skills/test_broad_gate.py tests/skills/test_seal_stamp.py` | holds (executed): exit 0, 406 passed, 1 skipped. The test diff leaves that case's body as it was (read: `git diff f2a664eb8...HEAD -- tests/`) |
| `seal stamp` with no argument and with `--shape` beside a malformed sprite exit 2 in one line, where the base ended in a traceback at exit 1 | `changelog.md` *Fixed*, second item; `frame/design.md` *Data & interfaces* | in the clone, `seal-mark.txt` cut to its first line, `python3 skills/verify/scripts/seal_stamp.py` and `... --shape`; then `seal_stamp.py` from `f2a664eb8` and no argument | holds (executed): HEAD exits 2 both times, stdout empty, stderr the one `SPRITE_MALFORMED` sentence; the base exits 1 and stderr ends in `ValueError: seal stamp: the disc's mark sprite ...`. The clone's sprite and code were restored after |
| *Removes*, the sprite read at import: no `SPRITE` constant stands | `frame/design.md` *Removes*, row 1 | `git grep -n -w SPRITE -- skills tests` at HEAD | holds (executed): prints nothing, exit 1 |
| *Removes*, the wrapper, its callers' calls and the arms only it fed; `changelog.md` *Removed*, `sibling_module` | `frame/design.md` *Removes*, rows 2 and 3; `changelog.md` *Removed*, first item | `git grep -n -e sibling_module -e 'will not load' -e 'Refused, SystemExit' -- skills/verify/scripts/broad_gate.py`; `git grep -n sibling_module -- tests skills lib`; `git grep -n seal-mark -- skills/verify/scripts/broad_gate.py` | holds (executed): each prints nothing and exits 1. The diff removes `main`'s early load, its `except Refused` around `repo_root`, `__main__`'s `try`, the `Refused` of `rounds_rows`, the sentences of `git`, `gitcmd_module` and `write_gate_file` and the sprite of the exit 2 list (read) |
| *Removes*, the wrapper's cases; `changelog.md` counts five | `frame/design.md` *Removes*, row 4; `changelog.md` *Removed*, first item | `git diff f2a664eb8...HEAD -- tests/ \| grep -E '^[-+]\s*(def test_\|class Test)'`, and `git grep` of the three names over `tests` | holds (executed): five removed, `Test_sibling_module`'s three and the two of `Test_main`; no name stands |
| *Removes*, the second same-commit rule and `HEX_REF`; `changelog.md` *Removed*, `HEX_REF` | `frame/design.md` *Removes*, row 5; `changelog.md` *Removed*, second item | `git grep -n -E 'startswith\((base\|ref\|one\|other)\)' -- skills/verify/scripts/seal_stamp.py`; `git grep -n -F '{4,40}'`; `git grep -n -w HEX_REF -- skills tests lib` | holds (executed): one line, `seal_stamp.py:1154` in `_same_commit`; the other two print nothing. No other comparison of two commits stands in `seal_stamp.py`: `refused_here` asks `_same_commit`, and `sealed_before` reads targets through it (read: `:1104-1190`) |
| *Removes*, the pin of `bbb2` as the commit | `frame/design.md` *Removes*, row 6 | `git grep -n bbb2 -- tests/skills/test_seal_stamp.py` | holds (executed): `bbb2` stands in the refused list (`:991`) and as a `False` row (`:998`), nowhere as accepted |
| The issue's `assets/seals/seal-mark.txt` is `skills/verify/scripts/seal-mark.txt` | `frame/design.md` G2 | `git ls-files \| grep -i seal-mark`; `git ls-files assets/seals` | holds (executed): the one sprite is `skills/verify/scripts/seal-mark.txt`; `assets/seals/` holds none |
| A refusal record's target and the SHA it is matched with are hex of 7 to 40, so the hex check drops nothing `refused_here` used to match | `trail/rounds/round-1.md` *Confirmations*, *Scope* item 5 | read: `seal_stamp.py#_target_of`, `#queue_for_written_guarantee` `:1320-1349`, `lib/fields.py:97`, `:205` | holds (read): every target is the `commit` group of `fields.COMMIT`, `[0-9a-f]{7,40}` |
| A hex `--base` of 4 to 6 characters now prints `<ref> @ <commit>` | `changelog.md` *Changed*, first item | read: `broad_gate.py#resolve_base`'s fallback `Base(given, given_commit, given, given_commit)` against `ref_is_commit` | holds (read): `ref` is the typed spelling, which `_same_commit` refuses under seven characters. Round 1's probe executed `sealed_names` for `ee8a` (carried, not re-run) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `build()` reads the sprite where it draws and nothing reads a file at import; the gate's load wrapper and the arms only it fed go, and `rounds_rows` catches a raising check itself; `ref_is_commit` answers through `_same_commit`, hex of 7 to 40, case-folded; `skills/code-review/orchestration.md:533` and `chain_check.py`'s comparisons stay out | the issue's *Direction* (its second option) and both *Done when* lines; the diff; every `## Removes` row, each re-run above | none. The departure on `rounds_rows` that phase 1 recorded was folded into *Scope* item 4 and *Data & interfaces* at `5d0a4758d` (read) |
| the build | phase 1 delivers *Scope* items 1 to 4 at `385ee7e2f`, phase 2 item 5 at `3bc7d5968`; each new case seen red; each mutant red | `frame/plan.md`'s two Status cells, each an ancestor of HEAD (executed, `git log`), with `trail/phases/phase-1.md` and `phase-2.md` standing, as `routing.md`'s `Implementation` row `crafter` asks; the sampled `seen red` and mutant claims, re-run above | none |
| the last round | round 2, over `6b6ef8ba9..f4e0fb468`, opens no finding and confirms round 1's finding 1, `fixed c0ee3fc7c`: both docstrings name the malformed sprite | the diff of `seal_stamp.py`'s `Exit codes` paragraph and `drawn_from`'s docstring (read); only round 2's record and `trail/gate.md` follow its target (executed) | none |
| the changelog | the gate's verdict no longer depends on the sprite; `seal stamp` and `--from` refuse it in one line, `--stop` draws nothing and exits 0, `--guarantee` queues; one same-commit rule, and two spellings of `--base` print differently; a module that raises at load ends the gate at exit 1, except `chain_check.py`; `sibling_module`, its five cases and `HEX_REF` removed | the design's *Data & interfaces*; the re-runs above; the diff | none |
| the orchestrator's part of the pull request body | `pr.md`: the title takes `fix:`, quoted from `frame/plan.md` *Judgments of the run*, and `Closes #1582.` | the quote stands word for word in that row (read); the issue's title opens `fix:` (executed, `gh issue view 1582`); `routing.md` *Why this way*, the orchestrator's account of the route under `agentic`, describes a change to two gate scripts and their cases, which is what the diff changes. Its sentence that helpers move between the scripts states the issue's first option, which the framer rejected in `frame/plan.md` *Alternatives considered* row B; the route it grounds is no lighter for that | none |

**Left open, and disclosed where the records name it** (read).
`skills/code-review/orchestration.md:533-534` still names only a `python3`
that cannot load `seal_stamp.py` and a working directory outside the clone
as where the `Stop` hook draws nothing; after this change a malformed sprite
is a third. `frame/design.md` *Scope*, *Out* leaves it to #1579 and
`gaps.md` *Not done* names it. `docs/checks/the-stamp.md` *The stamp* takes
the sprite's sentence through `## Rule changes` at the settle. The issue
asks neither.

**Not verified here.** S1's case on Windows: CI's `windows-latest` legs on
the pull request answer it (`gaps.md`). `frame/plan.md` *Overlap with the
release*, which reads #1573's and #1579's checkouts: the orchestrator
answers it, since this audit opened neither checkout.

```seal
target: cd55daf7bfe7cefc150f74aa10f411d42132b2a4 against f2a664eb85677c4a4656c76d2e01b7091b1609fe
Verdict: sealed
```

## Re-audit after the base moved

Audited at `b007ebcb013f512c18f1963acdea49d383cb5fdd` against the base
`release/v0.38.6`, which `release/v0.38.6@{upstream}` now resolves to
`da7bd39687fbc0e6b68a441d0fa3f49ecdaf1c74`, #1579's landing (executed,
`git rev-parse --verify --quiet`). Three commits follow the earlier block's
target (executed, `git log --oneline cd55daf7b..HEAD`): `1d6663009`
commits this file as written, `8e3cc7204` merges `da7bd3968` with first
parent `1d6663009`, and `b007ebcb0` appends `trail/gate.md`'s new run. This
audit re-runs the claims whose coordinates those commits touched and reads
the parties again. The re-runs ran in a new `git clone --no-local` of the
worktree, `<scratchpad>/1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite/at-base-2/repo`,
at HEAD.

**The broad run is at HEAD** (executed). `trail/gate.md`'s last `seal` block
reads `run: 8e3cc7204 against da7bd3968`. `8e3cc7204` is an ancestor of
HEAD, and `git log --no-merges --name-only 8e3cc7204..HEAD ^da7bd3968`
names one commit, `b007ebcb0`, touching only
`seal/threads/1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite/trail/gate.md`.
The log reads `BROAD GATE PASSED ... @ 8e3cc7204 against origin/release/v0.38.6 @ da7bd3968`,
suite 5652 passed and 9 skipped, chain exit 0, rounds 2 (read).

**The body's copy of the records holds** (executed). `seal pr-body
seal/threads/1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite
--body <scratchpad>/1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite/body.md
--check` exited 0 at HEAD.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The merge brought only the base's change: the branch's own diff of code and cases is the one the earlier block audited | `8e3cc7204`, "merged with no conflict" (the orchestrator's account) | `git diff f2a664eb8 cd55daf7b -- skills tests lib` and `git diff da7bd3968...HEAD -- skills tests lib`, each with its `index` and `@@` lines dropped, then `cmp` | holds (executed): the two are byte for byte the same. `git diff da7bd3968 HEAD --stat -- skills tests lib` names the same four files, 176 insertions and 191 deletions |
| The base's change meets the audited units in comments alone | the orchestrator's account | `git diff f2a664eb8 da7bd3968 -- skills/verify/scripts/broad_gate.py lib/config.py`, and `--stat` over `seal_stamp.py`, `seal-mark.txt`, both test files, `lib/sibling.py`, `lib/fields.py`, `lib/routing.py` and `chain_check.py` | holds (executed): `broad_gate.py` changes two citations, in `moved_line`'s docstring and `gate`'s comment, from `skills/code-review/orchestration.md` to `skills/code-review/gate-to-pull-request.md`; `lib/config.py` changes one docstring of `pact_declaration`; the rest print nothing |
| The two modules' cases pass at HEAD | `trail/phases/phase-2.md` *The phase boundary set passed* | in the clone at HEAD, `bin/test -q tests/skills/test_broad_gate.py tests/skills/test_seal_stamp.py` | holds (executed): exit 0, 406 passed, 1 skipped |
| S1's, S2's and S3's cases are red against the base's code, the base now `da7bd3968` | `trail/phases/phase-1.md` and `phase-2.md`, the seen-red bullets | in the clone, `broad_gate.py` and `seal_stamp.py` restored from `da7bd3968`, then `bin/test -q -p no:xdist` over the S1 case, both S2 cases and `Test_ref_is_commit::test_answers_as_a_refusal_record_is_matched` | holds (executed): 9 failed, 3 passed. S1 fails on `cut.returncode` with stderr `... seal_stamp.py will not load, so nothing ran ...`; `--from` on `assert 0 == 2`; `--stop` on its `capsys` line; S3 on the rows `bbb2`, `bbb222`, `BBB2222`, the 41-character row, `cafe` and `zzzzzzz`. The clone's code was restored after |
| *Removes* and `changelog.md` *Removed*: nothing removed stands, in `broad_gate.py`, which the merge touched, or elsewhere | `frame/design.md` *Removes*, rows 1 to 3 and 5; `changelog.md` *Removed* | the earlier block's searches, at HEAD: `git grep -n -w SPRITE -- skills tests`; S4's two; `git grep -n seal-mark -- skills/verify/scripts/broad_gate.py`; `git grep -n -w HEX_REF -- skills tests lib`; S3's | holds (executed): each prints nothing and exits 1, except S3's, which prints one line, `seal_stamp.py:1154` in `_same_commit` |

The guard-removed re-runs of the earlier block, the 41-character row and
`rounds_rows`' `[raises]`, are not re-run: the merge changed no statement
of `seal_stamp.py` and none of `rounds_rows` (executed, the diffs above).

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | as the earlier block reads it; *Scope*, *Out* gives `skills/code-review/orchestration.md:533` to #1579, "which moves that paragraph to another file in this release" | the diff, unchanged by the merge; #1579 moved the paragraph to `skills/code-review/gate-to-pull-request.md:215-220` (executed, `git grep -n` for `cannot load` and `seal_stamp.py`) | none |
| the build | as the earlier block reads it | the re-runs above; `frame/plan.md`'s Status cells, `385ee7e2f` and `3bc7d5968`, still ancestors of HEAD | none |
| the last round | round 2, as the earlier block reads it | only round 2's record, `trail/gate.md`, this file and the merge of the base follow its target, and the merge changes no line of the branch's own diff (executed) | none |
| the changelog | as the earlier block reads it | the re-runs above; no sentence of it or of `pr.md` names a file the merge moved (executed, `git grep -n orchestration.md` over both prints nothing) | none |
| the orchestrator's part of the pull request body | `pr.md`, unchanged since the earlier block | `seal pr-body --check` at HEAD, exit 0; the quote in `frame/plan.md` *Judgments of the run*; the account of the merge in this audit's spawn, which the first two rows above re-ran | none |

**A coordinate the merge moved, in the closing memo** (read). `gaps.md`
*Not done* (`:13`) names `skills/code-review/orchestration.md:533`, which
no longer holds that paragraph: #1579 moved it to
`skills/code-review/gate-to-pull-request.md:215-220`, as the design said it
would. What the memo says of the paragraph still holds at its new place: it
names a `python3` that cannot load `seal_stamp.py` and a working directory
outside the clone, and not a malformed sprite. #1579 has landed, so the
work item the memo hands that sentence to is closed, and no open work item
holds it. The issue asks nothing of that paragraph, and
`docs/checks/the-stamp.md` takes the sprite's sentence at the settle, so
this is no reason to withhold.

**Not verified here**, as in the earlier block: S1's case on Windows, which
CI's `windows-latest` legs answer on the pull request.

```seal
target: b007ebcb013f512c18f1963acdea49d383cb5fdd against da7bd39687fbc0e6b68a441d0fa3f49ecdaf1c74
Verdict: sealed
```
