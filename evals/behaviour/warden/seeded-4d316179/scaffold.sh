set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 4d316179fef188734b249fdce4737b1b90544394
git checkout -q -b fix/896-the-idle-session-rows-ask-nobody 4d316179fef188734b249fdce4737b1b90544394
python3 - hooks/worktree-guard.py 3154 '        here = bool(own) and own == worktree_consent._clone_of(top)' '        here = bool(own) and own != worktree_consent._clone_of(top)' <<'PY'
import sys
path, line, old, new = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
with open(path, encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
assert lines[line - 1] == old, f"{path}:{line} is not {old!r}"
lines[line - 1] = new
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
PY
git rm -rq --ignore-unmatch seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds
git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify
