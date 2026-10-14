# Conformance evals

Five cases proving the preset's claims with real agent runs, via
`claude plugin eval` (early access — runs once enabled on the account):

```bash
claude plugin eval . --allow-tools Bash Write Edit
```

| Case | Claim it proves | Graders |
|---|---|---|
| implement-proof | implement skill fires on build requests and ends with a proof block only fillable by reading the spec | Skill fired (with-only) · proof-block regex · file_exists |
| review-verdicts | code-review fires, catches a planted spec violation, reports with proof | Skill fired · violation quoted · proof-block regex |
| pr-body-style | PR bodies follow writing-style norms (no file-by-file listing, migration called out, plain Korean) | LLM judge · Skill fired |
| lint-hook *(experimental)* | plugin hooks fire inside eval runs — probe; reference docs leave this undefined | file-content regex |
| commit-gate *(experimental)* | the unreviewed-commit gate interrupts inside eval's dontAsk mode — probe | last-message regex |

The two experimental probes are diagnostics as much as tests: their pass/fail
answers whether hook enforcement is exercisable under eval at all.
`claude plugin eval .` reads every case under `evals/` at any depth, so it
runs the behaviour suite below as well.

## The behaviour suite — `behaviour/<agent>/`

**A rewrite of an agent's preload is proved not worse by running this suite
on the old tree and on the new one.** `scripts/noninferiority.py run` runs one
agent's cases on one side, and `compare` writes the record the five pass
rules judge. `tests/test_a_rewritten_definition_proved_non_inferior.py`
recomputes every record. The cases are generated, never edited by hand:

| Generator | Cases |
|---|---|
| `scripts/replay_targets.py` | `warden/replay-*`: a round record's target, each finding the next round confirmed fixed a `truth-` grader |
| `scripts/seed_defects.py` | `warden/seeded-*`: a shipped diff with one mutation in a unit it touched |
| `scripts/rule_cases.py` | `<agent>/rule-*`: a fixture repository, one grader per rule an output can show |

```bash
python3 evals/scripts/noninferiority.py run --agent warden --rev <merge base> \
  --out seal/specs/<id>/evals/baseline-warden.json
python3 evals/scripts/noninferiority.py compare --agent warden --phase 3 \
  --old seal/specs/<id>/evals/baseline-warden.json --new <new side>.json \
  --out seal/specs/<id>/evals/warden-phase-3.md
```
