### Changed

- **Under `automation`, a worktree creation in another clone no longer
  reaches the person (#903).** The `automation` answer consents to a
  `git worktree add` only in the clone it was given in. A creation in
  another clone, where the session had created no worktree, among idle
  sessions or where sessions cannot be counted, told the model to put two
  options to the person with `AskUserQuestion`, and asked the person
  directly on every attempt after, in a run whose person had said nobody
  would answer.

  1. Under that answer both rows now refuse the creation to the model on
     every attempt. The refusal says the answer consents to a creation only
     in the clone it was given in and that nobody is at the keyboard to
     choose, names no way on, no question tool and no token, and says that
     re-issuing the command unchanged meets the same refusal.
  2. A person sees nothing new. Without the press both rows give the same
     two options and the same prompt after them, word for word, and in the
     clone the answer was given in a creation is allowed as before.
  3. On Windows, where sessions can never be counted, every Bash creation
     in another clone under the press is this refusal.
