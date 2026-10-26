# Review round 2: 1793051803-settle-runs-in-local-mode

target: 137d0a9c, fixes 12bd3195..137d0a9c

This is a verifying round. It read the fix range `12bd3195..137d0a9c` and, as
the caller asked, the whole diff `91d57028...137d0a9c` again, in a
`git clone --no-local` of the repository at `137d0a9c`. Carried from round 1
and not established again: where `released_local`, `merged_pull_requests`,
`records_of`, `survey` and `apply` sit in `skills/settle/scripts/settle.py`,
what the `gh` stub fixture of `tests/test_settle.py` answers, and that no
`seal/parity.md` is declared. Every verdict below was reached again on the
code at `137d0a9c`.

## Findings

### 1. The fix for round 1 finding 2 changed what shared mode does from a subdirectory, and no case pins that half

severity: should
location: `tests/test_settle.py:844-861`, `skills/settle/scripts/settle.py:893-897`
evidence: executed `bin/test tests/test_tmp_round2_probe.py -q -p no:xdist -s`, `grep -n -- '"--root"' tests/test_settle.py`
verdict: open
regression: round-1#2

The unit is the line `root = optin.repo_root(root) or root` in
`settle.py#main`, which 662dae5c added for both modes. The frame's phase 1
row in `plan.md` is verified by S1 to S10, each case seen red, and
`spec.md` *Out* keeps shared mode as #1033 left it; the fix changed shared
mode's answer from a subdirectory and pinned only the local half, because
round 1's finding named only the local case.

What was claimed: round 1's answer, the `overview.md` divergence row and the
changelog fragment's bullet each say a shared-mode run from a subdirectory
now reads the repository instead of refusing. The claim holds. The probe
built a shared repository with one released work item and ran the dry run
from the top and with `--root` at `docs/`. Both exited 0 with the same
output. `--apply` from `docs/`, on a copy, removed the released directory.

No case holds it. The grep shows every shared-mode `main` call in
`tests/test_settle.py` passing the repository's top. The one subdirectory
case, at line 854, runs the `local` fixture. So an edit that keeps the
refusal for shared mode passes the module. That edit is what `spec.md`
*Out* "Shared mode" literally asks for, so a reader of the frame has a
reason to make it. Contract rule 14 asks that a fix which changes what a
person sees pin it in the same commit. From a subdirectory a person used to
read "has no seal/specs/ at either place", and now reads the dry run, or
with `--apply` a removal. The changelog fragment states that change, and no
case stands behind it.

```python
    def test_a_shared_run_from_a_subdirectory_reads_the_repositorys_top(
        self, repo, gh, capfd
    ):
        """#955: `main` resolves the root to the repository's top in both
        modes, so a shared run from a subdirectory prints what a run from the
        top prints. It used to refuse, saying the repository had no
        seal/specs/ at either place, which was false there."""
        item(repo, "1700000001-a", [op("add", "S", new="Rule.")])
        commit(repo, "released a")
        top = dry_run(repo, capfd)
        code = settle.main(["--root", str(repo / "docs"), "--released-at", "main"])
        out = capfd.readouterr()
        assert (code, out.out + out.err) == top, out.out + out.err
        assert "at either place" not in out.err, out.err
        assert gh.calls() == [], gh.calls()
```

It stands in `Test_main` beside
`test_a_local_run_from_a_subdirectory_reads_the_repositorys_top`. Contract
rule 15: seen red with `optin.repo_root` answering "" (the case then exits 2
with the refusal).

answer: 6d4412ac adds `Test_main::test_a_shared_run_from_a_subdirectory_reads_the_repositorys_top` beside the local case, and `overview.md`'s divergence row names both cases. It is the round's case with two changes. `item` gets `op(...)` and not `[op(...)]`, because `spec()` puts its argument into `## Rule changes` as text, so a list would put the list's repr there. And the run from the top must exit 0 and place group 1 at `docs/a.md:3-9`, so the equality compares a real dry run. Before the commit, `mutation-check` over `settle.py` saw the case red under two mutants, and the held bytes were restored each time. The first keeps the refusal for shared mode only, resolving to the top only where the top has no `seal/`; the new case exits 2 with "has no seal/specs/ at either place", and the local case stays green. The second has `optin.repo_root` answering ""; both subdirectory cases fail.

## Confirmations

confirms: round-1#1
3093c521 holds. The limits paragraph of `skills/settle/SKILL.md:299-306`
names the fork match and says the one-issue flow does not rule it out. The
changelog fragment's `Limits` bullet (`changelog.md:9`) says the same. The
S10 case pins both phrases and asserts "never produces this" absent
(`tests/test_settle_reads_before_it_removes.py:320-327`). `git grep` for
"never produces" finds it only in round 1's record. Executed, with the
module run below.

confirms: round-1#2
662dae5c holds for the shape the finding named. A local run with `--root`
at a subdirectory reads `docs/a.md:3-9`, and with `optin.repo_root`
answering "" the case `tests/test_settle.py:844` fails (probe). The caller
asked whether applying the fix to shared mode holds against `spec.md`
*Out* "Shared mode". It holds. `--root`'s help already promised the
repository's root, "repository root (default: the one this is run in)"
(`settle.py:870`). The refusal shared mode gave from a subdirectory said the
repository has no root, which was false. `fold_check.py:389` resolves a
typed root the same way. Run from the top, shared mode is unchanged: the
probe's two outputs match, and every existing shared-mode case passes.
`overview.md` records it in its divergence table, which is where the frame
takes a divergence, so *Out* needs no rewrite. The missing pin is finding 1.
Executed for the probe and the module, read for the rest.

confirms: round-1#3
53972b46 holds. `merged_pull_requests` refuses a list holding an entry that
is not an object (`settle.py:238-239`), and keeps a null merge commit as
None (`settle.py:241-247`). `released_local` skips None in its search and
names it "#<n> with no merge commit" (`settle.py:301-307`). `NO_BRANCH`
names the reader (`settle.py:254-257`). The `entry` state
(`tests/test_settle.py:993`), the null case (`:1080`) and the unreadable
`Review` case (`:1131`) pass. `spec.md` *In* item 3 still lists "no
`routing.md` or no `Branch` row". That stands: the frame's item is
incomplete there, not false, and `overview.md` *Fed back into the spec*
carries the third reading. The `## Rule changes` `add` that will become
policy was rewritten by c78335ce. Its clause "whose `routing.md`
`hooks/routing.py` does not read" is awkward but not wrong, so it is no
finding. Executed, with the module run.

confirms: round-1#4
ef9048c7 and ef5e520c hold. The skill's *A settle is not a work item* says
git history keeps the removed specs only where the root is shared
(`SKILL.md:352-354`), pinned at
`tests/test_settle_reads_before_it_removes.py:177`. The new operation for
`docs/one-root-by-lifetime.md` *The dependency rule* parses, and the
shared-mode dry run places it in group 53 at `docs/one-root-by-lifetime.md:29-49`
with `from found, to not found`. Executed.

confirms: round-1#5
9cfb9820 holds. The *Where it reads* bullet names
`<git-common-dir>/seal/specs/<id>/` (`SKILL.md:257-261`), pinned at
`tests/test_settle_reads_before_it_removes.py:302`. `--released-at`'s help
makes the ref the subject (`settle.py:876-879`), pinned through `--help` in
`tests/test_settle.py:863`. Read, and executed with the module.

confirms: round-1#6
9f854538 holds. The two cases stand at `tests/test_settle.py:1052` and
`:1064`. The probe ran each under its mutant: with `reaches` replaced by
`rule_changes._ancestor` the first fails, and with `gh`'s list cut to its
first entry the second fails. Executed.

confirms: none
The frame sentences the smith named stand as the frame's record:
`spec.md` *Out* "A guard for a reused branch name", `plan.md` *Technical
context* last bullet and *Alternatives considered* (the chosen row and the
guard row), and `questions.md` A8. Each says what the one-issue flow
produces. A fork's branch is named by someone outside the flow, so the
sentence stays true of the flow. What was false was the skill's sentence,
which told a person the match cannot happen, and it changed. *In* item 11
changed with it because it specifies that sentence. *Out*'s "cannot
produce it" and item 11's "makes either match unlikely" do not contradict:
the first is about what the flow makes, the second about what a settle can
meet. The owner's direction they cite covers edge cases outside the normal
flow, and the fork match is one. Read.

confirms: none
The round 1 focus, walked again over the whole diff. No path found removes
an unshipped local work item. `apply` intersects the directories on disk
with `released` (`settle.py:830`). `released_local` calls a work item
released only on a merge commit that is not None and that the ref reaches
(`settle.py:301-312`). A `gh` that cannot be asked exits 2 before anything
is read. The new root line does not move the records root, which comes from
the common git directory (`records_of`, `settle.py:583-584`, compares real
paths). A `Branch` row reading `--repo=x/y` reaches the stub as the value of
`--head`, as one argument (probe); the real `gh`'s flag parsing of it was
not run. Shared mode never asks `gh`: only `survey`'s local branch calls
`released_local` (`settle.py:607-611`), and `test_shared_mode_never_asks_gh`
passes. Executed for the probe and the modules, read for the rest.

confirms: none
The touched modules and the censuses pass at `137d0a9c`: 530 passed over
the settle, rule-changes, stamp, census, line-wrap and pasted-passage
modules, and 185 passed with 8 skipped over the other modules that call
`settle`. The durations case passes, and `.test_durations` drops only the
two removed cases' entries. `test-layout --pairs` names no pair over the two
changed test files. `uvx ruff check` and `uvx ruff format --check` over the
three changed Python files report nothing. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The branch on Windows at `137d0a9c`. The dispatched `tests` run 40415159490 passed all four Windows groups at `12bd3195`. The fix range adds cases and puts `optin.repo_root` in front of every `main` call, and no run exists at the head | `skills/settle/scripts/settle.py:897`, `tests/test_settle.py:844-1150` | the orchestrator, from a `tests` run at the head, its four Windows groups |
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| A local-mode settle run end to end against a real local root and the real `gh`. Only fixture repositories with a stub have run it | `spec.md` *Out* | the owner, at the first local-mode settle |
| Q1's default, `gh` alone, against the hosts and merge methods the owner wants local mode to support | `questions.md` Q1 | the repository owner, at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_round2_probe.py -q -p no:xdist -s`, five cases over the `repo`, `local` and `gh` fixtures of `tests/test_settle.py` | 5 passed. Shared root, one released item: dry run from the top and from `docs/` both exit 0 with equal output; `--apply` from `docs/` on a copy removes the directory. With `optin.repo_root` answering "", the local subdirectory case fails. With `reaches` as `rule_changes._ancestor`, the equal-commit case fails. With `gh`'s list cut to one entry, the first-reached case fails. `Branch` row `--repo=x/y`: the stub logs `--head --repo=x/y`, exit 0, unreleased. File deleted |
| `bin/test tests/test_settle.py tests/test_rule_changes.py tests/test_settle_reads_before_it_removes.py tests/test_seal_stamp.py tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_censuses.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py -q` | exit 0, 530 passed |
| `bin/test tests/test_a_reference_root_is_read_and_never_taken.py tests/test_settle_applies_rule_changes_in_place.py tests/test_a_document_has_room_for_the_next_fold.py tests/test_routing.py tests/test_unverified_rows_close.py tests/test_chain_hooks_hardening.py tests/test_fold_check.py tests/test_a_document_that_names_a_script_says_how_to_reach_it.py -q` | exit 0, 185 passed, 8 skipped |
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` | exit 0, 1 passed |
| `bin/test-layout --pairs tests/test_settle.py tests/test_settle_reads_before_it_removes.py` | 2 files read, 0 pairs |
| `uvx ruff check` and `uvx ruff format --check` over `skills/settle/scripts/settle.py`, `tests/test_settle.py`, `tests/test_settle_reads_before_it_removes.py` | exit 0 each |
| `bin/settle --released-at HEAD` | exit 0; this spec's `add` at `spec.md:184` (`to not found`), its stamp `change` at `spec.md:206` and its dependency-rule `change` at `spec.md:212` (each `from found, to not found`) |
| `gh run list --branch feat/955-settle-runs-in-local-mode`, then `gh run view 40415159490` | one dispatched `tests` run, at `12bd3195`, every job a success; no pull request is open |
