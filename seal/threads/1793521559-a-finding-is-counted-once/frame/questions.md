# Questions for the planner: 1793521559-a-finding-is-counted-once

The ticket left these judgments open, and the tree or a probe answered each one. They are not reopened:

- Whether the count is a command written in the step or a `seal settle` output: `frame/plan.md` *Alternatives considered*, the `seal settle` row and the chosen row.
- Whether the count reads the record through the block parser or through a grep: `frame/plan.md` *Alternatives considered*, the grep row and the `python3 -c` row.
- Whether records alone reads the finding block's `location:` alone or both blocks': `frame/design.md` *Grounding*, the row on where the defect shows and the constructed-record row.
- Whether the pull-request check's records-alone rule changes with the count: `frame/design.md` *Grounding*, the `#finding_of` row.
- Whether the count belongs in `chain_check.py` or in the script alone: `frame/plan.md` *Alternatives considered*, the `Parsed.inside` row.
- Which work items are rows: `frame/design.md` *Grounding*, the `settle.py#released` row and the `routing.py#parse` row.
- What a record the reader refuses does to the count: `frame/design.md` *Grounding*, the `release_seal.py#chain_counts` row.
- Whether the step is kept at all: `frame/plan.md` *Alternatives considered*, the remove row.
- Whether the new check line can name a module this pull request adds: `frame/design.md` *Grounding*, the `rules.py#RULE_FILES` row.

Two assumptions are written down, since neither changes what gets built:

- "Records alone" keeps the step's reach, paths under `seal/threads/` of any work item, and not the narrower one the pull-request check reads, the work item's own records. The step's paragraph defines it that way, and the issue does not ask to change it.
- The commit and the pull request take `fix:`. The issue's title does, and a script that ships to no user adds nothing to the plugin, which is what the release pull request refuses a `feat:` in a patch for.

No question is left for a person, a measurement or the work, so the table holds no row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
