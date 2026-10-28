# Overview: 1793188384-the-release-notes-are-kept-twice

## Why this work exists

A change's release note was kept three times, in its fragment, in the gathered `changelog/X.Y.Z.md` and in the GitHub Release, and two copies had already drifted; the note is now built at the tag from the fragments, and the gathered files and the gather are gone.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Readers of the gather that `## Removes` does not list | `## Removes` lists the gather's mentions it found. The build found four more that state the removed step or count it: `CONTRIBUTING.md` *What a contribution is asked for*, its paragraph ("The version and changelog steps") and its `changelog.md` fragment row; `skills/verify/orchestration.md:91-94` ("Two steps ... one runs a script under `.github/scripts/`"); four cases of `tests/behaviour/test_the_gate_names_every_step_ci_runs.py`, which count 7 steps and 3 that run only into `main`; and `hygiene.yml`'s milestone-step comment ("like the version and changelog steps") | Each is rewritten in phase 3, the phase that removes the step | `frame/design.md` *Grounding*: "Every case, comment, census entry and sentence outside the policy root that names `changelog/`, `CHANGELOG.md` or the gather is removed or re-pointed in the phase that removes what it names." |
| `release_body`'s signature | *Data & interfaces*: "`release_body` takes the theme and the rendered fragments where it takes the gathered section today, and drops the trailing link." | `release_body(theme, rendered, pulls, owner)`. `repo` and `tag` fed only the link, so they went with it, and `tests/github/test_release_seal.py#note`'s one call changed | Spec silent on the two parameters the link alone read |
| S1's history | S1 names two fragments added after `v1.2.2`, one removed before `v1.2.3` | S1 also adds, in the settle's commit, a fragment with the removed one's text and an empty fragment | `seal mutate` showed nothing pinned `--no-renames` or the empty skip, both stated in *Data & interfaces* |

## Not verified

| Item | Who must answer |
|---|---|
| Whether the tag's job can list the milestones under `contents: write` alone (`frame/questions.md` Q3, default (a)) | the orchestrator, reading the log of the tag run of the release carrying this work |
| The full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, at the broad gate |
| S11: every released version's note holds its file after the republish | the orchestrator, in phase 5 |
| Step 3 of the `update` skill run by a session updating across a real release | the first person to update to the release carrying this work |

## Not done

`skills/implement/orchestration.md:530` and `:578` still state the gather, and so do `:538` and `:541` ("one fragment per work item that a release gathers", "running the gather"). The file is #1041's work item's, and `frame/questions.md` Q4's default (a) leaves it alone; the orchestrator names the sentences in the pull request body.

`tests/behaviour/test_first_setup_asks_once.py` still passes `fold_ledger` to `test_the_rows_that_read_this_repository_do_not_travel`. That script left the tree in #950, so the parameter reads nothing, the same way `gather_changelog` would have. It is #950's leftover, not this work's.

## Fed back into the spec

none
