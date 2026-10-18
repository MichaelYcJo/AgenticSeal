# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 10

target: e8a8ac06, fixes 40271149..e8a8ac06

## Findings

none

This is the verifying round after the cap. Both of round 9's closes hold,
and no unit the two fix commits added or changed carries a defect they
introduced, by reading or by execution.

## Confirmations

confirms: round-9#1
Holds. fa551683 replaces `STAMP_GIVEN_TO_THE_GATE` and its comment
(`tests/test_one_word_one_meaning.py:477-493`) with round 9's paste-ready
fix as written: the pattern's three alternations and the comment's words
match the record's fenced block line for line (read, against
`rounds/round-9.md:61-79`).

Executed (probe rows 1, 3 and 4). The new case
`test_the_stamp_sweep_reads_the_gates_run_and_the_passive`
(`tests/test_one_word_one_meaning.py:512-539`) fails with the pattern put
back to the two-word window, on its first sentence, `the broad gate's run
draws the stamp`, and passes with the pattern at e8a8ac06; the old pattern
lets all six of the sentences its docstring says pass it go by. The case
asserts the refusal of the nine sentences round 9 named, all but `the
stamp the broad gate draws`, which its docstring names as still passing,
and of `a stamp drawn from the broad-gate run`. The widened pattern finds
nothing in any `SEAL_SWEPT` file at 40271149 or at e8a8ac06, the emblems
page's new sentences among them.

The fold case's new comment is true (executed, probe row 4, and read
against `LITERAL_SEAM` at `tests/test_one_word_one_meaning.py:58`). The
pattern carries two apostrophes and no double quote, `LITERAL_SEAM.search`
finds nothing in it, and between the two apostrophes stand `s)?(?:\s+[\w`,
more than blanks and a string prefix. `test_folding_the_seam_cannot_hide_an_instance_it_would_have_found`
passes in the module run.

What the widened reach still lets through is outside round 9's sentences,
and no fix commit made it: the old pattern let each of these through too,
so none is a regression. The passive with `are` or `were` (`stamps are
drawn by the broad gate`), the passive over `a` rather than `the` (`drawn
by a broad gate`), and four words or more between `gate` and `stamp`
(`the broad gate's passing run draws the stamp`) pass it (executed, probe
row 4). No swept file says any of them (executed, probe row 6). The
hand-back names them for the filing ladder rather than this record's
findings.

confirms: round-9#2
Holds. 9e8c1532 applies round 9's wording to the page's title, its history
paragraph and the first sentence of §*The next entry*
(`assets/seals/README.md:1`, `:6-9`, `:70-71`), and the page now claims
only the gold lily and the red lily as entries and names the S as having
none (read).

Each fact the new sentences state holds. `## Candidates for #857` is the
heading at `assets/seals/README.md:76`, and its first paragraph is the one
that calls the mark a placeholder, Georgia Bold's S (read).
`skills/verify/scripts/seal-mark.txt` is in v0.21.1 as well as in the three
tags round 9 checked, and `git diff` of it from v0.20.0 to v0.21.1 and to
e8a8ac06 is empty; `seal_stamp.py` at e8a8ac06 still reads its chart from
that file (`skills/verify/scripts/seal_stamp.py:209`). So "from 0.20.0
through 0.22.0" covers every tag that carried the S, and "has been on every
release's stamp since 0.20.0" is true at the target (executed, probe row 5).
The rest of §*The next entry*'s paragraph, the version check, still reads
as a true rule for writing the S's entry, and `test_release_hygiene.py`'s
version cases pass with the page naming 0.20.0 and 0.22.0, both tagged
(executed, probe row 2).

The class the fix pass enumerated holds (executed, probe row 5): a
`git grep -i` of `every emblem`, `each emblem`, `both emblems`, `all
emblems` and the old `added when its release is tagged` outside
`seal/specs/` and `CHANGELOG.md` finds only the `SEAL_SWEPT` comment at
`tests/test_one_word_one_meaning.py:241`, whose "each emblem" tells what
the page used to say, as history. #978 is open, titled for the S's missing
entry, in milestone `release: 0.22.2` (executed, probe row 5).
`overview.md`'s emblems-page row and its `## Not done` bullet name the S,
#978 and `rounds/round-9.md` finding 2, and agree with the page (read).

confirms: none
The record commit e8a8ac06 changes only round 9's two `verdict:` lines to
`fixed fa551683` and `fixed 9e8c1532` and their two `answer:` lines, and
each `fixed` commit changes a path its finding's `location:` names:
fa551683 `tests/test_one_word_one_meaning.py`, 9e8c1532
`assets/seals/README.md` (read, `git diff 40271149 e8a8ac06` and `git show
--stat` of each).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified` by this round. `broad-gate.md` names 2475178a, and the commits since then change the tree | — | the broad run after the rounds settle, before the sealer is spawned again |

## Probes

| Command | Result |
|---|---|
| `bin/test` of `test_one_word_one_meaning.py`, `test_no_real_identifiers.py`, `test_docs_line_wrap.py`, `test_no_passage_is_pasted_into_a_second_file.py` and `test_the_record_is_written_in_words.py` with `-q`, in the round's clone at e8a8ac06 | 82 passed, exit 0 |
| `bin/test tests/test_release_hygiene.py -q -k version`, in the same clone | 14 passed, exit 0 |
| `STAMP_GIVEN_TO_THE_GATE` put back to the two-word pattern in the clone with the `Edit` tool; `bin/test tests/test_one_word_one_meaning.py -q -p no:xdist -k` of the new case, the fold case and the swept-file case; the file restored with `git checkout`; the new case run again | 1 failed (the new case, on `the broad gate's run draws the stamp`), 2 passed, exit 1; `git status --short` clean after the restore; 1 passed |
| one probe script, run once with the clone's interpreter and deleted: the old pattern against the case's first six sentences; the widened pattern against twelve more sentences, over every `SEAL_SWEPT` file at 40271149 and at e8a8ac06 folded as `flat` folds them, and over the page; `LITERAL_SEAM` over the pattern, and its quotes counted | old pattern: all six pass; widened: `are`/`were` passive, `a broad gate` and a four-word window pass, `was drawn by the broad gate` refused, four of five true sentences pass and `the commit gate stamps nothing` is refused, as the old pattern refused it; 0 hits at both commits and on the page; no seam; two apostrophes, no double quote; exit 0 |
| `git cat-file -e` and `git diff --quiet` of `seal-mark.txt` at v0.21.1 and e8a8ac06 against v0.20.0; `git grep -n -i -E` of the emblem claims outside `seal/specs/` and `CHANGELOG.md`; `gh issue view 978` | present, unchanged at both; one hit, the history comment at `tests/test_one_word_one_meaning.py:241`; open, milestone `release: 0.22.2` |
| the 25 `SEAL_SWEPT` files concatenated with their whitespace folded, `grep -o -i -P` for `stamps are` or `were drawn`, `drawn by` or `from a gate`, and four to six words between `gate` and `stamp` | no match, exit 1 |
| this record: copied into the clone and staged; `bin/test` of `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py` and `test_docs_line_wrap.py` with `-q`; `chain_check.py --baseline f6ae6db6 --root <the clone> --worktree` | 82 passed, exit 0; exit 0 as a draft, naming the broad run and the guarantee behind HEAD and the sealer's `withheld`, and no refusal of this record or of round 9's two closes |
