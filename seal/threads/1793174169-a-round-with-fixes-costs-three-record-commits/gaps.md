# Overview: 1793174169-a-round-with-fixes-costs-three-record-commits

## Why this work exists

In #955 and #1016 the orchestrator rewrote every `verdict:` line in a commit of its own after the fix pass wrote the `answer:` lines, so a round with fixes cost three record commits; the orchestrator's and the crafter's files now say that the fix pass commits both lines of a finding together and that the orchestrator writes neither.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Whether the chain check's acceptance changes | `routing.md` *Why this way*: "The change moves who writes a round's verdicts and answers and what the chain check accepts". `frame/design.md` *Out of scope*: "`skills/code-review/scripts/chain_check.py` is unchanged by this work." The phase left `chain_check.py` unchanged | the frame | `routing.md` was written before the frame, and the frame settled it: `frame/questions.md` head item 1, "No check changes, although `routing.md` says the chain check's acceptance moves", with the grounds in `frame/plan.md` *Alternatives considered* row D. Q1 of `frame/questions.md` stays open, and the phase built on its default (a), no check |
| The transcript line numbers of the cause | `frame/design.md` *Scope* item 4 cites the spawn prompts at lines 7831, 8015 and 8971 of session `50face2d-96d3-4774-92e7-faa0805279a3`'s `.jsonl`, and `137d0a9c` at line 7953. `grep -n` over that file finds "Leave every `verdict:` line" at 7832 and 8972, "Leave `verdict:` as it stands" at 8016, and "chore: verify #955's round 1 answers" first at 7954. The changelog fragment cites 7832, 8016 and 8972 | the line numbers `grep -n` prints | Each frame number is one lower than the line an editor or `sed -n` opens, which reads as counting from zero. A reader of the fragment opens the file with a tool that counts from one. The frame's `49a2dd0d` at line 8058 is not used by the fragment; `grep -n` finds that hash first at 8067 |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at this work item's last commit | the orchestrator, through `seal gate` (contract rule 2) |
| S5: the `add` item in `frame/design.md` `## Rule changes` parses whole through `skills/settle/scripts/rule_changes.py` | the round's proofer, through its `chain_check.py` run over the branch |
| S6: the changelog fragment names the cause as `frame/design.md` *Scope* item 4 states it | the round's proofer and the sealer, by reading |
| The sentence added to the `Grounds` cell of row *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* in `skills/implement/orchestration.md`: `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` requires the cell and reads none of its words, so no case holds the sentence | the round's proofer, by reading |

## Not done

A chain-check refusal of a finding whose two lines were committed apart was not built. `frame/questions.md` Q1 asks the owner whether to build one, and the phase built on its default (a), no check. The owner has not answered Q1.

## Fed back into the spec

none
