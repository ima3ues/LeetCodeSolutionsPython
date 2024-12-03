# Easy
# 941 Valid Mountain Array (Array)
# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Base Code
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

# Solution
class Solution(object):
    def validMountainArray(self, arr):
        # a mountain array must have at least 3 elements
        if len(arr) < 3:
            return False
        
        left = 0
        right = len(arr) - 1

        # firstly we need to keep in mind that, while loop will stop when the situation doesn't meet the conditions
        # the addition on left and right index will be the same (meet at the peak) if the array is a valid mountain array 
        while left + 1 < len(arr) - 1 and arr[left] < arr[left + 1]:
            left += 1
        while right - 1 > 0 and arr[right] < arr[right - 1]:
            right -= 1
        # ensures both pointers meet at the same peak
        return left == right