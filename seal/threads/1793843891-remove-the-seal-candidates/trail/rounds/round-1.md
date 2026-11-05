# Review round 1: 1793843891-remove-the-seal-candidates

```seal
target: 1d9da419 against release/v0.32.3
```

The round reviewed the four commits from 858c5fb7 to 1d9da419 against `origin/release/v0.32.3`, which is 9dd67e2a, the commit the tag v0.32.2 names (executed: `git rev-parse v0.32.2^{commit}`). This is round 1, so no earlier round's facts are carried. The repository declares no `seal/parity.md`, and `seal/config.md` has no `Record language` row, so the record is in English. The diff adds no test, so no new case is read against its group.

Stage 1 read the change against #1375's body (read: `gh issue view 1375`, no comments), `frame/design.md` *Scope* 1 to 7 and its acceptance rows, `frame/plan.md`'s phase row, `docs/releasing/branch-and-release.md:30-43` and `docs/layout/the-record-layout.md:32-74`. Stage 2 read the two rewritten prose files for wrong statements, dangling pointers and broken links, and the version move for what reads it.

The axes for this change are: what still names the removed files (the class of rule 12), the links and cited sections in the two files, the measurement the preview sentence records, the scope of the trademark notice, the version move, and the changelog fragment's facts. The table's request, authorization, query, concurrency and error-path axes have nothing to act on here, because the diff changes no code.

## Findings

None. Each axis above was read or run, and the grounds are under *Confirmations*.

## Confirmations

What matched: *Scope* 1 and S1. `git ls-files assets/seals/candidates` prints nothing, and `test -e assets/seals/candidates` exits 1 (executed). The tag v0.32.2 still holds the eleven files: `git ls-tree -r --name-only v0.32.2 -- assets/seals/candidates` lists 11, and `git cat-file -e v0.32.2:assets/seals/candidates/bee-28-pixel.png` exits 0 (executed). So the changelog's `git show` example names an object that exists.

What matched: S2 and the class of sentences that name the directory or its marks. Both of #1375's searches outside `seal/threads/` exit 1 (executed). This round built its own list by search, which is a sample by wording, as the crafter's phase record also calls its list. `git grep -n -i "candidat"` outside `seal/threads/` and `.test_durations` hits only code variables, `skills/implement/bootstrap.md`'s `Broad gate` candidates, `skills/parity-setup/SKILL.md:26` and test names about commit candidates. None is about the seal (executed). `git grep -n -i -w "bee"` hits `assets/seals/README.md:122` alone. `git grep -n -e "후보" -e "꿀벌"` hits `docs/layout/one-root-by-lifetime.ko.md:148` alone, which means a commit candidate (executed). The crafter claimed one remaining hit about the seal candidates, the horned owl's entry. That is what this round found.

What matched: G2, nothing reads the directory. `git grep -n "assets"` over `tests`, `hooks`, `bin`, `.github`, `skills`, `docs` and the config files hits `.github/scripts/publish_release_note.py:653`, a comment about `owl.svg`, `docs/releasing/branch-and-release.md:104`, also about `owl.svg`, and the path list entry `tests/behaviour/test_the_release_check_watches_what_ships.py:55` (executed). The root `README.md:2,136` and `README.ko.md:2,140` name only `owl.svg` and `owl.png`, which stay (executed). `git grep -n '\.ans\b'` outside `seal/threads/` and `assets/` hits `TRADEMARKS.md:10` alone, so no check or exception keyed on the removed `.ans` files is left standing (executed).

What matched: *Scope* 2 and S4. `assets/seals/README.md` has no `## Candidates` heading. Its headings end at `## The next entry` (`:223`), and the file ends at `:230` with one newline (executed: `grep -n '^#'`, `od -c` on the tail). No remaining line points into the removed section. A scan of `:93-230` for "below", "above", "frame", "disc" and `read_sprite` finds only pointers to sections that stay (executed). The sprite rule that the removed paragraph explained stands in `skills/verify/scripts/seal_stamp.py#read_sprite`, as G6 says. This round did not reread that docstring, because the diff does not touch it.

What matched: *Scope* 3 against G5. The new sentence at `assets/seals/README.md:35-38` claims a Pillow 12.3.0 match for the gold lily, the red lily and the placeholder S. At 74a680c1, where the old wording came in, `git ls-tree -r --name-only 74a680c1 -- assets/seals` lists `gold-lily.ans`, `red-lily.ans`, `placeholder-s.ans` and `owl.ans` in the directory, and three `.ans` files in `candidates/` (executed). The sentence there (`git show 74a680c1:assets/seals/README.md`, `:29-31`) sets `owl.png` apart as "drawn the same way", which the new text keeps under the file's later name `horned-owl.png`. At the base, the directory also held the little owl's `owl.ans`, whose preview was drawn with Pillow 13.0.0. So the base's "every preview of a `.ans` in this directory" was already wider than what had been measured, and the rewrite narrows it to the measured set. G5 says `git log -S` gives two commits. This round's `git log --oneline -S "Pillow 12.3.0" -- assets/seals/README.md` printed only 43cbc361, because 74a680c1 reworded the sentence without changing the string's count (executed). G5 does not name its search string. The coordinate it cites, 74a680c1, holds the wording G5 quotes, so the grounding stands.

What matched: *Scope* 4. `assets/seals/README.md:122` reads "over the bee, in two forms", with "below" gone and no other word changed in the item (read: the diff). The cost the plan names, a bee that no file at HEAD shows, is the one `frame/plan.md` *Technical context* accepts.

What matched: *Scope* 5 and S5. `TRADEMARKS.md:10-12` names every `.svg`, `.png` and `.ans` file under `assets/seals/` and drops the candidates and `.txt` clauses. `ls assets/seals/` lists no `.txt` file (executed), and `skills/verify/scripts/seal-mark.txt` keeps its own item at `TRADEMARKS.md:13-14`. Every file the notice still names under `assets/seals/` is a drawing of the gold lily, the red lily, the placeholder S or an owl, each of which a release carried by the README's own entries. The one exception is `owl-social.*`, a social preview of the owl. The base's wording already put it under the same claim, so the diff does not change that.

What matched: S3. Every `](target)` in `assets/seals/README.md`, resolved from `assets/seals/`, and in `TRADEMARKS.md`, resolved from the root, exists: 11 targets, 0 missing, in one `python3 -c` command that writes nothing (executed). The crafter claimed 11 and 0. This round counted the same.

What matched: S6, the wrap, and the version move by narrow runs. `bin/test` over `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_the_release_check_watches_what_ships.py` and `tests/behaviour/test_release_hygiene.py` ended 170 passed, exit 0 (executed). `bin/test` over the 20 modules `git grep -l plugin.json -- tests` lists ended 1249 passed, 1 skipped, exit 0 (executed). The crafter claimed 20 modules from that search. This round's search listed 20.

What matched: *Scope* 6 and S7. `.claude-plugin/plugin.json:4` reads `0.32.3` and parses as JSON (executed). `git grep -n "0\.32\.[23]"` outside `seal/threads/` and `.test_durations` hits that line alone, so no second version string was left at 0.32.2 (executed). `docs/releasing/branch-and-release.md:30-38` puts the move in the commit that adds the release's first changelog fragment. 4c453c20 holds both `plugin.json` and `changelog.md` (executed: `git show --stat 4c453c20`).

What matched: *Scope* 7. `changelog.md` holds one `### Removed` entry naming #1375 and no `### Process changes` table. The diff touches none of the files that `docs/layout/the-record-layout.md:52` names as needing that table (read). The entry's facts match the tree. The eleven files are three sets of `.ans`, `.png` and `.txt`, plus `bee-web.svg` and `bee-web.png`. The README removed three `###` entries and four image links (read: the diff). The little owl has been the mark since 0.25.1 (`assets/seals/README.md:150`).

What matched: the changed paths. `git diff --stat origin/release/v0.32.3..HEAD` lists the eleven removed files, `assets/seals/README.md`, `TRADEMARKS.md`, `.claude-plugin/plugin.json` and this work item's records, and nothing else (executed). The crafter claimed 1d9da419 changes only `frame/plan.md`'s Status cell. `git diff 4c453c20 1d9da419` changes that one row, and only its last cell (executed).

What matched: no case is written new. The crafter claimed the phase adds no behaviour, so no case is owed. The diff removes files and prose and moves one version string. The checks that parse the two files and the version ran green above. `skills/code-review/SKILL.md` *Probes and regression tests* says a change that adds no behaviour owes no case written new (read).

What matched: the suite's label. `gaps.md` labels the full suite, the lint and the format check `unverified` and names the orchestrator's broad run as the answerer (read). The label is honest. The crafter also claimed a 37-module run of 2498 passed, 10 skipped. This round re-ran 22 modules, the union of the two runs above (executed: `sort -u` over the two module lists), and not the rest of the crafter's 37 (see *Not judged*).

No finding is open. What comes due next is the orchestrator's broad run of the `Broad gate` row, and then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at 1d9da419 | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| The crafter's 37-module run (2498 passed, 10 skipped). This round re-ran the plan's three modules, `test_release_hygiene.py` and the 20 `plugin.json` modules. It did not re-run the other tree-globbing modules the phase record lists | `seal/threads/1793843891-remove-the-seal-candidates/trail/phases/phase-1.md` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `git ls-files assets/seals/candidates`; `test -e assets/seals/candidates` | nothing listed; exit 1 |
| `git grep -n "seals/candidates\|candidates/" -- ':!seal/threads'`, then with `bee-28\|bee-web\|section-28\|section-14` | exit 1, exit 1 |
| `python3 -c` resolving each `](target)` of `assets/seals/README.md` and `TRADEMARKS.md` | 11 targets, 0 missing |
| `python3 -c 'import json; print(json.load(open(".claude-plugin/plugin.json"))["version"])'` | `0.32.3` |
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_release_hygiene.py -q -p no:randomly` | 170 passed, exit 0 |
| `bin/test` over the 20 modules of `git grep -l plugin.json -- tests`, `-q` | 1249 passed, 1 skipped, exit 0 |
| `git ls-tree -r --name-only v0.32.2 -- assets/seals/candidates`; `git cat-file -e v0.32.2:assets/seals/candidates/bee-28-pixel.png` | 11 files; exit 0 |
| `git log --oneline -S "Pillow 12.3.0" -- assets/seals/README.md`; `git ls-tree -r --name-only 74a680c1 -- assets/seals` | 43cbc361 alone; the four `.ans` files and three candidate `.ans` files named above |
