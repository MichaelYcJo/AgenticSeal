---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds/round-2.md'}
pattern: '^location: .*(?:docs\/the-record-layout\.md:(?:133|134|135|136|137|138|139|140|141|142|143|144|145|146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163)(?!\d))'
flags: 'm'
---
Round 2's finding 1: The fix's two limit sentences are wider than `own_commits`: a base that merged an item commit older than `a` owns no later base commit, and a topic forked before `a` that merged `a` owns its fix; the same wording is in two docstrings round 1's fixes changed, three ledger rows, `overview.md` and `phases/phase-1.md`
