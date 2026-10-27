set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin cdd0ce137490ab1092f44da2baee7f633408dd39
git fetch -q --no-tags origin 5e2e9ad5d4a3b5add6a7c3d83a74363cd11a10b7
git checkout -q -b fix/894-under-automation-the-guard-asks-nobody cdd0ce137490ab1092f44da2baee7f633408dd39
