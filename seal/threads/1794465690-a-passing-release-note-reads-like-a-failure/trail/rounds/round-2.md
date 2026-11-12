# Review round 2: 1794465690-a-passing-release-note-reads-like-a-failure

```seal
target: 12074fd9d, fixes e18a067b0..12074fd9d
```

This round verifies the fixes. The fix diff is `e18a067b0..12074fd9d`: round 1's record at `d282efd68`, the framer's fold at `68a00d031`, the fix pass at `191599e1e`, round 1's close blocks at `e4fc2f17a`, and the orchestrator's fold of `frame/plan.md` at `12074fd9d`. The code under review stays inside that diff. The scripts are not in it, and nothing in them changed (executed: `git diff --stat e18a067b0..12074fd9d`).

The work item's records were read whole at `12074fd9d`. `routing.md`, `frame/questions.md`, `gaps.md` and `pr.md` did not change after `e18a067b0`, where round 1 read them whole. The changed hunks of `frame/design.md`, `frame/plan.md` and `changelog.md` were read against the rest of each file. Carried from round 1 without re-deriving: the coordinates of the policy bullet, `docs/releasing/branch-and-release.md:59-115`, and of the colour table, `.github/scripts/publish_release_note.py:667-687`. Each `pr.md` quote still stands word for word at its coordinate: `frame/questions.md:12`, and `frame/plan.md:66`, which the new judgment row at `:67` left in place.

## Findings

### 1. G18's new sentence says no `to:` puts a new sentence before the policy sentence after it, and operation 1's `to:` does

```seal
severity: should
location: `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/frame/design.md:26`
evidence: read `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/frame/design.md:26`, `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/frame/design.md:81-109`, `docs/releasing/branch-and-release.md:75-99`; executed the five operations applied in memory to the whitespace-collapsed policy document, with the settled bullet printed and read
regression: round-1#1
```

Why it matters: G18 is a grounding row in `frame/design.md`, the file the settle and the sealer read for why the operations are safe. The framer's fold at `68a00d031` added this sentence to it: "After the settle, the policy sentence that follows each operation's `from:` still has the antecedent it has now, because no `to:` puts a new sentence between the two." The conclusion holds. The reason given for it is false for operation 1. Its `to:` (`frame/design.md:85`) adds "The paragraph's opening and closing tags keep the seal from matching a longer line of counts, so the seal finds only the whole header." That sentence stands between the header sentence and `docs/releasing/branch-and-release.md:78`, "The release's theme follows it". The antecedent holds only because the added sentence ends on "the whole header", which round 1's fix chose for that reason. Operations 2 and 3 do meet the stated reason. Operation 2's widened `from:` carries the "They are" sentence along with it. Operation 3 ends on the alt-text sentence that the "So" at `:98` follows.

The frame before the fold said only that each operation rewrites one sentence. The fold added a general reason that holds for operations 2 and 3, and it does not hold for the operation 1 text that round 1's own fix gave. A later edit of operation 1 that trusts G18 could add a sentence there ending on any noun, and nothing in the frame would say why that breaks "follows it". The fix states the reason operation by operation.

```markdown
| G18. `skills/settle/rule-changes.md` *A rule has one shape* (read) | Each operation below rewrites sentences inside the existing bullet, which has no bold rule sentence and no check line. After the settle, the policy sentence that follows each operation's `from:` still has the antecedent it has now. Operation 1's added sentence ends on the header, which the next sentence's "it" names. Operation 2's `from:` takes the "They are" sentence with it, so its added sentence comes after that sentence. Operation 3 ends on the alt-text sentence that the next sentence's "So" follows. The cases that hold the new text are named in *User scenarios & acceptance*. The proofer reads whether the bullet should carry a check line. |
```

No other line of the work item states this reason. It appears in `frame/plan.md:67`, the judgment row, only as the aim ("still leans on the sentence it leaned on"), which is true (read).

```seal
verdict: fixed 7a91dbcd9
answer: The framer folded the finding into G18, and the orchestrator committed it at 7a91dbcd9. G18 now gives the reason for each operation, with the proofer's sentences for operations 1 to 3 word for word, and adds two more. Operation 4's `to:` holds the alt-text sentence that stood inside its `from:`. Operation 5 ends on a semicolon whose clause names its own subject. Against `docs/releasing/branch-and-release.md:96-107`, the sentence after operation 4's `from:` ("Under any other value…") leans on nothing before it, and the clause after operation 5's semicolon opens with `templates/setup/config.md` as its subject, so both added sentences hold. The same commit adds a judgment row at `frame/plan.md:68`. No other file changed.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `## Rule changes` operations 1, 2 and 3 at `frame/design.md:85`, `:90-91` and `:96-97` carry round 1's text. Applied in memory to the whitespace-collapsed policy document, the five operations give a bullet in which ":78" follows "the whole header", "They are" follows the paragraph of results, and "So a reader…" follows "A badge's alt text is that label and value in words" (executed, and the printed bullet read). Each of the five `from:` values, operation 2's widened one among them, is found once (executed). `changelog.md:4` now reads "beside its bright red value" (read). Finding 1 above is in G18, a unit the fold changed. The rule changes this close names hold.

What holds: the fix's reach. The fix pass's class was a sentence that places a badge's label colour under, on or behind its value colour, found by searching for words, which it called a sample. This round searched again, over both scripts, both test files, `docs/releasing/` and the whole work item directory. The pattern caught `on`, `under`, `behind`, `over`, `below` and `above` before a colour word, and a colour word before `on`, `under` or `behind` (executed: `git grep -n -i -E` at HEAD). The only hits about badges are `trail/phases/phase-2.md:7` and `:9`, "blue on grey". The orchestrator left those as a phase record's account of what the build found, and the colours they name are right (`.github/scripts/publish_release_note.py:687`, read). So no finding is opened on them. `frame/plan.md:19`, folded at `12074fd9d`, now reads "a blue value beside a grey label". This search is a sample too: it reaches only the words in its pattern.

What holds: *Scope* item 4 as folded (`frame/design.md:35`). Every label but `SEALED` has the label colour `555555`, `SEALED`'s pair is `d42420` and `8e0c12`, `suite` is `2ea44f`, the three grey counts are `6e7781`, and every other value is `0969da`. All of this matches `.github/scripts/publish_release_note.py:674-687` (read).

```seal
confirms: round-1#2
```
What holds: the docstring of `test_a_badge_takes_its_two_colours_from_its_label` (`tests/github/test_publish_release_note.py:1072-1084`) now says it was seen red at every parameter but `SEALED`, and that `SEALED`'s red came from removing its entry. That agrees with `trail/phases/phase-2.md:17` and `:23` (read). The rewritten first sentences state the colours as the code gives them. The two test comments (`tests/github/test_publish_release_note.py:279-282`, `tests/github/test_release_seal.py:254-257`) and the spelling case's docstring (`tests/github/test_publish_release_note.py:1025-1027`) name a value colour beside a label colour. No assertion changed in `191599e1e` (read: its diff). The two test files pass at HEAD (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the release page draws the one-line headers as GitHub's `/markdown` endpoint did | `frame/questions.md` Q1, open at its default | the orchestrator, by the measurement Q1 names, or the owner on the 0.38.0 note after its seal job runs |
| The broad gate. The suite stays `unverified`. The fix pass's count of 1,221 over `tests/text` and `tests/behaviour` was not re-run here | `seal/config.json` `Broad gate` | the orchestrator's broad run, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py -q -p no:xdist` | exit 0, 125 passed |
| `uvx ruff check` and `uvx ruff format --check` over the two test files | exit 0 each |
| `python3 -c` applying the five operations of `frame/design.md` to the whitespace-collapsed `docs/releasing/branch-and-release.md` and printing the bullet | the settled bullet, read; each `from:` found once |
| `git grep -n -i -E` for a preposition of place beside a colour word, at HEAD | two hits about badges, both in `trail/phases/phase-2.md` |
