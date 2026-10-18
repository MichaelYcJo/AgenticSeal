# framer — phase 4 non-inferiority

| Field | Value |
|---|---|
| Agent | framer |
| Phase | 4 |
| Baseline run | 2026-10-18T01:06:46.419Z b3fad3b7641d |
| New run | 2026-10-18T04:39:56.920Z 9dd1c4d0f053 |
| Baseline suite | af9c924b7c5b03af5291017c226842655a8d83dd 62f007f6dedd9ba73b0cb08df7cf497f8179bc82 |
| New suite | af9c924b7c5b03af5291017c226842655a8d83dd 62f007f6dedd9ba73b0cb08df7cf497f8179bc82 |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 16.9055 |
| New spend USD | 16.1196 |
| Baseline tokens read, every model | 3275602 |
| New tokens read, every model | 3258508 |
| Baseline tool calls | 120 |
| New tool calls | 109 |
| Baseline wall seconds | 2018.5 |
| New wall seconds | 2031.1 |
| Baseline preload bytes | 89444 |
| New preload bytes | 86353 |
| Baseline tokens per tool call | 27296.7 |
| New tokens per tool call | 29894.6 |
| Baseline tokens per true find | unknown |
| New tokens per true find | unknown |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | framer rule-framer-document-helpers | reach-framer | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-document-helpers | shape-builds-nothing-edit | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-document-helpers | shape-builds-nothing-write | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-document-helpers | shape-marks-the-spec | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-document-helpers | shape-phases-carry-verified-by | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-document-helpers | shape-writes-plan | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-document-helpers | shape-writes-questions | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-document-helpers | shape-writes-spec | 2 | 2 | 2 | 2 |
| reach | framer rule-framer-keep-trailing-space | reach-framer | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-keep-trailing-space | shape-builds-nothing-edit | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-keep-trailing-space | shape-builds-nothing-write | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-keep-trailing-space | shape-marks-the-spec | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-keep-trailing-space | shape-phases-carry-verified-by | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-keep-trailing-space | shape-writes-plan | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-keep-trailing-space | shape-writes-questions | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-keep-trailing-space | shape-writes-spec | 2 | 2 | 2 | 2 |
| reach | framer rule-framer-loud-flag | reach-framer | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-loud-flag | shape-builds-nothing-edit | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-loud-flag | shape-builds-nothing-write | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-loud-flag | shape-marks-the-spec | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-loud-flag | shape-phases-carry-verified-by | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-loud-flag | shape-writes-plan | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-loud-flag | shape-writes-questions | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-loud-flag | shape-writes-spec | 2 | 2 | 2 | 2 |
| reach | framer rule-framer-word-count | reach-framer | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-word-count | shape-builds-nothing-edit | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-word-count | shape-builds-nothing-write | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-word-count | shape-marks-the-spec | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-word-count | shape-phases-carry-verified-by | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-word-count | shape-writes-plan | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-word-count | shape-writes-questions | 2 | 2 | 2 | 2 |
| shape | framer rule-framer-word-count | shape-writes-spec | 2 | 2 | 2 | 2 |

## New preload

| File | sha256 |
|---|---|
| agents/framer.md | c2e7a7d7437485042ebda52e71a6a7137f9a1511258feb2e779ac19db9769486 |
| skills/agent-contract/SKILL.md | 642b0da67c6795a1aa75ba16d0b17bac4e48639d05134bcdb050c34fcec6ee4e |
| skills/implement/SKILL.md | dbff9bdf37f25fa177ad93cd49aac7a5260e4da73ccd2c47e7da6cd4d3340556 |
| skills/writing-style/SKILL.md | 5e1a12a78c7058f5e91059cf384ef33c38f8f816042d029bacad4be4b111e1bb |

Verdict: fail

- the new side read 29894.6 tokens across every model per tool call (3258508 over 109), not below the baseline's 27296.7 (3275602 over 120) (rule 5)
