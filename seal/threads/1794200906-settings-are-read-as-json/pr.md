- "**A repository's settings are a JSON file, `seal/config.json`, read by Python's own JSON parser (#1454).**" (`changelog.md` *Changed*, the first item)
- "The settings were a markdown table, `seal/config.md`, read by a table walker of the plugin's own. That walker had to decide what a fence, an HTML comment, a blank line or an escaped pipe meant inside a table, and #867, #871, #925, #1119, #415, #429 and #430 were each a table shape it read differently from the person who wrote it." (`changelog.md` *Changed*, the first item)
- "**`seal mode` writes `seal/config.json`, and converts an old `seal/config.md` once.**" (`changelog.md` *Changed*, the second item)
- "**The migration config is `seal/parity.json`, and its machine-local paths are `~/.claude/agentic/parity-paths.json`.**" (`changelog.md` *Changed*, the third item)
- "**A pact's signers stand in a `Pact signers` key of the pact repository's `seal/config.json`, and the checkout map is `~/.claude/agentic/pact-paths.json`.**" (`changelog.md` *Changed*, the fourth item)
- "**The table walker lives in `lib/tables.py`, and no setting is read through it.**" (`changelog.md` *Changed*, the fifth item)
- "**Every shipped text calls a setting a key and names `config.json`.**" (`changelog.md` *Changed*, the sixth item)
- "Updating: run `seal mode` once in each repository that holds `seal/config.md`. It writes `seal/config.json` from the table and removes the old file, and until then `seal gate`, `seal fold`, `seal pact` and `seal mode --check` exit 2 and name `seal mode`, `seal pr-body` refuses with the same sentence and exits 1, and `seal rules`, `seal settle` and `seal unverified` read the default policy root and reference roots." (`changelog.md`)
- "Rewrite three files by hand from the old ones, since no command converts them." (`changelog.md`)

Closes #1454.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
