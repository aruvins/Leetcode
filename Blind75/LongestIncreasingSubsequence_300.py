# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

# Solution 1: Brute Force - DFS
# Input: [0,1,0,3,2,3]
# For every element decide whether it is included or not (2 choices for element)
# O(2^n) = 2*2*2*2*2*2

# Solution 2: DFS- With Cache
# Input: [1,2,4,3]
# Check all subsequence starting each element (imagine a tree)
# Check with DFS and cache all subtrees as you go through the tree

# Solution 3: Dynamic Programming
# Input: [1,2,4,3]
# Check all subsequence starting each element (imagine a tree)
# Start with arr[3] = 3 and you know that the subsequence ends there -> add to cache so you dont need to calculate again -> LIS[3] = 1
# go to arr[2] = 4 and it ends there -> add to cache -> LIS[2] = 1
# go to arr[1] = 2 and see you can either go to arr[2] or arr[3] -> add tree to cache -> LIS[1] = 1 + LIS[2] = 2 or LIS[1] = 1 + LIS[3] = 2
# go to arr[0] = 1 and you can either go to arr[1], arr[2], or arr[3] and see that LIS[1] is longest so -> LIS[0] = 1 + LIS[1] = 3
# Return the max LIS[]
# Time: O(n^2)

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]: #ensure increasing
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
