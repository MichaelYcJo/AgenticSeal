set -eu
git init -q .
git remote add origin https://github.com/MichaelYcJo/AgenticSeal.git
git fetch -q --no-tags origin 837ac652efb7c3bbd6b56f78ffab9d4476967daf
git fetch -q --no-tags origin bc44b3f5a3e408156e4e4942c3093632e2ca6ae2
git checkout -q -b fix/1200-project-rules-live-in-the-repository 837ac652efb7c3bbd6b56f78ffab9d4476967daf
