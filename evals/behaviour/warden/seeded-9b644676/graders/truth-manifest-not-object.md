---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384161-the-plugin-directory-check-reads-the-directory/rounds/round-1.md'}
pattern: '^location: .*(?:\.github\/scripts\/plugin_directory_check\.py:(?:282|283|284|285|286|287|288|289|290|291|292|293|294|295|296|297|298|299|300|301|302|303|304|305|306|307|308|309|310|311|312)(?!\d))'
flags: 'm'
---
A plugin.json whose top level is not an object ends in a TypeError the except clause does not catch.
