# Implementation Plan: a sha:path citation opens after the squash (#1270)

## Technical context

The build adds one test module and corrects one record line. It changes no
shipped file. The code it builds on:

- `tests/censuses.py:1113-1116`, `COMMIT_PATH`: the one reader of the
  `<commit>:<path>` form, `(?<![\w/:])[0-9a-f]{7,40}:[\w./-]+`. The new
  module imports it. `tests/censuses.py:850`, `RECORDS`, is the scope the
  citation readers keep, and the module departs from it on purpose
  (`frame/design.md` G4).
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py:185-198`,
  `corpus`: `git ls-files -z`, then `conftest.on_disk`, then a UTF-8 read
  that drops what does not decode. The new module reads its files the same
  way, so a file the working tree deleted cites nothing.
- `.github/workflows/test.yml:118-120`: every pytest job checks out with
  `fetch-depth: 0`, so `refs/remotes/origin/main` and each
  `refs/remotes/origin/release/*` stand in CI.
  `tests/text/test_ci_gives_the_checks_what_they_need.py` holds that depth.
- `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:18`:
  the one citation the check refuses at HEAD (`frame/design.md` P2).

**Failure scenario, six months out.** The reaching refs are named by
pattern: `main` and `release/*`, from `docs/branch-and-release.md` *Work
accumulates on a release branch*, rulesets table. If release branches are
renamed, or the repository stops squashing, the patterns and the rule
change's wording move together. Until they do, every citation of the new
branch names is refused loudly, and none passes quietly. A second failure
is local and loud too. A contributor who cites a sibling's squash before
fetching it sees a red that CI does not show, and the refusal message
names `git fetch` as the answer. The quiet failure is the one the rule
accepts: a cross-branch citation in `trail/` or `guarantee.md` passes, as
`137d0a9c` and `7ef6abbf` did (`frame/design.md` P1). The proofer reads
those files.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. A test module over every tracked file outside `evals/behaviour/`, `trail/` and `guarantee.md`, which refuses a commit that no `main` or `release/*` ref reaches (this plan) | A cross-branch citation in `trail/` or `guarantee.md` passes. P1 lists 5 such lines in #1257's `phase-3.md`, one in #1137's round 5 and one in #1252's guarantee over five releases | Chosen. It refuses every in-scope instance on record (`frame/design.md` G1) with 0 false refusals over ten revisions (P2), it reads one exact form, and it stores nothing |
| A2. Build nothing. Rely on review, and add a sentence to `skills/writing-style/SKILL.md` on citing the squash | The record is three work items through sealed chains with the citation in their frame (G1). The only catch came from a round 1 axis that no file asks for. A sentence adds a reading and holds nothing | Rejected. This is the decision the issue offers, weighed under `skills/core/SKILL.md` *The rule a mechanism is kept against*. The record of what the check would have caught outweighs the cost of one module |
| A3. Read every tracked file, `trail/` and `guarantee.md` included, under the same refusal. This replaces the structure `RECORDS` keeps rather than narrowing it | Every round record's evidence line `git show <target>:<path>` is refused at its own pull request. After its squash, the same line is refused on every later branch until the settle. P1 finds such lines at every tag from `v0.24.0` to `v0.27.3` | Rejected. The coupling is the one `docs/one-root-by-lifetime.md` *The dependency rule* and `docs/the-review-record.md` *`target:` names a commit, not a content anchor, because a round records a moment* accept. The premise that keeps `trail/` unread was checked: P1 shows that all but three dead trail citations name the citing pull request's own commits |
| A4. A1, plus reading the branch's own `trail/` and `guarantee.md` under "an ancestor of HEAD". The own work item is found by matching `routing.md`'s `Branch` row with the current branch, or with `GITHUB_HEAD_REF` on CI's detached merge ref | This catches the three cross-branch trail citations of P1. It needs a branch name, which a detached checkout outside a pull request lacks, so a push run on a release branch judges no work item. It adds an environment read to a suite case | Rejected for this item. The files it adds leave with the work item, and the proofer reads them. If a cross-branch trail citation recurs after this release, this is the next step, and the module's reader already holds half of it |
| A5. A `hygiene.yml` step over the lines `origin/<base>...HEAD` adds, with the base handed in | Lines in released records are left alone, but a new CI step is owed a `PARTITION` row in `skills/verify/scripts/broad_gate.py`, the shipped gate. The gate then reports one more CI step it does not answer, and the tree that passes the suite still holds the dead line at `1793538230` | Rejected. The suite runs in CI and under `seal gate`, so a module reaches both without a new step |
| A6. A census in `tests/censuses.py`, beside `COMMIT_PATH`, which keeps the structure that already reads the form | The census framework judges one file at a time from the file alone. Its docstring says a census reads the file at REL, and `evals/scripts/noninferiority.py` loads the module by path without pytest. A census that asks git about refs adds a history dependency to every module's `test_census` run | Rejected. The module imports `COMMIT_PATH`, so the form keeps one reader and the census contract stays as it is |
| A7. An arm of `skills/code-review/scripts/chain_check.py`, which every user's pull request runs | It encodes this repository's squash policy in every user's gate. A repository that merges without squashing keeps its feature commits, so the arm refuses citations that resolve there | Rejected. `skills/core/SKILL.md` *The rule a mechanism is kept against* governs this plugin's own mechanisms, and a user's repository keeps or drops its own mechanisms by its own policy |
| A8. A1, plus `git cat-file -e <commit>:<path>` on the path | `COMMIT_PATH`'s `[\w./-]+` takes a sentence's closing period into the path (read), so a correct citation at the end of a sentence is refused | Rejected. The issue asks whether the commit resolves, and reachability is exact where the path half is not |
| A9. Reachability from "the base", as the issue words it | The suite is not handed a base. The test job would have to read `GITHUB_BASE_REF`, and `seal gate` would have to export one | Departed from, on `frame/design.md` G9's grounds: `main` plus every `release/*` ref covers the base of both kinds of pull request this repository opens |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 6 | Seen red: the tree case run on the tree before item 5's edit fails naming `1793538230` `frame/design.md:18`. Each planted case is seen red against a reader mutant the phase record names. Mutants: `trail/` widened to all of `seal/threads/` makes S4's `frame/plan.md` side red; the containment test replaced by `cat-file -t` makes S2 red, because the planted feature commit exists locally; the missing-object branch removed makes S5 red. Narrow run at the phase boundary, in one command: the new module, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/test_censuses.py` (it reads `COMMIT_PATH`'s module), and `tests/text/test_ci_gives_the_checks_what_they_need.py`. `uvx ruff check` and `uvx ruff format --check` on the new module. After the orchestrator merges `release/v0.28.1` in, the tree case once more, with each correction item 6 makes listed in the phase record. The module's duration as `--durations` prints it on the crafter's system | 44b215bc |

## Operational impact

None for a user of the plugin: no shipped file changes. For a contributor,
the suite gains one case that reads the `main` and `release/*` refs. In a
checkout with neither, it skips and says why. In a checkout whose refs are
older than a cited squash, it fails and names `git fetch`. CI needs no
change (`frame/design.md` G9).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
