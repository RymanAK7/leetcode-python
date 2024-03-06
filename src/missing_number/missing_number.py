from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_0_to_n = (n * (n + 1)) // 2
        sum_nums = sum(nums)
        return sum_0_to_n - sum_nums


'''

Algorithm makes use of the fact that sum of numbers from 0 to n is n*(n+1) / 2

time complexity : O(n)
space complexity : O(1)

Where n is the length of the input list nums.

space complexity is constant time.
All operations such as storing constants
in varaibles and mathematical operations
have constant time regardless
of the input length.

time complexity has linear time as it iterates
through the list once to calculate the sum of the
input list

'''
