# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# Solution: 
# input: [1,2,3,1,4,5]
# look at only the first 2 houses and determine the max between (the current house + the value stolen) and the next house
# update array so as to hold the value stolen
# rob2 should always hold the current max value
# Think of this as a two pointer problem where rob2 holds the current max and (rob1 + current element value) tries beats rob2
# Time: O(n) since you're looping through every element

# [1,2,3,1]
# rob1, rob2
# 0 1
# 1 2
# 2 4
# 4 4


# [2,7,9,3,1]
# rob1, rob2
# 0 2
# 2 7
# 7 11
# 11 11
# 11 12



from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for robValue in nums:
            temp = max(robValue + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


