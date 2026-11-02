# implement, a work item across repositories

The orchestrator opens this file where a work item commits in more than one
repository, and not otherwise. `skills/implement/orchestration.md` holds the
rest of starting a work item.

## Orchestrator: a work item that commits in more than one repository

The routing question is still asked once, in the shape
`skills/implement/orchestration.md` *Orchestrator: how the work is routed*
states, and every answer it writes goes into every repository the work item
commits in. Asking it again per repository is the mid-run question this
section exists to remove, arriving once per checkout.

**Only a gated repository gets a declaration.** A gated repository is one
with a `seal/` root at either place (contract rule 11). Write
`seal/threads/<work-item-id>/routing.md` into each one before that
repository's first edit, each naming that repository's own branch, each in a
command of its own, and commit each with that repository's absolute path
written out after `git -C` (contract rule 16). A repository with no root is not
opted in by this step: writing the file would create its root, and creating
a root is the bootstrap's decision and the person's. Name such a repository
in the handback and write nothing into it.

**One id, minted once, names the directory in every repository.** Take
`date +%s` once, pick one slug, and use the resulting directory name in every
repository. The id is what every share is keyed by, its changelog
fragment among them. A directory named differently in each repository would
have to be renamed later, and the rename moves the fragment with it.
Nothing checks this, because nothing can tell an id minted twice from a
signer's own work item that cites the pact without changing it, and that
second case is legitimate and common.

**Where the repositories keep a contract together, they sign a pact.**
`docs/the-pact.md` holds the model. Two conditions decide it, and both must
hold: the work item commits in more than one repository, and those
repositories share contract. A sentence is contract when another
repository's code would be wrong if it changed. Where both hold:

- the one copy of the contract is `seal/pact.md` in one of the repositories,
  begun from `templates/setup/pact.md` and written by the build there, framed by
  a work item's design in that repository. That repository is the pact's repository;
- every other repository of the work item is a signer, and the orchestrator
  writes one row into its `seal/config.md` where it is absent: `Pact`, the
  origin remote URL of the pact's repository. `templates/setup/config.md` *Pact*
  documents it. The pact's repository needs no row, because it is identified
  by holding `seal/pact.md`;
- each signer cites the clauses it was built against as pact anchors, one
  row each of a `| Pact | Clause | Hash |` table in its `frame/design.md`,
  the `Pact` cell holding the pact's origin URL; `seal pact`, run at the
  pact's repository, reads every signer and says where they disagree.

Where only the first condition holds, the repositories get their
declarations and nothing else: no pact, and no `Pact` row.
