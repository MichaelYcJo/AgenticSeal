# Phase 3: 1793843890-the-directory-tracks-a-dist-branch

## What this phase found

**The frame holds against the tree for Scope 5, 6 and 7, with two exceptions below.** At `e1ee1f36`, `.github/workflows/publish-release.yml`'s `publish` job wrote the output `tag` from the tag step, and its `seal` job checked out with `persist-credentials: false`. `.github/scripts/plugin_directory_check.py#is_ancestor`, `#line` and the `--ref` default of `main` stood at the lines `frame/plan.md` *Technical context* gives. `.github/scripts/tag_release.py` and `tests/github/test_tag_release.py` were the pattern the row names (read). `frame/questions.md` Q1 is open, and the build takes its default, the GitHub Actions bot.

**Exception 1, a frame statement HEAD contradicts.** `frame/plan.md` *Technical context* gives as its second failure scenario that a push to `dist` by hand gets the next release's push refused as a non-fast-forward. The script reads `dist`'s tip from `origin` at each run, so the next release builds its commit on the commit pushed by hand and is not refused. A push is refused only where `dist` moves between the run's `ls-remote` and its push, which D4 below holds. A commit pushed by hand therefore stays in `dist`'s history, and the next release's tree replaces its tree. The hand-back names this for the orchestrator, because this phase does not write `frame/plan.md` beyond its Status cell.

**Exception 2, a sentence the rule changes do not reach.** `docs/releasing/branch-and-release.md` *Cutting a release* says that `plugin_directory_check.py` reports whether a pinned commit "is on `main`". At HEAD the check reads the pin against `main` and `origin/dist`. `frame/design.md` *Rule changes* adds a paragraph to that section and changes no sentence in it. The hand-back names this for the orchestrator to fold into *Rule changes*.

**How `dist_branch.py` builds the tree.** The script reads the tag into an index of its own (`GIT_INDEX_FILE` set to a file in a temporary directory). It removes from that index every path that `git archive --format=tar <tag>` does not list, through `update-index --force-remove -z --stdin`, and writes the tree with `write-tree`. Python's `tarfile` reads the archive's listing. This is the second spelling `frame/design.md` *Grounding* probed, and the probe gave the same tree as the first. The first spelling was not taken. It extracts the archive and runs `git --work-tree=<dir> add -A`, and that would read the extracted `.gitignore` and could leave a tracked file out. The spelling taken keeps each kept file's mode and object from the tag. Judged against `frame/design.md` *Data & interfaces*, the `dist_branch.py` item. That item says the script "builds the tree of `git archive`", and the tree built is the same tree.

**The rest of the script, each decision with its grounds:**

- The tip is read with `git ls-remote --heads origin refs/heads/dist`. Where it names a commit, `git fetch -q origin refs/heads/dist` brings that commit's objects. The new commit names the tip as its one parent. Where `origin` has no `dist`, the commit has no parent. This follows *Data & interfaces*.
- Where the tip's tree is the tree built, nothing is committed or pushed. The run prints `nothing to push: dist's tip <commit> already holds the archive of <tag>` and exits 0.
- The message's first line is `dist: <tag>`. Its body is ``The tree of `git archive <tag>`, the release tagged at <commit>.``
- The push is `git push origin <commit>:refs/heads/dist`. It has no force flag and no `+` refspec.
- `DRY_RUN` builds the tree, prints `would push a commit of tree <tree> for <tag> ...`, and commits and pushes nothing. `tag_release.py`'s dry run also creates nothing.
- Exit 2 where `TAG` is empty. *Data & interfaces* names no exit for that case. `plugin_directory_check.py` beside it gives exit 2 to a malformed argument, which is also the caller's mistake.
- Every git failure is caught as one exception and printed as `nothing was pushed for <tag>: git <command> failed: <git's error>`, with exit 1. A tag the checkout cannot resolve is one of these failures.
- Four choices were dropped before mutation, because no case could see them and none answered a case the workflow meets. They were a `refs/tags/` prefix on the tag's lookup, `--no-tags` on the fetch, a filter of directory entries from the archive's listing (`ls-files` lists no directory), and a guard that skipped `update-index` when nothing was removed. Commit `b6b72d54` drops them.
- The limit `frame/plan.md` *Technical context* names, a tag pushed by hand for an older version, stands in the script's docstring.

**The identity is in the workflow, not the script.** The job's step sets `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME` and `GIT_COMMITTER_EMAIL` to the GitHub Actions bot. The script writes the commit with whatever identity git reads. So `frame/questions.md` Q1 has one place to change, the job's environment. Its value is Q1's default, the bot's own noreply address, which the spawn prompt's rule against writing a real address was read as not reaching. That address is not a person's, and Q1 names it as the default.

**The `dist` job** follows *Data & interfaces*. It has `needs: publish`, `if: needs.publish.outputs.tag != ''` and `actions/checkout@v4` with `fetch-depth: 0`. The checkout's credentials persist, and nothing in the job carries `continue-on-error`. Its step runs `python3 .github/scripts/dist_branch.py` with `TAG: ${{ needs.publish.outputs.tag }}`. The workflow's header comment gained a paragraph saying what the job does and why a red run is the right outcome. The comment above `permissions:` counted the writes the workflow makes, and it now counts five: the commit on `dist` is the fifth. The docstring of `tests/behaviour/test_a_release_publishes_its_note.py#test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit` counts the same five now.

**`plugin_directory_check.py` reads a pin against two refs.** `REFS = ("main", "origin/dist")` is the default. A `--ref` given on the command line is the one ref compared. `line` takes the refs as its trailing positional arguments, `*refs`. So every existing call that passes `"main"` alone still reads one ref, and none was edited. The line names each ref that holds the pin: `Reachable from origin/dist.` It says `NOT reachable from main or origin/dist.` only where every ref answered and none holds the pin. That sentence names "a rewritten `dist` or a squashed release branch". Where no ref holds the pin and one ref cannot answer, the line says the answer is unknown, because a ref this clone lacks is not a ref that lacks the commit. The header line names the refs: `plugin 'agentic', against main and origin/dist`. The docstring's `reachable` line, its usage lines and `tests/github/test_plugin_directory_check.py`'s A6 line say the same. Judged against `frame/design.md` *Data & interfaces*, the `plugin_directory_check.py` item, and *Removes*, its third row.

**New cases, each in its group.** `bin/seal layout --pairs` names no pair in any module this phase writes (executed, exit 0).

- `tests/github/test_dist_branch.py` is new, under the name rule change R1's `check:` line gives. It holds D1 to D6, seven cases in `Test_main`, and `test_census`. Each case drives a real repository in `tmp_path` whose `origin` is a bare repository beside it, so nothing is pushed anywhere else. D2 and D3 build the earlier tip from a second clone. That way the run under test has to fetch the tip, as a fresh checkout would. D4 moves `dist` from inside the run, between its read of the tip and its push, by wrapping the module's `git`. It records every call. It asserts the push was refused, that `dist` kept the other writer's commit, and that no `push` or `fetch` carried `--force`, `-f` or a `+` refspec. D5 also holds that the checkout's own index is left as it was.
- `tests/behaviour/test_a_release_publishes_its_note.py#test_the_dist_job_adds_the_release_to_dist_and_goes_red_where_it_cannot` reads the `dist` job of the comment-free workflow with the module's `job` and `steps` helpers.
- `tests/github/test_plugin_directory_check.py` gained `two_refs`, a fixture repository whose `main` and `refs/remotes/origin/dist` share no commit, and two cases in `Test_module`. One reads `line` against both refs: a pin on each ref, a pin on neither, and a ref the clone lacks. The other runs `main` with and without `--ref`.
- `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#LISTS_A_FIXTURE` gained two rows. One is phase 1's `tests/evals/test_noninferiority.py#test_leaves_the_repository_s_own_index_as_it_was`, which `frame/plan.md` *Judgments of the run* gave this phase. The other is `tests/github/test_dist_branch.py#entries`, which runs `ls-tree -r` on a fixture commit. No other new case runs `ls-files`, `ls-tree` or `--name-only`.

**Seen red** (executed).

- `bin/test tests/github/test_dist_branch.py -q -p no:xdist` against no script ended 8 failed. Each of the seven `Test_main` cases failed at loading the script, after its fixture had built, and `test_census` failed on the missing file.
- The workflow case failed against the workflow with no `dist` job, with `ValueError: '  dist:' is not in list` from `job`.
- Against the one-ref reader, the `line` case failed with `TypeError: line() takes 7 positional arguments but 8 were given`. The `main` case failed on its assertion, `against main and origin/dist`, with the run printing `NOT reachable from main`.
- Before the two rows went in, `bin/test tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py -q -p no:xdist` ended 2 failed. It named both scopes as unclassified. With the rows in, it ended 9 passed.
- D5's index assertion was shown red by m2 below.

**Mutation** (executed). One `bin/seal mutate` per break, with every target committed before the runs, at `b6b72d54`. The script's cases were `bin/test tests/github/test_dist_branch.py -q -p no:xdist`. The check's were `bin/test tests/github/test_plugin_directory_check.py -q -p no:xdist`, and the workflow's were `bin/test tests/behaviour/test_a_release_publishes_its_note.py -q -p no:xdist -k dist_job`.

- m1, no path removed from the index: red, D1, on its tree assertion.
- m2, `git` setting no `GIT_INDEX_FILE`: red, D5, on the checkout's index.
- m3, no parent: red, D2, because the push was refused.
- m4, the fetch removed: red, D2 and D3, because `rev-parse <tip>^{tree}` failed.
- m5, the no-op check made `if False:`: red, D3.
- m6, `git push --force` in place of the push: red, D4, which failed at `assert mod.main() == 1` because the forced push succeeded. This is the plan row's red for the no-force case. The assertion on the flags D4 recorded comes after that line, and no break made it fail alone.
- m7, the dry run's branch made `if False:`: red, D5, because `dist` was pushed.
- m8, the subject `dist v1.2.3`: red, D2.
- m9, the body without the tag's commit: red, D2.
- m10, exit 0 for an empty `TAG`: red, D6.
- m11, the guard for a remote with no `dist` removed: red, D1 to D4 among the failures read, because the fetch of a `dist` the remote lacks failed.
- m12, exit 0 for a git failure: red, D4 and D6.
- p1, `REFS = ("main",)`: red, the `main` case.
- p2, the holders replaced by the first ref: red, both new cases.
- p3, the unknown branch made `elif False:`: red, the new `line` case and `test_a_commit_this_clone_does_not_have_is_not_called_unreachable`.
- p4, the old "NOT reachable" sentence: red, the `line` case.
- p5, `--ref` ignored: red, the `main` case.
- p6, "NOT reachable" naming the first ref alone: red, the `line` case.
- w1, the job's `if:` on `created == 'true'`: red.
- w2, the job's checkout without `fetch-depth: 0`: red.
- w3, `continue-on-error: true` on the job: red.
- w4, `TAG` removed from the step: red.
- w5, the committer's name `ci`: red.

Result: 23 breaks, 23 red, none survived.

**Scope 7, the smoke run from the archive of HEAD** (executed). `git archive b6b72d54 | tar -x` wrote 187 files under the scratch directory. The archive's top-level entries are those `frame/design.md` *Grounding* lists, and no `tests/`, `evals/`, `seal/`, `.test_durations` or `CLAUDE.md` is among them. The scratch repository was opted in by hand. It got `templates/setup/seal-README.md` as `seal/README.md`, a `seal/config.md` with `Mode shared` and `Broad gate true`, and a copy of this work item under `seal/threads/`. `refs/remotes/origin/main` was set to its HEAD. Each command below ran from the scratch repository with the archive's `bin/seal`, and then with the worktree's.

- `python3 <archive>/hooks/dispatch.py session-core`, with `CLAUDE_PLUGIN_ROOT` set to the archive and a `SessionStart` payload, exited 0. It printed `AgenticSeal core from <archive>/skills/core/SKILL.md, plugin 0.32.2, sha256 0f9785...`, then the file below its front matter. The hash is the archive's file's (`shasum -a 256`). The `session-start` group exited 0 and printed nothing.
- `seal gate --preflight --base HEAD~2` exited 0 with `PREFLIGHT PASSED`.
- `seal rules --check` exited 0 with `all 0 check lines in 0 rule files hold.`
- `seal settle`, the dry run, exited 0. It read the copied work item, `1 work item`, `3 groups; 4 open rows in 1 record`.
- Each output from the archive matched the worktree's, with the root's path replaced, except the gate's temporary directory name. A `grep -i` for `no such file`, `FileNotFoundError`, `Traceback`, `cannot be read` and `missing` over the three outputs found only a sentence of the settle's own help text.

The first two attempts exited 2. zsh passed each command line as one argument, and then the scratch repository had no `Broad gate` row and no `origin/main`. Each was the same from the archive and from the worktree. The run did not install the plugin from `@dist` or start a session. That is the owner's act after the release, in `frame/plan.md` *Operational impact*.

**`dist_branch.py` over this repository's tree** (executed). A `git clone --no-local` of the worktree was made under the scratch directory, with `b6b72d54` tagged `vprobe` and `origin` set to a bare repository there. `TAG=vprobe python3 .github/scripts/dist_branch.py` exited 0 and pushed a first commit of `dist`. A second run exited 0 with `nothing to push`. `dist`'s tree listed 187 files, and its list of paths equalled `git archive vprobe | tar -t`'s files (`diff`, exit 0). The commit's message read `dist: vprobe`, with the body naming `b6b72d54`.

**The phase boundary** (executed). One `bin/test ... -q` command ran 107 modules at `b6b72d54` and ended 5759 passed, 14 skipped, exit 0. The list came from `git grep -l -E` under `tests/` for each changed file's name, `.github/`, `workflows`, `"scripts"`, `ls-files`, `git_listing`, `changelog`, `trail/phases`, `gaps.md`, `plan.md`, `rglob` and `os.walk`. `tests/conftest.py`, `tests/censuses.py` and the two oracle modules were left out because they hold no cases. The two shrunken-corpus failures that phase 2 recorded do not occur at this commit.

**The commit after the runs.** `6ee044c9` changes only text: `dist_branch.py`'s docstring, its line for an empty `TAG` (now `TAG is empty, so there is no release to add to dist`), and two docstrings and one assertion's spelling in the new cases. The workflow case's docstring had cited `frame/questions.md` Q1, a record the settle removes, and it now names the bot alone. No case reads the changed line. After it, the four modules of this phase's cases ran in one `bin/test ... -q` command, 41 passed, exit 0, and `ruff check` and `ruff format --check` passed over the three files (executed). The mutation, smoke and boundary runs above were made at `b6b72d54` and were not repeated.

**Other statements of what this phase changed** (a sample, by wording). `git grep -n -i -E` for `ancestor of main`, `NOT reachable`, `against main`, `reachable from` and `--ref` was run outside `seal/threads/` and `.test_durations`. It found `docs/releasing/release-checklist.md` *6. After the merge*, "whether that commit is an ancestor of `main`", which `frame/design.md` *Rule changes* changes at the settle. The other hits are about other commands. A second `git grep -i` was run on `docs/`, `CONTRIBUTING.md`, both READMEs, `skills/`, `agents/` and `templates/`, for the word `dist`, for `export-ignore` and for `git archive`. It found one hit, `dist` in `skills/verify/scripts/unverified_check.py#SKIP_DIRS`, a directory name a walk skips, which says nothing of the branch. Exception 2 above came from reading *Cutting a release* whole. A statement in another spelling escapes these searches.
