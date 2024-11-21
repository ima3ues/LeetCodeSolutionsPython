# Easy
# 1342 Number of Steps to Reduce a Number to Zero
# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# Base Code
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

# Solution
class Solution(object):
    def numberOfSteps(self, num):
        current = num
        accumulator = 0
        while current != 0:
            if current % 2 == 0:
                current /= 2
                accumulator += 1
            elif current % 1 == 0:
                current -= 1
                accumulator += 1
        return accumulator