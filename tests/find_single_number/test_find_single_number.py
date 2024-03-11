import pytest
from src.find_single_number.find_single_number1 import Solution1
from src.find_single_number.find_single_number2 import Solution2


s1 = Solution1()
s2 = Solution2()


@pytest.mark.parametrize("input_data, expected_output, description", [
    ([100], 100, "Input list length 1"),
    ([2, 2, 1], 1, "Input list length 3"),
    ([4, 1, 2, 1, 2], 4, "Input list length 5"),
    ([-100, 200, -100, -300, 200], -300, "List with negative numbers"),
    (list(range(-1000, 1000)) + list(range(-1000, 1000)) +
     [1000], 1000, "Long input list")
])
def test_find_single_number(input_data, expected_output, description):
    assert s1.singleNumber(
        input_data) == expected_output, f"Solution 1: {description}"

    assert s2.singleNumber(
        input_data) == expected_output, f"Solution 2: {description}"
