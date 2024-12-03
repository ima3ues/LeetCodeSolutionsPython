# Easy
# 414 Third Maximum Number (Array)
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# Base Code
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# Solution
class Solution(object):
    def thirdMax(self, nums):
        non_duplicate = []
        
        for each_num in nums:
            if each_num not in non_duplicate:
                non_duplicate.append(each_num)
        non_duplicate.sort(reverse = True)
        if len(non_duplicate) < 3:
            compare = None
            for each_non_dup in non_duplicate:
                if compare >= each_non_dup:
                    compare = compare
                else: 
                    compare = each_non_dup
        else:
            compare = non_duplicate[2]
    
        return compare