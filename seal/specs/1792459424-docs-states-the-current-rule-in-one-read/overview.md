# docs/ states the current rule in one read (#941) — overview

## Why this work exists

A rule names what reads it on one `check:` line no near miss passes, and
every document under `docs/` states the current rule once, in one read.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The count of label lines | `spec.md` Scope 1: "all 240 lines". Built: 243 at ac83bdf3 | 243 | three are indented under list items, and `git grep -E '^\s*'` misses them; `rules.py`'s reader counts 243 (`phases/phase-1.md`) |
| One `nothing` line | `spec.md` Scope 1: each of the 18 rewritten to the no-target form. Built: 17; `docs/measuring-a-run.md`'s names `tests/test_session_cost_post.py` | a target | its old reason named the test that holds half the rule; a no-target line would hide it |
| Where the grammar is stated | `spec.md` *Data & interfaces*: "every other file points here until settle moves it to `skills/settle/SKILL.md`". Built: stated in the skill now | the skill | settle writes `docs/`, never `skills/`, and this item's `## Rule changes` is the no-change block, so nothing would move it; a consuming repository reads the skill, and a work item's spec leaves with its directory |
| A removal `## Removes` did not name | `skills/verify/scripts/coordinates.py#named_unit`, `#unit_kinds`, `#_parsed_kinds` and their case in `tests/test_a_unit_is_bounded_where_a_parser_decides.py` | removed | their one reader was `fold_check.py#target_problem`, which this item removes (`git grep`) |
| Which phase drops the editions' enforcement pairing | `spec.md` Scope 2 and `plan.md` phase 2: the marker arm of `tests/test_both_editions_carry_the_same_folds.py`. Built: its enforcement pairing went in phase 1 | phase 1 | it read `fold_check.numbered_statements`, which phase 1 removes |
| A removal `## Removes` did not name | `tests/test_one_word_one_meaning.py#FOLD_MARKER` and its two blankings | removed | once `docs/` holds no marker, the only marker naming the swept word is in `changelog/`, which the sweep excludes (`git grep`) |
| One `nothing` line's paragraph | `spec.md` Scope 1: the 18 lines rewritten where they stand. Built: `docs/branch-and-release.md`'s line moved under the third-reader paragraph | moved | its reason describes that paragraph, and `tests/test_the_release_tail_does_not_end_at_the_tag.py` pins it as that paragraph's record line (`phases/phase-2.md`) |
| What the dry run lists | `plan.md` phase 3: "`bin/settle` dry run lists #953's spec and this one as nothing to apply, not as refused". Built: #953's spec parses and is held for its open Q4; this spec is refused at line 199 | reported | this spec's `why:` continues two spaces in where the grammar takes four; `spec.md` is the framer's to correct (`phases/phase-3.md`) |
| A backlog spec tied between groups | `spec.md` *Data & interfaces*: "belongs to the document group whose documents name, by `check:` line, the most of its live test files". Built: a tie goes to the group the spec's title is about, and to the later phase where the title names none of the tied groups | by title, then later | spec silent on a tie; phase 9 takes what no group took, so a later phase loses nothing (`phases/phase-4.md`) |
| A row closed by a release's own run | `spec.md` *Data & interfaces*: "only these close one", none of them a tag's workflow. Built: `1791076834`'s row about the real gather and note at 0.18.1 closed on `changelog/0.18.1.md` and the `v0.18.1` release `publish-release.yml` published from it | closed | the row asks for exactly that run, and it happened; the list's pull request legs cannot run a tag's workflow (`phases/phase-7.md`) |
| Three exemptions `## Removes` did not name | `spec.md` *Removes* names the narrated sections of the one-root editions, not what kept them exempt. Built: `tests/test_no_document_names_the_old_roots.py#DESIGN_RECORD`, the two one-root entries of `tests/test_release_hygiene.py#RECORDS_OF_A_MOMENT`, and git 2.54.0's entry for `docs/worktree-guard-spec.md` in `#VERSIONS_OF_ANOTHER_PRODUCT` | removed | each exempted text no longer exists, and both sweeps pass over the files without the entries (`phases/phase-9.md`) |
| What S13 names | `spec.md` S13: both `--baseline` runs "name each as settled". Built: seven of the eight | seven | `1791019421` held no `overview.md`, so neither run has a record of it to name; both exit 0 |
| What S11 lists | `spec.md` S11: each backlog spec "listed with nothing to apply and none as refused". Built: 33 backlog directories held for an open row | held | `spec.md` *Data & interfaces*: "A row none of these closes stays open, and its directory stays"; each is named in its group's phase record (Q4) |
| What a marker is given to | `spec.md`: "a rule whose test drives a script that can refuse a commit or fail a required job". Built: measured per test by a trace, and the worktree guard's and `broad-gate`'s lines left on files | measured | spec silent on how; a trace reads it, and the six lines drive the shared PreToolUse entry for a worktree creation or run the checks outside any commit or job |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over the phases built | the orchestrator, at `broad-gate` once the rounds settle |
| `rules --check` and the marker walk on Windows, where a path inside a test's `tmp_path` is spelled with `\` | the Windows leg of CI on the pull request |

## Not done

nothing

## Fed back into the spec

none
