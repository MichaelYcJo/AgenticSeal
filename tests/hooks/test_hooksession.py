"""`hooks/lib/hooksession.py`: which variable names the session.

The module holds one constant and no function, so the census is its only
case. `skills/implement/scripts/seal.py`'s cases read the variable it names.
"""

from conftest import census_case

TARGET = "hooks/lib/hooksession.py"


test_census = census_case(TARGET)
