set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/AgenticSeal.git
git fetch -q --no-tags origin cf10986e728079b6f5e832ec90d4d88f2544ffbc
git fetch -q --no-tags origin dd60a7a048172bf5ed204602c300e0e46a5341d3
git checkout -q -b fix/1150-replay-targets-reads-both-layouts cf10986e728079b6f5e832ec90d4d88f2544ffbc
