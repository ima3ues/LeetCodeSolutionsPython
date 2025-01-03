# Medium
# 209 Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Base Code
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
# Solution (which is correct but exceed the time limit)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        for each_num in nums:
            if each_num >= target:
                return 1
        i = 0
        alist = []
        while i < len(nums):
            ans = nums[i]
            accumulator = 0
            j = i + 1
            while j < len(nums):
                ans += nums[j]
                accumulator += 1
                if ans >= target:
                    alist.append(accumulator + 1)
                j += 1
            i += 1
        if alist == []:
            return 0
        else:
            return(min(alist))
        
# Solution 
class Solution(object):
    def minSubArrayLen(self, target, nums):
        total = sum(nums)
        if total < target:
            return 0
        elif total == target:
            return len(nums)
        
        for each_num in nums:
            if each_num >= target:
                return 1
            
        left = 0
        curr = 0
        slide_length = len(nums)
        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                slide_length = min(slide_length, right + 1 - left)
                curr -= nums[left]
                left +=1
        
        return slide_length