"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        count = 0
        ans = {}
        self.dfs(root, count, ans)
        return ans[max(ans)]
        
    def dfs(self, node, count, ans):
        if node:
            count += 1
            
            if count in ans:
                ans[count] += node.val
            else:
                ans[count] = node.val

            self.dfs(node.left, count, ans)
            self.dfs(node.right, count, ans)
