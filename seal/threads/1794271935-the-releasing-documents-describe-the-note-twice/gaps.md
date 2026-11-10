# Closing memo: 1794271935-the-releasing-documents-describe-the-note-twice

## Not verified

- nothing
  why: phase 1 changed prose, one workflow comment and one case; each claim it rests on was run or read, as `trail/phases/phase-1.md` records, and the broad gate is the orchestrator's.

## Not done

Two sentences of `docs/releasing/branch-and-release.md` *Cutting a release*
still describe how the directory serves a listing, and phase 1 left both as
they stand. In the `dist` paragraph, the workflow "pushes without force,
because the directory serves a scanned commit of the branch it tracks", and
in the paragraph **A third reader of those commits is outside this
repository.**, "a plugin submitted at its developer portal is served from a
scanned commit of the branch or tag the submission tracks", followed by
"this plugin's submission tracks `dist`". Each states how the directory
treats a submission and which branch this plugin's submission names, which
stays true while the listing is on hold, and neither says the directory
takes, lists or serves this plugin's versions, which is what
`frame/design.md` *Scope* item 3 removes. The proofer reads both against
that item.
