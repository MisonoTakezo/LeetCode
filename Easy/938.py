"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans
  
