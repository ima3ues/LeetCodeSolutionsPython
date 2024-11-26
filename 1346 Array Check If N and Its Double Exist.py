# Easy
# 1346 Check If N and Its Double Exist (Array)
# Given an array arr of integers, check if there exist two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Base Code
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

# Solution
class Solution(object):
    def checkIfExist(self, arr):
        i = 0
        for each_num in arr:
            j = 0
            while i >= 0 and j < len(arr):
                while i != j:
                    if each_num == arr[j] * 2:
                        return True
                    else:
                        return False
                j += 1
            i += 1
                        
        