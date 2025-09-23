class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2:
        #     return n

        # dp = [0] * (n+1)
        # dp[0], dp[1] = 1,1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        memo = {}

        def dfs(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            if i in memo:
                return memo[i]

            memo[i] = dfs(i-1) + dfs(i - 2)
            return memo[i]

        return dfs(n)

