---
type: 'regex'
target: 'trace'
pattern: '\brefused\b'
flags: 'i'
---
The report says the run was refused. Fails by design until phase 4 replaces this case: `broad-gate` no longer reads the round record, so nothing refuses this run.
