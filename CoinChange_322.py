# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

# Solution 1: Greedy (Doesn't work)
# coins = [1,3,4,5], Amount = 7
# Solution = 5 + 1 + 1 = 7 (3 coins)
# Correct solution: 4 + 3 = 7 (2 coins)

# Solution 2: DFS 
# coins = [1,3,4,5], Amount = 7
# Create a tree with every branch being the combo of coins and end branch whenever leaf is negative or 0
# Notice how certain paths repeat for example if remaining amount is 1 then you know you only need to use a 1 coin to reach 0
# Top-down memoization

# Solution 3: DP- Bottom-up
# DP[0] = 0 = 0 coins
# DP[1] = 1 = 1 coin
# DP[2] = 1 + DP[1] = 2 coins
# DP[3] = 3 = 1 coin
# DP[4] = 4 = 1 coin
# DP[5] = 5 = 1 coin
# DP[6] = DP[5] + DP[1] || DP[1] + DP[5] || DP[3] + DP[3] = 2 coins
# DP[7] = DP[4] + DP[3] || DP[3] + DP[4] = 2 coins
# Time: O(amount* len(coins))       Space: O(amount)

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1,amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a],1 + dp[a-c]) 

        return dp[amount] if dp[amount] != amount + 1 else -1