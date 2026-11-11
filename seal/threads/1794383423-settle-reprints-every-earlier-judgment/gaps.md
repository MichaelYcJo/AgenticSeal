# Closing memo: 1794383423-settle-reprints-every-earlier-judgment

## Not verified

| Item | Who must answer |
|---|---|
| closed Phase 1: `versions` reads the commit a nested annotated tag peels to through `for-each-ref`'s `%(*objecttype)` and `%(*objectname)`, which git 2.50.1 peels to the commit; whether an older git peels one level only, so that a nested version tag labels nothing where `git tag --contains` counted it, was not run | round 1, finding 1, ran it: git 2.39.3 peels one level. `0a354b5a7` peels each version tag with `^{}` through `git cat-file --batch-check`, and `Test_versions::test_accepts_a_version_tag_of_a_tag_at_the_commit_it_peels_to` failed with git 2.39.3 first on PATH before it and passes with it on 2.39.3 and 2.50.1 |
| Phase 2: whether the settling session reads the bounded section and runs `seal settle --all-earlier` where a kind it reads may have come before the two newest removing commits, as step 5 of `skills/settle/SKILL.md` says (design S8); no case holds it | the owner, at the next settle |

## Not done

Phase 1: `blobs` reads one header per name from `git cat-file --batch`, and
an output that ends before the last name raises `ValueError`, not the
`RuntimeError` the section names as not read. Git writes one answer per input
line and exits non-zero where it stops, so a short output with exit 0 was
not guarded against; the design's *Scope* item 6 names a failing call, and
this is not one.

Phase 2: the line that counts the older removing commits names
`seal settle --all-earlier` alone, and does not carry the `--released-at`
the dry run was given. A settling session that ran the dry run at another
ref adds that ref when it runs the flag. The design's *Data & interfaces*
gives the line as the bare command, and step 2 of the procedure in
`skills/settle/SKILL.md` runs the dry run at the default ref, which the bare
command reads too, so the line prints no ref.
