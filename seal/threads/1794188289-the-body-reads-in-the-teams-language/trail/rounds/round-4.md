# Review round 4: 1794188289-the-body-reads-in-the-teams-language

```seal
target: 106c5aad, fixes ddc867f2..106c5aad
```

This is the verifying round over the repair made after the seal, the path
`skills/code-review/orchestration.md:354-358` gives a defect that one
platform shows once the pull request opens: a verifying round on the fix's
diff, the broad run again, and the sealer again. No round record named this
fix. The fix diff `ddc867f2..106c5aad` was read whole. It holds two
commits. `9bdf9f7a` changes one case of `tests/skills/test_chain_check.py`,
its docstring and three of its statements. `106c5aad` appends one
paragraph to `trail/phases/phase-2.md` *What this phase found* (executed:
`git diff --stat ddc867f2 106c5aad`). The commits from the last round's
target `e4b4d22f` to `ddc867f2` are round 3's record, the gate record and
the guarantee, all records of this work item (executed: `git diff --stat
e4b4d22f 106c5aad`).

The work item's `routing.md`, the three frame files, `gaps.md`,
`changelog.md` and `pr.md` were read whole at `106c5aad`. None of the seven
changed after `e4b4d22f`, and the fix diff contradicts no sentence of
theirs. `frame/design.md:42`, *Scope* item 3, says the translated file is
read as `pr.md` is read, "as its bytes stand", and that `--check` compares
the first part line by line. The repaired case holds both. The quotes of
`pr.md` were not compared again by script. `pr.md`, `changelog.md`,
`frame/plan.md` and `gaps.md` stand byte for byte as they did at
`f2b29c48`, where round 2's probe found all twelve quotes at their sources
and round 3 carried that result (executed: the `git diff --stat` above
names none of the four). No `pr.<lang>.md` is owed: both language rows of
`seal/config.md` read `English` (`seal/config.md:9-10`).

Carried from round 3, not re-established: the twelve quotes' sources, and
where `pr_body.py#first_part` and `#compared` live. Re-established this
round: how `read_own` reads a file, how the arm compares the first part,
the Windows failure itself, and every verdict below.

No `seal/parity.md` is declared. The fix diff adds no test case. It
rewrites one existing case, so no new case is read against its group.

## Findings

None. The fix diff holds no defect this round found.

## Confirmations

What matched: the cause the fix names is the cause CI shows. The failed run
`42561139757` failed one job, `pytest (windows-latest, 3.12, --splits 4
--group 3, ...)`, on one case,
`tests/skills/test_chain_check.py::Test_body::test_reads_the_translation_as_the_bodys_first_lines`,
at `test_chain_check.py:3505`. That line at `ddc867f2` is
`assert composed.startswith("닫는다 #1.\nCloses #1.\n")`. The assertion
printed the body opening with the translation line, then `Closes #1.`,
each ending in `\r\n`. The job ended "1 failed, 904 passed, 16 skipped".
The other three Windows jobs and every other job passed (executed: `gh run
view 42561139757 --json jobs` and `--log-failed`).

What matched: the code is right to keep the bytes, and the case was wrong
to assume LF. `tests/conftest.py:1136-1140` (`write`) calls
`Path.write_text` with no `newline`, which ends each line with the
platform's line end. `pr_body.py:398-426` (`read_own`) opens each
first-part file with `newline=""` and returns it as its bytes stand, which
`frame/design.md:42` fixes. The arm drops line ends before it compares.
`pr_body.py:895-922` (`_first_part`) compares
`READER.gfm_lines(head)` with `READER.gfm_lines(text)` of each file, and
`lib/blocks.py:382-388` (`gfm_lines`) strips `\r\n` from each line unless
`keepends` is asked for (read).

What matched: the repaired case still fails on each defect it pins, under
LF writes and under CRLF writes alike. Three hand mutations of
`pr_body.py` were run against the case in a clone at `106c5aad`. Each run
was done once plainly and once with a probe plugin that makes
`Path.write_text` end lines with CRLF (executed: `## Probes`).

- `compared` reading `pr.md` alone (`pr_body.py:972`): red at
  `test_chain_check.py:3515`, `assert code == 0`, both runs.
- `first_part` returning `pr.md` alone where the rows differ
  (`pr_body.py:480`): red at `:3509`, the assertion on the first two lines,
  both runs.
- `_check` skipping the first part's comparison (`pr_body.py:939`): red at
  `:3519`, `assert code == 1`, both runs. This mutant is caught only by the
  case's second half, the half the fix rewrote. Under CRLF writes the old
  `composed.replace("닫는다 #1.\n", "", 1)` matched nothing, so that half
  could not have been the catch there.

The old case at `ddc867f2` failed under the CRLF plugin at the
`startswith` assertion, with the body CI printed, and passed without it.
The repaired case passed both ways (executed). The docstring's added
sentence states what the case does, and its "Seen red with `compared`
reading `pr.md` alone, where the composed body was refused at its first
line" matches the first mutant.

What matched: no other case this work added assumes `\n` over a file that
`write` or `Path.write_text` wrote. The list is closed: the files `git diff
c4bb8877 106c5aad -- tests evals` names. They are seven test modules,
`evals/scripts/rule_cases.py` and five sealer scaffolds whose diff adds
only the two language rows (executed). The seven modules were run under the
CRLF plugin and passed, 502 cases (executed: `## Probes`). The plugin
patches `Path.write_text` alone. A search of the lines the diff adds found
no other text-mode writer: no `open(`, no `write_config`, no `newline=` and
no `os.linesep` (executed: `git diff c4bb8877 HEAD -- tests evals | grep
-nE`, exit 1). The first-part files of `tests/skills/test_pr_body.py` are
written with `write_bytes` (`test_pr_body.py:275`, `:279`), so its byte
comparisons hold on any platform. `tests/evals/test_rule_cases.py:201-236`
writes the records and the body through `Path.write_text` alike and compares
lines through `seal pr-body --check`. The text cases read the repository's
own files, which `.gitattributes` checks out with `eol=lf` (read). CI agrees
at `ddc867f2`: that one case was the only failure on Windows (executed:
above).

What matched: the paragraph `106c5aad` appends to `trail/phases/phase-2.md`
holds at each claim this round checked. It names the leg, the case, the
assertion, the cause in `write` and `read_own`, and the arm's
`gfm_lines`. It says the old `replace` would have taken nothing out. It
says a mutation dropping the translation from `first_part` went red at the
line assertion. It says the changed modules passed under the plugin with
this case as the one failure, 501 passed. That count is this round's 502
less the one case that failed then. The paragraph names its plugin by a
`<scratchpad>/` path, not a machine path.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite as a whole, the repository-wide lint and the typecheck: `unverified`, since contract rule 2 leaves the broad gate to the orchestrator. The four Windows jobs of the `tests` run `42562185058` at `106c5aad` were still pending when this round read them | the `Broad gate` row of `seal/config.md`; pull request #1456's checks | the orchestrator, at the repair's broad run and on the pull request's checks |
| The `hygiene` run `42562185034` at `106c5aad` failed in the `release` job. The last round's target, the gate run and the guarantee are behind `9bdf9f7a`, and the body's line 18 carries a seal mark the records no longer give. The repair path owes each of these, and this record answers the first | `skills/code-review/orchestration.md:354-371` | the orchestrator (the gate run and the body sent again), then the sealer |
| Round 1's other three rows of `## Not judged`, which round 3 carried. The fix diff touches none of their coordinates | `trail/rounds/round-1.md` *Not judged* | the repository owner and the settling session, as round 1 names them |

This round leaves no finding open. Next come the orchestrator's broad run
at HEAD, the sealer's spawn, and then the body sent again after the new
verdict.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_chain_check.py::Test_body::test_reads_the_translation_as_the_bodys_first_lines -q -p no:xdist`, in a `git clone --no-local` at `106c5aad` under `<scratchpad>/1453-r4/clone` | exit 0, 1 passed |
| the same with `-p test_tmp_crlf_plugin`, a probe plugin in the clone's `tests/` that makes `Path.write_text` end lines with CRLF where no `newline` is given | exit 0, 1 passed |
| the same two runs with `tests/skills/test_chain_check.py` restored from `ddc867f2` | under the plugin exit 1, at the `startswith` assertion, the body opening with the translation then `Closes #1.`; without it exit 0 |
| the case, plainly and under the plugin, with `pr_body.py:972` `first_part(item, root)` as `[(OWN_PART, read_own(item))]` | exit 1 both, at `test_chain_check.py:3515` |
| the same with `pr_body.py:480` returning `[(OWN_PART, own)]` | exit 1 both, at `:3509` |
| the same with `pr_body.py:939` `causes = _first_part(head, parts)` as `causes = []` | exit 1 both, at `:3519` |
| `bin/test tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_waiver_decided_at_start.py tests/evals/test_rule_cases.py tests/skills/test_chain_check.py tests/skills/test_pr_body.py tests/text/test_the_settings_have_a_front_door.py -q -p no:xdist -p test_tmp_crlf_plugin`, in the same clone at `106c5aad` | exit 0, 502 passed |
