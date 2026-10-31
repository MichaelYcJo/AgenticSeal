# Review round 1: 1793438028-pre-0-23-upgrade-readings-removed

```seal
target: d25aad94 against origin/release/v0.27.0
```

This round reviews phase 1, `b212e774..d25aad94`, against the frame at `8a6c5a4b` (`frame/design.md`, `frame/plan.md` row 1). No earlier round exists, so no fact was carried; every coordinate below was opened this round. Phases 2 and 3 are not built, and what they own (`hooks/stub-remove.py`, the update skill's old markers, `seal.py#OLD_PLUGIN_CLONE`, README *Coming from `specseal@specseal`*) is not judged here.

## Findings

### 1. Three sentences outside `docs/` still describe the removed migration, one of them a docstring the frame names for correction

```seal
severity: must
location: `tests/hooks/test_optin.py:432-435`, `tests/hooks/test_optin.py:562-563`, `skills/implement/bootstrap.md:29-31`
evidence: executed `git grep -n -E 'session-start|the migration (write|question)|migration$' d25aad94 -- tests/hooks/test_optin.py skills/implement/bootstrap.md`, `git ls-files hooks/root-migrate.py`
```

The frame lists `tests/hooks/test_optin.py`'s legacy-directory case among the cases kept, and says "Each docstring that says `hooks/root-migrate.py` reads the name is corrected (item 9)" (`frame/design.md:109-115`). Phase 1's plan row takes "the part of item 9 that cites `hooks/root-migrate.py`". The case is `test_refuses_the_legacy_directory`, and its docstring still says a repository holding `.specseal/` stands as any other "until the session-start hook moves it, which is the only thing that reads the name" (`tests/hooks/test_optin.py:432-435`). No hook moves it: `git ls-files hooks/root-migrate.py` prints nothing at `d25aad94`. The crafter corrected the scratch case two cases above it (`:419-421`) and left this one.

Two more sentences of the same class are outside the crafter's search, which `gaps.md` *Not verified* hands to this round as a sample for paraphrase.

- `tests/hooks/test_optin.py:562-563` says "The template is what first setup and the migration write into a root". The migration was `hooks/root-migrate.py#rewrite_readme`. The phase rewrote the same clause in `hooks/lib/optin.py`'s comment above `MARKER` to "which first setup writes", and left this copy.
- `skills/implement/bootstrap.md:29-31` says "this is the only place the mode and the migration question are asked at all". That sentence was written (`5aed51cb`) above a paragraph that asked about the 0.3.x layout. Since then the 0.3.x repository was told rather than asked, and this phase removed the paragraph that told it. Step 1 now carries two questions, the mode and the `Broad gate` row (`skills/implement/bootstrap.md:44-46`), and no migration question. An orchestrator reading the sentence is told a question exists that the bootstrap never asks.

The class is any sentence that states the session-start move or the 0.3.x migration as current. Paraphrase is an unbounded domain, so the search in *Probes* is a sample, and the fix pass names its own method.

```python
# tests/hooks/test_optin.py, test_refuses_the_legacy_directory
        """S3. Without this case the constant can come back and everything stays
        green.

        `.specseal/` reads as an ordinary directory now. A repository still
        holding one is a repository that never opted in, which is the same
        standing as any other repository on the machine, and nothing reads
        the name.
        """

# tests/hooks/test_optin.py, Test_module.test_the_template_opens_with_the_marker
        """The template is what first setup writes into a root, so its first
        line and the constant are one value, pinned here."""
```

```markdown
<!-- skills/implement/bootstrap.md, the paragraph's last sentence -->
not know to ask, so this is the only place the mode is asked at all.
```

```seal
verdict: fixed 885b3c1f
answer: The finding holds for the two `tests/hooks/test_optin.py` docstrings, and both now carry the round's text. For `skills/implement/bootstrap.md:29-31`, the sentence was wrong to read but not in the way the round says. "The migration question" did not mean the 0.3.x move. It came from 716d8548, where the sentence read "the only place the migration question gets asked" above the question "Does this project port behavior from an existing codebase?". The bootstrap still asks that question, in its step 3 (`skills/implement/bootstrap.md:163-165` at 885b3c1f). The round's paste-ready text, "the only place the mode is asked", would drop a question the bootstrap asks. So the fix is in my words: "the only place the mode, and whether the project ports an original codebase, are asked at all". Both fixes are in 885b3c1f. `bin/test tests/hooks/test_optin.py tests/behaviour/test_first_setup_asks_once.py` passed, as did the other five modules that read `bootstrap.md` (executed). The class sweep covered every file phase 1 touched, plus `skills/`, `templates/`, `agents/`, `hooks/`, both READMEs, `CONTRIBUTING.md`, `CLAUDE.md` and `seal/README.md`. It searched with `git grep -i -E` for moves of a root or records, `migrat`, `session[- ]start`, `earlier release`, `before the rename`, `0.22`, `0.3.x` and `old`/`earlier layout`, and a second pass covered `docs/` in English and Korean. It found no further sentence that states the move as current outside `docs/`. Every `docs/` hit stands inside a `from` of `## Rule changes`, or is phase 2's (`docs/the-routing-check.md:22-25`) or unrelated (`docs/release-checklist.md:220`, the experiments). Four hits stand on purpose. `skills/settle/SKILL.md:173` and `rule_changes.py:343` describe threads `#EARLIER` still places, which the frame keeps. `tests/behaviour/test_first_setup_asks_once.py:681` says a paragraph was replaced, which is history. `tests/hooks/test_dispatch.py:1149` names the move as what the group no longer runs. Paraphrase is unbounded, so this sweep is a sample too.
```

### 2. The old-roots scan still exempts a `specs/<` after a `/`, an exception whose only lines this phase removed

```seal
severity: should
location: `tests/behaviour/test_no_document_names_the_old_roots.py:29-31`
evidence: executed `git grep -n -F '/specs/<' b212e774 -- templates skills agents docs README.md README.ko.md seal/README.md CONTRIBUTING.md CLAUDE.md SECURITY.md .github/workflows`, `git grep -n -F '/specs/<' d25aad94 -- templates skills agents docs README.md README.ko.md seal/README.md CONTRIBUTING.md CLAUDE.md SECURITY.md .github/workflows`
```

`OLD_ROOT` is `\.specseal/|(?<![\w/.])specs/<`, and its comment says a `specs/<` after a `/` is "the 0.22.x `seal/` layout the migration names". At `b212e774` the only scanned lines that hold `/specs/<` are the two READMEs' by-hand step `git mv specs/<id> seal/specs/<id>` (`README.md:407`, `README.ko.md:399`). Phase 1 removed both sections and the migration. At `d25aad94` no scanned line holds `/specs/<`, so the `/` in the lookbehind and the comment's clause stand on a fact that is gone.

The exception is not inert. With it, a shipped document can tell a session to write under `seal/specs/<id>/`, the 0.22.x layout, and the scan passes. Nothing reads that layout any more, which is the miss the module's docstring says it exists to catch ("sends that session to write a file nothing reads"). `skills/core/SKILL.md` *The rule a mechanism is kept against* asks that a change remove, in the same commit, the exception that stood on the old fact. The narrowed pattern below can flag no line in the scanned set today, because the second search above prints nothing. The fix pass still runs the module.

```python
# `.specseal/` anywhere; `specs/<` unless it is part of a longer path segment.
OLD_ROOT = re.compile(r"\.specseal/|(?<![\w.])specs/<")
```

```seal
verdict: fixed 88d4f27c
answer: Fixed in 88d4f27c with the round's pattern and comment. The exemption now refuses a line it used to pass, so `test_the_check_can_fail` gains the line "write it under `seal/specs/<work-item-id>/`". That line carries an `# exempt from old_names:` comment, because `tests/test_censuses.py`'s census refused the old spelling in it (executed). The case was seen red against the old lookbehind with `bin/seal mutate tests/behaviour/test_no_document_names_the_old_roots.py --replace` (the new pattern swapped back to the old) `--tests "bin/test tests/behaviour/test_no_document_names_the_old_roots.py -q -p no:xdist -k test_the_check_can_fail"`, which printed `red` (executed). `bin/test tests/test_censuses.py tests/behaviour/test_no_document_names_the_old_roots.py -q` gave 194 passed, so the narrowed scan flags no line in the scanned set (executed).
```

## Confirmations

```seal
confirms: none
```
Departure 1, the moved case. The crafter claimed that `test_no_hook_names_the_0_3_x_roots` moved into `tests/behaviour/test_no_document_names_the_old_roots.py` without its rider assertion, because the policy sentence it holds stays after the settle. The case stands at `tests/behaviour/test_no_document_names_the_old_roots.py:99-109`. The rider assertion read `hooks/root-migrate.py`, which is deleted, so the dropped line had nothing left to read. The policy sentence "no code of the plugin opens a top-level `specs/` or `.specseal/`" is kept by the first item of *Rule changes* (`frame/design.md` *Rule changes*, its `to:` text). Read against its group: `tests/censuses.py:1041-1044` keeps `.specseal` in `KEPT_OLD_NAMES`, so the census does not refuse the name in a hook, and no other case reads `hooks/` for it. The case covers something no other case covers. The module passed (executed, *Probes*). The crafter's mutation run was not re-run (read).

```seal
confirms: none
```
Departure 2, the dropped `move` needle. The crafter claimed that the two needles describe the move and that *Rule changes* removes them at the settle. `frame/design.md:223` holds "on each branch whose tree still holds them" inside the `remove` item for *What first setup asks*. `frame/design.md:258` holds "앞선 배치가 남아 있는 브랜치마다" inside the Korean `remove` item. The kept needles, `templates/setup/hygiene.yml`, the common directory and `AskUserQuestion`, stand in no `from` text. Kept, the needle would go red at the settle in a session that did not cause it, the reasoning `frame/plan.md` Alternatives I applies. The module passed (executed).

```seal
confirms: none
```
Departure 3, the `ruff.toml` floor entry. The crafter claimed the `seal.py` entry was stale once `hooks/root-migrate.py` left, and that `tests/hooks/test_launch.py::Test_module::test_what_runs_before_any_floor_is_linted_at_the_floor` refused it. The case at `tests/hooks/test_launch.py:202-232` fails on a table entry that no floorless run reaches. It passes at `d25aad94` without the entry (executed). The crafter grounded the 3.12 floor in `.github/workflows/test.yml`. The floorless runs of `seal.py` are elsewhere: `.github/workflows/hygiene.yml:165` and `templates/setup/hygiene.yml:90` run `python3 seal.py mode --check` on `ubuntu-latest` (`:36`, `:52`), outside `hooks/lib/launch.py`. Those runs never reach `datetime.UTC`, which `seal.py` reads only inside `manifest_of` and `export` (`skills/implement/scripts/seal.py:521`, `:650`), so the change holds there too (read).

```seal
confirms: none
```
The contract departure on `tests/test_censuses.py`. The caller relays that the crafter edited this file through a shell script and not the `Edit` tool, and `trail/phases/phase-1.md` does not record it. The edit landed whole: both fixture tuples swap `hooks/root-migrate.py` and `tests/hooks/test_root_migrate.py` for the two files `KEPT_FILES` still names (`tests/test_censuses.py:818-819`, `:835-836`), and the module passed (executed). The branch's `routing.md` declares the branch, so the edit check the shell bypassed would have let the edit through. Whether the process departure is worth a record row is the orchestrator's call.

```seal
confirms: none
```
The *Removes* rows phase 1 owns are carried out at `d25aad94` (read, the diff `8a6c5a4b..d25aad94`). These are `hooks/root-migrate.py` and its two test files; `root-migrate.py` in `hooks/dispatch.py#GROUPS`; `optin.EARLIER_HEADINGS`, `optin.earlier` and the module docstring clause; `seal.py#earlier_root` and its three calls, with its case in `tests/skills/test_seal.py`; the bootstrap's two paragraphs and "nor one of those headings"; the `skills/config/SKILL.md` paragraph; the exception sentence in `templates/setup/seal-README.md` and `seal/README.md`, whose blobs stay equal (both `7b887f5a`); both READMEs' 0.3.x section and `root-migrate` gate row; the 0.3.x case with `OLD_LAYOUT` and `EARLIER_SEAL`; the three `KEPT_FILES` entries and the `.specseal` comment; the four `KEEP` entries; the `LISTS_A_FIXTURE` entries; `agents/proofer.md`'s check target; and the `seal.py` and test docstrings the row names. No living file outside `docs/` and the work item's records names a removed unit, except `tests/behaviour/test_chain_hooks_hardening.py:92`, which `frame/design.md` *Out of scope, found and kept* keeps as history (executed, *Probes*). `seal rules --check` holds, and the citation case passes over the `docs/` lines that still cite the removed units inside a `from` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at this branch's head: the full suite, the repository-wide `ruff check` and `ruff format --check`. This round ran seven modules and `seal rules --check`, labelled in *Probes*, and the suite stays `unverified` | `gaps.md` *Not verified*, row 1 | the orchestrator, by `seal gate` |
| Whether phase 1's sweep left a sentence describing the removed move in words no pattern holds. Finding 1 is what this round's search found, and that search is a sample: paraphrase is unbounded | `gaps.md` *Not verified*, row 2 | the fix pass, by its own enumeration, and the next round |
| Whether the `Test_classify` case that now plants its shape under `stub-remove.py` keeps a neighbour gate once phase 2 empties the group | `tests/hooks/test_dispatch.py:465`, `trail/phases/phase-1.md` *For phase 2* | phase 2's crafter, and the round that reviews it |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_launch.py tests/behaviour/test_no_document_names_the_old_roots.py tests/behaviour/test_first_setup_asks_once.py tests/test_censuses.py -q` | 247 passed, exit 0 |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_chain_hooks_hardening.py tests/hooks/test_optin.py -q` | 131 passed, exit 0 |
| `python3 .github/scripts/rules.py --check` | "all 265 check lines in 54 rule files hold", exit 0 |
| `git grep -n -I -i -E` for `root-migrate`, `root_migrate`, `EARLIER_HEADINGS`, `earlier_root`, `optin.earlier`, `rename_state`, `THREAD_PATHS`, `test_the_root_migrates_itself`, `Coming up from 0.3` and `0.3.x 에서` over `d25aad94`, outside `seal/threads`, `CHANGELOG.md` and `.test_durations`, with `evals/` included | nine lines: eight in `docs/`, each inside a `from` of *Rule changes*, and `tests/behaviour/test_chain_hooks_hardening.py:92` |
| `git grep -n -I -i -E` for paraphrases of the move (`session-start move`, `the migration`, `migration hook`, `waiting for its move`, `earlier release`, `earlier layout`, `earlier root`, `before the rename`, `0.22.x`, `seal/specs`, `old layout`, `specseal-`, `.claude/specseal`, `moves a work item`, `moves the layout`) over `d25aad94`, outside `seal/threads`, `CHANGELOG.md`, `.test_durations`, `evals/` and `docs/`; then every phase-1 file read for `move`, `migrat`, `0.22`, `0.3.x`, `earlier` and `rename` | three sentences found, finding 1. Every other hit is the migration config of `seal/parity.md`, phase 2's or phase 3's, or history *Out of scope, found and kept* names |
| `git grep -n -F '/specs/<'` over the scanned set at `b212e774` and at `d25aad94` | two README lines at `b212e774`, none at `d25aad94`, finding 2 |
