from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for num in nums:
            if num in elements:
                return True
            else:
                elements.add(num)
        return False


'''

time complexity : O(n)
space complexity : O(n)

Where n is the length of the list nums.
creating a set, adding elements to set
and checking for element inclusion in a 
set all have constant time O(1) due to the
hash implemntation of sets in python

'''
