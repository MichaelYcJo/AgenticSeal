# Review round 3: 1793240967-the-worktree-guard-was-never-weighed

target: 6dbce088, fixes a3255131..6dbce088

This is a verifying round. The diff read is `a3255131..6dbce088`. It holds
f720935f, the fix for round 2's finding 1, and 0bc5fe17, the round-2 record
as the fix pass left it. It also holds 7c1a0074, the orchestrator's fold into
the frame, and 6dbce088, the merge of `origin/release/v0.24.1` at 19372f7d.
The fix pass's answer, the commit messages and the spawn prompt were read as
claims. That includes the orchestrator's executed account of the merge. Each
claim below says what was claimed and what was found. The commands ran in a
`git clone --no-local` of the branch at 6dbce088.

Carried from rounds 1 and 2, and not re-established: the merge base
1e82fd0a, and the 17 `check:` lines of `docs/worktree-guard-spec.md` that name
the five test files this work deletes. Also carried:
`hooks/implementer-notice.py:112-116` as the one reader of
`hooks/lib/cmdline.py`'s outputs. Re-established this round: `seal/parity.md`
is not declared (executed, `ls`), so this round writes no `original:` line.
`seal/config.md` holds no `Record language` row (read), so the record is in
English. The S7 sweep and the rules check were run again at the merge,
because the merge brought 114 changed files from the release branch.

## Findings

### 1. The frame's grounding row still says `seal rules --check` reads the policy in force, and Scope In 7 of the same file says it excuses one shape

severity: should
location: `seal/threads/1793240967-the-worktree-guard-was-never-weighed/frame/design.md:17`
evidence: executed `git grep -n -i "policy in force"`
verdict: fixed 6eb32d52
reopens: round-2#1

The close does not hold in one place. Round 2's finding 1 was that the texts
describe the check as reading the policy in force, while it excuses only a
line inside a section that a pending `remove` with no `from` takes out, under
a shared root. f720935f narrowed every shipped text, and they now hold (see
`## Confirmations`). The fix pass's sweep ran `git grep -i "policy in force"`
outside the records, so it did not reach the frame. The orchestrator's fold,
7c1a0074, rewrote only the four frame lines that round 2's `location:` named:
`frame/design.md:104-108` and `:146`, `frame/plan.md:59` and
`frame/questions.md:22`. The search above, run at 6dbce088, finds the same
claim standing in the *Grounding* table's layout row at `frame/design.md:17`:
"`seal rules --check` reads the policy in force and excuses each such line,
naming this work item (Scope In 7)". Round 2 named the class and missed this
instance.

So the frame now says two things about one check. Scope In 7, at
`frame/design.md:104-109`, says the check "excuses one shape of pending rule
change", and that a pending `change`, or a `remove` with a `from`, excuses
nothing. The grounding row cites Scope In 7 and states the wider claim. The
sealer reads the frame against the tree, and a session reading the grounding
row first takes the wider claim. The repository rule *text an agent or a
check reads has one reading* (`CLAUDE.md`) refuses that. The rest of the row
holds. Its first sentence restates the layout rule's definition at
`skills/implement/SKILL.md:75`, which is about the policy and not about the
check.

The fix is the orchestrator's, in the same kind of fold as 7c1a0074. In
`frame/design.md:17`, the clause after "five test files this work deletes;"
becomes:

```markdown
`seal rules --check` excuses each such line, naming this work item, because this design's pending `remove` with no `from` takes their section out at the settle (Scope In 7).
```

answer: Holds, and 6eb32d52 closes it. That commit is the orchestrator's frame fold, not a crafter commit, and it changes only `frame/design.md` (one line, read with `git show --stat`). The *Grounding* layout row at `frame/design.md:17` now reads "`seal rules --check` excuses each such line, because this design's pending `remove` with no `from` takes its section out, and names this work item (Scope In 7)". That is the shape Scope In 7 and `.github/scripts/rules.py` state, so the frame says one thing about the check. `git grep -n -i "policy in force"` over the work item's frame prints only that row's first sentence (executed). As this finding says, that sentence restates the layout rule's definition at `skills/implement/SKILL.md:75` and is not a claim about the check. The design's `remove` of `docs/worktree-guard-spec.md` carries no `from`, so the clause matches what the check does in this tree: `bin/seal rules --check` exited 0 with 17 excused at f720935f (executed in round 2's fix pass). No code change was owed or made.

## Confirmations

confirms: none
f720935f's shipped texts say what the code reads. The fix pass claimed each
text now names the one shape excused, says that a pending `change` or a
`remove` with a `from` excuses nothing, and says no line is excused where the
`seal/` root is local. `skills/settle/scripts/rule_changes.py:259` skips every
item that is not a `remove` with `o.old` empty. `pending` at `:233-250` globs
`<root>/seal/threads/*/frame/design.md`, so a root under the common git
directory gives no item (read). The module docstring of
`.github/scripts/rules.py:28-38` matches both facts, and so does the
`unresolved` docstring at `:308-314`. The same holds for
`skills/settle/SKILL.md:125-129`, the module docstring, section comment and
`removed_by` docstring of `rule_changes.py`, and the excuse case's docstring
in `tests/github/test_rules.py:514-518`. The two READMEs' command tables and
the changelog fragment's bullet at `changelog.md:12` match too. The Korean
table names the pending `change` and leaves the `remove` with a `from`
implicit, as the English one does, since the sentence before it already says
"with no `from`" (read). `tests/github/test_gather_changelog.py`, which the
module docstring cites, stands at 6dbce088 and says why it has no case (read).
The answer's claim that no behaviour changed holds: f720935f's diff changes
docstrings, a comment, Markdown and the fragment, and no statement (read).
`git grep -n -i "policy in force"` outside `seal/threads/` prints
`agents/framer.md:54,175`, `skills/implement/SKILL.md:75` and the two cases
that pin the layout rule's sentence. The answer gave `:152` for the second
framer line, which the merge moved to `:175`. None of them says what the
check reads (executed).

confirms: none
0bc5fe17 changes only the finding's `verdict:` line, to `fixed f720935f`, and
its `answer:` line in `trail/rounds/round-2.md`. Nothing else in the record
changed (read, `git diff a3255131 0bc5fe17`).

confirms: none
7c1a0074 rewrites the four frame lines round 2 named to the narrowed claim.
*Scope* In 7 at `frame/design.md:104-109` names the one shape, a pending
`change` and the local root. S8's title at `:147` says "at a shared root".
`frame/plan.md:59-61` and `frame/questions.md:22-24` say the excuse comes from
this design's pending `remove` (read). Finding 1 above is the one line the
fold did not reach.

confirms: none
The merge keeps this work item's removals. The S7 sweep of
`frame/design.md` *Data & interfaces*, run at 6dbce088, prints 495 lines
(executed, exit 0). Outside `seal/threads/`, the replay eval and
`docs/worktree-guard-spec.md`, it prints the same five lines as round 2:
`docs/README.md:41`, `docs/the-review-record.md:633`,
`docs/the-routing-check.md:81`, `tests/behaviour/test_release_hygiene.py:129`
and `tests/hooks/test_root_migrate.py:927`. S7 lists each of them. Round 1's
search for the removed modules, variables, files and test paths, widened to
`userConfig` and `agentic-worktree`, prints the same lines round 1 accounted
for. Those are `tests/behaviour/test_chain_hooks_hardening.py:151,158,166`,
the generic option reader; `tests/conftest.py:504`; and
`tests/hooks/test_dispatch.py:1157` (executed, exit 0). The release side
changes no file under `docs/`, `.github/scripts/` or `skills/settle/`, and
does not touch `tests/conftest.py` or `.test_durations` (executed,
`git diff --stat 1e82fd0a 19372f7d`). So the documents that this design's
`## Rule changes` quotes in its `from` lines are byte for byte what this branch
read. `.test_durations` holds 6,069 entries, and its one key for a missing
file is the one 1e82fd0a's copy already held (executed).

confirms: none
The seven files git auto-merged keep both sides, and no hunk of one side
stands on the other's text. The orchestrator claimed a clean auto-merge, and
`comm` of the two sides' changed paths gives exactly those seven files
(executed). Each side's hunks were read (`git diff 1e82fd0a 7c1a0074` and
`git diff 1e82fd0a 19372f7d`, per file):

- `.claude-plugin/plugin.json` carries the release's `0.24.1` and has no
  `userConfig`.
- `skills/implement/orchestration.md` keeps this item's two citations of
  `docs/the-routing-check.md` *The edit check* at `:141` and `:145`. They
  stand outside the Bootstrap text that #1046 moved to
  `skills/implement/bootstrap.md`. A search of `bootstrap.md`,
  `skills/parity-setup/` and `agents/framer.md` for `worktree` finds only the
  word for a git worktree (executed). The routing question that
  `hooks/lib/press.py:3,32` and `tests/hooks/test_press.py:434-438` cite stays
  in `orchestration.md:92-105` (read).
- `hooks/lib/routing.py` takes the release's removal of `OLD_BY_CRAFTER` and
  this item's comment at the `NO_WORK_ITEM_AGE` line, in separate hunks.
- `hooks/mode-gate.py` takes the release's two citations of `bootstrap.md`
  and this item's two docstring sentences without the guard, in separate
  hunks.
- `skills/implement/SKILL.md` takes #1156's test-first sentence and this
  item's removed paragraph, in separate hunks.
- `tests/behaviour/test_chain_hooks_hardening.py` takes the release's change
  to the parity test and this item's change to the option test.
- `tests/censuses.py` takes the release's comment on `KEPT_OLD_NAMES` and
  this item's removed entries.

confirms: none
The rules check and the fold check hold at the merge. `bin/seal rules --check`
exits 0 with "17 excused in 268 check lines of 55 rule files, and every other
line holds". Every excused line names this work item (executed). The
release's two new check lines resolve. `python3 skills/settle/scripts/fold_check.py --root .`
exits 0 and prints "the index docs/README.md names every document" (executed).

confirms: none
The narrow modules of this work item and of the auto-merged files pass at
6dbce088 (executed, each command exit 0). The press, gate, dispatch, cmdline
and notice modules give 173 passed. The rules, rule changes, release hygiene,
fold, rider and cited-section modules give 210. The line-wrap, both-editions,
settle and settle-reads modules, which pin the fix's documents, give 144. The
hooks-hardening, censuses, mode-gate and routing modules give 293.
`uvx ruff check` and `uvx ruff format --check` pass over the three Python
files f720935f changed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over 6dbce088: unverified | the whole tree | the orchestrator, at the broad gate |
| Whether `.test_durations`, which prices none of the release's new cases or this item's 30 unpriced cases, stays under `test_the_durations_file_prices_the_suite`'s shares: unverified, because that case belongs to the broad run | `.test_durations` | the orchestrator, at the broad gate |
| The orchestrator's `git grep -i "worktree guard"` over the skills, agents, templates, hooks, `CONTRIBUTING.md` and both READMEs: read in the spawn prompt and not re-run as given; the S7 sweep above covers those paths with a wider pattern | the spawn prompt | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git diff a3255131 0bc5fe17 -- seal/threads/1793240967-the-worktree-guard-was-never-weighed/trail/rounds/round-2.md` | two changed lines, the finding's `verdict:` and `answer:` |
| `git grep -n -i "policy in force"` | exit 0; outside `seal/threads/` only the layout rule's definition and its pins; inside this work item, `frame/design.md:17` and the records |
| The S7 sweep of `frame/design.md` *Data & interfaces* | exit 0, 495 lines, five outside the threads, the replay eval and the guard's document, each listed by S7 |
| `git grep -n` for the removed modules, variables, test paths, `userConfig` and `agentic-worktree`, outside the threads, the replay eval and the guard's document | exit 0, five lines, each accounted for in round 1 |
| `git diff --stat 1e82fd0a 19372f7d -- docs/`, then `-- tests/conftest.py hooks/ .github/scripts skills/settle` | no file under `docs/`; `hooks/lib/routing.py` and `hooks/mode-gate.py` only |
| `comm -12` of the two sides' `git diff --name-only` against 1e82fd0a | exit 0, the seven auto-merged files |
| `python3 -` listing `.test_durations` keys whose file is missing | 6,069 entries, one missing file, the one 1e82fd0a's copy holds |
| `bin/test tests/hooks/test_press.py tests/hooks/test_question_gate.py tests/hooks/test_routing_edit_gate.py tests/hooks/test_dispatch.py tests/hooks/test_cmdline.py tests/hooks/test_implementer_notice.py -q` | exit 0, 173 passed |
| `bin/test tests/github/test_rules.py tests/skills/test_rule_changes.py tests/behaviour/test_release_hygiene.py tests/skills/test_fold_check.py tests/text/test_a_rider_reaches_its_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | exit 0, 210 passed |
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py -q` | exit 0, 144 passed |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/test_censuses.py tests/hooks/test_mode_gate.py tests/hooks/test_routing.py -q` | exit 0, 293 passed |
| `bin/seal rules --check` | exit 0, 17 excused in 268 check lines of 55 rule files, each naming this work item |
| `python3 skills/settle/scripts/fold_check.py --root .` | exit 0, "the index docs/README.md names every document" |
| `uvx ruff check` and `uvx ruff format --check` over `.github/scripts/rules.py`, `skills/settle/scripts/rule_changes.py` and `tests/github/test_rules.py` | exit 0 each |
