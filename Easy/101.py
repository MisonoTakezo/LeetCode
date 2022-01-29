"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
        
    def dfs(self, left, right):
        if (left and right) and left.val == right.val:
            return self.dfs(left.left, right.right) and self.dfs(right.left, left.right)
        elif left is None and right is None:
            return True
        else:
            return False
