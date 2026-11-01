set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/AgenticSeal.git
git fetch -q --no-tags origin 6ff6df90533086283226c5abda03c67e2ee9b76a
git fetch -q --no-tags origin 39c3bf24b7e295b5880c83ecc2f8006208282693
git checkout -q -b chore/1167-judgment-where-meaning-is-the-question 6ff6df90533086283226c5abda03c67e2ee9b76a
