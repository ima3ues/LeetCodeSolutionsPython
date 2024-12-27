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
        for each_num in nums:
            if each_num >= target:
                return 1
        all_possible = []
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                current_sum = nums[i] + nums[j]
                if current_sum >= target:
                    all_possible.append((i, j))
                j += 1
            i += 1
        update = []
        for (i, j) in all_possible:
            if j > i:
                update.append(j - i + 1)
        if update == []:
            return 0
        else:
            return(min(update))