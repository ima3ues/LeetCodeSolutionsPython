# Easy
# 1480 Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Base Code
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

# Solution
class Solution(object):
    def runningSum(self, nums):
        sum_array = [0] * len(nums)
        sum_array_index = 0
        sum_array_ttl_num_per_index = 0
        for each_num in nums:
            sum_array_ttl_num_per_index += each_num
            sum_array[sum_array_index] = sum_array_ttl_num_per_index
            sum_array_index += 1
        return sum_array