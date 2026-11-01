set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/AgenticSeal.git
git fetch -q --no-tags origin 1090b7c3b56a4f99cbd4d748d9429eda2171ee70
git fetch -q --no-tags origin 5560c742e2c40f11855869021e343533e50ca960
git update-ref refs/remotes/origin/release/v0.27.0 5560c742e2c40f11855869021e343533e50ca960
git checkout -q -b fix/1126-settle-keeps-a-gaps-file-anywhere 1090b7c3b56a4f99cbd4d748d9429eda2171ee70
python3 - skills/settle/scripts/settle.py 537 '            if place is None or not os.path.isfile(path):' '            if place is None and not os.path.isfile(path):' <<'PY'
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
git update-ref refs/remotes/origin/release/v0.27.0 5560c742e2c40f11855869021e343533e50ca960
git reflog expire --expire=now --all
rm -f .git/FETCH_HEAD
git gc -q --prune=now
