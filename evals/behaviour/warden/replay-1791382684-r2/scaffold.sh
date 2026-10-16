set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 7ef6abbf3f7413e68761ea2046723f9093f3ff38
git fetch -q --no-tags origin a6b0ac200865f1b12662c2a6b5f1f448338d529c
git checkout -q -b chore/834-every-reader-and-record-is-inventoried 7ef6abbf3f7413e68761ea2046723f9093f3ff38
