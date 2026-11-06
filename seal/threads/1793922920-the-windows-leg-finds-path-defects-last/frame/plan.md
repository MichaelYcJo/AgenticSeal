# Implementation Plan: 1793922920-the-windows-leg-finds-path-defects-last

## Technical context

The tree as read at `e2f197dc`.

The census builds on `tests/censuses.py`. Each census is a function
`<name>(rel, root=None)` returning one line per problem (`:9-13`), and
`judge` runs the `CENSUSES` tuple (`:1311-1327`). `_python` (`:117-122`)
gives a `.py` file's text, and `_held` (`:77-98`) turns the flagged lines
into problem lines and reads the exemption comments. `bindings` and `dotted`
(`:336-377`) resolve a call's function through the file's imports, which is
how `encoding` sees `subprocess.run` under any import spelling, and how this
census sees `os.path.join` under `from os.path import join` or
`import os.path as osp`. A module file runs every census over its `TARGET`
through `census_case` (`tests/conftest.py:834`), and
`tests/test_censuses.py#Test_module` (`:1081-1104`) runs them over every
tracked file no module file names, the test files among them. So a
contributor running the module they touched meets the census at that run,
and nobody meets it first on the Windows leg.

The repair the census names already stands in the tree:
`skills/verify/scripts/broad_gate.py:2523` joins
`*GATE_FILE.split("/")`, the fix the 1051 branch made after run
40500883542.

The constraints. `skills/verify/scripts/test_layout.py:12-15` asks for a
class `Test_<name>` with an accepts case and a refuses case for each public
top-level function of `tests/censuses.py`. `tests/censuses.py` imports
nothing from `tests/conftest.py`, because
`evals/scripts/noninferiority.py` loads it by path (`:26-28`). The
`encoding` census reads every tracked `.py`, and so does this one, which
adds `evals/` to the four roots the issue names; the probe found one site
there.

This work's dispatched run of `tests`, which the orchestrator reads before
the broad run, reads the four shipped files Scope item 3 rewrites on
Windows, where their paths now take `\` throughout.

The failure scenario of the chosen approach, six months on. A path
constant moves into a shared module, such as `hooks/lib/optin.py`, and a
caller joins it as `os.path.join(root, optin.SOME_PATH)`. The census reads
one file at a time, so it sees no `/`, and the Windows leg is again the
first to report it, at the pull request. The census comment names that
limit, and the repair is the same split. A second scenario: exemptions
gather on lines where the `/` is the value under test. Each one states its
reason, and `_held` refuses one that excuses nothing, so an exemption leaves
the tree with the line it excused.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. A census reading literal arguments of `os.path.join` only, the issue's ask as written | It sees none of the recorded defects: the 1051 failure joined a module constant, and the issue's first defect built its `/` outside `os.path.join` (design *Grounding*). At `e2f197dc` it finds two `"/c"` fixture roots and nothing shipped. A mechanism with no catch on its record costs its upkeep for nothing | Rejected |
| 2. A census reading literal and f-string arguments and the file's own module-level constants assigned once | A constant imported from another module passes it, as `chain.BROAD_GATE_FILE` and `settle.SPECS` do today; Scope item 3 rewrites those two by hand, and the census comment names the limit | **Chosen.** It reads a parser's result and nothing guessed (`skills/core/SKILL.md` *The rule a mechanism is kept against*). It would have caught run 40500883542 at the slice. It costs under a second over the whole tree. It takes the form, reach and exemption the `encoding` census set for the last Windows-only class (#741, #762) |
| 3. The census of row 2, also resolving constants imported from the plugin's other modules | A census that opens other files breaks *each judged one file at a time* (`tests/censuses.py:1-13`): a module's `census_case` would turn red on an edit to a file it does not name, and the reader would have to follow `sys.path.insert` and `load_module` spellings, which no parser result gives | Rejected; two sites today, rewritten by hand |
| 4. ruff's `PTH118` (`os.path.join` should be `pathlib`) | It flags all 1063 calls, the correct ones with them, and its repair is a move to `pathlib` across the tree, which is a different work item with its own argument | Rejected |
| 5. Build no census; keep the Windows leg and the stated limit as they stand | A constant joined with a `/` reaches the pull request again, as at run 40500883542, and pays the repair path `skills/code-review/orchestration.md` *The stated limit* gives: a verifying round, the broad run and the sealer again | Rejected for row 2, whose cost is a sub-second walk and 13 one-time rewrites |
| 6. Replace the structure: stop claiming Windows, removing `bin/seal.cmd`, `bin/test.cmd` and the four `windows-latest` legs, and saying so in the README | Local mode's users, the company repositories where Windows is common, meet the defects nobody else sees. In the window design *Grounding* read, the leg found Windows-only failures at four pull requests, and the `O_EXCL` defence of `skills/implement/scripts/seal.py:578-607` would be proved by no run | Rejected. The premise that keeps the leg was checked: local mode stands (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*), and the claim stands in the wrappers, the legs and `README.md:375-379` |
| 7. Run the other platforms by `workflow_dispatch` before the broad run for every work item, not only where the risk is platform-specific | It departs from the owner's decision recorded in #943 (`b196fe9b`), that a one-platform defect in work nobody expected to be platform-specific is a stated limit; it adds one run of every leg per work item | Not built; `questions.md` Q2 holds it for the owner |
| 8. #103's second ask: a question in `skills/code-review/SKILL.md`'s axes for a defence resting on a POSIX-only guarantee | The same rule would stand in two files, contract rule 13 and the checklist, and the next edit would change one of them | Rejected. Contract rule 13 binds the proofer, and ten test files carry its cases |
| 9. #32's ask: a helper that runs each hook printing a path with `os.path` as `ntpath`, and a case per hook asserting one dialect | Three of the four hooks it names are gone, the fourth prints no path, and the one hook with a recorded failure already has its case (design *Grounding*). A case per hook with no catch on record is upkeep with nothing caught | Rejected |
| 10. Move #32's three link cases onto `tests/conftest.py#symlink_or_skip` in this work item | #1247's work item has made the same edit on `test/1247-three-link-cases-skip-on-windows-by-platform` (`b97741a0`), which merges first, so two branches would edit the same lines | Rejected; the cases are #1247's (design *Scope*, Out) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1, 2, 3 and 4 | `tests/test_censuses.py#Test_slash_in_join` cases S1 to S4, and S5 by `Test_judge`'s exemption cases through `_held`, as `frame/design.md` S5 allows, each refusing case shown red with only the guard it names removed (the census out of `CENSUSES`; the constant resolution out; the f-string check out); `Test_module::test_every_file_no_module_file_declares_meets_every_census` red before Scope item 3's rewrites and green after; the narrow run of each module file whose site Scope item 3 changed; S6's `git grep` | 087f6210 |

## Operational impact

None for a deployer: no shipped behaviour, command, dependency or
environment variable changes. The four shipped files Scope item 3 touches
return the same path on POSIX. A contributor's run of any module file now
refuses a `/` inside an `os.path.join` argument, with the repair in the
message. CI's jobs and legs are unchanged; the census runs inside the
existing pytest legs.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
