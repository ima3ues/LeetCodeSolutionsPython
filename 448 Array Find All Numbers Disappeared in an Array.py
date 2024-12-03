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
        duplicate_nums = []
        for each_num in nums:
            if each_num not in duplicate_nums:
                duplicate_nums.append(each_num)
        duplicate_nums.sort()
        i = 0
        counter = 1
        return_list = []
        for i in range(len(nums) - 1):
            if duplicate_nums[i] != counter:
                return_list.append(i)
                counter += 1
        return return_list