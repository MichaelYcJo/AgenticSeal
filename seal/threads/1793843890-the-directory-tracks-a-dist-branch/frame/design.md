# Design: the directory tracks a dist branch (#1374)

## Grounding

Every line coordinate and every present-tense statement of the tree in this
section was read at commit `efd8edec` (`routing: declare #1374 under
automation`, on `release/v0.32.3` cut from `9dd67e2a`, v0.32.2), and a
crafter reading a later HEAD reads them as of that commit.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A fact has one source. The paths that leave `dist` are listed once, as `export-ignore` lines in `.gitattributes`, and the workflow holds no list. A script holds a gate on what a real parser returns, so the census reads `git archive`'s own output and not a reading of `.gitattributes` it re-implements. |
| `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*, the paragraph opening **A third reader of those commits is outside this repository.** | The directory serves a scanned commit of the branch the submission tracks. So `dist` takes one new commit per release and is never force-pushed: a rewritten branch would orphan the commit a listing is served from. That paragraph's sentence tying the directory to the merge-commit rule on `main` stops being true once the directory reads `dist`, and `## Rule changes` corrects it. |
| `docs/releasing/branch-and-release.md` *Cutting a release*, the paragraph opening **Every act the release performs once it reaches `main` belongs to a machine** | Adding the release's commit to `dist` is an act of the release, so a workflow performs it on the push to `main`, in `.github/workflows/publish-release.yml`, the workflow that already creates the tag. |
| `docs/releasing/release-checklist.md` *6. After the merge*, the box opening **The marketplace files and the directory's page have been read** | This box is where a person reads what the directory serves. It names `dist` after this work, through `## Rule changes`. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | The subject of this work item is the release workflow and the branch it writes, not the policy root. So the two release documents change through `## Rule changes`, for the settle, and the crafter does not edit `docs/` directly. |
| `contract rule 11` | Every `skills/`, `templates/`, `docs/` and `agents/` path in a skill or an agent definition is the plugin's own. Those are the citations an installed copy has to hold. A citation of `tests/` or `evals/` is a coordinate for a contributor working in a clone, and `dist` does not have to resolve it. |
| `tests/behaviour/test_the_release_check_watches_what_ships.py`, `SHIPS` and `STAYS_HOME` (lines 38 to 69) | These sets answer a different question: which top-level entries need a version bump when they change. `docs/` is in `STAYS_HOME` and stays in `dist`, because agents open it. The two lists are not one fact, and this work keeps both. |
| `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, module docstring lines 32 to 37 | This module is the census that reads cited paths. It reads section citations (`` `path.md` *Section* ``) and name citations (`path.py#name`) over every tracked file. A token is read only where its path's first segment is a top-level entry of the repository it reads. Applied to the archive as the repository read, that rule leaves a citation into a wholly dropped entry such as `tests/` unread. |

### What the tree and the probes answered

| Fact | Label | How |
|---|---|---|
| With `/tests/`, `/evals/`, `/seal/`, `/.test_durations` and `/CLAUDE.md` marked `export-ignore`, `git archive` of a tag holds 186 files, 3,461,120 bytes as a tar. The tag's tree holds 884. The archive's top-level entries are `.claude-plugin .gitattributes .github .gitignore agents assets bin CONTRIBUTING.md docs hooks LICENSE README.ko.md README.md ruff.toml SECURITY.md skills templates TRADEMARKS.md`. | executed | In a `git clone --no-local` under the scratch directory: the five lines committed, `git tag vprobe`, `git archive vprobe \| tar -t`, `git archive vprobe \| wc -c`. |
| `git archive` reads the attributes of the tree it archives. `v0.32.2`, whose tree has no `export-ignore` line, archives whole (883 files) after a later commit adds the lines. | executed | `git archive v0.32.2 \| tar -t` in the same clone. |
| `git archive vprobe evals/behaviour/` exits 0 with an empty archive. A reader that archives a path the attributes drop gets nothing, and nothing says so. | executed | `git archive --format=tar vprobe evals/behaviour/; echo $?`, then `tar -t` counted 0. |
| `git --attr-source=<empty tree> archive` and `GIT_ATTR_SOURCE` still drop the marked paths (186 files). Attribute sources do not turn `export-ignore` off. | executed | Both spellings run against `vprobe`, git 2.50.1. |
| A whole tag tree, `export-ignore` notwithstanding, comes out of `git worktree add --detach <dir> <tag>`. It also comes out of a temporary index: `GIT_INDEX_FILE=<tmp> git read-tree <tag>`, then `git checkout-index -a --prefix=<dir>/`, which wrote 884 files with `.test_durations` among them. A subtree comes out of `read-tree --prefix=evals/behaviour/ <tag>:evals/behaviour`, which wrote 247 files, the count `git ls-tree -r` gives. | executed | In the same clone. The worktree was removed and pruned. |
| `git check-attr export-ignore` answers `unspecified` for `tests/conftest.py` and for `tests` under the pattern `/tests/`, and `set` for `.test_durations`. A directory pattern matches a directory that `git archive` walks, not a path `check-attr` is handed. A reader built on `check-attr` would miss every directory the archive drops. | executed | `git check-attr export-ignore -- tests/conftest.py tests .test_durations`. |
| A commit whose tree is the archive's can be built two ways, and both give tree `9a543f32`. One extracts the archive and runs `git --work-tree=<dir> add -A` under a temporary index. The other reads the tag into a temporary index and runs `update-index --force-remove` on every path the archive's listing lacks. `git commit-tree -p <previous>` then chains it, and `git archive` of the result again lists 186 files. | executed | `git write-tree` and `git rev-parse <commit>^{tree}` compared. |
| Files the archive keeps cite paths the archive drops 14 times: 13 name citations into `tests/` or `evals/`, and `` `evals/README.md` *The behaviour suite* `` in `docs/running/measuring-a-run.md:86`. All 14 are under an entry the archive drops whole, so the module's top-level rule leaves them unread in the archive. No file the archive keeps cites a section of a file under `seal/` or of `CLAUDE.md`. | executed | `git grep`-equivalent `grep -o` over the 186 kept files for the two citation shapes. It is a sample of spellings, since it imitates the module's regexes rather than running them. |
| Two readers in the tree build a tree with `git archive`: `.github/workflows/test.yml` job `release-report` (line 280) extracts the last release tag for `.github/scripts/release_report.py --at`, and `evals/scripts/noninferiority.py#extract` (line 177) extracts a plugin tree and the suite at `--suite-rev`. `release_report.py` exits 2 where the tree at `--at` has no `.test_durations` (its docstring, lines 38 to 40). | executed | `git grep -n -i 'archive\b\|tarball\|zipball'` outside `seal/`, then read. The method lists the property itself: a git archive or a GitHub archive endpoint is the only thing that honours `export-ignore`. |
| No shipped script joins a path under `tests/`, `evals/`, `seal/`, `.test_durations` or `CLAUDE.md` to its own directory or to the plugin's root. The shipped readers of those names (`.github/scripts/rules.py#RULE_FILES`, `skills/settle/scripts/settle.py#TESTS`, `skills/verify/scripts/payload_meter.py`, `skills/settle/scripts/passages.py#TOP_FILES`, `skills/code-review/scripts/chain_check.py`) resolve them in the user's repository. | executed, a sample | `git grep` for `join(HERE\|ROOT\|...` with those literals, which found none, then the five files read for the root they resolve against. A path built another way escapes the grep, and the smoke run of phase 3 is what reads that class. |
| `bin/test` run where no `tests/` exists prints that it runs AgenticSeal's own suite and exits 2 (`.github/scripts/run_tests.py#main`). `bin/` stays in `dist` and `bin/test` fails there with that message. | read | `.github/scripts/run_tests.py` lines 564 to 574. |
| `assets/` stays: the README shows `assets/seals/owl.png`, and the publish workflow attaches the PNG `plugin.json` names as `icon`. | read | `README.md:136`, `.github/workflows/publish-release.yml` lines 33 to 37. |
| Neither marketplace file has an entry for `agentic` today: official has 315 entries, community 2,283. | executed | `python3 .github/scripts/plugin_directory_check.py --root <scratch clone>`, exit 0. |
| `claude.com/docs/plugins/submit`, read 2026-11-05: "Merge to the tracked branch, and the directory picks up the commit, checks it, and publishes it." "When you select **Submit for review**, the directory scans the newest commit on the tracked branch or tag." The tracked branch is set in the form, defaults to the default branch, and is changed later on the plugin's Settings tab. This answers the issue's second open question: a listing tracking `dist` needs no resubmission per release. | read | `WebFetch` of the page. |
| The owner decided on 2026-11-05: the branch is `dist`; `release/vX.Y.Z` keeps its name; the paths leave by `export-ignore` and `dist`'s tree is `git archive` of the tag; each release adds a commit, never a force-push; `dist` is built whatever the directory says about Verified organizations, and preparing for that rule is #1376; #1375 removes `assets/seals/candidates/` and moves the version to 0.32.3. | nobody's finding opened in the tree | Relayed by the orchestrator's spawn prompt from its conversation with the owner. The owner answers it. `routing.md` *Why this way* records the Verified organization choice. |
| The form passed for `agenticseal-dir-test@proposed`, v0.32.2's tree less `tests/`, `evals/` and `seal/`, with 8 warnings and 18 policy holds, and timed out on the whole tree. | nobody's finding opened in the tree | #1374's body and comment, read off the owner's screenshots. The owner answers it. |

## Scope

In:

1. `.gitattributes` marks `/tests/`, `/evals/`, `/seal/`, `/.test_durations` and `/CLAUDE.md` `export-ignore`, with a comment that says what the lines decide and that a pull request adding a development-only path adds its line here.
2. The census in `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads a second corpus, the archive git builds from the tree, with both of its readers, `citations` and `names`. A citation in a file the archive holds dangles where the archive lacks its target, and the module's top-level rule applies with the archive as the repository read. A fixture case holds that a cited file marked `export-ignore` fails, and that the same citation passes the tree reading.
3. `tests/behaviour/test_the_release_check_watches_what_ships.py#test_every_top_level_entry_is_classified`'s message also names `.gitattributes`, so whoever classifies a new top-level entry decides whether `dist` holds it.
4. The two readers that build a tag's whole tree stop using `git archive`: the `release-report` job of `.github/workflows/test.yml`, and `evals/scripts/noninferiority.py#extract`. Each reads the whole tree, a probed spelling or an equivalent the crafter names in the phase record.
5. A new script, `.github/scripts/dist_branch.py`, and a new job, `dist`, in `.github/workflows/publish-release.yml`. On a run whose `publish` job names a tag, the job adds one commit to `dist` whose tree is `git archive` of the tag, parented on `dist`'s tip, or as the first commit where `dist` does not exist. It makes no commit where the tip's tree is already the tag's archive, and pushes without force.
6. `.github/scripts/plugin_directory_check.py` reads a pin's ancestry against both `main` and `dist`'s remote-tracking ref, and names the one that holds it. "NOT reachable" names a rewritten `dist` or a squashed release branch.
7. A smoke run from the extracted archive of HEAD against a scratch repository, recorded in the phase record: the `SessionStart` hook prints the core, and `seal gate --preflight`, `seal rules --check` and `seal settle`'s dry run end with no missing-file error.
8. The three rule changes below.

Out:

- Preparing for command hooks that need a Verified organization. The owner put it in #1376 (backlog) on 2026-11-05.
- `assets/seals/candidates/` and the version move to 0.32.3. Both are #1375's, in the same release, and this work leaves `.claude-plugin/plugin.json` alone.
- Leaving more paths out of `dist`, such as `bin/test`, `.github/workflows/` or `ruff.toml`. None raised a finding in the form, and a later pull request adds its line to `.gitattributes`.
- The replies to the directory's reviewer on the 18 holds. The owner sends them after submitting.
- A ruleset on `dist`, submitting `MichaelYcJo/AgenticSeal@dist` at the portal, installing from it, and deleting `MichaelYcJo/agenticseal-dir-test`. Each is the owner's act outside the tree, and `plan.md` *Operational impact* lists them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| The release adds a commit to `dist` | Given a repository with the `export-ignore` lines and a tag `vX.Y.Z`, when `dist_branch.py` runs with `TAG=vX.Y.Z`, then `dist` gains one commit whose tree equals the tree of `git archive vX.Y.Z`, whose parent is the previous tip, and whose message names the tag. | `tests/github/test_dist_branch.py`, against a fixture repository and a bare local remote |
| `dist` does not exist yet | Given no `dist` on the remote, when the script runs, then it pushes a first commit with no parent. | the same module |
| A re-run makes nothing | Given `dist`'s tip already has the tag's archive as its tree, when the script runs again, then it pushes nothing, says so, and exits 0. | the same module |
| `dist` is never rewritten | Given the remote's `dist` moved past the commit the script built on, when it pushes, then the push is refused as a non-fast-forward and the script exits non-zero. No command it runs carries `--force` or a `+` refspec. | the same module |
| The workflow runs the job on a release alone | Given `publish-release.yml`, the `dist` job needs `publish`, runs where `needs.publish.outputs.tag` is not empty, checks out the whole history and runs `dist_branch.py` with the tag. | a case reading the workflow, beside `tests/behaviour/test_a_release_publishes_its_note.py` |
| A cited file marked `export-ignore` fails | Given a fixture where `manual/a.md` cites `` `manual/b.md` *Here* `` and `.gitattributes` marks `/manual/b.md export-ignore`, when the census reads the archive, then the citation dangles. The tree reading passes it. Shown red with the archive reading removed. | `tests/behaviour/test_a_cited_section_stands_in_its_file.py` |
| The tree passes the archive reading | When the census reads this repository's archive, then no citation dangles and at least as many are read as the module's floor asks of the tree reading. | the same module, its tree case for the archive |
| A tag's whole tree still reaches the release table | Given a tag whose tree marks paths `export-ignore`, when the `release-report` job builds `--at`, then `.test_durations` and `CLAUDE.md` are there. | `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py` reads the step's command, and the phase record shows the command run against such a tag |
| The eval suite still reaches its side | Given a fixture tag marking `/evals/` `export-ignore`, when `extract(tag, ["evals/behaviour/..."], dir)` runs, then the case files are written. Shown red against the archive-based `extract`. | `tests/evals/test_noninferiority.py` |
| A dist pin reads as reachable | Given a pin naming a commit of `dist`, when `plugin_directory_check.py` reports it, then it says which ref holds it, and "NOT reachable" appears only where neither `main` nor `dist` does. | `tests/github/test_plugin_directory_check.py` |
| The archive runs as a plugin | Given the extracted archive of HEAD as the plugin's root and a scratch repository, when the `SessionStart` hook, `seal gate --preflight`, `seal rules --check` and `seal settle`'s dry run run, then none ends with a missing-file error. | the phase 3 record, `executed` |
| The form answers for `@dist` | After the release, the owner enters `MichaelYcJo/AgenticSeal@dist` in the portal's form and it answers. | the owner's reading. The run does not wait on it. |

## Data & interfaces

- `.gitattributes`: the existing `* text=auto eol=lf` line stays first. Five lines follow, each anchored at the root: `/tests/ export-ignore`, `/evals/ export-ignore`, `/seal/ export-ignore`, `/.test_durations export-ignore`, `/CLAUDE.md export-ignore`. A `#` comment above them says that these are the paths `dist` and every `git archive` leave out, why a list of what leaves is kept rather than one of what stays, and that a pull request adding a development-only path adds its line here.
- `.github/scripts/dist_branch.py`: reads `TAG`, and `DRY_RUN` where set, which prints the plan and pushes nothing, the shape of the other scripts beside it. It builds the tree of `git archive "$TAG"` and reads `dist`'s tip from `origin` with `git ls-remote --heads`, fetched where it exists. It writes one commit with `git commit-tree`, message first line `dist: <TAG>` and body naming the tag's commit, and pushes `<commit>:refs/heads/dist`. Exit 0 where a commit was pushed or none was needed. Non-zero where a git call fails, the push refused among them, with the refusal printed. The author and committer are the GitHub Actions bot unless `frame/questions.md` Q1 is answered otherwise.
- `.github/workflows/publish-release.yml`: a third job, `dist`, with `needs: publish` and `if: needs.publish.outputs.tag != ''`. It runs `actions/checkout@v4` with `fetch-depth: 0` and the default persisted credentials, which the push uses under the workflow's `contents: write`, then `python3 .github/scripts/dist_branch.py` with `TAG: ${{ needs.publish.outputs.tag }}`. It has no `continue-on-error`: a release that did not reach `dist` is a red run, because the directory does not get it. The header comment gains the paragraph that says so.
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py`: `corpus` gains a reading of the archive. The membership is the list of paths `git archive` writes for the index's tree with the working tree's attributes, so a file staged but not committed, or an uncommitted `.gitattributes` line, is read as CI will read it once committed. The texts come from disk, as the tree reading's do. `citations` and `names` take that corpus, and a new tree case for each asserts that none dangles, with a floor. The exact git commands are the crafter's. The phase record names them, and says what an uncommitted change does to them.
- `evals/scripts/noninferiority.py#extract` keeps its signature. git's `read-tree` refuses a path that would land outside INTO, and a symlink whose target lies outside INTO is no longer refused; no commit of this repository holds a symlink. It writes REV's PATHS whole, `export-ignore` notwithstanding. Its error for a REV git does not resolve still names the git command that failed.
- `.github/workflows/test.yml` job `release-report`: the line that extracts the tag reads the tag's whole tree into `$RUNNER_TEMP/at`.
- `.github/scripts/plugin_directory_check.py`: the reachable fact is read against `main` and `origin/dist`. A `--ref` given on the command line still names the one ref compared. The output names the ref that holds the pin, and the docstring's `reachable` line says the same.

## Rule changes

- add
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  to: **The plugin directory reads `dist`, a branch that holds what the
    installed plugin runs, and the publish workflow adds one commit to it at
    each release.** The directory's form does not answer in time for this
    repository's whole tree, and answers for the tree without its suites and
    records (#1374). The paths that leave are marked `export-ignore` in
    `.gitattributes`, and the tree of each commit of `dist` is `git archive`
    of the release's tag. So the list lives in that one file and the workflow
    holds none. It lists what leaves and not what stays: a path forgotten
    there reaches `dist` and costs size or a finding, where a path forgotten
    in a list of what stays would be missing from every listed copy with
    nothing here to see it. The workflow's `dist` job builds the commit with
    `.github/scripts/dist_branch.py` on the previous commit of `dist`, makes
    none where that commit's tree is already the tag's archive, and pushes
    without force, because the directory serves a scanned commit of the
    branch it tracks and a rewritten branch would orphan it. The census that
    reads cited sections and names reads the files `dist` holds against
    `dist`'s files too, so a cited file marked `export-ignore` fails CI. A
    reader here that needs a tag's whole tree checks the tree out rather than
    archiving it, since an archive leaves the marked paths out. GitHub's
    source archives of a release leave them out too. `marketplace.json`'s
    `source` is `./`, so `/plugin marketplace add` installs the whole tree from
    the default branch, `main`.
    check: tests/github/test_dist_branch.py tests/behaviour/test_a_cited_section_stands_in_its_file.py
- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: says per file whether the plugin has an entry, which
    commit it pins and whether that commit is on `main`.
  to: says per file whether the plugin has an entry, which
    commit it pins, and which of `main` and `dist` holds that commit.
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: The plugin directory, the catalog people browse inside Claude, holds a
    commit too: a plugin submitted at its developer portal is served from a
    scanned commit of the branch or tag the submission tracks
    (`claude.com/docs/plugins/submit`). Breaking the rule above therefore also
    breaks a consumer nobody here can reach, for people the owner cannot name.
  to: The plugin directory, the catalog people browse inside Claude, holds a
    commit too: a plugin submitted at its developer portal is served from a
    scanned commit of the branch or tag the submission tracks
    (`claude.com/docs/plugins/submit`), and this plugin's submission tracks
    `dist`. The publish workflow adds each commit of `dist` and rewrites none
    (*Cutting a release* above), so the rule above does not reach the
    directory's commit. A marketplace file's pin can still name a commit of
    `main`, and breaking the rule above breaks that pin, a consumer nobody
    here can reach, for people the owner cannot name.
- change
  file: docs/releasing/release-checklist.md
  section: 6. After the merge
  from: the entry pins, and whether that commit is an ancestor of `main`.
  to: the entry pins, and whether that commit is an ancestor of `main` or of
    `dist`, naming the one that holds it.
- change
  file: docs/releasing/release-checklist.md
  section: 6. After the merge
  from: It picks up each new version from its tracked branch without a
    resubmission,
  to: It picks up each new version from its tracked branch, `dist`, without a
    resubmission,
- change
  file: docs/releasing/release-checklist.md
  section: 6. After the merge
  from: Whether it shows up at all is what a search for the plugin inside
    Claude answers.
  to: Once the publish workflow's `dist` job has run,
    `git log -1 --format=%s origin/dist` names the release as `dist: vX.Y.Z`.
    A red `dist` job is a release the directory did not get, and a re-run of
    the workflow adds the commit. Whether it shows up at all is what a search
    for the plugin inside Claude answers.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `git archive` extraction of the last release tag | `.github/workflows/test.yml` *release-report*, the step's `git archive "$tag" \| tar -x` line (line 280 at `efd8edec`) | A checkout of the tag's whole tree. From the release after this one, the tag's archive would lack `.test_durations` and `CLAUDE.md`, and `release_report.py` exits 2 on the first. |
| The `git archive` call that builds an eval side | `evals/scripts/noninferiority.py#extract` | A reader that writes the revision's tree whole. `git archive <rev> evals/behaviour/` exits 0 with nothing in it once `/evals/` is marked. The case `tests/evals/test_noninferiority.py#Test_extract::test_refuses_a_rev_git_does_not_resolve`, which matches `^git archive`, changes with the command its error names. |
| The single-ref ancestry reading of a marketplace pin, against `main` by default | `.github/scripts/plugin_directory_check.py#main`, its `--ref` default, and `#line`'s "NOT reachable" sentence | A reading against `main` and `dist`. A pin of a `dist` commit would otherwise read as what a squashed release branch leaves behind. |
| The sentence saying the merge-commit rule on `main` protects the directory's commit | `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* | `## Rule changes` above, written at the settle. |

This work adds a job, a script, a census reading and five attribute lines. Nothing existing can go in return. No mechanism here built a tree for the directory before, the census reading reuses the module's two readers and adds no third, and the list of what leaves lives in `.gitattributes` and nowhere else.

Framed 2026-11-05 by framer, before the build.
