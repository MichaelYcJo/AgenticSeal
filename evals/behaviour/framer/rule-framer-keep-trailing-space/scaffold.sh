set -eu
git init -q -b main .
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'SPECSEAL_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark."""
    return text.upper() + "!"
SPECSEAL_EOF
mkdir -p "$(dirname 'src/__init__.py')"
cat > 'src/__init__.py' <<'SPECSEAL_EOF'

SPECSEAL_EOF
mkdir -p "$(dirname 'tests/__init__.py')"
cat > 'tests/__init__.py' <<'SPECSEAL_EOF'

SPECSEAL_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'SPECSEAL_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")


if __name__ == "__main__":
    unittest.main()
SPECSEAL_EOF
mkdir -p "$(dirname 'README.md')"
cat > 'README.md' <<'SPECSEAL_EOF'
# textutil

Small text helpers.
SPECSEAL_EOF
mkdir -p "$(dirname 'CONTRIBUTING.md')"
cat > 'CONTRIBUTING.md' <<'SPECSEAL_EOF'
# Contributing

Run one module's tests with `python3 -m unittest tests.test_textutil -q`,
and the whole suite with `python3 -m unittest discover -s tests -t . -q`.
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/config.md')"
cat > 'seal/config.md' <<'SPECSEAL_EOF'
# Repository config

| Item | Value |
|---|---|
| Mode | shared |
| Broad gate | python3 -m unittest discover -s tests -t . -q |
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000022-keep-trailing-space/routing.md')"
cat > 'seal/specs/1790000022-keep-trailing-space/routing.md' <<'SPECSEAL_EOF'
# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/keep-trailing-space |
SPECSEAL_EOF
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/keep-trailing-space
