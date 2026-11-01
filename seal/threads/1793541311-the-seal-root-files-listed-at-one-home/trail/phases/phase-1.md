# Phase 1: 1793541311-the-seal-root-files-listed-at-one-home

## What this phase found

### Whether the frame holds

It holds, read at `94551a71` before the first edit. Every coordinate `frame/plan.md` *Technical context* gives stands where it says. In `skills/implement/SKILL.md`, the paragraph at lines 87-98 ends "lives as long as its work item:", the fenced tree is lines 100-117, and line 76 is the lifetimes table's `seal/` row. `skills/verify/orchestration.md:433` is the `Findings by Location` row. `skills/implement/scripts/seal.py:92-99` is the docstring paragraph *What the reminder counts, and what it does not*. The measure stands at `48d035aa` as design G4 quotes it: `git show 48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md`, *The table* row K3, decides "one source and a link", and its *Instances K3* names the `seal/` layout. The three tests the plan names read only what this phase leaves in place. `test_the_session_rule_sits_in_the_layout_section_of_the_skill` reads the `## Document layout` and `## Procedure` headings. `test_the_two_layout_trees_no_longer_show_it` reads the trees of `seal/README.md` and `templates/setup/seal-README.md`. The three cases that cite *Document layout — two roots, three lifetimes* cite the heading, which stays.

### Departures from the frame

None. Three wording choices were left to the build:

- **Scope item 1.** The sentence that led into the tree now ends at "lives as long as its work item." A new sentence follows it: each file the root holds is in `docs/the-record-layout.md` *seal/*, and each file of a work item's directory is in `docs/the-record-layout.md` *seal/threads/<work-item-id>/*. The path is written before each italic section, so `tests/behaviour/test_a_cited_section_stands_in_its_file.py#PATH_CITED` reads both citations. A second italic with no path before it is not read.
- **Scope item 3.** The location row says "every file the root holds outside `threads/`, each named in `docs/the-record-layout.md` *seal/*, is the repository's own and belongs under `docs`". The rule the row states is unchanged.
- **Scope item 4.** The docstring keeps its sentence "So a release whose only change was to `follow-up.md` reports 0." That sentence is an example of the gap. It does not list the root's files, and P2 below does not find it.

Judged against `frame/design.md` *Scope* items 1, 3 and 4, and `skills/writing-style/SKILL.md` *English prose rules*.

### How the phase is proved

The phase changes prose in two Markdown files and a docstring in one Python file, and it adds no behaviour. `skills/verify/SKILL.md` *The narrow command still has to be able to fail* gives two rows for this. *Prose only* is proved by whatever parses the files. *A comment or docstring inside source* is proved by the module still importing. No case was written new, and no `seal mutate` run is owed (`frame/plan.md` *Phases*).

- **S1** (executed at `f15fcb33`): `git grep -n -E '├──|└──' -- skills` prints nothing, exit 1.
- **S2** (executed). P1 and P2 were re-run from the design's description by a script under `<scratchpad>/1232/`, because the frame's own scripts are gone. Run at `cd694aa3`, the script prints the five P1 files and the nine P2 files *The probes* lists. Run on the working tree after the edits, P1 prints four trees, `README.md:123-138`, `README.ko.md:118-132`, `seal/README.md:83-101` and `templates/setup/seal-README.md:83-101`, each listing `README.md config.md parity.md pact.md follow-up.md threads/`. P2 prints windows in six files: the four P1 files, `agents/crafter.md` and `docs/the-record-layout.md`. It prints none in `skills/implement/SKILL.md`, `skills/verify/orchestration.md` or `skills/implement/scripts/seal.py`.
- **P3** (executed at `f15fcb33`, by `skills/settle/scripts/rule_changes.py#parse` and `#section_lines` over this tree). The design's `## Rule changes` parses into three `change` items. `errors` and `unread` are both empty. Each section is found once, at lines 267-278 for *seal/*, 10-26 for *The root and its lifetimes* and 10-28 for *루트와 그 안의 수명*. Each `from` is found in its section, and no `to` is.
- **The new citations can fail** (executed, a coverage probe, not a mutation of a unit). `seal mutate` renamed each new cited section in turn, using `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -x`. The renames were `*seal/*` to `*seall/*` in `skills/implement/SKILL.md`, `skills/verify/orchestration.md` and `skills/implement/scripts/seal.py`, and `*seal/threads/<work-item-id>/*` to `*seal/threadz/*` in the skill. Each run went red, and `test_every_cited_section_stands_in_its_file` named the planted citation at its line: `SKILL.md:100`, `orchestration.md:433` and `seal.py:95`. `seal mutate` restored each file from the bytes it held, and `git status --short` printed nothing afterwards.
- **The module still imports** (executed at `f15fcb33`). `ast.parse` reads `skills/implement/scripts/seal.py`, and `uvx ruff check` and `uvx ruff format --check` pass on it. The boundary run below loads it through the modules that import it.

### The phase-boundary run

Executed at `f15fcb33`: one `bin/test -q` over 87 modules gave 4374 passed, 8 skipped and 1 failed, in 47.50 s. The set is the union of two `git grep` lists over `tests/`, without `conftest.py` and `censuses.py`. The first list is each module that names `implement` with `SKILL.md`, `verify` with `orchestration.md`, or `seal.py`. The second is each module that lists files (`glob(`, `rglob`, `listdir`, `ls-files`, `os.walk`, `iterdir`, `git_listing`, `build_tracked_tree` or `corpus(`) and also names `skills`, `.md"` or `.py"`. The plan counts 42 modules that list files. This pattern is wider and found 54, and 53 of them name `skills`, `.md"` or `.py"`, so they joined the set. The set is a sample of the modules that read a changed path, because a module that reaches the files through a path built elsewhere is not on it (contract rule 12). The broad gate is the orchestrator's.

The one failure, read: `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` named this work item because it had no `gaps.md`. This phase writes that file, and the case was re-run after it was written (`gaps.md` *Not verified*).

### The class, and how it was listed

The class is every place that lists the root's files, in a drawing or in prose (design G6). P1 lists the drawings by their box lines, and P2 lists the prose by six-line windows naming three or more of the root's entries. Both methods match spellings, so the list is a sample for a list worded in a way neither matches, as *Scope* says. `README.md:117` names the follow-up list, the config and the migration config in prose. It is in P2's `README.md` window, and design *Scope* leaves it to #1102 with the README's tree (G7). One search was added for text about the skill's tree: `git grep -i` for "layout tree", "skill's tree" and a tree named beside `implement/SKILL.md`, outside `seal/threads/`. It found no sentence about the removed tree, only `test_the_two_layout_trees_no_longer_show_it`, which reads the two seal-README trees.

### Owed by another party

`skills/verify/orchestration.md` is a `skills/*/orchestration.md` file, so `docs/the-record-layout.md` *A change writes fragments, never a shared file* asks this work item's `changelog.md` to end with a `### Process changes` row. That section says "The orchestrator writes it with the fragment", so this phase writes the fragment without the row and leaves the row to the orchestrator. The change only links the record layout in place of a list, so the orchestrator decides whether the row describes a change to the way of working.
