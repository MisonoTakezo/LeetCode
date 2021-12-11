"""
Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.answer = 0
        self.dfs(root, None, None)
        return self.answer
    
    def dfs(self, node, parent, grand):
        if not node:
            return None
        if grand and grand.val % 2 == 0:
            self.answer += node.val
        self.dfs(node.left, node, parent)
        self.dfs(node.right, node, parent)
        