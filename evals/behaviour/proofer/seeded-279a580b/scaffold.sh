set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 7795f390014750b1a9917aa9d0e5dd0ff9ad0270
git fetch -q --no-tags origin 5623d7282eddd20b5949c4643ca9ee2808d143dd
git update-ref refs/remotes/origin/release/v0.21.0 5623d7282eddd20b5949c4643ca9ee2808d143dd
git checkout -q -b feat/837-a-records-finding-closes-once-at-the-runs-end 7795f390014750b1a9917aa9d0e5dd0ff9ad0270
python3 - skills/code-review/scripts/chain_check.py 1865 '        if found is None or NOTE not in found.group(0):' '        if found is None and NOTE not in found.group(0):' <<'PY'
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
GIT_COMMITTER_NAME="$(git log -1 --format=%cn)" GIT_COMMITTER_EMAIL="$(git log -1 --format=%ce)" GIT_COMMITTER_DATE="$(git log -1 --format=%cI)" git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify
git remote remove origin
git update-ref refs/remotes/origin/release/v0.21.0 5623d7282eddd20b5949c4643ca9ee2808d143dd
git reflog expire --expire=now --all
rm -f .git/FETCH_HEAD
git gc -q --prune=now
