---
type: 'regex'
target: {source: 'file', path: 'tests/test_textutil.py'}
pattern: 'def test_[\s\S]*def test_'
match: 'not_contains'
---
The rename wrote no case new: `tests/test_textutil.py` still holds one.
