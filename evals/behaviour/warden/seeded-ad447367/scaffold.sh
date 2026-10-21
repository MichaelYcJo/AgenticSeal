set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 7e68ed00f83d53a36ffdd6e2347e015b8f0d1168
git fetch -q --no-tags origin 5623d7282eddd20b5949c4643ca9ee2808d143dd
git update-ref refs/remotes/origin/release/v0.21.0 5623d7282eddd20b5949c4643ca9ee2808d143dd
git checkout -q -b fix/860-a-fix-range-is-its-own-commits-across-a-merge 7e68ed00f83d53a36ffdd6e2347e015b8f0d1168
python3 - skills/code-review/scripts/chain_check.py 4530 '    while i < len(tokens):' '    while i <= len(tokens):' <<'PY'
import sys
path, line, old, new = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
with open(path, encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
assert lines[line - 1] == old, f"{path}:{line} is not {old!r}"
lines[line - 1] = new
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
PY
git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify
git reflog expire --expire=now --all
rm -f .git/FETCH_HEAD
git gc -q --prune=now
