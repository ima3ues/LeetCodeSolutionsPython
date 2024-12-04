# Easy
# 66 Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Base Code
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

# Solution
class Solution(object):
    def plusOne(self, digits):
        string = ""
        for each_num in digits:
            string = string + str(each_num)
        new_int = str(int(string) + 1)
        return_list = []
        for each_val in new_int:
            return_list.append(int(each_val))
        return return_list

