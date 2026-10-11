# a unit the extractor cannot bound is refused (#870, #848) — questions for the planner

<!-- seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**What the tickets and the review left open that the tree answered, so
nobody reopens it.** The first six are the first frame's (2026-10-07); the
rest are the reframe's (2026-10-12).

- *Refuse, or read more shapes* (#870's first question). #834's table and the
  brief: the readers that converged refused the unknown; the family #848
  belongs to is the one that reads text it does not control. Refuse.
- *What verdict a refusal takes.* `docs/the-evidence-ledger.md` §*A row is a
  content anchor*: only the major level can be `BROKEN`, and an unresolvable
  major unit is. `templates/evidence-check.yml`: "A broken coordinate fails
  either way." So `BROKEN`, exit 2 under both readings, with the reason and
  the remedy on the line, and no new verdict word.
- *The Python `SyntaxError` fall-through.* Executed: a multi-line `def`
  through the indentation rule hashes lines 1–3 of 5. Same hole as #848.
  Refuse, naming the interpreter. Built in phase 1 and kept.
- *What an installer sees, and where the release says it.* The changelog
  fragment under `### Changed`, gathered into the release's file and the
  GitHub Release; the commit hook and the CI copy change at two different
  moments (`spec.md` §*Scope*, the installer paragraph). Under a freeze the
  repair is the policy's existing `Corrected ·` row.
- *The opener's never-matching shapes* (receivers, generics, typed constants,
  #888). The opener leaves the tree, so the question is moot.
- *Brace matching for brace languages, or one rule per language* (#870's
  second question). The first frame chose a walk over an allow-list, and the
  build and round 1 answered the question the frame could not: the walk is a
  lexer per family, each family has its own exceptions, and round 1 found
  three more inside the nine. Neither; refuse both, and the format is the
  quoted line. `spec.md` §*Why this work item was reframed*.
- *What a quoted-line anchor's region is, so that #848 is answered by the
  format.* The paragraph — the contiguous run of non-blank lines around the
  quoted line — as `text_regions` reads it today in every file. It is a
  structure the file itself shows and no language's grammar, so it needs no
  reader; #848's function has no blank line inside it, so one quote hashes
  it whole (executed by reading `text_regions`: the run is 1–5). A unit with
  blank lines is several paragraphs and is cited one quote per paragraph, in
  one cell. A two-quote range was weighed and put out
  (`plan.md` §*Alternatives considered*).
- *Whether `.pyi` stays on `ast`.* Yes: `ast` parses stubs, which is the
  parser the format asks for. A decorated stub reads `DRIFTED` once on
  upgrade, and the installer paragraph says so.
- *Whether the resurrection flag stays once no text rule exists.* No field
  no code can set survives: with `ast` and the heading path as the only rules,
  nothing resurrects, and a reader of a flag nobody sets is the shape #834's
  table calls a guess. It leaves with its consumers (`spec.md` *In* 5).
- *Whether this repository's 14 bare YAML rows are rewritten here or left for
  the owner.* Here: a work item that refuses a reading repairs the rows it
  refuses in its own tree, or the CI `ledger` job is red at the pull request
  and the next session pays the repair without the reading. Measured
  2026-10-12 (`spec.md` *In* 8): 7 in #864's fragment, re-anchored in place;
  7 released, repaired by `Corrected ·` rows.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | For each suffix on the day-one brace list, which string, char and comment forms does the lexer blank, and which raw-string forms does it refuse as unlexable? | the work | (a) the C-family set alone; (b) one form table per suffix with a case each | (b) | ✅ answered by phase 2: (b), nine families. **Superseded by the reframe of 2026-10-12**: the lexer and its tables leave the tree (`spec.md` *In* 5), so no form is blanked and the question has no object |
| Q2 | How many rows of this repository's own ledgers change verdict under the rules this work ships? | a measurement | The count is read off `bin/evidence-check --strict .` on the branch against the same command on `origin/release/v0.21.0`, after phase 7. Any `BROKEN` or `DRIFTED` the release branch does not show is a finding for the phase, not a question | 0 and 0 after phase 7; before it, 14 `BROKEN` (the bare YAML rows, measured 2026-10-12 at 64e7b0a6) plus the released rows whose coordinates name removed units (`0.4.0.md` lines 51 and 67, re-read by #867's and this item's fragments) | ✅ for the walk, measured in phase 3: 0 and 0. **Re-opened by the reframe**: ⬜ until phase 7 measures it again |
| Q3 | How many rows of a consuming repository's ledger change verdict on upgrade? | a measurement | `evidence-check --strict .` at 0.21.0 in that repository, run by its installer; the one known instance is #848's reporter, whose rows citing TypeScript units by symbol all read `BROKEN` with the remedy. The number is theirs to read and does not block this build; the changelog fragment tells them what each verdict means and what to run | unknown; the fragment is written so the number needs no reply | ⬜ |
| Q4 | What shape does `resolve_unit` return so a refusal and its reason reach every caller in one reading? | the work | (a) a three-field namedtuple; (b) a two-tuple and a second call | (a) | ✅ answered by phase 1: `Resolution`, a tuple that unpacks as the old pair and carries `refused`. **Superseded by Q6**: the pair's second field is the resurrection flag, which leaves |
| Q5 | Does YAML keep a bounding rule of its own, or is a bare YAML key refused like every other suffix outside the two parsers? | a person — the repository owner, who asked for the rule to be weighed and whose 14 rows it rewrites | (a) **refuse**: `block_span` leaves; `w.yml#on` reads `BROKEN` with the remedy; this repository's 14 bare YAML rows become quoted-line anchors in phase 7 (`spec.md` *In* 8); an installer's bare YAML rows read `BROKEN` once. (b) **keep the block rule, declared a guess**: `bounding_rule` keeps `"block"`, `block_span` stays with round 1's comment fix applied and its input class written as GUESS in the docstring and the skill; the 14 rows keep their spans; the next YAML form the rule does not read — a block scalar at the key's indent, a flow collection over several lines, a document marker, an alias — is silent. The frame judges (a): the rule imitates YAML's indentation grammar without a parser, round 1 already found a shape it misreads (a comment between compact items ends the key), the standard library has no YAML parser and `evidence-ci` vendors one stdlib file, and the quoted lines hash the same jobs here (`test.yml`'s `pytest` and `ledger` jobs have no blank line inside them) | (a) refuse — the build ships on it; (b) reopens phase 5's YAML half and phase 7's rows | ⬜ |
| Q6 | What does `resolve_unit` return once no field can be unsure? | the work | (a) `Resolution` stops being a tuple and carries `places` and `refused` as attributes; every site that unpacked the pair — `judge`, `read_citation`, `rider_check.py#region_lines`, `survivor_check.py`'s `resolves`, and the test call sites — reads `.places` in the same commit, and `resolve()` keeps returning the list; (b) the pair stays with a constant `False` in its second slot. (b) is a field nothing sets, which the head of this file refuses | (a); the constraint is that no field remains that no code can set, and every unpacking site changes in one commit | ✅ answered by phase 6: (a). `Resolution` carries `places` and `refused` and is no tuple; every unpacking site moved in 5b40f93d (`phases/phase-6.md`) |
| Q7 | Of the cases in `tests/test_a_row_points_by_content.py` (26 mentions), `tests/test_a_released_row_is_read_again_in_a_fragment.py` (21), `tests/test_a_signer_records_a_pact_change.py` (13), `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` (the walk, lexer and YAML cases, lines 295–647) and `tests/test_the_fixes_name_their_surface.py` (one comment), which pin a property of the text rule itself, and which used a brace-language fixture as a vehicle for a property that survives? | the work | A case whose property is the walk's, the lexer's, the block rule's, the statement words', the one-line call's or the unsure place's goes with the code it pins. A case whose property is the freeze's, the pact recorder's, `--into`'s or `--reverify`'s, and which reached it through a `.go` or `.cs` fixture the declaration rule was unsure of, is re-fixtured in `.py` or on a quoted line where the property still has an instance, and goes where its only instance was the unsure place (e.g. "a claim on a place the declaration rule is unsure of" has no instance left). Each deletion is named in `phases/phase-6.md` with the property it took | judged per case by phase 6, named in its record | ✅ answered by phases 5 and 6: each case named with its verdict in `phases/phase-5.md` and `phases/phase-6.md` |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build. Q5 is this kind, and it does not block: the build
  ships on its default, and the owner's `(b)` reopens two phases rather than
  the frame.
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
`Status` column is ticked by whoever answered, never by whoever asked. Sorting
the rows this way is also what keeps the batch short enough to answer in one
sitting: two of the three kinds never needed a person at all.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
