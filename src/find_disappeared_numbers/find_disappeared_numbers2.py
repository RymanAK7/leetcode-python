from typing import List

class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num)-1] = abs(nums[abs(num)-1])*-1
        return [i+1 for i in range(len(nums)) if nums[i]>0]


'''
Solving the follow up question : Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

time complexity: O(n)

The loop that iterates over each number in the input list nums has a time complexity of O(n), where n is the length of the input list.
Within this loop, the access and modification of elements in the list take constant time, O(1), because it's done by index.
The list comprehension at the end iterates over the entire modified nums list once more, which also has a time complexity of O(n).


Space complexity: O(1) [assuming the returned list does not count as extra space]


But in reality the returned list containing the disappeared numbers could potentially have a size of up to O(n-1) where in the worst case n-1 numbers from 1 to n are missing.
Thus, the space complexity is O(n), where n is the length of the input list.

'''