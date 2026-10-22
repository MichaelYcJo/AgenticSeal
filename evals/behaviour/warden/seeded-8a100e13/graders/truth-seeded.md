---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/rounds/round-1.md'}
pattern: '^location: .*(?:evals\/scripts\/noninferiority\.py:(?:656|657|658|659|660|661|662|663|664|665|666|667|668|669|670|671|672|673|674|675|676|677|678|679|680|681|682|683|684|685|686)(?!\d))'
flags: 'm'
---
The seeded defect: 'if new_total < old_total:' made 'if new_total <= old_total:' in `evals/scripts/noninferiority.py#verdict`.
