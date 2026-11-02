# Review round 5: 1793573496-the-settle-folds-named-directories-the-person-marks

```seal
target: 8e6cf41b6, fixes 3ed5dd51b..8e6cf41b6
```

This verifying round read the diff `3ed5dd51b..8e6cf41b6` in the branch's own
worktree. That diff holds the fix pass's commit (`ffb376cfa`), its close
blocks on round 4 (`92c1934c4`) and the orchestrator's fold into
`frame/design.md:99` (`8e6cf41b6`). The orchestrator's judgment row
(`frame/plan.md:55`) makes this the run's last round and limits it to round
4's two closes. This round stayed inside the fix diff. No `seal/parity.md` is
declared, so the round block holds no `original:` line. `seal/config.md`
holds no `Record language` row, so the record is English.

Carried from round 4 as coordinates, not re-established: where the listing
lives (`settle.py#history`, `#git_fields`), the probe shapes that showed
`--cc --name-status` prints `MM` for a clean merge of two edits while `--cc
-p` prints no hunk, and the class of ways a merge's result can differ from
every parent. Re-derived here: whether each text now states the rule, whether
the new case goes red, and whether the signature case holds under a foreign
signing program.

The fix pass's account was read as a claim and checked against the code. It
claimed the clean-merge case was seen red by `seal mutate` dropping `--cc`.
This round wrapped `settle.git_fields` to drop `--cc` and the case raised
`AssertionError`, executed; this is the same mutation, run as a wrapper and
not as `seal mutate`. It claimed the signature case passes under a global
`gpg.ssh.program=/usr/bin/false`. It does, executed, and it ran to its
assertions rather than skipping. It claimed `seal mutate` deleting the
`gpg.ssh.program` line survives because the case then skips. This round did
not run that; the claim agrees with the code at `test_settle.py:2183-2184`,
read.

## Findings

None. This round opens no finding, and so no `must`.

## Confirmations

```seal
confirms: round-4#1
```
What holds: each text on the history reader now states the rule and lists no
kinds of merge, read. `history`'s docstring says a merge is named at a path
where its result there differs from every parent's, however it came to
differ, and nowhere else (`skills/settle/scripts/settle.py:905-911`). Its one
example is marked as an example ("as for a merge with no conflict"), and it
is the shape round 4's probe built. The module docstring
(`settle.py:64-66`), the skill's listing bullet
(`skills/settle/SKILL.md:220-223`), the changelog fragment
(`changelog.md:3`) and the design's fold (`frame/design.md:99`) each say a
merge whose result differs from every parent's changed the file, and added it
where no parent holds it. The deletion sentence in the skill is marked "for
example" (`SKILL.md:224`).

The class was listed by searching the worktree for each phrase of the old
lists: "conflict it resolved", "two parents' edits", "resolved or wrote" and
"wrote it new". `git grep` found none outside the round records, executed.
That search is a sample of spellings. The texts that state the rule were
listed a second way, by taking apart what round 4's finding located: the
module docstring, `history`'s docstring, the skill's bullet, the changelog
and the design. Each was read whole at the lines above.

The case `test_a_clean_merge_of_two_edits_is_a_documents_last_change`
(`tests/skills/test_settle.py:2027`) is round 4's case, unchanged. It passes
at HEAD, executed, and goes red with `--cc` taken out of the reader's
arguments, executed. So the sentence the texts state is now pinned by a case
that has been seen red.

```seal
confirms: round-4#2
```
What holds: the signature case writes `gpg.ssh.program` as `ssh-keygen` into
its own repository's config (`test_settle.py:2173`), and the repository level
overrides the global level. Under a `GIT_CONFIG_GLOBAL` whose
`gpg.ssh.program` is `/usr/bin/false`, the case signed and passed with no
skip, executed. Round 4's probe showed the same configuration raising
`CalledProcessError` before the fix.

The orchestrator asked whether skipping is the right failure direction. It
is, for the input it targets. The case pins the reader's
`--no-show-signature`, not the machine's ability to sign. A machine that
cannot sign has no defect in the reader to show, so a failure there would
turn a missing tool into a red suite for code nobody touched. The
repository's own rule says the same: `symlink_or_skip`
(`tests/conftest.py:626-649`) asks by attempting the call and skips where the
platform cannot do it, and this case asks by attempting `ssh-keygen` and
`git commit -S`.

What the skip costs, and why it is no finding. `symlink_or_skip` asserts its
fixture's own precondition before the attempt, so that a fixture bug is not
read as "not available here" (`conftest.py:641-645`). This case has no such
separation. A probe gave the commit a mistyped `user.signingkey` path: git
exited 128 with `Couldn't load public key ... No such file or directory`,
executed. The case's guard at `test_settle.py:2183-2184` would read that
fixture bug as "git could not sign a commit" and skip. The case is right as
it stands, so this is a hazard for a later edit, not a defect the release
ships. The skip prints what failed, which is where a reader of `-rs` would
see it. CI held the case before this fix: run 41366101808 at `1ec48bd77`
succeeded on every leg while a failed signing still raised, read from
`gh run view`. Whether each leg at HEAD signs or skips is a row of
`## Not judged`.

```seal
confirms: none
```
What matched: the narrow runs passed, executed. `bin/test
tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py
tests/behaviour/test_a_reference_root_is_read_and_never_taken.py
tests/behaviour/test_docs_line_wrap.py
tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py
tests/behaviour/test_settle_applies_rule_changes_in_place.py -q` exited 0.
`bin/test tests/skills/test_settle.py -q -rs -p no:xdist -k "show_signature
or clean_merge or show_root"` ran three cases, all passed and none skipped.
`uvx ruff check` and `uvx ruff format --check` on `settle.py` and
`test_settle.py` exited 0. These are narrow runs, not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the lint and the format check at HEAD. This round ran six modules, and the suite is labelled `unverified` | the repository's `Broad gate` row | the orchestrator, by `seal gate --base origin/release/v0.28.0 --record <item>`, then the sealer |
| Whether each CI leg at `8e6cf41b6` signs and runs the signature case or skips it; the workflow's `-q` output does not name skips | `tests/skills/test_settle.py:2149`, `.github/workflows/test.yml` | the orchestrator, reading the next CI run with skip reasons shown |
| Round 4's row on configuration keys outside `log.` and `diff.`, and round 1's rows for design A7 and for Windows and case-insensitive paths, carried as they stand | `trail/rounds/round-4.md` and `trail/rounds/round-1.md` *Not judged* | the answerers those rounds name |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round5_1054.py -q -s -rs -p no:xdist`, one file in the worktree's `tests/skills/` importing `test_settle`, run twice, once for the exit code and once for the output | 3 passed. With `settle.git_fields` wrapped to drop `--cc`, the clean-merge case raised `AssertionError`. Under a `GIT_CONFIG_GLOBAL` holding `gpg.ssh.program = /usr/bin/false`, the signature case passed without a skip. With `user.signingkey` pointing at a missing file, `git commit -S` exited 128 with `Couldn't load public key` and `fatal: failed to write commit object` |

The probe file and its bytecode were removed before hand-back, and `git
status` in the worktree showed nothing else. Two earlier rounds' probe
bytecode files, `test_tmp_round2_1054` and `test_tmp_round3_1054`, stand in
`tests/skills/__pycache__/`; this round did not make them and left them.
