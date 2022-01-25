"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        n1, n2 = 0, 1
        for _ in range(n):
            n1, n2 = n2, n1 + n2
        return n2
