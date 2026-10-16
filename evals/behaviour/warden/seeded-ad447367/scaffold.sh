set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin ad4473676bd665cb3b9d6ece8b30ce9a88c3193a
git checkout -q -b fix/860-a-fix-range-is-its-own-commits-across-a-merge ad4473676bd665cb3b9d6ece8b30ce9a88c3193a
python3 - skills/code-review/scripts/chain_check.py 4647 '    while i < len(tokens):' '    while i <= len(tokens):' <<'PY'
import sys
path, line, old, new = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
with open(path, encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
assert lines[line - 1] == old, f"{path}:{line} is not {old!r}"
lines[line - 1] = new
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
PY
git rm -rq --ignore-unmatch seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds
git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify
