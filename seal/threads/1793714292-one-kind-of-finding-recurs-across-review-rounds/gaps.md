# Closing memo: 1793714292-one-kind-of-finding-recurs-across-review-rounds

## Not verified

| Item | Who must answer |
|---|---|
| No case reads the sentence that replaces #1020's check in `docs/releasing/release-checklist.md` *2b. Settle what earlier releases left behind*, where the settling session files one issue naming each stale copy, the record it stood in, and the file the lesson belongs in. The paragraph's `check: tests/github/test_finding_counts.py` reads the count's script and not that sentence, before this phase or after it. A diff that drops or rewords the sentence passes the suite | the proofer at review |
| The changelog fragment's first entry states that every chain of three or more findings that ran under the current *The run* had a judgment row at or before its third finding, in the two windows `frame/design.md` G8 and G10 read. That rests on the framer's reading of #1038's and #947's records (G8, G9) and on the framer's executed probe over 34 pull requests (G10). This phase did not run that probe again | the proofer at review, against `frame/design.md` G8 to G10 |

## Not done

Phase 1 did not correct the two commit citations in `frame/design.md` G8
and G9, `3937d861` and `1c1d18a5`, which
`tests/text/test_a_cited_commit_outlives_the_squash.py` refuses because no
`main` or release ref contains either. `agents/crafter.md` *Job* names no
write to `frame/design.md`. `trail/phases/phase-1.md` names the squash
commits on `main` that hold the same bytes.

Phase 1 did not touch the other statements of the zero-finding round, at
`README.md:207` and `skills/code-review/orchestration.md:125-129`.
`frame/design.md` *Scope*, its *Out* list, leaves both: #1288 and #1318
rewrite that skill section in this release, and #1102 rewrites the README.
