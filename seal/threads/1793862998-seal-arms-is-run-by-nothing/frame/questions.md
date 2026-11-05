# Questions for the planner: 1793862998-seal-arms-is-run-by-nothing

The ticket left these judgments open, and the tree answered each. Their grounds stand where each line points, and nobody reopens them here.

- Whether the policy root is edited in place or through `## Rule changes`: `frame/plan.md` *Alternatives considered* A5, with design G7.
- Where `clear_bytecode_cache`, `restore` and `command_words` live once `arm_check.py` goes: `frame/plan.md` *Alternatives considered* A2.
- Whether the `arms-grammar` job is kept for the moved cases until #1065: `frame/plan.md` *Alternatives considered* A6, with design *Not covered until #1065*.
- Whether `.test_durations` drops the entries of the cases that leave: `frame/plan.md` *Alternatives considered* A7.
- Which script the cases of design G10 take as their example of a subcommand: design *Scope* item 7.

No row below needs a person. The owner's decision in #1393 settles what the product should be.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does `clear_bytecode_cache` keep its `cwd=None` reading once it lives in `mutation_check.py`, where every call passes `cwd` (design G8)? The tree cannot answer it, because it turns on what the moved cases need when phase 1 writes them, and no probe can show that before they exist. | the work | Keep it: the move changes no behaviour, and the absolute-prefix half of the moved case still drives it. Remove it: `cwd` becomes required, and the moved case loses the half that calls with no `cwd`. | Keep it as moved. Phase 1 records the call in its phase record. | open |
