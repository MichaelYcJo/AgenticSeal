# Review round 1: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: 3f2f5a5d against release/v0.22.4

## Findings

### 1. The pull request that runs `seal mode local` with the checks kept fails the chain step, and the switch tells the person it passes

severity: must
location: `skills/code-review/scripts/chain_check.py:2162-2170`, `skills/code-review/scripts/chain_check.py:2220-2231`, `skills/implement/scripts/seal.py:2380-2384`, `tests/e2e/teammate/test_teammate_flow.py`, `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:199-203`
evidence: executed `python3 test_tmp_round1_probe.py`
verdict: open

Before this branch, `seal mode local` staged the workflow's removal in the
same change as the root's (`remove_workflow`, called from `switch`). So the
pull request that moved the root to local mode also deleted
`.github/workflows/hygiene.yml`, and GitHub ran no hygiene job on it. This
branch keeps the workflow through the switch, as `spec.md` *In* item 4 asks.
Now the hygiene job runs on that pull request, and its chain step fails it.

The frame meant this pull request to pass. `plan.md:64` (row H) refuses to
keep the base comparison where no root is in the tree, because "the pull
request that runs `seal mode local` with the workflow kept deletes every
`overview.md`, and the deletion arm fails it with no way out but removing the
checks in the same pull request". `spec.md:131-134` builds that into
`unverified_check.py#absent_root`. The chain step reads the same pull request
the other way. `chain_check.py#main` adds every deleted `routing.md` to
`declarations` (lines 2162 to 2170), and lines 2220 to 2231 refuse each one
git does not carry at HEAD, unless a settle removed it.

`spec.md:199-203` leaves `chain_check.py` unchanged on the premise that it
"already exit[s] 0 for a pull request that declares nothing (executed)". That
premise holds for a teammate's pull request. It does not hold for the switching
pull request, which the frame never ran through the chain step.

This round built the case. The base is a shared root with one work item
(`routing.md`, `spec.md`, an `overview.md` with an open row, a round record)
and the plugin's workflow installed by `seal pr-checks install`. The branch ran
`seal mode local` and committed it. Then the round ran the three steps with
the local root moved aside, as a CI checkout holds none, and
`GITHUB_HEAD_REF`, `GITHUB_EVENT_PATH` (not a draft) and `--baseline
origin/main` set. Results: `unverified_check.py` exit 0, naming the absent
root; `seal.py mode --check` exit 0; `chain_check.py` exit 1, with
`::error file=seal/specs/1790000000-work/routing.md,line=0::git does not carry
this file at HEAD: a declaration CI cannot open is not a declaration`.
Meanwhile `seal mode local` printed `.github/workflows/hygiene.yml stays: in
local mode its checks examine nothing and pass` (executed, same probe).

Who meets it: every person who installed the checks and later switches to
local mode while any work item is unsettled. The switch's own line tells them
the kept workflow passes. The pull request goes red, and the only ways out are
the two the frame refused: merge it red, or remove the checks in the same pull
request. `tests/e2e/teammate/test_teammate_flow.py` runs only a teammate's
README change, so nothing in the suite reaches this pull request.

The fix makes the chain step read the tree the way `absent_root` reads it.
With no root at HEAD, nothing is declared. The pull request then lands on the
existing `not declarations` branch, which prints the reason and still judges
the trailers. This also lets a pull request that deletes a shared root whole
pass every step. `plan.md:64` already accepts that for the unverified step,
because the diff shows the whole root leaving. `spec.md:199-203` has to be
amended to match. The precondition: `git ls-tree HEAD -- seal` prints "" where
HEAD carries no top-level `seal` entry, and `git()` answers None on a failure,
which keeps the declarations judged (it fails closed).

```python
    declarations = sorted(declarations)
    # The pull request that moves the root to local mode takes every
    # declaration out with the root. With no root at HEAD nothing is
    # declared, as `unverified_check.py#absent_root` reads it (#952).
    if declarations and git(root, "ls-tree", "HEAD", "--", routing.optin.HOME) == "":
        declarations = []
```

The fix also owes a case that is seen red first. In
`tests/e2e/teammate/test_teammate_flow.py`, one more case runs every step on
the base "a work item with an open row and a round record", with a head
commit that ran `seal mode local` (the plugin's workflow committed at the
base). And `spec.md:199-203` gets a sentence naming the switching pull
request as the shape that needs the chain step changed.

answer:

### 2. A workflow pinned to a release before this one stays through `seal mode local` and fails every later pull request, while the switch and the mode gate say it passes

severity: should
location: `skills/implement/scripts/seal.py:2380-2384`, `hooks/mode-gate.py:246-250`, `README.md:510-512`, `README.ko.md:503-506`, `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/changelog.md:8`
evidence: executed `python3 test_tmp_round1_probe.py`
verdict: open

This is the population `spec.md` S5 and `plan.md:77-83` (*Operational
impact*) describe: a repository bootstrapped before this change, with the
plugin's workflow pinned to an older release. The plan says such a workflow
keeps its pin "until a person moves the pin", and that the phase 1 fix reaches
its CI only then. The switch does not know that. It prints the same promise
whatever the pin is.

The round built the case. The repository has a `Mode` row reading `shared`,
and a committed workflow written from the template at `02ee12de` and pinned
to `v0.22.2`. `seal pr-checks` reported `pinned to v0.22.2`, and `seal mode
--check` exited 0. So far S5 holds. Then `seal mode local` left `.github/`
untouched and printed `.github/workflows/hygiene.yml stays: in local mode its
checks examine nothing and pass`. On a teammate's next pull request, the
unverified step from `02ee12de` (standing in for the pinned clone, since
`absent_root` is new in `846e25ad`) exited 2: `no such path: seal/specs/ —
and nothing under it at origin/main either`. The same step from this branch
exited 0.

Every workflow installed before this release is pinned to a release without
`absent_root`, so for those repositories the switch now leaves behind the
red-forever workflow that `remove_workflow` existed to take out. The mode
gate's *Local* option (`hooks/mode-gate.py:248-249`) makes the same promise,
and the gate fires only for a root with no `Mode` row, which is an old
bootstrap and so an old pin. `README.md:510-512` and `README.ko.md:503-506`
state it of any workflow left after a move to local. The changelog's
*Compatibility* line names the pin and never says that the switch to local is
where the old pin costs a red build. These are sentences a person acts on, and
the action they invite is to keep a workflow that fails.

The fix reads the pin where the line is printed, and qualifies the three
texts. `plugin_version()` answers "" where the version cannot be read, and the
line then takes the cautious branch.

```python
        kind, text = workflow_at(repo)
        if kind == "plugin":
            pin, here = pinned(text), "v" + (plugin_version() or "?")
            if pin == here:
                print(
                    f"  {WORKFLOW} stays: in local mode its checks examine nothing "
                    "and pass, and `seal pr-checks remove` takes them out"
                )
            else:
                print(
                    f"  {WORKFLOW} stays, pinned to {pin or 'no release'}, not {here}: "
                    "its steps are that release's, and one older than this fails "
                    f"every pull request with no {optin.HOME}/ in the tree. Move its "
                    "`--branch` line to this release, or run `seal pr-checks remove`"
                )
```

For `hooks/mode-gate.py:248-249`, the *Local* option reads: "A workflow file
already in the tree stays. Pinned to this release, its checks examine nothing
in this mode; pinned to an older one, they fail every pull request until its
`--branch` line moves or `seal pr-checks remove` takes it out." The two README
sentences say the same, and the changelog's *Compatibility* line adds: "A
switch to local mode leaves such a workflow in place, and pinned to an older
release it fails every pull request there until the pin moves or `seal
pr-checks remove` takes it out." Each new text gets a pin in the case that
holds its file (`tests/test_seal.py` `Test_switch`, `tests/test_mode_gate.py`,
`tests/test_first_setup_asks_once.py`), seen red first.

answer:

### 3. A case pins the red-forever sentences this spec retires, so the settle that applies the spec turns two cases red

severity: should
location: `tests/test_first_setup_asks_once.py:659-666`
evidence: executed `python3 test_tmp_round1_probe2.py`
verdict: open

`test_the_record_no_longer_says_the_checks_would_refuse` asserts that
`docs/one-root-by-lifetime.md` and its Korean edition carry `examined nothing`
or `아무것도 안 본 채`, and `red forever` or `영원히 빨간불` (lines 665 and
666). Each phrase stands only in the paragraph that the spec's two `change`
items at `spec.md` lines 294 and 343 replace. Their `to` texts say "examines
nothing" and "아무것도 보지 않습니다". The comment above the asserts (lines
662 to 664) states the old fact as current. A workflow left after a switch to
local "is red on every pull request", which phase 1 made false for a
workflow at this release.

The smith's account: phase 2's record says the case "fails at the settle that
applies this spec's `## Rule changes`" and that "that run has to change the
case in the same commit" (`phases/phase-2.md`, *The frame holds*). The round
confirmed the first half. It applied this spec's 14 items alone to the
documents at HEAD, which equal `02ee12de`'s, with
`rule_changes.py#replay`, and ran `bin/test` over the six modules that read
those documents. Both parameters of this case failed, and nothing else did
(2 failed, 84 passed).

The second half goes against the repository's practice. A settle is not a work
item (`skills/settle/SKILL.md` *A settle is not a work item*): it edits under
`seal no-work-item`, and `--apply` writes the documents only. A test edit
pushed onto it is a change nobody frames or reviews. The precedent is
`seal/specs/1792624592-the-release-seal-is-drawn-from-the-stamps-cells/plan.md:77`
(row A6). It met this exact choice for two `docs/` pins of a sentence its rule
changes rewrote, and chose "drop now". Kept, "the settle that applies this
spec meets two red cases, and `settle --apply` writes no sentence by hand".
Contract rule 19 asks the same of this branch: the case standing on the old
fact goes in the change that retires the fact. `spec.md` *Places*
(`spec.md:193`) lists this file's lines 71 to 91, 409 to 480 and 495 to 510,
and misses this case, which is how it was left.

The fix removes the two asserts and the comment that states the old fact. The
first assert, which still holds of both editions, stays.

```python
def test_the_record_no_longer_says_the_checks_would_refuse(parts, wrong):
    text = read(*parts)
    assert wrong not in text, "/".join(parts)
```

answer:

## Confirmations

confirms: none
No earlier round exists, so no fact was carried and every fact below was
established this round. The smith's account claims the plan's narrow set
exits 0. Executed: `bin/test tests/e2e/teammate tests/test_unverified_check.py
tests/test_mode_gate.py tests/test_first_setup_asks_once.py tests/test_seal.py
-q` in a clean clone at `3f2f5a5d` gave 788 passed, nothing skipped, so the
flow case ran its four bases here.

confirms: none
The 14 items of `spec.md` *Rule changes* parse with `rule_changes.py#parse`
and no error. Each one placed with `apply_op` against the documents at
`02ee12de`: every `from` appears once in its section, and the `add` finds its
section (executed, `python3 test_tmp_round1_probe.py`). `git diff --stat
02ee12de 3f2f5a5d -- docs` is empty, so the policy in force at the pull
request is `02ee12de`'s (executed).

confirms: none
No other unsettled spec under `seal/specs/` changes the sentences this spec
changes. The search was every spec's operations overlapping this spec's
places, by `rule_changes.py#overlapping`, plus a search of their `from` and
`to` texts for the red-forever, two-option and install wordings (executed).
`1792628098-tests-rebuilt-one-file-per-module` changes the `check:` lines of
the same sections. Replayed with nothing held, its operations on these four
files and then this spec's all apply (executed,
`python3 test_tmp_round1_probe3.py`). So nothing has the shape of #1025
between the two. The full replay in merge order holds this spec anyway, by
waiting, as row 2 of `## Not judged` says.

confirms: none
`seal pr-checks` refuses every near miss the round tried, at exit 2 with
nothing written under `.github/`. Executed, 18 argument lists: `Install`,
`INSTALL`, `instal`, `install ` and ` install` (a space inside the
argument), `remov`, `Remove`, `rm`, `--install`, `add`, `install remove`,
`install x`, `uninstall` and `--check` after `pr-checks`, and `pr-check`,
`pr_checks`, `prchecks` and `checks` as the subcommand. The argparse
`choices=("install", "remove")` is at `skills/implement/scripts/seal.py` in
`main` (read).

confirms: none
Every state `spec.md:87-111` lists answers as written (executed,
`python3 test_tmp_round1_probe.py`). The report, nothing there: exit 0, *not
installed*. Install: exit 0, staged (`A` in porcelain). Install again: exit
0, *already this plugin's, pinned to v0.22.3*. Remove, nothing there: exit
0. An untracked file identical to what install writes: removed, exit 0. An
untracked file that differs: exit 1, kept. A symbolic link, a file with
invalid UTF-8 bytes, and a mode-000 file: the report exits 0 naming the
reason, and install and remove exit 1 with the file kept. Install with no
root, with only a local root, and with `seal` a plain file: exit 1, nothing
under `.github/`.

confirms: none
`seal mode` writes and removes nothing under `.github/`. Executed: `seal mode
local` and then `seal mode shared` over a committed workflow left `git status
--porcelain -- .github` empty both times. `git grep -n -e
'install_workflow(' -e 'remove_workflow('` over `*.py` finds the two
definitions, the two calls in `seal.py#pr_checks` and the cases in
`tests/test_seal.py`, and no other caller, `hooks/` included (executed). So
S5's "no shipped code writes the workflow outside `seal pr-checks install`"
holds.

confirms: none
An upgraded shared repository with a `Mode` row and a workflow pinned to
`v0.22.2` reads correctly with nothing asked again, until it switches to
local. Executed: `seal pr-checks` reports `pinned to v0.22.2`, and `seal mode
--check` exits 0. The mode gate's silence on a declared row is
`tests/test_mode_gate.py`
`Test_main::test_accepts_a_root_whose_config_answers_or_refuses_the_mode`
(read, and the module ran green above). What breaks after the switch is
finding 2.

confirms: none
The smith reported one commit chained after `cd` and `git add` in one shell
command. The commits `846e25ad`, `4d019bcc`, `231ebb1c`, `ce6b9afe`,
`45bdd069` and `3f2f5a5d` each touch only the files their phase names. Each
carries `SpecSeal-Routing: 1792976216-the-records-and-the-pr-checks-are-two-answers`,
with author and committer both the repository's identity (executed, `git log`
and `git show --stat`). So the chained command changed nothing in the tree,
and it is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the flow case runs or skips on the Windows legs of `.github/workflows/test.yml` (`questions.md` Q2) | `tests/e2e/teammate/test_teammate_flow.py` | the pull request's CI run on `windows-latest`, read by the orchestrator |
| The settle holds this spec behind specs refused for reasons outside this branch. The full merge-order replay refuses `1792619408-an-automation-run-stops-at-the-parity-arm` (#1025's instance), and with that one left out it refuses `1792627930-the-section-sign-is-still-syntax`, whose `from` is not in `docs/the-review-record.md` *The guarantee*. `1792628098` waits on them, and this spec waits on `1792628098` at *Shared or local* (executed, both probes). Whether an issue tracks the second stale `from` was not read | `seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md:279` | the orchestrator |
| `seal pr-checks install` writes the workflow where `seal/` is a symbolic link to a directory outside the tree (executed: exit 0), though git commits the link and not the records the checks read. Whether that layout is a limit to state or a refusal to add was not judged | `skills/implement/scripts/seal.py:1849-1856` | the framer |
| The full suite, the repository-wide lint and the typecheck: not run, as contract rule 2 assigns them to the broad gate after the rounds settle; the smith's suite stands `unverified` | the branch | the orchestrator, by `broad-gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/e2e/teammate tests/test_unverified_check.py tests/test_mode_gate.py tests/test_first_setup_asks_once.py tests/test_seal.py -q`, in a clone at `3f2f5a5d` | exit 0, 788 passed |
| `python3 test_tmp_round1_probe.py`, in the clone: the rule changes parsed and placed at `02ee12de`, the overlap search over every unsettled spec, the merge-order replay, the `seal pr-checks` near misses and states, the upgraded repository with a `v0.22.2` pin, and the three steps on the pull request that ran `seal mode local` | all 14 items placed; no spec changes the same sentences; 18 near misses exit 2, nothing written; every state as `spec.md` says; an old-pinned unverified step exits 2 after the switch (finding 2); on the switching pull request the chain step exits 1 and the other two exit 0 (finding 1) |
| `python3 test_tmp_round1_probe2.py`, in the clone: this spec's items alone applied to `docs/`, then six modules that read them run with `bin/test`; the replay with #1025's spec left out | `test_the_record_no_longer_says_the_checks_would_refuse` fails on both parameters, 84 others pass (finding 3); the replay still holds this spec behind `1792627930` and `1792628098` |
| `python3 test_tmp_round1_probe3.py`, in the clone: `1792628098`'s operations on this spec's four files, then this spec's, replayed with nothing held | both apply, nothing refused |

The three probe files and the scratch repositories they built were deleted
after their one run, and `git checkout HEAD -- docs` restored the clone's
documents. `git status --porcelain` in the clone was empty afterwards
(executed).
