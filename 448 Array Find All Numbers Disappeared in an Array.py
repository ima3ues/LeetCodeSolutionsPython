# Easy
# 448 Find All Numbers Disappeared in an Array (Array)
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Base Code
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

# Solution
class Solution(object):
    def findDisappearedNumbers(self, nums):
        check_list = []
        for i in range(1, len(nums) + 1):
            check_list.append(i)

        return_list = []
        for each_num in check_list:
            if each_num not in nums:
                return_list.append(each_num)

        return return_list