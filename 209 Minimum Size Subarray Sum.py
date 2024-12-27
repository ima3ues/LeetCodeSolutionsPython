# Medium
# 209 Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Base Code
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
# Solution
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left, right = 0, len(nums) - 1 
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum >= target:
                return current_sum
            elif current_sum < target:
                left += 1
            else:
                return 0