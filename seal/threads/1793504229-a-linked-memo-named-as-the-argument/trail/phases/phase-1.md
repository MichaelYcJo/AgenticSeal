# Phase 1: 1793504229-a-linked-memo-named-as-the-argument

## What this phase found

**The frame held at every coordinate it names.** Read at 847338fd before the first edit, whose `unverified_check.py` is 4da937fa's byte for byte (`git diff --stat 4da937fa HEAD` lists only the three frame files). `real(` stood at lines 943, 1569, 1608, 1626 and 1708 and nowhere else. `#overviews` stood at lines 929 to 956, `#real` at 1022 to 1033, and the second arm at 1680 to 1706 with `os.path.islink(path)` at line 1688. The comment #1235 edits stood at line 113, and this phase did not touch it. `Test_overviews`, `Test_real` and the link cases of `Test_main` stood at lines 1454, 1532 and 2228. No function outside the module calls `real`, `overviews` or `unique_by_target` (`git grep` over `hooks`, `skills` and `bin`). `.claude-plugin/plugin.json` reads 0.27.1.

**The reader is `as_named`, and the repository rule is a function of its own, `repository_of`.** The design leaves the reader's name to the builder. `repository_of` holds Scope item 2: the repository of the real path of the nearest existing ancestor, and only where that is none, the repository holding the deepest link. It is its own function because two callers need it: `as_named` needs the top to know where the kept components start, and `main` needs the root. `as_named` finds the top with `os.path.samefile`, the comparison `absent_root` already makes, so a top that git spells with `/` on Windows still matches. It joins the kept components to `real(prefix)`, not to git's spelling of the top. A path with no link therefore keeps the exact spelling `real()` gave it before, and every line the check prints for such a path is unchanged. Judged against `frame/design.md` *Data & interfaces*, which this reading follows.

**`main` reads each argument through `as_named` once, into a map named `compared`.** The other-volume refusal, the typo check and the presence arm's prefixes read that map. `#overviews` calls `as_named` itself, because it keeps its signature (`frame/design.md` *Data & interfaces*). `as_named` gives back its own output unchanged, so the second call answers the same path. The other-volume refusal used to read `real(nearest_existing(p))`. It now reads `as_named(p)`, which reaches the repository through `nearest_existing` inside `repository_of`. A missing path has the same relative form either way, so the refusal answers the same.

**The second arm's condition is the design's, `os.path.realpath(path) == path`, without a case fold.** On Windows a person can type a component in another case than the disk holds. Then the path is not its own real path, and the arm reads the base at the typed spelling. git's tree lookup is case-sensitive, so `show` answers None and the arm reports nothing. No line is reported twice, so the condition was left as the design states it.

**`as_named` takes `os.path.abspath` of the argument first, so a `..` after a link is removed by text.** `specs/a/../b` reads as `specs/b` even where `specs/a` is a link elsewhere, where `real()` used to follow the link and then go up. The path as typed is what this work keeps, so the text reading is the one that matches it. No case pins this, and no layout of the plugin names a record that way.

**Two departures from the frame's list of cases.**

- `Test_repository_of` was added with two cases, though Scope item 5 lists a unit case for the reader alone. The module's docstring gives one class per function, and `repository_of` is a function the frame did not name. Its first case pins the layout the deepest-link alternative breaks (`frame/plan.md` *Alternatives considered*, the deepest-link row): a checkout linked from a directory that is itself a repository is compared in the checkout. No case did that before. The second case pins the walk to the link's repository.
- The lost-nothing case runs two shapes, a file link and a directory link, and not the third. The case pins that the scan and the base listing agree on the path as named. A file under a linked directory reaches `#overviews_at` through the same file prefix as a file link, so a third parameter would cover nothing the first does not.

**Each new case was seen red first** (executed, `bin/test tests/skills/test_unverified_check.py -p no:xdist -q -k ...` with the cases written and the script still at 4da937fa's bytes):

- `Test_main::test_refuses_a_row_lost_through_a_link_the_person_names`, all three shapes: `assert 0 == 1`. Each run exited 0.
- `Test_main::test_refuses_a_row_lost_through_a_named_link_out_of_every_repository`: `assert 2 == 1`, with `--baseline HEAD needs a git repository, and <path> is not in one` on stderr.
- `Test_repository_of`, both cases, and `Test_as_named`, all three cases: `AttributeError`, since neither function existed.
- `Test_main::test_accepts_a_link_the_person_names_that_lost_no_row`, both shapes, passed at 4da937fa, as `frame/design.md` *Grounding* says of P9. It was seen red against a mutation of the build instead, the fifth run below.

**Six `seal mutate` runs, each red** (executed at e4ba92f5, each `seal mutate` exit 0):

1. `as_named` made to return `real(path)` where it found the top: the three named-link shapes, the out-of-every-repository case and `Test_as_named::test_accepts_a_link_inside_the_repository_under_its_own_name` failed.
2. `repository_of`'s walk made to find nothing (`top = None` for each link): `Test_repository_of::test_accepts_the_repository_holding_a_link_out_of_every_repository` and the out-of-every-repository case failed.
3. `repository_of` made to take the deepest link first, and the real path's repository only after: `Test_repository_of::test_accepts_the_repository_the_real_path_is_in_over_the_links` failed, and nothing else did.
4. The second arm's condition put back to `not os.path.islink(path)`: the directory-link and linked-directory shapes failed.
5. The presence arm's `here` built from real paths: both shapes of the lost-nothing case failed.
6. `as_named` made to resolve the argument's directory and keep its last component, the directory-only alternative: `test_refuses_a_deletion_reached_through_a_linked_path[a file]` failed, as `frame/plan.md`'s *Verified by* cell says it must. `[a row]` passed.

A seventh run, the real path's repository dropped with no fallback, failed 51 cases. That shows the rule is load-bearing, but it does not isolate a unit, so the third run above is the one that counts for it.

**The plan's *Verified by* command ran green** (executed): `bin/test tests/skills/test_unverified_check.py -q -k "Test_real or Test_overviews or Test_unique_by_target or Test_main or Test_as_named or Test_repository_of"`, 90 passed, none skipped. `uvx ruff check` and `uvx ruff format --check` passed on the two changed files after one fix, an unused name in the lost-nothing case. `seal layout --pairs tests/skills/test_unverified_check.py` exited 0 with 0 pairs.

**No other place states the reading that changed.** The search was `git grep -i` for `resolved once`, `real()`, `come through here`, `argument is resolved`, `islink(path)` and `whose own path held` across the tree outside `seal/threads/` and `CHANGELOG.md`, and for `symbolic link`, `symlink` and `realpath` in `docs/` and `skills/verify/`. It found the module's own four sentences, rewritten in place, and other readers' resolution in `broad_gate.py`, `pact_check.py`, `payload_meter.py` and `seal.py`, which `frame/design.md` *Scope*, *Out* leaves alone. The resolved-once sentences in `docs/the-record-layout.md`, `docs/the-broad-gate.md` and the module's docstring are about the base revision, not the path. This is a search on wordings, so it is a sample (contract rule 12).
