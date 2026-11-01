set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/AgenticSeal.git
git fetch -q --no-tags origin 968f5ac4313f69ba2273c2653bb3997fb3684f45
git fetch -q --no-tags origin 15a5ce66a01cf4b45ae34b89ac7c35acca12fc02
git update-ref refs/remotes/origin/release/v0.27.0 15a5ce66a01cf4b45ae34b89ac7c35acca12fc02
git checkout -q -b feat/1198-fields-stand-in-marked-blocks 968f5ac4313f69ba2273c2653bb3997fb3684f45
python3 - hooks/lib/blocks.py 451 '        if at_start and line in walked.opens' '        if at_start or line in walked.opens' <<'PY'
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
git update-ref refs/remotes/origin/release/v0.27.0 15a5ce66a01cf4b45ae34b89ac7c35acca12fc02
git reflog expire --expire=now --all
rm -f .git/FETCH_HEAD
git gc -q --prune=now
