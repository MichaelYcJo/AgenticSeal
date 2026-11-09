# Questions for the planner: settings are read as JSON (#1454)

The issue's *To weigh* list and the judgments it left open were answered from the tree, each at the coordinate named here:

- The migration of repositories that hold `seal/config.md`: `frame/plan.md` *Alternatives considered* A8 and A9, and `frame/design.md` *Scope* item 2.
- JSON carries no comment, so where the pointer to the documentation goes: `frame/design.md` *Grounding* G14 and `frame/plan.md` A7.
- The rows agents read to judge, the language rows among them: `frame/design.md` G2 and *Scope* item 7.
- Whether the walker keeps a reader, and what code goes: `frame/design.md` G9, *Scope* item 6 and *Removes*; `frame/plan.md` A12.
- The order after #1453: `frame/design.md` G7.
- Which files the issue's "path map" and "anchor" name: `frame/design.md` G10.
- Whether a setting stays a "row": `frame/plan.md` A13.
- Whether values become typed: `frame/plan.md` A6.
- Where the parity fields and the pact's signers stand: `frame/plan.md` A10 and A11.
- The order against the release's other items: `frame/plan.md` *Overlap with the release*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should `seal mode` also convert `seal/parity.md` into `seal/parity.json`, a `seal/pact.md` signer table into the `Pact signers` key, and `~/.claude/agentic/pact-paths.md` into `pact-paths.json`, as it converts `config.md`? The tree cannot answer it: this repository holds none of the three (`ls seal/`), and how many repositories outside it hold one, and who would convert them by hand, is known only to the owner. | a person | **No converter**: the release note's *Updating* line says what to write; `chain_check.py` refuses a `parity.md` without a `parity.json` where the parity arm reads it, `seal pact` refuses a pact with no `Pact signers` key, and a signer the old map would have found is reported not found. Each repository with such a file pays one hand edit. **A converter for each**: three more readers of old tables in `seal.py`, one of them carrying `parity.md`'s *Coordinate-trust exceptions* table and *Scope notes* prose into JSON; about one more phase, and more cases to keep until the converters are removed. | No converter; the build proceeds on it. | open |
