# 1791867522-the-routing-sentence-is-pinned-and-hidden-lines-names-its-inputs — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here. -->

📋 implement applied
· spec:     #922; #872's `rounds/round-3.md` and `rounds/round-3-report.md` (🟡 10, 🟡 11 and their paste-ready text); `docs/the-evidence-ledger.md` §*The fold, and what tells it from a deletion*, the liveness statement; `hooks/routing.py#shown` and `#table_rows`; `hooks/config.py#hidden_lines`, `#unfenced`, `#read_table`, `#pact_reviews`; `tests/test_routing_is_recorded.py` S10 (R1 to R9)
· evidence: `seal/ledger/1791867522-the-routing-sentence-is-pinned-and-hidden-lines-names-its-inputs.md` N1, N2, N3; `Re-read · P3-1`, `Re-read · C2` and W2 in `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` re-stamped in place by `--reverify --into`
· verified: executed: N1's case seen red under `bin/mutation-check`, and the other 225 routing cases surviving the same mutation; an R8 probe of both declaring readers; the narrow modules; `evidence-check --strict`; `fold-check`; `survivor-check`. Read: the callers of `unfenced` and `hidden_lines`

## Why this work exists

Round 3 of #872 found the routing half of the liveness statement had no test behind it and both declaring clauses over-reached past a fence that closes, and `hidden_lines`' `Reads:` line named one input. The statement now says what each reader does and names the cases that hold it, and the line names every input the function is handed.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How many inputs `hidden_lines` is handed | #922 and round 3's paste-ready line: "names one of its four inputs", the four being `seal/config.md`, `seal/pact.md`, a `seal/pact-changes/` record and the pact path map / `hooks/config.py#pact_reviews` also reads a `seal/pact-reviews/` record through `read_table`, `gfm_table` and `unfenced` (called by `pact_check.py#pact_reviews`) | the code: the line names five | `git grep` of every `read_table(` call: `hooks/config.py:1591` is `pact_reviews`, which round 3's caller list did not trace |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, repository lint and typecheck: unverified here, by contract §2 | the sealer, once the rounds settle |

## Not done

`evidence-check --strict .` exits 2 on this branch, and not because of it: 47 rows anchored on `docs/worktree-guard-spec.md` §*Known limits* and §*Creation consent — the first creation is the question, not every one* are drifted, in `seal/releases/0.18.0.md`, `0.18.2.md`, `0.18.3.md`, `0.20.0.md`, `0.21.0.md` and in the fragments of 1791852610 and 1791852612. This branch changes neither that document nor those ledger files, so the base `2d4fbdff` carries them (read, not run at the base). They were left unstamped because nobody here read them. `--reverify --into` had written two `Re-read ·` rows for them (K6, G17) into this fragment, and those were removed for the same reason. They belong to whoever merged #916 or #917 into `release/v0.21.1`.

#872's own changelog fragment, `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/changelog.md`, still says the two hooks "still read a row below a comment opener nobody closed". That is the same wording this work scoped past a fence that closes, at release-note level. `survivor-check` over this range does not report it. It is that work item's file and not this one's, so it was left. Whether the release note should carry the qualifier is the orchestrator's call before the 0.21.1 gather.

## Fed back into the spec

none
