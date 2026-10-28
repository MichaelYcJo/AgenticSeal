# Review round 1: 1793140810-each-directory-holds-everything-in-one-level

target: f46a87dc against origin/release/v0.23.1

No earlier round exists, so this round carries no coordinate from one and
re-derived every fact it states.

## Findings

### 1. A machine updated from 0.23.0 keeps a preset block that names a moved template, and the update step that would refresh the block reads the old path

severity: should
location: `seal/threads/1793140810-each-directory-holds-everything-in-one-level/changelog.md:6`, `seal/threads/1793140810-each-directory-holds-everything-in-one-level/frame/plan.md:176-177`, `templates/setup/claude-md-block.md:16`
evidence: executed `git cat-file -e HEAD:templates/sdd-routing.md`, `git cat-file -e HEAD:templates/claude-md-block.md`, `git cat-file -e origin/release/v0.23.1:templates/claude-md-block.md`, `grep -c templates/sdd-routing.md <installed 0.23.0 copy>/templates/claude-md-block.md`, `bash -c "diff <(sed -n '/agentic:start/,/agentic:end/p' <HEAD archive>/templates/claude-md-block.md) <(sed -n '/agentic:start/,/agentic:end/p' <installed 0.23.0 copy>/templates/claude-md-block.md)"`
verdict: open

The preset block is the part of `CLAUDE.md` every session on the machine
loads. A session on a machine updated to 0.23.1 is told to write
`routing.md` from a template the plugin no longer holds at that path, and
the one procedure that refreshes the block fails on this update.

Claimed: `frame/plan.md:176-177` says "The CLAUDE.md block names
`skills/implement/orchestration.md`, which does not move", and the changelog
fragment (`changelog.md:6`) names two sentences in an installed repository
as the only old spellings a user keeps. Found: the block also names
`templates/sdd-routing.md`. The tree's block now spells
`templates/records/sdd-routing.md` (`templates/setup/claude-md-block.md:16`).
The block 0.23.0 installed spells the old path once (the `grep -c` above
printed 1), and `git cat-file -e HEAD:templates/sdd-routing.md` exits 128.
The block lives in `~/.claude/CLAUDE.md` or a project's `CLAUDE.md`, outside
the plugin, and `skills/update/SKILL.md:94-95` states that
`claude plugin update` never opens that file. So the stale sentence stays on
the machine until something rewrites the block.

The update does not rewrite it. `/agentic:update` runs from the release the
session loaded, 0.23.0. That release's step 4 diffs
`~/.claude/plugins/marketplaces/agenticseal/templates/claude-md-block.md`,
and its step 2 has just moved the marketplace clone to 0.23.1, where that
file is gone (`git cat-file -e HEAD:templates/claude-md-block.md` exits 128;
at the base it exits 0). The probe ran that diff against an archive of HEAD.
`sed` reported "No such file or directory", and `diff` exited 1 with all 17
lines of the installed block marked as added. That is the row "The block
differs" of the step's table, whose action replaces the marker region from
a source that is not there. A session either writes an empty block or stops
with no instruction for this case.

The fragment is the one text that reaches that session in time. Step 3 of
the same 0.23.0 procedure reads `changelog/0.23.1.md` before step 4, and it
gives "a path that moved" a line of its own for the user. The fragment lists
`claude-md-block.md` among the files of `templates/setup/`. It says nothing
about the block already on the machine, or about the step the user takes.
This is a `should`: the release ships a sentence an agent acts on that names
a missing path, and the path can be recovered, because the 0.23.1 edit gate's
refusal names `templates/records/sdd-routing.md`
(`hooks/routing-edit-gate.py:81-106`).

Add this entry under `### Changed` in `changelog.md`, after the entry that
begins "**Two sentences in an installed repository**":

```markdown
- **The preset block on a machine names a template that moved, and the update from 0.23.0 cannot refresh it (#1060).** The block between `<!-- agentic:start -->` and `<!-- agentic:end -->` in `~/.claude/CLAUDE.md`, or in a project's `CLAUDE.md`, tells a session to write `routing.md` from `templates/sdd-routing.md`, which is now `templates/records/sdd-routing.md`. `/agentic:update` run from 0.23.0 compares the block with `templates/claude-md-block.md` in the marketplace clone, which is now `templates/setup/claude-md-block.md`, so its comparison reads no source. After the update, run `bash install.sh "$HOME/.claude/CLAUDE.md"` from `~/.claude/plugins/marketplaces/agenticseal/`, which writes the 0.23.1 block over the old one and backs the file up first.
```

In `frame/plan.md`, replace the sentence at lines 176 and 177 with:

```markdown
The CLAUDE.md block names `skills/implement/orchestration.md`, which does
not move, and `templates/sdd-routing.md`, which moves to
`templates/records/sdd-routing.md`; a machine keeps the old block until it
is rewritten, and the changelog fragment says how.
```

The fix precondition: `install.sh` takes its source from beside itself
(`install.sh:44`), so it writes the marketplace clone's block, which is the
release just installed. The fix touches no OS boundary in the plugin.

answer:

## Confirmations

confirms: none
Claimed (`frame/design.md` scenario "The hooks an installed repository
registers are the same", and phase 2): each gate loads its modules from
`hooks/lib/` wherever the plugin stands. Found, executed: a probe extracted
HEAD's tracked files into a directory laid out as the plugin cache and ran
`dispatch.run_gate` for every gate `hooks/dispatch.py#GROUPS` names. All 15
loaded, with no failure of phase `load`. `opted_in` answered False for a
plain repository, so it read `hooks/lib/optin.py` (`hooks/dispatch.py:328-331`)
rather than falling back to True. `tests/hooks/test_dispatch.py`, the
fresh-interpreter case among its cases, passed in the narrow run.

confirms: none
Claimed: `bin/seal`, `bin/seal.cmd`, `install.sh` and `uninstall.sh` resolve
the moved paths. Found: `bin/seal --help` from the same cache-shaped copy
exited 0, so `bin/seal:20` reaches `hooks/lib/launch.py` (executed).
`bin/seal.cmd:9` and `install.sh:44` and `:58-59` name the new paths (read),
and `uninstall.sh` names no moved path (executed: `grep` for `templates` and
`hooks` over it found nothing).

confirms: none
Claimed (`frame/plan.md` *Operational impact*): the hygiene workflow a
repository holds runs scripts that do not move, from a clone at its pinned
tag. Found: `templates/setup/hygiene.yml:55`, `:83` and `:95` clone at
`v<version>` and run `chain_check.py` and `seal.py`, and the template's two
changed lines are a comment (executed: `git diff -M` over `templates`).
`skills/implement/scripts/seal.py:1922` and `:2043` join `templates`,
`setup` and `hygiene.yml` from single segments (read). No reader compares a
repository's workflow text with the template's: `seal.py#workflow_at`,
`#pinned` and `#left_workflow_line` read the clone line and the pin only
(read `skills/implement/scripts/seal.py:1933-1996`).

confirms: none
Readers that shrink instead of failing. Executed searches: every `glob`,
`listdir`, `scandir`, `iterdir` and `os.walk` in `tests/`, `.github/scripts/`,
`skills/*/scripts/`, `evals/scripts/` and `hooks/`; every glob pattern over
`hooks`, `tests` and `templates`; every join of a moved module's file name
without `lib`; every `TESTS`, `TEMPLATES` and `HOOKS` constant; and the
census's blind side, a vacated spelling after a `/` or a `\` inside a longer
path, for the modules, the templates and the 154 moved test files. None
found a reader the phase records do not already name. The readers opened
were `.github/scripts/rules.py:54`,
`tests/text/test_the_record_is_written_in_words.py:39`,
`tests/text/test_a_record_carries_no_comment.py:24`,
`tests/behaviour/test_the_root_migrates_itself.py:32`,
`tests/behaviour/test_one_word_one_meaning.py:920`,
`skills/verify/scripts/test_layout.py:1097-1101`,
`tests/hooks/test_launch.py:323-347`, `evals/scripts/replay_targets.py:222-237`
and `tests/conftest.py:31-39`. Each reads the new layout.

confirms: none
Claimed (phase 5): nothing outside the records names a removed skill.
Found, executed: `git grep` for `agentic:<name>`, `skills/<name>`, each
backticked bare name, `audit-rules` and the old skill count found nothing
outside `seal/threads/` and the changelogs. The one `debug` left,
`tests/hooks/test_review_skill_gate.py:92`, is a skill name the gate is
handed and no reference to a removed directory, as phase 5 says.
`bin/seal rules --check` read 265 check lines in 55 rule files and exited 0,
eight fewer rule files than phase 4's 63.

confirms: none
Windows separators, read. Each added join that is used as a path splits a
`/`-spelt name into segments: `tests/conftest.py#load_hook_module` and
`#run_hook`, `evals/scripts/replay_targets.py:231`,
`tests/evals/test_seed_defects.py:88`, `tests/censuses.py#vacated`. Each
path compared as text is made with `/` first: `test_layout.py:1077-1078`
and `:1188` replace `os.sep`, and `test_layout.py#_area` is compared with a
`posixpath.dirname` of that text. `tests/skills/test_seal.py:416` and
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:714`
compare a native `co_filename` with a native join. Reading found no `/`
constant joined and then compared as text. The run on Windows is a row of
`## Not judged`.

confirms: none
Each departure in `gaps.md` was read against the code, and none hides a
defect. Row 19, the walk in `tests/conftest.py:31-39`, would make a second
file of one name shadow the first. `tests/test_conftest.py`'s name case
refuses two Python files of one name under `tests/`, so the walk cannot do
that. Row 21's scaffold skip (`tests/evals/test_seed_defects.py:85-90`)
skips only a file the tree does not hold, and the check it feeds fails at
load where a needed sibling is missing. Row 23, executed: the design's
pattern matches no file in `tests/text/`, and it misses exactly nine files
in `tests/behaviour/`, the nine the row names.

confirms: none
Claimed: `f46a87dc` commits the durations of the run after the moves.
Found, executed: every one of the 158 tracked test files has a key in
`.test_durations`, and no key names an old top-level path. The tree's
`bin/seal layout --check` exited 0 with 158 files read and none refused.
`bin/seal layout --pairs` names none of the cases this work wrote new, and
reading the four cases of `tests/test_censuses.py#Test_vacated_paths` and
`tests/hooks/test_dispatch.py:1274-1300` found each case covering a
behaviour no other case of its class covers.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether an installed repository's first session after updating to 0.23.1 runs its hooks as before | `frame/questions.md` Q3 | the owner, in the first session after `/agentic:update` |
| Path separators at runtime on Windows; this round ran no Windows leg and did not open run 40611201777 | CI run 40611201777, its four Windows shards | the orchestrator, who read that run |
| The full suite, the repository-wide lint and the typecheck over the branch | the branch at `f46a87dc` | the orchestrator, through `bin/seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_dispatch.py tests/hooks/test_launch.py tests/behaviour/test_the_installer_writes_the_block_from_its_template.py tests/text/test_the_changelog_is_gathered_at_release.py tests/behaviour/test_chain_hooks_hardening.py -q -p no:randomly` | exit 0, 103 passed |
| `git archive HEAD` extracted under the round's scratch directory as `cache/agentic/0.23.1`, then `bin/seal --help` from that copy | exit 0 |
| `test_tmp_cache_load.py`: loads `hooks/dispatch.py` from the copy, calls `run_gate(gate, "{}")` for every gate of `GROUPS`, and `opted_in` on a plain `git init` repository, with `HOME` pointed at scratch | 15 gates, no failure of phase `load`; `opted_in` False; exit 0. Deleted with the copy after its run |
| the 0.23.0 step 4 `diff` with its source pointed at the copy's `templates/claude-md-block.md` | `sed` reported "No such file or directory"; `diff` exited 1 with the 17 installed block lines marked as added |
| `bin/seal layout --check` | exit 0, 158 files read, 0 refused, 91 declare no TARGET |
| `bin/seal rules --check` | exit 0, all 265 check lines in 55 rule files hold |
| `bin/seal layout --pairs` | exit 0; no pair names a case this work wrote new |
| keys of `.test_durations` compared with `git ls-files` of the test files | every tracked test file keyed; no key at an old top-level path |
