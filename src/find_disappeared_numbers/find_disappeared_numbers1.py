from typing import List


class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappered_nums = []
        numbers = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in numbers:
                disappered_nums.append(i)
        return disappered_nums


'''

time complexity : O(n)
space complexity : O(n)

Time Complexity: O(n) - The dominant factor
is the loop iterating through the range object
(which depends on the length of the nums list).
The creation of the set is also O(n).

Space Complexity: O(n) - This comes from the
creation of the set (numbers) and the disappered_nums list,
both of which can potentially store
n-1 elements in the worst case.

'''
