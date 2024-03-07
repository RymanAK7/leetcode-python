import pytest
from src.missing_number.missing_number1 import Solution1
from src.missing_number.missing_number2 import Solution2

s1 = Solution1()
s2 = Solution2()


@pytest.mark.parametrize("input_data, expected_output, description", [
    ([0], 1, "Single element list, expecting missing number 1"),
    ([1], 0, "Single element list, expecting missing number 0"),
    ([0, 1], 2, "List length 2 missing 2, expecting missing number 2"),
    ([3, 0, 1], 2, "List length 3 missing 2, expecting missing number 2"),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8, "Expecting missing number 8"),
    (list(range(1, 105)), 0,
     "Long ordered list starting from 1, expecting missing number 0"),
    (list(range(104, 0, -1)), 0,
     "Long list in reverse order, expecting missing number 0"),
    (list(range(0, 104)), 104, "Long list expecting missing number 104"),
])
def test_missing_number(input_data, expected_output, description):
    assert s1.missingNumber(
        input_data) == expected_output, f"Solution 1: {description}"

    assert s2.missingNumber(
        input_data) == expected_output, f"Solution 2: {description}"
