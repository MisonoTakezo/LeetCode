"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.mx = 0
        self.dfs(root)
        return self.mx
    
    def dfs(self, root):
        if root is None:
            return 0
        right = self.dfs(root.right)
        left = self.dfs(root.left)
        self.mx = max(self.mx, right + left)
        return 1 + max(right, left)
