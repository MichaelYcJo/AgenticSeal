# four `Reads:` lines say refused where an off-shape `## Removes` line passes (#905) — questions for the planner

<!-- seal/specs/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here.
Framed by `specseal:framer` on Fable 5.1 for #905. Nobody answers mid-run:
every row carries a default and the plan is built on it. -->

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `spec.md` §*The
judgment the ticket left open* or in `plan.md`'s Alternatives table.

1. **Correct the four words, or make them true?** Make them true: an
   off-shape line under `## Removes` is `REFUSED` naming it, and a test holds
   the behaviour. `mixed` would record a tolerant owned-format reader, the
   shape #834's table found behind every reopened family, and would leave a
   removal written as a bullet unread by anybody (`spec.md` §*The judgment*
   1–5; `plan.md` Alternatives rows 1–4).
2. **Does the direction word stay in the grammar?** Yes, in this item. It is
   the inventory's predictive column and the per-unit statement of #835's
   rule 1 (*a guess only as an allow-list that refuses the unknown*);
   changing it is a `feat:` to a shipped `docs/` rule, the owner's, and P1
   below carries it without blocking.
3. **Which units change?** `removes_section` and `removal_findings` — the two
   whose text was false. `file_claims` and `check_records` are true read
   through once the helper refuses, and editing them would move ten released
   anchors for nothing (`plan.md` Alternatives, last row).
4. **What passes under the heading?** A table row (header and rule rows
   included), a line beginning `nothing`, a blank line, and whatever
   `claim_lines` already treats as a quotation or an aside — a fence, an HTML
   comment. Everything else is refused, whatever it looks like: deciding from
   its look is a guess-class reader (`spec.md` §*The judgment* 3).
5. **Where does prose go?** A row's last cell, the `nothing` line's reason,
   or an HTML comment; the refusal says so (`spec.md` In 1).
6. **Is the empty-section refusal's wording kept?** Yes, byte for byte;
   `test_presence_is_required_at_or_above_the_cutoff` pins it, and a required
   section holding only a bullet gets both findings (S3).
7. **How is ⬜ 4 fixed?** The lead, limit 5 and the `Enforced by:` line name
   the warden; limit 5 keeps its facts and adds the act — the warden reading
   a caller's change opens the lines of the helpers whose value it changes —
   and `agents/warden.md` §*Role* is told so in one sentence, because nothing
   tells it today (`grep -n 'Reads:' agents/warden.md skills/code-review/*.md`
   is empty). P2 lets the owner take the document-only wording instead.
8. **How is ⬜ 5 fixed?** The clause is replaced on its line by what the gate
   does since #836 (round 6's option B wording); the module's `Reads:` line
   stays `unknown passed`, which #904 settled.
9. **What does the frame remove?** The three clauses, quoted whole in
   `spec.md` §*Removes*, so the records arm reads each as gone; the silent
   drop has no coordinate and is replaced in place.
10. **When is the fragment written?** Last. Until it exists the item is not
    live for the records arm, and the frame's own `## Removes` rows would read
    `STANDING` at exit 2 while the clauses still stand (`plan.md`
    Alternatives, *Write the ledger fragment at phase 1*).
11. **Does this item meet any live frame with prose under the section?** No,
    measured 2026-10-13 at 39a315a5: 4 frames carry the heading, 2 carry
    off-shape lines, both shipped in 0.21.0 with no fragment; the six 0.21.1
    sibling branches on `origin` hold no `spec.md` yet (`spec.md` §*The
    judgment* 4). M1 measures it again at the gather.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| P1 | **Does the direction word stay in the `Reads:` grammar, and is any general rule wanted over it?** #834's round 6 found a fourth wrong direction word on lines a person wrote, and the issue says a word a reader cannot check costs what the withdrawn backfill cost. This item makes four words true and test-held, which is #836's form applied to one class, and touches the grammar not at all. Whether every direction word should be held by a test, or the word should retire from the grammar, is a change to #835's rule in `docs/the-reader-registry.md` and to `tests/reader_registry.py#DIRECTIONS`, a `feat:` | **a person**: the repository owner. The word is the inventory's one predictive column and the per-unit statement of rule 1's condition; keeping or retiring it is what the registry is for, which somebody has to be accountable for | **(a)** the word stays and nothing general is added; a false word is the warden's, as limits 1 and 5 say, and the pattern this item sets — make it true, pin it — is followed when the next one is found. **(b)** the word stays and a rule is opened as its own issue: a `Reads:` line whose direction a test can hold names the test, the way a ledger row does. **(c)** the word retires: `DIRECTIONS` goes, 26 lines lose their last word, the registry's definition and `CONTRIBUTING.md`'s bullet are rewritten — and `grep -rn "Reads: guess"` can no longer tell a bounded guess from an unbounded one | (a); the build is the same under every answer, so the row does not block; (b) and (c) are each a new issue the orchestrator files on the owner's word | ⬜ |
| P2 | **Does the warden get a sentence for limit 5, or is limit 5 stated as unread?** The frame names the warden as the reader of a caller-staled helper's line and tells it so in `agents/warden.md` §*Role* (one sentence, a preloaded body every spawn pays for, #292). The alternative keeps the registry honest without touching an agent: limit 5 says such a line is read by nobody until the helper itself changes, and the lead says so too | **a person**: the repository owner. Whether an agent is told to do a thing, or a limit is recorded as unread, is what the agent set does, which somebody has to be accountable for | **(a)** the sentence is added; the lead, limit 5 and `Enforced by:` name the warden; round 6's own reading of helpers at their callers becomes a told act. **(b)** no agent edit; limit 5 and the lead say the line is nobody's until the helper changes, and the `Enforced by:` line says so for that limit | (a); the plan is built on it; (b) is one sentence removed and two reworded, no code moves | ⬜ |
| M1 | **At the 0.21.1 gather, does any sibling frame carry a line under `## Removes` that this refusal names?** Measured 2026-10-13 at 39a315a5: no live frame does, and the six sibling branches on `origin` hold no `spec.md` yet | **a measurement**: the orchestrator at the release gather, `bin/evidence-check --strict .` on `release/v0.21.1` with every item landed — the run `docs/release-checklist.md` already makes | **Exit 0:** nothing to do. **A `REFUSED` naming a sibling's line:** that sibling moves the line into a row's last cell, the `nothing` reason or a comment, in its own integration commit; the refusal's text names the remedy | the run the checklist already makes | ⬜ |
| W1 | **The shape `removes_section` hands the off-shape lines back in** — a fifth element `[(number, text)]`, or one list of `(number, text, kind)`; and whether the refusal's detail names the two shapes in one sentence or two | **the work**: phase 2 | S1–S3 hold either way; the detail text is pinned whole by the new cases (§14) | — | ⬜ |
| W2 | **Where in `agents/warden.md` §*Role* the sentence sits, and how its ledger row anchors it** — a quoted-line anchor on the sentence (the paragraph region), or the section heading | **the work**: phase 1 for the sentence, phase 3 for the row | `tests/test_one_word_one_meaning.py` and `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` pass; the row is OK under `--strict` | — | ⬜ |

**`Who can answer` takes one of three values and nothing else.**

- **a person** — what the product should be, or a value somebody has to be
  accountable for. The only kind of row that blocks the build, and under this
  run's `automation` answer neither P1 nor P2 does: each is built on its
  default and reversed by an edit no later than the review rounds.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records the decision in `phases/phase-N.md`.

**The framer opens rows and does not own their answers.** The `Status` column
is ticked by whoever answered, never by whoever asked. Answered rows feed back
into `docs/` before this directory's work merges.
