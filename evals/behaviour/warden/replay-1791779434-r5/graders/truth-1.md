---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-5.md'}
pattern: '^location: .*(?:docs\/worktree-guard-spec\.md:(?:22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52)(?!\d))'
flags: 'm'
---
Round 5's finding 1: The policy, ledger S1 and spec In 2 say the deny infers nothing about git; its index-residue note says *These commands clean the tree*, and for a tracked file `.gitignore` matches, the restore leaves it dirty
