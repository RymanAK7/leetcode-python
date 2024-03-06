from src.contains_duplicate.contains_duplicate import Solution

s = Solution()


def test_nums_length_one():
    assert not s.containsDuplicate([109])


def test_nums_length_two():
    assert not s.containsDuplicate([1, 2])
    assert s.containsDuplicate([1, 1])


def test_nums_length_greater_than_two():
    assert s.containsDuplicate([1, 2, 3, 1])
    assert not s.containsDuplicate([1, 2, 3, 4])
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])


def test_nums_large_length():
    assert not s.containsDuplicate(list(range(1, 106)))
