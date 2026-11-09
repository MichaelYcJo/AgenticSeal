# Review round 1: 1794200905-a-foreign-seal-dir-keeps-the-records-shared

```seal
target: 2159b115 against origin/release/v0.37.0
```

This is a finding round over the whole branch. The base `origin/release/v0.37.0` is `c0bf670d`, and it is also the merge base, so `git diff c0bf670d 2159b115` holds this item's changes alone, the merge `71a77691` bringing in #1445 and #1459 adding nothing of theirs to it (executed: `git merge-base HEAD origin/release/v0.37.0`). The round worked in a `git clone --no-local` of the worktree at `2159b115`. No earlier round exists, so this round carried no fact and re-established every fact it uses. `seal/parity.md` is not declared, so no parity comparison applies. The record language is English (`seal/config.md`), and `Commit and pull request language` is English, so no `pr.<lang>.md` is owed.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` to `phase-4.md` whole at `2159b115`, and issue #1059 with its comments (executed: `gh issue view 1059 --json title,body,state` and `gh issue view 1059 --comments`). Every quote of `pr.md` stands word for word in `changelog.md` or `gaps.md` at the coordinate it names (executed: `grep -cF` of each quote, each 1).

## Findings

### 1. Beside a project's own `seal/`, `seal pr-checks install` refuses by saying `seal/` is not in the tree, where the person's package stands

```seal
severity: should
location: `skills/implement/scripts/seal.py:1971-1976`, `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py:274`
evidence: read `skills/implement/scripts/seal.py:1961-1976`, `lib/optin.py:200-202`, `skills/implement/scripts/seal.py:2215-2217`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/design.md:34`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/changelog.md:7`
```

Why it matters: the changelog's *Updating* line sends exactly this repository to the plugin again: one that first setup put in local mode because its own `seal/` stood there (`changelog.md:7`). There, `install_workflow` takes the shared place from `optin.home_paths`, which is `<repo>/agentic-seal` because `seal` stands unmarked (`lib/optin.py:200-202`), finds it unmarked, and prints `f"{WORKFLOW} was NOT written: {optin.HOME}/ is not in this tree, ..."` (`seal.py:1974`). The person reads "seal/ is not in this tree" with their package's `seal/` in the tree in front of them. *Scope* item 3 (`frame/design.md:34`) says a path a person reads in a message is the real path. Phase 1 claimed every message of `seal.py` that names the root was built and mutated (`phase-1.md` table: `refusals`, `switch`, `import_`, `export`). `install_workflow` is the same module's message of the same class and is not on that list, so the list was a sample of the class rule 12 asks for. The case at `:274` holds only the shared state, so no case reads this line beside the package.

The fix names the shared place by its own name and states what is missing there, which holds in both states the shared place can be in, absent and the project's own (the *Out* item on both names). No case pins the old text (executed: `git grep -n "is not in this tree" -- tests` lists nothing).

```python
    shared, _local = optin.home_paths(repo)
    if not shared or not optin.marked(shared):
        # The shared place by its own name: beside a project's own `seal/`
        # it is `optin.SECOND_HOME`, and the project's `seal/` stands in the
        # tree, so "seal/ is not in this tree" would be false there (#1059).
        name = display(repo, shared) or optin.HOME
        return "no-root", (
            f"{WORKFLOW} was NOT written: no root stands at {name}/ in this "
            "tree, and the checks read committed records, which only a root in "
            f"the tree has. `seal mode {SHARED}` puts it in the tree."
        )
```

```python
def test_pr_checks_install_names_agentic_seal_where_no_root_stands_beside_the_package(
    package, capsys
):
    """With no root beside the package, `seal pr-checks install` writes
    nothing and names the place it looked by its own name, `agentic-seal/`,
    not the package's `seal/`, which stands in the tree."""
    code, out = said(capsys, package, "pr-checks", "install")
    assert code == 1, out
    assert "no root stands at agentic-seal/ in this tree" in out, out
    assert not (package / ".github").exists()
```

### 2. The root's README gives the by-hand moves with `seal` in every path, and says to substitute only after them, pointing at a paragraph that does not give the name

```seal
severity: should
location: `templates/setup/seal-README.md:38-48`, `seal/README.md:38-48`
evidence: read `templates/setup/seal-README.md:36-48`, `templates/setup/seal-README.md:60-71`, `tests/behaviour/test_first_setup_asks_once.py:516-537`, `tests/behaviour/test_first_setup_asks_once.py:603`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/trail/phases/phase-4.md:55-63`
```

Why it matters: this file is the root's own `README.md`, so in the repository #1059 serves it is `agentic-seal/README.md`, and a person reading it there is beside their package's `seal/`. The paragraph gives the moves as commands to run: from shared to local, `git rm -r --cached "$(git rev-parse --show-toplevel)/seal"` and `mv "$(git rev-parse --show-toplevel)/seal" "$(git rev-parse --git-common-dir)/seal"` (`:42-43`). Run as written there, they untrack the person's package and move it under the git directory, and the local-to-shared pair moves the local root to `seal/seal`. The sentence that says to substitute stands in the next paragraph (`:46-48`), after the commands. It says the name is the one "the marker paragraph below gives", and the marker paragraph (`:60-71`) gives no name: it says "the second name `skills/core/SKILL.md` defines", a file of the plugin, not of the person's repository. Phase 4 put the sentence apart because `switch_block` reads exactly two code spans after each lead (`phase-4.md:55-63`). That test reads only the text after `From local to shared:` (`test_first_setup_asks_once.py:531-537`), so a sentence before that lead, in the same paragraph, leaves its spans as they are.

The fix moves the sentence ahead of the commands and names the folder by the README's own place. It writes no `agentic-seal`, which `test_no_other_scanned_file_states_the_second_name` refuses in a scanned file. Both files take the same text, since `test_first_setup_asks_once.py:603` holds them byte-identical.

```markdown
location is the only signal. The by-hand move asks git for both paths, so
the commands land the same from a subdirectory. Where the folder holding
this file is not named `seal`, as beside a project's own `seal/`, each
`--show-toplevel` path below ends in this folder's name in place of `seal`;
run as written there, the commands would move the project's own directory.
From local to shared:
`mv "$(git rev-parse --git-common-dir)/seal" "$(git rev-parse --show-toplevel)/seal"`,
`git add "$(git rev-parse --show-toplevel)/seal"` and a commit. From shared
to local: `git rm -r --cached "$(git rev-parse --show-toplevel)/seal"`,
`mv "$(git rev-parse --show-toplevel)/seal" "$(git rev-parse --git-common-dir)/seal"`
and a commit of the removal.
```

The paragraph that stood at `:46-48` goes with this change. The changelog's third item says the template "says that the by-hand moves end in the root's own name" (`changelog.md:5`), which stays true.

### 3. The folds left two frame statements of the two-name design for `chain_check.py`, which a renamed root contradicts

```seal
severity: should
location: `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/plan.md:24`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/design.md:45`
evidence: executed `bin/test tests/behaviour/test_tmp_root_renamed.py -q -p no:xdist` (the probe of `## Probes`); read `skills/code-review/scripts/chain_check.py:1840-1860`, `skills/code-review/scripts/chain_check.py:2061-2090`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/design.md:76`
```

Why it matters: phase 2 replaced the frame's two names with one, `chain_check.py#root_name`: the marked root of the tree the check reads, else the merge base's, else `optin.HOME` (`chain_check.py:1840-1860`). The fold `948ff0da` rewrote *Data & interfaces* to say so (`design.md:76`), and left two sentences that state the earlier design. `frame/plan.md:24` says the root-leaving test "asks for HEAD's entry at the merge base's name". `frame/design.md:45` says a reader at another commit reads under the working tree's name "except `chain_check.py`'s test of a root leaving", so the declarations, the designs the pull request edits and the parity config are said to follow the working tree's name, and only the root-leaving test the merge base's. In the tree, every one of those reads takes `root_name`'s one name (`chain_check.py:2061-2090`). The two statements disagree in the case *Out* names. The probe built a marked `seal/` at the merge base, renamed it to a marked `agentic-seal/` on the branch beside a new package `seal/__init__.py`, and ran the check. The branch's declaration was judged under `agentic-seal/threads/` (exit 1, its missing `trail/gate.md` and `guarantee.md` named). `frame/plan.md:24` predicts the opposite: the merge base's name is `seal`, and HEAD's `seal` entry is the new package, so the test would read the package as the root that stayed. With the package absent, it would read the root as gone and declare nothing. The same probe deleted another work item's `routing.md` under the old name without moving it, and the check named nothing of it: a declaration deleted under the old name in a rename is not judged. That is *Out*'s limit, and `design.md:45` does not say it. A sealer or a later item reading either sentence judges the rename by a design the tree does not run.

The one-name build is the better of the two for this case, as the confirmation below says, so the fix is to the frame. The fix pass writes no frame file, so the orchestrator's fold owes these two sentences.

```markdown
| `chain_check.py` reads the root as leaving where HEAD has no marked root | A pull request that deletes only `README.md` reads as declaring nothing, where today a `seal` entry of any kind keeps the declarations judged (G11). | rejected; the test asks for HEAD's entry at the name `chain_check.py#root_name` gives, the marked root of the tree the check reads and else the merge base's (`frame/design.md` *Data & interfaces*) |
```

```markdown
- **A root renamed between commits.** A reader that reads at a commit other than the working tree reads under the name the working tree resolves, except `chain_check.py`, which reads every record under the one name `root_name` gives: the marked root of the tree it reads, else the merge base's (*Data & interfaces*). A pull request that renames the root is read under the new name, and a declaration it deletes under the old name without moving it is not judged. A repository that moved its root from one name to the other reads its earlier history under the current name. This is a limit, stated in `home_paths`'s docstring and `chain_check.py#root_name`'s.
```

### 4. The core says `seal/` names the records root in every shipped text, and its next sentence and the bootstrap use `seal/` for the project's own directory

```seal
severity: should
location: `skills/core/SKILL.md:23-26`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/changelog.md:5`
evidence: read `skills/core/SKILL.md:18-26`, `skills/implement/bootstrap.md:37-44`, `templates/setup/seal-README.md:60-63`, `skills/config/SKILL.md:26-29`, `skills/agent-contract/SKILL.md:125-133`
```

Why it matters: the core is read by every agent and every session, and it says "`seal/` is that root's name in every text this plugin ships" (`:23-24`). Its next sentence opens "Where the repository's own `seal/` belongs to something else" (`:24`), where `seal/` is the directory named `seal` and not the root. The texts that tell an agent what to do with that directory use it the same way: the bootstrap's "A `<repo>/seal/` whose `README.md` does not open with the marker is the project's own" (`bootstrap.md:37-38`), the template's "every gate passes over a `seal/` whose `README.md` does not open with it" (`seal-README.md:61-62`), and the config skill's "a `seal/` made here without that README" (`config/SKILL.md:28-29`). Read under the core's definition, the bootstrap's sentence says the shared root without its marker is the project's own, which beside a package is `agentic-seal/`. `skills/core/SKILL.md` *Each agent judges its own target* holds every sentence an agent reads to one reading by `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, whose second rule refuses one word carrying two meanings. The definition can keep the owner's design and name its exception, so every one of those sentences reads one way under it.

```markdown
lifetimes* places. `seal/` is that root's name in every text this plugin
ships, except where a text says a `seal/` is the project's own or that its
`README.md` does not open with the marker: that is the directory named
`seal`. Where the repository's own `seal/` belongs to something else, the
shared root is `agentic-seal/`, recognised by the same marker,
`lib/optin.py#MARKER`, as the first line of its `README.md`.
```

The changelog's third item paraphrases the core's sentence ("says that `seal/` is the root's name in every text the plugin ships", `changelog.md:5`), so the fix pass owes it the same exception. `pr.md` does not quote that sentence.

### 5. The changelog and `pr.md` say one case holds the second name to the core and to each README, where three cases do

```seal
severity: should
location: `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/changelog.md:5`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/pr.md:7`
evidence: read `tests/behaviour/test_no_document_names_the_old_roots.py:325-359`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/trail/phases/phase-4.md:22-29`
```

Why it matters: the release note reads "a case in `tests/behaviour/test_no_document_names_the_old_roots.py` holds the second name to the core's sentence and to one line of each README". The module holds three: `test_the_core_states_the_second_name_once`, `test_each_readme_states_the_second_name_on_one_line_of_shared_or_local` and `test_no_other_scanned_file_states_the_second_name` (`:325-359`), as phase 4 says (`phase-4.md:22-29`). `pr.md:7` quotes the sentence, so the body the pull request carries says it too. The fix changes the changelog's clause and the quote in the same words, since `seal pr-body` copies the quote and the sealer reads it against its source.

```markdown
A census in `tests/censuses.py` refuses a string constant that spells either name in any module outside `lib/optin.py`, and three cases in `tests/behaviour/test_no_document_names_the_old_roots.py` hold the second name to the core's sentence and to one line of each README.
```

## Confirmations

What matched: S3, the pull request that deletes the root and the one that deletes only its marker (`tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py:390-404`, `:487-507`). The cases ran and passed at the target (executed: `bin/test` over the behaviour module, `tests/lib/test_optin.py` and `tests/behaviour/test_no_document_names_the_old_roots.py`, 128 passed). Read against `chain_check.py:1840-1860` and `:2083-2090`: deleting `agentic-seal/` leaves HEAD no marked root, `root_name` takes the merge base's `agentic-seal`, and `git ls-tree HEAD -- agentic-seal` is empty, so nothing is declared. Deleting only the marker gives the same name and an entry that stays, so the declaration is judged.

What matched: the one name of phase 2, judged against the frame's two. Where HEAD carries a marked root, the frame's second name, the merge base's, differs from HEAD's only for a renamed root. For that case the probe of finding 3 showed the one-name build judging the branch's declaration under the new name. The frame's version would have asked for the old name's entry at HEAD, which is the new package or nothing. The departure removes a mechanism the mutants showed nothing caught (phase 2: dropping either `changed_routing` call stayed green), and reads the case *Out* names better than the two-name design. What it leaves, a declaration deleted under the old name in a rename, is the limit finding 3 asks the frame to state. The `optin.HOME` fallback where neither tree is marked keeps every existing fixture's unmarked `seal/threads/` read as before, which S7 asks for.

What matched: the surviving mutant of `edited_work_items`'s `depth` (`chain_check.py:1400-1414`) is equivalent (read). `depth` is the number of parts of `work_items`, and `work_items` is always `f"{home}/threads"` with `home` from `root_name`, which returns only `optin.HOME` or `optin.SECOND_HOME` (`lib/optin.py:219-222`, `chain_check.py:1856-1860`). Both are one path segment, so a mutant computing `depth` from `seal/threads` gives the same number for every input the check can hand it.

What matched: the `root_name` census in place of a text case with an allowlist (`tests/censuses.py:1429-1526`). The module docstring makes a census the home of a rule every tracked file of a kind keeps, and says no census keeps a list of exemptions (`tests/censuses.py:17-24`). The three `# exempt from root_name:` lines stand at `lib/fields.py:68`, `skills/implement/scripts/seal.py:2764` and `skills/settle/scripts/rule_changes.py:653`, each above a constant that names no directory or a path of 0.22.x history. An exemption that excuses nothing is refused (`tests/test_censuses.py`, `test_accepts_a_line_an_exemption_excuses_and_refuses_one_that_excuses_nothing`). The census, its cases and the tree-wide run pass at the target (executed: `bin/test tests/test_censuses.py tests/behaviour/test_every_tracked_file_meets_every_census.py tests/behaviour/test_first_setup_asks_once.py -q`, 274 passed). Its limits stand in its comment (`tests/censuses.py:1443-1447`). *Scope* item 4 now states the census, so frame and tree agree.

What matched: both READMEs, read as a person setting up a repository whose own `seal/` is a Python package (`README.md:186-190`, `README.ko.md:189-193`). The sentence stands below the table of answers in *Shared or local*, says the plugin leaves the package alone, that both shared answers put the root at `<repo>/agentic-seal/`, that in shared mode each `seal/` the README names means that folder, and that only local is offered where that name is taken too. Each of those holds in the code: `home_paths` (`lib/optin.py:200-202`), `home_at` (`:327-329`), and the bootstrap's paragraph (`skills/implement/bootstrap.md:37-50`). *Where the records live* points back to that section without the name (`README.md:284`, `README.ko.md:287`). The two READMEs say the same in each language. What would mislead that person is the root's own README of finding 2, not these lines.

What matched: S1, S2, S4, S5 and S6 each have a case that names the second place by its path, and the cases pass (executed, the 128 above). The removals *Removes* names are gone from the tree (read: `lib/config.py:588-600`, `lib/gate.py:15-26`, `lib/routing.py:94-97`, `skills/implement/scripts/seal.py:1437-1440`, `skills/settle/scripts/settle.py:205-210`, `.github/scripts/publish_release_note.py:139-149`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| S7: the full suite, the lint and the typecheck at `2159b115`, which this round did not run (contract rule 2); the suite is `unverified` | `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/gaps.md:7` | the orchestrator, at the broad gate |
| Issue #1059's *Done when* says "no other document states the second name", and both READMEs state it. The frame grounds the exception on the owner's request of 2026-11-09, which reached the frame through the orchestrator's prose and stands on no comment of the issue; this round cannot read the owner's words | `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/plan.md:60`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/design.md:26` | the orchestrator, who relayed the request, and the sealer, who reads the issue against the tree |
| `pr.md` closes #1059 while `frame/questions.md` Q1, the measurement the *Done when* asks for, is `open`, and `gaps.md` names it owed | `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/pr.md:11`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/questions.md:17` | the orchestrator, by the measurement Q1's default names |
| The `agentic-seal/` cases and `home_paths`'s `lexists` fallback on Windows | `lib/optin.py:200-202` | CI's Windows leg |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_root_renamed.py -q -p no:xdist`, a probe that commits a marked `seal/` with two declarations on `main`, then on `feature` runs `git mv seal agentic-seal`, adds `seal/__init__.py` and commits, and runs `chain_check.py --baseline main` as a ready pull request; a second parameter also removes the other item's `routing.md` with `git rm -qf` before the commit | First run: the first parameter printed `agentic-seal/threads/1794200001-a-declared-item/trail/gate.md:0` and `.../guarantee.md:0` refusals and exited 1; the second errored in the probe's own `git rm` without `-f`. Re-run with `-f` and `-k True`: the same two refusals, exit 1, and no line naming `seal/threads/1794200009-other/routing.md`. The probe file is deleted |
