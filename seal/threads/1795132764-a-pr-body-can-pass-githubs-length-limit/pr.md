- "In which unit does GitHub count a pull request body's 65,536 characters? The one source read reports code points, and it is a community measurement" (`frame/questions.md`, row Q1, the Question cell)
- "UTF-16 code units, counted as D1 states" (`frame/questions.md`, row Q1, the Default until answered cell)
- "Code points or UTF-16 code units: D1's UTF-16 count fits under both, and the code stands as written. UTF-8 bytes: a body in Korean passes GitHub's limit at about a third of `LIMIT`, and D1's count becomes `len(text.encode("utf-8"))`" (`frame/questions.md`, row Q1, the Options cell)
- "Not taken. The fold line names the record's path in the work item, as every other fixed line does, and the reader opens it in the branch the pull request shows" (`frame/plan.md` *Alternatives considered*, row 3, the Verdict cell)
- "CI checks out the pull request's merge commit, so the commit `compared` reads there is not the branch head the body was written at, and the body arm refuses every folded body" (`frame/plan.md` *Alternatives considered*, row 3, the Failure scenario cell)
- "`compose` takes the first part as `first_part`'s list, `parts`, not as one text, `head`." (`trail/phases/phase-1.md` *What this phase found*, the second item)
- "`chain_check.py#body`'s docstring now names the fold's sentence as a notice, a departure from *Scope*'s Out list." (`trail/phases/phase-1.md` *What this phase found*, the seventh item)
- "For records past GitHub's limit no such body could be sent, so the behaviour was wrong against that rule, and the fold makes it match." (`frame/plan.md` *Judgments of the run*, the row titled "The title takes `fix:`")

Closes #1559.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
