---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-3.md'}
pattern: '^location: .*(?:evals\/scripts\/seed_defects\.py:(?:363|364|365|366|367|368|369|370|371|372|373|374|375|376|377|378|379|380|381|382|383|384|385|386|387|388|389|390|391|392|393)(?!\d))'
flags: 'm'
---
Round 3's finding 1: `seed_defects.py --case` says no shipped commit read has a name's digits as its first eight, for a name whose commit the run read and listed
