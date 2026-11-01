# Review round 2: 1793538230-code-text-brought-to-the-tree

```seal
target: afde315b, fixes c2535dcd..afde315b
```

This is a verifying round. Its target is the diff of round 1's fixes, `c2535dcd..afde315b`: the orchestrator's fold in 1ac8b651 (`frame/design.md` *Scope* 4 and a row of `frame/plan.md` *Judgments of the run*), the fix pass's 18bbd105 (`hooks/lib/console.py`'s docstring and `changelog.md`), and the close block in afde315b. The round worked in a `git clone --no-local` of the worktree under the session's scratch directory, checked out at `afde315b`. No `seal/parity.md` is declared, so the record carries no `original:` line. `seal/config.md` has no `Record language` row, so the record is in English.

Carried from round 1 and not re-derived: the reasons the docstring gives for `.github/scripts/release_report.py`, `.github/scripts/release_seal.py`, `.github/scripts/rules.py` and `hooks/dispatch.py` (round 1's sixth confirmation), since lines 52-56 of the docstring are unchanged by the fix apart from "This command lists them" becoming "This command lists every place that spells the loop"; and the issue's scope for #1255 as `frame/design.md` *Out* states it, which this round read again only to set it beside the new sentence. Re-derived: which of the 14 scripts under `skills/*/scripts/` reach `hooks/lib/`, what each of their loops says above it, and whether the listing command lists every place that spells the loop.

The axes walked are the claims of the rewritten paragraph, one sentence at a time, against the code each names; the changelog fragment's restatement of those claims; the orchestrator's fold against the section it cites; and the spawn prompt's question, whether `trail/phases/phase-2.md` decision 2 may stand as written.

## Findings

### 1. The console docstring says no script under `skills/*/scripts/` states why it copies the loop, and `chain_check.py` states one

```seal
severity: should
location: `hooks/lib/console.py:50-51`, `skills/code-review/scripts/chain_check.py:108-110`, `skills/code-review/scripts/chain_check.py:230-242`, `seal/threads/1793538230-code-text-brought-to-the-tree/changelog.md:4`, `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:28`
evidence: executed `for f in $(git grep -l "[.]reconfigure(" -- 'skills/*.py'); do n=$(grep -n "[.]reconfigure(" $f | head -1 | cut -d: -f1); sed -n "$((n-14)),$((n+1))p" $f; done`, `sed -n 200,250p skills/code-review/scripts/chain_check.py`
regression: round-1#1
```

The unit is `hooks/lib/console.py`'s module docstring, lines 46-51, which 18bbd105 rewrote. The frame, as the orchestrator folded it in 1ac8b651, says at `frame/design.md:28` that the scripts under `skills/*/scripts/` keep their copies with "no stated reason". The fix wrote that as "None of them says why it copies the loop rather than loading this module the same way" (`hooks/lib/console.py:50-51`). The sentence came from round 1's paste-ready text, and neither the fold nor the fix pass read the comment above each of the 14 loops.

Why it matters: the paragraph is what #1255 will read to learn why each copy exists, and this sentence tells it that no script under `skills/` has a reason to keep its copy. `skills/code-review/scripts/chain_check.py:108-110` runs its loop first in the file, under the comment "Before the readers load below: a refusal printed at import must not meet a console's code page." The readers are loaded at import in a `try` (`chain_check.py:230-242`): a reader that will not load ends the run at exit 2 with "chain-check: the shared reader would not load", and the exception text can carry a path. Loading `hooks/lib/console.py` by path would be one more such load, and if it failed, that refusal would print before the streams were set. That is the constraint the comment states, and it is the same kind of reason the docstring accepts from the three release scripts at lines 52-55: a module that will not load must end in the script's own named result. A session that takes the docstring's word could move `chain_check.py` onto a load of this module and open the gap its comment closes. The other 13 loops were read: `seal.py`, `settle.py`, `deferral_check.py`, `session_cost.py`, `unverified_check.py`, `seal_stamp.py` and `arm_check.py` say that `hooks/lib/console.py` owns the reasoning; `fold_check.py` says "as every other shipped script does"; `pr_body.py` says why the streams need the loop; `broad_gate.py` and `seal_stamp.py` say why the loop comes after a question asked of stdout; `core_check.py`, `pact_check.py` and `payload_meter.py` carry no comment. None of those 13 gives a reason for copying rather than loading, so the sentence holds for them. The changelog fragment repeats the claim ("none states a reason", `changelog.md:4`).

The fix replaces lines 50-51 of `hooks/lib/console.py` and keeps the rest of the paragraph:

```text
`skills/code-review/scripts/chain_check.py` runs its loop before it loads
any of them, so that the refusal it prints when one will not load does not
meet a console's code page, and a load of this module would be one more
load that can fail first. None of the others says why it copies the loop
rather than loading this module the same way. Which entry points owe the
answer is #1255's.
```

The changelog fragment's second bullet changes "and none states a reason" to "and only `skills/code-review/scripts/chain_check.py` states one, that its loop must run before anything it loads". The frame's parenthesis at `frame/design.md:28` is the orchestrator's to fold the same way.

```seal
verdict: fixed bbf80a99
answer: The finding holds: `skills/code-review/scripts/chain_check.py:108-110` runs its loop under "Before the readers load below: a refusal printed at import must not meet a console's code page", and its readers load at import in the `try` at lines 230-242 (read). The paste-ready text was read against the module docstring it lands in: "them" in "before it loads any of them" points back to the `hooks/lib/` modules of the sentence before, and "the others" to the other scripts under `skills/*/scripts/`, so it went in as written in place of "None of them says why ... #1255's". The changelog fragment's second bullet now says only `chain_check.py` states a reason, that its loop must run before anything it loads. The frame's parenthetical was re-folded by the orchestrator in 3e81b425, and this pass did not edit the frame. `uvx ruff format --check`, `uvx ruff check` and an import under `python3 -W error` passed on `hooks/lib/console.py`, and `bin/test` over `tests/hooks/test_console.py`, `tests/test_censuses.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_one_word_one_meaning.py`, `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` and `tests/behaviour/test_docs_line_wrap.py` gave 341 passed and 8 skipped (executed). The old sentence still stands in round 1's close block and paste-ready text, and in the 1ac8b651 row of `frame/plan.md` *Judgments of the run*; each is a record of what was decided then, and this pass edits neither.
```

### 2. The console docstring hands "which of them owes the import" to #1255, and #1255 holds which entry points owe the answer, not whether they import it

```seal
severity: should
location: `hooks/lib/console.py:51`, `seal/threads/1793538230-code-text-brought-to-the-tree/changelog.md:4`, `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:28`
evidence: executed `gh issue view 1255 --json title,state,body`
regression: round-1#1
```

The unit is the same docstring, line 51, which 18bbd105 wrote. The frame's *Out* item names #1255 as the issue "which decides which entry points owe the answer", and the fold at `frame/design.md:28` turned that into "which owe the import is #1255's". The fix wrote the fold's words: "which of them owes the import is #1255's" (`hooks/lib/console.py:51`). The words came from round 1's paste-ready text, and nobody opened #1255 to see whether it holds that question.

Why it matters: #1255 is open, and its body widens `tests/censuses.py#entry_point` to every `__main__` of shipped code. It refuses an entry point whose answer is not `STREAMS`' answer, or that gives no answer, and it lets an entry point that owes no answer carry its reason at its line. Its *Done when* is that "every entry point gives `STREAMS`' answer or carries its reason". Nothing in it asks whether an entry point that gives the answer should import `hooks/lib/console.py` instead of copying the loop. So the docstring sends a reader to a home that does not hold the question, and #1255's frame has no reason to take it up. The changelog fragment repeats the hand-off ("leaves which of them should import the module to #1255", `changelog.md:4`). Contract rule 4 asks that what is left open names who answers it, and a named home that does not hold the question answers nobody.

The fix says what #1255 holds. The replacement text in finding 1 ends with "Which entry points owe the answer is #1255's", which is this fix too. The changelog fragment's last clause becomes "and leaves which entry points owe the answer to #1255". If the orchestrator wants the import question owned, it adds it to #1255 (an agent posts nothing); then the docstring may name #1255 for it.

```text
Which entry points owe the answer is #1255's.
```

```seal
verdict: fixed bbf80a99
answer: The finding holds as the round measured it; this pass did not reopen #1255 and relies on the round's executed `gh issue view 1255` for what its body holds. The docstring's last sentence on the skill scripts now reads "Which entry points owe the answer is #1255's.", the round's text, and the changelog fragment's last clause now reads "and leaves which entry points owe the answer to #1255". `git grep -n -i -E "owes? the import|import is #1255|should import the module"` over the tree finds those words only under `seal/threads/`, in round 1's records, the 1ac8b651 row of `frame/plan.md` *Judgments of the run* and this round's own text (executed). The frame was re-folded by the orchestrator in 3e81b425 and was not edited here. Whether the import question gets an owner by being added to #1255 is the orchestrator's, as the round's *Not judged* table says.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the false reason is gone. `hooks/lib/console.py:46-49` no longer says the scripts under `skills/*/scripts/` are standalone by design, and `git grep -n -i "standalone by design"` finds the phrase only under `seal/threads/` (executed). The new claim that most of these scripts reach `hooks/lib/` holds. Of the 14 the listing command names under `skills/`, 11 reach it. `skills/implement/scripts/seal.py:237-242` refuses when a module is missing and then inserts `hooks/lib/` into `sys.path` and imports four modules. `chain_check.py`, `core_check.py`, `unverified_check.py`, `fold_check.py`, `settle.py`, `pact_check.py`, `broad_gate.py` and `payload_meter.py` load modules by path, and `pr_body.py` and `seal_stamp.py` load them through `chain_check.py`. `arm_check.py`, `deferral_check.py` and `session_cost.py` hold no `spec_from_file_location`, `sys.path.insert`, `import_module` or `runpy` (executed, `## Probes`). The fix pass's count, 11 and 3, matches. Round 1 counted 9 because its search did not follow a load through a sibling script. The removed sentence "A copied loop is cheaper than the machinery that would avoid it" is stated nowhere else in the tree, and neither is "copied loop" (executed). "What must not diverge is the ANSWER" stays, as *Scope* 4 asks. The module imports under `python3 -W error`, and the four test modules that read it or every tracked file passed (executed, `## Probes`). Findings 1 and 2 are new defects in the sentence that replaced the old one, not the old defect standing.

```seal
confirms: none
```
What matched: the rewritten line "This command lists every place that spells the loop, with this file among them" (`hooks/lib/console.py:56-59`). `git grep -l "reconfigure"` and `git grep -l "[.]reconfigure("`, both over `*.py` outside `tests` and `evals/behaviour`, list the same 19 files (executed: `diff` of the two listings, exit 0). Every file that names `reconfigure` at all is one the command lists. A loop spelt without the word `reconfigure` is outside any search on words, and is the open part of that sample.

```seal
confirms: none
```
What matched: the orchestrator's fold in 1ac8b651. The new row of `frame/plan.md` *Judgments of the run* cites `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, which stands at line 25. That section says a decision made after the frame is committed is folded in place into `frame/design.md` or `plan.md`, with one row in *Judgments of the run* giving the decision, its grounds and the document (read). The row's grounds, `skills/implement/scripts/seal.py:238-242`, are the `sys.path` insert and the four imports (read). *Scope* 4 was rewritten where it stands and not beside it. The words the fold wrote are findings 1 and 2.

```seal
confirms: none
```
What matched: the spawn prompt asks whether `trail/phases/phase-2.md` decision 2 may still state "The scripts under `skills/*/scripts/` are standalone by design". It may. `skills/implement/SKILL.md:358` gives the phase record to the builder, as what building the phase found, written when the phase closes (read). The decision is phase 2's account of the premise it took, and round 1's finding 1 records that the premise was false, at the decision's own coordinate. The correction stands where the next readers look: `frame/design.md` *Scope* 4 and the *Judgments of the run* row that `seal settle` reads. No settle script reads `trail/phases/` (executed: `grep -n -i "phases"` over `skills/settle/SKILL.md` and `skills/settle/scripts/`, no line). The sealer reads the phase record as a claim against the tree and the rounds (`agents/sealer.md:78`). So nothing acts on the sentence as current guidance. Rewriting it would make phase 2's record say something phase 2 did not decide. Contract rule 19 governs text that states a fact, and this record states what a party took as fact at the time.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `afde315b`. `gaps.md` labels them unverified and names the orchestrator, and the fix pass changed no label, so the label is honest | the whole tree | the orchestrator, by `seal gate` once findings 1 and 2 are closed and a verifying round leaves nothing open |
| Whether the import question of finding 2 should be added to #1255 | #1255 | the orchestrator |
| Whether the new case passes on the Windows legs (`frame/questions.md` Q1), carried open from round 1 and outside this fix diff | `tests/hooks/test_console.py:102-128` | the pull request's Windows legs, read by the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'`, then for each file under `skills/` a `grep -nE` for `sys.path.insert`, `spec_from_file_location`, `_load_hook(`, `import_module`, `chain_check` and a `hooks/lib` path, and `grep -cE "spec_from_file_location\|sys\.path\.insert\|import_module\|runpy"` over `arm_check.py`, `deferral_check.py` and `session_cost.py` | 19 files, 14 under `skills/`; 11 of the 14 load `hooks/lib/` modules; the three counts are 0 |
| the 16 lines above each `skills/` script's first `.reconfigure(` | `chain_check.py:109-110` alone ties the loop's place to the loads that follow it |
| `diff` of `git grep -l "reconfigure"` and `git grep -l "[.]reconfigure("` over the same pathspec | no difference, exit 0 |
| `git grep -n -i "cheaper than the machinery\|standalone by design\|copied loop"` | lines under `seal/threads/` alone |
| `python3 -W error -c "import sys; sys.path.insert(0,'hooks/lib'); import console"` | `ok`, exit 0 |
| `bin/test tests/hooks/test_console.py tests/test_censuses.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_one_word_one_meaning.py -q -p no:xdist` | 252 passed, exit 0 |
| `gh issue view 1255 --json title,state,body` | open; the body decides which entry points owe `STREAMS`' answer and asks nothing about importing the module |
