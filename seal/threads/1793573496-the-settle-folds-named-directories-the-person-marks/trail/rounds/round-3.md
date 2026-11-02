# Review round 3: 1793573496-the-settle-folds-named-directories-the-person-marks

```seal
target: 75284e476, fixes f37176aef..75284e476
```

This verifying round read the diff `f37176aef..75284e476` in the branch's own
worktree. That diff holds round 2's record (`2c4023db8`), the orchestrator's
judgment row (`daeba6a38`), the fix pass's two commits (`2ba0c6866`,
`fed390e7b`), its close block (`9faca3bac`) and the orchestrator's fold
(`75284e476`). Carried from rounds 1 and 2 as coordinates, not
re-established: where the listing lives (`settle.py#history`, `#changed`,
`#documents`), the `Test_main` cases that read it, and round 1's `MM` case.
No `seal/parity.md` is declared, so the round block holds no `original:`
line. `seal/config.md` holds no `Record language` row, so the record is
English.

The fix pass's account was read as a claim. It said its status shapes came
from a probe and from "git's rule that a merge is named only where its result
differs from every parent". This round read the rule from git's own pages
instead: `git-diff-tree(1)` *DIFF FORMAT FOR MERGES* and the `-c` and `--cc`
entries, and the status letters under *Possible status letters are*. The
pages say the combined status is "concatenated status characters for each
parent". They also say a combined diff "lists only files which were modified
from all parents". `--cc` compresses only the patch output. The letters git
documents are `A`, `C`, `D`, `M`, `R`, `T`, `U` and `X`. With `--no-renames`
there is no `C` or `R`. `U` names an unmerged index entry and never a
commit. `X` names a git bug. So a commit's letters are `A`, `M`, `T` and
`D`, and the letters of one path cannot mix `D` with the others: a `D`
against one parent means the result lacks the path, and any other letter
means the result holds it. The stated rule (no `D` changes the path, all `A`
also adds it, all `D` is neither) reads every status git can print for these
arguments. Two things the rule stands on do not hold, and they are this
round's findings. The docstring's premise that a clean merge names nothing
is false (finding 1). A user's git configuration can take away the commits
the rule reads, or put text into the fields it parses (finding 2). Neither
is a `must`.

## Findings

### 1. A clean merge that combined both branches' edits to one document is named, and the docstring says no clean merge is

```seal
severity: should
location: `skills/settle/scripts/settle.py:900-903`, `skills/settle/scripts/settle.py:63-66`, `skills/settle/SKILL.md:220-224`, `seal/threads/1793573496-the-settle-folds-named-directories-the-person-marks/changelog.md:3`, `tests/skills/test_settle.py:1998-2025`
evidence: executed `bin/test tests/skills/test_tmp_round3_1054.py -q -rP -p no:xdist (test_tmp_clean_merge_of_two_hunks, a merge with no conflict of a branch that edited line 25 of adr/0001.md and one that edited line 2)`
regression: round-2#1
```

The unit is `settle.py#history`'s docstring. The design's *Data & interfaces*
(`frame/design.md:99`) and phase 1's plan row say the last change is the last
line that names the path, read by one rule over the status letters. The fix
`2ba0c6866` kept that rule. But it repeated a sentence from `47c1bf70b`, round
1's fix, that a clean merge names nothing, and it built the enumeration on
that sentence. That sentence came from round 1's probe, a merge in which only
one side had touched the file. git's own page (`git-diff-tree(1)`, `-c`)
says a combined diff lists every file "modified from all parents", and a
merge with no conflict that combines two branches' edits to one file is such
a file.

Why it matters: the docstring is the place where the run decided which
shapes the history reader meets. It says "A merge is named at a path only
where its result differs from every parent, so a clean merge, or one whose
result is one parent's, names nothing" (`settle.py:900-903`). The first half
is git's rule. The second half does not follow from it. The probe built a
document on `main`. `side` edited line 25 and `main` edited line 2, and
`git merge --no-ff` merged them with no conflict. `git log --cc` gave the
merge `MM adr/0001.md`, and `history` returned the merge (`c44f439`) as the
document's last change, executed. The listing is right to do this: the
merge's tree holds content that neither parent held, and the rule reads `MM`
as a change. What is wrong is the text that explains it. The skill tells the
settling session that a merge is the change only where it "resolved a
conflict in it" (`SKILL.md:221-222`), and the module docstring
(`settle.py:65`) and the changelog say the same. A session that reads a
merge as a document's last change will then believe a conflict was resolved
there. The next agent to edit `history` reads that clean merges never count.
No case pins this shape: the four merge cases all build a conflict, a
deletion, or a file one parent lacks.

Not a `must`: what the listing prints is correct for this shape. Only the
sentences that explain it are wrong.

The docstring at `settle.py:900-903`:

```python
    parent holds it, and this commit does not). A merge is named at a path
    only where its result differs from every parent: one that resolved a
    conflict in it, wrote it new, or combined two parents' edits to it with
    no conflict. A merge whose result is one parent's names nothing. The
    letters of one status are either all `D` or all from `A`, `M` and `T`.
```

The module docstring (`settle.py:64-65`), the skill's bullet
(`SKILL.md:221-222`) and the changelog's sentence say, in their own words: "a
merge that wrote a file no parent holds added it, and one whose result
differs from every parent at it, a conflict it resolved or two parents'
edits it combined, changed it". The case goes beside
`test_a_merge_that_resolved_a_document_is_its_last_change`. The merge is
clean, so `git` with `check=True` stands:

```python
    def test_a_clean_merge_of_two_edits_is_a_documents_last_change(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 3's finding 1: a merge with no conflict that combines
        two branches' edits to one document holds content neither parent
        holds, so `--cc` names it `MM` and it is the last change."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        body = "".join(f"line {i}\n" for i in range(30))
        write(repo, "adr/0001.md", body)
        commit(repo, "a decision")
        first = stamp(repo)
        git(repo, "checkout", "-qb", "side")
        write(repo, "adr/0001.md", body.replace("line 25\n", "line 25, side\n"))
        commit(repo, "side edits the end")
        git(repo, "checkout", "-q", "main")
        write(repo, "adr/0001.md", body.replace("line 2\n", "line 2, main\n"))
        commit(repo, "main edits the start")
        git(repo, "merge", "--no-ff", "-q", "-m", "merge side", "side")
        merged = stamp(repo)
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0001.md  added {first}  last changed {merged}\n" in text, text
```

The case passes against the current reader, because the behaviour is
already right. It pins the explanation that the docstring and the skill now
give, and it goes red under a reader that skips a merge it calls clean.

### 2. A user's `log.showRoot` or `log.showSignature` changes what the history reader parses, and the listing then misdates documents

```seal
severity: should
location: `skills/settle/scripts/settle.py:915-919`, `skills/settle/scripts/settle.py:895-897`, `skills/settle/scripts/rule_changes.py:358-363`, `tests/skills/test_settle.py:2109`
evidence: executed `bin/test tests/skills/test_tmp_round3_1054.py -q -rP -p no:xdist (test_tmp_config_shapes: settle.history under GIT_CONFIG_GLOBAL holding log.showRoot=false, log.follow=true, diff.renames=copies, log.diffMerges=first-parent)`, `git -c log.showRoot=false log --root ... HEAD -- adr, in a scratch repository under the round's scratch directory`, `git -c log.showSignature=true log -z ... HEAD -- adr over an ssh-signed commit, with and without --no-show-signature`
```

Why it matters: `history` runs `git log` with no `-c` and no flag that fixes
these two keys (`settle.py:915-919`). So the git configuration of the person
running the settle decides what the walk reads. The docstring says "a commit
with one parent, or none, has one letter" (`settle.py:896-897`). That is true
only while git shows the root commit's diff.

- **`log.showRoot=false`**. The probe set it through `GIT_CONFIG_GLOBAL` and
  called `history` on `docs`, which the fixture's root commit adds. It
  returned `({}, {})`, executed. A document the root commit added and no
  later commit changed is listed `no commit adds it`. If a later commit
  changed it, `last` holds that commit but `added` holds nothing, and
  `documents` prints `no commit adds it` (`settle.py:967-968`, `:985-986`),
  read. The skill says that line means "untracked or staged and never
  committed" (`SKILL.md:226-227`). With `--root` added, the same
  configuration printed `A adr/0001.md` at the root commit, executed.
- **`log.showSignature=true`** on a signed commit. git writes its
  verification text into the log's standard output, before that commit's
  header. Over an ssh-signed commit with no allowed-signers file, the field
  that should open with byte 0x01 read `No signature`, a newline, then
  `\x01fc95695 2026-11-02`, executed. The loop strips only newlines on the
  left (`settle.py:929`), so it reads that field as a status. It then reads
  the next status as a path and the signed commit's path as a status. The
  signed commit's change is lost: the earlier commit stays the last change,
  and a document the signed commit added prints `no commit adds it`, read.
  A repository whose merges GitHub signs, read by a person with this key
  set, meets this on every signed commit. With `--no-show-signature` the
  same configuration printed the header alone, executed.

How the class was listed (contract rule 12): this round took apart the list
of configuration keys `git-config(1)` documents under `log.` and `diff.`,
46 keys. Each was read against what the reader's command prints. Most govern
patch text, colour, decoration or dates, and `--format=%x01%h %cs` with
`--name-status` prints none of these. Four were run and change nothing:
`log.follow`, `diff.renames` (`--no-renames` overrides it),
`log.diffMerges` (`--cc` overrides it; read for merges, run on a history
with none), and `color.ui` and `color.diff` set to `always`. Two change the
output: `log.showRoot` and `log.showSignature`. The list stops at the keys
git documents for these two prefixes. A key from another prefix that
reshapes `git log` output was not looked for, so that part is a sample.

The same class reaches `rule_changes.py#order` (`rule_changes.py:358-363`),
which orders designs with a `git log` that has the same exposure to
`log.showSignature`. That line stands at the base and is outside this
branch's diff. Where it is fixed is the orchestrator's call.

Not a `must`: both keys are off by default, and the defect stands in the
reader as phase 1 built it, not in this fix diff. It still prints a wrong
line to a person, so the release would ship it.

```python
    fields = git_fields(
        root, "log", "-z", "--full-history", "--topo-order", "--reverse",
        "--no-renames", "--name-status", "--cc", "--root", "--no-show-signature",
        "--format=%x01%h %cs", "HEAD", "--", rel,
    )  # fmt: skip
```

Precondition: `--no-show-signature` needs git 2.10 or later. `--root` does
nothing where `log.showRoot` is true, which is git's default. The docstring
gains: "`--root` and `--no-show-signature` hold the walk to these fields
whatever the person's `log.showRoot` and `log.showSignature` say." A case
beside `test_a_file_under_two_named_directories_is_listed_once` sets the
key for the run only. `GIT_CONFIG_COUNT` needs git 2.31 or later:

```python
    def test_a_document_the_root_commit_added_is_dated_under_any_show_root(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 3's finding 2: `log.showRoot=false` hides the root
        commit's names from `git log`, and the listing reads it anyway."""
        root = git(repo, "log", "-1", "--format=%h %cs").strip()
        monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
        monkeypatch.setenv("GIT_CONFIG_KEY_0", "log.showRoot")
        monkeypatch.setenv("GIT_CONFIG_VALUE_0", "false")
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "docs")
        assert code == 0, text
        assert f"    docs/a.md  added {root}  last changed {root}\n" in text, text
```

This round did not run either case it proposes: the snippets above and in
finding 1 are unverified, and the fix pass shows each red before it is
committed. A signature case needs a signed commit, which `ssh-keygen` and
`gpg.format=ssh` can make inside the fixture. Where `ssh-keygen` is missing
it skips, as `symlink_or_skip` does for links. Whether that case earns its
cost beside the flag is the fix pass's call. The flag alone is read by no
case.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `history` adds a path only where every letter of its status is
`A` (`settle.py:925-926`), read. Each new case was run against the reader at
`2c4023db8` and at HEAD, executed.
`test_a_merge_that_wrote_a_document_no_parent_holds_adds_it` failed at
`2c4023db8` and passed at HEAD. This is round 2's own shape, `AA`.
`test_a_deletion_is_no_change_to_a_document_head_holds` failed at
`2c4023db8` and passed at HEAD.
`test_a_merge_that_rewrote_a_document_one_parent_lacks_changes_it` (`AM`)
passed at both. That matches the fix pass's account: the case was added to
kill the mutant `"A" in status`, and the old reader is not that mutant. The
mutation run itself was read, not re-run. Round 1's
`test_a_merge_that_resolved_a_document_is_its_last_change` passed at both.
The probe also built `DD` (a merge that deleted a file both parents hold)
and `AAA` (an octopus merge that wrote a file none of its three parents
holds). `--cc` printed exactly those statuses, and `history` read `AAA` as
the add and `DD` as neither, executed. The module docstring, the skill's
bullet, the changelog and the design's fold say that a merge that wrote a
file no parent holds added it, and that a deletion is neither its add nor
its change, read. Finding 1 above corrects the docstring's premise about
clean merges. The rule itself holds against git's documented letters, as
the opening section sets out.

```seal
confirms: none
```
What matched: the orchestrator's fold (`frame/design.md:99`) states the
reader's one rule in the words the docstring uses (`settle.py:905-911`),
read. The judgment row at `frame/plan.md:53` makes the re-created untracked
file a limit, and the docstring's last sentence (`settle.py:912-914`) states
it, read. That sentence names a path HEAD "holds again only untracked". A
path staged again and never committed meets the same limit, since `git
ls-files --cached` lists it. The skill's `no commit adds it` sentence says
"never committed", which stays true, so this is no finding.

```seal
confirms: none
```
What matched: each new case covers what its group did not. `Test_main`'s
merge cases before this diff held one shape, `MM`. `AA`, `AM` and the
deletion each read a different branch of the rule, read. The narrow runs
passed, executed: `bin/test tests/skills/test_settle.py
tests/text/test_settle_reads_before_it_removes.py
tests/behaviour/test_a_reference_root_is_read_and_never_taken.py
tests/behaviour/test_docs_line_wrap.py -q` exited 0 with 178 passed, and
`bin/test tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py
tests/behaviour/test_settle_applies_rule_changes_in_place.py
tests/skills/test_rule_changes.py -q` exited 0 with 109 passed and 8
skipped. These are narrow runs, not the broad gate. No line the diff adds to
`settle.py` or `test_settle.py` is longer than 88 characters, read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the lint and the format check at HEAD. This round ran seven modules, and the suite is labelled `unverified` | the repository's `Broad gate` row | the orchestrator, by `seal gate --base origin/release/v0.28.0 --record <item>`, then the sealer |
| The fix pass's `seal mutate` claims (the `"A" in status` mutant that `fed390e7b` kills, and the add and `D` arms going red), read and not re-run | `trail/rounds/round-2.md`, close block of finding 1 | the sealer, which re-runs a sample of the crafter's claims |
| `log.showSignature` over a GPG-signed commit; only an ssh-signed commit with no allowed-signers file was run | `skills/settle/scripts/settle.py:915-919` | the fix pass for finding 2, whose flag covers both signing formats |
| Configuration keys outside `log.` and `diff.` that reshape `git log` output, which finding 2's list did not take apart | `skills/settle/scripts/settle.py:915-919` | the orchestrator, judging whether finding 2's list is enough |
| Round 1's rows for design A7, and for Windows and case-insensitive paths, carried as they stand | `trail/rounds/round-1.md` *Not judged* | the answerers round 1 names |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round3_1054.py -q -rP -p no:xdist`, one file in the worktree's `tests/skills/` using `test_settle`'s fixtures | A merge with no conflict of edits to lines 2 and 25 of `adr/0001.md`: `--cc` printed `MM adr/0001.md` at the merge, and `history` gave the merge `c44f439` as the last change. A merge that deleted `adr/0001.md`, which both parents held, printed `DD`. An octopus merge that wrote `adr/octo.md` printed `AAA`, and `history` gave it as the add. Under `GIT_CONFIG_GLOBAL` with `log.showRoot=false`, `history(repo, "docs")` returned `({}, {})`. `log.follow=true`, `diff.renames=copies` and `log.diffMerges=first-parent` left the result unchanged. Each of the four merge cases of `Test_main` was run with `test_settle.settle` replaced by the reader at `2c4023db8` and then at HEAD: the `AA` and deletion cases failed at `2c4023db8` and passed at HEAD, and the `AM` and `MM` cases passed at both. The file was removed before hand-back |
| `git -c <key> log -z --full-history --topo-order --reverse --no-renames --name-status --cc --format=%x01%h%x20%cs HEAD -- adr` in a scratch repository under the round's scratch directory, for `log.showRoot` true and false, `color.ui=always` and `color.diff=always`, and again with `--root` under `log.showRoot=false` | `log.showRoot=false` dropped the root commit's `A adr/0001.md`, and `--root` brought it back. Neither colour key changed a byte |
| The same command with `-c log.showSignature=true` after an ssh-signed commit (`gpg.format=ssh`, a key made by `ssh-keygen` in the scratch repository), then with `--no-show-signature` | Without the flag, `No signature` and a newline came before the signed commit's header field. With it, the header stood alone. The scratch repository and key were removed before hand-back |
