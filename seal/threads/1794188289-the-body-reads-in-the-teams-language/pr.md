- "**Both language rows of `seal/config.md`, `Commit and pull request language` and `Record language`, are required, and `seal pr-body` refuses to compose a pull request body without either (#1453).**" (`changelog.md` *Fixed*, the first item)
- "A downstream repository whose team writes its pull requests in Korean had neither row." (`changelog.md` *Fixed*, the first item)
- "An absent row read as English and nothing said so, so its records and its pull request bodies came out in English, and every party passed them." (`changelog.md` *Fixed*, the first item)
- "No commit is refused for the rows: a commit in a repository without them is still written in English." (`changelog.md` *Fixed*, the first item)
- "**First setup and the start of a work item ask for the two rows.**" (`changelog.md` *Fixed*, the second item)
- "Where nobody is there to answer, the orchestrator writes both rows as the language of the titles, `English` where there are none, and `routing.md` *Why this way* says so in one sentence." (`changelog.md` *Fixed*, the second item)
- "**Where the two rows name different languages, the pull request body opens in the team's language.**" (`changelog.md` *Fixed*, the third item)
- "`seal pr-body` writes it above `pr.md`, so the body opens with that file, then `pr.md`, then the heading and the records' copy." (`changelog.md` *Fixed*, the third item)
- "Where the rows name one language, the body opens with `pr.md` as before." (`changelog.md` *Fixed*, the third item)
- "Until both rows are written, `seal pr-body` refuses, and the pull request check's body arm, where the workflow runs this release, fails a ready pull request at `seal/config.md`." (`changelog.md` *Updating*)
- "The pull request's title takes `fix:`, and the kind that came closest is `feat:`." (`frame/plan.md` *Judgments of the run*, the prefix row)
- "whether a downstream repository whose `Record language` is `English` and whose `Commit and pull request language` is `Korean` gets a body that opens with `pr.ko.md` and passes both `seal pr-body --check` and the pull request check's body arm; the cases build such a repository in a fixture, and no real repository has run the installed release" (`gaps.md` *Not verified*, the second row)

Closes #1453.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
