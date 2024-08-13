# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

# Solution 1: Brute Force
# Treat as decision tree
# For example n = 5
#                                                    0
#                                                   / \
#                                                  /   \
#                                                 /     \
#                                                /       \
#                                               /         \
#                                              /           \
#                                             /             \
#                                            /               \
#                                           /                 \
#                                          /                   \
#                                         /                     \
#                                        /                       \
#                                       /                         \
#                                      /                           \
#                                     /                             \
#                                    1                               2
#                                   / \                             / \
#                                  /   \                           /   \
#                                 /     \                         /     \
#                                /       \                       /       \
#                               /         \                     /         \
#                              /           \                   /           \
#                             /             \                 /             \
#                            2               3               3               4
#                           / \             / \             / \             / \
#                          /   \           /   \           /   \           /   \  
#                         /     \         /     \         /     \         /     \
#                        /       \       /       \       /       \       /       \
#                       3         4     4         5     4         5     5        6 
#                      / \       / \   / \             / \
#                     4   5     5   6 5   6           5   6
#                    / \
#                   5   6

# There are 7 instances where the decision tree ends in 5
# Use DFS to search tree
# Time: O(2^n)

# Solution 2: Memoization
# notice how the tree following the number 2 (on left side third level and right side second row) is the same on the left and right side
# Use memoization to limit number of calculations
# You can use the same logic for the number 3 -> Memoization
# Same for 4
# Time: O(n)
# Bottom up DP approach where you start at the base case(5) and move up
# DP = [([n+1] + [n+2]),([n+1] + [n+2]),([n+1] + [n+2]),([n+1] + [n+2]),1,1]
# DP = [8,5,3,2,1,1]


class Solution:
    def climbStairs(self, n: int) -> int:
        pos1, pos2 = 1, 1

        for i in range(n-1):
            temp = pos1
            pos1 = pos1 + pos2
            pos2 = temp
        return pos1