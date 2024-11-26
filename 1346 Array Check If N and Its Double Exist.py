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
        for i in range(len(arr)): 
            for j in range(len(arr)): 
                if i != j and arr[i] == 2 * arr[j]: 
                    return True
        # if no pair is found, return False (because the question ask for "exist")
        return False  
                        
        