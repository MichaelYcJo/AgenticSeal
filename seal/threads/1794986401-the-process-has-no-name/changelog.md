### Changed

- **The plugin's whole process is named the AgenticSeal process (#1557).** Everything the plugin does with one issue, from the routing question to the sealer's guarantee, had no name another repository could cite. The README and the core called it "the workflow", a word the same files also used for a GitHub Actions workflow, and a repository documenting the plugin built a name from "seal" and "review chain" and translated it word by word. Both READMEs now define the name near the top, give the Korean form "AgenticSeal 프로세스", and say a product name is not translated. The plugin's description, the core, `CLAUDE.md`, `CONTRIBUTING.md`, the `seal/README.md` template, the pull-request check's header and `lib/optin.py`'s docstrings use the name wherever "workflow" meant the process. Where "workflow" names a GitHub Actions workflow, it stays.
- The version moves to 0.38.3.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-18 | `skills/core/SKILL.md`: the opening sentence names and defines the AgenticSeal process, the heading *The first value* reads *efficient development through the AgenticSeal process*, and the core says "GitHub Actions workflow" where it means one | The core called the process "the workflow", the word it also used for the GitHub Actions workflow that runs the pull request's check | https://github.com/MichaelYcJo/AgenticSeal/issues/1557 |
| 2026-11-18 | `CLAUDE.md` cites the core's renamed heading | The citation follows the heading | https://github.com/MichaelYcJo/AgenticSeal/issues/1557 |
