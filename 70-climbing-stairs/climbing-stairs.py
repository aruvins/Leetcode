class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)

        def dfs(n):
            if (n<0):
                return 0
            elif n == 0:
                return 1
            elif memo[n] != -1:
                return memo[n]
            else:
                memo[n] = dfs(n-1) + dfs(n-2)
                return memo[n]

        return dfs(n)