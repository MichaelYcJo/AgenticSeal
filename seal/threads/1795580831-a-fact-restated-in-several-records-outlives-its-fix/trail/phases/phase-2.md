# Phase 2: 1795580831-a-fact-restated-in-several-records-outlives-its-fix

## What this phase found

**The frame holds against the tree.** The coordinates `frame/plan.md` *Technical context* gives for this phase stood at `496803609`: `hooks/ask-under-automation.py` and `hooks/core-start.py` as the pattern, `tests/hooks/test_ask_under_automation.py` running its command through `tests/hooks/test_core_start.py#start`, and `tests/behaviour/test_chain_hooks_hardening.py#HOOK_ENTRIES` and `#HOOK_FILES` as the registry. The statements of the hooks that `frame/design.md` G17 lists stood where it says. `lib/optin.py#marked` reads a root's marker, so the hook calls it and copies no marker comparison.

**The script is `hooks/edit-leaves-copies.py`.** It is named in the shape of the two beside it, a kebab-case phrase of what happens: `core-start`, `ask-under-automation`.

**A record that cannot be read silences the whole hook.** `frame/design.md` *Data & interfaces* says the hook "prints nothing where the payload, the path, the root or a file cannot be read". The phase read "a file" as any file of the set it searches, so one record that is not UTF-8 text stops the print for every place. The other reading, which skips that file and names the rest, was not built. Judged against that paragraph, and against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a reading guessed from words is reported, never used to block, and a silence costs one copy the next round can find.

**Three decisions the frame left open.** Judged against `frame/design.md` *Data & interfaces*, which bounds the text under G15's 10,000 characters and says nothing of the three:

- A `file_path` that is not absolute prints nothing. The harness hands an absolute path, and a relative one would resolve against whatever directory the hook process runs in.
- A span is shown beside its place cut after `SHOWN` characters, 240, with ` ...`. An edit that replaces a long passage would otherwise spend the limit on one place.
- Places past the limit are counted on one line, `- and <n> more places, not listed`, and the closing sentence on what the writer does still stands.

**The spans come from `old_string` alone, as the frame states.** So an edit whose `old_string` holds few words beyond the change prints nothing: in the timing run below, a change at the end of `old_string` gave a span of five words and no print. G7's replay took its three words of context from the file's old text, not from `old_string`, so it found copies this hook does not find. Reading the context from the edited file was not built, because the frame reads `old_string` and a `replace_all` edit gives several places to read it from.

**Five guards went, because another guard or the catch-all raise held each.** Reading each condition for what it alone refuses showed three. `len(rel) >= 2` in `#_located`: the `.md` check refuses the empty path it guarded. The `isinstance` checks of `tool_input` and its fields in `#main`: a field of another type raises at its first use, or names no record, and the raise prints nothing. `joined not in kept` in `#_spans`: `#_places` removes the duplicate through `set`. `f6f528bb1` removed them and the sort of `#_records`, which `#_places`'s sort already gave. Mutants 8 and 28 of the batch below survived and showed two more: the directory pruning in `#_records`, since the file filter already drops every record under `trail/`, and `if not spans: return` in `#main`, since an empty span list yields no place. `e480f342c` removed both.

**The README case reads the fourth hook too.** `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#README_FACTS` gained `` `PostToolUse` `` and `` `hooks/edit-leaves-copies.py` ``, beside the facts of the other three hooks, so each edition's section is held to name the hook (contract rule 14). `frame/design.md` *Scope* item 12 names the prose and no case.

**The hook's wall time is a probe, not a case.** `frame/questions.md` Q1's answer says phase 2's cases measure it. A case that asserts a time fails on a slow runner and passes on a fast one, whatever the hook does, so the phase measured it once instead (executed): `test_tmp_hook_time.py` under this phase's scratch directory ran the hook's script five times on an edit of this work item's `frame/design.md` that replaced "next round" with "following round" in a sentence of *Data & interfaces*. It took 0.032 s to 0.037 s a run, against 0.017 s to 0.018 s for `python3 -I -c pass`, and printed `frame/design.md` line 93, where the sentence still stood since no edit had landed. Its first run used a change at the end of `old_string`, printed nothing for the reason the paragraph on spans gives, and the probe was changed and run again.

**Seen red, before the code.** The cases ran against a stub `hooks/edit-leaves-copies.py` that printed nothing, with `hooks/hooks.json`'s entry already in place: `bin/test -q -p no:xdist tests/hooks/test_edit_leaves_copies.py` failed 8 of 14. The six cases that print a place failed at `json.loads` on an empty stdout. The case of another payload's shape failed on its last line, which asserts that the unchanged payload prints. The census failed on the stub's `__main__` block. The six cases that assert nothing is printed passed there, as such cases do, and take their red from the guards' mutants below (contract rule 15). The cases added at `f6f528bb1` (an edit that changes only whitespace, an item directory outside `threads/`, a copy in a file that is not `.md`, an edited file that is not there, and a span cut at `SHOWN`) were written after the code and take their red from mutants 11, 2, 9 and 27 of the batch below, and the cut from 22 and 13. Each of those mutants was run again alone at `a09121619` under `-k` naming its one case, and each case failed. The README case failed on `` `PostToolUse` `` before either edition was edited.

**Mutation.** `seal mutate hooks/edit-leaves-copies.py`, one batch at `f6f528bb1`, with `--tests "bin/test -q -x -p no:xdist tests/hooks/test_edit_leaves_copies.py"`:

| # | Replace | Verdict |
|---|---|---|
| 1 | `if not os.path.isabs(path):` with `if False:` | red |
| 2 | `if os.path.basename(parent) == optin.WORK_ITEMS and` with `if True and` | red |
| 3 | `optin.marked(` with `bool(` | red |
| 4 | `if inner.endswith(".md") and _read(inner):` with `if _read(inner):` | red |
| 5 | the same with `if inner.endswith(".md"):` | red |
| 6 | `#_read`'s `rel.split("/", 1)[0] != TRAIL and rel != GUARANTEE` with `rel != GUARANTEE` | red |
| 7 | the same with `rel.split("/", 1)[0] != TRAIL` | red |
| 8 | `dirs[:] = [d for d in dirs if _read(prefix + d)]` with `dirs[:] = dirs` | survived; the pruning went in `e480f342c` |
| 9 | `if name.endswith(".md") and _read(prefix + name):` with `if _read(prefix + name):` | red |
| 10 | the same with `if name.endswith(".md"):` | red |
| 11 | `if tag == "equal":` with `if False:` | red |
| 12 | `AROUND = 3` with `AROUND = 2` | red |
| 13 | `words[max(0, start - AROUND) : end + AROUND]` with `words[start - AROUND : end + AROUND]` | red |
| 14 | `len(span) >= MIN_WORDS` with `len(span) > MIN_WORDS` | red |
| 15 | `len(joined) >= MIN_CHARS` with `len(joined) > MIN_CHARS` | red |
| 16 | the floor's condition with `len(joined) >= MIN_CHARS` alone | red |
| 17 | the floor's condition with `len(span) >= MIN_WORDS` alone | red |
| 18 | `collapsed = " ".join(text.split())` with `collapsed = text` | red |
| 19 | `lines[collapsed.count(" ", 0, at)]` with `lines[0]` | red |
| 20 | `at = collapsed.find(span, at + 1)` with `at = -1` | red |
| 21 | `return sorted(set(places))` with `return places` | red |
| 22 | the cut at `SHOWN` with `shown = span` | red |
| 23 | `if len(entry) + 1 > room:` with `if False:` | red |
| 24 | `room -= len(entry) + 1` with `room -= 0` | red |
| 25 | the room's reserve of 100 characters taken out | red |
| 26 | `if payload.get("tool_name") != "Edit":` with `if False:` | red |
| 27 | the check that the edited file is there with `if False:` | red |
| 28 | `if not spans:` with `if False:` | survived; the early return went in `e480f342c` |
| 29 | `"hookEventName": "PostToolUse",` with `"PreToolUse"` | red |
| 30 | `RULE`'s value with `"rule 19"` | red |

At `e480f342c`, a second batch broke the reshaped units: the file filter's `.md` check, `if not places:` with `if False:`, and the walk's `files` with `files[:0]`. Each was red. `seal mutate hooks/hooks.json` replaced the entry's matcher `Edit` with `Write`, and in a second mutant dropped the command's ` || exit 0`, under `bin/test -q -x -p no:xdist tests/behaviour/test_chain_hooks_hardening.py -k registers_its_hooks`; both were red. `seal mutate README.md` replaced `` runs `hooks/edit-leaves-copies.py`. Where `` with `runs its script. Where` under the README case, and was red. On `README.ko.md`, removing `` **`PostToolUse`** `` from the item survived, since the section's sentence on what goes into the session's context still names `` `PostToolUse` ``. Replacing `` `hooks/edit-leaves-copies.py` 를 돌립니다 `` with `스크립트를 돌립니다`, the script's one occurrence in that section, was red. The case reads each fact anywhere in the section, so a fact stated twice in it is held once.

**Other statements of the hooks the plugin ships, a sample.** `git grep -n -i -E "three hooks|four hooks|훅 세|훅 네|plugin ships .{0,20}hook|PreToolUse"` outside `seal/threads` printed, beside the passages this phase rewrote: `docs/running/measuring-a-run.md:140`, which says "the plugin's two hooks" and stands in the policy root, where `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/design.md` `## Rule changes` rewrites it to cite `README.md` *What runs on your machine* with no count, which holds with four; `skills/implement/orchestration.md:307` and `lib/routing.py`, which state the `PreToolUse` hook alone and stay true; and `tests/behaviour/test_chain_hooks_hardening.py:451`, a docstring listing the hooks that reach no network, which `a09121619` rewrote. A statement of the hooks in other words stands outside the search. The read of the range against HEAD found that the README editions, `CONTRIBUTING.md`, the hook's opening line and its cases' opening line each said the hook searches the item's "other" records, where it searches the edited file too; `a09121619` rewrote each.

**The phase-boundary set.** It is `tests/text` and `tests/behaviour`, which hold the tree-wide files `CONTRIBUTING.md` *The test layout* names and the two other files of the plan row, `tests/hooks`, and `tests/skills/test_seal_stamp.py`, which reads `hooks/hooks.json`'s `Stop` entry. The other test files that `git grep` lists as naming `hooks/hooks.json`, `README.md`, `SECURITY.md`, `CONTRIBUTING.md` or `skills/code-review/orchestration.md` write those names into fixtures or docstrings and read none of them. The command:

```
bin/test -q tests/text tests/behaviour tests/hooks tests/skills/test_seal_stamp.py
```

It exited 0 with 1119 passed and 9 skipped, at `a09121619` with this record, `gaps.md`, `changelog.md` and the Status cell in the working tree. Its first run, at `e480f342c`, failed two cases: `tests/behaviour/test_docs_line_wrap.py` on a README line past the wrap, and `tests/behaviour/test_this_repository_passes_its_own_checks.py`, because `seal layout --check` wants each class's cases named `test_accepts_` and `test_refuses_`. `b5bc887fe` renamed the cases and rewrapped the line.
