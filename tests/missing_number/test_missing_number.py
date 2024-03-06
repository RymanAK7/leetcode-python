from src.missing_number.missing_number import Solution

s = Solution()


def test_nums_length_one():
    assert s.missingNumber([0]) == 1
    assert s.missingNumber([1]) == 0


def test_nums_length_greater_than_or_equal_two():
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([3, 0, 1]) == 2
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_nums_large_length():
    assert s.missingNumber(list(range(1, 105))) == 0
    assert s.missingNumber(list(range(104, 0, -1))) == 0
    assert s.missingNumber(list(range(0, 104))) == 104
