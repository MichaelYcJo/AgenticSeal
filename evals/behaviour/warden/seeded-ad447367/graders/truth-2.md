---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds/round-1.md'}
pattern: '^location: .*(?:docs\/the-record-layout\.md:(?:106|107|108|109|110|111|112|113|114|115|116|117|118|119|120|121|122|123|124|125|126|127|128|129|130|131|132|133|134|135|136)(?!\d))'
flags: 'm'
---
Round 1's finding 2: The rule's home says a merged-in commit descends from the range's start never; a back-merge makes a sibling's commit owned, and an own commit on a topic forked before the start is not owned, and the limit paragraph names neither
