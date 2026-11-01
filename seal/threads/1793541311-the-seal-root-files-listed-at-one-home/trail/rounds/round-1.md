# Review round 1: 1793541311-the-seal-root-files-listed-at-one-home

```seal
target: 27d1b356 against cd694aa3
```

The target is the branch at `27d1b356` against its merge base with `origin/release/v0.27.3`, `cd694aa3`. The release branch has since moved to `361ed0cb`. Its new commits change none of the files this diff changes, and none of `docs/the-record-layout.md`, `docs/one-root-by-lifetime.md`, `docs/one-root-by-lifetime.ko.md`, `README.md` or `README.ko.md` (executed, `git diff --name-only cd694aa3 origin/release/v0.27.3`). No earlier round exists, so no fact is carried; every fact below was established this round. `seal/` declares no `parity.md`, so the round block holds no `original:` line. `seal/config.md` has no `Record language` row, so the record is English.

The axes walked: completeness of the class (every place that lists the `seal/` root's files), what the removed tree said and where each fact now stands, the truth of each rewritten sentence against the code it describes, the citations the new sentences add and whether the check that reads them can fail, the rule changes' parse, and the honesty of the build's labels. Inputs, authorization, query scope, ordering, concurrency and security have no subject here: the diff changes prose and one docstring, and no code path.

## Findings

### 1. The README's `seal/` row still lists three of the root's files, the same short list Scope item 2 removed from the skill, and the design gives no grounds for leaving it

```seal
severity: should
location: `README.md:117`, `README.ko.md:112`, `seal/threads/1793541311-the-seal-root-files-listed-at-one-home/frame/design.md:44`
evidence: executed `python3 test_tmp_root_lists.py`, `sed -n 108,140p README.md`, `sed -n 110,113p README.ko.md`
```

Why it matters: the class this work owes, by `frame/design.md` G6 and contract rule 12, is every place that lists the root's files, in a drawing or in prose. `README.md:117`, the `seal/` row of *Where the records live*, reads "everything this plugin maintains — the follow-up list, the repository's own config (the two language rows and the mode live there), the migration config — and, beneath it, the work items". `README.ko.md:112` says the same in Korean. That is the list Scope item 2 removed from the skill's lifetimes row, and it omits the same two files, `seal/pact.md` and `seal/README.md`. `frame/plan.md:24`, alternative A6, rejected leaving such a list on contract rule 12, because "a reader [...] meets a list without it".

The build's account is a claim here. `trail/phases/phase-1.md:37` says of `README.md:117` that "design *Scope* leaves it to #1102 with the README's tree (G7)". The design does not. `frame/design.md:44`, the only Out item for the READMEs, gives grounds for their trees alone: "Their trees list what the home lists once item 5 is settled". The row is not a tree, and it does not list what the home lists. G7's ground is #1102's comment 6552868724, which says "The layout tree links the home #1232 gives it", again the tree alone. #1102's K3 instances, read at `48d035aa` in `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md` *Instances K3*, are K3.1 (`README.md:118`), K3.2 (`README.md:208-209`) and the drawn layout, and none of them is this row. The row was found by P2 (it sits in P2's `README.md` window) and was then read as part of P1's tree. The list the build handed back is therefore not whole for the prose half of the class, and the hand-back did not say so.

This round's probe listed every paragraph and every table row of a tracked text file outside `seal/threads/` and `tests/` that names two or more of the root's entries, a lower bar than P2's three. Read one by one, the lists of the root's files at `27d1b356` are the four drawn trees, `docs/the-record-layout.md` *seal/*, and these two README rows. Every other hit names two files for another reason, such as a reading order or a parser's constants. The probe matches English spellings, so it is a sample for a list worded otherwise. It did not match the Korean row, which was read by hand.

The fix that matches Scope items 2 to 4 links the home in place of the list, in both editions, which the hygiene workflow's step holds to moving together:

```markdown
| `seal/` | permanent | everything this plugin maintains, each file named in `docs/the-record-layout.md` *seal/*, and, beneath it, the work items. Its existence, with its `README.md` opening with the marker line `templates/setup/seal-README.md` starts with, is also what opts the repository in, for each hook whose Where column under *The gates* below names `seal/` |
```

```markdown
| `seal/` | 영구 | 이 플러그인이 유지하는 전부(파일 하나하나는 `docs/the-record-layout.md` *seal/* 에 있다)와 그 아래의 작업 항목들. 이 디렉터리가 있고 그 안의 `README.md` 가 `templates/setup/seal-README.md` 의 첫 줄인 표시 줄로 시작한다는 것 자체가 옵트인이며, 이것을 보는 훅은 아래 「게이트」 표의 "어디서" 열에 `seal/` 이 적힌 훅이다 |
```

The other route is an Out item at `frame/design.md:44` that names the row and gives its own grounds, for example that #1102 rewrites the whole section. No document read this round gives those grounds today: #1102's body asks for a rewrite of both editions, and its comment names the tree alone.

## Confirmations

```seal
confirms: none
```
What matched: S1. No drawn tree stands under `skills/`. `git grep -n -E '├──|└──' -- skills` printed nothing and exited 1 at `27d1b356` (executed).

```seal
confirms: none
```
What matched: the three passages Scope items 2 to 4 name no longer list root files, and each links `docs/the-record-layout.md` *seal/*. These are `skills/implement/SKILL.md:76`, `skills/verify/orchestration.md:433` and `skills/implement/scripts/seal.py:94-96` (read). The removed wordings "repository's config, the migration config", "Root-level files" and "the root also holds" stand nowhere outside `seal/threads/` (executed, `git grep -n -e` over the three wordings, no output).

```seal
confirms: none
```
What matched: the rewritten docstring is true of the code. `skills/implement/scripts/seal.py:466-474`, `work_item_of`, counts a path only where it has three or more parts and the first is `threads`, and `check` at `skills/implement/scripts/seal.py:2707-2733` compares only `work_item_digests`. So any file the root holds outside `threads/` is not counted, as the docstring says. The export state file sits under the common git directory (`state_path`, `skills/implement/scripts/seal.py:787-789`), not in the root, so it is no unlisted root file (read).

```seal
confirms: none
```
What matched: the new citations are read by the check and can fail. In the clone, `*seal/threads/<work-item-id>/*` at `skills/implement/SKILL.md:100` was planted as `*seal/threadz/*`, and `*seal/*` at `skills/implement/scripts/seal.py:95` as `*seall/*`. `bin/test -q -p no:xdist tests/behaviour/test_a_cited_section_stands_in_its_file.py` then failed, and `test_every_cited_section_stands_in_its_file` named both planted citations at those lines. Both files were restored with `git checkout --` (executed). This re-runs a sample of the build's coverage claim in `trail/phases/phase-1.md` *How the phase is proved*.

```seal
confirms: none
```
What matched: P3 and S5's parse. `skills/settle/scripts/rule_changes.py#parse` read the design's `## Rule changes` with policy root `docs` as three `change` operations, with `errors` and `unread` empty. `#section_lines` found *seal/* at lines 267-278 of `docs/the-record-layout.md`, *The root and its lifetimes* at 10-26 of `docs/one-root-by-lifetime.md` and *루트와 그 안의 수명* at 10-28 of its Korean edition. Each `from` was found once in its section, and each `to` was found nowhere (executed). The two added rows describe `seal/parity.md` and `seal/pact.md` as `templates/setup/parity.md` and `docs/the-pact.md` *The words* do (read).

```seal
confirms: none
```
What matched: the removed tree carried no fact that the tree alone held, as design G11 claims. The `routing.md` writer and timing stand at `skills/implement/SKILL.md:332`, and the framer reads it at `agents/framer.md:43`. The rounds leaving at the settle stand in `docs/the-record-layout.md` *seal/threads/<work-item-id>/*. `seal gate --record` is at `docs/the-review-record.md:159`, and `guarantee.md` from its template is at `agents/sealer.md:100` and `docs/the-review-record.md:274` (read). The other citations of *Document layout — two roots, three lifetimes*, at `agents/framer.md:188`, `skills/implement/orchestration.md:371` and `README.md:119`, cite it for the policy in force and the rule changes, which the section still states. The citation it no longer answers, in `docs/one-root-by-lifetime.md` *The root and its lifetimes* and its Korean edition, is changed by the design's `## Rule changes` (read).

```seal
confirms: none
```
What matched: the period between merge and settle is accounted for. `docs/the-record-layout.md` *seal/* lacks the `parity.md` and `pact.md` rows until the settle, and the skill now sends a reader there. That is the route design G3 leaves, since a pull request does not edit `docs/`. `skills/implement/SKILL.md:74` states that the policy in force includes the unsettled designs' rule changes, and `frame/plan.md` *Operational impact* names the gap (read).

```seal
confirms: none
```
What matched: the narrow run over the changed paths. Every module under `tests/` that names `implement/SKILL.md`, `verify/orchestration.md` or `seal.py`, 41 of them, together with `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, gave 1959 passed and 8 skipped in one `bin/test -q` at `27d1b356` (executed). This is a probe and not the seal. It is a sample of the modules that read a changed path, because a module that reaches a file through a walk is not on it.

```seal
confirms: none
```
What matched: the labels and the owed process row. `gaps.md` *Not verified* labels the full suite, lint and format unverified and names the orchestrator through `seal gate` as the one who answers them. S3, S4 and S5 each name who answers them. `changelog.md` ends with `### Process changes` and one row in the shape `docs/the-record-layout.md` *A change writes fragments, never a shared file* asks for, since the diff changes `skills/verify/orchestration.md` (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD | the branch at `27d1b356` | the orchestrator, by `seal gate`, after the rounds settle |
| S3 and S4: the settle writes the *seal/* table with six rows, and the record layout alone for the layout file by file | `frame/design.md` *Rule changes* | the repository owner, at the settle after 0.27.3 |
| S5 at the pull request: `chain-check` reads the three `change` items and refuses nothing | the `hygiene` workflow's chain step | the pull request's CI |
| A list of the root's files worded in a way neither P1, P2 nor this round's probe matches, in English or Korean | the tracked tree outside `seal/threads/` | open: no method lists the class whole (contract rule 12); the next round over this class reads what it opens |

## Probes

All probes ran in `<scratchpad>/1793541311-the-seal-root-files-listed-at-one-home/round-1/clone`, a `git clone --no-local` of the worktree checked out at `27d1b356`. The probe file was deleted and the planted renames restored before hand-back.

| Command | Result |
|---|---|
| `python3 test_tmp_root_lists.py`: every paragraph and table row of a tracked `.md`, `.py`, `.yml`, `.txt`, `.toml` or `.json` file outside `seal/threads/` and `tests/`, kept where it names two or more of the root's entries in their English spellings | 21 units. Read one by one, the lists of the root's files are the trees at `README.md:121`, `README.ko.md:116`, `seal/README.md:81` and `templates/setup/seal-README.md:81`, and the row at `README.md:117`. The other 16 name two files for another reason. `README.ko.md:112` was not matched and was read by hand |
| `git grep -n -E '├──\|└──' -- skills` | no output, exit 1 |
| `bin/test -q` over the 43 modules listed in the narrow-run confirmation | 1959 passed, 8 skipped, exit 0 |
| `bin/test -q -p no:xdist tests/behaviour/test_a_cited_section_stands_in_its_file.py` with `*seal/threadz/*` planted at `skills/implement/SKILL.md:100` and `*seall/*` at `skills/implement/scripts/seal.py:95` | exit 1, 1 failed and 42 passed. Both planted citations were named at their lines |
| `rule_changes.parse` and `rule_changes.section_lines` over `frame/design.md` with policy root `docs` | 3 `change` operations, no errors, no unread lines. Each `from` was found once in its section, and no `to` was found |
| `git diff --name-only cd694aa3 origin/release/v0.27.3`, filtered to the changed files, the two `docs/` files of the rule changes and the READMEs | no output |
