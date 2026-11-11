# Phase 1: 1794376287-check-lines-ride-in-every-preload

## What this phase found

**The frame holds, except at three points below.** Before the build, the frame's coordinates were opened at `bc05d454d`, whose tree outside this work item's directory is `896f50cab`'s. `grep -n '^check:'` over the six files printed exactly the 41 lines *Scope* item 1 lists (executed). `agents/sealer.md:152-154` held the rule *Scope* item 2 names, and each test unit stood at the line *Scope* items 5 to 11 give, with one exception noted below (read). `seal/follow-up.md` holds no row on check lines (read). Judged against `frame/design.md` *Scope* and `agents/crafter.md` *The frame is judged before it is built to.*

**G14's "Nothing else reads it" does not hold, so step 1 of `agents/sealer.md` now cites rule 2.** `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_sealer_cites_contract_rule_2` asserts that `agents/sealer.md` contains `rule 2`. The removed rule's second sentence, "The record holds the run rule 2 names.", was the definition's only citation of rule 2. With *Scope* item 2 applied, the S6 run failed on that case (executed). G14's `git grep` searched for the rule's lead, and the case reads only the citation, so the search could not find it. Three options were weighed:

- Keep the rule without its check line. `frame/plan.md` *Alternatives considered* row 5 rejected this at 97 B per sealer spawn.
- Remove the case. `frame/design.md` *Scope*, Out, keeps every test, and the case pins a citation that #120 and #969 put in the sealer's own file.
- Cite rule 2 where step 1 already refuses a broad run. This costs 14 B.

The third was taken: step 1's last sentence reads "Nothing broad is run in its place (rule 2)." It is rewrapped to stay inside 88 columns. Judged against `frame/design.md` *Scope*, Out, and `skills/core/SKILL.md` *The rule a mechanism is kept against*. This is a departure from the frame: `agents/sealer.md` changes at `:65`, a line *Scope* items 1 and 2 do not name.

**So the sealer's preload differs from D3 by those 14 B.** `wc -c` at `e9658c727` gives these preloads (executed): crafter 30,828 B, framer 35,884 B, proofer 31,474 B and tracer 24,148 B, each as D3 states. The sealer's is 31,866 B where D3 states 31,852 B, so a sealer spawn saves 1,320 B where D3 states 1,334 B. `agents/sealer.md` holds 10,515 B, and the contract holds 12,029 B as D3 states.

**G4's blank line after each line holds for 37 of the 41.** The last line of `agents/crafter.md` (`:187`), `agents/proofer.md` (`:190`), `agents/sealer.md` (`:195`) and `skills/agent-contract/SKILL.md` (`:228`) ends its file, with nothing after it (executed, `awk` over each file). Deleting it joins no paragraph either way, so the build is unchanged.

**The docstring *Scope* item 5 quotes stands at `:458-459`, not at `:457-458`** (read, at `f47b1d5ae` and `bc05d454d` alike). The text is the one the item quotes, so the edit went in as the item states.

**D2 was seen red at the base before any line was deleted.** With only the case and its loader written into `tests/text/test_every_agent_reads_the_contract.py`, `bin/test tests/text/test_every_agent_reads_the_contract.py -p no:xdist -q -k carries_no_check_line` failed for each of the five definitions and for `skills/agent-contract/SKILL.md`, and passed for `skills/core/SKILL.md` (executed). Each failure named the file and every line number with its text. For `skills/agent-contract/SKILL.md` it listed lines 32, 41, 71, 85, 100, 108, 119, 141 and 228. This is S5 at the base.

**D2 reads rules.py through `tests/conftest.py#load`, the loader the suite already has.** The parametrized set is each `agents/*.md`, then `skills/<name>/SKILL.md` for each name `listed_skills` reads from any definition, each once. Today that is the five definitions, the core and the contract. The failure message names the file, each line's number and text, and `skills/settle/rule-changes.md` *A rule has one shape*. The case went into the module's own group under a heading *what a preload carries*, beside the shape cases that read the same frontmatter (`agents/crafter.md` *A new test starts from its group.*). No earlier case of the module, nor of `tests/github/test_rules.py`, asserts that a file holds no check line (read).

**D1 went in with D2's words and new line breaks.** `frame/design.md` D1 has a 92-column line. `skills/settle/rule-changes.md` is held to 88 columns by `tests/behaviour/test_docs_line_wrap.py#COVERED`, so the paragraph is rewrapped, and its words are D1's.

**Each new or re-sliced unit was mutated, and each mutation was killed.** Each run used `bin/seal mutate` after the commit, and `git status --short` was empty after each one (executed):

- `agents/tracer.md`, line 57 turned into `check: tests/behaviour/test_a_probe_that_commits_says_so.py`, against `-k carries_no_check_line`: `red`, failing on `agents/tracer.md carries a check line at line 57`. This is S5 at the build commit.
- `skills/agent-contract/SKILL.md`, line 31 turned into a check line, against the same cases: `red` on the contract's parameter. This shows that the skills `listed_skills` reads are in the set.
- *Scope* item 6: `agents/framer.md`'s "as rule 10 says" turned into "as rule 11 says", against `tests/text/test_the_handoff_before_round_one.py -k carries_its_opening`: `red`.
- *Scope* item 7: `agents/crafter.md`'s "`## What this phase found` and to the hand-back" turned into "its section and to the hand-back", against `tests/behaviour/test_chain_hooks_hardening.py -k names_the_phase_record_section`: `red`.
- *Scope* item 8: `agents/crafter.md`'s "`new?` means nothing" turned into "`old?` means nothing", against `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -k names_the_failure_words`: `red`.
- *Scope* item 9: `agents/sealer.md`'s "`trail/gate.md` and `guarantee.md`, owes a new audit" with "and `guarantee.md`" removed, against `tests/behaviour/test_the_sealer_guarantees.py -k exempts_only_the_closing`: `red`.

The assertions *Scope* items 5 and 10 remove and the docstring clause item 11 removes add nothing to break.

**The re-sliced units read the text they read at the base.** For *Scope* items 6 to 9, a `python3` comparison of each old slice at `896f50cab` with its new slice at `e9658c727` found each pair equal once whitespace was collapsed (executed). This is the S6 clause on G8's comparison.

**The scenarios**, at `e9658c727` (executed):

- S1: `grep -c '^check:'` prints `0` for each of the five definitions and for the contract, and for `skills/core/SKILL.md`.
- S2: `git diff --name-status --diff-filter=DR 896f50cab HEAD -- tests evals` prints nothing. Each of the 32 distinct targets the base's lines name passes `test -e`.
- S3: `bin/seal rules --check` exits 0 and prints `seal rules: all 179 check lines in 69 rule files hold.`. That is G7's 178 plus D1's one. `bin/seal rules agents/sealer.md` prints `(no check line)` under each heading.
- S4: the figures above. Four agents match D3, and the sealer differs by 14 B, for the reason given.
- S5: D2 red at the base, and red at the build commit with one line restored, as above.
- S6: `bin/test` over the eight changed test modules, `tests/github/test_rules.py`, `tests/behaviour/test_this_repository_passes_its_own_checks.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `-q`, gave 483 passed and 1 failed. The failure was `test_every_spec_directory_that_reached_the_ladder_has_an_overview`, which names this work item because `gaps.md` was not yet written.
- S7: `git diff --stat 896f50cab...HEAD -- ':!seal/'` lists 15 files: the six of *Scope* item 1, `skills/settle/rule-changes.md` and the eight test modules of *Scope* items 4 to 11.

**The phase-boundary run**, one command through the repository's runner: `bin/test tests/text tests/behaviour tests/github/test_rules.py tests/github/test_release_report.py tests/skills/test_rule_changes.py tests/skills/test_payload_meter.py tests/skills/test_passages.py tests/skills/test_chain_check.py tests/skills/test_mutation_check.py tests/skills/test_session_cost.py tests/evals/test_noninferiority.py tests/test_censuses.py tests/test_conftest.py -q`. The files outside `tests/text` and `tests/behaviour` are those whose text names `agents/`, `agent-contract` or `rule-changes` (executed, `git grep -l`). That search is a sample of the files that read a changed path. At `e9658c727` the run gave 3,238 passed, 8 skipped and 1 failed, and the failure was the same overview case (executed). With this record, `gaps.md`, `changelog.md` and the Status cell written, `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/github/test_publish_release_note.py -q` gave 92 passed, exit 0, the overview case among them. `bin/seal unverified` over this work item's directory and `bin/seal layout --check` exit 0 (executed). `uvx ruff check` and `uvx ruff format --check` over the eight changed test modules exit 0 (executed).

**The scratch directory stays.** `agents/crafter.md` as installed (0.37.2) asks the crafter to remove its scratch directory before it hands back. The spawn says to remove nothing under the scratchpad, and contract rule 17 at `896f50cab` says no agent removes a scratch directory or a file in one. So `<scratchpad>/1794376287-check-lines-ride-in-every-preload/phase-1/` is left as it stands.
