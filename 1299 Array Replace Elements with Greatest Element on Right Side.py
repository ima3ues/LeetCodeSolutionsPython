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
            append_val = None
            # if range(i + 1, len(arr) - 1) it will generates numbers from i + 1 to len(arr) - 2
            for j in range(i + 1, len(arr)):
                if arr[j] > append_val:
                    append_val = arr[j]
            return_list.append(append_val)
        return_list.append(-1)
        return return_list
                