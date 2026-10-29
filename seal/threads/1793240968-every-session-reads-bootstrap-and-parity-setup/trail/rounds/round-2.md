# Review round 2: 1793240968-every-session-reads-bootstrap-and-parity-setup

target: 53c50c81, fixes 25fe2900..53c50c81

## Findings

### 1. Under shared, records only, step 7 tells the person that nothing refuses a round record without an `original:` line, and `seal gate` refuses one once a ready pull request is open

severity: should
location: `skills/parity-setup/SKILL.md:59-72`, `tests/behaviour/test_chain_hooks_hardening.py:264-276`, `seal/threads/1793240968-every-session-reads-bootstrap-and-parity-setup/changelog.md:5`
evidence: executed `bin/test tests/skills/test_tmp_records_only_refuses_on_a_ready_pr.py -p no:xdist -q`
verdict: open
regression: round-1#1

The unit is step 7 of `skills/parity-setup/SKILL.md`, at `:69-72`: "In local
mode, and under shared, records only, no pull-request check reads a round
record or a guarantee: say that the `original:` line is still written, and
that nothing refuses a record without it." The frame's phase 1 row in
`frame/plan.md` and `frame/design.md` *Scope* item 1 send the bootstrap's yes
to this procedure and say nothing of step 7. The fix pass added the
records-only clause to answer round 1's `## Not judged` row, and it came from
the answer's premise that "`seal gate` runs `chain_check.py` before any pull
request exists".

That premise holds only for the gate's first run. `chain_check.py` asks
`gh pr view --json isDraft` wherever no event payload exists
(`skills/code-review/scripts/chain_check.py:769-793`). It judges strictly any
state other than a draft that it saw (`:2235`), and a round record with
no `original:` line is a problem at `--sealing` too, since only the
guarantee's line is spared (`:2327-2335`). Nothing in that path reads `.github/`. So
under shared, records only, the broad gate refuses the record whenever a
ready pull request is open for the branch. That happens when the gate runs
again after the pull request has opened, and when a person opens the pull
request before the gate runs. The probe planted the module's migrating
branch with no `.github/` directory, no event payload, and the suite's `gh`
stub on PATH. With `gh` answering ready, the `--sealing` run exited 1 and
named both round records. With no pull request it exited 0 and named the
same two records.

The orchestrator reads step 7 and says it to the person, so the person is
told that no check enforces the line under the default mode. The test
comment at `tests/behaviour/test_chain_hooks_hardening.py:264-267` states
the same premise ("only installed pull-request checks refuse a record"). The
assertion at `:276` pins the sentence that carries it. `changelog.md:5`
repeats it for the release notes. Local mode is unaffected:
`read_record` reads `seal/parity.md` through `git show HEAD:` (`:736-747`,
`:1826`). A local root is not in git, so `originals_of` returns nothing there.

```markdown
   (`skills/legacy-parity/SKILL.md` *Recording the comparison*). Under
   shared, records only, no workflow reads a round record, but `seal gate`
   runs the same check: say that the `original:` line is still written, that
   the gate refuses a round record without it once a ready pull request is
   open for the branch, and that before then it names the record and passes.
   In local mode git carries neither `seal/parity.md` nor a round record, so
   no check reads either: say that the line is still written, and that
   nothing refuses a record without it.
```

```python
    # The bootstrap's yes reaches the procedure right after the mode answer,
    # local included (#1046, rounds 1 and 2). Local mode commits nothing and
    # no check reads it; under shared, records only, `seal gate` still refuses
    # a round record with no `original:` line once a ready pull request is open.
    procedure = " ".join(open(setup, encoding="utf-8").read().split())
    assert "Where the root is `<repo>/seal/`, commit it." in procedure, (
        "the parity-setup procedure commits the declaration in every mode"
    )
    assert "In local mode the root sits under the common git directory" in procedure
    assert "`seal pr-checks` reports the checks installed" in procedure, (
        "the parity-setup procedure promises a pull-request refusal that "
        "only installed checks give"
    )
    assert "the gate refuses a round record without it once a ready pull" in procedure, (
        "the parity-setup procedure says nothing refuses under shared, records "
        "only, where `seal gate` refuses once a ready pull request is open"
    )
    assert "In local mode git carries neither" in procedure
```

The fragment's sentence at `changelog.md:5` becomes: "In local mode it says
that the line is still written and that nothing refuses a record without it.
Under shared, records only, it says that `seal gate` refuses a round record
without the line once a ready pull request is open."

answer:

## Confirmations

confirms: round-1#1
The local-mode half of the close holds. Step 6 commits `seal/parity.md` only
where the root is `<repo>/seal/`, and in local mode it writes the file under
the common git directory and commits nothing (`skills/parity-setup/SKILL.md:49-57`).
That matches `skills/implement/bootstrap.md:80-87`. Step 7 no longer promises
a refusal in local mode, and that is true. `chain_check.py` reads the
migration config through `git show HEAD:` (`skills/code-review/scripts/chain_check.py:736-747`,
`:1826`), and it drops every declaration where HEAD has no top-level `seal`
entry (`:2229-2230`) (read). `skills/legacy-parity/SKILL.md:28-34` now says
the same about committing. Finding 1 above is a separate defect, which the
fix's records-only clause introduced.

confirms: none
The four new assertions pin text that was absent before the fix (contract
rule 15). Each phrase, searched in the whitespace-folded
`25fe2900:skills/parity-setup/SKILL.md`, matched zero times, so each
assertion fails against the old text. The fix pass claimed it saw them red
first, and this round did not re-run that red. At `53c50c81`,
`bin/test tests/behaviour/test_chain_hooks_hardening.py -q` exited 0 with 30
passed (executed).

confirms: none
`seal pr-checks` reports the plugin's workflow with the word `installed`
(`skills/implement/scripts/seal.py:2280-2285`), so the condition in step 7 at
`skills/parity-setup/SKILL.md:63-64` names output a person can read (read).
A workflow that pins a release older than the parity rule reads no
line of that kind, and `seal pr-checks` still reports `installed`. `docs/the-review-and-parity-arms.md:143-147`
already states that as a cost, so this round raises no finding on it.

confirms: none
The fix pass named `README.md:252` for a reviewer to judge: "Your checkout
path stays out of the committed file". Its Korean twin is `README.ko.md:246`.
This round raises no finding on either (read). The instruction they carry,
that the checkout path stays out of `seal/parity.md` and lives in
`~/.claude/agentic/parity-paths.md`, holds in every mode. "Committed" is true
of the default mode and of the other shared mode. No person or agent does
anything different because of it. The sentence that round 1 named was
different: step 6 told the session to commit, and step 7 told the person
what a check would refuse. Both are rewritten (read,
`skills/parity-setup/SKILL.md:49-72`).

confirms: none
This round re-established nothing outside the fix diff. It carried round 1's
facts without re-deriving them: the byte-for-byte move, the word counts, and
the nine modules passing at `904078cf`. `git diff 25fe2900..53c50c81` touches
`skills/parity-setup/SKILL.md`, `skills/legacy-parity/SKILL.md`,
`tests/behaviour/test_chain_hooks_hardening.py`, `changelog.md` and
`trail/rounds/round-1.md`, and no other file (executed).
`trail/rounds/round-1.md` changes only its `verdict:` and `answer:` lines.
`seal/parity.md` is not declared in this repository, so this record names
no baseline commit of an original.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch; `gaps.md` labels them `unverified`, the label is honest, and this round ran none of them | the branch at `53c50c81` | the orchestrator, at `seal gate --record` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_records_only_refuses_on_a_ready_pr.py -p no:xdist -q`, one file in a `git clone --no-local` at `53c50c81`, importing `test_chain_check.py`'s `branch`, `migrating` and `check`: no `.github/`, `GITHUB_EVENT_PATH` unset, PATH from `conftest.gh_answers` for `ready` and for `unknown`, then `check(root, capsys, "--sealing")` | exit 0, 2 passed: with `ready`, chain-check exited 1 and named both round records; with `unknown`, it exited 0 and named the same two |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py -q` in the same clone | exit 0, 30 passed |
| `git show 25fe2900:skills/parity-setup/SKILL.md`, whitespace folded, searched with `grep -c -F` for each of the four new assertion phrases | 0 matches for each |
| `git diff --stat 25fe2900..53c50c81` | five files, as `## Confirmations` lists |
