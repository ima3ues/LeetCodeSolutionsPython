# Easy
# 941 Valid Mountain Array (Array)\
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
        next_i = 1 
        while next_i < len(arr):
            for each_num in arr:
                if each_num == arr[next_i]:
                    return False
                next_i += 1
        middle = len(arr) // 2
        
                

