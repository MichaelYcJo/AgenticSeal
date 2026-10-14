set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/SpecSeal.git
git fetch -q --no-tags origin 65385bd1edcc280e108e32457d4e9960795ee79f
git fetch -q --no-tags origin 9b5239c6ded482c279f11e28f32479f3289f277a
git checkout -q -b fix/872-whether-a-ledger-line-is-live-has-seven-rules 65385bd1edcc280e108e32457d4e9960795ee79f
