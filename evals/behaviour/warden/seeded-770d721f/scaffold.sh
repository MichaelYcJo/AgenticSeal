set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 770d721f7c4d5d11c1e347ba4171c1e40cf7f478
git checkout -q -b fix/873-survivor-check-reads-a-range-as-its-own-commits 770d721f7c4d5d11c1e347ba4171c1e40cf7f478
python3 - skills/code-review/scripts/survivor_check.py 528 '    if separator(spec) != "..":' '    if separator(spec) == "..":' <<'PY'
import sys
path, line, old, new = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
with open(path, encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
assert lines[line - 1] == old, f"{path}:{line} is not {old!r}"
lines[line - 1] = new
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
PY
git rm -rq --ignore-unmatch seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/rounds
git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify
