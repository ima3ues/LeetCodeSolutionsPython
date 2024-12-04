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

# Solution (which is correct but exceed the time limit)
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
    
# Solution 
class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        count = [0] * n  
        
        # as each number are in ascending from 1 to n, therefore we can use accumulator at each number's index
        for num in nums:
            count[num - 1] += 1  
        
        missing = []
        for i in range(n):
            if count[i] == 0:
                missing.append(i + 1)
        
        return missing