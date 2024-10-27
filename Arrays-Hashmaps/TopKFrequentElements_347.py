# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Solution:
# Create a hashmap {element: numOfElements}
# Loop through the array and update the hashmap keeping count of the amount of elements see
# Time: O(n) because you are required to loop through every element in the array

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        adj_map = {}
        freq = [[] for i in range(len(nums) + 1)] #empty array that keeps track of the number of elements (we will use this to determine top K) (We also know that the max number of elements is len(nums))

        for n in nums:
            adj_map[n] = 1 + adj_map.get(n,0) #update map with the count of the elements
        
        for num, numElements in adj_map.items():
            freq[numElements].append(num) #append the number to the numElements to keep track

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res