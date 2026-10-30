# Review round 8: 1793273065-the-core-reaches-no-users-repository

target: e2fbae86, fixes 51e582c2..e2fbae86

This is a verifying round, round 3 of the count after the reframe (round 6
was round 1, round 7 round 2). It reads the diff of round 7's fix pass:
the fix commit `f1217ac9`, the fix pass's record commit `0f8ccab7`, and
`e2fbae86`, which the orchestrator added to the target and which replaces
`.test_durations` with a CI artifact. `git diff --name-only 51e582c2
e2fbae86` names four paths: `.test_durations`, `round-7.md`,
`tests/censuses.py` and `tests/test_censuses.py` (executed). None of them
holds a unit of round 6 findings 1 to 3, which round 7 confirmed, so this
round does not reopen them.

Carried from round 7 and not searched again: `tests/censuses.py`
*real_identifiers* as the census that holds `CONTRIBUTING.md` *House rules*
**No real identifiers**, and `evals/scripts/noninferiority.py#masked` as
its other reader. Carried from round 5: how a durations refresh is judged,
the artifact compared byte for byte and the file's keys read against a
collection under the pytest CI installs. Re-established this round: every
verdict below, the census over the tracked tree, the case red against
round 7's pattern, and the collection at both ends of the range (executed,
*Probes*).

## Findings

This round opens no finding.

## Confirmations

confirms: round-7#1
The finding asked the census to read a user path spelled as a projects
directory's slug, the home directory's spelling included, and to state in
the comment what its reading of the name implies. Both hold.
`tests/censuses.py:911` is `"-" + r"Users-([\w.]+)"`, round 7's
paste-ready pattern, and `:903-910` is round 7's comment word for word
(read). The pattern now ends where the name's word characters and dots
end, so the character after the name no longer decides anything. Called
through `refused_user_paths`, it reads `somebody` from a repository slug,
from a home-directory slug followed by `/`, a backtick, a space or the end
of the line, and from the same slug in a side's JSON form ahead of `\n`
(executed, *Probes*). The fixture user `x` passes in each of those
spellings, and so does a longer name whose first part, up to a dash, is
`x`. A placeholder `-Users-<name>`, with or without a repository after it,
and a pattern `` `-Users-[A-Za-z]` `` match nothing. A name that opens
with `x` and goes on in word characters, such as `xavier`, is read whole
and refused (executed, *Probes*).

The comment states the precondition's consequences as the finding asked.
It says the name is read up to the first character that is neither a word
character nor a dot. It then says a name holding a dash, or a dot the slug
spells as a dash, is read by its first part and refused unless that part
is the fixture user's. The probe agrees on each point. A raw dotted name
is read whole, a dashed name by its first part, and a dashed name whose
first part is `x` passes (executed, *Probes*). The docstring of
`refused_user_paths` (`:937-945`) still describes both arms.

The extended case pins the fix. With `:911` edited back to round 7's
pattern in this round's clone, the case fails at exit 1. Line 1 is refused
by a match that ends in a dash, where the case expects the slug without
it, and line 4, the home-directory session, is not refused at all. With
the edit undone, the case passes (executed, *Probes*). The case's new home
fixture line, `-Users-x/`, holds the fixture user, so the case also shows
that dropping the dash lets `x` through in the home spelling. The fix
pass's account claimed the same red run, line 1 refused and line 4 not,
and 176 cases passing in `tests/test_censuses.py`. This round's red run
gives the same lines, and its narrow run passed the module (executed,
*Probes*).

No legitimate line is refused. The census over the 626 tracked files at
`e2fbae86` refuses no line, as it refused none with round 7's pattern
(executed, *Probes*). `git grep -n -E -- "-Users-[A-Za-z0-9_.]+"` finds 14
lines outside `.test_durations` and none in it, and every match is
`-Users-x` (executed), as the fix pass's answer claimed.
`evals/scripts/noninferiority.py#masked` replaces the shorter match by
`/Users/x/`. A repository slug therefore keeps the dash after the name,
so a slug naming `somebody` before `repo` becomes `/Users/x/-repo` where
it was `/Users/x/repo`. The census refuses nothing in the masked text (executed,
*Probes*). A match still starts at a dash and now ends at a word
character or dot, and neither is part of a JSON escape, so `apart` is not
reached by the arm. `tests/evals/test_noninferiority.py` passes (executed,
*Probes*).

confirms: none
`e2fbae86` is the `test-durations` artifact of CI run 41006808781 and
nothing else. `git show e2fbae86 --name-status` names one path,
`.test_durations` (executed). The run is the branch's own. `gh run view`
gives head `044da6e6`, branch `feat/1177-the-core-reaches-no-users-repository`,
workflow `tests`, conclusion success, and a `durations` job that succeeded
with every pytest leg (executed, *Probes*). The downloaded artifact and
`git show e2fbae86:.test_durations` are 901,701 bytes each, `cmp` exits
0, and the file holds no carriage return (executed, *Probes*).

confirms: none
The file prices every case id the tree collects and names none the tree no
longer has. The run's legs install pytest 9.2.0, pytest-split 0.11.0 and
pytest-xdist 3.8.0 (executed, the run's log). Under those versions in a
scratch environment, `--collect-only` over `tests` collects 6,194 unique
ids at `e2fbae86` and the same 6,194 at `044da6e6` (executed, *Probes*).
The file holds 6,194 entries. No collected id is unpriced and no entry is
gone. Against the file at `0f8ccab7`, which held 6,146 entries, the new
one adds 73 and drops 25 (executed, *Probes*). These are the
orchestrator's figures. The commits after `044da6e6` add no case id. The
two collections are one set, and `git diff 044da6e6 e2fbae86 -- tests`
adds no `def` line and no `parametrize` (executed). `f1217ac9` extends
`test_refuses_a_user_path_spelled_as_a_projects_directorys_slug`, an id
the file prices. `bin/test -q tests -k test_the_durations_file_prices_the_suite`
passes (executed, *Probes*).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `e2fbae86`. Contract rule 2 keeps them from this round, and `trail/gate.md` and `guarantee.md` are stale against this range | the tree | the orchestrator, through `seal gate` |
| Whether the shards balance with the refreshed file in place. The file bounds age, not imbalance, and only a CI run on `e2fbae86` shows the legs' times | the next `tests` run | the orchestrator |
| Whether the core's three rewritten sentences need S11 run again, carried from round 7. `gaps.md` *Not verified* records the owner's decision of 2026-10-30 not to run the proofer's and crafter's sides | `skills/core/SKILL.md` | the orchestrator |
| Whether the real user path round 6 finding 4 removed from the tree must also leave the pushed history, carried from round 7. `4d436388` added it, and the commits PR #1186 holds keep it until the squash | the remote's refs for PR #1186 | the owner |
| `frame/questions.md` Q2 and Q3, carried from round 7 | `frame/questions.md` | the owner after the release (Q2); anyone with an `ANTHROPIC_API_KEY` (Q3) |

## Probes

| Command | Result |
|---|---|
| `python3 -I -c` calling `censuses.real_identifiers` on every file `git ls-files` lists at `e2fbae86`, then with `SLUG_USER_RE` rebound to round 7's `"-" + r"Users-([\w.]+)-"` in the same process | 626 files, no refusal either way |
| `refused_user_paths` in the same process on a repository slug and a home-directory slug ending in `/`, a backtick, a space, the end of the line and a JSON `\n`, each with a name built as `'-' + 'Users-somebody'`; on `john.doe`, `john-doe-repo`, `xavier-repo`, `x-ray-repo`; on `-Users-x` in four endings; on the placeholder and pattern lines | the name `somebody` read in every spelling; `john.doe` read whole, `john` read from `john-doe-repo`, `xavier` read whole, each refused; every `x` line, `x-ray`, the placeholders and the pattern return nothing |
| `noninferiority.masked` on the same slug lines, then `refused_user_paths` on its output | the slug becomes `/Users/x/`, a repository slug keeping its dash (`/Users/x/-Documents-GitHub-repo`); nothing refused |
| `tests/censuses.py:911` edited back to round 7's pattern with the `Edit` tool in this round's clone, `bin/test -q -p no:xdist tests/test_censuses.py -k projects_directorys_slug`, then the edit undone the same way | exit 1, 1 failed: line 1 refused by a match ending in a dash, line 4 not refused; `git status --short` empty after |
| `bin/test -q tests/test_censuses.py tests/evals/test_noninferiority.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -rs` in the clone at `e2fbae86` | exit 0, 446 passed, 2 skipped: the shards module's `:347` and `:487`, each "the suite was not collected" |
| `bin/test -q tests -k test_the_durations_file_prices_the_suite` in the clone | exit 0, 1 passed |
| `uvx ruff check` and `uvx ruff format --check` over `tests/censuses.py` and `tests/test_censuses.py` | exit 0 each |
| `gh run view 41006808781 --json headSha,headBranch,event,workflowName,conclusion,jobs`; the `Successfully installed` lines of `gh run view 41006808781 --log` | head `044da6e6`, branch `feat/1177-the-core-reaches-no-users-repository`, `pull_request`, `tests`, success; every pytest leg and `durations` success, `release-report` skipped; pytest 9.2.0, pytest-split 0.11.0, pytest-xdist 3.8.0, markdown-it-py 4.2.0, cmarkgfm 2025.10.22 |
| `gh run download 41006808781 -n test-durations -D <scratch dir>`, then `cmp` against `git show e2fbae86:.test_durations`; `grep -c` for a carriage return | download exit 0; 901,701 bytes each; `cmp` exit 0; 0 carriage returns |
| `uv venv` in the round's scratch directory with the five versions above; `python -m pytest tests -q -p no:xdist -p no:cacheprovider --collect-only` at `e2fbae86` and at `044da6e6`; `python3 -I` reading the ids against the file at `e2fbae86` and at `0f8ccab7` | 6,194 collected at each commit, one set, 6,194 unique; 6,194 entries, 0 unpriced, 0 gone; 6,146 entries before, 73 added, 25 dropped. The environment, the artifact and the clone were removed afterwards |
