# Review round 2: 1792540458-on-demand-files-state-the-current-rule

target: ac92a9e6, fixes 4ce4daf0..ac92a9e6

This round has two jobs. It verifies the fix range 4ce4daf0..ac92a9e6: round
1's record 75708a42, the smith's fixes bd1aa449, their record 4c4c8e11 and
the framer's amendment ac92a9e6. It also reads the files round 1 listed under
`## Not judged` against their base b3154f43: `templates/config.md`,
`CONTRIBUTING.md`'s body, the phase 6 skills round 1 did not read (`audit`,
`build-fix`, `checkpoint`, `confidence-check`, `debug`, `feature-planner`,
`gap-analysis`, `learn`, `parity-setup`, `security-audit`, `testing`,
`skills/writing-style/outside-the-review.md`) and the templates round 1 did
not read (`sdd-questions.md`, `sdd-overview.md`, `sdd-guarantee.md`,
`seal-README.md`, `pact.md`, `parity.md`, `hygiene.yml`). The work ran in a
`git clone --no-local` at ac92a9e6.

Carried from round 1 without re-searching: the coordinates of its nine
findings, and where the routing question, section 6 and the broad run's
follower rule live (`skills/implement/orchestration.md` *Orchestrator: how
the work is routed*, `skills/implement/SKILL.md` section 6,
`agents/sealer.md` step 1). Every verdict below was reached again on the
tree at ac92a9e6. The executed lines of findings 3, 8 and 9 were re-run, and
they print what the confirmations below say.

## Findings

### 1. The block's two new routing clauses are the only clauses of the bullet no case pins

severity: should
reopens: round-1#1
location: `tests/test_first_setup_asks_once.py`, `templates/claude-md-block.md:16`
evidence: read `templates/claude-md-block.md:16`, `tests/test_first_setup_asks_once.py:728-760`
verdict: open

The close of round 1's finding 1 does not hold yet. The text is right: the
bullet now reads "Except under `no work item`, write
`seal/specs/<work-item-id>/routing.md` ..." and names "that file's
*Orchestrator: how the work is routed*" as where the question and the boxes
are stated (read, `templates/claude-md-block.md:16`). But bd1aa449 touched no
test. `skills/code-review/SKILL.md` *A finding is not closed too early*
says a claim a fix writes into a document closes when a test pins the
document, not when the sentence lands. The bullet is the one text every
session on a machine reads, and its group already pins it clause by clause:
`tests/test_first_setup_asks_once.py:728-760` holds the Bootstrap lead, the
orchestration file's path, `neither`, and both root places, each as its own
case. The two clauses this work item added for round 1 are the only rules
of the bullet with no case, so the next shortening of the 1,669 bytes can
take either back and stay green. Round 1's other wording fixes (findings 2,
3, 4 and 6) are one-reading repairs whose reader is the warden
(`skills/writing-style/SKILL.md`, rule 3's `check:` line), and are confirmed
below. This one is a rule that decides whether a session writes a file.

The case below is seen red by deleting "Except under `no work item`, " from
the template, then the pointer clause, one at a time (contract §15).

```python
def test_the_preset_writes_no_declaration_under_no_work_item():
    """Round 1 of #940, finding 1. The write is conditioned on the answer,
    and the block names the file that states question 1 and the boxes, so a
    session in a rooted repository that reads only the block neither writes
    a declaration nobody gave nor asks a question it has no text for."""
    rule = routing_rule()
    lead = rule[: rule.index("write `seal/specs/")]
    assert "Except under `no work item`" in lead, (
        "the routing rule writes routing.md under every answer, "
        "`no work item` included"
    )
    assert "*Orchestrator: how the work is routed*" in lead, (
        "the routing rule names question 1 and the boxes without naming the "
        "section that states them"
    )
```

answer:

### 2. The seal README states the drain a second time, with a moment and a destination section 6 no longer has

severity: should
reopens: round-1#5
location: `templates/seal-README.md:65-74`, `seal/README.md:65-74`
evidence: read `templates/seal-README.md:65-74`, `seal/README.md:65-74`, `skills/implement/SKILL.md:472-487`, `skills/implement/orchestration.md:65-66`, `tests/test_first_setup_asks_once.py:635`
verdict: open

Round 1's finding 5 was about the moment the orchestrator drains a work
item's open rows. The fix moved section 6 to "once the last round record has
no finding open, and before it runs `broad-gate --preflight`" and named the
drain in the code-review step (read, `skills/implement/SKILL.md:472-487`).
The fix pass's answer names those two places and no search for other
statements of the drain, and contract §12 owes the fix to every instance of
the class. A third instance stands in `seal/README.md` and its template,
which `tests/test_first_setup_asks_once.py:635` holds equal. Its
`## Export rules` is the same drain: "Item still here" against
"Destination", then "They run before a work item closes."
`skills/implement/orchestration.md:65-66` says this README "carries the
export rules so that a session that never loads this skill still sees them",
so the session it is written for reads no section 6 to correct it.

It disagrees with section 6 in three ways:

- the moment is "before a work item closes", which names no party and reads
  as the merge or the seal, both after the broad run. Draining there is the
  stale `broad-gate.md` round 1 described;
- "Open decisions" go to "the policy document's open-questions section",
  which is a `docs/` edit a pull request does not make. Section 6 sends them
  to an `add` in `spec.md`'s `## Rule changes`;
- an open finding goes to "the implementation commit", with no verifying
  round, where section 6 has a doable item reviewed by a verifying round
  before the broad run.

Phase 7 rewrote these lines (read, the word diff against b3154f43, where the
heading was *Export rules — drain before closing*), so the disagreement is
this work item's to settle. The repair states the moment and the party once
and sends the reader to section 6 for the rest. Both files change together,
because the test holds them equal.

```markdown
## Export rules

The orchestrator moves every row still open out of the work item's
directory once the last round record has no finding open, and before it
runs `broad-gate --preflight`. A commit after the broad run leaves
`broad-gate.md` stale for the sealer.

| Item still here | Destination |
|---|---|
| A finding still open in `seal/specs/<work-item-id>/rounds/round-N.md`, a test to plant among them | a commit of this pull request, reviewed by a verifying round, or `seal/follow-up.md` where it waits on prerequisite work |
| An open decision | an `add` in `spec.md`'s `## Rule changes` to the policy document's open-questions section |

The implement skill's section *6. Drain the rows before the broad run, and
keep the records* holds the rule. A work item that closes without its rows
moved leaves them where nothing looks: a prescribed test unplanted, a
decision nobody recorded.
```

answer:

## Confirmations

confirms: round-1#2
The block's two lint lines now carry their scope: line 8 reads "the full suite, the repository-wide lint and the typecheck run once, after the review rounds settle", and line 14 reads "Before each commit, run lint, format and typecheck over the files it changes" (read, `templates/claude-md-block.md:8`, `templates/claude-md-block.md:14`). The two no longer read as one act, and contract §2's repository-wide lint is the line-8 one. `tests/test_broad_gate_rule.py:365` still finds `Verification Scope`. The block is 1,669 bytes (executed `wc -c`).

confirms: round-1#3
`skills/implement/orchestration.md:475-478` reads "basing on `main` means running the gather, because `main` is the branch where the entries are due; the contribution guide names the command" (executed, round 1's `sed -n 460,478p` re-run as `sed -n 461,479p`, since the file moved one line). "The default branch" is gone from the paragraph, and the reason is back.

confirms: round-1#4
`templates/sdd-routing.md:88-91` and `skills/implement/orchestration.md:370-373` both say the routing question goes through "before the person has answered it in this session", which matches `hooks/question-gate.py:17-22` (read). The fix pass found and corrected the second statement in the same commit.

confirms: round-1#6
`CLAUDE.md:47` says "the owner's two directions bind every sentence of them", and leaves the count of rules to `skills/writing-style/SKILL.md` (read). The Bootstrap lead departs from round 1's paste: it reads "asks once, in the one call step 1 states", not "in one `AskUserQuestion` call". The departure holds on its grounds: `tests/test_first_setup_asks_once.py:142` asserts `boot.count("AskUserQuestion") == 1`, so the paste would have turned that case red, and step 1 at `skills/implement/orchestration.md:102-104` states the call and its two questions once. The lead and step 1 no longer state different counts. The phrase "the one call step 1 states" leaves out a "that", and it still reads one way: the call step 1 states.

confirms: round-1#7
`skills/update/SKILL.md:104-109` names the command, `bash install.sh "$HOME/.claude/CLAUDE.md"`, run from the clone, and names `--project` and option 2 as the two ways to write the copy the test refuses (read). `install.sh:23-26` honours an explicit target (read). `spec.md` Scope 4 still says "running `./install.sh` from a clone installs that tree's block". That is the frame's general wording of the same act and does not contradict the skill.

confirms: round-1#8
`skills/verify/scripts/broad_gate.py:4-5` now cites "The CLAUDE.md block's **Verification Scope** rule (`templates/claude-md-block.md`)". Round 1's `git grep -n 'Verification Scope' -- CLAUDE.md templates/claude-md-block.md` re-run prints only `templates/claude-md-block.md:8`, where the docstring now points (executed).

confirms: round-1#9
`phases/phase-9.md` adds the row "orchestrator, with both `skills/verify/` files | 159,334 | 151,600 | yes" and says the margin counted alike is 7,734 bytes. Round 1's two sums re-run print 151600 at 493d9816 and 159334 at b3154f43 (executed).

confirms: none
The departure in round 1 finding 1's byte account holds. `questions.md` Q4's default put the account in "the phase record", and the account went to `overview.md`'s row on what the block keeps, with Q4's Status answered. `skills/implement/SKILL.md` section 5 says a fix pass writes no phase record, so `overview.md` is the build's account a fix pass may write. The framer's ac92a9e6 amends Scope 2 and S1 to the same 169 bytes, which keeps the frame and the build telling one story (read, `spec.md:63-67`, `spec.md:207`).

confirms: none
The departure in round 1 finding 5's heading holds. Section 6's heading is *6. Drain the rows before the broad run, and keep the records*. A heading naming the sealer's spawn would contradict the moment the section now states. `git grep` for the old heading finds it only in `phases/phase-9.md:33-34` and `phases/phase-9.md:133`, the record of what phase 9 built, which a fix pass leaves alone. The one live citation, `skills/code-review/orchestration.md:177`, names the new heading (executed).

confirms: none
The fix range's new text reads one way against the owner's two rules. The new sentences in `templates/claude-md-block.md:16`, `skills/implement/SKILL.md:474-487`, `skills/code-review/orchestration.md:173-177`, `skills/update/SKILL.md:104-109` and the framer's `spec.md` Scope 9 each name the party, the moment, the file and the done state, state no count twice, and use no symbol as a separator (read). `bin/rules --check` exits 0 at ac92a9e6 (executed).

confirms: none
The rest of round 1's `## Not judged` files lose no rule an agent acts on, and the rewritten sentences in them read one way. Read against b3154f43 by word diff: `templates/config.md`, whose criterion heading, the `Mode` and `Broad gate` exceptions, the pipe rule and rule 3 keep every instruction; `CONTRIBUTING.md`, whose census rows in `phases/phase-8.md` match what left; the eleven small skills, whose changes are dashes, arrows and slashes put into words and "you" given a party; `outside-the-review.md`; and the templates `sdd-questions.md`, `sdd-overview.md`, `sdd-guarantee.md`, `pact.md`, `parity.md` and `hygiene.yml`. `sdd-overview.md` drops the note that the check counts rows and not their text, which was a limit for people; the rule an agent acts on, "closed by marking it, never by deleting the row", stays. The one finding from this reading is finding 2, in `seal-README.md`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The tests run 39533477920 at ac92a9e6, which the spawn prompt says is running | CI | the orchestrator, who relays a failure |
| The full suite, the repository-wide lint and the typecheck: not run by this round, as contract §2 requires; the suite stays `unverified` | the branch | the orchestrator's `broad-gate` run once the rounds settle |
| Whether the rewritten files leave each agent no worse at its cases, which only the paid non-inferiority run measures | `questions.md` Q1 | the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/rules --check` | exit 0, all 244 check lines in 62 rule files hold |
| round 1's executed lines for findings 3, 8 and 9, re-run at ac92a9e6 | the `main` sentence at lines 475-478; `Verification Scope` only at `templates/claude-md-block.md:8` in the two files searched; 151600 and 159334 |
| `wc -c templates/claude-md-block.md` | 1669 |
