# Review round 3: 1793240968-every-session-reads-bootstrap-and-parity-setup

target: 6553add0, fixes 9f4c756e..6553add0

## Findings

This round raises no finding. The one close it answers holds, and the fix
diff adds no unit that is wrong.

## Confirmations

confirms: round-2#1
The close at `eca53e15` holds. Step 7 of `skills/parity-setup/SKILL.md`
now gives each setup its own sentence (`:63-76`). Under shared, records
only, it says three things. No workflow reads a round record. `seal gate`
runs the same check. The gate refuses a round record without the
original line once a ready pull request is open for the branch, and before
then it names the record and passes. Each part is true.

The fix pass claimed that `seal gate` runs the same check. The gate's chain
arm runs `chain_check.py --baseline <base> --root <root> --sealing`, with no
`--worktree` and nothing about `.github/`
(`skills/verify/scripts/broad_gate.py:2983-2988`, `:147`, `:150`) (read).
`chain_check.py` asks `gh pr view` where no event payload exists (`:768-800`),
and judges strictly any state it saw other than a draft (`:2233-2235`, `:2342`).
At `--sealing` only the guarantee's `original:` line is spared
(`:2327-2336`) (read).

This round re-ran round 2's executed evidence, written again from its
`## Probes` row. It added the draft state, which the new "before then"
clause also covers. In a `git clone --no-local` at `6553add0`, the module's
migrating branch had no `.github/` directory, no event payload and the
suite's `gh` stub on PATH. A ready answer made the `--sealing` run exit 1
and name both round records. A draft answer and a no-pull-request answer
each made it exit 0 and name the same two (executed, see `## Probes`).

The local-mode sentence (`:74-76`) is carried from round 2 and not
re-derived. `read_record` reads `seal/parity.md` through `git show HEAD:`
(`skills/code-review/scripts/chain_check.py:736-747`, `:1826`), and a local
root is not in git. The fix diff touched no line of `chain_check.py`, so
nothing re-opens that fact.

Two limits stand, and neither is a finding. First, the records-only
sentence does not repeat the earlier clause's "changes anything outside the
document roots". It says the gate runs "the same check", and `originals_of`
applies that condition (`chain_check.py:1815-1824`) (read). A person who
reads it as covering a docs-only pull request is told of a refusal that
does not come, and writes a line the proofer writes anyway. Second, where
neither the event payload nor `gh` can see the pull request, the state is
`unknown`, the run is not strict, and the gate passes with a ready pull
request open (`:796-800`, `:2233-2235`) (read). That is outside the normal
flow, where `gh` opens the pull request.

confirms: none
The two new assertions pin text the old step 7 lacked (contract rule 15).
In whitespace-folded `9f4c756e:skills/parity-setup/SKILL.md`, "the gate
refuses a round record without it once a ready pull" matched 0 times, and
"In local mode git carries neither" matched 0 times. So each assertion
fails against the text before the fix (executed). The fix pass claimed it
saw them red and that `bin/seal mutate` turned them red. This round did not
re-run either act, since the phrase search already shows the assertions
fail on the old text. At `6553add0`,
`bin/test tests/behaviour/test_chain_hooks_hardening.py -q` exited 0 with 30
passed (executed). The diff adds no test function, only assertions inside
`test_parity_declaration_is_bootstrappable_not_hand_written`, so no group
reading is owed.

confirms: none
The other two places that stated the old premise now state the new one
(read). The test comment at
`tests/behaviour/test_chain_hooks_hardening.py:264-269` says local mode has
no check and that `seal gate` refuses under shared, records only, once a
ready pull request is open. `changelog.md:5` gives the same three sentences
for the three setups as step 7. A `git grep` for "nothing refuses", "no
pull-request check reads" and "only installed" outside `seal/threads/`
found only step 7's local-mode sentence and the test's two assertion
messages (executed). No other sentence states the old premise (contract
rule 19).

confirms: none
This round stayed inside the fix diff. `git diff --stat 9f4c756e..6553add0`
touches four files: `skills/parity-setup/SKILL.md`,
`tests/behaviour/test_chain_hooks_hardening.py`, `changelog.md` and
`trail/rounds/round-2.md` (executed). `trail/rounds/round-2.md` changes
only its `verdict:` and `answer:` lines. `eca53e15` touches
`skills/parity-setup/SKILL.md`, which finding 1's `location:` names. It
carried, without re-deriving, round 1's byte-for-byte move, its word counts
and its nine modules passing at `904078cf`, and round 2's local-mode
reading. `seal/parity.md` is not declared in this repository (`seal/` holds
`config.md`, `follow-up.md`, `README.md` and `threads/`), so this record
names no baseline commit of an original.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch; `gaps.md` labels them `unverified`, the label is honest, and this round ran none of them. Nothing is open after this round, so the broad run is what comes due, and the sealer's spawn after it | the branch at `6553add0` | the orchestrator, at `seal gate --record` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round3_records_only_states.py -p no:xdist -q -s`, one file in a `git clone --no-local` at `6553add0`, importing `test_chain_check.py`'s `_branch_template`, `branch`, `check`, `migrating` and `original_lines`: no `.github/`, `GITHUB_EVENT_PATH` unset, PATH from `conftest.gh_answers` for `ready`, `draft` and `unknown`, then `migrating(root, (None, None))` and `check(root, capsys, "--sealing")` | exit 0, 3 passed: `ready` gave chain-check exit 1 naming both round records; `draft` and `unknown` each gave exit 0 naming the same two |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py -q` in the same clone | exit 0, 30 passed |
| `git show 9f4c756e:skills/parity-setup/SKILL.md`, whitespace folded, searched with `grep -c -F` for each of the two new assertion phrases | 0 matches for each |
| `git grep -n -i -e "nothing refuses" -e "no pull-request check reads" -e "only installed"` outside `seal/threads/` | `skills/parity-setup/SKILL.md:76` and `tests/behaviour/test_chain_hooks_hardening.py:277`, `:282` |
| `git diff --stat 9f4c756e..6553add0` | four files, as `## Confirmations` lists |
