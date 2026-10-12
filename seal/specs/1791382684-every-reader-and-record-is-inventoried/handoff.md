# 0.21.0 — handoff after the first builds

Written 2026-10-08 (evening, KST) by the orchestrating session, for a session
on another machine. Every branch below is pushed. Nothing here depends on the
old machine's worktrees, memory or scratch files. Each open work item also
carries its own `seal/specs/<id>/handoff.md` on its branch, and that file says
what its next step is.

## Where the run stands

Ten of the eleven work items are squashed into `release/v0.21.0` (2026-10-12).
#835 is being framed again against the landed tree, and #834's own build
follows it. Each sibling landed one at a time: the next merged the release
branch in, re-read what drifted, and was sealed again before it landed.

| Issue(s) | Work item | PR | State | Next step |
|---|---|---|---|---|
| #858 | 1791384161 | #875 | **merged** 9b644676 | — |
| #864 | 1791384162 | #876 | **merged** d712a632 | — |
| #837 | 1791384154 | #879 | **merged** 279a580b | — |
| #867 | 1791384156 | #882 | **merged** 56ade5c8 | — |
| #869, #852, #853 | 1791384158 | #880 | **merged** b6c81a83 | — |
| #860, #805 | 1791384160 | #878 | **merged** ad447367, after a reframe at round 3 | — |
| #836 | 1791384153 | #887 | **merged** 23f5977c; reframed (the collection half observes the pytest recorder's record), capped at round 4, deferred #891 | — |
| #868, #856 | 1791384157 | #881 | **merged** 9afc90aa; reframed twice (the brace reader deleted, a named limit), capped at round 6, deferred #893 | the owner's P2: round 6 found `git rebase main other` from a diverged `main` refusable at `reference-transaction`, which narrows delete's ground (#893) |
| #870, #848 | 1791384159 | #889 | **merged** be464c06; reframed (the lexer deleted, bound only where a parser exists), capped at round 3, deferred #892 | — |
| #866 | 1791384155 | #890 | **merged** c38f97d7; capped at round 3 with nothing to fix | — |
| #835 | 1791384152 | none | framed 2026-10-07; refreshed 2026-10-12 (62c27416); the Fable framer runs again against the landed tree at c38f97d7 | approve `plan.md`, then the smith |
| #834 (its own build) | 1791382684 | none | the inventory only | after #835 |

`release/v0.21.0` is at c38f97d7. Not framed for 0.21.0: #844 (a docstring
reflow) and #857 (the stamp's mark waits on the owner's design; it is still
in the milestone).

## Decisions the owner made (2026-10-08)

- The seven handoff questions were all answered at their defaults, except
  that #856 is (c), confirmed. All eleven items ship in 0.21.0.
- **"나머지 전부다 동시진행해 최초 세팅대로 automation"**: run everything
  concurrently under the original `automation` answer, with no mid-run
  questions.
- **The owner's go-ahead (“진행해”) covers squash-merging a sealed PR into
  `release/v0.21.0`.**
- **#868's `questions.md` P1 is built on its default (yes) and is not yet
  answered by the owner.** The reframe widened #856's rule from "a git word"
  to every word of every segment. The over-stop is 42 of 33,287 recorded
  pairs, one of them git. If the owner says no, the frame reopens.

## Review of the run (2026-10-08, the owner and the orchestrating session)

0.21.0's theme was to break the guess → record → re-tag loop: #834's inventory
gives every reader one of three fates, which are observe, force a format, or
delete. The owner read the run against that theme and judged that much of the
open work patches over the problem and makes new ones. **The owner has since decided to reframe all three inside 0.21.0** (§*What
the owner decided*). Every finding
round so far has found the next case of the same class, and another fix pass
would add one more layer of the same patch.

### The six merged items keep to the theme

- #860 reads what git computes (`git log --ancestry-path --no-merges`).
  The frame only went wrong in the prose describing it. The reframe stated the
  rule once and pinned the shapes as tests.
- #869 replaced reading pytest's printed text with a record pytest's own hooks
  write. That is a guess turned into an observation.
- #867 merged several readers into one and held the heading rule to
  CommonMark.
- #858, #864 and #837 add no guessing reader.

### The three open chains each predict a foreign tool, and patch the prediction

| Item | What it does now | Why it is a patch | The observation-based direction to weigh |
|---|---|---|---|
| #868 (#856's braces) | reads a segment's raw text with quoted spans neutralised and stops on anything brace-like | still imitates bash. Six rounds, one reframe; the stop rule costs 42 of 33,287 recorded pairs | observe the act instead of predicting the command: git's `reference-transaction` hook sees HEAD move whatever spelled the command. This is #692's own conclusion ("shell prediction does not converge") |
| #870 | a string, comment and bracket lexer for nine language families | every family has its own exceptions; round 1 found three more of the same class | force a format: bound units only where a real parser exists (`.py`), and require a quoted-line anchor everywhere else |
| #836 (the collection half) | reads a test file statically to decide whether pytest would collect and could fail the test | each round finds another `skip`/`xfail` spelling | observe: #869's pytest recorder already writes a line per test that ran in the sealed run. Whether a cited test ran is in that record |

The other half of #836, a ledger row naming the test that holds its claim, is
not a prediction. It can stand apart from the collection half.

### The ledger's re-read cost is structural

This run wrote **360 `Re-read ·` rows against 55 `Corrected ·` rows**, across
the nine fragments (counted at the release branch and the open branches).
Most of the 55 record a change the branch made on purpose, not a stale claim
that re-reading caught. So almost all re-reading confirmed and changed
nothing. The release branch holds 2,347 released rows, and the cost recurs on
every edit to a cited unit. Siblings editing the same unit doubled it: four
PRs sealed against one base left 33 drifted rows nobody read.

Test rows (#836) and a bulk migration of #836 Q1's (c) would lower the cost
inside the hash ledger's premise without questioning that premise. Whether a
row of claim plus hash is the right record at all is the question to open, in
0.22.0 or later.

### Derived prose was where most findings sat

After round 1, #860's findings were all about sentences restating its rule
more widely than the code. Each closed by deleting the sentence. "One owner
per rule" holds in `docs/` and breaks in docstrings, changelog fragments and
ledger claims. The word-list guard #860 added is itself a patch, and its
docstring says so.

### The run's own mechanics were patched by hand

- **No rule says which plugin version governs a run.** When #837 landed, the
  tree's `round-record` and the installed 0.20.0 one disagreed, and the run
  went on with the installed copy by hand.
- **A smith's hand-back checks lived only in prompts.** The eight guard
  modules, `survivor-check` and `correction-check` were not in one command.
  Five of seven first PRs went red on CI over this.
- **Landing order and re-seals were a scratch script and memory.**

The fix for these is one hand-back command and a pinned plugin version per
run, not longer prompts.

### What the owner decided (2026-10-12)

1. **Reframe #868, #870 and #836's collection half inside 0.21.0**, against
   the observation-based direction above.
   - Each goes back to its framer with its round records as input, the way
     `skills/code-review/orchestration.md` §*A fix of a fix twice sends the
     work item back to its framer* runs a reframe.
   - Each framer is also given this section: the owner's reason is the theme,
     not a fix-of-a-fix count.
   - The open findings of each chain's last record close `deferred the
     frame`, and each PR takes `chain: reframed`.
2. **0.21.0 ships as the six merged items plus #866, #835 and #834's build**,
   with the three reframed items once they land.
3. **#836 Q1 stays at (a) for now.** A bulk migration of the released rows
   that already cite a test needs #836's test rows, and #836 is being
   reframed. Decide (c) and its timing after #836 lands. Weigh it then against
   the ledger-premise question above.

## How a chain is run, as this run learned it

Each step below cost a red CI run, a reopened round or a reframe before it was
written down.

1. **Records are written with the installed generator**, not the tree's.
   #837's `round_record.py` refuses ⬜ rows in a fix table and is now in the
   release branch. The run is governed by the installed 0.20.0 rules:
   `python3 ~/.claude/plugins/cache/specseal/specseal/0.20.0/skills/code-review/scripts/round_record.py {new|close} … --root .`
   Every ⬜ still takes a row (`answered` with grounds, or `corrected at`).
2. **Before landing a sealed PR, check whether the release branch moved since
   its seal.** If it did:
   1. `git merge` it in (never rebase);
   2. read the drifted ledger rows again (`evidence-check .`);
   3. run `correction-check` and `broad-gate --preflight`;
   4. seal again.

   Four PRs sealed against one base and landed in sequence left the release
   branch with 33 drifted rows. #836's branch clears them (`overview.md`
   §*The release branch's integration drift, cleared here*), so **land #836
   before #870 and #866**.
3. **Landing script** (re-create it; it lived in the old scratch dir): wait on
   `gh pr checks --watch`, stop on any non-SUCCESS, `gh pr ready`, wait for
   the re-run, then
   `gh pr merge <n> --squash --match-head-commit <full sha>`, and read
   `state` and `mergeCommit` back.
4. **Every smith spawn prompt names:**
   - the ledger fragment's full file name,
     `seal/ledger/<id>-<slug>.md`. A bare id folds under a heading that names
     no work item;
   - the eight suite-wide guard modules:
     `test_a_shrunken_corpus_declines_to_judge`,
     `test_a_rider_reaches_its_file`,
     `test_every_reader_ends_a_line_where_gfm_does`,
     `test_one_word_one_meaning`, `test_no_real_identifiers`,
     `test_a_record_states_what_the_tree_has`, `test_release_hygiene`,
     `test_docs_line_wrap`;
   - `survivor-check --range origin/release/v0.21.0...HEAD --exempt …` and
     `correction-check`, which CI's `release` job runs.

   Narrow runs missed each of these once.
5. **Probes that run bash or git use a scratch repository as `cwd`.** One
   reviewer probe ran `git switch` in the main checkout. Git refused it, and
   nothing changed.
6. **When a fix would list one more spelling, change what the check reads
   instead.** #860 (three rounds of merge-shape examples) and #868 (three
   rounds of brace spellings) were each reframed for this.
   - #860 now states the rule once, as the git command `own_commits` runs, and
     pins each shape as a test.
   - #868 now reads a segment's raw text with quoted spans neutralised and
     errs toward stopping.
7. **A subagent refused by the permission layer is not done for.** Re-run the
   step with a fresh agent. Do not write files on its behalf. A previous
   attempt left `<old scratch>/1791384158/round-2/`, which is old-machine
   scratch only.

## Issues this run filed

- #877: `survivor-check` reads a hand-typed `--range` holding a merge.
- #883: a head run that pytest stopped with exit 0 still seals.
- #884: unplaced counts; fixed by #880.
- #885: remove `SCALE_FOR_OLDER_HOOKS` after 0.21.
- #886: the guard reads past substitution, a here-string, an untokenizable
  line, or `--git-dir`.
- #888: evidence-check's opener misses a Go receiver, a generic function and a
  typed constant. Closed as moot when #870 landed.
- #891: a skipped or xfailed subtest at pytest's default verbosity still holds
  its ledger test row (#836's round 4).
- #892: a claim on a decorated Python definition leaves the decorators out of
  its hash (#870's round 3).
- #893: a tokens comment and the rebase sentence say more than the guard and
  git do (#868's round 6); the second bears on the owner's P2.

Filed earlier by the frames: #871, #872, #873, #874.

## Starting on a new machine

1. `git fetch origin`, then check `git config user.email` against the pinned
   address before the first commit.
2. Make one worktree per item that runs concurrently:
   `git worktree add ../SpecSeal-worktrees/<issue> <branch>`. The guard asks
   once; `[worktree-ok]` answers it for concurrent work.
3. Run tests with `bin/test <files>` (not `uv run --frozen pytest`). Use
   `uvx ruff` and `gh issue view N --json title,body,comments`.
4. Agents: framer on `model: fable`; smith, warden and sealer on
   `model: opus`.
5. At each segment's end, post its reading with `session_cost.py --segments
   <transcript> --post --says -` to the open `flow-measurement` issue (#865).
   `--post` exits 0 even when the post fails, so read its last line.
6. Keep the machine awake on an unattended run (`caffeinate -i`).

## After all eleven land

The release preparation follows `docs/release-checklist.md` §*2. Gather,
fold, bump*:
- gather the eleven `changelog.md` fragments and fold the ledger fragments;
- retire the process records with `settle --retire-process`;
- bump the version;
- open the release PR into `main`, which takes a merge commit.

0.20.0's process records (1791270161–1791270165) are still in the tree, as
#864's frame noted.
