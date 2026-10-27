# Phase 3: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | c0f77564 |

## What this phase was asked

Build `frame/plan.md`'s row 3 and nothing of phases 4 and 5: the names.
That is `plugin.json`, `marketplace.json` with `renames`, the agents moved to
`crafter.md`, `proofer.md` and `tracer.md`, the `agentic:` prefix everywhere,
the slug, `PLUGIN_CLONE` and `workflow_at` recognising both clone lines, the
trailer with its grace for the old key, `implementer.py`,
`review-skill-gate.py`, `install.sh` and `uninstall.sh` replacing the old
block, `skills/update/SKILL.md`, the eval directories and prompts, `docs/` in
place with the rule-change rows applied, and `LICENSE`. #1051's body is the
one source of the names. The `bin/` wrappers and `seal <subcommand>` stay
phase 4's, and the census and the tagline sentence stay phase 5's.

The owner's verification decision in `frame/plan.md` *Verification this work
item owes* bound the phase. A name or path that moves is proved by the
existing cases passing under the new name. A case is written new, and seen
red once, only for behaviour that did not exist before. No `mutation-check`.
The row's cases and the modules `git grep` finds reading what changed run in
one `bin/test` command.

## What this phase found

**The cases written new, and the cases relied on.** Five cases are new, one
for each behaviour that did not exist before, and each was seen red once
against the tree with only the rename in place. In
`tests/test_chain_check.py`,
`Test_routing_trailers::test_reads_the_trailer_a_commit_before_0_23_0_carries`
failed while `TRAILER` read `Seal-Routing` alone. In `tests/test_seal.py`,
`Test_workflow_at::test_accepts_a_file_cloning_the_old_slug_as_its_own` and
`Test_install_workflow::test_accepts_its_own_file_under_the_old_slug_by_rewriting_it`
failed with `other` and `kept` while `PLUGIN_CLONE` held only the new slug.
In `tests/test_the_installer_writes_the_block_from_its_template.py`,
`test_install_sh_replaces_the_block_under_the_old_markers_once` and
`test_uninstall_sh_removes_the_block_under_the_old_markers` failed while the
scripts knew only the new markers: the installer appended a second block and
the uninstaller left the old one. Everything else is an existing case under
the new name: the implementer mark and notice, routing, review-skill gate,
session cost, payload meter, the behaviour-suite modules, the definition
readers that open `agents/crafter.md`, `agents/proofer.md` and
`agents/tracer.md`, and the docs readers whose pinned sentences now carry the
new paths. The last run of the phase was 132 modules in one command: 6342
passed, 3 failed in `tests/test_plugin_directory_check.py`, which pins the
plugin's name, and that module passed once its pins read `agentic`.

**The frame does not hold in three places.** First, the old-block case
belongs in `tests/test_the_installer_writes_the_block_from_its_template.py`,
the module that runs `install.sh`, not in
`tests/test_first_setup_asks_once.py`, which the row names and which only
reads the block. Second, the rule-change rows write 0.23.0, 0.23.x and
0.24.0 into `docs/`, and
`tests/test_release_hygiene.py::test_no_loaded_file_names_a_version_at_or_above_the_running_one`
refuses every version at or above the running one in a loaded file. Every
grace sentence says "before the plugin was renamed AgenticSeal" and "the
next minor release removes" instead. Third, the *Naming* row for the agents
repeated the `add` row of `docs/the-agent-set.md` word for word, and
`tests/test_no_passage_is_pasted_into_a_second_file.py` refused the pair, so
*Naming* points at that section. `gaps.md` holds each, with the routing
answer, the scaffolds and the renamed heading below.

**The routing answer follows the agent.** `hooks/routing.py#BY_CRAFTER` is
`crafter`, and the template, the boxes of the routing question and the
README rows spell it. A declaration written before the rename that answers
`Implementation` with `smith` now reads as unanswered, so the notice stays
silent for it. This work item's own `routing.md` answers `smith`; it is the
orchestrator's file.

**What the behaviour suite keeps and what it moves.** The agent directories,
the reach graders (`reach-crafter.md`, `reach-proofer.md`), the prompts, the
case names inside `case.yaml` and the generators' agent keys follow the
agents. The case directory names (`rule-warden-one-finding`,
`rule-smith-*`) and the `specseal` key of a saved side's JSON stay: renaming
either changes what `recurred_truths.json` and a saved side are keyed by,
which phase 5's census decides. The 14 rule-case scaffolds answer
`Implementation` with `crafter`, because `tests/test_evals_layout.py` holds
them byte for byte to `rule_cases.py`; the 8 replay and seeded scaffolds keep
their bytes and their old clone line. `noninferiority.py` reads a suite by
its agent's directory, so a side taken before the rename cannot be compared
with one taken after it; a work item that starts after the merge takes both
sides after it.

**Messages a person reads changed with the names.** The implementer notice
opens with `[agentic]`, the migration and stamp lines with `agentic:`, the
version notice names AgenticSeal and `agentic@agenticseal`, the review-skill
gate offers "AgenticSeal review" and `@agent-agentic:proofer`, and
`session_cost.py` names a crafter row and a proofer's verifying round. Each
case that pins the text pins the new text.

**What is left for phases 4 and 5.** Prose that names smith, warden or scribe
outside `docs/`, the brand SpecSeal in prose, identifiers spelt
`specseal_...`, the `SPECSEAL_RECORD_*` variables, the eval case directory
names and the descriptions in both manifests are phase 5's census and sweep. The
`bin/mutation-check` comment naming `agents/smith.md` is phase 4's, which
removes the wrapper. `docs/release-checklist.md` still names SpecSeal's
directory listing, because nobody has read the listing since the rename.
`docs/one-root-by-lifetime.md` *What first setup asks* still says the
session-start hook moves the layout from before the root; phase 1 removed
that arm and no rule-change row covers the sentence, so it is the frame's to
answer.

**The suite writes into the real home directory.** Each run that reached the
session-start group left `~/.claude/agentic/version-check`, as phase 2's
record says. Each was removed after its run, and `~/.claude/specseal/` was
never touched.
