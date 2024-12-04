# Easy
# 724 Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Base Code
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# Solution
class Solution(object):
    def pivotIndex(self, nums):
        pivot = 0
        for pivot in range(len(nums) - 1):
            right_accumulator = 0
            left_accumulator = 0
            i = 0
            while i < pivot:
                right_accumulator += nums[i]
                i += 1
            j = len(nums) - 1
            while j > pivot:
                left_accumulator += nums[j]
                j -= 1
            if right_accumulator == left_accumulator:
                return pivot
            else:
                pivot += 1
        return -1