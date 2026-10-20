# docs/ states the current rule in one read (#941) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**What the ticket left open and the tree answered**, so nobody reopens it.
Each line names where the answer was read or how it was counted.

- *How many label lines?* 240, not 168: docs 163, agents 43, skills 34;
  57,801 bytes, median 176 characters (executed, `git grep -E
  '^\s*Enforced by:'` over the tree outside `seal/` and `tests/`).
- *How is the no-target form spelled?* `check: none reader: <who reads it>`,
  one line, stated once in `spec.md` *Data and interfaces*. The owner asked the
  frame to pick a colon form with no dash (2026-10-20); `plan.md` A1 to A3.
- *Which rules get a marker?* A rule whose test drives a script that can
  refuse a commit or fail a required pull-request job; every other rule
  names files (`spec.md`). The marker names are the work's, recorded in
  `phases/phase-1.md`.
- *Does the shape arm survive?* No. It binds by marker id, and settle writes
  no marker since #953 (`skills/settle/SKILL.md` *What --apply does*).
  #953's frame left its successor to this item (its `questions.md`, head).
- *Do the backlog directories leave in this pull request?* Only the 8 with
  nothing open at the tree and at `origin/main`. The other 117 hold 305 open
  rows at main, and the release pull request's readers ask there
  (`hygiene.yml` line 160; `skills/settle/SKILL.md` *A released work item
  with no spec.md*: the closure merges to the branch the release merges to
  first). The owner's `settle --apply` after 0.22.3 removes them, because each
  then carries a no-change block (`plan.md` A11 to A14).
- *Does a removed pre-model spec pass CI?* Yes when nothing is open:
  `unverified_check.py#settled` lines 1290 to 1302 implement #953's Q2 (a)
  (read). That row is still open in #953's `questions.md`; this item rests on
  the default it shipped.
- *Which documents pass one read?* `docs/worktree-guard-spec.md` (37,178
  estimated tokens) and `docs/one-root-by-lifetime.ko.md` (28,936); bytes
  halved, as `fold-check` estimates (executed). The split comes after the
  rewrite, only for what is still past.
- *Is `docs/one-root-by-lifetime.md` dissolved?* No, rewritten in place in
  both editions (#923's `questions.md`, owner 2026-10-14).
- *Where is the line with #940 and #942?* `spec.md` *Scope*, Out: this item
  converts the label, the markers and the no-change spelling in every file
  and rewrites only `docs/` prose; #940 rewrites the prose of `skills/`,
  `templates/`, `CLAUDE.md` and `CONTRIBUTING.md`; #942 moves tests after
  this item, and `rules --check` names any `check:` target a move breaks.
- *Is the conversion script kept?* No (`plan.md` A10).
- *Does a docs rewrite owe the proof?* Only where a preload changes. `docs/`
  is opened on demand; the label lines in `agents/*.md` and
  `skills/agent-contract/SKILL.md` are preloaded. The owner chose no paid run
  (Q1); phase 9 reads the preload bytes with `wc -c`.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Is the non-inferiority proof run, and how? The issue says #923's proof applies, and the tree cannot weigh the spend: its records cost about 65 USD and 3.2 hours a side for the four agents (read: #957 and #968's `evals/*.md`, framer about 15, smith 6, sealer 4, warden 40) | a person | (a) all four agents, both sides, after phase 9: about 130 USD and 6.4 hours serial; (b) the new side only, against the newest recorded sides of #957 and #968 as the baseline: about 65 USD, but those were measured on trees whose preloads have changed since; (c) not run: the only preload change is the label lines, rule 4 (bytes) is read for free with `wc -c`, and no case exercises `docs/` | (a), because the issue states the proof applies; the build does not wait on it, phase 10 does | answered 2026-10-20 by the repository owner, asked by the orchestrator: (c) not run. No paid non-inferiority evaluation; rule 4 (preload bytes) is read for free with `wc -c`, since the only preload change is the label lines and no case exercises `docs/` |
| Q2 | Syntax a check reads outside `docs/`, in files this item does not rewrite: the section sign (the contract's `## §N` headings, read by four tests, and 141 citation lines in `skills/`, `agents/`, `templates/`, `CLAUDE.md`, `CONTRIBUTING.md`); a coordinate's `#` and `>` (`templates/sdd-spec.md`'s `## Removes`, `skills/verify/scripts/coordinates.py`); the changelog's `<!-- specs/<id> -->` lines (`gather_changelog.py` writes and reads them); the arrow in the template heading `## Open questions → questions.md`. Who removes them is sequencing across items, which the tree cannot decide | a person | (a) not here: `docs/` drops them in what this item writes, #940 takes the on-demand files, a later item the contract's numbering, and the tree carries two citation spellings until then; (b) here, tree-wide, which adds every skill and agent citation and the contract's numbering to this item | (a) | answered 2026-10-20 by the repository owner, asked by the orchestrator: (a) not here. `docs/` drops such syntax in what this item writes; #940 and a later item take the rest |
| Q3 | Does `docs/experiments/` stay? It is dated scratch that states no policy, cited by both READMEs, `docs/release-checklist.md` and `skills/update/SKILL.md`. The tree says it is no policy and says nothing about whether it belongs | a person | (a) kept as it is, outside this item; (b) removed, with its four citers rewritten | (a) | answered 2026-10-20 by the repository owner, asked by the orchestrator: (a) `docs/experiments/` kept as it is, outside this item |
| Q4 | How many open rows does no closer in `spec.md` close? Unknowable until each of the 305 rows is read | the work | each group's phase counts them and names the directories they keep | every such directory stays, named in its phase record | answered 2026-10-20 by the work, phases 4 to 9: 33 backlog directories held, each listed in its phase record |
| Q5 | Is bytes halved a fair estimate for `docs/one-root-by-lifetime.ko.md`, whose Korean runs about 2.15 bytes a token (#953's Q4)? The answer moves whether the rewritten edition must split | a measurement | one `Read` of the rewritten file: a cut at 25,000 tokens reports the real count | the estimate, as `fold-check` reads it | answered 2026-10-20 by a measurement, phase 9: the rewritten Korean edition is about 8,400 estimated tokens by halved bytes and about 7,800 at 2.15 bytes a token, so it splits under neither: no |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip. Measured: six probes at about three seconds each answered a row that
  had been written into the human batch, and they showed the ticket's own
  instruction was wrong.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way is also what keeps the
batch short enough to answer in one sitting: two of the three kinds never
needed a person at all.

Answered rows feed back into `spec.md`'s `## Rule changes` (a policy clause
or an open-questions section) before this directory's work merges.
