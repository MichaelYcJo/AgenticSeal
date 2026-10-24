# 1792619407-the-replay-scaffold-and-reader-misread-rounds — review round 1

target: 8ef3a12c against release/v0.22.3

## Findings

### 1. The S10 case fails on Windows because it hands a native Windows path to the scaffold as an unquoted shell word

severity: must
location: `tests/test_a_rewritten_definition_proved_non_inferior.py:2514`
evidence: read `tests/test_a_rewritten_definition_proved_non_inferior.py:2501-2520`, `evals/scripts/replay_targets.py:663-707`, `evals/scripts/seed_defects.py:276-297`
verdict: fixed 0cc8be41

The orchestrator relayed `tests` run 39688600936 at 8ef3a12c. The run failed one case on one Windows split:
`test_the_seeded_scaffold_leaves_round_1s_tree_and_no_copy_of_it`. Its stderr reads
`fatal: 'C:UsersrunneradminAppDataLocalTemp...shipped' does not appear to be a git repository`, exit 128. A
ready pull request fails on a red leg, so this blocks the merge.

The defect is in the case, not in the generator. The case passes `str(repo)` as the remote URL at line 2514.
`replay_targets.py#scaffold` writes that URL into `git remote add origin {url}` without quoting it, and `sh`
removes each backslash of an unquoted word, so the Windows path arrives without its separators. The generator
never writes a backslash there. `seed_defects.py` takes its URL from `replay_targets.py#origin_url`, which
returns `https://github.com/<owner>/<repo>.git` or stops the run with SystemExit. So every committed scaffold
carries the https URL, and a real user on Windows who runs a case does not meet this defect. Only this case
gives the generator a path that no real call gives it.

The fix gives the case a URL, the shape the real input has. `Path.as_uri()` gives `file:///C:/...` on Windows
and `file:///...` elsewhere, and `sh` leaves it unchanged. The fixture already sets `uploadpack.allowAnySHA1InWant`,
which a fetch by SHA over `file://` needs. Whether git for Windows fetches a SHA from that URL has not been run
here; the next Windows leg answers that.

```python
    (clone / "scaffold.sh").write_text(
        # A URL, as `replay_targets.py#origin_url` gives the generator: a
        # native Windows path in an unquoted `sh` word loses its backslashes.
        "set -eu\n" + sd.scaffold(t, repo.as_uri()) + "\n",
        encoding="utf-8",
    )
```

answer: The case now passes `repo.as_uri()`, the shape `origin_url` gives the generator, with a comment saying why. On macOS the module ran 122 passed (executed). Whether git for Windows fetches a SHA over `file:///C:/...` is unverified here; the orchestrator's next Windows leg answers it.

### 2. Findings after an unclosed comment vanish from the false count while the check refuses the record

severity: should
location: `evals/scripts/noninferiority.py:263-283`, `tests/test_a_rewritten_definition_proved_non_inferior.py:1077`
evidence: executed `python3 test_tmp_986_probe.py`
verdict: fixed 0cc8be41

Scope item 1 of `spec.md` says that a section the check would refuse is still one row, "so a finding written in
a broken shape counts as false instead of vanishing". Plan row R2 rejects a reader that lets a warden lower its own
false-finding rate with a broken record. `finding_rows` still does that for one shape. It splits the lines
`reader.readable` leaves (`noninferiority.py:274`), and `readable` blanks an HTML comment that never closes to
the end of the file. Every finding after the opener is gone from the split. The check knows this.
`chain_check.py#unclosed` (`skills/code-review/scripts/chain_check.py:1127`) refuses such a record because "every
`### ` heading and `verdict:` line after it would vanish". `record_findings` puts that refusal first.
`finding_rows` calls `finding_spans` directly and never consults `unclosed`.

The probe wrote a record of three findings and opened a comment in finding 1's prose without closing it.
`finding_rows` gave 1 row. The check read 0 findings and refused the record, first with the refusal that the
comment opened at its line never closes. Two findings left the false count of a record the check refuses. With every region closed,
the same record gave 3 rows, which matches the check's 3 findings.

The fix fails closed where the check does. Where `unclosed` refuses the text, the split reads the raw lines, so a
hidden `### ` section is still a row. A fenced `### ` line in such a record then adds a row. That is more false
rows, which is the direction a refused record should take. A case beside S2 pins it: three findings, the first
opening a comment that never closes, give three rows.

```python
    check, reader = rt.record_reader()
    # A region nobody closed hides every finding after it from `readable`,
    # and the check refuses the record for it (`chain_check.py#unclosed`).
    # Such a record is split on its raw lines, so a hidden finding still
    # counts as a false row instead of vanishing.
    if check.unclosed(reader, text, ""):
        lines = reader.gfm_lines(text)
    else:
        lines = reader.readable(text)
```

answer: `finding_rows` splits the raw lines where `chain_check.py#unclosed` refuses the text, as the fix block gives. `test_a_comment_that_never_closes_hides_no_finding_from_the_false_count` stands beside S2: three findings, the first opening a comment that never closes, give three rows and three false. `mutation-check` with the branch made `if False:` went red (executed).

### 3. The mask leaves a user path the scan refuses once the side's JSON escapes the character after it

severity: should
location: `evals/scripts/noninferiority.py:238-260`, `tests/test_a_rewritten_definition_proved_non_inferior.py:1614`
evidence: executed `python3 test_tmp_986_probe.py`
verdict: fixed 0cc8be41

`masked` runs the scan's functions on each line of the plain text. The committed side holds the text as one JSON
string, and the scan reads that JSON line. `phase-1.md` found that difference for hosts, and
`noninferiority.py:259` adds a space after a control character for them. User paths have the same gap, and the fix
does not cover them. `USER_PATH_RE` (`tests/test_no_real_identifiers.py:43`) matches `/Users/` followed by one
or more characters that are not whitespace, a quote, a backtick, a parenthesis or a slash. A backslash is allowed.
JSON writes a quote, a backslash and each control character with a backslash in front.

The probe masked each text and then scanned the side line by line, as the test at line 1614 does. Two texts
produced a refusal in the written side. A user root at the end of a line became the root followed by the escaped line break and the next word. A quoted user root
became the root followed by an escaped quote. Neither text is masked, because on the plain line the scan finds nothing to replace. The second
shape is the one a warden writes when it quotes this branch's own test line 404, `"/Users/" + "someone/"`, in a
fix block. The committed side would then fail `test_no_user_paths`, and the orchestrator would have to edit a side
by hand. Q4 was answered to avoid exactly that. The six other edge texts the probe wrote (a host after a tab, CR or
line break, the fixture path with and without its slash) scanned clean.

The fix closes the gap the way line 259 closes it for hosts. A space goes after `/Users/` where JSON would escape
the next character, and a case adds both texts to the masked-record test. The pattern below restates the scan's
`/Users/` prefix. A version that avoids that copy would scan each line's JSON form with `refused_user_paths`.

```python
    # A user path the scan sees only in the side's JSON: `/Users/` followed by
    # a character JSON writes as an escape, whose backslash the scan's class
    # takes as the user name. RESTATES the prefix of the scan's USER_PATH_RE.
    escaped = re.compile(r"(?<=/Users/)(?=[\"\\\x00-\x1f])")
    return escaped.sub(" ", glued.sub(" ", "\n".join(lines)))
```

answer: Built as the version the finding names without the copy. `noninferiority.py#apart` reads the text's JSON form, the one `write_side` writes, with the scan's own `refused_domains` and `refused_user_paths`, and sets one space beside an escape a refused match takes in: after it where the match starts inside the escape, before it where the match runs into it. It replaces the host-only pattern at line 259, so hosts and user paths take one path and no pattern is restated. The masked-record case adds the user root before a line break and inside quotes, and the written side scans clean (executed). Five mutations went red: `apart` not called, each of its two placements forced, user paths left out of the JSON-form scan, and its loop bound (executed). cdfd5f95 bounds that loop at the text's length, because a placement that fails to clear a refusal would otherwise loop for ever.

### 4. The seeded commit is the one commit with committer eval and today's date, which points a warden at the seed

severity: should
location: `evals/scripts/seed_defects.py:292`, `evals/behaviour/warden/seeded-279a580b/scaffold.sh:18`, `evals/behaviour/warden/seeded-ad447367/scaffold.sh:18`, `evals/behaviour/warden/seeded-8a100e13/scaffold.sh:18`, `evals/behaviour/warden/seeded-f1c9932d/scaffold.sh:18`, `tests/test_a_rewritten_definition_proved_non_inferior.py:2501`
evidence: executed `sh evals/behaviour/warden/seeded-279a580b/scaffold.sh`, `git log -3 --format=%h%x20%cn%x20%ce%x20%cd`
verdict: fixed 0cc8be41

The scaffold amends the seed into the target commit as `-c user.name=eval -c user.email=eval@example.com`, so git
records the amended commit with committer `eval <eval@example.com>` and the date of the run. In each of the four
clones, `git log -3` shows HEAD with committer eval and the date of this round. Every commit before HEAD has the
real committer and its original date. The old scaffold had the same line, but its tree was one commit on its
parent, so the mark told a warden nothing new. The new tree is a whole branch, and the mark names the one commit
that holds the seed. Q5 says this commit otherwise touches only records. So `git log --format=fuller`, or any log
that shows committers, leads straight to the diff the seed is in. Q5 asks the owner about the `HEAD^` diff. This
finding is a separate signal, and it costs nothing to remove.

The fix keeps the committer the original commit had. `--amend` already keeps the author. The committer's
email is already in every other commit object in the clone, so the change exposes nothing new. The S10 case then
asserts that HEAD's committer and committer date equal the fixture target's.

```python
            # The amended commit keeps the original's committer and date, so
            # no field of the log marks the commit the seed was amended into.
            'GIT_COMMITTER_NAME="$(git log -1 --format=%cn)" '
            'GIT_COMMITTER_EMAIL="$(git log -1 --format=%ce)" '
            'GIT_COMMITTER_DATE="$(git log -1 --format=%cI)" '
            "git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify",
```

answer: The amend sets the committer's name, email and date from the target commit, as the fix block gives. On the orchestrator's direction from the Not judged row, the scaffold also runs `git remote remove origin` after the amend and writes the base ref round 1 names again, since removing the remote removes it. The overview carries that as its own divergence row. The replay scaffold keeps its remote and is unchanged (S12). The four seeded cases were regenerated. Each scaffold was run once over the network in an empty directory (executed). Each exited 0, HEAD's committer and date equal the original target's, `git remote` printed nothing, the refs were the branch and the one base ref, and every earlier S10 check still held. The fixture case asserts the committer, the empty remote list and the base ref. Four mutations went red: the date dropped, the name dropped, the remote kept, the base ref not written again (executed).

### 5. Three records say three of the four round 1 records name origin/release/v0.21.0, and two do

severity: should
location: `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/spec.md:113`, `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/overview.md:18`, `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/phases/phase-2.md:50-51`
evidence: executed `git show 279a580b:seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds/round-1.md`, `git show ad447367:seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds/round-1.md`, `git show 8a100e13:seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/rounds/round-1.md`, `git show f1c9932d:seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/rounds/round-1.md`
verdict: fixed 5020c9e8

`spec.md` scope item 5, the overview's base-ref row and `phase-2.md` each say that three of the four round 1
records name `origin/release/v0.21.0`. Read at each squash commit, two of them do: `279a580b` and `ad447367`, in
their asked paragraphs. `f1c9932d` reads `target: 56172bbe against release/v0.22.1`, which is also gone from the
remote. `8a100e13` reads `target: 4279671d against release/v0.22.2`, which still exists. So three of the four
name a ref the remote no longer has, but only two name v0.21.0. The sentence probably dates from the four cases
before two were replaced. A later reader who looks for a fourth v0.21.0 record will not find one. The value is
also written three times, which the owner's direction in `skills/writing-style/SKILL.md`
§*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* forbids. The fix states it once, in the spec, and the
other two records cite it.

```markdown
   Where round 1 names a base ref the remote no longer has, the squash commit's
   first parent stands for it (`replay_targets.py#ref_base`). Three of the four
   do: two name `origin/release/v0.21.0` and one `release/v0.22.1`.
```

answer: `overview.md`'s base-ref row and `phase-2.md` no longer state the count; each points at `spec.md` scope item 5 for which refs are gone. `spec.md` is the framer's file, and the smith's definition names no write to it. So `spec.md:113`'s last sentence, which still says three of the four name `origin/release/v0.21.0`, is the orchestrator's to replace with the fix block's three lines. Until then the one statement the other two records cite is the wrong one.

## Confirmations

confirms: none
The implementer's account says the reader counts what the check counts, so a fenced or commented `location:`
line is no row. Where every region closes, it does. The probe's three-finding record gave 3 rows, and the check
read 3 findings. `finding_rows` (`evals/scripts/noninferiority.py:263-283`) calls `finding_spans`, `label_of` and
`LOCATION_ROW` of the loaded check. The S1 to S5 cases (`tests/test_a_rewritten_definition_proved_non_inferior.py`)
pin a fenced line, a section with no `location:` line, a line outside every finding, a truth found only in a
fence, and the patched split. Read and executed.

confirms: none
The account says the scan's allow logic moved into `refused_domains` and `refused_user_paths` without a change in
behaviour. Read against the base, `tests/test_no_real_identifiers.py:64-93` has the same branches in the same order
as the inline loops `domains_in` and `user_paths_in` had at 5aed51cb, and the violation strings are the same.
`identifier_scan` drops only an `ImportFrom` of `conftest`. The module's other imports are `os` and `re`, so a run
without pytest loads it. Read.

confirms: none
The account says the scaffold leaves no ref, file or object naming the original target. I ran all four
regenerated scaffolds in empty directories, each with exit 0. Each clone holds two refs, the branch and one
`refs/remotes/origin/release/*` base ref, both in `packed-refs`. It has no tag, no stash, nothing in
`git fsck --unreachable --no-reflogs`, `cat-file -e` of the original target exits 128, and `grep -rl` of the target
under `.git` outside its objects exits 1. Executed. Findings 4 and the `## Not judged` rows below name what does
remain.

confirms: none
The account says `ref_base` lets the squash commit's first parent stand for a deleted base. For each of the four
cases, the base in the scaffold equals the parent of the first commit of `base..target`: 5623d728 twice, 769f2aa4
and f6ae6db6. So the merge-base gives the fork point that round 1's ref named. Executed.

confirms: none
The account says the two replacements follow Q3's rule, the next smallest commit `seed_defects.py --list` names
that builds. After the pull heads were fetched from the GitHub remote into the scratch clone, `--list` named
8a100e13 at 1334 lines and f1c9932d at 3485 lines as its two smallest buildable commits, ahead of 75502328 at 4515.
Executed. `evals/scripts/recurred_truths.json` holds no `seeded-` entry (executed `grep`).

confirms: none
The new tests were read against their groups. Each covers a reading no earlier case of
`tests/test_a_rewritten_definition_proved_non_inferior.py` did: the fence, the refused shape, the split, the kept
text, the two refusals, the mask, the round 1 target, the confirmed truths, a round with no successor, the shared
line and the scaffold run. No duplicate was found. Read.

Nothing was carried from an earlier round: this is round 1.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Each clone keeps `origin` at the GitHub URL with the default refspec. A warden's `git fetch origin` would bring back every head, and the release branches hold the shipped, unmutated code. The old scaffold kept the same remote. Whether that stands beside Q5 is a value for a person, and only Q1's paid run shows whether a warden fetches | `evals/scripts/replay_targets.py:699` | the repository owner, with `questions.md` Q5 |
| The generator reads round 1's target from local objects. In a clone without the pull heads, `--list` left f1c9932d and four others out as "target does not resolve", so `--case seeded-f1c9932d` cannot regenerate that case there. Whether the suite counts as generated from such a clone is not settled | `evals/scripts/seed_defects.py:340-396` | the orchestrator |
| A fence opened in one finding and closed by the next finding's opener hides one finding from both the check and the harness, and the check refuses nothing (probe: 2 rows, 2 findings, of 3). This is the check's own reader and outside this diff | `skills/verify/scripts/unverified_check.py:417` | the repository owner |
| Whether finding 1's `as_uri()` fix fetches a SHA under git for Windows | `tests/test_a_rewritten_definition_proved_non_inferior.py:2514` | the orchestrator, from the next Windows leg |
| The full suite, the repository-wide lint and the typecheck at 8ef3a12c, labelled `unverified` here | the branch | the orchestrator, at its one broad run |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_986_probe.py` in the scratch clone at 8ef3a12c | Exit 0. A: all regions closed gave 3 rows and 3 check findings. A misnested fence gave 2 rows and 2 findings with no refusal. A comment that never closed gave 1 row, 0 findings and the `unclosed` refusal. B: 11 of the 141 committed records differ between rows and visible headings, all of them `-report.md` records of the shape before #1000. C: `/Users/` at a line end and a quoted `"/Users/"` were refused in the written side. Six other texts scanned clean |
| `sh <case>/scaffold.sh` for the four seeded cases, each in an empty scratch directory | Exit 0 each. Then `for-each-ref`, `packed-refs`, `fsck --unreachable --no-reflogs`, `cat-file -e` of the original target (128 each), `grep -rl` of it under `.git` outside the objects (1 each), `config --get-regexp ^remote` and `log -3` with committer fields |
| `git fetch` of `refs/pull/*/head` from the GitHub remote into the scratch clone, then `python3 evals/scripts/seed_defects.py --list` | Exit 0. Before the fetch, f1c9932d was left out as "target 56172bbe does not resolve". After it, f1c9932d was listed at 3485 lines |
| `git rev-list --reverse <base>..<target>` and the parent of its first commit, for the four cases | The parent equals the scaffold's base in each case |
