# warden — phase 2 non-inferiority

| Field | Value |
|---|---|
| Agent | warden |
| Phase | 2 |
| Baseline run | 2026-10-14T00:22:18.406Z 9f46fd963e32 |
| New run | 2026-10-14T00:33:20.783Z 49f1e6cecaec |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 1 |
| Baseline false rows | 1 |
| New report rows | 1 |
| New false rows | 0 |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | warden replay-1791382684-r5 | reach-warden | 1 | 1 | 1 | 1 |
| shape | warden replay-1791382684-r5 | shape-loses-a-record | 1 | 1 | 0 | 1 |
| shape | warden replay-1791382684-r5 | shape-needs-a-fix | 1 | 1 | 0 | 1 |
| shape | warden replay-1791382684-r5 | shape-report-exists | 1 | 1 | 1 | 1 |
| shape | warden replay-1791382684-r5 | shape-verdicts-table | 1 | 1 | 1 | 1 |
| truth | warden replay-1791382684-r5 | truth-2 | 0 | 1 | 1 | 1 |

## New preload

| File | sha256 |
|---|---|
| agents/warden.md | c25379d8db3acc6d753ffc470348ef7004a32ea6b544ac2c78407e0ad5ce7930 |
| skills/agent-contract/SKILL.md | 739a7a1b0c3d95aac18f9896be1bd9af7c8388e2a224087d4f2161ab37e511f5 |
| skills/code-review/SKILL.md | 5c1c7ebaa781df385f57e80a43e21a97f1558853d461b79c8a439058751f419d |
| skills/writing-style/SKILL.md | a73becceca50362d723b64c565f11bbdae6d4d763c0ce6e392c36d149338cf06 |

Verdict: fail

- shape grader warden replay-1791382684-r5/shape-loses-a-record failed on the new side (0/1)
- shape grader warden replay-1791382684-r5/shape-needs-a-fix failed on the new side (0/1)
