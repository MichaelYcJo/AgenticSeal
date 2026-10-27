# Security

## Reporting

Use **[private vulnerability reporting](https://github.com/MichaelYcJo/AgenticSeal/security/advisories/new)**.
It is enabled on this repository, so a report reaches the maintainer without
being visible to anyone else, and the fix and the disclosure can be prepared
in the same place. Please do not open a public issue for a suspected
vulnerability — an issue is the disclosure, and it happens before there is
anything for a reader to upgrade to.

Expect an acknowledgement within a week. There is no bounty; there is a
credit line in the advisory unless you ask for none.

## What this project is, and where its risk actually sits

SpecSeal is a Claude Code plugin. What ships is Python that runs in two places
a reader should keep separate:

- **`skills/*/scripts/`** — the checkers, run from CI and from a terminal
  (`seal fold`, `seal unverified`, `seal pact` and the rest), which read a
  repository's records and the files those records name.
- **`hooks/`** — gates the harness invokes around commits, branch switches and
  session start. Some of them run without anybody asking, which is the whole
  point of a gate and also the reason a defect in one is worth more than the
  same defect in a checker.

The records are committed files, so writing one normally requires write
access to the repository, and in an ordinary project a malicious record crosses
no privilege boundary that a malicious commit does not cross already. Two
situations break that assumption, and they are the ones worth reporting:

1. **A repository whose CI runs these commands on pull requests.** A pull
   request from a fork can add records. What a fork's workflow run holds — a
   token, an environment, a filesystem — is then the surface.
2. **A developer with an untrusted repository checked out locally.** Running
   a checker, or a hook firing on its own, acts on that repository's content
   on a real machine. This is the case that can happen without the developer
   deciding to do anything.

A report that names one of those two is a report about a real boundary. A
report that assumes the attacker already commits to the repository under
review is describing something this project does not defend against, and
saying so plainly in the report saves a round trip.

## What is in scope

Path handling that leaves the repository being checked; anything a hook does
to a tree the user did not ask it to touch; a gate that reports a pass it did
not establish (**a check that fails open is a security defect here, not a
correctness one**, and each gate's test file holds its cases for that class);
command construction that reaches a shell; and any write that
follows a link or changes a mode the user did not choose.

## What is not

Findings that require the reporter to already control the repository under
review, unless they reach one of the two situations above. Denial of service
against a checker whose whole runtime is measured in milliseconds. Anything
in `seal/`, which holds records rather than code.

## Supported versions

The latest release is supported. Advisories name the versions they affect and
the version that carries the fix; nothing older is patched in place, because
the fix is always available by upgrading.
