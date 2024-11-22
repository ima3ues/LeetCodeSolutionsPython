# Easy 
# 977 Squares of a Sorted Array (Array)
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Base Code
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

# Solution
class Solution(object):
    def sortedSquares(self, nums):
        result = []
        for each_num in nums:
            squared = each_num ** 2
            result.append(squared)
        result.sort()
        return result