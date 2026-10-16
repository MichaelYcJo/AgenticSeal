set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 9b644676f92775d1a8fd44cf8a4a03233667f85d
git checkout -q -b fix/858-the-plugin-directory-check-reads-the-directory 9b644676f92775d1a8fd44cf8a4a03233667f85d
python3 - .github/scripts/plugin_directory_check.py 236 '            f"{head} an entry, pinning no commit (source: {url or '"'"'none'"'"'}).",' '            f"{head} an entry, pinning no commit (source: {url and '"'"'none'"'"'}).",' <<'PY'
import sys
path, line, old, new = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
with open(path, encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
assert lines[line - 1] == old, f"{path}:{line} is not {old!r}"
lines[line - 1] = new
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
PY
git rm -rq --ignore-unmatch seal/specs/1791384161-the-plugin-directory-check-reads-the-directory/rounds
git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify
