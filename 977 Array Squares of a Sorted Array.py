# Easy **need to revise again as i couldn't get the ans quickly**
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
        nums_squared = [num ** 2 for num in nums]
        nums_squared.sort()
        return nums_squared