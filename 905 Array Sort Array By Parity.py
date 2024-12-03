# Easy
# 905 Sort Array By Parity (Array)
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# Base Code
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

# Solution
class Solution(object):
    def sortArrayByParity(self, nums):
        i = 0
        odd_nums = []
        while i < len(nums):
            if nums[i] % 2 != 0:
                odd_nums.append(nums[i])
                nums.remove(nums[i])
                i -= 1
            i += 1
        for each_num in odd_nums:
            nums.append(each_num)
        return nums