# Easy
# 747 Largest Number At Least Twice of Others
# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

# Base Code
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
# Solution
class Solution(object):
    def dominantIndex(self, nums):
        maximum = max(nums)
        i = 0
        while i < len(nums) and nums[i] != maximum:
            if nums[i] * 2 > maximum:
                return -1
            i += 1
        return nums.index(maximum)