set -eu
git init -q -b main .
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'IADD_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark."""
    return text.upper() + "!"
IADD_EOF
mkdir -p "$(dirname 'src/__init__.py')"
cat > 'src/__init__.py' <<'IADD_EOF'

IADD_EOF
mkdir -p "$(dirname 'tests/__init__.py')"
cat > 'tests/__init__.py' <<'IADD_EOF'

IADD_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'IADD_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")


if __name__ == "__main__":
    unittest.main()
IADD_EOF
mkdir -p "$(dirname 'README.md')"
cat > 'README.md' <<'IADD_EOF'
# textutil

Small text helpers.
IADD_EOF
mkdir -p "$(dirname 'CONTRIBUTING.md')"
cat > 'CONTRIBUTING.md' <<'IADD_EOF'
# Contributing

Run one module's tests with `python3 -m unittest tests.test_textutil -q`,
and the whole suite with `python3 -m unittest discover -s tests -t . -q`.
IADD_EOF
mkdir -p "$(dirname 'agentory/README.md')"
cat > 'agentory/README.md' <<'IADD_EOF'
# What IADD keeps in agentory/
IADD_EOF
mkdir -p "$(dirname 'agentory/config.json')"
cat > 'agentory/config.json' <<'IADD_EOF'
{
  "Mode": "shared",
  "Broad gate": "python3 -m unittest discover -s tests -t . -q"
}
IADD_EOF
mkdir -p "$(dirname 'agentory/threads/1790000021-loud-flag/routing.md')"
cat > 'agentory/threads/1790000021-loud-flag/routing.md' <<'IADD_EOF'
# Routing: 1790000021-loud-flag

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/loud-flag |
IADD_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/loud-flag
