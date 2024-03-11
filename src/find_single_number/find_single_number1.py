from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        for key, value in num_count.items():
            if value == 1:
                return key


'''
time complexity : O(n)
space complexity : O(n)

where n is the length of the input array `nums`

Time complexity is O(n) because
we iterate through the array once to count
the occurrences of each number.

The space complexity is O(n) as well.
This is due to the dictionary `num_count`
which stores the count of each unique number in the array.
The length of the dictionary will always be (n//2)+1
since every element appears twice except one.
This results in space complexity of O((n//2)+1)
which simplifies to O(n).


'''
