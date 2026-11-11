# Questions for the planner: 1794390764-scripts-load-a-reader-from-its-sibling (#1482)

The tree answered these judgments that the ticket left open. Each line
points at where the grounds stand:

- Which loading mechanism is the one: `plan.md` *Alternatives considered*,
  A1 to A4, with `frame/design.md` *Grounding* G7 and G14.
- Whether the readers go to `lib/blocks.py` or a new module, and how many
  modules: `plan.md` *Alternatives considered*, A5 and A7, with
  `frame/design.md` *Grounding* G8.
- Whether "no script loads `unverified_check.py`" reaches the predicates
  `chain_check.py` and `settle.py` read from it, which the issue's *Change*
  does not list: `plan.md` *Alternatives considered*, A6 and A8, with
  `frame/design.md` *Grounding* G9.
- Whether a command copied alone still exits 2 in a sentence, now that the
  file holding the sentence is itself absent from the copy: `plan.md`
  *Alternatives considered*, A9 and A10, with `frame/design.md` *Grounding*
  G10.
- Whether the guard stands at import or inside the function that first
  loads: `plan.md` *Alternatives considered*, A13.
- Which strings the floor walk reads as a load: `plan.md` *Alternatives
  considered*, A14 and A15.
- Whether `rules.py` and `release_report.py` are guarded: `plan.md`
  *Alternatives considered*, A16.
- Whether a caller that goes on past an absent module still shows the
  loader's sentence: `frame/design.md` *Scope* item 4 and *Data &
  interfaces*, the `going_on` bullet, after round 1's finding 1.
- Whether `seal layout --moved` can be the check of the moved cases:
  `frame/design.md` *Grounding* G13 and scenario S8, with `plan.md`
  *Alternatives considered*, A17.
- Whether "one place" for the sentence can be literal: `frame/design.md`
  *Data & interfaces*, *The sentence*. It is one constant, and the guard
  spells it again in each guarded command because nothing can be read from
  an absent file.
- Whether a check should hold the one loader: `plan.md` *Alternatives
  considered*, A11.
- Whether the duplicate helpers the issue lists are part of this work:
  `frame/design.md` *Scope*, out of scope item 1.
- Whether `lib/`'s own imports and the session hook change: `plan.md`
  *Alternatives considered*, A12, with `frame/design.md` *Grounding* G11.
- Whether `def load` in one place counts `session_cost.py#load`:
  `frame/design.md` *Grounding* G5 and scenario S3.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does any module a script loads, beyond the ones a settle loads, keep state at module level that one shared instance changes, in a command's process or across the test files of one `pytest` process? The tree could not answer at framing: G7 probed `seal settle` alone, and the answer for the other scripts depends on which argument sets and which test files run together, which no single probe lists. | the work | Where none does, `load` shares every module as designed. Where one does, the phase that meets it either moves that state into the caller or records why the module is loaded apart, and writes the decision in its phase record. | One shared instance per file, as `frame/design.md` *Data & interfaces* states. | open |
