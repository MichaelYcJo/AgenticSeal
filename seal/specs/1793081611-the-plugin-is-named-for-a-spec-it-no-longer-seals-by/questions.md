# Questions for the planner: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

What the ticket left open and the tree answered, so nobody reopens it:

- **The marker's text** is the first line of `templates/seal-README.md`,
  the heading `# What AgenticSeal maintains in seal/`, read exactly. The
  README is the one file the plugin already writes into every root, and a
  heading is what a person reads first (`plan.md` *Alternatives
  considered*).
- **The changelog fragment marker `<!-- specs/<work-item-id> -->` keeps
  its spelling.** `gather_changelog.py` decides what is gathered by that
  marker across every released file, and the 0.4.0 root move kept it for
  the same reason (`tests/test_no_document_names_the_old_roots.py#KEEP`).
- **The recorded eval scaffolds keep their clone line**; the eval
  directories and prompts rename with the agents (`spec.md` *Scope*).
- **`docs/` is rewritten in place for names and paths**, and `spec.md`
  *Rule changes* carries each rule whose content changes.
- **`bin/test` stays**, and #1060 decides where the repository's developer
  scripts live. `chain-check` keeps no `bin/` command: it has none now, and
  CI runs it by path.
- **`templates/sdd-spec.md` becomes `templates/sdd-design.md`**, because a
  template is named for the file it starts.
- **`LICENSE` reads "AgenticSeal contributors"**: the line is the brand
  where a person reads it, which #1051 says is written as AgenticSeal.
- **`.test_durations` is not living text**: the runner regenerates it, and
  the census does not read it.
- **The `renames` map is written** even though the marketplace's own name
  changes: it is the documented carrier of a plugin's rename and costs one
  line.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | #1051 fixes `seal gate`, `seal settle`, `seal cost`, `seal mutate` and writes `seal check` fifth, where the `bin/` list has `unverified-check` fifth. `check` says nothing about what is checked, and `chain-check`, which the same list names next, is what a reader would take "check the seal" to mean. The tree cannot say which tool the owner meant by `check`, nor name the eight tools the issue left to "the rest" | a person | (a) `seal check` runs `unverified-check`, as the issue's order reads; (b) no subcommand is called `check`, and each name says its tool. Either way the eight unnamed tools need names | (b): `unverified` for `unverified-check`, `arms` for `arm-check`, `deferrals` for `deferral-check`, `fold` for `fold-check`, `pact` for `pact-check`, `payload` for `payload-meter`, `stamp` for `seal-stamp`, `layout` for `test-layout`, `rules` for `rules`; no `check` | open |
| Q2 | The fifteen state files under the git common directory and the `~/.claude/specseal/` directory carry the old `name`, and #1051's mapping does not list them; the census the issue asks for refuses the old prefix. Whether they take `agentic-` (the plugin's `name`) or `seal-` (the root they sit beside) is a naming choice the tree does not decide, and a person types one of them (`.git/agentic-scratch`) | a person | (a) `agentic-` and `~/.claude/agentic/`, following the plugin's `name`; (b) `seal-` and `~/.claude/seal/`, following the root; (c) keep `specseal-` with fifteen census exemptions. (a) and (b) each need the migration to rename what it meets; (c) leaves the old name where a person reads it | (a) | open |
| Q3 | From phase 2's commit this work item stands at `seal/threads/<id>/`, and the installed 0.22.4 edit gate reads `seal/specs/<id>/routing.md`, so it refuses every edit on this branch. The only reading the installed plugin accepts is `seal no-work-item`, which records that the session's change belongs to no work item, and this change does. Nothing in the tree says whether that record is acceptable for the one run whose release renames the gate's own path | a person | (a) the orchestrator runs `seal no-work-item` once per session on this branch, commits keep `Seal-Routing: <id>`, and `plan.md` *Operational impact* records why; (b) the orchestrator upgrades the installed plugin to this branch's tree mid-run, which no command of the plugin does and which changes the gates under a running session; (c) this work item's directory stays at `seal/specs/` until the last commit, and CI fails the trailer arm on every push before it | (a) | open |
| Q4 | Whether the three lines README.md prints carry a user from `specseal@specseal` to `agentic@agenticseal` is settled only on a machine that holds the old install, after the release tag exists; `claude plugin validate .` checks the catalog and not a registration, and no fixture in this repository holds Claude Code's plugin registry | a person | (a) the owner runs the three lines on a machine installed at 0.22.4 after the release and reports; (b) the README prints them labelled as read from the reference and not run. Either way the build prints them | (b) until (a) is done; the README carries no label, and this row is the record that nobody has run them | open |
