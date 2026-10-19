---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384161-the-plugin-directory-check-reads-the-directory/rounds/round-1.md'}
pattern: '^location: .*(?:tests\/test_the_plugin_directory_answers_the_box\.py:(?:167|168|169|170|171|172|173|174|175|176|177|178|179|180|181|182|183|184|185|186|187|188|189|190|191|192|193|194|195|196|197)(?!\d)|tests\/test_the_plugin_directory_answers_the_box\.py:(?:184|185|186|187|188|189|190|191|192|193|194|195|196|197|198|199|200|201|202|203|204|205|206|207|208|209|210|211|212|213|214)(?!\d))'
flags: 'm'
---
The no-commit case asserts an entry and pinning no commit and not the source text, so the seed passes it.
