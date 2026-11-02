# Implementation Plan: a release is sized with no ceiling (#1289)

## Technical context

The policy change is the one `change` in `frame/design.md` *Rule changes*, and the settle after 0.28.1 writes it into `docs/issues-and-milestones.md:32-37`. The build edits no `docs/` file. What it edits:

- `tests/behaviour/test_a_release_is_sized_by_a_criterion.py` (286 lines at the base). After the build it holds `OWNER`, `read`, `flat` and `test_the_rule_says_what_it_does_not_change` (`:170-179`), under a docstring rewritten to say what the module reads and why it reads with wraps collapsed. `tests/text/test_the_release_tail_does_not_end_at_the_tag.py:24-27` cites that reason, and its sentence stays true as long as `flat` and its reason stay.
- `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:72`, the row registering `#tracked` in `APPLIES_THE_SHARED_GUARD`. The module's sweep turns red on a path-listing scope missing from its tables, so the row leaves in the same commit as `tracked`.
- `.test_durations:133-140`, one row per case of the module. Seven leave and `:136` stays.
- `seal/follow-up.md:43`, the row on `hits()` (design G11).

What the framer's probes found, each run from a `git clone --no-local` of the worktree at `343b9dde` under `<scratchpad>/1289-probe/`, with this `frame/design.md` copied into the clone and nothing committed. The directory was removed before the hand-back.

- `rule_changes.py#parse` returns one `change`, `errors=[]` and `unread=[]`. `section_lines` spans the section at lines 7 to 61. The `from`, whitespace collapsed, stands once in the document. `apply_op` applies it, and the applied section holds no `ceiling` and holds the new bold sentence (executed).
- `chain_check.py --baseline 40e6c23e --root . --worktree` exits 0. It prints two pin notices at the `from`'s line, `design.md:78`: `tests/behaviour/test_a_release_is_sized_by_a_criterion.py:46` holds "ceiling, not a target", and `:165` holds "Three or four is a". It refuses nothing in the `to` and names no copy. The other lines it prints are the records a framed work item has not written yet: `plan.md`, round records, `trail/gate.md` and `guarantee.md` (executed).
- With `test_the_count_survives_as_a_ceiling` and `SHARED_CEILING` cut from the clone's module, the same run prints no pin notice (executed). This is design S2 before and after.
- `STATES_A_SIZE` against five count sentences and two judgment sentences: it misses all five counts and matches both judgments (executed, design G7).

The failure scenario of the chosen approach, six months out: a session writes "keep a release to about four items" into a skill or a template. No case reads it, so it reaches review, and the proofer has to see that it restates the owner's rule with a number. The sweep would not have caught it either (design G7). The other failure is a release that grows while each added issue looks small. The description is the signal, and it fails where whoever places the issue writes the grounds without reading what the description already holds.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Rewrite the paragraph as a judgment with no number, ending with `check: none reader: whoever places an issue in a release milestone`. Remove the ceiling's case and the sweep. Keep the module with its one case under `:61` | A count restated in other words reaches review with no case reading it (*Technical context*) | **Chosen.** It states what the owner decided (design G1), keeps the criterion so a reader has something to judge by, and removes a script that blocks on a guess from words (design G8). |
| 2. Keep the sweep, rewrite only its docstring, and remove the ceiling's case: the structure kept | A skill that states the judgment, "judge whether the release's size still fits one description", fails the suite, and the session rewords it to pass the regex (contract rule 18). A count stated as "at most four work items" passes. | Rejected. The premise that keeps the sweep is that it catches a second statement of a release's size. Checked by probe: it misses every count tried, the issue's own sentence among them, and refuses both judgment sentences (design G7). Its comment at `:209-211` records no catch in the tree. |
| 3. Remove the whole module now, with a `change` moving `:61` to a `none reader:` line | `seal rules --check` refuses `:61` while it names a path that is no file, and a pending `change` excuses nothing. So the module would stay whole until the settle and a successor issue would delete it, as #1243 did for #1197 (design E5) | Rejected. A successor issue and a module kept whole cost more than the one case that already reads `:39-43`. The case is a wording pin by #1278's *The criterion*, and this design's `from` does not touch it, so `chain-check` names none of it. |
| 4. Replace the number with a softer one: "about four", "a handful", "rarely more than four" | Read as a limit again, as "three or four is the size" was in 0.11.1 and "a ceiling, not a target" was on 2026-11-02 (design E1) | Rejected. It is the defect the owner removed (design G1, G9). |
| 5. Pin the absence: a case asserting no document under `docs/` or `skills/` states a number for a release's size | The class of such sentences is unbounded in its spellings (contract rule 12), so the case is a spelling list again. #1278's *The criterion* counts an absence assert as wording | Rejected (design G8, E3). |
| 6. State the judgment again where the triage acts, in `skills/implement/orchestration.md` | Two documents state one rule, and a reader can leave with either answer | Rejected. `docs/issues-and-milestones.md` is the owner and the section is read at every milestone move. One source, and every other place links to it (`skills/core/SKILL.md` *The rule a mechanism is kept against*). |
| 7. Leave the ceiling's case for the settle to repoint or remove | The settle's broad run meets it red after the pull request that could answer it merged, which is what #1216's notice exists to prevent (design E4) | Rejected. The case is removed in this pull request, and `chain-check` names no pin once it is (*Technical context*). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 2, 3, 4, 5, 6, 7, 8 and 9 | S2, S3, S4 and S5 executed at the phase's commit; S1 re-run by the crafter with `rule_changes.py#parse`; S6 at review; the suite beyond the narrow run labelled `unverified`, answered by the orchestrator's broad gate | `ea581e55e` |

The narrow run, in one command at the phase's boundary: `tests/behaviour/test_a_release_is_sized_by_a_criterion.py`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, `tests/text/test_the_release_tail_does_not_end_at_the_tag.py`, the modules that read `.test_durations` and the modules that read `seal/follow-up.md`, each list taken by `git grep -l` at the phase's base, and `skills/code-review/scripts/chain_check.py --worktree` for S2. A module reading a changed path by another spelling is outside the list, which is why the list is a sample and the broad gate answers the rest.

## Operational impact

None. No migration, environment variable, dependency or configuration row. A maintainer reads the change in the release note, and the settle after 0.28.1 writes it into `docs/`.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-02 | The orchestrator folds round 1's findings 1 and 2 into the design's `to` and *Scope* item 1 as the fix pass wrote them in finding 1's close block: an overflowing issue moves to a later `release:` milestone, a `feat:` only where `docs/branch-and-release.md` sends it, and the judgment weighs work items | The fix pass agreed with both findings and may not edit the frame; the crafter re-parsed the replacement with `rule_changes.parse` in a scratch copy (one op, no errors, nothing unread, placed); the verifying round reads the folded text | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*; `docs/branch-and-release.md` *Work accumulates on a release branch* |
