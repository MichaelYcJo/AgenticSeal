# Review round 2: 1793152332-the-stamps-mark-is-an-owl

target: 656df69d, fixes 10a8444a..656df69d

## Findings

None. The fix range closes round 1's one finding and introduces no defect.

## Confirmations

confirms: round-1#1
The close `fixed 3155da43` holds. `3155da43` changes the two lines the
finding named, and only those. `tests/behaviour/test_the_release_seal_is_drawn.py:36`
and `tests/github/test_run_tests.py:444` now read
`word.lower().startswith("pillow")`, as the two cases in
`tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` already
did. All four absence assertions now fold case (read). In a clone at
`656df69d`, `bin/test` over the two changed modules and
`tests/github/test_release_seal.py` exited 0, with 102 passed (executed).
The probe then put the pin back in its capitalised spelling: `Pillow==12.3.0`
on the `seal` job's install line in `.github/workflows/publish-release.yml`,
and in `PACKAGES` in `.github/scripts/run_tests.py`. The workflow case and
both parametrisations of the build case each failed at the line the fix
changed (executed). With the two test files restored to `10a8444a`, the
same three cases passed over the same patched files. So the fix is what
refuses the pin (executed). In round 1's finding, `656df69d` changes only
the two lines the fix pass writes, the verdict and the answer. `37ffc99d`
adds `round-1.md` as round 1 wrote it (read).

confirms: none
Round 1 left this question open: whether `ccf642bf`'s new case
`test_refuses_an_icon_that_is_not_a_png_and_writes_nothing`
(`tests/github/test_release_seal.py:858`) owed a red run. It did not, and
round 1's row is answered. The coordinator's claim is that the refusal
existed before that commit and that `Test_main` already held it.
`cd6af1be:.github/scripts/release_seal.py:454-458` refuses a file without
the PNG signature and `IHDR`. `cd6af1be:tests/github/test_release_seal.py:304`
holds that refusal as the `the icon is not a PNG` parameter of `Test_main`
(read). The phase 1 record says that parameter was seen red against
`71bed8ff`. That is the implementer's account, and this round did not
repeat it. `release_seal.py` is unchanged from `cd6af1be` to `656df69d`
(executed: `git diff --stat` printed nothing). The case's other half
asserts that `draw` leaves no file at the path it was handed. That is also
behaviour `cd6af1be` already had, because `draw` writes the copy only after
every check passes (`.github/scripts/release_seal.py:459-463`, read).
`frame/plan.md` *Verification this work item owes* asks for a red run only
for behaviour that did not exist before. It also asks for one red run per
new behaviour, and phase 1 gave the refusal its run. So the case owes none.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch, labelled `unverified` | the whole tree | the orchestrator, through `bin/seal gate` now that no finding is open |
| Every row round 1 left here other than the `ccf642bf` row, which this round answers above. They are outside the fix range and carry forward unchanged | `trail/rounds/round-1.md` *Not judged* | the answerer each row names |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the repository into `<scratch>/1793152332-the-stamps-mark-is-an-owl/round-2/clone`, checked out at `656df69d` | HEAD `656df69de9793a12677ff9ad9c7364b2c8586bcd` |
| `bin/test -q tests/behaviour/test_the_release_seal_is_drawn.py tests/github/test_run_tests.py tests/github/test_release_seal.py` in the clone, under a scratch home and caches | exit 0, 102 passed |
| `Pillow==12.3.0` put on line 101 of `.github/workflows/publish-release.yml` and into `PACKAGES` at line 135 of `.github/scripts/run_tests.py` in the clone, through the Edit tool. Then `bin/test -q -p no:xdist` over `test_the_publishing_workflow_installs_the_pins_the_runner_holds` and `Test_build::test_a_fresh_build_installs_the_pinned_parser` | exit 1, 3 failed, each at the fixed line |
| `git checkout 10a8444a --` the two test files in the clone, then the same `bin/test` command over the same patched files | exit 0, 3 passed |
| `git diff --stat cd6af1be HEAD -- .github/scripts/release_seal.py` | no output, so the file is unchanged |
