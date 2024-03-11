import pytest
from src.find_disappeared_numbers.find_disappeared_numbers1 import Solution1

from src.find_disappeared_numbers.find_disappeared_numbers2 import Solution2

s1 = Solution1()
s2 = Solution2()


@pytest.mark.parametrize("input_data, expected_output, description", [
    ([1], [], "Input list length 1"),
    ([1, 1], [2], "Input list length 2"),
    ([2, 2], [1], "Input list length 2"),
    ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6], "List length 8"),
    (list(range(5, 105)) + [5, 6, 7, 8, 9], [1, 2, 3, 4, 105], "Long list")
])
def test_find_disappeared_numbers(input_data, expected_output, description):
    assert s1.findDisappearedNumbers(
        input_data) == expected_output, f"Solution 1: {description}"

    assert s2.findDisappearedNumbers(
        input_data) == expected_output, f"Solution 2: {description}"
