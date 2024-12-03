# Easy
# 1299 Replace Elements with Greatest Element on Right Side (Array)
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

# Base Code
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

# Solution
class Solution(object):
    def replaceElements(self, arr):
        return_list = []
        i = 0
        for i in range(len(arr) - 1):
            current = arr[i]
            for j in range(i, len(arr)-1):
                if current < arr[j]:
                    current = arr[j]
                else:
                    current = arr[i]
                return_list.append(current)
        return return_list
                