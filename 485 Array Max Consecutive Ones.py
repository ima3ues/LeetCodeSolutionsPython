# Easy
# 485 Max Consecutive Ones (Array)
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Base Code
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# Solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        accumulator = 0
        comparer = 0
        for each_num in nums:
            if each_num == 1:
                accumulator += 1
                if comparer < accumulator:
                    comparer = accumulator
            else:
                accumulator = 0
        return comparer