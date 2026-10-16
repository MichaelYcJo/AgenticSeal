set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 97c910d5bdaddf61aece9018c465857883978d37
git fetch -q --no-tags origin 602fb87b709abe077db23ec520df331284754242
git checkout -q -b chore/834-every-reader-and-record-is-inventoried 97c910d5bdaddf61aece9018c465857883978d37
