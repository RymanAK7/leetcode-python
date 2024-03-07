from typing import List


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        elements = set(nums)
        missing_element = next(
            (i for i in range(len(nums)) if i not in elements), None)
        return missing_element if missing_element is not None else len(nums)


'''
time complexity : O(n)
space complexity : O(n) from creating a set from the list

where n is length of input list nums

'''
