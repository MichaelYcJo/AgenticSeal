# Phase 1: 1794128303-the-plugin-ships-two-hooks-again

## What this phase found

**The frame holds for this phase, with one citation that does not.** Every
coordinate phase 1's row names stood at `563f906a`: no tracked file under
`hooks/` or `tests/hooks/`, `0fd6046ad^:hooks/core-start.py` and
`0fd6046ad^:hooks/lib/core.py` with their two test modules,
`tests/lib/test_launch.py#before_any_floor` starting from the launcher's
text, `payload_meter.py#ENTRY_ROW`, and the roots sentence. The one *no*:
`frame/plan.md` *Technical context*, the paragraph opening **What returns
and from where**, cites `skills/verify/scripts/payload_meter.py` at the
commit `0fd6046ad` for the meter that shows `HOOK_ROW` and the `_core`
loader. At `0fd6046ad` the meter holds
`ENTRY_ROW`. `HOOK_ROW` and `_core` stood at `0fd6046ad^`, and `git diff
0fd6046ad^ 0fd6046ad` over the meter is the change this phase reversed.
`0fd6046ad` also stands on no `main` or release ref (`git branch -a
--contains` names only the #1376 feature branch), so
`tests/text/test_a_cited_commit_outlives_the_squash.py` fails on
`frame/plan.md:9`. It fails the same way at `563f906a`: executed in a
scratch worktree of that commit, which was then removed. The squash on
`main` that holds the same history is `1ae24b1e0`, so
`1ae24b1e0^:skills/verify/scripts/payload_meter.py` is the citation that
opens in every clone. The frame is the framer's and the orchestrator's to
fold, so this phase leaves the sentence and the failing case as they are.

**`hooks/core-start.py` answers the console with `lib/console.py`'s loop,
not with `console.to_utf8()`.** `frame/design.md` *Data & interfaces* says
the script calls `console.to_utf8()` and exits 0 on every path, including
an exception. Those two cannot both hold under
`tests/censuses.py#entry_point`, which wants the answer to be the
`__main__` block's first statement. `to_utf8()` needs `lib/` imported
first, and an import that fails would raise before any catch. So the block
opens with the loop over `STREAMS`' pairs in the form `loop_pairs` reads,
as `skills/verify/scripts/seal_stamp.py`'s block does. Then a
`try`/`except BaseException` wraps `main()`, and `sys.exit(0)` follows.
`main()` imports `core` itself. A copy of the script with no `lib/` beside
it exits 0 with both streams empty, which
`tests/hooks/test_core_start.py#Test_main::test_refuses_to_fail_where_its_library_is_gone`
holds. The behaviour is the design's, and only the call's spelling
differs.

**`main()` keeps no guard of its own for an unreadable payload.** The
first build checked for a JSON error and for a `cwd` that is not a
non-empty string. `seal mutate` left both checks green with each removed.
`json.load` and the `["cwd"]` read raise on every payload that is not a
JSON object holding `cwd`, and the catch in `__main__` already turns those
raises into exit 0 with nothing printed. A `cwd` that is not a path
reaches `optin.repo_root`, which answers "" for it. So the guards went in
commit `2662b961`, and the case's five payloads still print nothing. The
old hook printed the plugin's own core for such a payload. The new one
prints nothing, because `frame/design.md` *Data & interfaces* says
"nothing on a payload that is not JSON or holds no `cwd`".

**The closing line's words are this phase's**, as `frame/questions.md`'s
assumptions leave them to the crafter. `lib/core.py#START` reads: "Where a
request to change code or to work an issue arrives in this session, this
session is the orchestrator and opens `<root>/skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket* before its first edit. Where a
request to review a pull request, a diff or a branch arrives, it opens
`<root>/skills/code-review/SKILL.md`." Each path is joined with
`os.path.join` under the absolute plugin root, so it follows the
platform's separator. `tests/lib/test_core.py#Test_rendered` pins the
line. The tree's whole output measures 8,515 characters with the line
included, under `CAP` (executed: `seal payload --root .`, and the hook run
by hand on Python 3.12.11 and on `/usr/bin/python3` 3.9.6, both exit 0).

**Five edits stand outside item 1's text, each on the unit item 1
changes:**

- `tests/lib/test_launch.py`: the test docstring at `:203-212`, the
  constant and comment at `:310-311` and the docstring at `:375-388`.
  Item 2 lists them for phase 2. They describe the derivation item 1
  restarts from `hooks/hooks.json`, and `frame/plan.md` *Constraints* puts
  the derivation and its `ruff.toml` line in one commit. `STAMP` went,
  since nothing read it once `hooked` became the start. `hooked` reads
  only each command's `python3` half and does not test the
  `${CLAUDE_PLUGIN_ROOT}` prefix. The hardening case holds both, so a
  branch for either decided nothing, as the mutation runs below show.
- `tests/skills/test_payload_meter.py:9,102,456` and the `/agentic:start`
  wording in `payload_meter.py`'s docstrings. Item 3 lists them for phase
  3, but they describe the session row item 1 rewrites, so they turn
  false in this phase.
- `tests/behaviour/test_chain_hooks_hardening.py`, the module docstring at
  `:4-6`. `## Removes` lists it under *the "registers no hook"
  statements*. Its first sentence turns false in this phase. The new text
  names the two test modules that hold what each command does, which
  stays true after phase 2.
- `ruff.toml`'s comment over `per-file-target-version` now names the
  scripts `hooks/hooks.json`'s commands run. It still names the stamp's
  launcher, because the launcher stands until phase 2, which item 2 gives
  `ruff.toml:32-36`.
- `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#OPENS_NOTHING`
  gains the hardening case. The case now derives a path list with `git
  ls-files`, and that module refuses an unclassified scope. The case only
  tests membership in the list and opens none of its paths. The frame
  names no edit to that module.

**Two smaller changes.**
`tests/behaviour/test_the_release_check_watches_what_ships.py#test_the_release_document_names_the_same_roots`'s
docstring said "both say six". It now states no count, because a seventh
root made the old number false and a count stated there drifts with every
root. `CLAUDE.md` loses the sentence "A session the entry never reached is
outside the workflow and bound by nothing in the core". *Scope* item 1
gives the paragraph's new content in full, and that sentence is not in it.

**Seen red, each before its case was committed:**

- `tests/hooks/test_core_start.py#Test_main::test_refuses_to_print_into_a_repository_with_no_root`
  and `tests/lib/test_core.py#Test_output::test_refuses_a_repository_with_no_marked_root`:
  `seal mutate lib/core.py` replaced `if not optin.opted_in(cwd):` with
  `if False:`, which is `output` without the opt-in test, and both went
  red at their `== ""` assertion.
- `tests/behaviour/test_chain_hooks_hardening.py#test_the_plugin_registers_two_hooks_and_writes_none_into_git`:
  `seal mutate hooks/hooks.json` added a third event, `Notification`, and
  the case went red at its event-keys assertion.
- `tests/skills/test_payload_meter.py`'s four session cases and the
  `core.py` row of `test_a_script_copied_alone_exits_2_and_names_what_it_misses`
  ran against the meter as it stood at `563f906a`, before the meter was
  edited. All five failed, and the first failed at `[f["path"] for f in
  hooks] == [HOOK_ROW]`, which is the row's name.

**Mutation runs**, each `seal mutate` over the committed tree. "red" means
a case went red:

- `lib/core.py`, at `8c268944` and `ebd9c215`: eleven mutants, all red.
  Their targets: the opt-in test, the closing line dropped, the clone
  rule, the frontmatter cut, the manifest's version, the review path,
  `HEADER`, `manifest`'s object test, `MISSING`, `CAP`, and `origin`'s
  no-repository answer.
- `hooks/core-start.py`: at `8c268944`, five mutants, three red and two
  survived. The survivors are the two guards the paragraph above
  removed. At `2662b961`, four mutants, all red. Their targets: the catch
  narrowed to `KeyboardInterrupt`, `CLAUDE_PLUGIN_ROOT` ignored, `if
  text:` made `if True:`, and the payload read replaced.
- `skills/verify/scripts/payload_meter.py`, at `8c268944`: four mutants,
  all red. Their targets: `HOOK_ROW`'s text, the `missing` branch, the
  counted text cut to below the header, and `_core`'s path.
- `tests/lib/test_launch.py#hooked`: at `2662b961`, `start = set()` went
  red and the prefix test survived. At `ebd9c215`, with the prefix test
  gone, the prefix strip removed went red. The `py -3` branch was removed
  at `2662b961` with no run of its own: the hardening case holds both
  halves to one script, so the branch could add no path.

No unit of this phase is only renamed or moved, so no census of old
spellings is owed.

**What phase 2 meets.** From this phase's commits on, the tree states two
facts that phase 2's files still contradict. Both are listed in
`frame/design.md` *Scope* item 2 and `## Removes`, and this phase did not
write them:

- The "registers no hook" sentences: `README.md:50,297`,
  `CONTRIBUTING.md:450`, `SECURITY.md:25`, `docs/checks/the-stamp.md:14`,
  `docs/running/measuring-a-run.md:135,138`, `skills/update/SKILL.md:214`,
  `skills/verify/scripts/seal_stamp.py:59,1513`,
  `skills/verify/scripts/session_cost.py:3104`,
  `tests/behaviour/test_chain_hooks_hardening.py:447`,
  `tests/behaviour/test_first_setup_asks_once.py:283`,
  `tests/behaviour/test_release_hygiene.py:1134`, and
  `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:219,228,236`.
  The hardening case's line moved from `:407` to `:447` because its
  docstring grew.
- The floor set's lists that do not name the hook scripts:
  `CONTRIBUTING.md:118-119`, `lib/launch.py:35-37` and
  `tests/censuses.py:892`.

The sentences that say `/agentic:start` opens the core are phase 3's, at
the coordinates *Scope* item 3 lists.

**The phase's scoped run.** One command, `bin/test <89 modules>
tests/text/ -q`. The 89 modules are every test module that names a path
this phase changed, or reads `git ls-files`, `os.walk` or `glob(` over the
tree, together with the plan row's modules. It ran over `24e29ed1` with
this record, `gaps.md` and the Status cell in the working tree, which is
the content of the commit that adds them. The run gave 3543 passed, 8
skipped and 1 failed. The failure is
`tests/text/test_a_cited_commit_outlives_the_squash.py#test_every_cited_commit_outlives_the_squash`
on `frame/plan.md:9`, the frame's citation above, and that line is its
only hit. A run at `ebd9c215`, before `gaps.md` stood, also failed
`test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which `gaps.md` answers. `seal rules --check` and `seal layout --check`
both exit 0. `git ls-files hooks/` lists `hooks/core-start.py` and
`hooks/hooks.json`.
