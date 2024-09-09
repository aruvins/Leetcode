# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:
# https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png

# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100

# Personal Notes:
# Similar solution to Leetcode 1143: Longest Common Subsequence

# Solution: Sum
# set end = 1 and from every position = sum up the down and the right position
# Time: O(n*m)      Space: O(n)
# Input: m = 3, n = 7
# [28][21][15][10][6 ][3 ][1 ][0 ]
# [7 ][6 ][5 ][4 ][3 ][2 ][1 ][0 ]
# [1 ][1 ][1 ][1 ][1 ][1 ][1 ] <-Ending square
# [0 ][0 ][0 ][0 ][0 ][0 ]

# Solution: Math
# The number of unique paths can be calculated as the combinatorial of the (m-1) downs and (n-1) rights
# This works because at every given point you can either chose to go down or right but it doesn't matter which path you take since it leads to the same outcome
# Time: O(1)        Space: O(n)
# Explanation of the math of finding possible combinations is given below
    # Exponent: Let us say there are four different grades in a class - A, B, C, D. Five students. We can provide a grade to any number of students. We won't run out of grades. When more students get added we can keep giving them all A grades, for instance. For n students and k grades the possible number of outcomes is k^n.
    # Factorial: Consider a scenario where you have three different candies. The candies can be same, or have differences in flavor/brand/type. Now you have to distribute this to three children. When you give away your first candy to the first kid, that candy is gone. We have finite number of objects to be distributed among a finite set of members. Also notice that different distribution will result in a different outcome for the children. This is permutation (order matter...which kid gets which candy matters),but this is also a special case of permutation because number of members are equal to number of products. We have n! outcomes when there are n candies going to n children.
    # Permutation: Consider the case above, but instead of having only 3 children we have 10 children out of which we have to choose 3 to provide the 3 candies to. This is also permutation but a more general case. Here number of members is not equal to number of objects. We have n!/(n-r)! outcomes. From the example, we have 10 children so n = 10, 3 candies so r = 3. So factorial is same as the permutation, but when n = r.
    # Combination: Now consider a slightly different example of case 3 above. Instead of assigning candies, you have to pick three candies from a bucket full of candies. The bucket may have about 10 candies in total. And you get to keep all 3 of them that you pick. Now, does it matter in what order you pick the three? It doesn't. In a scenario like this, picking candy1, candy2, candy3 in that order will be no different for you from picking candy3, candy2, candy1 (different order). So this is a case pf permutations but where certain outcomes are equal to each other. Hence the total combinations of r picks from n items is n!/r!(n-r)!
    # Source: https://math.stackexchange.com/questions/3013209/permutations-vs-combinatorial-vs-factorials-vs-exponents

import math

# DP Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
    

# Math Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)