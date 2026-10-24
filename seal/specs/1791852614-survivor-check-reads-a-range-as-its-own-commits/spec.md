# Feature Specification: survivor-check reads a range as its own commits (#873)

<!-- seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-record-layout.md` §*A range owns the commits that descend from its start* | the one owner sentence: a range `a..b` owns exactly the commits `git log --ancestry-path --no-merges a..b` lists, read by `chain_check.py#own_commits` and nowhere else. This work makes the sweep a carrier of that sentence and defines nothing beside it; a shape is a case of `tests/test_a_range_owns_what_git_lists_for_it.py`, never a sentence here |
| `docs/review-chain-spec.md` §*The survivor sweep — a corrected sentence standing somewhere else* | *every place … still carrying wording the range removed*. With a merge inside a two-dot range, *the range removed* today means *the two ends differ*, and the merged side's removals are reported as this range's. The file stands at 999 lines under the 1000-line ceiling (`seal/config.md`), so no statement is added to it; the statement goes in the home above |
| `docs/the-reader-registry.md` §*The four classes and the line that declares one*, §*The census* | every unit this work adds or changes declares `Reads:` and leaves `tests/undeclared_readers.txt`; a reader that lets an unknown input through as if understood is the class the inventory exists to close, and *state the limit* (the issue's third option) is that class |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below; `seal/config.md` declares `Removes from 1791780031`, so the section is required of this frame |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | the sweep is CI's failing step on a pull request into a release branch. Each case is seen red first, the direction is stated (S1, S7), the prompt budget is zero, and the one new refusal names the spelling that reads the range right |
| `CLAUDE.md` §*The goal a design is chosen against* | between refusing the shape and reading it, the design that answers the question the caller asked without a second run is the one that stops nobody; the refusal is kept only for a shape that owns nothing |
| `skills/agent-contract/SKILL.md` §12, §14, §15 | the class is every reader of *what the range removed or wrote* in `corrected`, both lists; the refusal's text is pinned; every case is seen red first |

## Scope

### The defect, in one shape

`skills/code-review/scripts/survivor_check.py#corrected` lists the paths
`git diff --name-only a b` names and counts each file's sentences at `a` and
at `b`: a sentence the file holds fewer times at `b` is *removed*, one it
holds more times is *written*. Both counts are taken at the range's two ends
and nothing asks which commit made the change. On a two-dot range that holds
a merge of the base, the tree at `b` carries everything the merge brought
in, so a sentence another work item corrected on the base reads as wording
this range removed, and its standing twin is reported as this range's
survivor. It is `round_record.py#touched`'s shape (#860) one script over,
and #860's frame left it out by name (`seal/specs/1791384160-…/spec.md`
§*Out*).

### Measured in this frame

Executed 2026-10-13 in a scratch repository, git driven from Python
(contract §8), nothing left behind. `base` holds `notes.md` and `docs.md`
each carrying one sentence; `feature` is cut from it and makes `f1`; the base
makes `S1`, which corrects `notes.md` and leaves `docs.md`; `feature` merges
the base and makes `f2`. Neither `f1` nor `f2` touches either file.

| Run | What it said |
|---|---|
| `--range f1..f2` (the fix pass's spelling, holding the merge) | exit 1, `docs.md:3` reported as standing wording *this range* removed, the corrected sentence named at `notes.md:3` — `S1`'s correction read as `f1..f2`'s |
| `--range root..f2` | the same report |
| `--range base...feature` (CI's spelling) | exit 0, *against 0 sentence(s) the range removed* |
| `--range root..f1` (no merge) | exit 0 |
| `git log --ancestry-path --no-merges f1..f2` | `f2` alone |
| `git log --ancestry-path --no-merges <merge-base>..feature`, the merge base being `S1` | `f2` alone: the own commit made before the merge, `f1`, has no `S1` as an ancestor and is not listed |
| `git log --ancestry-path --no-merges root..feature` | `f2`, `f1`, `S1`: the base's commit descends from `root`, so from that start it is owned |
| `git log --ancestry-path S1..f1` | nothing: a start that does not reach its end owns nothing |

The last three rows decide two things. The own-commits reading applies to a
two-dot range and not to `A...B`, because `A...B` resolves its start to the
merge base, and from the merge base the own commits made before the merge
are not on an ancestry path. And a two-dot range whose start is below the
merged side's commits owns them, which is what the owner sentence says and
what #860 accepted as the notice's input on CI's checkout; the spelling for
a whole branch is `A...B`, which `parse_range` already resolves.

### In

1. **`corrected` keeps a removed sentence and a written sentence only where
   one of the range's own commits removed or wrote it, on a two-dot
   range.** The own commits are what `chain_check.py#own_commits` lists;
   `survivor_check.py` loads `chain_check.py` by path the way it loads
   `unverified_check.py` and `evidence_check.py`, and a copy without it
   refuses with exit 2 and a sentence naming what the sibling is for. For
   each own commit the pass reads the commit and its parent at the paths the
   commit changed, restricted to the paths the two-ends list kept, and
   collects the `(path, sentence key)` pairs the commit lost and the pairs
   it gained. In `corrected`'s per-path loop a sentence enters `gone` only
   if some own commit lost it at that path, and `fresh` only if some own
   commit gained it there. Both lists, because `written` is subtracted from
   every removed sentence's score: a sentence the merge brought in that
   shares a phrase with an own correction would otherwise hide the survivor.
   The filter is applied where the sentence is appended, before the pairing
   across paths, so a sentence an own commit removed at one path that the
   merged side wrote at another is removed and looked for, not paired away.
   The two-ends counting, the changelog's held and split sentences, the
   retired directories, the removed ledger rows and the pairing across paths
   are unchanged.
2. **`A...B` is read at its two ends, as today.** Its start is the merge
   base, so everything the base holds is in both trees. The own-commits
   pass is not run on it; the measurement above is why it cannot be.
3. **A two-dot `--range` whose start does not reach its end is refused**,
   exit 2, nothing examined, the message naming both ends and saying to
   write `A...B` for a range whose start is on the base. The refusal is the
   run's own `--range`'s, asked in `main`'s path through
   `chain_check.py#is_ancestor` as `round_record.py#parse_range` asks it;
   `whole_range` resolves a declaration's range exactly as before, so no
   `survivors.md` row changes what it prints. Such a range owns nothing, and
   a silent empty report over it is the inventory's *unknown passed*.
4. **The texts.** `parse_range`'s sentence that both spellings mean the
   same thing is replaced by one saying what each spelling reads;
   `corrected`'s docstring and the module docstring's §*What it does not
   answer* link `docs/the-record-layout.md` §*A range owns the commits that
   descend from its start* and define nothing: the one permitted gloss is
   the git command, and no sentence states a shape or a time. The limits
   inherited from the home are stated as limits, in the home's words: a
   change made only inside a merge's conflict resolution is in no own
   commit, so the sweep does not see it. The home gains one bold statement
   that the sweep reads a two-dot range this way and `A...B` at its ends,
   with its `Enforced by:` line; `docs/review-chain-spec.md` gains no line.
5. **The pins.** `tests/test_the_rules_have_one_owner.py` rule 18's
   carriers gain `survivor_check.py`; `tests/test_the_range_rule_states_no_shape.py`'s
   `LINKERS` gains it, so its linking sentences are held to the word list;
   `tests/test_a_corrected_sentence_survives_elsewhere.py#test_every_path_list_this_module_derives_from_git_is_filtered_or_named`
   counts the own-commits list as a path list and classifies it as filtered
   by `corrected`'s intersection with the two-ends list.
6. **`Reads:` lines** on `corrected`, `parse_range`, `main` where it
   changes, and every unit added, each removed from
   `tests/undeclared_readers.txt`.

### Out

| Left out | Why, and who answers |
|---|---|
| a change made only inside a merge commit's conflict resolution | the home's first limit, inherited unchanged: it is in no own commit. Today the two-ends reading sees it on a two-dot range; after this work it does not, which is the direction #860 chose for both of its readers. Nobody; stated in §*What it does not answer* |
| `A...B` reading its own commits | measured above: from the merge base, the own commits made before the merge are not listed. The two ends are the right reading there, and the issue says so |
| a two-dot range whose start is the base's tip at the branch's cut, or older | the owner sentence answers it: the base's later commits descend from that start and are owned. The spelling for a whole branch is `A...B`, and no sentence here says which commits such a range owns — a shape is a case of the shape module, never a sentence (`spec.md` of 1791384160 §*Reframed after round 3*) |
| the skip of the own-commits pass where a two-dot range holds no merge | on a linear range the filter keeps everything, so the pass is a cost and not a reading; whether the cost is worth a skip is `questions.md` Q1, a measurement the work takes |
| `whole_range`'s matching of a declaration's range | unchanged; In 3 keeps the refusal off it on purpose |
| `broad_gate.py`'s and `hygiene.yml`'s spelling, `origin/<base>...HEAD` | unchanged, and already the reading this work keeps for `A...B` |
| `tracked`, `corpus` and the pool | the pool is the tree at `b` and asks nothing about commits |
| the floor, the n-gram scoring, the calibration over 77 ranges | the filter removes sentences before scoring and adds none; on a range with no merge the score is unchanged (S5) |
| `round_record.py`, `chain_check.py` | #860's work, shipped in 0.21.0; this work only imports `own_commits` and `is_ancestor` |
| `docs/review-chain-spec.md`'s sweep statement | at the ceiling (999 lines); the home carries the statement |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the measured shape | Given the fixture of §*Measured in this frame* / When the sweep runs over `f1..f2` / Then exit 0 and the report says 0 sentences removed; `docs.md` is not named | a case in the new module, red against `corrected` as it stands (exit 1 today, executed in the frame) |
| S2 an own correction is still measured | Given the same history where `f2` corrects a sentence in `other.md` whose twin stands in `filler.md` / When the sweep runs over `f1..f2` / Then `filler.md` is reported with `other.md`'s corrected sentence, and `docs.md` is not | the same module, red against a filter that drops every sentence |
| S3 the merged side's wording does not subtract | Given `S1` writes a sentence sharing a phrase with the sentence `f2` corrects / When the sweep runs over `f1..f2` / Then the survivor of `f2`'s correction is still reported at the same score as on a history without `S1` | the same module, red against a filter of `gone` alone |
| S4 per sentence, not per path | Given one file that both `S1` and `f2` change, `S1` removing one sentence and `f2` another, each with a twin elsewhere / When the sweep runs over `f1..f2` / Then `f2`'s twin is reported and `S1`'s is not | the same module, red against a per-path restriction |
| S5 a range with no merge is unchanged | Given every existing case of `tests/test_a_corrected_sentence_survives_elsewhere.py` and the real ranges it measures / When the module runs / Then it passes unchanged | the module whole, at the phase boundary |
| S6 `A...B` reads its two ends | Given the fixture, where `f1` corrects a sentence whose twin stands elsewhere, and the branch merged the base after `f1` / When the sweep runs over `base...feature` / Then `f1`'s survivor is reported | the new module, red with the own-commits pass applied to `A...B` |
| S7 a start that does not reach its end | Given `--range S1..f1` / When the sweep runs / Then exit 2, nothing examined, the message names both ends and says to write `A...B`; and an exemption row spelled that way prints exactly what it printed before | two cases in the new module, the first red against `parse_range` as it stands |
| S8 a copy without its sibling | Given `survivor_check.py` copied without `chain_check.py` beside it / When a two-dot range is run / Then exit 2 and a sentence naming what the sibling is for | a case in the new module, the shape `seal/releases/0.15.4.md` P4 pins for `evidence_check.py` |
| S9 one home | Given the home and its carriers / When rule 18 and the no-shape guard run / Then `survivor_check.py` names the section and its linking sentences hold no listed word | `tests/test_the_rules_have_one_owner.py`, `tests/test_the_range_rule_states_no_shape.py` |
| S10 the path list is classified | Given the own-commits list in `corrected` / When the path-list case runs / Then it is counted and classified, and dropping the intersection with the two-ends list is red | `test_every_path_list_this_module_derives_from_git_is_filtered_or_named` |
| S11 every unit declares | Given the changed and added units / When the registry check runs / Then each carries a `Reads:` line and none stands in the census | `tests/test_a_reader_declares_its_input_class.py` |
| S12 the records | Given this item's fragment, the released rows anchoring on `corrected` and `parse_range`, and `changelog.md` / When `evidence-check --strict` runs on the branch / Then it is green, with the re-reads in the fragment and no released file changed | `bin/evidence-check --strict`; `survivor-check` over the branch |

## Data & interfaces

- **New, in `survivor_check.py`:** a loader for `chain_check.py` in
  `evidence()`'s shape, and one unit taking the own commits and the
  two-ends path list and returning the pairs each own commit lost and
  gained: `{(path, key)}` twice. The sentence key is `Sentence.key`, the one
  `corrected` already counts; the per-commit read is `read_blobs` at
  `<full>` and at `<full>^` over the commit's changed paths, which
  `own_commits` already lists with each commit.
- **Changed:** `corrected(root, a, b)` gains the spelling of the range (or
  the own commits) as an input and keeps its return shape `(gone, written,
  split)`; `parse_range` keeps its signature and returns the spelling it
  read, or a sibling unit does, so that `main` can refuse the two-dot shape
  and `whole_range` need not; `examine` and `survivors` carry the extra
  input through.
- **The report format is unchanged.** What changes is which sentences the
  *corrected* count and the survivor rows name on a two-dot range holding a
  merge, and one new refusal at exit 2.
- **No new dependency.** `own_commits` and `is_ancestor` are `chain_check.py`'s,
  which ships beside the sweep under `skills/code-review/scripts/`.
- **Ledger:** this item's fragment carries the new claims and the
  `evidence-check --reverify --into` re-reads of every released row whose
  anchor on `corrected` or `parse_range` moves (`docs/the-evidence-ledger.md`
  §*A released row is read again in the branch's fragment*).

## Rule changes

- nothing
  why: overturned: the survivor sweep left with the ledger (5b1f6fae).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the sentence that both range spellings mean the same thing because only the two endpoints are read | `skills/code-review/scripts/survivor_check.py#parse_range>"mean the same thing here"` | replaced by the sentence saying what each spelling reads (In 4); the claim is false from In 1 on |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline. No row
there is a person's.

Framed 2026-10-13 by framer, before the build.
