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
            return_list = [[1]]
            prev_list = 0
            length = 1
            while length < numRows:
                list_in_list = []
                i = 0
                while i < len(return_list[prev_list]):
                    if i == 0:
                        list_in_list.append(return_list[prev_list][i])
                    else:
                        list_in_list.append(return_list[prev_list][i - 1] + return_list[prev_list][i])
                    i += 1
                list_in_list.append(return_list[prev_list][0])
                return_list.append(list_in_list)
                prev_list += 1
                length += 1
        return return_list