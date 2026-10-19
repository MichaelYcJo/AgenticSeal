# 1792365855-the-placeholder-s-emblem-has-no-assets-entry — review round 2

target: 20783810, fixes cee31b88..20783810

This is a verifying round. It read only the fix range: `eba4fa05`, which
rewrites `assets/seals/README.md`, and `20783810`, which closes round 1's
finding 1. Carried from round 1, not established again here: the coordinates
of the three duplicate statements (`assets/seals/README.md:84-87`, `:99`,
`:105-111` at `abc49184`) and where `seal-mark.txt`'s facts live in
`skills/verify/scripts/seal_stamp.py`. I re-derived each verdict below
against the tree at `20783810`. I opened `seal_stamp.py` outside the fix
diff because the coordinator asked whether its comments stand. The branch
does not change that file.

## Findings

No finding this round.

## Confirmations

confirms: round-1#1
The close holds. Read, at `20783810`: the **Issue** line of the entry
(`assets/seals/README.md:84-86`) is now the page's only statement that the
mark is Georgia Bold's S held in `seal-mark.txt` and that #857 decides what
it becomes. §*Candidates for #857* (`:103-107`) is round 1's paste-ready
text, word for word. It opens with "The placeholder S above", so it points
to the entry instead of restating it. §*The next entry* (`:98-99`) no longer
says who chooses the mark. Executed: `grep -n` for `#857`, `seal-mark.txt`,
`Georgia`, `parchment`, `sheet`, `28 lines` and `settled` on the page. `#857`
now stands at `:86`, at the section heading `:101`, at `:107` (why the
candidates wait) and at `:165` (#857's lesson about scaling a mark). None of
these four repeats the claim "What the mark becomes is #857", which stands
only at `:86`. `seal-mark.txt` stands at `:32` (how the command loads the
chart), `:86` and `:123` (how a candidate replaces it), and each states a
different fact. One overlap is left: the chart's shape, 28 lines of 28 over
`.M`, is at `:105` and again at `:125`, where it describes what `read_chart`
refuses. That pair was on the page before this branch, and `:125` describes
a check rather than restating a fact, so it is not part of finding 1's
class. Executed: `git show --stat eba4fa05` changes only
`assets/seals/README.md`, a path the finding's `location:` names. In
`20783810`, round 1's record changes only two lines of the finding, its
verdict and its answer.

confirms: none
Dropping "took the parchment sheet away" from the entry holds, and the entry
stays true without it. Read: §*Candidates for #857* at
`assets/seals/README.md:118-121` states that the owner retired the parchment
sheet the same day and that the shipped stamp has no sheet. The entry's
remaining clause is "#832 settled the 28-cell frame and left the mark a
placeholder". That is accurate (`149ca9e`, #832 through #859, carried from
round 1), and it no longer repeats the sheet. The image's alt text at `:78`
describes no sheet, which agrees with this.

confirms: none
The smith judged that the comments in `skills/verify/scripts/seal_stamp.py`
should stay: the docstring at `:10-22` and the comment at `:202-208`, which
both say the mark is a placeholder S until #857. That judgment stands.
Read: those comments describe the module's own data file, at the place a
person replacing `seal-mark.txt` reads. They are the source for the chart's
current status, and the README entry links to the same file and the same
issue rather than being the source. The two also age differently. When #857
lands, the code comment becomes false and must change in that commit. The
entry's sentence records history ("#832 ... left the mark a placeholder ...
What the mark becomes is #857"), and that sentence stays true then. So these
are not two copies that must change together, and finding 1's class does
not reach them. This branch does not change the file
(`git diff 769f2aa4..20783810 -- skills` is empty).

confirms: none
The rewritten page still passes the sweep that reads it. Executed: `bin/test
tests/test_one_word_one_meaning.py -q -p no:xdist` in a clone at `20783810`
passed 26 tests, exit 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: unverified, not run in this round under contract §2 | the branch at `20783810` | the orchestrator, through `broad-gate` |
| How `placeholder-s.ans` prints in a truecolour terminal, and how the preview's three new styles compare with a real one, carried open from round 1. Neither file changed in this fix range | `assets/seals/placeholder-s.ans`, `assets/seals/README.md:22-24` | the owner, through the orchestrator |

## Probes

| Command | Result |
|---|---|
| `grep -n` for `#857`, `seal-mark.txt`, `Georgia`, `parchment`, `sheet`, `28 lines`, `settled` over `assets/seals/README.md` at `20783810` | "What the mark becomes is #857" only at `:86`; the chart shape at `:105` and `:125`; the sheet's retirement only at `:118-121` |
| `git show --stat eba4fa05`; `git diff 769f2aa4..20783810 -- skills` | `assets/seals/README.md` only; empty |
| `bin/test tests/test_one_word_one_meaning.py -q -p no:xdist` in the clone | 26 passed, exit 0 |
