# Easy
# 226 Invert Binary Tree (Tree)
# Given the root of a binary tree, invert the tree, and return its root.

# Base Code
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

# Solution
class Solution(object):
    def invertTree(self, root):
        if not root: 
        # this line used to stop the recursion when it reaches the end of the tree (leaf nodes)
        # when the recursion reaches a leaf node, since these children are None, the function should stop there instead of continuing to call itself indefinitely
            return root
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        # why? - the problem explicitly asks to return the **root**
        return root