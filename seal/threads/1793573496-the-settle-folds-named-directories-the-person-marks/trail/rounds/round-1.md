# Review round 1: 1793573496-the-settle-folds-named-directories-the-person-marks

```seal
target: 0cdf4ce70 against origin/release/v0.28.0
```

This round reviewed the branch at `0cdf4ce70` against `origin/release/v0.28.0`
(`57d6665b5`), in the branch's own worktree. No earlier round exists, so no
verdict was carried. Carried as coordinates and not re-established: the
frame's probes P1 and P2, and phase 1's `seal mutate` table in
`trail/phases/phase-1.md`, which this round read and did not re-run. No
`seal/parity.md` is declared, so the round block holds no `original:` line.
`seal/config.md` holds no `Record language` row, so the record is English.

## Findings

### 1. The listing names a parent's commit as the last change of a document a merge resolved

```seal
severity: should
location: `skills/settle/scripts/settle.py:878-902`, `tests/skills/test_settle.py:1940`
evidence: executed `python3 test_tmp_named.py (a no-ff merge whose conflict resolution rewrites adr/0001.md, then settle.main --root repo --from repo/adr)`, `git log -z --full-history --topo-order --reverse --no-renames --name-status --cc --format=%x01%h %cs HEAD -- adr (same history)`
```

Why it matters: the line `last changed <commit>` is what the settling
session reads in two places. *Directories a person names* uses it to place a
promoted document in its group ("a document deciding as of its last
change"). It also uses it to tell a document skipped at an earlier settle,
with `git merge-base --is-ancestor <last change> <merge commit>`. The
docstring at `settle.py:878-884` claims `last` is "the last commit naming
it". `git log --name-status` prints no diff for a merge commit unless asked.
So a merge whose conflict resolution rewrote a document is never read as a
change to it.

The probe built `base` adding `adr/0001.md`, a `side` branch and `main` each
editing it, and a `--no-ff` merge whose resolution wrote new content. The
listing printed `adr/0001.md  added 9a6fadf  last changed f0c11b8`. That is
the side branch's commit, whose content the file no longer holds, and no
`changed in the working tree` follows it. The merge `568e4f3` is the commit
that last changed it. Run with `--cc`, the same `git log` adds the fields
`""`, `"MM"`, `"adr/0001.md"` after the merge's header. The loop at
`settle.py:887-901` already reads that shape as a status and then a path, so
`last` becomes the merge. A clean merge adds no field under `--cc`, so a
document a clean merge brought in keeps the side branch's commit, as now.
`rule_changes.py#order` reads a design's adding commit with no merge diff,
and `--cc` leaves `added` as it is for every path a commit outside a merge
adds. The two orders still compare as design G14 asks.

The squash-merge flow this repository uses never produces this. A user
repository that merges with merge commits does produce it, and the listing
is for such repositories' decision records.

```python
    fields = git_fields(
        root, "log", "-z", "--full-history", "--topo-order", "--reverse",
        "--no-renames", "--name-status", "--cc", "--format=%x01%h %cs",
        "HEAD", "--", rel,
    )  # fmt: skip
```

The case belongs beside A2 in `tests/skills/test_settle.py`'s `Test_main`.
`git` there runs with `check=True`, and a conflicting merge exits 1, so the
merge goes through `subprocess.run` directly:

```python
    def test_a_merge_that_resolved_a_document_is_its_last_change(
        self, repo, capfd, monkeypatch
    ):
        """#1054: a merge whose conflict resolution rewrote a document is the
        commit that last changed it, since `git log` prints a merge's change
        only under `--cc`."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "adr/0001.md", "one\n")
        commit(repo, "a decision")
        first = stamp(repo)
        git(repo, "checkout", "-qb", "side")
        write(repo, "adr/0001.md", "side\n")
        commit(repo, "side")
        git(repo, "checkout", "-q", "main")
        write(repo, "adr/0001.md", "main\n")
        commit(repo, "main")
        subprocess.run(
            ["git", "-C", str(repo), "merge", "--no-ff", "-q", "side"],
            capture_output=True,
        )
        write(repo, "adr/0001.md", "resolved\n")
        commit(repo, "merge side, resolved")
        merged = stamp(repo)
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0001.md  added {first}  last changed {merged}\n" in text, text
```

The skill's line on the listing (`skills/settle/SKILL.md:218-220`) and the
module docstring's (`settle.py:62-64`) then say that a merge's own change is
read too.

### 2. A `--from` refused as no directory names the repository, though the path was read from the working directory

```seal
severity: should
location: `skills/settle/scripts/settle.py:480-483`, `skills/settle/scripts/settle.py:851-863`, `tests/skills/test_settle.py:2026`
evidence: read `skills/settle/scripts/settle.py:480-483`, `skills/settle/scripts/settle.py:851-863`, `skills/settle/scripts/settle.py:1270-1310`
```

Why it matters: `named_directory` resolves GIVEN with
`os.path.abspath(given)`, from the directory the command runs in
(`settle.py:856`). The refusal then says `--from {given} names no directory
in the working tree of {root}`, and `main` has replaced ROOT with the
repository's top (`settle.py:1278`). Run from `docs/` with `--from adr`,
or as `seal settle --root /r --from adr` from elsewhere, the command reads
`<cwd>/adr`. It then tells the person that `adr` is no directory of the
repository, while `/r/adr` is one. The sentence is false, and the person's
next act, checking the repository for `adr`, finds it there. The help and
the skill both say a relative `--from` is read from the directory the
command runs in, so the behaviour is the frame's and only the sentence is
wrong.

```python
FROM_NOT_A_DIRECTORY = (
    "settle: --from {given} names no directory: read from the directory this "
    "runs in, it is {path}, so nothing was read.\n"
)
```

with `FROM_NOT_A_DIRECTORY.format(given=given, path=path)` at
`settle.py:859`. The parametrized refusal case at `tests/skills/test_settle.py:2026`
pins the opening `names no directory`, which still holds. Contract rule 14
asks a case to pin the new clause. A case run with `monkeypatch.chdir(repo / "docs")`
and `--from adr`, where `adr/` exists at the top, should assert that the
sentence names `docs/adr` (no sentence like that is in the tree yet).

### 3. The cheat-sheet case reads a 900-character window, not the row, and the `seal settle` row was cut to fit it

```seal
severity: should
location: `tests/text/test_settle_reads_before_it_removes.py:22-33`, `README.md:265`, `README.ko.md:259`
evidence: executed `python3 - (length of the seal settle row in README.md and README.ko.md, and the offset of frame/design.md after the cell in the folded text)`
```

Why it matters: the crafter claimed in `trail/phases/phase-2.md` that the
English row put `` `frame/design.md` `` at character 917, past the window,
and so dropped "before its first edit" and "`--apply` refuses `--from`" from
it. The case at `test_settle_reads_before_it_removes.py:32` reads
`document(edition).split("`seal settle [--apply]`")[1][:900]`. That is 900
characters of the whole folded file after the cell, and not the row. The
measurement found the English row 932 characters long now, with the path at
878, and the Korean row 600 characters long. So the Korean window reads 300
characters into the `seal fold` row. The case refuses a correct row past 900
characters and would pass a row that lacks the path where the next row
names it. `skills/core/SKILL.md` *The rule a mechanism is kept against*
holds a check to a fact it reads exactly, and the row is one line.
Contract rule 18 allows the crafter to report the refusal instead of fixing
it, and the crafter reported it. The prose was still bent to fit a check
that reads the wrong unit. The README row now says "first asks", which is
true, so the row states nothing false. It lost the one sentence that tells
a reader `--apply` refuses `--from`.

```python
def test_the_cheat_sheets_name_the_design_file_the_settle_reads():
    """Contract rule 14's half of D3. Each README edition's `seal settle`
    row names the file whose rule changes the settle reads. Whether a
    released work item with no design leaves like any other is the
    proofer's to read."""
    for edition in ("README.md", "README.ko.md"):
        with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
            # The row is one line of the table: the cell, then up to its end.
            row = f.read().split("`seal settle [--apply]`")[1].split("\n", 1)[0]
        assert "`frame/design.md`" in row, (
            f"{edition}'s cheat-sheet row does not name the rule arm"
        )
```

With the case reading the row, `README.md:265` can carry the two clauses
again: "The session running the settle first asks the person, before its
first edit, which directories to name and which of their documents to
promote, ...". `--from` is refused beside `--apply`. `README.ko.md:259`
carries the same pair.

### 4. A case's docstring still says no code of the plugin opens a top-level `specs/`

```seal
severity: should
location: `tests/behaviour/test_no_document_names_the_old_roots.py:98-101`
evidence: executed `python3 - (each tracked file outside seal/threads, whitespace folded, searched for top-level specs/, never read or never open specs, and reference root near never)`
```

Why it matters: `test_no_hook_names_the_0_3_x_roots` opens "No code of the
plugin opens `.specseal/` or a top-level `specs/`". After this branch,
`seal settle --from specs` opens a top-level `specs/` where a person names
it. Design G6 and the rule change for `docs/one-root-by-lifetime.md` add "on
its own" to the same sentence for that reason. The policy root waits for
the settle, and this docstring does not: it is under `tests/`, which the
build edits. Design G6 named this module for its allowlist entries and kept
them, and phase 2's census searched for "asks nobody" and "never input" but
not for this sentence (contract rule 19). The case checks `hooks/` alone,
so its assertion holds and only its premise is stale. A session reading the
docstring takes it as the rule and reads `--from` as a breach of it. The
census was a search by wording, so it is a sample. It found this docstring
and the two `docs/` editions, which the rule changes cover. Every other hit
spoke of a reference root being read and never moved or written, which
stays true.

```python
def test_no_hook_names_the_0_3_x_roots():
    """No code of the plugin opens `.specseal/` or a top-level `specs/` on
    its own, so no file under `hooks/`, its modules in `hooks/lib/` among
    them, names the first or keeps a constant for the second."""
```

## Confirmations

```seal
confirms: none
```
What matched: no text of the build lets a reader take the script's listing
for a proposal, read at each place it is described. `DOCUMENTS_HEADING`
(`settle.py:465-470`) says the settling session proposes and the person
marks. The module docstring (`settle.py:57-70`) says "nothing here reads
what a document says". The `--from` help (`settle.py:1253-1263`) says it
lists and writes nothing. The skill's bullet ends "No line of it is a
proposal" (`skills/settle/SKILL.md:212-227`), *The listing is not a
proposal* says whose the proposal and the mark are, and step 3 says "the
row is yours to write". The changelog says `seal settle` "reads no
document's content and proposes nothing". The README rows say the command
lists. The nearest wording is the changelog's "with a mark where the
working tree changed it", which uses the word "mark" in the sense the same
paragraph later gives the person's mark. The sentence after it removes the
doubt, so it is no finding. A fix pass that touches the fragment can write
"and with `changed in the working tree` where the working tree changed it".

```seal
confirms: none
```
What matched: phase 1's departure holds. Claimed: `git diff HEAD --name-only
-z --no-renames` answers what `git status --porcelain -z` answered for a
tracked file. `changed` (`settle.py:905-909`) names each tracked path whose
working tree, staged or not, differs from HEAD, one path per field, read.
Status also names an untracked file and a staged new file. `documents` prints
both as `no commit adds it` with no working-tree flag, so the listing loses
nothing. One state differs: a change staged and then reverted in the working
tree. Status names it, while `git diff HEAD` does not, and the listing then
says nothing of the working tree, which matches HEAD, so the line is true.

```seal
confirms: none
```
What matched: the frame's earlier decisions are kept, read against D1 to D6.
The script prints only git's facts (D5, G1). `--apply` is unchanged and
refuses `--from` (`settle.py:1266-1268`, D4). The intro states at most two
questions, both before the first edit (`skills/settle/SKILL.md:26-32`), and
step 7 forbids any other question (D6). The departure from #1051 is
confined to a directory a person names, and no configuration row or
discovery was added (D2). Grounding G10 holds by reading:
`hooks/question-gate.py#main` lets every question through where
`routing.declared` finds no declaration. `seal no-work-item` writes no
declaration (`hooks/lib/routing.py:432-438`). So a settle's branch is read as
attended. The release checklist runs the settle only when the owner calls
it (`docs/release-checklist.md:33-35`), so the questions do not reach a
`yes` run.

```seal
confirms: none
```
What matched: the two candidates `gaps.md` *Not done* left are no
findings. `DOCUMENTS_HEADING` cites `skills/settle/SKILL.md` without a
section. `GROUPS_HEADING` (`settle.py:409-414`) and `JUDGMENTS_HEADING`
(`settle.py:443-449`) cite the file the same way, and the heading states
the one fact a reader acts on: the session proposes, and the person marks.
The taglines at `README.md:7-8` and `README.ko.md:7-8` speak of the
workflow that frames, builds, inspects and seals a change. The settle is a
release step the owner calls, and the routing question already stood
before the tagline. Design A9 does not cover them, and no sentence of
theirs is about the settle.

```seal
confirms: none
```
What matched: design A9 holds by a whitespace-folded search, executed over
every tracked file outside `seal/threads/` for "asks nobody", "asking
nobody", "ask no one", "without asking", "asks no question", "never asks",
"asks nothing", "묻지 않" and "아무에게도" near "settle". The only hit about
the settle is `docs/release-checklist.md` *2b*, which the design's `change`
rewrites at the settle. Each `from` of the three `change` operations was
found once in its file with whitespace folded, executed. The pending
designs `1793541310`, `1793541311` and `1793538229` quote other sentences
of the shared sections (executed `awk` over their `## Rule changes`), as
design G9 says.

```seal
confirms: none
```
What matched: the new cases each cover something their group did not, read
against `Test_main`. The only whole-output assertion in the module is the
settled-root case (`tests/skills/test_settle.py:1920`), so A1's absence
check is the one case that holds a dry run with work items free of the
listing. A3 holds the dedupe and the cwd-relative read, A6 holds the dry run
with `--from` and the apply writing nothing under the named directory, and
the A4 cases hold one sentence per refusal. The three modules the plan names
ran green, executed: `bin/test tests/skills/test_settle.py
tests/text/test_settle_reads_before_it_removes.py
tests/behaviour/test_a_reference_root_is_read_and_never_taken.py -q`, exit
0, 128 passed. That is a narrow run, not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Design A7: the two questions, the proposal table and what reaches the policy root, built on `questions.md` Q1 default (a) with no case | `skills/settle/SKILL.md` *Directories a person names* | the owner, reading the first settle's pull request body against its diff |
| The full suite, the lint and the format check at HEAD; this round ran three modules and labels the suite `unverified` | the repository's `Broad gate` row | the orchestrator, by `seal gate --base origin/release/v0.28.0 --record <item>`, then the sealer |
| The listing and the refusals on Windows, and a `--from` whose case differs from the `seal/` root's on a case-insensitive file system, where `os.path.realpath` keeps the case given and `inside` compares strings | `skills/settle/scripts/settle.py:840-863` | the `windows-latest` jobs at the pull request; the orchestrator for whether the second needs a limit sentence |
| Phase 1's `seal mutate` table, carried as read and not re-run | `trail/phases/phase-1.md` | the sealer, which re-runs a sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_named.py <worktree>`, one file under the round's scratch directory, building a repository with a `--no-ff` merge whose conflict resolution rewrote `adr/0001.md`, then `settle.main(["--root", repo, "--from", "repo/adr"])` | exit 0; the listing printed `adr/0001.md  added 9a6fadf 2026-11-02  last changed f0c11b8 2026-11-02`, the side branch's commit, while the merge `568e4f3` wrote the file's content |
| `git log -z ... --name-status [--cc] ... HEAD -- adr` over the probe's repository, fields split on NUL | without `--cc` the merge's header is followed by nothing; with `--cc` it is followed by `""`, `"MM"`, `"adr/0001.md"`. The probe file and its repository were removed before hand-back |
