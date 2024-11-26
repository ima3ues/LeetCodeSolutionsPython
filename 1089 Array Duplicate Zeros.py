# Easy
# 1089 Duplicate Zeros (Array)
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Base Code
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

# Solution
class Solution(object):
    def duplicateZeros(self, arr):
        # make a copy of the original array
        original = arr[:]
        
        #use two pointers to copy elements with zero duplication
        i = 0  # pointer for the original array
        j = 0  # Pointer for the modified array
        
        # iterate until we fill the modified array
        while j < len(arr):
            arr[j] = original[i] 
            # j + 1 < len(arr) is used to ensure that we don't go out of bounds when duplicating a zero
            if original[i] == 0 and j + 1 < len(arr):
                # move to the next position
                j += 1
                arr[j] = 0
            # move to the next element in the original array
            i += 1  
            # move to the next position in the modified array
            j += 1             