# Easy
# 1295 Find Numbers with Even Number of Digits (Array)
# Given an array nums of integers, return how many of them contain an even number of digits.

# Base Code
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# Solution
class Solution(object):
    def findNumbers(self, nums):
        accumulator = 0
        for each_num in nums:
            if len(str(each_num)) % 2 == 0:
                accumulator += 1
        return accumulator