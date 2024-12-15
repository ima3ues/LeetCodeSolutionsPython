# Medium
# 54 Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Base Code
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

# Solution
class Solution(object):
    def spiralOrder(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        i = 0
        j = 0
        return_list = []
        direction = 1

        current_col = columns - 1
        current_row = rows - 1
        current_col2 = 0
        current_row2 = 1
        while len(return_list) < rows * columns:
            return_list.append(matrix[i][j])

            if direction == 1:
                if j == current_col:
                    current_col -= 1
                    i += 1
                    direction = 2
                else:
                    j += 1

            elif direction == 2:
                if i == current_row:
                    current_row -= 1
                    j -= 1
                    direction = 3
                else:
                    i += 1

            elif direction == 3:
                if j == current_col2:
                    current_col2 += 1
                    i -= 1
                    direction = 4
                else:
                    j -= 1

            elif direction == 4:
                if i == current_row2:
                    current_row2 += 1
                    j += 1
                    direction = 1
                else:
                    i -= 1

        return return_list