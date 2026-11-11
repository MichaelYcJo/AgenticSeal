# Closing memo: 1794383423-settle-reprints-every-earlier-judgment

## Not verified

| Item | Who must answer |
|---|---|
| Phase 1: `versions` reads the commit a nested annotated tag peels to through `for-each-ref`'s `%(*objecttype)` and `%(*objectname)`, which git 2.50.1 peels to the commit; whether an older git peels one level only, so that a nested version tag labels nothing where `git tag --contains` counted it, was not run | the proofer, by `git for-each-ref --format='%(*objecttype)'` over a nested tag on an older git |

## Not done

Phase 1: `blobs` reads one header per name from `git cat-file --batch`, and
an output that ends before the last name raises `ValueError`, not the
`RuntimeError` the section names as not read. Git writes one answer per input
line and exits non-zero where it stops, so a short output with exit 0 was
not guarded against; the design's *Scope* item 6 names a failing call, and
this is not one.
