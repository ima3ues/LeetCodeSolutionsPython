# Medium
# 167 Two Sum II - Input array is sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Base Code
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

# Solution (which is correct but exceed the time limit)
class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        while i < len(numbers):
            j = 0 
            while j < len(numbers):
                if i != j and target == numbers[i] + numbers[j]:
                    return [i + 1, j + 1]
                else:
                    j += 1                
            i += 1

# Solution 
class Solution(object):
    def twoSum(self, numbers, target):