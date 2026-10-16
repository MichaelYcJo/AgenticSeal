---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384161-the-plugin-directory-check-reads-the-directory/rounds/round-1.md'}
pattern: '^location: .*(?:\.github\/scripts\/plugin_directory_check\.py:(?:221|222|223|224|225|226|227|228|229|230|231|232|233|234|235|236|237|238|239|240|241|242|243|244|245|246|247|248|249|250|251)(?!\d))'
flags: 'm'
---
The seeded defect: 'f"{head} an entry, pinning no commit (source: {url or \'none\'}).",' made 'f"{head} an entry, pinning no commit (source: {url and \'none\'}).",' in `.github/scripts/plugin_directory_check.py#line`.
