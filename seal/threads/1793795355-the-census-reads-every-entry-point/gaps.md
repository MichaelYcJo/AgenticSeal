# Closing memo: 1793795355-the-census-reads-every-entry-point

## Not verified

| Item | Who must answer |
|---|---|
| The seventeen repaired entry points, run under a cp949, cp932 or cp936 console on Windows. The census reads each answer from source, and no case runs these scripts under a console that cannot encode what they print | the repository owner, on a Windows console |

## Not done

The `.test_durations` keys for the renamed case
`test_accepts_the_call_first_a_module_and_a_file_outside_hooks` and the
removed `test_a_release_script_run_on_its_own_gives_the_answer_streams_holds`
were left as they stand. The file is measurement data that CI's `durations`
job writes from the Windows shards (`.github/workflows/test.yml:208`). A key
for a case that is no longer collected should price nothing, because the
split divides the cases it collects; that was read, not run.

`.github/scripts/label_merged_on_release_branch.py` and
`release_completeness_check.py` spell the loop, although each loads
`close_issues_on_release.py` at import, which puts `hooks/lib/` on
`sys.path` and imports `console`. Design *Scope* item 5 sends a file that
puts `hooks/lib/` on `sys.path` at import to `console.to_utf8()`, and phase
1 read that as the file's own imports. Both loops give `STREAMS`' answer,
which is what the census reads, and changing their form is outside phase
2's row. `hooks/lib/console.py` counts them among the scripts that reach
`hooks/lib/` at import and give no reason for the loop. Whether they should
make the call is the proofer's to judge at review (phase 2's record).
