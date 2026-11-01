---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-1.md'}
pattern: '^location: .*(?:evals\/scripts\/replay_targets\.py:(?:953|954|955|956|957|958|959|960|961|962|963|964|965|966|967|968|969|970|971|972|973|974|975|976|977|978|979|980|981|982|983)(?!\d))'
flags: 'm'
---
Round 1's finding 1: `replay_targets.py --list --case NAME` that reads no record prints nothing and exits 0
