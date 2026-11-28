# Review round 1: 1795830609-iadd-is-the-method-and-a-product-only-expresses-it

```iadd
target: 59cf3d37 against 801465cb
```

The round read the branch `feat/1658-the-plugin-stays-agentic` at `59cf3d37` against `801465cb`, #1656's merge on the release branch, in a `git clone --no-local` under the round's scratch directory. It read the work item's `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and the five phase records whole at the target, and #1656's rewritten `changelog.md` beside its text at `801465cb`. No `pr.md` stands yet. No earlier round exists, so no fact was carried and every verdict below is this round's own. No `agentory/parity.json` is declared, so no parity comparison is owed.

The method for the class the plan's failure scenario names, a word renamed into the wrong layer, was this. A script under the round's scratch directory paired each removed word run with its added run in `git diff -M --word-diff=porcelain -U0 801465cb..59cf3d37 -- . ':!agentory/threads' ':!iadd/threads'`, with git's word regex `[A-Za-z0-9_]+|[^[:space:]]`, and printed each pair with its count and files; the same script ran over `35bef264..59cf3d37`, from 0.39.4. Every pair was read. Then the tree was searched both ways for the wrong layer: `agentory` before a subcommand, a `:`, `-scratch`, `-stamp`, `_pytest`, `.claude`, `RUNNER_TEMP`, `marketplaces`, `plugins/` or `"bin"`, and `agentic` before `/threads`, `/README`, `/config.json`, after `keeps in`, `common-dir)/` or `.git/`, and as a quoted literal joined to a root. Each search printed nothing but the census's own fixtures in `tests/test_censuses.py`, which spell names that open with the root's letters on purpose. That list is whole for the words the range changed. It is a sample for a sentence the rename made false without holding a renamed word, which finding 1 is: those were found by reading the paragraphs around the hunks that touch the plugin's command, its workflow and its root, and by `git grep` on the facts each states.

Each of the 352 lines of `frame/keep.txt` outside #1656's directory was read for its kind. Each is the fence's family, the trailer, the hook's line, the marker, the definition's path, the method's name, the reserved name of questions row Q2, or row 48 of `agentory/follow-up.md`. None holds a product's or a place's `iadd` beside it. The 10 lines phase 5 added and the 5 phase 4 added are the kinds their phase records name.

## Findings

### 1. The release's steps tell a repository at 0.39.x to move only the tag its `hygiene.yml` pins, and that file then runs a dispatcher this release does not ship

```iadd
severity: should
location: `agentory/threads/1795798115-the-plugin-is-named-for-the-seal/changelog.md:7`, `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/plan.md:61`, `skills/implement/scripts/agentic.py:1732-1736`, `tests/skills/test_agentic.py:2921-2924`, `docs/layout/one-root-by-lifetime.md:153-155`, `docs/layout/one-root-by-lifetime.ko.md:145-147`, `docs/running/the-review-and-parity-arms.md:156-158`, `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/keep.txt`
evidence: executed `git show 35bef264:templates/setup/hygiene.yml`, whose mode step at lines 97 to 100 runs `python3 "$RUNNER_TEMP/agentic/skills/implement/scripts/seal.py" mode --check`; executed `python3 skills/implement/scripts/seal.py mode --check` in the clone at `59cf3d37`, exit 2, no such file; executed ``git grep -n -E '`--branch` line|`--branch` 줄|the pin.s `v<version>`|tag (its )?`?hygiene\.yml`? pins' -- . ':!agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/keep*'``; read `templates/setup/hygiene.yml:70-100`, `skills/implement/scripts/agentic.py:1697-1736` and `:1832-1852`, `README.md:102-105`
```

Why it matters: the 0.40.0 note is what a person moving a repository reads, and CodeChallenge moves after the release by these steps (#1658 *How it ships*). A `hygiene.yml` that `seal pr-checks install` wrote at 0.39.x runs `skills/implement/scripts/seal.py` in its mode step. #1658's own fragment says the command is `agentic`, where it was `seal`, and that `bin/agentic` runs `skills/implement/scripts/agentic.py`. So a copy whose `--branch v0.39.x` alone moves clones a release with no `seal.py`. Its mode step then exits 2 on every pull request, in shared mode and in local mode alike. The chain step's path, `skills/code-review/scripts/chain_check.py`, is the same in both releases, so it is the mode step alone that breaks. `README.md:102-105` already gives the repair that holds, `agentic pr-checks remove` and then `agentic pr-checks install`. `remove_workflow` removes a file that carries the plugin's clone line, which a 0.39.x copy does, and `install_workflow` writes the template pinned to the installed release.

Phase 5 rewrote the bullet in #1656's fragment and dropped its clause *the template now clones into `$RUNNER_TEMP/iadd`*. That clause was the one hint in the note that the file itself had changed. The rewritten bullet keeps *Move the tag `hygiene.yml` pins*, and `frame/plan.md` *Operational impact* states the same step. The other statements the search printed are older sentences in paragraphs this range edited. Each says that moving the `--branch` line brings an older workflow back. The dispatcher's rename makes each false for every file written before it, and none of them holds a renamed word, so the keep file's acceptance cannot see them. `agentic mode local` prints one of them as its way out (`skills/implement/scripts/agentic.py:1732-1736`), and `tests/skills/test_agentic.py:2921-2924` pins it.

The search is a sample under contract rules 12 and 19. A statement of this step in other words escapes it. The search also printed `agentory/threads/1795798115-the-plugin-is-named-for-the-seal/frame/plan.md:72`, a record of #1656 that *Out of scope* keeps byte for byte, and the fix leaves it. The bullet of #1656's fragment holds the marker and the fence, so its line stands in `frame/keep.txt`. The fix pass owes that line in the same commit, sorted as *The keep file* states.

In `agentory/threads/1795798115-the-plugin-is-named-for-the-seal/changelog.md`, line 7, the bullet's last sentence:

```markdown
Then write `.github/workflows/hygiene.yml` again with `agentic pr-checks remove` and then `agentic pr-checks install`, which pins the release that carries this change. An older release reads no `agentory/` root and lets a pull request pass with no work item judged, and a copy whose tag alone moves still runs `skills/implement/scripts/seal.py`, which this release does not ship, so its mode step fails every pull request.
```

In `frame/plan.md` line 61, the end of the bullet from *the keys `Pull request seal mark`*:

```markdown
the keys `Pull request seal mark` and `Release note seal mark` to their inspection names, and `.github/workflows/hygiene.yml` written again by `agentic pr-checks remove` and then `agentic pr-checks install`, pinned to the release that carries this work. A 0.39.x copy whose tag alone moves still runs `skills/implement/scripts/seal.py` in its mode step, which this release does not ship. The template clones into `$RUNNER_TEMP/agentic`.
```

In `skills/implement/scripts/agentic.py#left_workflow_line`, the last return, and its pin at `tests/skills/test_agentic.py:2921-2924` with the same words (contract rule 14):

```python
    return (
        f"{WORKFLOW} stays, {here}: a release before this one fails every pull "
        f"request with no {optin.HOME}/ in the tree. Run `agentic pr-checks "
        f"remove`, or move its `--branch` line to {to} and its mode step to "
        "`skills/implement/scripts/agentic.py`"
    )
```

In `docs/layout/one-root-by-lifetime.md`, lines 153 to 155:

```markdown
a trailer naming a work item. One pinned to an older release fails every pull
request there until `agentic pr-checks remove` takes it out, or until its
`--branch` line moves to the installed release and its mode step runs
`skills/implement/scripts/agentic.py`, and `agentic mode local` names the pin
when it leaves such a file.
```

In `docs/layout/one-root-by-lifetime.ko.md`, lines 145 to 147:

```markdown
그보다 오래된 릴리스로 고정된 워크플로는 `agentic pr-checks remove` 로 빼거나,
`--branch` 줄을 설치된 릴리스로 옮기고 mode 단계가
`skills/implement/scripts/agentic.py` 를 돌리게 고치기 전까지 그곳의 모든 PR 을
실패시키고, `agentic mode local` 은 그런 파일을 남길 때 고정된 릴리스를 알려 줍니다.
```

In `docs/running/the-review-and-parity-arms.md`, lines 157 and 158:

```markdown
runs a `chain-check` that reads no `original:` line, until a person writes
it again with `agentic pr-checks remove` and then `agentic pr-checks install`,
which pins the installed release. And a declaration
```

```iadd
verdict: fixed 9bc4b51f
answer: Applied in `9bc4b51f` at each place the location names but `frame/plan.md:61`. #1656's fragment, line 7, now tells a repository to write `.github/workflows/hygiene.yml` again with `agentic pr-checks remove` and then `agentic pr-checks install` once the release that carries this change is installed, and says that a copy whose tag alone moves still runs `skills/implement/scripts/seal.py` in its mode step, which this release does not ship. The pass wrote that sentence in its own words: the command `agentic` and the install's pin to the installed release exist only once that release is installed, which the paste-ready text left unsaid. `frame/keep.txt` line 39 takes the new line, and the acceptance A of `frame/design.md` *The keep file* prints nothing. `skills/implement/scripts/agentic.py#left_workflow_line` now names `agentic pr-checks remove` first, and then the `--branch` line moved with the mode step pointed at `skills/implement/scripts/agentic.py`; `tests/skills/test_agentic.py` pins the new words, and three `bin/agentic mutate` runs, one taking `mode` out of the clause, one taking `step` out and one naming `seal.py`, each failed the case's three parameters. The two editions of `docs/layout/one-root-by-lifetime.md` take the paste-ready text, the Korean one rewrapped, and `docs/running/the-review-and-parity-arms.md` takes it with *that file* for *it*, whose antecedent could be read as the repository. `frame/plan.md:61` is not changed: `agents/crafter.md` *Job* gives the crafter no frame line but its phase's Status cell, so the hand-back gives the orchestrator the paste-ready text. The work item's own `changelog.md` names no step a repository takes, so it owes this fix nothing. The evidence's `git grep`, run again at `c7f5fe66`, prints `frame/plan.md:61`, left to the orchestrator; #1656's `frame/plan.md:72`, a record that `frame/design.md` *Scope*, *Out of scope*, keeps byte for byte; this record's own lines; and `docs/layout/one-root-by-lifetime.ko.md:146`, `docs/layout/one-root-by-lifetime.md:155`, `skills/implement/scripts/agentic.py:1735` and `tests/skills/test_agentic.py:2924`, each of which now names the mode step beside the `--branch` line. A sample beyond it, ``git grep -n -i -E -- '--branch|v<version>|the pin\b|the pin.s|pinned to|older release|tag .{0,30}pins|pins .{0,20}tag|move.{0,20}(the )?(tag|pin)|고정|태그' -- . ':!agentory/threads' ':!*.py'`` and ``git grep -n -i -E 'pr-checks (remove|install)|hygiene\.yml' -- . ':!agentory/threads' ':!tests'``, found no other sentence that tells a person to move the pin alone: `README.md:102-105` and `README.ko.md:107-110` already give the removal and then the install, and `templates/setup/hygiene.yml:11-12` and `:25-27` speak of a copy of this release's template, whose mode step runs `agentic.py`. A statement of the step in words none of these searches holds is outside the sample.
```

### 2. The acceptance row for the root's discovery says the cases of `tests/lib/test_optin.py` verify that an `iadd/` is no root, and no case builds one

```iadd
severity: should
location: `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/design.md:69`
evidence: executed `git grep -n -i -F iadd -- tests/lib/test_optin.py`, which printed nothing; executed `git grep -n -F 'keeps in iadd/' -- tests evals`, which printed nothing; executed ``git grep -n -E '"iadd"\)|/ "iadd"|"iadd" /|iadd/README' -- tests``, which printed only fence lines of `tests/conftest.py` and `tests/lib/test_fields.py`; read `tests/lib/test_optin.py:319-336` and `:458-478`
```

Why it matters: the row's *Then* says that an `iadd/` whose README opens with `# What IADD keeps in iadd/` is no root and that the repository's root is then the local one. Its *Verifiable how* cell names the cases of `tests/lib/test_optin.py`. The inspector reads that cell as a pin of the clause. No case in that file, or anywhere under `tests/`, builds an `iadd/` or writes the old marker. The cases there build the root at `agentory/` alone, marked, foreign, absent or a file (`tests/lib/test_optin.py:319-336`, `:458-478`). The clause holds by reading: `lib/optin.py#home_paths` joins `HOME` and nothing else, and G3 says no reader accepts the old spelling. Phase 1's record writes no case, as the *Names or places only* row of `skills/verify/SKILL.md` *The narrow command still has to be able to fail* allows a rename. So the defect is the cell's claim, and the fix rewrites the cell. A case for the old name would put `iadd` into `tests/` under no kind *The keep file* gives.

```markdown
| The root is found under its new name alone | Given a repository whose `agentory/README.md` opens with `# What IADD keeps in agentory/`. When `bin/agentic mode` runs. Then it names that directory as the root. An `iadd/` whose README opens with `# What IADD keeps in iadd/` is no root, and the root of that repository is the local one | the cases of `tests/lib/test_optin.py`, which build the root at `agentory/` alone; that an `iadd/` is no root is read from `lib/optin.py#home_paths`, which joins `HOME` and no other name, and no case builds one |
```

```iadd
verdict: fixed f968c0a9
answer: The orchestrator applied the paste-ready row as given in `f968c0a9`, since a cell of `frame/design.md` is a frame statement the orchestrator narrows to HEAD. The row's *Verifiable how* now says the cases of `tests/lib/test_optin.py` build the root at `agentory/` alone, and that an `iadd/` is no root is read from `lib/optin.py#home_paths`, which joins `HOME` and no other name.
```

### 3. `routing.md` says this tree holds `iadd/`

```iadd
severity: should
location: `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/routing.md:24`
evidence: executed `git ls-tree -d HEAD -- iadd agentory` at `59cf3d37`, which printed `agentory` alone; read `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/routing.md:24`
```

Why it matters: the bullet *The parties' type* states in the present that this tree holds `iadd/`, and gives it as the reason the parties are spawned as `general-purpose` agents. Since phase 1's commit `2e156d57`, the tree holds `agentory/` and no `iadd/`. The reason still stands, because the installed 0.39.x reads only `seal/`, but the sentence an agent reads to judge the spawn names a root the tree no longer holds. The file is dated to the routing answer, and no frame section's dating covers it. `git grep -n -F 'tree holds' -- agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it` printed this line beside lines where the words state another fact: the acceptance's reading of a `<` line in `frame/design.md` *The keep file*, the keep files' copies of #1656's lines, and the phase records. That search is a sample.

```markdown
- **The parties' type.** The installed plugin is `agentic` 0.39.x, which reads a `seal/` root, and this tree held `iadd/` when the work was routed and holds `agentory/` from phase 1's commit. Neither is a root the installed plugin reads. As in #1656 after its phase 7, the framer, the crafter, the proofer and the inspector are spawned as `general-purpose` agents bound by this tree's `agents/<name>.md`, `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md`, and every subcommand runs from this tree's `bin/`.
```

```iadd
verdict: fixed f968c0a9
answer: The orchestrator applied the paste-ready bullet as given in `f968c0a9`, since `routing.md` is the orchestrator's record. *The parties' type* now says the tree held `iadd/` when the work was routed and holds `agentory/` from phase 1's commit, and that neither is a root the installed plugin reads.
```

## Confirmations

What matched: the acceptance of `frame/design.md` *The keep file*. A, run from the clone's root against `frame/keep.txt`, printed nothing and exited 0, and N printed `docs/method/iadd.md` alone (executed).

What matched: #1656's directory moved byte for byte. `git diff -M --name-status 801465cb HEAD` over both of its paths printed `R100` for each of its 20 files but `changelog.md`, which git reads as one deletion and one addition at this similarity. `python3 skills/code-review/scripts/chain_check.py --baseline 801465cb --root . --worktree` exited 0 and named only this work item's records (executed).

What matched: the root and the product sit in their layers. The word census and the two-way searches above printed no root joined as `agentic` and no product's file, variable, prefix or command spelt `agentory` (executed). `lib/optin.py:41` is `HOME = "agentory"` and `:76` the marker. The other readers take the name from `HOME`: `git grep -n -E '(optin|OPTIN|routing\.optin)\.HOME' -- '*.py' ':!tests'` printed 22 lines. Outside `tests/`, the quoted literal `agentory` stands in `lib/optin.py#HOME` and a docstring of that file, in `evals/scripts/rule_cases.py`, and in one message of `skills/verify/scripts/pact_check.py` (executed). `agentic import` refuses a member outside `optin.HOME` (`skills/implement/scripts/agentic.py:798-799`, read), as #1658's fragment says.

What matched: the names #1658's fragment says 0.39.4 shipped. `git grep -c -F` at `35bef264` found `AGENTIC_GATE_INVOKED_AS`, `AGENTIC_RECORD_DIR`, `AGENTIC_RECORD_KEY`, `agentic_pytest_record`, `agentic-scratch`, `agentic-stamp`, `agentic-stamp-refused`, `agentic-last-export.json`, `".claude", "agentic", "pact-paths.json"` and `$RUNNER_TEMP/agentic` (executed). `skills/update/SKILL.md` is byte for byte its 0.39.4 text (`git diff 35bef264 HEAD -- skills/update/SKILL.md` printed nothing, executed). `lib/core.py#HEADER` read `AgenticSeal core from` at 0.39.4, as #1656's rewritten first bullet says (executed).

What matched: `docs/method/iadd.md` *The names* against `frame/design.md` *The names in docs/method/iadd.md* and #1658's table. The rule opens the section. The three rows IADD, `agentic` and `agentory/` take the frame's sentences, and the `agentic` row names the `name`, the prefix, the command, the variables `AGENTIC_*`, the marketplace `agenticseal` and the repository. The rows for the thread, the agents, the inspection, the three states, the settle and `IADD-Routing:` stand as at the base with `agentory/`. The `iadd` block's row and the answer `agentic`'s row stand, and the sentence on lowercase identifiers is gone (read `docs/method/iadd.md:65-86`).

What matched: the Korean documents. `README.ko.md` and `docs/layout/one-root-by-lifetime.ko.md` are the two Korean files the range changes. No `agentic` is followed by a particle for a word that ends in a vowel, and no `agentory/` by one for a word that ends in a consonant, by `git grep` over `*.ko.md` (executed). `README.ko.md` takes `` `/plugin uninstall agentic` 을 `` and *agentic 은*, which the new name's reading takes (read).

What matched: the locator rule's pin goes red with phase 2's reason. With `the plugin's name and` taken out of the message at `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:298`, `bin/test ... -k repair` failed one case. The file was then restored with `git checkout --`, and `git status --short` printed nothing (executed).

What matched: the narrow cases of the acceptance rows and of the files the root and the plugin's name reach. `bin/test` over `tests/lib/test_optin.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/github/test_plugin_directory_check.py`, `tests/github/test_publish_release_note.py` and `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` passed 351 and skipped 9. `bin/test` over `tests/test_censuses.py`, `tests/behaviour/test_this_repository_passes_its_own_checks.py` and `tests/behaviour/test_release_hygiene.py` passed 264. `bin/agentic --help` printed `usage: agentic [-h]`. `bin/agentic mode --check` and `bin/agentic fold` exited 0 (executed). Each phase record labels the full suite `unverified` with the orchestrator as its answerer, and `gaps.md` *Not verified* holds a row for each phase. The labels are honest.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check of `agentory/config.json`'s `Broad gate` key | `gaps.md` *Not verified*, rows 1 to 5 | the orchestrator, at the broad run |
| Whether `/plugin install agentic@agenticseal`, `/agentic:update` and the `agentic:` agent types work in a real session once the release is installed | `gaps.md` *Not verified*, row 6 | the orchestrator, after the release is installed |
| Whether the hand-written proofer cases still reach their graders as `agentic:proofer` | `frame/questions.md` Q4 | a measurement, `evals/scripts/noninferiority.py run`, which the orchestrator or the owner starts |
| Whether #1656's entry in the 0.40.0 note may link to this pull request | `frame/questions.md` Q3 | the owner |

## Probes

| Command | Result |
|---|---|
| `git grep -P '(?i)iadd' -- . ':!agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it' \| LC_ALL=C sort \| diff - agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/keep.txt` | no output, exit 0 |
| `git ls-files -- . ':!agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it' \| grep -i iadd` | `docs/method/iadd.md` |
| `python3 -I census.py <clone> 801465cb..59cf3d37` and `35bef264..59cf3d37`, the word-pair script under the round's scratch directory | 272 and 2059 pairs. The two largest of the range are `iadd` to `agentory`, 1889, and `iadd` to `agentic`, 1740 |
| `python3 skills/implement/scripts/seal.py mode --check` at `59cf3d37` | exit 2: the file does not exist |
| `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:298` with `the plugin's name and` removed, then `bin/test <that file> -q -k repair` | 1 failed, 1 passed; the file restored with `git checkout --` |
| `python3 skills/code-review/scripts/chain_check.py --baseline 801465cb --root . --worktree` before the record was written | exit 0; notices for this work item's missing round, gate record and inspection |
