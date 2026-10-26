# Phase 7: 1792935671-the-routing-check-moves-to-the-sessions-tools

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | 6f1bde24 |

## What this phase was asked

Build phase 7 of `plan.md` *Phases*: the prose follows. Contract rule 8 retires to one line under its number. Rule 9's second reason becomes the edit check, and its heredoc-exception paragraph goes. Rule 16 loses its second reason. The review-mark and parity-mark steps go from `skills/code-review/orchestration.md`, `agents/warden.md`, `skills/legacy-parity/SKILL.md` and `skills/parity-setup/SKILL.md`. The waiver paragraph in `skills/implement/SKILL.md` goes, with the `[no-review]` lines and the wake/quiet table of `skills/implement/orchestration.md`. `README.md`, `README.ko.md` and `templates/claude-md-block.md` change. The changelog fragment carries the three answers of `plan.md` *Operational impact*, names the defaults of the owner's open Q1 and Q2, and says that the owner's own `: '[no-review]';` instruction waives nothing after this release, without editing anyone's `CLAUDE.md`. `docs/` stays untouched. Verify with `tests/test_the_agent_contract_holds_the_universal_rules.py`, `tests/test_every_agent_reads_the_contract.py`, the module pinning each changed skill, `rules --check`, and a `git grep` for `specseal-reviewed`, `specseal-parity`, `no-review]`, `specseal.waive` and `commit-review-gate` that finds only the changelog and released history.

## What this phase found

**The frame holds, and the class it names is wider than its list.** The plan's grep is the definition of done, and it found the old marks and waiver in files phase 7's row does not name (executed). Each states a rule that rested on the commit gate, so each was corrected (contract rule 12):

- `agents/smith.md`: the rule *The waiver is one command's.* is removed.
- `agents/scribe.md`: two pointers at rule 8 and the parity mark in its `## Never`.
- `agents/warden.md`: the probe rule said a heredoc gives the commit gate a command to read and pointed at rule 8. It now says a probe leaves nothing and its files are edits (rules 7 and 9).
- `skills/settle/SKILL.md`: a settle committed with `: '[no-review]';`. It now edits under `seal no-work-item`, and its commits carry the `no work item` trailer.
- `skills/verify/SKILL.md` and `skills/writing-style/SKILL.md`: their example of an instance named by its owner was the warden's review mark. It is now the warden's round record, in both languages.
- `templates/seal-README.md`, and `seal/README.md`, which `tests/test_first_setup_asks_once.py` holds to the template byte for byte: the review and parity marks left the list of what sits beside the root.
- `skills/implement/SKILL.md` *Commit at the smallest step*: its second cost driver was the commit gate's review arm. The paragraph now says no gate stops a commit, and it keeps the sentence its home test pins.
- `hooks/implementer.py` and `hooks/routing.py`: two comments named `specseal-reviewed`.

A divergence row in `overview.md` records this.

**Two misses of earlier phases, found by the grep.**

- `tests/test_optin.py` ran `hooks/commit-review-gate.py`, which phase 5 removed. `run_hook` of a missing file prints nothing, so the case passed with nothing behind it. It now runs the edit gate before any declaration, where the gate would refuse but for the opt-out marker. Seen red with the marker write removed (`mutation-check`, executed).
- `tests/test_the_hook_surface_git_offers.py` kept two cases whose unit phase 6 removed: `specseal.waive` reaching `pre-commit`, and the paths `pre-commit` sees. Both are removed. The cases under the markers `no-verify-met-where-the-branch-moves` and `gits-own-commits-not-judged` stay: they pin facts git still has, and `docs/` names the markers until the settle.

**What the grep still finds, and why each stands** (executed):

- `docs/`, `CHANGELOG.md`, `changelog/` and `seal/`: the policy root changes only at the settle, and the rest is released history.
- `hooks/cmdline_base.py`: frozen at `86256492`.
- `.test_durations`: the frame's *Removes* says the recorder rewrites it at the next broad run.
- References to the path `docs/commit-review-gate-spec.md`: in `hooks/launch.py`, `hooks/one_heredoc.py` and fourteen test files. The document stands until the settle removes it. `hooks/one_heredoc.py` still cites it as the home of the grammar `hooks/tokens.py` reads.
- Absence assertions in `tests/test_a_probe_that_commits_says_so.py`, `tests/test_review_axes.py`, `tests/test_settle_reads_before_it_removes.py` and `tests/test_one_word_one_meaning.py`.
- The docstring of the caseless `tests/test_the_waiver_can_be_typed.py`, which `docs/` names.
- One past-tense sentence in `hooks/worktree-guard.py` (*The commit gate learned this about `[no-review]`*).

**Rule 8 retired to one line:** *Retired by #1027, which removed every gate that read a commit; nothing replaced it, and a probe's leavings are rule 7's.* `tests/test_a_probe_that_commits_says_so.py` keeps its file name, because three definitions name it on `check:` lines. Its cases now hold that the retired rule carries none of its shapes, that no definition points a probe at it, and that the warden's and scribe's own paragraphs point at rules 7 and 9. Rule 9's second reason is the edit check: an edit through the shell is invisible to `hooks/routing-edit-gate.py`, citing `docs/the-routing-check.md` *The edit check* as the edit gate already does. Rule 16 keeps the reason about the shell's starting directory.

**`tests/test_edits_go_through_the_edit_tool.py`.** Its cases on what the commit gate counted in a heredoc body went: the command-word position, `eval`, the string a shell runs, and the one heredoc shape with the policy's grammar slots. The marker `one-heredoc-shape-is-data` left this file. `tests/test_one_heredoc.py` still carries it for `docs/commit-review-gate-spec.md` line 191, so no placeholder was needed.

**`skills/implement/orchestration.md`.**

- Question 1's exit names `seal no-work-item` and the trailer.
- The routing file's paragraph no longer reasons from the commit gate.
- The four-combinations table says edits go through.
- The wake/quiet table and its two paragraphs became one paragraph saying where the comparison with the original is recorded under each answer, with the two shapes that leave code uncompared. A third shape, a declaration rewritten from one answer to the other, no longer holds: the sealer compares the audited commit as a whole.
- The *standing waiver* paragraph now also says why `seal no-work-item` is not one.
- `## Orchestrator: closing the cycle` left `skills/code-review/orchestration.md` with its delivered-by row, because the review mark was its whole content.

**`skills/legacy-parity/SKILL.md` *Recording the comparison*** is now a table of who writes the `original:` line under each answer: the warden in each round record, the sealer once in `guarantee.md`. A warden that cannot resolve the original raises `unread`, and a sealer that cannot compare writes `withheld`, as `agents/sealer.md` step 5 says (read).

**READMEs.** The intro names the routing declaration, not the review mark. The flow diagram ends at the edit check. The gate table replaces the git-hooks row and the commit-review-gate row with `routing-edit-gate` and `stub-remove`. The inline switches lose the three waivers and gain `seal no-work-item`, and the root-move paragraph and the first limit are rewritten. The links to the two retiring documents are removed, and the Korean count reads three. `tests/test_no_passage_is_pasted_into_a_second_file.py` refused the first draft of the README rows for copying `skills/implement/SKILL.md`, and the settle paragraph for copying the orchestration file's exit row, so both were reworded.

**The changelog fragment** is `changelog.md`, all under `### Changed`. It carries the three answers, the latency phase 2 measured (a median 68 ms per edit against the installer's 113 ms per Bash call), compatibility, and the two defaults that stand until the owner answers Q1 and Q2. The owner's instruction is named as "an instruction file that still names `: '[no-review]';` for `no work item`, such as a `CLAUDE.md` block installed by an earlier release", with `bash install.sh` as the way to the current block. No `CLAUDE.md` was edited.

**How each new or changed case was seen red, executed.** Every changed test file was copied into a `git clone --no-local` of `863fd292`, the tree before this phase. Fifteen of the new and changed cases failed there. The sixteenth, the opt-out case of `tests/test_optin.py`, passes in that tree because the edit gate was already present, and it was seen red by `mutation-check` instead. A second `mutation-check` put a gate clause back into rule 16, and the absence case went red. `git status --short` was clean after each run, and the clone was deleted.

**Tests, executed.**

- 97 modules, the changed test files plus every module that names a changed README, agent, skill, template or hook file: 4,500 passed, 12 skipped, 1 failed. The failure was a line of `skills/implement/SKILL.md` past the wrap limit, left by an edit; it was fixed and `tests/test_docs_line_wrap.py` passed.
- The changelog and record readers: 472 passed.
- `rules --check`: all 249 check lines hold, one fewer than phase 6 because the smith's waiver rule took its line. `test-layout --check`: 0 refused. `ruff check` and `ruff format --check` over the changed Python files: clean.
