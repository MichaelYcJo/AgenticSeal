---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-1.md'}
pattern: '^location: .*(?:evals\/scripts\/replay_targets\.py:(?:195|196|197|198|199|200|201|202|203|204|205|206|207|208|209|210|211|212|213|214|215|216|217|218|219|220|221|222|223|224|225)(?!\d))'
flags: 'm'
---
The seeded defect: 'if not wanted(item) or not os.path.isdir(rounds):' made 'if not wanted(item) and not os.path.isdir(rounds):' in `evals/scripts/replay_targets.py#records`.
