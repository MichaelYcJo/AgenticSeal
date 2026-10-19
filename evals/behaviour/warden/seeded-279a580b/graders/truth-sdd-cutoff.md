---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds/round-1.md'}
pattern: '^location: .*(?:seal\/specs\/1791384154-a-records-finding-closes-once-at-the-runs-end\/spec\.md:(?:77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100|101|102|103|104|105|106|107)(?!\d))'
flags: 'm'
---
spec.md and plan.md state NOTES_FROM = 1791384154 while the code ships 1791384163, and the divergence table has no row for it.
