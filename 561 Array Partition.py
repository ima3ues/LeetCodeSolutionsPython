# Easy 
# 561 Array Partition 
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# Base Code
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# Solution
"""
题目核心目标是什么？
    把数组分成 两两一组（比如 (a, b)）。
    每组中，取较小的那个数字。
    让这些较小数字的总和尽可能大。
在每一组里，只能取较小的数字。所以：
    如果大的数字被浪费（比如和一个特别小的数字分在一组），就无法让较小值的总和最大化。
    为了最大化较小值的总和，我们要找到一种最优分组方式。
"""
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        final_list = []
        i = 0
        while i < len(nums):
            final_list.append((i, i + 1))
            i += 2
        accumulator = 0
        for each_pair in final_list:
            accumulator += min(each_pair)
        return accumulator     