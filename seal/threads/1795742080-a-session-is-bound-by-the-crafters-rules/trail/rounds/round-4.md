# Review round 4: 1795742080-a-session-is-bound-by-the-crafters-rules

```seal
target: 5a5e5b1d4, fixes f725c0b24..5a5e5b1d4
```

This round verifies the fix for round 3. The range `f725c0b24..5a5e5b1d4` holds the round commit `1229e106a`, the crafter's fix `89e4f4841`, the close block `e1f7903a5` and the orchestrator's *Judgments of the run* row `5a5e5b1d4`. The range holds no merge (executed, `git log --merges`). `git diff --stat f725c0b24..5a5e5b1d4` names `lib/gitcmd.py`, `skills/implement/scripts/range_read.py`, `frame/plan.md` and `trail/rounds/round-3.md` (executed). The code reviewed is `89e4f4841`: a paragraph of `lib/gitcmd.py`'s docstring at `:54-61` and the comments at `range_read.py:131-132` and `:416-418`. The round read outside the fix range only where the fix reaches: `docs/running/what-a-script-gates.md:24-45`, which the orchestrator's row judges, and the `## Rule changes` of `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md`, the one unsettled design that names the same section.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md` whole at `5a5e5b1d4`, in a clone at that commit. The commit language and the record language are both English (read, `seal/config.json`), so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared.

Carried from round 3 and not established again: what git does with `diff.ignoreSubmodules` and with a `.gitmodules` entry's `ignore` on `diff --raw` and on `status` (round 3 `## Probes` row 1), and that each flag is pinned by a case seen red with only that flag removed (round 3 rows 2 and 3). The fix changes no code line, so neither check has a reason to fail. Established again at this target: the evidence search of round 3's finding, the narrow set, and each claim of the close block and of the orchestrator's row.

The claims weighed. The close says `lib/gitcmd.py`'s docstring gains round 3's paragraph after the sentence on `core.quotePath`. `lib/gitcmd.py:54-61` holds it as given (read). It says the two comments of `range_read.py` are replaced by round 3's comments. `:131-132` and `:416-418` hold them (read). It says the evidence search prints `lib/gitcmd.py:55`, `:58` and `:59`, and `range_read.py:131`, `:139`, `:416` and `:426`. The search, run again, prints those seven lines and no others (executed). It says the commit adds no behaviour and owes no `seal mutate` run and no case. `git show 89e4f4841` changes docstring and comment lines alone, so that holds (executed). The flag's behaviour stays held by `test_accepts_a_submodule_by_name_and_does_not_print_it` and `test_accepts_an_uncommitted_submodule_named_as_not_read`, which round 3 saw red with each flag removed (carried).

The orchestrator's row at `frame/plan.md:82` claims that `docs/running/what-a-script-gates.md` "states nothing the docstring contradicts". `docs/running/what-a-script-gates.md:30-31` says "`argv` sets each key measured to do that with `-c`". `lib/gitcmd.py:54-61` now names `diff.ignoreSubmodules` as a key measured to take a submodule's path out, and as one `argv` does not set. The claim does not hold, and finding 1 says why. The row also quotes the policy as saying "a `-c` key found later is added to the docstring". `:34-35` says "a key or subcommand found later is added there and nowhere else" (read).

`chain_check.py --worktree` printed no notice at a line of `frame/design.md` naming a test pin or a copy (executed).

## Findings

### 1. `docs/running/what-a-script-gates.md` says `argv` sets each measured key with `-c`, the work now holds a measured key by a flag, and `frame/design.md` states no rule change for it

```seal
severity: should
location: `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md:128-143`, `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/plan.md:82`, `docs/running/what-a-script-gates.md:30-35`
evidence: read `docs/running/what-a-script-gates.md:24-45`, `lib/gitcmd.py:30-61`, `lib/gitcmd.py:83-89`, `skills/implement/SKILL.md:63`, `skills/implement/orchestration.md:83-101`, `skills/settle/rule-changes.md:9-60`, `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md` `## Rule changes`; executed `git grep -n -F -e 'key measured' -e 'keys measured' -e 'nobody has measured' -e 'gitcmd.py#argv' -- ':!seal/threads'` and `git grep -n "section: Which gate" -- 'seal/threads/*/frame/design.md'` in a clone at `5a5e5b1d4`
regression: round-3#1
```

Why it matters: the section *Which gate a script holds* is the rule a review reads a git call against ("Whether a call is one of these is read at review", `:44`). It says at `:30-31` that `argv` "sets each key measured to do that with `-c`", where "that" includes taking a commit's paths out. `lib/gitcmd.py#KEYS` (`:83-89`) does not hold `diff.ignoreSubmodules`, and `lib/gitcmd.py:54-61` says the key takes a submodule's path out and that a script passes `--ignore-submodules=none` for it. A reviewer who reads the next script that lists a diff's paths against the policy finds the call built by `argv` and passes it. That is the defect round 3 found in the docstring, now one level up. The settle writes only the sections the released designs' `## Rule changes` name (`skills/settle/rule-changes.md` *Rule changes*). This design names *The checks* alone (`frame/design.md:128-143`), and the one other unsettled design that names *Which gate a script holds* changes its bold lead and leaves `:30-35` as it stands (read). So no settle ever corrects the sentence.

The grounds. The unit is the paragraph of `lib/gitcmd.py:54-61`, which `89e4f4841` wrote for round 3's finding, together with the flag in `DIFF` and in `_uncommitted` that round 2's fix wrote. *Data & interfaces* of `frame/design.md:119` has the script start git through `lib/gitcmd.py#git` "as `docs/running/what-a-script-gates.md` *Which gate a script holds* asks", and the frame states no change to that section. The fixes held a measured key by a flag the section does not name. The defect came from there. Round 3's paste-ready fix wrote the paragraph and did not weigh the section's sentence, so the omission stands in round 3's fix as much as in the pass that applied it. `skills/implement/SKILL.md:63` says "A work item whose subject is the code states the rules its work changes in `## Rule changes`". Before this work no run had measured the key, so the section's `:43` made it a limit, and the sentence at `:30-31` held. This work measured it in rounds 2 and 3 and chose a flag, so the work changes what the sentence states.

The orchestrator's row gives two grounds for writing no entry. The first is that the docstring is the fact's one home. The section does not only point at the docstring. It states the mechanism itself, and that statement is now false. The second is that an entry "would widen the frame after a fix, which a fold whose source is a fix does not do". `skills/implement/orchestration.md:90-96` bounds the orchestrator's fold of a statement a crafter's hand-back names. It gives "the framer's" fold "of a round finding that says a frame sentence no longer holds", and this finding is that. Round 1's finding 1 widened the frame the same way, by *Scope* item 11 (`frame/plan.md:80`).

The search printed `docs/running/what-a-script-gates.md:31` and `:43`, and four lines outside the fact (`docs/releasing/release-checklist.md:340`, `skills/implement/scripts/range_read.py:66`, `tests/github/test_publish_release_note.py:130` and `tests/skills/test_broad_gate.py:2254`). It did not print `lib/gitcmd.py:33-35`, which states the same sentence across a line break. There the docstring's own paragraph at `:54-61` gives the exception, so that statement is not left false. The search is a sample under contract rules 12 and 19, since a statement in other words escapes it.

The fix. The framer folds one operation into `frame/design.md` `## Rule changes`, after the last item. The section is `Which gate a script holds`, and `docs/README.md` names no `.ko.md` edition for the file (carried from `frame/design.md` G15). The `to` names the docstring as the home of each setting and its flag, and restates neither the setting nor the flag:

```text
- change
  file: docs/running/what-a-script-gates.md
  section: Which gate a script holds
  from: `argv` sets each key measured to do that with `-c`, which outranks
    every configuration file. Its docstring names each key, what it changes
    and the subcommands it changes, and a key or subcommand found later is
    added there and nowhere else.
  to: `argv` sets each key measured to do that with `-c`, which outranks
    every configuration file. A setting measured to do it that no `-c` key
    reaches, such as one a file of the repository carries, is held by a flag
    on each command it reshapes. `lib/gitcmd.py`'s docstring names each key,
    and each such setting with its flag, with what it changes and the
    subcommands it changes, and one found later is added there and nowhere
    else.
```

The orchestrator rewrites its row at `frame/plan.md:82` in place, since its ground and its quote of the policy are what this finding contradicts:

```text
| 2026-11-27 | Round 3 holds one `should` finding, which the crafter's fix pass answers at `89e4f4841` in `lib/gitcmd.py`'s docstring and two comments of `range_read.py`. The pass names `docs/running/what-a-script-gates.md` *Which gate a script holds* as saying less than that docstring now does: it says that a key or subcommand found later is added to the docstring, and not that a setting no `-c` key reaches is named there with its flag. Round 4 finds that the section's sentence "`argv` sets each key measured to do that with `-c`" no longer holds once the work holds `diff.ignoreSubmodules` by a flag, and the framer folds a `change` of that section into `frame/design.md` `## Rule changes` | A work item whose subject is the code states the rules its work changes in its design, and a round finding that says the frame no longer holds is the framer's fold | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*; `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **The framer writes a decision's fold** |
```

The fix crosses no OS boundary and changes no code. `docs/running/what-a-script-gates.md` is the policy root, which this work item writes only through the settle, so the fix leaves that file as it stands.

## Confirmations

```seal
confirms: round-3#1
```
What holds: `lib/gitcmd.py:54-61` names `diff.ignoreSubmodules` and the `ignore` of a `.gitmodules` entry, what each takes out of `diff` and `status`, that `-c diff.ignoreSubmodules=none` does not reach the `.gitmodules` entry, and the flag a script passes, citing `range_read.py#DIFF` and `#_uncommitted` (read). Both comments of `range_read.py` cite the module and no longer give the reason (read). The finding's evidence search, run again, prints `lib/gitcmd.py:55`, `:58` and `:59` beside the four lines of `range_read.py` (executed). The next script that lists a diff's or a status's paths, written against the module, now finds the setting there. Finding 1 of this round is a regression in the policy section that the paragraph now departs from, and it leaves the docstring as round 3's finding asked.

What matched: the paragraph against the tree. "as `skills/implement/scripts/range_read.py#DIFF` and `#_uncommitted` do" names two names the script defines, at `:133` and `:413`, and each passes the flag (`:139`, `:426`) (read). The paragraph states the rule a script follows, "passes `--ignore-submodules=none` on each such command", and no count of the scripts that follow it. The earlier paragraph's "The subcommands these keys change are `log` and `status`" speaks of the keys of `KEYS`, so `diff` named in the new paragraph does not contradict it (read).

What matched: the records against the fix. `changelog.md`, `gaps.md`, *Scope* item 11, S6 and *Data & interfaces* state what the command names and not which setting or flag holds it, so the fix leaves each true (read). `gaps.md:7` still labels the suite `unverified` with the orchestrator as its answerer, so the label is honest.

What matched: the narrow set, run once in the clone at `5a5e5b1d4`: `bin/test tests/lib/test_gitcmd.py tests/skills/test_range_read.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py -q` gave 246 passed and 9 skipped, exit 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether other scripts that list a diff's or a status's paths drop a submodule under the two settings, such as `skills/code-review/scripts/chain_check.py:401` and `:409`, carried from rounds 2 and 3 and not judged again | outside the fix range | the orchestrator, which decides whether to file it |
| The oldest git the plugin supports, carried from round 3 | `skills/implement/scripts/range_read.py:133-140`, `:420-428` | the orchestrator, with the owner if a floor is to be stated |
| Whether step 1's sentence on contract rules 4 and 5 needs a count of its own, carried from round 1 and not judged again | `skills/implement/orchestration.md:36-40`, `seal/follow-up.md:48` | the orchestrator, with the framer at the fold |
| `seal range` on Windows | `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/gaps.md:8` | CI's Windows leg |
| The full suite, the repository-wide lint and the format check | the work item's tree | the orchestrator, at the broad run once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git grep -n -F -e 'ignoreSubmodules' -e 'ignore-submodules' -- lib skills .github hooks docs`, in the clone at `5a5e5b1d4` | `lib/gitcmd.py:55`, `:58`, `:59`; `skills/implement/scripts/range_read.py:131`, `:139`, `:416`, `:426` |
| `git grep -n -F -e 'key measured' -e 'keys measured' -e 'nobody has measured' -e 'gitcmd.py#argv' -- ':!seal/threads'`, same clone | `docs/releasing/release-checklist.md:340`, `docs/running/what-a-script-gates.md:31`, `:43`, `skills/implement/scripts/range_read.py:66`, `tests/github/test_publish_release_note.py:130`, `tests/skills/test_broad_gate.py:2254` |
| `git grep -n "section: Which gate" -- 'seal/threads/*/frame/design.md'`, same clone | `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md:124`, `:137` |
| `bin/test tests/lib/test_gitcmd.py tests/skills/test_range_read.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py -q`, same clone | 246 passed, 9 skipped, exit 0 |
