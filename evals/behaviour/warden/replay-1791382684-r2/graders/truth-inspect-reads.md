---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791382684-every-reader-and-record-is-inventoried/rounds/round-2.md'}
pattern: '^location: .*(?:skills\/verify\/scripts\/deferral_check\.py:(?:176|177|178|179|180|181|182|183|184|185|186|187|188|189|190|191|192|193|194|195|196|197|198|199|200|201|202|203|204|205|206)(?!\d))'
flags: 'm'
---
inspect's Reads: line leaves out the workflow_files and read_events loop that decides too late.
