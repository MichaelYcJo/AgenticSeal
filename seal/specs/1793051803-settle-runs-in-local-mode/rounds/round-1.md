# Review round 1: 1793051803-settle-runs-in-local-mode

target: 12bd3195 against release/v0.22.4

Round 1 has no earlier record, so nothing is carried. Every fact below was
established this round in a `git clone --no-local` of the repository at
`12bd3195`, against the fork point `91d57028`. No `seal/parity.md` is
declared, so no parity comparison applies.

## Findings

### 1. A merged pull request from a fork's branch of the same name reads an unshipped local work item as released, and the limit sentence says the flow never produces it

severity: should
location: `skills/settle/SKILL.md:294-300`, `skills/settle/scripts/settle.py:209-245`, `seal/specs/1793051803-settle-runs-in-local-mode/changelog.md:8`, `tests/test_settle_reads_before_it_removes.py:293-311`
evidence: executed `gh pr list --help`, `grep -n 'gh.merged(' tests/test_settle.py`
verdict: fixed 3093c521

`settle.py#merged_pull_requests` asks `gh pr list --head <branch> --state
merged`. The help text of `gh` says of `--head`: "Filter by head branch
("<owner>:<branch>" syntax not supported)". The filter matches the branch's
name and not the repository it lives in. So a pull request from a fork whose
branch carries the work item's branch name, once merged, makes the work item
read as released. Where its merge commit reaches `--released-at`,
`--apply` removes the work item's directory from the git directory, and no
commit holds it. That is the one irreversible act this change adds.

The skill's limits paragraph names the reused-name case only for "a later
work item" on the same branch. It then says "the one-issue flow cuts one
branch per issue, so it never produces this". That reason holds for the
branches the flow cuts. It does not hold for a branch an outside contributor
names in a fork, which the flow does not control. A person reading the limit
is told the shape cannot happen, which is wrong.

A guard is not the fix here. Comparing `headRepositoryOwner` with the base
repository's owner would read every pull request from a contributor's own
fork as unreleased, which breaks a local-mode repository that works through
a fork. The owner's standing direction for an edge outside the flow is a
limit sentence, so the sentence states the shape as it is.

```markdown
<!-- skills/settle/SKILL.md, the limits paragraph, replacing its last sentence -->
A branch name that a later work item reuses, after an earlier pull request
from it merged, reads that later work item as released. So does a merged
pull request from a fork whose branch has the same name, since
`gh pr list --head` matches a branch's name and not its owner. The one-issue
flow names each branch after its issue, which makes either match unlikely;
it does not rule out the second, because the flow does not name a fork's
branches.
```

The changelog fragment's `Limits` bullet takes the same clause. Contract
rule 14: `test_the_module_and_the_skill_both_say_how_local_mode_settles`
gains the new sentence among its pinned phrases.

answer: 3093c521 replaces the limit's last sentence in `skills/settle/SKILL.md` with the round's text, gives the changelog fragment's Limits bullet the fork clause, and pins both new phrases in `test_the_module_and_the_skill_both_say_how_local_mode_settles` with "never produces this" asserted absent; the pin was seen red against the old sentence, and a mutant naming a clone for the fork went red. No guard. `spec.md` *In* item 11 and *Out*, `plan.md` *Technical context* and `questions.md` A8 still say the flow cannot produce the shape; they are the frame's and stand for its owner.

### 2. Run from a subdirectory, local mode reads the policy root under that subdirectory and reports every document as not in the tree

severity: should
location: `skills/settle/scripts/settle.py:876-881`
evidence: executed `bin/test tests/test_tmp_round1_subdir.py -q -p no:xdist -s`
verdict: fixed 662dae5c

`settle.py#main` takes `root` from `--root`, or from the working directory,
and never resolves it to the repository's top. In shared mode a subdirectory
holds no `seal/` and the common git directory holds none either, so the run
refuses. In local mode `optin.py#home_at` finds `<git-common-dir>/seal/`
from any subdirectory, so the run goes on. Then the policy root,
`citations`' tracked files and `tests/` are all read under the subdirectory.

The probe ran the local fixture twice, once from the top and once with
`--root` at a subdirectory. From the top, the place line reads
`docs/a.md section S, at docs/a.md:3-9`, with `from found`. From the
subdirectory, it exits 0 and reads "the document is not in the tree in the
working tree", with `from not found` for a document that is there. The
settling session reads those facts to write each section. `--apply` from
the subdirectory removes the same directories, because the records root is
right, but it skips `fold-check`'s lines, since the policy root reads as
absent.

`fold_check.py:389` already resolves its root to the top through
`optin.repo_root`. The same line here closes the shape. It also changes
shared mode's answer from a subdirectory: today that answer is the refusal
"has no seal/specs/ at either place", which is false there. The fix pass
weighs that change against `spec.md` *Out* "Shared mode". Shared mode run
from the top is unchanged by it.

```python
    root = os.path.abspath(args.root or os.getcwd())
    # The root is resolved through the one resolver, `hooks/optin.py#home_at`,
    # handed the common git directory this also needs for the opt-out sentence.
    optin = load(OPTIN, "specseal_optin")
    # The repository's top, as `fold_check.py` resolves it: the policy root,
    # the tracked files and `tests/` are read from it, and a subdirectory holds
    # none of them. Precondition: `repo_root` answers with links resolved, or
    # "" outside a repository, where ROOT stays as given and the no-root
    # refusal below answers.
    root = optin.repo_root(root) or root
    common = optin.git_common_dir(root)
    home = optin.home_at(root, common)
```

The regression case belongs in `tests/test_settle.py` `Test_main`. It runs
the `local` fixture with `--root` at a subdirectory and asserts the place
line names `docs/a.md:3-9`.

answer: 662dae5c resolves `root` through `optin.repo_root` in `settle.py#main`, in both modes, and adds `Test_main::test_a_local_run_from_a_subdirectory_reads_the_repositorys_top`, seen red first with the place line "the document is not in the tree in the working tree", and red again under the mutant that drops the line. Shared mode run from a subdirectory now reads the repository instead of refusing with a false "no seal/specs/ at either place"; run from the top it is unchanged. `overview.md` records it as a divergence from *Out* "Shared mode", `phases/phase-1.md` names it, and the changelog fragment gains a bullet for it.

### 3. Two unreleased reasons tell the person something the input does not say

severity: should
location: `skills/settle/scripts/settle.py:239-250`, `skills/settle/scripts/settle.py:257-297`, `skills/settle/SKILL.md:264-267`, `tests/test_settle.py:1016-1024`, `tests/test_settle.py:1043-1061`
evidence: executed `bin/test tests/test_tmp_round1_probe.py -q -p no:xdist -s`
verdict: fixed 53972b46

The smith reported one reading the frame does not cover: a `routing.md`
whose `Review` row `hooks/routing.py#parse` cannot read parses to nothing,
so the work item reads as naming no branch. The direction is right. Every
reader of `routing.parse` treats a file it does not read as no declaration,
and this one leaves the work item untouched. The words are wrong, though.
The probe gave a `routing.md` a capitalised `Review` answer, "Through the
review chain", and a `Branch` row of `feat/1-a`. The dry run said "no `routing.md` names a branch
in its `Branch` row, so `gh` was not asked". A person opens the file and
finds the row there. The skill's three states say "no `routing.md` or no
`Branch` row", which does not cover this file either.

The second reason is the same class. The smith fed back that "a listed pull
request whose `mergeCommit` is null counts as no merged pull request". The
query asks for `--state merged`, so a listed pull request has merged by
`gh`'s own answer. The probe stubbed `gh` to answer `[{"number": 11}]`. The
dry run said "no pull request from `feat/1-a` has merged", which is false:
`gh` said one had. Both readings keep the item unreleased, which is the
safe direction for `--apply`. What is wrong is the sentence. It sends the
settling session to look for a cause that is not there.

A list entry that is not an object is skipped today. That is the garbled
answer *In* item 4's widening refuses when the whole answer is not a list,
so the entry gets the same refusal.

```python
def merged_pull_requests(root, branch):
    """`[(number, merge commit or None)]` for the pull requests from BRANCH
    that have merged, as `gh` lists them, asked from the repository's top.
    Raises `Unasked` where `gh` is not on PATH, does not run, exits non-zero
    or answers anything but a list of objects."""
    ...
    if not isinstance(answer, list) or not all(isinstance(pr, dict) for pr in answer):
        raise Unasked(f"{asked} did not answer a list of pull requests")
    out = []
    for pr in answer:
        merge = pr.get("mergeCommit")
        commit = merge.get("oid") if isinstance(merge, dict) else None
        out.append((pr.get("number"), commit if isinstance(commit, str) and commit else None))
    return out


NO_BRANCH = (
    "no `routing.md` that `hooks/routing.py` reads as a declaration names a "
    "branch, so `gh` was not asked"
)
```

```python
        # in released_local, replacing the `reached` and `listed` lines
        reached = next(
            ((n, c) for n, c in prs if c is not None and reaches(root, ref, c)), None
        )
        if reached is None:
            listed = ", ".join(
                f"#{n} at {c}" if c else f"#{n} with no merge commit" for n, c in prs
            )
```

```markdown
<!-- skills/settle/SKILL.md, What released means -->
  from the repository's top, once per branch. A work item is unreleased,
  and untouched, in three states: no `routing.md` that `hooks/routing.py`
  reads as a declaration naming a branch, no merged pull request from that
  branch, or no listed merge commit reachable from `--released-at`, a pull
  request listed with no merge commit among them. Shared mode never asks `gh`.
```

The two cases at `tests/test_settle.py:1016` and `:1043` pin the old words
and change with them. Under contract rule 14, a third case pins the
unreadable `Review` row: a `routing.md` with a `Branch` row and a `Review`
answer outside the vocabulary, whose reason is the new `NO_BRANCH` and for
which `gh` is not asked.

answer: 53972b46 takes the round's proposal: a list entry that is not an object refuses like a non-list answer, a pull request listed with no merge commit stays in the list and reads `#<n> with no merge commit` in the not-reached reason, and `NO_BRANCH` names `hooks/routing.py`. The skill's three states, the module docstring's, `declared_branch`'s docstring, the changelog fragment, `overview.md` *Fed back into the spec* and `phases/phase-1.md` say the same. The two pinned cases are rewritten (the null case renamed `test_a_pull_request_listed_with_no_merge_commit_is_named_as_such`), `test_a_local_routing_md_routing_py_does_not_read_names_no_branch` is added, and S5 gains an `entry` state; all five were seen red against the old code, and four mutants of the new lines went red. GitHub's GraphQL reference types `PullRequest.mergeCommit` as a nullable `Commit` beside a non-null `merged`, so the schema allows the shape; it does not say how often it occurs. `spec.md` *In* item 3 and its `## Rule changes` `add` still say "no `Branch` row"; they are the frame's.

### 4. The skill still says the removed specs are in git history, which no local-mode settle makes true

severity: should
location: `skills/settle/SKILL.md:344-346`, `docs/one-root-by-lifetime.md:31-36`, `seal/specs/1793051803-settle-runs-in-local-mode/spec.md:179-207`
evidence: executed `git grep -n -i -E 'git history|in history|recover' -- docs skills templates agents README.md seal/README.md`
verdict: fixed ef9048c7

*A settle is not a work item* says "It keeps no log: what changed is the
diff, and the removed specs are in git history." In local mode no commit
ever held the removed specs. The new *In local mode* section of the same
skill says so: "No commit holds what it removes". One skill now states both
facts about the same act. `spec.md` *Grounding* row 13 called this section
"kept whole for local mode", and the build followed the frame. The frame
missed this sentence, and contract rule 19 asks that it change with the fact.

The search finds one more sentence of the class.
`docs/one-root-by-lifetime.md` *The dependency rule* says a comment naming
a work item "still resolves through git history once the folder is gone".
Once settle removes local directories, no history holds them. The policy
root changes only through `## Rule changes`, so that sentence goes there.
The third hit, `docs/the-record-layout.md:114`, is about what the settle
itself wrote, which its pull request does put into git history. That one
still holds.

```markdown
<!-- skills/settle/SKILL.md, A settle is not a work item -->
its pull request. It keeps no log: what changed is the diff. Where the root
is shared the removed specs are in git history; in local mode no commit
holds them, and the dry run names `seal export` for whoever wants a copy.
```

```markdown
- change
  file: docs/one-root-by-lifetime.md
  section: The dependency rule
  from: and it still resolves through git history once the folder is gone
  to: and where the root is shared it still resolves through git history
    once the folder is gone; in local mode no history holds the folder, so
    the pointer names a work item that has left
```

Add the operation to `spec.md` `## Rule changes` and re-run
`rule_changes.py#parse` over the file (S12).

answer: ef9048c7 rewrites *A settle is not a work item* in `skills/settle/SKILL.md` as the round proposes and pins the new sentence in `test_the_skill_says_a_settle_is_not_a_work_item_and_owes_no_range_row`, seen red under the old sentence. The `docs/one-root-by-lifetime.md` operation is the orchestrator's ef5e520c in `spec.md` `## Rule changes`. `docs/the-record-layout.md:114` stands, as the round says: it is about what the settle wrote.

### 5. Two of the new sentences have two readings

severity: should
location: `skills/settle/SKILL.md:257-260`, `skills/settle/scripts/settle.py:860-867`
evidence: read `skills/settle/SKILL.md:257-260`, `skills/settle/scripts/settle.py:860-867`
verdict: fixed 9cfb9820

`CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*.

- The skill says "Every `seal/specs/<id>/` path is read and removed under
  `$(git rev-parse --git-common-dir)/seal/`". Joined as written, the path
  is `<git-common-dir>/seal/seal/specs/<id>/`. The code reads
  `<git-common-dir>/seal/specs/<id>/` (`settle.py#records_of`, which takes
  the directory that holds the root). A settling session closes rows in
  these records by hand at step 4, so the path it opens matters.
- `--released-at`'s help says "A work item is released when its directory
  is present there, or in local mode when it reaches the merge commit".
  The subject of "it reaches" is the work item, and the meaning is the ref.

```markdown
- **Where it reads.** Every `seal/specs/<id>/` path is read and removed
  under `$(git rev-parse --git-common-dir)`, so a work item's directory is
  `<git-common-dir>/seal/specs/<id>/`, and it is printed as
  `seal/specs/<id>/`. The policy root, the tracked files the citations are
  read from, and `tests/` are read from the repository's top.
```

```python
        help="the branch a release merges to. A work item is released when "
        "its directory is present there, or in local mode when this ref "
        "reaches the merge commit of the pull request from the work item's "
        "branch (default: origin/main)",
```

answer: 9cfb9820 rewrites both sentences to the round's text: the skill's *Where it reads* bullet names `<git-common-dir>/seal/specs/<id>/`, and `--released-at`'s help says "this ref reaches". The bullet is pinned in the S10 case and the help in `test_the_local_dry_runs_texts_say_what_they_hold`, each seen red under the old wording.

### 6. Two readings of released that the smith chose on purpose have no case

severity: should
location: `tests/test_settle.py:1016`
evidence: executed `grep -n 'gh.merged(' tests/test_settle.py`, `bin/test tests/test_tmp_round1_probe.py -q -p no:xdist -s`
verdict: fixed 9f854538

The smith claimed two choices. The first is that `settle.py#reaches` asks
git itself, not through `rule_changes.py#_ancestor`, because `_ancestor`
answers False for two equal commits (`phases/phase-1.md`). The second is
that where several merged pull requests come from one branch, the first
listed whose merge commit the ref reaches is taken (`overview.md` *Fed back
into the spec*). The probe shows both hold. `--released-at` given as the
merge commit itself reads the item as released, and
`rule_changes._ancestor(oid, oid)` is False. Two pull requests listed with
the first unreached read the item as released with the second. But every
local case passes `--released-at main` (`tests/test_settle.py:92`), and
every `gh.merged` call lists one pull request (the grep: eleven calls, one
pair each). So a mutant that reuses `_ancestor`, or one that looks at the
first listed pull request alone, passes the module. Both mutants read fewer
items as released, which is the safe direction. Still, the reason the smith
gave for each choice is the only thing that holds it.

```python
    def test_a_released_at_given_as_the_merge_commit_reaches_it(self, local, gh, capfd):
        """`reaches` asks git itself because `rule_changes.py#_ancestor`
        answers False for two equal commits, so a `--released-at` naming the
        merge commit still reads the item as released."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        oid = merge(local, "feat/1-a")
        gh.merged("feat/1-a", (11, oid))
        code = settle.main(["--root", str(local), "--released-at", oid])
        out = capfd.readouterr()
        assert code == 0, out.err
        assert f"released at {oid}: 1 work item;" in out.out, out.out

    def test_the_first_listed_pull_request_the_ref_reaches_is_taken(
        self, local, gh, capfd
    ):
        """Several merged pull requests from one branch: one the ref does not
        reach does not hide a later-listed one it does."""
        git(local, "branch", "other")
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        stray = merge(local, "feat/1-a", into="other")
        git(local, "switch", "-q", "main")
        git(local, "merge", "-q", "--no-ff", "-m", "m", "feat/1-a")
        reached = git(local, "rev-parse", "HEAD").strip()
        gh.merged("feat/1-a", (12, stray), (11, reached))
        code, text = dry_run(local, capfd)
        assert code == 0, text
        assert f"1700000001-a  pull request #11  merge commit {reached}" in text, text
```

Contract rule 15: each is seen red under its mutant, `reaches` replaced by
`_ancestor` and `prs` cut to `prs[:1]`.

answer: 9f854538 adds `test_a_released_at_given_as_the_merge_commit_reaches_it` and `test_the_first_listed_pull_request_the_ref_reaches_is_taken` to `Test_main`. With `mutation-check` after the commit, the first went red with `reaches` returning `rule_changes._ancestor(root, commit, ref)` ("0 work items"), and the second with the search cut to `prs[:1]`; the file was restored from the held bytes each time.

## Confirmations

confirms: none
No path found reads an unshipped work item as released, apart from finding
1's fork shape and the reused-name limit. Each shape the round looked for
fails closed, toward unreleased and untouched. A ref that does not resolve
is refused before `gh` is asked (the case at `tests/test_settle.py:410`). A
`gh` that is absent, exits non-zero or answers anything but a list exits 2
and removes nothing (S5's six cases). A merge commit the ref does not reach
is unreleased (S3). A merge commit git does not hold makes
`merge-base --is-ancestor` exit 128, which `reaches` reads as unreached
(`settle.py:196-202`). No `routing.md` and no `Branch` row are unreleased,
with `gh` not asked (S7). A `--released-at` given as the merge commit itself
reaches it, and the first reached of several listed pull requests is taken
(finding 6's probe). A branch holding `;`, `$(x)` and spaces reaches `gh` as
one argument, with no shell between (probe). `--apply` takes its candidates
from the disk again and intersects them with `released` (`settle.py:817`).
Executed for the probes, read for the rest.

confirms: none
Shared mode is unchanged and never asks `gh`. `records_of` compares
`home_at`'s answer with `<root>/seal`, and both are built from the one
`root` string (`hooks/optin.py:132-160`, `settle.py:570`), so a shared root
reads as shared. Every shared path keeps `records == root`: `has_spec`,
`open_rows`, `in_tree`, `closed_rows` and `apply`'s removal. `released` and
`rules.order` are untouched. The diff of `tests/test_settle.py` changes no
shared-mode case, and `test_shared_mode_never_asks_gh` asserts an empty
`gh` log over both commands. Read, and executed with the module.

confirms: none
The four divergences in `overview.md` hold. S2's case stands in
`tests/test_settle.py` as `tests/test_rule_changes.py:7` says such cases
do. *In* item 4's widening to an answer that is not a list follows the same
item's own reason (finding 3 carries it one step further). S9's place line
is the words `rule_changes.py#section_lines` gives for an absent document in
shared mode too. S10's case was rewritten to S10's assertions, renamed, and
its `.test_durations` entry removed with it. Read.

confirms: none
The text sweep holds. Outside `docs/`, `tests/`, `seal/specs/` and
`changelog/`, no line says `settle` refuses local mode or retires no
local-mode work item. The two that remain, `docs/the-review-record.md:382`
and its pin `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:207`,
are the settle's per `spec.md` *Out* and `## Rule changes` (S11). The
`README.md` and `README.ko.md` `settle` rows say nothing about local mode.
Executed with `git grep`.

confirms: none
S12 holds: the shared-mode dry run at `--released-at HEAD` in the clone
places this spec's `add` in a group with `to not found` and its `change`
with `from found, to not found`. Executed.

confirms: none
The touched modules pass. `bin/test` over `tests/test_settle.py`,
`tests/test_rule_changes.py`, `tests/test_settle_reads_before_it_removes.py`,
`tests/test_seal_stamp.py`,
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` and
`tests/test_censuses.py` gave 477 passed. The durations case
`test_the_durations_file_prices_the_suite` passes with the two removed
entries gone and the new cases unpriced. `test-layout --pairs` over the two
changed test files names no pair, so no new case duplicates its group.
Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The new cases on Windows: the `gh.cmd` stub found through `PATHEXT`, run through `cmd.exe` with `%*`, and the path joins under the common git directory. No `tests` run exists for this branch, because the workflow runs on a pull request and none is open | `tests/test_settle.py:99-116`, `overview.md` *Not verified* | the orchestrator, from the pull request's `tests` run, its four Windows groups |
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| Whether GitHub ever lists a merged pull request with a null `mergeCommit`, such as one marked merged by a push to the base. It decides how often finding 3's second reason is met, not whether its words are wrong | `settle.py:239-245` | the fix pass, from GitHub's GraphQL reference for `PullRequest.mergeCommit` |
| A local-mode settle run end to end against a real local root and the real `gh`. Only fixture repositories with a stub, and one read-only real query, have run it | `spec.md` *Out* | the owner, at the first local-mode settle |
| Q1's default, `gh` alone, against the hosts and merge methods the owner wants local mode to support | `questions.md` Q1 | the repository owner, at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_round1_probe.py -q -p no:xdist -s`, five cases over the `local` and `gh` fixtures of `tests/test_settle.py` | 5 passed. `--released-at <merge commit>`: exit 0, 1 released; `_ancestor(oid, oid)` False. Two pull requests, first unreached: released with #11. `Review` row unreadable, `Branch` row present: "no `routing.md` names a branch in its `Branch` row", `gh` not asked. `gh` answering `[{"number": 11}]`: "no pull request from `feat/1-a` has merged". Branch `feat/a;b $(x) c`: one argument to `gh`. File deleted |
| `bin/test tests/test_tmp_round1_subdir.py -q -p no:xdist -s`, the local fixture from the top and with `--root` at a subdirectory | 1 passed. Top: `place: docs/a.md section S, at docs/a.md:3-9`, `from found`. Subdirectory: exit 0, "the document is not in the tree in the working tree", `from not found`. File deleted |
| `bin/test tests/test_settle.py tests/test_rule_changes.py tests/test_settle_reads_before_it_removes.py tests/test_seal_stamp.py tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_censuses.py -q -p no:xdist` | exit 0, 477 passed |
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` | exit 0, 1 passed |
| `bin/test-layout --pairs tests/test_settle.py tests/test_settle_reads_before_it_removes.py` | 2 files read, 0 pairs |
| `bin/settle --released-at HEAD` | exit 0; 47 released; this spec's operations at `spec.md:181` (`to not found`) and `spec.md:202` (`from found, to not found`) |
| `gh run list --commit 12bd3195` in the working repository | no run |
