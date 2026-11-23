# Review round 2: 1795406406-code-stands-on-facts-that-no-longer-hold

```seal
target: 4dac381e1, fixes 909602a0b..4dac381e1
```

This is the verifying round after round 1's fix pass. The range is `909602a0b..4dac381e1`, seven commits. Two touch code: `f6551bb0d` changes `skills/implement/scripts/seal.py`, `templates/setup/hygiene.yml` and `tests/skills/test_seal.py`. The other five touch the work item's records: `frame/design.md`, `frame/plan.md`, `pr.md`, `changelog.md` and `trail/rounds/round-1.md` (executed: `git diff --stat 909602a0b 4dac381e1`). The round worked in a `git clone --no-local` of the branch checked out at `4dac381e1`, under `<scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-2/clone`. The work item's records were read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` to `phase-5.md` and `trail/rounds/round-1.md`. No `pr.<lang>.md` stands, and none is owed, since `Commit and pull request language` is English. No `seal/parity.json` is declared.

Carried from round 1 and not established again: the acceptance searches of `frame/design.md` S4, S5, S7, S9, S14 and S15. They read code this range does not change, since `lib/`, `skills/verify/`, `skills/settle/`, `skills/code-review/` and `.github/` are byte-identical between `909602a0b` and `4dac381e1` (executed: `git diff --quiet 909602a0b 4dac381e1 -- skills/verify lib`, exit 0, and the stat above).

## Findings

### 1. The review-chain check still prints that it examined nothing on a pull request whose trailers it judges, the claim round 1's finding 3 corrected elsewhere

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1909-1924`, `tests/skills/test_chain_check.py:3701-3707`, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/changelog.md`
evidence: executed `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-2/test_tmp_round2_left_workflow.py <clone> <scratch>`, `git grep -n -e 'declared neither way' -e 'examined nothing'`, `git log -S'examined nothing' -- skills/code-review/scripts/chain_check.py`, `git log -S'def trailer_findings' -- skills/code-review/scripts/chain_check.py`; read `skills/code-review/scripts/chain_check.py:1886-1924`, `skills/code-review/scripts/chain_check.py:2001-2015`, `skills/code-review/scripts/chain_check.py:2160-2209`, `docs/checks/the-routing-check.md` *At the pull request*, `templates/setup/hygiene.yml:17-21`
reopens: round-1#3
```

Why it matters: round 1's finding 3 held that "examines nothing" is false for a workflow left in a local-mode repository, because its review-chain step still judges the commit trailers. The fix pass corrected the line `seal mode local` prints and the template's header, and the orchestrator added two `## Rule changes` operations for `docs/layout/one-root-by-lifetime.md` and its Korean edition. The close does not hold for the class: the step itself still prints the claim.

The fix pass claimed that its search on `examined nothing`, among other words, found one more statement of the claim, in `docs/layout/one-root-by-lifetime.md`. The same search reaches two messages in `skills/code-review/scripts/chain_check.py#declared_for_this_branch`, and the hand-back lists neither:

- `:1919-1924`, printed where no committed declaration names the branch: "this pull request declared neither way, so the review-chain check examined nothing."
- `:1911-1918`, printed where the clone holds a local root: "So no routing declaration for `{branch}` can be read from what git carries, and the review-chain check examined nothing."

Both stand on a fact that no longer holds. The `examined nothing` wording came in with #90 and #245. Trailer judging came later, with #1027 (`trailer_findings` at `:2001-2015`, executed: `git log -S`). After the notice, `main` judges the trailers in the same branch (`:2202-2208`). A trailer naming an undeclared work item is a problem there, and an error on a ready pull request. Where the clone holds a local root, each work item's trailer is printed as a notice.

The probe reproduced the state the new template header describes. It used a repository with no `seal/` in its tree and `GITHUB_HEAD_REF` set, and ran the target's `chain_check.py` on two commits. Both runs printed the `declared neither way ... examined nothing` notice. The run on the commit carrying `Seal-Routing: some-item` then printed, under that notice, that the commit "carries `Seal-Routing: some-item`, and no routing declaration this pull request judges names that work item". So one run of the step says it examined nothing and then reports what it found in a trailer. Every pull request of a local-mode repository whose workflow was left behind reaches `:1919-1924`. `ROOT_LEFT_SAYS` appears only on the pull request that deletes the root. Since `f6551bb0d`, the header of that same workflow file says the step "judges the commit trailers alone". The log and the header now contradict each other.

The messages are lines a person reads, so the fix follows contract rule 14: the case that pins the wording changes in the same commit, and the changelog names the change. `ROOT_LEFT_SAYS` (`:1935-1940`) already says "judged the commit trailers and nothing else", and the fix uses those words.

```python
# skills/code-review/scripts/chain_check.py, declared_for_this_branch, the two returns under `if not matching:`
    if not matching:
        home = local_root(root, routing)
        if home:
            return [], (
                f"this repository keeps its root at {home} — local mode, where "
                "nothing under the root is committed. So no routing declaration "
                f"for `{branch}` can be read from what git carries, and the "
                "review-chain check judged the commit trailers and nothing else. "
                "`seal mode shared` moves the root into the tree and gets the "
                "declarations judged."
            )
        return [], (
            "this pull request declared neither way, so the review-chain check "
            "judged the commit trailers and nothing else. Nothing git carries "
            f"under `{work_items}/` declares `{branch}`. Add {work_items}/"
            f"<work-item>/{routing.FILENAME} to declare."
        )
```

```python
# tests/skills/test_chain_check.py, the case at :3701-3707
    def test_local_mode_still_judges_no_declaration(self, repo):
        """Naming the root does not turn an untracked declaration into a checked
        one: CI reads what git carries, and local mode commits nothing, so the
        trailers are all the check judged."""
        local_item(repo)
        _code, out = run_check(repo)
        assert "judged the commit trailers and nothing else" in out, out
        assert "examined nothing" not in out, out
        assert "through the review chain" not in out, out
```

```markdown
<!-- changelog.md, ### Fixed, appended to the entry on `seal mode local` and the workflow template -->
The review-chain check's own notice for a pull request that declares nothing, and for a clone that keeps its root locally, now says the check judged the commit trailers and nothing else, where it said the check examined nothing.
```

The snippets stop at these three files. `tests/skills/test_chain_check.py:1787` and `:4529` pin `declared neither way`, which stays. Each of those cases reaches `:1919-1924`, so the fix pass can add the new words to one of them, the case at `:1777-1788` being the closest. The search found no document, README or eval that quotes either message: `git grep` on `declared neither way` and `examined nothing` over `docs`, `skills`, `agents`, `templates`, the READMEs, `CONTRIBUTING.md` and `evals` lists only the code, its case, `docs/layout/one-root-by-lifetime.md:150`, which the new operation rewrites, and unrelated uses in `.github/scripts/issue_claims_check.py` and `skills/verify/SKILL.md:176`. The two docstrings of `seal.py` that phase 3 wrote cite `ROOT_LEFT_SAYS` for the left workflow. After this fix, the later pull requests' notice says the same thing, so neither docstring needs a change. A statement of the claim in other words is the part this search does not reach.

```seal
verdict: fixed fc573606d
answer: The finding holds, and round 1's close overstated its search: the `git grep` that reached `docs/layout/one-root-by-lifetime.md` ran on `examine nothing`, which does not match `examined nothing`, so the two notices of `chain_check.py#declared_for_this_branch` were missed. Both notices now say the review-chain check judged the commit trailers and nothing else, the words of `ROOT_LEFT_SAYS`, and the local-mode notice ends with `seal mode shared` getting the declarations judged where it said "gets the check running". The local-mode case is renamed `test_local_mode_still_judges_no_declaration` and pins the new words; the new words went into `test_the_shared_sentence_says_what_it_searched_and_for_what`, the case of the function's own class that holds the shared sentence, rather than the case at `:1777-1788`, which holds the spec reading. Each changed case was seen red against the old messages before the code changed, and each `examined nothing` negative was seen red under `seal mutate` putting the phrase back beside the new words, the file restored each time. The changelog's entry on the left workflow names the notice. The wider search, a sample, ran `git grep` over the whole tree outside `seal/threads/` and the recorded eval cases on `examine`, `examines`, `examined` and `examining nothing`, `checks nothing`, `checked nothing`, `reads nothing`, `judged nothing`, `nothing was checked`, `nothing is declared`, `nothing to check`, `declared neither way`, `nothing can disagree`, `declared nothing`, `declares nothing`, `undeclared`, `neither way`, `asks nothing`, and on the identifiers `declared_for_this_branch`, `ROOT_LEFT_SAYS`, `local_root(` and the notices' own words. Outside the two notices, every match on the no-root or left-workflow path states what holds: `seal.py`'s `mode --check` line and its comment, `left_workflow_line`'s docstring, the template header, `docs/checks/the-pull-request-check.md` *nothing-declared-nothing-owed*, `docs/checks/the-routing-check.md`, `CONTRIBUTING.md` *What a contribution is not asked for* and the teammate flow's docstring. The only false statement in `docs/` is `docs/layout/one-root-by-lifetime.md:149-152` and its Korean edition, which `4dac381e1` already gave operations. A statement of the claim in other words is the part the sample did not reach.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the first sentence of the gate-change row at `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/frame/plan.md:68` now says the change "blocks more in `chain-check` and on two root states of `seal unverified`, allows more on a U+2705 row of `seal unverified`". Its grounds give the exit 1 to exit 0 and the cost of a wrong allow. Both match the measurement: round 1's probe was re-run, executing the `909602a0b` copy of `unverified_check.py` and `lib/gaps.py`, which is byte-identical to the target's. It printed base exit 1 with `1 unreadable`, and head exit 0 with the row listed as `open` (executed). The quote at `pr.md:2` equals the row's Judgment cell whole, and the quote at `pr.md:1` stands in the row at `:67` (executed: a Python comparison of the two files' lines). The other readers that load `lib/gaps.py` were checked for a gate the row misses. `pr_body.py` reads only `GAPS.HEADING` from it (executed: `grep -n 'GAPS\.'`, one line, `:222`), so the body arm gains no allow.

```seal
confirms: round-1#2
```
What holds: the grounds cell of the same row now carries the sentence round 1 gave on what each changed reader reads. Each claim in it matches the code (read). `lib/fields.py:188-196` holds `confirms:` to `round-<N>#<n>`. `lib/items.py:33` matches `nothing` after any list marker with `re.IGNORECASE`, and `#unread_block` (`:89-99`) names only such a line. `lib/gaps.py#parse_section` closes a row only where `closing_word` answers the word `closed`. The three cases it names stand: `tests/lib/test_fields.py:125`, `tests/lib/test_items.py:123` and `tests/lib/test_gaps.py:95`.

What matched: for round 1's finding 3, the three statements it located now say what the code does (read: `skills/implement/scripts/seal.py:1736-1737`, `templates/setup/hygiene.yml:17-21`, `tests/skills/test_seal.py:2744-2748` and `:2795`). The line `seal mode local` prints matches `left_workflow_line`'s docstring (`:1724-1731`). The header's claim that every step passes matches `docs/checks/the-routing-check.md` *At the pull request*: at a local root a commit carries no trailer, and the step does not read the body when nothing is declared (`chain_check.py:2202-2208`). The installed copy carries the header, because `seal.py#plugin_workflow` writes the template whole, replacing only the version placeholder. These statements hold. Finding 1 above reopens the class for the step's own notice.

What matched: the two `## Rule changes` operations added at `4dac381e1` parse, and the settle can place them (executed: the probe `test_tmp_round2_rule_changes.py`). `rule_changes.py#parse` reports no error and no unread line over the whole section. Every operation's `from` is found once in its section through `#section_lines` and `#pattern`, the ten operations among them, and `#apply_op` places each. The paragraph each new operation leaves in `docs/layout/one-root-by-lifetime.md` *Shared or local* and in `docs/layout/one-root-by-lifetime.ko.md` *shared 인가 local 인가* was printed and read. Each says the workflow passes, that `chain_check.py` reads nothing as declared and judges the commit trailers alone, and that it exits 0. The two editions say the same. `chain_check.py --worktree` printed no pin or copy notice at a line of the design, so keeping "so nothing is declared" in the English `to` leaves no test literal the operation takes out (executed). The phrase is true there, by `ROOT_LEFT_SAYS` and by the `declared neither way` path.

What matched: the new changelog entry, `changelog.md:4`, says what `f6551bb0d` changed. Its condition, "pinned to the installed release", is `left_workflow_line`'s `pin == "v" + version` (read, `seal.py:1734`). *Scope* item 10 of `frame/design.md` names one `### Fixed` entry, for item 4, as what the build's last phase writes. The second entry came from the fix pass, which that sentence does not cover, so the frame is not contradicted.

What matched: the narrow modules of the fix and the files that read the template pass. `bin/test -q tests/skills/test_seal.py tests/text/test_ci_gives_the_checks_what_they_need.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` gave 488 passed and 8 skipped, exit 0 (executed). `uvx ruff check` and `uvx ruff format --check` over `seal.py` and `tests/skills/test_seal.py` exit 0 (executed). The fix pass says the printed-line case was seen red against the old message. That follows from the diff, since the case asserts the new words and the old code printed others (read). It also says the older-pin case's negative assert was seen red only under `seal mutate`. That is the only way a negative assert of words the old code never printed can be shown red, and the round did not run it again.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite, the repository-wide lint and the format check (`Broad gate` of `seal/config.json`). The suite stays `unverified` (contract rule 2) | `seal/config.json` | the orchestrator's broad run, after finding 1 is closed |
| The close-issues workflow without the label step, on a push to `main` | `.github/workflows/close-issues-on-release.yml` | the close-issues run when this release reaches `main`, read by the repository owner (`gaps.md`) |
| The older-pin case's negative assert at `tests/skills/test_seal.py:2795`, seen red under `seal mutate` by the fix pass and not run again here | `tests/skills/test_seal.py:2795` | the sealer, from the fix pass's account |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-2/test_tmp_round2_left_workflow.py <clone> <scratch>`: a repository with no `seal/` in its tree, branch `feature` with `GITHUB_HEAD_REF` set, `chain_check.py --baseline main` run after a commit with no trailer and again after one carrying `Seal-Routing: some-item` | both runs exit 0 (state unknown, so not strict); both print `this pull request declared neither way, so the review-chain check examined nothing.`; the second then prints that commit's `Seal-Routing: some-item` names a work item no declaration judges |
| `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-2/test_tmp_round2_rule_changes.py <clone> <design>`: `rule_changes.py#parse`, `#section_lines`, `#pattern` and `#apply_op` over every operation of `## Rule changes` | no error, no unread line; each of the ten `from` found once in its section and placed; the two *Shared or local* paragraphs printed as the settle leaves them |
| `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-1/test_tmp_round1_probe.py`, re-run from round 1's `## Probes` | base: exit 1, `1 unreadable`; head: exit 0, the U+2705 row listed as `open` |
| `bin/test -q` over the four modules named under *Confirmations* | 488 passed, 8 skipped, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `skills/implement/scripts/seal.py` and `tests/skills/test_seal.py` | both exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 02369a0e9 --root <the branch worktree> --worktree`, before this record | exit 0; no notice at a line of the design; round 1's finding 3 named as owed a verifying round |
