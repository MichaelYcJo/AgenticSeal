# settle squashes specs into docs/ in place (#953) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**What the ticket left open and the tree answered**, so nobody reopens it.
Each line names where the answer was read.

- *Does `docs/release-checklist.md` still require `settle` at every release?*
  No. §2b, line 101: "`settle` runs when the owner calls it, not at every
  release." The first half of the issue's item 6 already holds. Only the
  step's command sequence changes (`spec.md` `## Removes`).
- *Where does the one-read limit come from?* The tree holds only the
  1000-line `Document line ceiling` row (`seal/config.md`;
  `docs/the-record-layout.md` §*The size a reader takes whole*). The reading
  tool's own limits are 2000 lines per call (its description) and 25,000
  tokens per call (measured in this session; it reported "cap 25000"). The
  token figure becomes a new optional row, `Document token ceiling`
  (`spec.md` *Data & interfaces*).
- *Does this item set this repository's ceilings?* No. Declaring the token
  row now would refuse `docs/worktree-guard-spec.md` and
  `docs/one-root-by-lifetime.ko.md` at once, and splitting them belongs to
  #941's rewrite (#941: "split to fit one read").
- *Does `target_problem` move?* No. `fold_check.py` stays the module, so
  `bin/rules` → `.github/scripts/rules.py#target_problem` →
  `fold_check.py#target_problem` is unchanged (`plan.md` A7).
- *Does the marker-bound shape check go?* Not here. #941 changes the label to
  `check:`, and the shape's successor goes with it. Until #941 removes the
  legacy markers, `Fold shape from`, `tests/test_both_editions_carry_the_same_folds.py`
  and the line-wrap exemption keep reading them.
- *Does the index duplicate `docs/the-record-layout.md` §*docs/*?* It
  replaces it. The table moves to `docs/README.md` (`plan.md` A6).
- *Does this item apply its own changes through its own `## Rule changes`?*
  No. The issue names the files it rewrites, and the change that sets the
  model up cannot wait for a `settle` (`spec.md` `## Rule changes`).
- *Does `--retire-process` survive?* No. Issue item 6: "The process record
  leaves with the spec it belongs to." Both arms already run only at the
  owner's settle (`plan.md` A5).
- *Is local mode in scope?* No: #955. `settle` keeps refusing it.
- *Does editing `agents/framer.md` owe a behaviour-eval run?* No.
  `tests/test_a_rewritten_definition_proved_non_inferior.py`'s docstring:
  "nothing here makes a later edit of a definition owe a run, by design."
- *What order is "merge order"?* Ancestry of the first commit on
  `--released-at` that adds each `spec.md`. Specs on parallel histories that
  name one place are a conflict, printed and never guessed (`spec.md` *Merge
  order*). The issue asks that "a conflict the order cannot settle is shown",
  and this is the narrowest reading of it.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | The issue's operation line has three fields: `<op> · <file> §<heading> · <rule>`. To rewrite or delete *a sentence*, as item 3 says, an operation has to name which one, and the issue does not say how. Is the quoted-text anchor right, `change · <file> §<heading> › "<text as it reads now>" · <rule>`? So are the two extra shapes: `remove` with no quote deletes the section, and `add` with no `§` creates a document. The tree cannot answer this, because the line's grammar is a product decision the owner started and did not finish | a person | (a) as defaulted: one sentence named by quoting it, whitespace collapsed; (b) `change`/`remove` take the whole section, which loses the sentence-level rewrite item 3 asks for; (c) another anchor the owner names, such as a stable id per rule, which puts a key back into `docs/`, the thing the marker's removal takes out | (a). The build proceeds on it, and the parser is one module, so another anchor changes one file and its cases | open |
| Q2 | Should a released spec with **no** `## Rule changes` section (every pre-model spec) and nothing open pass the CI readers when its directory is removed, with no marker and nothing to replay? This moves a gate toward allowing more. Today a removed pre-model spec passes only where a `docs/` marker absorbed it. The tree cannot decide it: the failure direction of a gate is the owner's call (`CONTRIBUTING.md` §*What a change to a gate must carry*), and the only thing in the tree that bears on it is #941's plan, which needs exactly this to settle the backlog | a person | (a) accept it: #941 can retire the backlog after reading each spec by hand, and a branch that deletes an unread pre-model directory passes CI, which the reviewer reads in the diff; (b) refuse it unless a legacy marker covers it, so `folded_items` survives until #941; but #941 removes the 129 markers, so (b) leaves its directories with no way out, the state #517 ended; (c) refuse it unless the pull request carries a declared settle, which needs a declaration a fold has never had (`skills/settle/SKILL.md` §*A fold is not a work item*) | (a) | open |
| Q3 | Issue item 2 says "A pull request does not edit `docs/`". Should a check gate it, refusing a declared work item's pull request whose diff touches the policy root? The tree cannot answer it now: this item and #941, both declared work items, edit `docs/` by the issues' own design, so a gate landing here refuses the milestone's next item, and when to start gating is the owner's sequencing | a person | (a) no gate in #953: the rule is stated in the implement skill, the framer definition and the spec template, and review reads it in the diff; a gate is weighed after #941 lands; (b) gate now, with #941 exempted by name, which builds an exception into a new gate on its first day | (a) | open |
| Q4 | Is `ceil(bytes / 2)` a safe token estimate for every script a policy root may hold? Measured here: English text at 2.85 bytes a token, mixed Korean at 2.15. Dense Hangul or symbol-heavy text was not sampled, so the bound is unproven for it | a measurement | one `Read` of a dense-Hangul file past the 25,000-token cap gives its reported count; a ratio under 2 lowers the divisor | `bytes / 2`. A document the estimate passes and the tool still cuts is a limit sentence in `skills/settle/SKILL.md`, not a guard | open |
| Q5 | Once `folded_items` is gone, how does `tests/conftest.py#cutoff_item_is_traceable` tell a settled id from a typo? Its docstring makes a work item traceable when its directory is present or a policy document absorbed it. The framing could not settle the mechanism: it depends on what the phase-3 predicate exposes | the work | the phase decides, for example from `git log` showing the path existed at a commit, and records it in `phases/phase-3.md` | phase 3's choice, and the cases that call the helper stay green before and after | open |

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

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
