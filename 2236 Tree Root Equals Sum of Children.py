# Easy
# 2236 Root Equals Sum of Children (Tree)
# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

# Base Code
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
# Solution
class Solution(object):
    def checkTree(self, root):
        parent = root.val
        left_child = root.left.val
        right_child = root.right.val

        if (parent == left_child + right_child):
            return True
        else:
            return False