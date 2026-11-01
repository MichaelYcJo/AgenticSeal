set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/AgenticSeal.git
git fetch -q --no-tags origin ab958884529f986a6b75fd23e8b38e954b6148d9
git fetch -q --no-tags origin 48d035aa65cb566d32fd41972466e0825db54b9a
git update-ref refs/remotes/origin/release/v0.27.1 48d035aa65cb566d32fd41972466e0825db54b9a
git checkout -q -b fix/1225-a-linked-memo-named-as-the-argument ab958884529f986a6b75fd23e8b38e954b6148d9
python3 - skills/verify/scripts/unverified_check.py 1739 '            if os.path.realpath(path) == path:' '            if os.path.realpath(path) != path:' <<'PY'
import sys
path, line, old, new = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
with open(path, encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
text = lines[line - 1]
end = "\r" if text.endswith("\r") else ""
assert text[: len(text) - len(end)] == old, f"{path}:{line} is not {old!r}"
lines[line - 1] = new + end
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
PY
GIT_COMMITTER_NAME="$(git log -1 --format=%cn)" GIT_COMMITTER_EMAIL="$(git log -1 --format=%ce)" GIT_COMMITTER_DATE="$(git log -1 --format=%cI)" git commit -q -a --amend --no-edit --no-verify
git remote remove origin
git update-ref refs/remotes/origin/release/v0.27.1 48d035aa65cb566d32fd41972466e0825db54b9a
git reflog expire --expire=now --all
rm -f .git/FETCH_HEAD
git gc -q --prune=now
