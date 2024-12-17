# Easy
# 118 Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.

# Base Code
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
# Solution
class Solution(object):
    def generate(self, numRows):
        if 1 <= numRows <= 30:
            current_row = 0
            return_list = []
            while current_row < numRows:
                list_in_list = []
                start_num = 1
                i = 0
                while i < current_row:
                    list_in_list.append(start_num)
                    i += 1
                return_list.append(list_in_list)
                current_row += 1

        return return_list