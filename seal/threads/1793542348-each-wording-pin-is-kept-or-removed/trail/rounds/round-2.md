# Review round 2: 1793542348-each-wording-pin-is-kept-or-removed

```seal
target: 726ccee6, fixes 4134d5bf..726ccee6
```

This is a verifying round. Its target is the diff of round 1's fixes, `4134d5bf..726ccee6`: five commits that touch `changelog.md`, `frame/design.md`, `frame/plan.md` and the close blocks of `trail/rounds/round-1.md`, all under this work item's directory. The review was done in a `git clone --no-local` of the worktree at `726ccee6`. No `seal/parity.md` is declared (executed: `ls`), so no parity reading and no `original:` line are owed.

Carried from round 1, not re-established: the coordinate of the case that reads the cap's default count, `tests/behaviour/test_chain_hooks_hardening.py:898-911`, which this round opened at that coordinate; and round 1's reading that the three asserts held back under Scope item 9 are phrases kept for a `docs/` line, which this round re-read at their lines. Every verdict below was reached on the tree at `726ccee6`.

## Findings

### 1. The fragment's rewritten lead says the suite keeps only asserts that pin a fact, while four kept asserts pin a phrase of a rule

```seal
severity: should
location: `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/changelog.md:3`
evidence: read `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/changelog.md:3-4`, `tests/text/test_broad_gate_rule.py:62-68`, `tests/text/test_a_rider_reaches_its_file.py:85-88`, `tests/text/test_settle_reads_before_it_removes.py:54-60`, `tests/text/test_a_gate_that_fails_says_so.py:16-32`, `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/gaps.md:26-28`
reopens: round-1#2
```

Why the close does not hold: round 1's finding 2 was that the fragment promises more independence from a rule's wording than the build gives. Round 1 said that this finding concerns what the changelog says about the asserts held back under Scope item 9. The fix pass claimed that the bullet's bold lead "made the same claim" and now says the suite "keeps only the asserts on a rule's text that pin a fact a reader acts on". The tree says otherwise. Four kept asserts pin a phrase of a rule and no fact:

- `tests/text/test_broad_gate_rule.py:65`, `tests/text/test_a_rider_reaches_its_file.py:88` and the loop at `tests/text/test_settle_reads_before_it_removes.py:59-60` each carry the comment "A phrase of the rule, not a fact" (`:62`, `:85`, `:54`).
- `tests/text/test_a_gate_that_fails_says_so.py:25-28` asserts the bold sentence of `docs/the-session-hooks.md` *Registration* and has no comment. Scope item 7 keeps it whole.

The work item's other records already call these wording: `gaps.md:26` says "Phase 1 kept two asserts that pin wording", and #1277's title says #1233 "left one wording-pin module" (executed: `gh issue view 1277`). Why it matters: the release note now tells a maintainer that no kept assert across the 56 modules pins a rule's phrase. A maintainer who rewords `docs/the-broad-gate.md:42`'s rule, or the *Registration* lead, finds a case red that the note said was gone.

The same overclaim stands in two more sentences of the same bullet, found by taking the bullet apart sentence by sentence; that is the whole list for this fragment.

- "107 asserts stay, each with a comment above it naming the fact it pins and who reads that fact". This sentence is unchanged from round 1's target, but it is false for the same four: the gate's assert has no comment, and the other three comments say "not a fact".
- "its comment names the fact to keep", which the fix pass took from round 1's paste-ready text. The defect in that clause therefore came from round 1's own fix text, and not from the fix pass.

Bullet 4's last sentence names the four as staying, but it does not say that they pin a phrase. So the fragment as a whole never states it. The other records are right: `gaps.md:26-28`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md` each name their held-back assert as wording. A `git grep` for the comment's marker over `tests/` lists exactly the three Scope item 9 asserts (executed). The gate module is Scope item 7's one exception.

The fix rewrites these three sentences of `changelog.md:3` and leaves the rest of the bullet as it is. The bold lead:

```markdown
**Across the 56 modules #1237's measure listed, this repository's suite keeps the asserts on a rule's text that pin a fact a reader acts on, and keeps the few that pin a rule's phrase only until a follow-up issue moves the `docs/` lines that need them (#1233).**
```

The sentence that opens "107 asserts stay":

```markdown
107 asserts stay. Each carries a comment above it naming the fact it pins and who reads that fact: a citation a reader resolves, a command, flag or value a reader copies, a spelling a script or a parser matches, or a program's output. The exceptions pin a phrase of a rule, not a fact: the one assert of `tests/text/test_a_gate_that_fails_says_so.py`, which stays whole and carries no comment, and three asserts kept so that a `docs/` check line keeps a reader, whose comments say so.
```

The sentence that opens "A kept assert still matches its literal whole" keeps its text and gains one sentence after it:

```markdown
Rewording the phrase one of the exceptions pins turns it red as well, until the follow-up issue removes it.
```

```seal
verdict: fixed 9c0ec060
answer: The finding holds; the four asserts were read at their lines in the fix pass: the three comments open "A phrase of the rule, not a fact" at `tests/text/test_broad_gate_rule.py:62`, `tests/text/test_a_rider_reaches_its_file.py:85` and `tests/text/test_settle_reads_before_it_removes.py:54`, and `tests/text/test_a_gate_that_fails_says_so.py:25-28` asserts the *Registration* lead with no comment. 9c0ec060 rewrites the three sentences of `changelog.md:3` in my own words for the same facts. The lead says the suite keeps four asserts that pin a rule's phrase until a follow-up issue moves the `docs/` lines that need them. "107 asserts stay" now says 103 carry a comment naming a fact and its reader, and names the four with what each carries. The rewording sentence speaks of a kept assert that pins a fact, followed by the paste-ready sentence for the four. Each sentence was read against the four asserts before the commit. The paste-ready "Each carries a comment" was not taken, because it is false for the four the next sentence names. `grep` over the work item's records for "keeps only", "each with a comment", "every kept assert" and "names the fact to keep" lists only the rewritten lead and `trail/phases/phase-1.md:19`, whose "Every kept assert has its fact and its reader" is phase 1's record, which this pass does not write; its held-back assert's own comment says it pins a phrase (executed).
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the round-cap `change` now names the module whose case reads the cap's default count. `frame/design.md:104-107` reads `to: No person is asked mid-run.` followed by `check: tests/behaviour/test_chain_hooks_hardening.py`. This round confirmed it four ways:

- `rule_changes.py#parse` over the design at `726ccee6` returns both `change` items with `errors=[]` and `unread=[]`. Each `from` stands once in its section. After the `to` is applied, the new check line's target is a file of the tree, and the `to` stands once (executed, *Probes* row 1).
- `tests/behaviour/test_chain_hooks_hardening.py:908` asserts "three finding rounds by default" over the flattened `docs/the-review-record.md`. That literal stands once in the file, at `:427`, the lead sentence of the rule `:428` closes (executed: `grep -n`). The case passes at `726ccee6` (executed, row 3).
- `bin/seal rules --check` exits 0 (executed, row 2).
- The places round 1 named moved with it: G5, G7, the `## Removes` row at `frame/design.md:126`, `frame/plan.md` A8 and the new A10 (read). The fix pass also caught an instance round 1 did not list: `changelog.md:4` named the settling session, and now names the same module (read).

The fix pass named `025edf92` on the `verdict:` line and `changelog.md:4` on the close's `location:` line. The frame's change is `3d7e63ff`, and the answer says so. Both commits are on the branch and both are in this round's diff. The orchestrator's two acts hold as well:

- `frame/plan.md`'s first judgment row was rewritten in place without the round-cap line (read).
- #1277's body no longer holds the round-cap line, and its title counts five `docs/` lines, which are the three Scope item 9 lines and the two lines whose module no longer reads the rule (executed: `gh issue view 1277`).

A `git grep` over the work item for the old claim's words ("settling session at the dry run", "only case reading", the case name, "round cap") finds the claim nowhere else that is live (executed, row 5). The matches are A10, which names it as the alternative rejected, round 1's record, and `trail/phases/phase-1.md:5`, which the next block rules on.

One sentence of the new G5 is the framer's account and cannot be opened: "The span probe listed that assert for `:428`, and the frame first read it as wording". The frame at `e953d0a9` names no case of `tests/behaviour/test_chain_hooks_hardening.py` (executed, row 4), so what the framer's probe printed then is not in the tree. No reader acts on that sentence, so it is no finding.

```seal
confirms: none
```
What matched: `trail/phases/phase-1.md:5` stands as it is, which is the question the caller put to this round. The line says `#test_the_cap_counts_from_the_last_design_change` "is the only case reading the cap". Read beside the module the same sentence names, `tests/text/test_the_rules_have_one_owner.py`, the claim is true: that module held no other such case. Read as the whole suite, it is false, because `tests/behaviour/test_chain_hooks_hardening.py:908` read the count at `361ed0cb` too. Phase 1 recorded what it found when it found it. The line stands for three reasons:

- `agents/crafter.md:164` says a fix pass "writes no phase record", and the proofer edits none.
- The correction lives in the documents a later reader acts on. The settle reads the frame's `## Rule changes`, which now names the right module. G5 says the frame first read the case otherwise and that phase 4 kept the assert. `trail/phases/phase-4.md:39` calls the removed case "the cap's other case". Round 1's finding 1 states the contradiction.
- Rewriting the line would rewrite history, and the core sends history to the work record. This line is the work record.

```seal
confirms: none
```
What matched: the fix diff stays inside the work item's directory (executed: `git diff --stat 4134d5bf..726ccee6`), so it changes no code, test or rule file. The suite label stays as the crafters left it, `unverified`. This round finds that label honest: the fix diff ran nothing new, and the one case it rests on was run here.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite at `726ccee6`. This round ran one case, the one finding 1 of round 1 rests on | the whole suite | the orchestrator, by `seal gate --base origin/release/v0.27.3 --record seal/threads/1793542348-each-wording-pin-is-kept-or-removed` |
| Round 1's rows of `## Not judged` were not re-opened, because the fix diff does not touch them: the 349 removed asserts outside its sample, comments stating a removed fact in other words, and the 13 `docs/` lines G5 read by case names | `trail/rounds/round-1.md` *Not judged* | the parties round 1 named for each |

## Probes

`<round>` below stands for the round's scratch directory, `<scratchpad>/1793542348-each-wording-pin-is-kept-or-removed/round-2`, and `<clone>` for the clone inside it. The probe file and the clone were removed before the hand-back.

| Command | Result |
|---|---|
| `python3 test_tmp_round2.py` in `<clone>`: `rule_changes.parse` over `frame/design.md`, each `from` counted in its section with `pattern`, the `to` applied in memory and each target of the resulting check line tested with `os.path.isfile` | exit 0; two `change` ops, `errors=[]`, `unread=[]`; `from-hits 1` and `to-hits-after 1` for both; `tests/behaviour/test_chain_hooks_hardening.py True` |
| `bin/seal rules --check` in `<clone>` | exit 0, `seal rules: all 283 check lines in 55 rule files hold.` |
| `bin/test -q tests/behaviour/test_chain_hooks_hardening.py -k test_the_run_names_its_default_round_count_and_the_follow_up_file` in `<clone>` | exit 0, `1 passed` |
| `git show e953d0a9:seal/threads/1793542348-each-wording-pin-is-kept-or-removed/frame/design.md`, counted with `grep -c chain_hooks_hardening` | `0` |
| `git grep -n -i -E` for the old claim's words over the work item's directory | matches in `changelog.md:4` (now the new module), G5, G7, Scope item 6, the `## Removes` row, A2, A8, A10, the judgment row, `trail/phases/phase-1.md:5`, `phase-4.md:39` and round 1's record; none states the old `to` as the frame's current choice |
| `git grep -n -E "not a fact\|Scope item (7\|9)" -- tests` | the three Scope item 9 comments at `tests/text/test_a_rider_reaches_its_file.py:85`, `tests/text/test_broad_gate_rule.py:62` and `tests/text/test_settle_reads_before_it_removes.py:54`, and two unrelated lines |
