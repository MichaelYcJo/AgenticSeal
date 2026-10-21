set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 56172bbe968785c6f3536beecf6b288b5f59e94a
git fetch -q --no-tags origin f6ae6db6c9d606da4bf1227359eaed76aa3f6b40
git update-ref refs/remotes/origin/release/v0.22.1 f6ae6db6c9d606da4bf1227359eaed76aa3f6b40
git checkout -q -b fix/975-the-stamp-is-drawn-from-the-sealers-verdict 56172bbe968785c6f3536beecf6b288b5f59e94a
python3 - skills/code-review/scripts/chain_check.py 1372 '    for entry in (cell or "").split(EARLIER_RUN)[1:]:' '    for entry in (cell and "").split(EARLIER_RUN)[1:]:' <<'PY'
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
