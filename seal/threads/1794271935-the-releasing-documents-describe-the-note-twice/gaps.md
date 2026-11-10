# Closing memo: 1794271935-the-releasing-documents-describe-the-note-twice

## Not verified

- nothing
  why: phase 1 changed prose, one workflow comment and one case, and phase 2 renamed four headings, rewrote their citations and one `--help` line, and changed prose; each claim either rests on was run or read, as `trail/phases/phase-1.md` and `trail/phases/phase-2.md` record, and the broad gate is the orchestrator's.

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

The docstring of
`tests/behaviour/test_release_hygiene.py#test_the_timer_sweep_survives_a_tracked_file_the_tree_deleted`
opens "#432's class in the module the release checklist runs at step 3."
The checklist held no step 3 at the start of this work, and no box of it
runs that module: it names the module only in its opening paragraph and on
two `check:` lines. Phase 2 left the sentence as it
stands. It names none of the four headings `frame/design.md` *Scope* item 5
renames, so it is outside that item, and rewriting it needs a fact this
work item did not establish: which act of a release meets that sweep first,
if any. The scenario S4 grep, `step (0|2b|5|6)`, does not reach it.
