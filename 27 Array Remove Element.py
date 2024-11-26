# Easy
# 27 Remove Element (Array)
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Base Code
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

# Solution (wrong version which seems correct)
class Solution(object):
    def removeElement(self, nums, val):
        for each_num in nums:
            if each_num == val:
                nums.remove(each_num)
# Explanation:
# when we use for...in..., python will automatically generate index
# when we use .remove, python will automatically move the value to the most left
# so for example, when the input is nums = [0,1,2,2,3,0,4,2] and val = 2
# at the 3rd iteration nums[2] = 2  → True, nums = [0, 1, 2, 3, 0, 4, 2] 
# the problem occurs at the 4th iteration where nums[3] = 3 -> False, nums = [0, 1, 2, 3, 0, 4, 2]
# continuously loop until the 7th iteration where nums[6] - 2 -> True, nums = [0, 1, 3, 0, 4, 2], this happens as nums.remove(each_num) removes the first occurrence of the value in the list, not the value at the current index
# therefore the final result was nums = [0, 1, 3, 0, 4, 2]

# Solution
class Solution(object):
    def removeElement(self, nums, val):
        