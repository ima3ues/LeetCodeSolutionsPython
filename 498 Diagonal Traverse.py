# Medium
# 498 Diagonal Traverse
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Base Code
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

# Solution
class Solution(object):
    def findDiagonalOrder(self, mat):
        # all start from up-right first
        rows = len(mat)
        cols = len(mat[0])
        i = 0
        j = 0
        return_list = []
        # 1 means moving up-right, -1 means moving down-left
        direction = 1 
        
        # check if each and every "box" have already inside the return list
        while len(return_list) < rows * cols:
            return_list.append(mat[i][j])
            
            # moving up-right
            if direction == 1: 
                # hit the right boundary, cannot continue move right
                if j == cols - 1:  
                    i += 1
                    direction = -1
                # hit top
                elif i == 0:  
                    j += 1
                    direction = -1
                else:
                    i -= 1
                    j += 1
            # moving down-left        
            else:  
                # hit bottom
                if i == rows - 1: 
                    j += 1
                    direction = 1
                # hit the left boundary, cannot continue move left
                elif j == 0:
                    i += 1
                    direction = 1
                else:
                    i += 1
                    j -= 1
        
        return return_list