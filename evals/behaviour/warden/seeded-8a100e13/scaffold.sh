set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 4279671d8c78df14a51ab1e1430cbc816034fa8b
git fetch -q --no-tags origin 769f2aa4e0fd2f9e35bce48cd0ca16d0339b7076
git update-ref refs/remotes/origin/release/v0.22.2 769f2aa4e0fd2f9e35bce48cd0ca16d0339b7076
git checkout -q -b chore/966-rule-3-decides-on-the-agent-not-one-run 4279671d8c78df14a51ab1e1430cbc816034fa8b
python3 - evals/scripts/noninferiority.py 671 '    if new_total < old_total:' '    if new_total <= old_total:' <<'PY'
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
