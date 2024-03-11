from typing import List


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


'''
Bitwise operation helps us improve memory space

The time complexity is O(n), where n is the
length of the nums list. It iterates
through the list once.

The space complexity is O(1), it uses a constant
amount of extra space regardless of the size of the input.
It only uses a single variable (result) to store the result.

'''
