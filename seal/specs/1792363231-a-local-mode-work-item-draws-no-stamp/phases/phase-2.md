# 1792363231-a-local-mode-work-item-draws-no-stamp — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | bf996b89 |


## What this phase was asked

Build the gate after the reframe at a7572788, approved at f6ad0b2c. That
means `hooks/sealer-stamp-queue.py` in `dispatch.GROUPS["post-edit"]`. It
returns, on a path that does not match, before any `git` call or import, and
it prints the `systemMessage`. Add a `sealer-stamp-queue` row to both
READMEs' hook tables. Build test-first. Before starting, re-read `spec.md`,
`plan.md` and `questions.md` at a7572788. Q1 is answered (a) and Q2 is
answered (b). Q3, the Windows `realpath`, is this phase's. Q4 and the
refusal record are phase 3's.

## What this phase found

**The frame holds for the gate.** The reframe changed nothing about it. The
plan's coordinates still match the tree. `GROUPS["post-edit"]` held
`lint-python.py` and `session-lease.py`. `hooks/hooks.json` runs that group
at `PostToolUse` for `Write|Edit|NotebookEdit`, so it needed no change.
`merge` carries one gate's `systemMessage` through as the group's output.

**The README row made two other sentences false in each edition, and they
were rewritten in the same commit (contract §19).** One is the count of
gates that wake on a condition: "Eight of the eleven" became "Nine of the
twelve", and "게이트 열하나 중 여덟" became "게이트 열둘 중 아홉". The other
is the opt-in list in the `seal/` row: "the stamp hook" became "the two
stamp hooks", and "도장 훅" became "도장 훅 둘".
`test_both_readmes_list_the_stamp_hook` pins the new words, asserts that
the old count is gone, and asserts both rows. It is not among the fourteen
cases S10 keeps untouched.

**What phase 4 still owes in the READMEs.** The `sealer-stamp` row and the
side-effect sentence still say only that the stamp is queued at the commit.
The #975 S11 half of `test_both_readmes_list_the_stamp_hook` pins those
phrases. Phase 4 rewrites both, together with the refusal record's
directory.

**How the order is proved.** S6 asks that nothing is loaded and no `git`
runs before the path's shape matches. The gate's only way to `git` is
`seal_stamp.py`, which `load_stamp` loads. So
`test_the_edit_gate_is_silent_off_a_guarantee` runs the gate in-process
with `load_stamp` replaced by a recorder. For each silent given it asserts
that the recorder was never called. A `Write` of the guarantee is the
control that shows the recorder is reached. The same case also runs each
given through `dispatch.py post-edit`, and asserts no output and no values
file.

**Where the drawing case lives.** S10 forbids editing
`test_the_main_sessions_stop_draws_each_undrawn_file_once`. So the draw of a
file this gate wrote is asserted in
`test_the_edit_gate_queues_a_local_mode_sealed_guarantee`: one `Stop` draws
it, and a second `Stop` prints nothing. S5's case from phase 1 also gained
its gate half: a `Write` of a shared-mode guarantee through the group says
nothing and queues nothing.

**Every branch of the gate was mutated at 7be9a83f, one `mutation-check`
run each.** Eight runs were made. Seven were caught by a case: the tool
check, the session check, the shape call, the shape pattern, the message,
the silence on a raise, and the silence on a payload that is not JSON. The
separator mapping survived. It mapped `os.sep` and then also every
backslash. On POSIX the second replacement only rewrites a literal
backslash in a file name, so bf996b89 removed it. The `os.sep` mapping
remains. It acts only on Windows, where no case here can reach it.

**Q3 is not settled on this machine.** The gate's `os.sep` mapping and the
writer's two `realpath` comparisons from phase 1 are the code the Windows
leg judges. Every case of phases 1 and 2 runs on that leg. `questions.md`
Q3 names the work as its answerer, through CI's Windows leg. That leg
cannot run here, so Q3 stays open for the orchestrator to read off CI.

**A stale count found and left alone.** The comment at `hooks/dispatch.py`
below `if __name__ == "__main__":` says "Seven of the eleven `__main__`
blocks in this tree". Seventeen `hooks/*.py` files held such a block before
this work, and the new gate makes eighteen. The count was already wrong, so
this phase did not touch it.

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
