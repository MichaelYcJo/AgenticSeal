set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 279a580b09e79d65763dd4df77d4a1350e4e9940
git checkout -q -b feat/837-a-records-finding-closes-once-at-the-runs-end 279a580b09e79d65763dd4df77d4a1350e4e9940
python3 - skills/code-review/scripts/chain_check.py 1877 '        if found is None or NOTE not in found.group(0):' '        if found is None and NOTE not in found.group(0):' <<'PY'
import sys
path, line, old, new = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
with open(path, encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
assert lines[line - 1] == old, f"{path}:{line} is not {old!r}"
lines[line - 1] = new
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
PY
git rm -rq --ignore-unmatch seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds
git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify
