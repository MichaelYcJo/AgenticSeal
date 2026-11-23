"""`evals/scripts/behaviour.py`, the case writer the generators share.

Its writers are held by the cases of the scripts that call them:
`tests/evals/test_rule_cases.py`, which reads each generated grader back
through `tests/workflows.py#front_matter`, and
`tests/evals/test_noninferiority.py`. This file holds the census over the
script.
"""

from conftest import census_case

TARGET = "evals/scripts/behaviour.py"

test_census = census_case(TARGET)
