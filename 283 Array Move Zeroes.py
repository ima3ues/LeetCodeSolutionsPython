# Easy
# Move Zeroes (Array)
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Base Code
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

# Solution
class Solution(object):
    def moveZeroes(self, nums):
        accumulator = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.remove(nums[i])
                i -= 1
                accumulator += 1
            i += 1
        for i in range(accumulator):
            nums.append(0)