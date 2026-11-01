---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-1.md'}
pattern: '^location: .*(?:evals\/scripts\/replay_targets\.py:(?:302|303|304|305|306|307|308|309|310|311|312|313|314|315|316|317|318|319|320|321|322|323|324|325|326|327|328|329|330|331|332)(?!\d))'
flags: 'm'
---
Round 1's finding 2: A record in `seal` blocks whose every block the parser refuses is still read as a table, with the false reason `Target SHA (none) does not resolve`
