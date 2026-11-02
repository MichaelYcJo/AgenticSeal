# Review round 4: 1793573496-the-settle-folds-named-directories-the-person-marks

```seal
target: 1ec48bd77, fixes 9a5751664..1ec48bd77
```

This verifying round read the diff `9a5751664..1ec48bd77` in the branch's own
worktree. That diff holds the fix pass's commit (`68b7f1970`), its close
blocks on round 3 (`fa514feed`) and the orchestrator's fold into
`frame/design.md:99` (`1ec48bd77`). Carried from rounds 1 to 3 as
coordinates, not re-established: where the listing lives
(`settle.py#history`, `#changed`, `#documents`), the four merge cases of
`Test_main`, round 3's reading of git's status letters, and round 3's list of
the `log.` and `diff.` keys. No `seal/parity.md` is declared, so the round
block holds no `original:` line. `seal/config.md` holds no `Record language`
row, so the record is English. The orchestrator's judgment row
(`frame/plan.md:54`) makes this the run's last round and sends the same
exposure in the base's readers to #1283; this round stayed inside the fix
diff and reports what it found there at the severity it found it.

The fix pass's account was read as a claim and checked against the code.
It claimed both new cases were seen red at `9a5751664`'s reader. This round
wrapped `settle.git_fields` to drop `--root` and `--no-show-signature` and ran
both cases through the wrapper: each failed on its listing line, executed.
That wrap is the same mutation the account's `seal mutate` run made, so the
mutation claim was re-run in this form and not as `seal mutate`. It claimed
the texts now say a merge whose result differs from every parent is a
change; `settle.py:906-909`, `settle.py:65-66`, `SKILL.md:221-223` and the
changelog do, read. It claimed the proposed clean-merge case covers nothing
its group does not. That holds for the reader's code and does not hold for
the claim the texts now make (finding 1).

## Findings

### 1. The texts still list how a merge comes to differ from every parent, the list misses a merge edited in the merge, and no case pins the clean-merge claim

```seal
severity: should
location: `skills/settle/scripts/settle.py:906-909`, `skills/settle/scripts/settle.py:64-66`, `skills/settle/SKILL.md:221-223`, `seal/threads/1793573496-the-settle-folds-named-directories-the-person-marks/changelog.md:3`, `tests/skills/test_settle.py:1999`
evidence: executed `bin/test tests/skills/test_tmp_round4_1054.py -q -s -p no:xdist (test_tmp_merge_shapes: git merge --no-ff --no-commit of side, adr/0001.md, which only side touched, edited at line 10 in the merge, and adr/0002.md edited by side at line 25 and by main at line 2)`
reopens: round-3#1
```

The close does not hold, for two reasons. `68b7f1970` removed the false
sentence "a clean merge names nothing". It replaced it with a closed list of
three ways a merge's result can differ from every parent, and a fourth way is
left out. And the close declined the case on grounds about the reader, while
the claim the texts now make rests on git's output.

Why it matters, first part. `history`'s docstring defines the named merge by
a colon and a list: "a merge that resolved a conflict in it, wrote it new, or
combined two parents' edits to it with no conflict" (`settle.py:906-909`).
The skill tells the settling session that a merge changed a file "by a
conflict it resolved or by two parents' edits it combined"
(`SKILL.md:221-223`). The module docstring (`settle.py:64-66`) and the
changelog say the same. A merge can also be edited in the merge itself:
`git merge --no-commit`, an edit, then the commit, which is how a merge
commit commonly fixes a build. The probe did this to `adr/0001.md`, which
only `side` had touched. `git log --cc --name-status` printed `MM
adr/0001.md` at the merge, and `history` gave the merge as the document's
last change, executed. That listing is right. The skill then tells the
session that a conflict was resolved or two edits were combined there, and
neither happened.

How the class was listed (contract rule 12), by taking the result apart.
At a path that a merge's result holds, each hunk of the result either
matches some parent's version or matches none. The result differs from every
parent in three cases. Some hunk matches no parent: a conflict it resolved or
an edit made in the merge, which git cannot tell apart. The hunks match
different parents: two parents' edits combined. No parent holds the path:
written new. The list in the texts names three of these four, and the one it
misses is the hand edit. So the fix is to state the rule and give the shapes
as examples, not to add a fourth item to a closed list.

Why it matters, second part. The decline said the clean-merge case reaches
the `MM` branch that `test_a_merge_that_resolved_a_document_is_its_last_change`
already drives. For the reader that is true. But the three texts now claim
that git names a clean merge of two edits, and the conflict case does not
test that claim. git's dense combined diff (`--cc`) calls a hunk
uninteresting where the result takes one parent's version, and a clean
merge of two edits has only such hunks. `git-diff-tree(1)` says of `--cc`:
"When all hunks are uninteresting, the commit itself and the commit log
message is not shown". The probe built that shape in `adr/0002.md`. `git log
-1 --cc -p -- adr/0002.md` printed the merge's header and no diff. `git log
-1 --cc --name-status` printed `MM adr/0002.md`, and `history` gave the merge
as the last change, executed. So the listing stands on `--name-status` not
applying the dense filter. The conflict case's resolved hunk is interesting,
so that case cannot catch a git, or a later reader, that drops a merge whose
hunks are all uninteresting. Only the clean-merge case does. It covers what
its group does not, and `skills/code-review/SKILL.md` *A finding is not
closed too early* says a claim a fix writes into a document closes when a
test pins it.

Not a `must`: what the listing prints is right for every shape the probe
built. The sentences and a missing case are wrong.

The docstring at `settle.py:906-909`:

```python
    parent holds it, and this commit does not). A merge is named at a path
    only where its result there differs from every parent, however it came
    to differ: a conflict it resolved, an edit made in the merge, two
    parents' edits it combined with no conflict, or a file it wrote new. A
    merge whose result at the path is one parent's names nothing. The
    letters of one status are either all `D` or all from `A`, `M` and `T`.
```

The module docstring (`settle.py:64-66`), the skill's bullet
(`SKILL.md:221-223`) and the changelog's sentence say, in their own words,
"one whose result at it differs from every parent, however it came to (a
conflict it resolved, an edit made in the merge, or two parents' edits it
combined), changed it". The case is round 3's, unchanged, beside
`test_a_merge_that_resolved_a_document_is_its_last_change`
(`tests/skills/test_settle.py:1999`). This round did not run it as a case;
the probe ran its shape through `history`, executed:

```python
    def test_a_clean_merge_of_two_edits_is_a_documents_last_change(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 4's finding 1: a merge with no conflict that combines
        two branches' edits to one document holds content neither parent
        holds. Its hunks are all ones `--cc` calls uninteresting, and
        `--name-status` still names it `MM`, so it is the last change."""
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

The case passes against the current reader. It goes red under a reader that
reads the merge's hunks the way `--cc -p` does, and it is the one case that
pins the sentence the texts now state.

### 2. The signed-commit case errors instead of skipping where the person's git config names another ssh signing program

```seal
severity: should
location: `tests/skills/test_settle.py:2133-2147`
evidence: executed `bin/test tests/skills/test_tmp_round4_1054.py -q -s -p no:xdist (test_tmp_signed_case_under_another_signing_program: the case run under GIT_CONFIG_GLOBAL holding gpg.ssh.program=/usr/bin/false)`, `bin/test tests/skills/test_tmp_round4b_1054.py -q -s -p no:xdist (the case's body with gpg.ssh.program=ssh-keygen set in the repository, under the same GIT_CONFIG_GLOBAL)`
regression: round-3#2
```

The unit is `test_a_signed_commit_is_read_under_any_show_signature`
(`tests/skills/test_settle.py:2125`), which `68b7f1970` added. The frame
(`frame/design.md:99`) names `--no-show-signature` so that a user's log
configuration does not change what the reader prints, and the fix built a
case that signs with an ssh key and skips where `ssh-keygen` is missing; the
defect came from setting `gpg.format` and `user.signingkey` in the
repository and leaving `gpg.ssh.program` to whatever level of the person's
configuration names one, so the skip checks one program while git signs with
another.

Why it matters: the case asks `shutil.which("ssh-keygen")` whether it can
run (`test_settle.py:2133`), then signs with `git commit -S`
(`test_settle.py:2147`). git signs with the program `gpg.ssh.program` names,
from the system, global or repository level, and only its default is
`ssh-keygen`. A contributor whose global configuration signs through another
program, such as a password manager's ssh signer, gets an error from this
case, not a skip. The probe ran the case under a global configuration whose
`gpg.ssh.program` was `/usr/bin/false`, standing in for such a program. The
commit failed with `fatal: failed to write commit object`, and the case
raised `CalledProcessError`, executed. The same body with `gpg.ssh.program`
set to `ssh-keygen` in the repository passed under that configuration,
executed.

How the class was listed (contract rule 12), by taking apart what `git
commit -S` with `gpg.format=ssh` needs: a git that knows the ssh format (2.34
or later), a signing program that `gpg.ssh.program` names, that program
supporting `-Y sign`, and a key it can read. The skip covers none of these
exactly. It checks that some `ssh-keygen` is on Python's `PATH`. The program
is the one this finding fixes. A git older than 2.34, or an `ssh-keygen`
without `-Y sign`, also errors and does not skip. That part is not fixed by
the line below. Whether to skip on a failed signing commit, with git's
message, is the fix pass's call. Such a skip would also hide a broken
signing setup in CI.

Not a `must`: CI's runners carry no such configuration, and the case is
right wherever git signs with `ssh-keygen`.

Beside `test_settle.py:2142-2143`:

```python
        git(repo, "config", "gpg.format", "ssh")
        git(repo, "config", "gpg.ssh.program", "ssh-keygen")
        git(repo, "config", "user.signingkey", str(key))
```

Precondition: the bare name `ssh-keygen` is resolved on git's own `PATH`, as
git's default is. On Windows, Git for Windows resolves its bundled copy,
which may not be the one `shutil.which` found. That was not run here.

## Confirmations

```seal
confirms: round-3#2
```
What holds: `history`'s `git log` carries `--root` and `--no-show-signature`
(`settle.py:924`), and its docstring says what each keeps
(`settle.py:895-898`), read. Each new case failed with the two flags taken
out by a wrapper on `settle.git_fields`. The show-root case printed no
`docs/a.md` line with the root commit. The signature case printed no
`adr/0001.md` line with the signed commit. Both passed at HEAD, executed.
The module docstring, the skill's bullet, the changelog and the design's
fold (`frame/design.md:99`) each name the two keys, read. The readers in the
base that share the exposure are #1283 by the orchestrator's row
(`frame/plan.md:54`), read, and were not reviewed here. Round 3's
`Not judged` row on a GPG-signed commit is answered by the flag, read:
`git-log(1)` says `--no-show-signature` overrides `log.showSignature`, with
no condition on the signing format. This was not run with a GPG signature.

```seal
confirms: none
```
What matched: each new case covers what its group did not. No case of
`Test_main` sets a `log.` key before this diff, read. Both cases set the key
through `GIT_CONFIG_COUNT=1` (`test_settle.py:2117`, `:2149`). That replaces,
for the rest of the case, the suite's `maintenance.auto=false`
(`tests/conftest.py:338-340`), which keeps a detached `git maintenance` from
racing a copied repository. Neither case commits after setting it, so no
maintenance starts, read; this is no finding. A later edit that commits
after the `setenv` would bring that race back.

```seal
confirms: none
```
What matched: the narrow runs passed, executed. `bin/test
tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py
tests/behaviour/test_a_reference_root_is_read_and_never_taken.py
tests/behaviour/test_docs_line_wrap.py
tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py
tests/behaviour/test_settle_applies_rule_changes_in_place.py -q` exited 0
with 226 passed and 8 skipped. `bin/test tests/skills/test_settle.py -q -rs
-k "show_root or show_signature" -p no:xdist` ran both new cases with no
skip, on this machine's `ssh-keygen` (OpenSSH 10.2) and git 2.50.1.
`uvx ruff check` and `uvx ruff format --check` on `settle.py` and
`test_settle.py` exited 0. These are narrow runs, not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the lint and the format check at HEAD. This round ran six modules, and the suite is labelled `unverified` | the repository's `Broad gate` row | the orchestrator, by `seal gate --base origin/release/v0.28.0 --record <item>`, then the sealer |
| The Windows and Linux legs at 1ec48bd77, among them whether the signature case signs on `windows-latest` with the `ssh-keygen` git resolves | run 41366101808 of `gh workflow run tests` | the orchestrator, which dispatched it and reads it before the broad run |
| Configuration keys outside `log.` and `diff.` that reshape `git log` output, carried from round 3 and not answered by the orchestrator's row | `skills/settle/scripts/settle.py:922-926` | the orchestrator, judging whether round 3's list is enough |
| Round 1's rows for design A7, and for Windows and case-insensitive paths, carried as they stand | `trail/rounds/round-1.md` *Not judged* | the answerers round 1 names |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round4_1054.py -q -s -p no:xdist`, one file in the worktree's `tests/skills/` importing `test_settle` | With `settle.git_fields` wrapped to drop `--root` and `--no-show-signature`, both new cases raised `AssertionError` on their listing line. Under a global configuration with `gpg.ssh.program=/usr/bin/false`, the signature case raised `CalledProcessError` from `commit -q -S`, `fatal: failed to write commit object`. A merge of `side` made with `--no-commit`, with `adr/0001.md` (touched only by `side`) edited in the merge and `adr/0002.md` edited by both sides at lines 2 and 25: `--cc --name-status` printed `MM` for both, `--cc -p -- adr/0002.md` printed the header and no diff, and `history` gave the merge as both documents' last change. 4 passed |
| `bin/test tests/skills/test_tmp_round4b_1054.py -q -s -p no:xdist` | The signature case's body with `gpg.ssh.program` set to `ssh-keygen` in the repository, under the same global configuration, passed |

Both probe files and their bytecode under `tests/skills/__pycache__/` were
removed before hand-back, and `git status` in the worktree showed nothing
else.
