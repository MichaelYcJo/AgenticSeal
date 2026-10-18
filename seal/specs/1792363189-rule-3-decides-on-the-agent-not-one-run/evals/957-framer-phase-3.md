# framer — phase 3 non-inferiority

| Field | Value |
|---|---|
| Agent | framer |
| Phase | 3 |
| Baseline run | 2026-10-17T01:07:54.506Z 82099e266694 |
| New run | 2026-10-17T13:53:48.659Z e58544e954ed |
| Baseline suite | af9c924b7c5b03af5291017c226842655a8d83dd 62f007f6dedd9ba73b0cb08df7cf497f8179bc82 |
| New suite | af9c924b7c5b03af5291017c226842655a8d83dd 62f007f6dedd9ba73b0cb08df7cf497f8179bc82 |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 16.5896 |
| New spend USD | 17.3532 |
| Baseline tokens read, every model | 3164345 |
| New tokens read, every model | 4736908 |
| Baseline tool calls | 112 |
| New tool calls | 141 |
| Baseline wall seconds | 1875.0 |
| New wall seconds | 2027.6 |
| Baseline preload bytes | 93453 |
| New preload bytes | 89310 |
| Baseline tokens per tool call | 28253.1 |
| New tokens per tool call | 33595.1 |
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
| skills/agent-contract/SKILL.md | e4f679e31c041d4f7934367a9ce3bd826cf68af03e9e5319e84b3a8d327e34b3 |
| skills/implement/SKILL.md | bafff509c7b31c46ba8be3bcd71681a8682c5af6c76bd3fa28a5d743415315d9 |
| skills/writing-style/SKILL.md | f509dfeeaec143e9c4d6580e77c919b885629da5bd28186db3bf569210dcd33e |

Verdict: fail

- the new side read 33595.1 tokens across every model per tool call (4736908 over 141), not below the baseline's 28253.1 (3164345 over 112) (rule 5)
