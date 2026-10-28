# Review round 1: 1793174170-two-facts-kept-in-several-files-have-drifted

target: bcc09e2f against 5287dd42

## Findings

### 1. The pointer that replaced the opt-in list leaves out implementer-notice

severity: should
location: `README.md:176`, `README.ko.md:170`, `README.md:114`, `README.md:419-423`, `README.ko.md:110`, `README.ko.md:411-415`, `tests/behaviour/test_first_setup_asks_once.py`
evidence: read `README.md:114`, `README.md:175-176`, `README.md:419-423`, `README.ko.md:110`, `README.ko.md:169-170`, `README.ko.md:411-415`, `hooks/implementer-notice.py:147`
verdict: fixed 21369c34
answer: The finding holds: `hooks/implementer-notice.py#notify` returns "" where `optin.opted_in(cwd)` is false, and the cell pointed at the row above. Both cells now carry the replacement text above, word for word, and the pointer sentences in *First run* and the `seal/` row are unchanged. `test_the_gates_table_says_the_root_may_sit_under_the_git_dir` in `tests/behaviour/test_first_setup_asks_once.py`, a path this finding's location did not list, now reads the notice's row among the `seal/` rows. It also refuses any Where cell that opens with "same " or "같은 ", the class a pointer by `seal/` drops. Run before the README fix, it failed for both editions with exit 1. After the fix the module passed, 51 cases, exit 0. `seal mutate` putting "같은 옵트인" back in Korean, and "the opt-in above" in English, went red with exit 0 each. No other Where cell in either table pointed at another row (read).

`frame/design.md` S2 replaces the list of opt-in hooks with a pointer to the
gate table. The `seal/` row now says the opt-in is read "for each hook whose
Where column under *The gates* below names `seal/`" (`README.md:114`). *First
run* says the same thing: "A gate whose Where column names `seal/` acts in a
repo that has a `seal/` directory" (`README.md:420`). The Korean edition says
it at `README.ko.md:110` and `:412`.

The implementer-notice row's Where cell does not name `seal/`. It reads "same
opt-in" (`README.md:176`) and "같은 옵트인" (`README.ko.md:170`), which means
the row above it. The hook is gated on the opt-in:
`hooks/implementer-notice.py:147` returns when `optin.opted_in(cwd)` is false.
At `5287dd42` the list named "the two implementer hooks", so the notice was
counted among the opt-in hooks. A reader who follows the new pointer word for
word finds eight rows that name `seal/` and misses the notice. An agent reads
it the same way. `CLAUDE.md` *text an agent or a check reads has one reading*
rules out a pointer that selects by a word one of the selected rows lacks.

`tests/behaviour/test_first_setup_asks_once.py#test_the_gates_table_says_the_root_may_sit_under_the_git_dir`
also selects rows by `` `seal/` `` in the Where cell, so it skips this row
too. Writing the cell out in full fixes the pointer and brings the row under
that case. The fix changes no sentence the pointer stands in.

In `README.md:176`, replace the last cell `same opt-in` with:

```markdown
`seal/` at the root, or under the common git dir in local mode — silent elsewhere
```

In `README.ko.md:170`, replace the last cell `같은 옵트인` with:

```markdown
루트에 `seal/` 이 있는 레포, 또는 local 모드로 공통 git 디렉터리 아래에 있는 레포. 그 밖에서는 아무것도 하지 않는다
```

### 2. The Korean root-migrate row says the dirty check reads the destination, and ties the notice to the refusal

severity: should
location: `README.ko.md:168`
evidence: read `README.ko.md:168`, `README.md:174`, `hooks/root-migrate.py:153-191`, `hooks/root-migrate.py:569-615`
verdict: fixed 21369c34
answer: The finding holds: `hooks/root-migrate.py#dirty` reads `sources(units)`, the directories the units come from. The Korean row now carries the replacement text above, word for word, as two sentences. `git grep` on "옮길 곳 아래" finds no other copy. No case pins the sentence's meaning. A `seal mutate` putting "옮길 곳 아래에" back survived the three modules that read the gate table (exit 1, `SURVIVED`). `frame/design.md` *Out of scope* keeps drift between the two editions' sentences a reader's to catch, since a reading guessed from words is a report and not a gate.

The crafter left the Does cells of the two new rows, and the Korean sentences
it rewrote, for this round to read (`gaps.md` *Not verified*). The English
`root-migrate` row says "It refuses the whole move over uncommitted changes
under what it would move, and says in one line what moved" (`README.md:174`).
That matches the code. `hooks/root-migrate.py#dirty` runs
`git status --porcelain` over `sources(units)`, the directories the units come
FROM (`:153-156`, `:179-180`).

The Korean row says "옮길 곳 아래에 커밋하지 않은 변경이 있으면 아무것도 옮기지
않고, 무엇을 옮겼는지 한 줄로 알린다" (`README.ko.md:168`). "옮길 곳" reads as
the place things are moved to, so the Korean row names the destination,
`seal/threads/`. The hook never reads the destination. A Korean reader with
uncommitted work under `seal/specs/` learns from this sentence that the move
goes ahead. The sentence is also one conditional with two clauses, so it says
the hook reports what it moved in the case where it moved nothing. The English
row states those as two separate facts.

In `README.ko.md:168`, replace the sentence quoted above with:

```markdown
옮길 것이 있는 디렉터리 아래에 커밋하지 않은 변경이 있으면 하나도 옮기지 않는다. 옮긴 것은 한 줄로 알린다.
```

## Confirmations

confirms: none
S1 holds. `hooks/dispatch.py:81-105` `GROUPS` names 15 distinct scripts. Each edition's gate table holds exactly those 15 first cells, `worktree_consent` and `root-migrate` among them (read, `README.md:172-186`, `README.ko.md:166-180`). `tests/behaviour/test_chain_hooks_hardening.py#test_the_gate_table_has_one_row_for_each_script_groups_registers` compares sorted lists, so a duplicate row fails as well as a missing one. It passed in this round's run (executed).

confirms: none
The four cells of the `worktree_consent` row hold in both editions, against `hooks/worktree_consent.py#main` and `#record` (read). The hook fires at PostToolUse for a Bash command holding a `git worktree add`, and for an Agent or Task call with `isolation: "worktree"`. It writes an empty file at `<git-common-dir>/agentic-worktree-consent/<session-id>` and prints nothing. It resolves the repository through `optin.repo_root` and not the opt-in, so "any git repo" is right. Nothing prunes the file, as the docstring says. The Korean cells say the same.

confirms: none
The English `root-migrate` row holds against `hooks/root-migrate.py#main`, `#dirty` and `#rename_state` (read). The README is rewritten to the marker. 0.22.x work items move to `seal/threads/<id>/` as staged `git mv`, or as renames under the common git dir in local mode. The move is refused over uncommitted changes. One line is printed. `rename_state` runs before the repository check, so the Where cell's "the state rename runs at every session start, silently" is right. The Korean Fires and Where cells match. Its Does cell is finding 2.

confirms: none
The other Korean sentences the work rewrote say what their English ones say (read): the 스킬 row (`README.ko.md:43`), the CLAUDE.md 블록 row (`:45`), the heading (`:26`), the privacy paragraph (`:218-224`), *처음 실행* (`:411-424`) and the way back in *shared 인가 local 인가* (`:519-524`). "어느 훅이든" is a little broader than "Each" in English. It stays true, because a hook that does not touch the network has nothing to stay silent about.

confirms: none
S6 holds. Both READMEs cite `skills/config/SKILL.md` *Before switching to shared, say what cannot be undone* and hold no `git reset -- :/seal`. The skill section holds the command, the staged-change reason, the pathspec reason and the citation of `docs/one-root-by-lifetime.md` *Shared or local*, a heading that stands at `docs/one-root-by-lifetime.md:118` (read). The claim "`seal mode` refuses a switch over a staged change" matches `skills/implement/scripts/seal.py#indexed`, which reads any staged pair except `D ` after the move as indexed (read, `:1757-1802`).

confirms: none
S7 holds. Both `BASELINE` entries are gone (`tests/text/test_no_passage_is_pasted_into_a_second_file.py:210-219`). `skills/implement/SKILL.md:355-359` links to `docs/the-agent-set.md` *One contract every agent receives, and one definition each*, which stands at `docs/the-agent-set.md:7`. No other line of that file changed (read, `git diff 5287dd42..bcc09e2f`). The module passed in this round's run (executed).

confirms: none
S8, S9 and S10 hold. The template's `concurrency` and `permissions` blocks match the repository's `.github/workflows/hygiene.yml:20-22`. Each repository comment on a shared step is the one pointer line. The template's chain-step comment names `docs/the-review-record.md` *What the check reads at the pull request*, which stands at `docs/the-review-record.md:179` (read). `tests/text/test_ci_gives_the_checks_what_they_need.py` and `tests/e2e/teammate/test_teammate_flow.py` passed in this round's run (executed).

confirms: none
S11, S12 and S13 hold. `pairs()` reads git's listing of `*.ko.md`, and the case requires `README` and `docs/experiments/README` among the pairs. `CONTRIBUTING.md:433-436` names every tracked pair. The manifest case compares both `marketplace.json` descriptions with `plugin.json`'s (read). All three modules passed in this round's run (executed).

confirms: none
The three divergences in `gaps.md` hold. `test_the_gates_table_says_the_root_may_sit_under_the_git_dir` now reads the gate table alone, so it no longer treats the records table's `seal/` row as a gate row. That is contract rule 18 applied to a check that refused correct prose (read, `tests/behaviour/test_first_setup_asks_once.py:651-668`). The second S6 case pins the reasons the frame moved into the skill. The `root-migrate` row's wording avoids the two names `tests/test_censuses.py` refuses, and still says what the hook does. `.test_durations` lost exactly the keys of the two removed cases (read). `gaps.md` *Not done* is right not to edit `docs/`: the frame's `## Rule changes` item is the settle's.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `bcc09e2f`. The crafter handed over with the suite `unverified`, and that label is honest: no phase record claims a broad run | the whole tree | the orchestrator, through `seal gate` (contract rule 2) |
| The crafter's red-first and `seal mutate` claims (32 mutants). This round re-ran the cases green and did not re-run a mutant | `trail/phases/phase-1.md` to `phase-5.md` | the sealer, which samples the crafter's claims |
| Whether the marketplace listing still renders right once the copies are held equal. The frame says no case in this tree can see it | `.claude-plugin/marketplace.json` | the owner, at the release |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 91 modules that `git grep -l` found naming a changed path or name (`README.md`, `README.ko.md`, `CONTRIBUTING.md`, `skills/config/SKILL.md`, `skills/implement/SKILL.md`, `templates/setup/hygiene.yml`, `workflows/hygiene.yml`, `.test_durations`, `hygiene.yml`, `the-agent-set`, `plugin.json`, `marketplace.json`, `dispatch.py`), with the changed test modules, `-q -p no:cacheprovider` | 4454 passed, 14 skipped, exit 0 |
| `bin/seal layout --check` | exit 0, 158 files read, 0 refused. It was run twice, once for the exit code and once for its last lines |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold. Run twice, as above |
