# Phase 1: 1793843890-the-directory-tracks-a-dist-branch

## What this phase found

**The frame holds against the tree for Scope 4.** `git diff --stat efd8edec 1107baaf` lists only the three frame files, so the code at the frame commit is the code the frame read (executed). At `efd8edec`, `.github/workflows/test.yml` line 280 holds `git archive "$tag" | tar -x -C "$RUNNER_TEMP/at"`, `evals/scripts/noninferiority.py#extract` archives REV's PATHS and extracts them with `filter="data"`, `run_side` calls it at `--rev` and at `--suite-rev`, `tests/evals/test_noninferiority.py#Test_extract::test_refuses_a_rev_git_does_not_resolve` matches `^git archive`, and `.github/scripts/release_report.py` reads `.test_durations` and `CLAUDE.md` under `--at` (read).

**The `release-report` job checks the tag out as a detached worktree.** The step's `mkdir` and `git archive` lines became `git worktree add --detach "$RUNNER_TEMP/at" "$tag"`, the first spelling `frame/design.md` *Grounding* probed. It is one line and needs no index file. The worktree leaves a `.git` file at the root of `$RUNNER_TEMP/at`. `release_report.py`'s one glob reads agent and document patterns, and the table it printed over the worktree matched, byte for byte, the table over a plain `checkout-index` of the same tag (executed, below). Judged against `frame/design.md` *Data & interfaces*, the `release-report` item.

**`extract` reads REV into an index of its own and checks PATHS out from it.** The commands are `git read-tree REV`, then `git ls-files -z --error-unmatch -- PATHS`, then `git checkout-index -z --stdin --prefix=<INTO>/`. Each runs under `GIT_INDEX_FILE` set to a file in a temporary directory. `git_bytes` gained two keywords for this, `index=` and `stdin=`. A worktree was not used here, because `run_side` writes the suite into a directory that already holds the plugin tree, and a worktree needs an empty directory. Judged against `frame/design.md` *Data & interfaces*, the `extract` item, and *Scope* 4.

**Departures from the frame in `extract`, each with its grounds:**

- The refusal of a member that would land outside INTO is now git's. `read-tree` refuses a tree entry that leaves the index's root. A probe built a commit whose tree holds one blob named `..` (`git hash-object -t tree --literally`, then `git commit-tree`). `extract` of that commit stopped with `git read-tree <commit>: error: invalid path '..'` and wrote nothing (executed). No case pins this refusal, and no case pinned the `filter="data"` one before it. Contract rule 13 applies: the defence is git's guarantee, and this build has no second refusal behind it.
- `tarfile`'s `data` filter also refused a symlink whose target leaves INTO. `checkout-index` writes such a link as the tree holds it. No commit of this repository adds a symlink: `git log --all --format= --raw`, filtered for mode `120000`, listed nothing (executed).
- A file already standing where `extract` writes now stops the run. `checkout-index` without `--force` exits 1 with `<path> already exists, no checkout` (executed), where `tar` overwrote. Neither caller meets one: `run_side` writes the whole tree into a fresh directory, and removes `evals/behaviour/` before it writes the suite there (read). `--force` was tried first and dropped, because no case could see it.
- A PATH that REV does not hold stops the run at `git ls-files`, as `git archive`'s pathspec error did. The new case `test_refuses_a_path_the_rev_does_not_hold` pins it.
- A relative INTO is made absolute before git gets it, because git runs with `-C ROOT` and would resolve it there. The `tar` extraction resolved it from the caller's directory.
- A removal `## Removes` did not name: the module's `io` and `tarfile` imports, which `extract` alone used.

**Cases beyond the plan's one new `extract` case.** The plan's row asks for one case shown red against the archive-based `extract`. That case is `test_accepts_what_export_ignore_marks`. Three more went in, each because a mutant of a unit this phase added survived or would have had nothing to fail:

- `test_leaves_the_repository_s_own_index_as_it_was`: with `GIT_INDEX_FILE` dropped, `extract` wrote the same files and reset ROOT's own index to REV. That mutant survived the first round of runs (m8 below).
- `test_accepts_an_into_relative_to_the_caller` holds the `abspath` above.
- `test_refuses_a_path_the_rev_does_not_hold` holds `--error-unmatch`.

They sit in `Test_extract` beside the two cases it had. A helper, `marked_repo`, builds the marked fixture repository for two of them, because the module-scoped `_suites` repository is shared and staging a change in it would reach other cases. `bin/seal layout --pairs` names no pair in `tests/evals/test_noninferiority.py` or in `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py` (executed, exit 0).

**The release table's case.** `test_the_table_reads_the_last_tag_s_whole_tree` is new in `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`. It reads the job's block with comment lines removed, as the module's other case does. It asserts the worktree line is there and `git archive` is not. Judged against `frame/design.md` *User scenarios*, the row *A tag's whole tree still reaches the release table*.

**Seen red** (executed, against the tree of `1107baaf` with only the new cases in place). `bin/test tests/evals/test_noninferiority.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py -q -p no:xdist -k "Test_extract or whole_tree"` ended 4 failed, 1 passed.

- `test_accepts_what_export_ignore_marks` failed at the first `extract` with `tarfile.ReadError`, because the archive of the marked `evals/behaviour` was empty.
- `test_refuses_a_rev_git_does_not_resolve` failed on its match, because the message opened `git archive`.
- `test_refuses_a_path_the_rev_does_not_hold` failed on its match the same way.
- `test_the_table_reads_the_last_tag_s_whole_tree` failed on the worktree line's assertion.
- The two cases added after the first commit were shown red by mutants m8 and m4b below, each with its one guard removed. Each failed on its own assertion.

**Mutation** (executed). One `bin/seal mutate` per break, over `bin/test tests/evals/test_noninferiority.py -q -p no:xdist -k Test_extract` for `evals/scripts/noninferiority.py`, and over `bin/test tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py -q -p no:xdist` for the workflow. The targets were committed at `243136b7` before every run. The runs from m2 to m9 ran while the relative-INTO case stood uncommitted in the test module, which no mutation writes. m8b and m4b ran at `c13683ed`, with everything committed.

- m1, `read-tree` without `index=`: red at `243136b7`.
- m2, `--error-unmatch` removed: red, `test_refuses_a_path_the_rev_does_not_hold`.
- m3, PATHS not passed to `ls-files`: red, `test_accepts_the_paths_named_and_the_whole_tree_for_none` and `test_refuses_a_path_the_rev_does_not_hold`.
- m4b, INTO handed to git unresolved: red, `test_accepts_an_into_relative_to_the_caller`.
- m5, the prefix without its trailing separator: red, three cases.
- m7, `checkout-index` without `index=`: red, `test_accepts_the_paths_named_and_the_whole_tree_for_none`.
- m8, `git_bytes` setting no `GIT_INDEX_FILE`: SURVIVED at `243136b7`, exit 1. With `test_leaves_the_repository_s_own_index_as_it_was` in place, m8b is red at `c13683ed`.
- m9, `git_bytes` passing no standard input: red, three cases.
- m6, the workflow's worktree line put back as the old `mkdir` and `git archive` pair: red, `test_the_table_reads_the_last_tag_s_whole_tree`.

Result: 9 breaks, 8 red at once, and the survivor red after its case.

**The `release-report` command against a tag marking paths `export-ignore`** (executed). A `git clone --no-local` of this worktree was made under the scratch directory. The five lines of *Data & interfaces* went into its `.gitattributes`, were committed, and were tagged `vprobe`. The tag's tree held 887 files, and `git archive vprobe | tar -t` listed 228 entries.

- The old form was `mkdir`, then `git archive vprobe | tar -x`. It wrote no `.test_durations`, and `release_report.py --against vprobe --at <dir>` with empty job files exited 2: `.test_durations under <dir> cannot be read ... Nothing was compared.`
- The new form was the step's own line with `tag=vprobe`, `git worktree add --detach "$RUNNER_TEMP/at" "$tag"`. It exited 0, and `.test_durations` and `CLAUDE.md` were in the directory. `release_report.py` over it exited 0 and printed the table under `### Against vprobe`.
- A `read-tree` and `checkout-index -a` of the same tag gave a table identical to the worktree's (`diff`, exit 0).

**`extract` over the same tag** (executed, the new `noninferiority.py` loaded with ROOT set to the clone). `extract("vprobe", [], d)` wrote 887 files, `.test_durations` and `CLAUDE.md` among them, the count `git ls-tree -r vprobe` gives. `extract("vprobe", ["evals/behaviour"], d)` wrote 247 files, the count `git ls-tree -r vprobe evals/behaviour/` gives.

**The phase boundary** (executed). One `bin/test ... -q` command ran 16 modules. These are the plan row's two modules and every test module that names `test.yml` or `noninferiority`, globs `.github/workflows/` or `evals/scripts/`, or reads every tracked file's citations. The list came from `git grep -l` under `tests/`, with `tests/conftest.py` and `tests/censuses.py` left out because they are not test modules. The command ended 859 passed, 4 skipped, 1 failed, exit 1. The failure was `tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census` on `seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/questions.md:16`: the `real_identifiers` census, on the owner's address spelled out. That line is the frame's Q1. This phase does not write `frame/questions.md`, and `git diff 1107baaf c13683ed -- seal/` is empty, so the failure stands at the frame commit too. The hand-back names it for the orchestrator. With this record, `gaps.md` and the Status cell written, the same command ran again with four modules that read a work item's records added: `test_chain_hooks_hardening.py`, `test_a_phase_hands_the_next_one_a_record.py`, `test_unverified_rows_close.py` and `test_docs_line_wrap.py`, all under `tests/behaviour/`. It ended 976 passed, 4 skipped, 1 failed, exit 1, and the one failure was the same `questions.md:16` line.

**Two docstrings counted the workflow's cases.** The module docstring of `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`, and `tests/github/test_release_report.py`'s, each said the first module keeps the one case that reads the `release-report` job. It keeps two now, so commit `ec580f88` says "the cases" in both. `git grep` on the module's file name outside `seal/threads/` and `.test_durations` listed these two and the `check:` line of `docs/releasing/release-checklist.md` *5. The release pull request*, which names the module and counts nothing (executed). Both modules ran green after the edit, exit 0.

**Other statements of the two readers** (a sample, by wording). `git grep -n -i -E "git archive|tar -x|tarfile|extract\("` outside `seal/threads/` and `.test_durations` found only `extract`, its two call sites, its cases, and `tests/censuses.py`'s `tarfile` rows, which list a module's binary reader and say nothing of `extract`. `git grep` for `release-report`, `--at` and `archive` in `docs/`, `CONTRIBUTING.md`, `README.md` and `evals/README.md` found no sentence that says how the tag's tree is built. A statement in another spelling escapes this search.

**What phase 2 meets.** Once `/evals/` is marked `export-ignore`, a `noninferiority.py run --rev` side gets its suite through `checkout-index`, and the archive no longer reaches either reader. Phase 2's census reads `git archive`'s own listing, which this phase leaves alone.
