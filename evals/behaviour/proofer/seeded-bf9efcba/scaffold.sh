set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/AgenticSeal.git
git fetch -q --no-tags origin b2e4ca18adb220c20aee9101b0d2fa74cf069676
git fetch -q --no-tags origin a92c358b819870cdb4d292247856e1b902fe7825
git update-ref refs/remotes/origin/release/v0.27.1 a92c358b819870cdb4d292247856e1b902fe7825
git checkout -q -b fix/19-row-deletion-check-and-a-symlink b2e4ca18adb220c20aee9101b0d2fa74cf069676
python3 - skills/verify/scripts/unverified_check.py 1605 '            if at is None or at.split("/")[0] == "..":' '            if at is None or at.split("/")[0] != "..":' <<'PY'
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
git update-ref refs/remotes/origin/release/v0.27.1 a92c358b819870cdb4d292247856e1b902fe7825
git reflog expire --expire=now --all
rm -f .git/FETCH_HEAD
git gc -q --prune=now
