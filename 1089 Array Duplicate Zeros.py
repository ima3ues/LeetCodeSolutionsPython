# Easy
# 1089 Duplicate Zeros (Array)
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the copy array are not written. Do the above modifications to the input array in place and do not return anything.

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
        # make a copy of the copy array
        copy = arr[:]
        
        #use two pointers to copy elements with zero duplication
        i = 0  
        j = 0  
        # iterate until we fill the modified array
        while i < len(arr):
            arr[i] = copy[j] 
            # i + 1 < len(arr) is used to ensure that we don't go out of bounds when duplicating a zero
            if copy[j] == 0 and i + 1 < len(arr):
                # move to the next position
                i += 1
                arr[i] = 0
            # move to the next element in the copy array
            i += 1  
            # move to the next position in the modified array
            j += 1             
            
# no need to worry about the below part will not duplicate the current index to 0:
# if copy[j] == 0 and i + 1 < len(arr):
#     # move to the next position
#     i += 1
#     arr[i] = 0
# as arr[i] = copy[j] this line already duplicate the current index to 0