- "**A repository whose own `seal/` belongs to something else, such as a Python package, can keep its records shared, under `agentic-seal/` (#1059).**" (`changelog.md` *Added*, the first item)
- "Before this release, first setup that met a `seal/` whose `README.md` does not open with the marker wrote nothing into it and put the root under the git directory, in local mode. Such a team could not share its records or run the pull request checks." (`changelog.md` *Added*, the first item)
- "The root in force is read in this order: a marked `seal/`, a marked `agentic-seal/`, then the local root under the common git directory, which keeps the name `seal`." (`changelog.md` *Added*, the first item)
- "A repository whose `seal/` carries the marker reads it as before." (`changelog.md` *Added*, the first item)
- "**Every command and check reads the records under `agentic-seal/` where the root has that name (#1059).**" (`changelog.md` *Added*, the second item)
- "**The text keeps calling the root `seal/`, and one sentence defines the name (#1059).**" (`changelog.md` *Added*, the third item)
- "A census in `tests/censuses.py` refuses a string constant that spells either name in any module outside `lib/optin.py`, and three cases in `tests/behaviour/test_no_document_names_the_old_roots.py` hold the second name to the core's sentence and to one line of each README." (`changelog.md` *Added*, the third item)
- "Updating: nothing to do for a repository whose root is a marked `seal/`. A repository that first setup put in local mode because its own `seal/` stood there can run `seal mode shared`, which moves the root to `agentic-seal/` and stages it." (`changelog.md`)

Closes #1059.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
