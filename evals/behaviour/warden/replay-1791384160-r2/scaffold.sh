set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 1923d2049d604a4684995f33cdb87f819b060aff
git fetch -q --no-tags origin d2b765876c8ba9e1ef1f8f5b9518767f5c2f718f
git checkout -q -b fix/860-a-fix-range-is-its-own-commits-across-a-merge 1923d2049d604a4684995f33cdb87f819b060aff
