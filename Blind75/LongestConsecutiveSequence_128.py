# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Solution: Sorting
# Cant sort since that is O(nlogn)

# Solution:
# First lets understand what we know about a sequence
# We know that for a sequence to start there must not be n element to the left so for example 1, there isnt an element 0 in the list
# and you can check the length of a sequence by checking if the element + 1 exists in the list so for example 1, check if 2 exists in the list
# you can convert this to a set to make operations faster
# Input: nums = [100,4,200,1,3,2]
# Check 100 and see if 99 exists, it doesn't so you start at 100 (length += 1)
# Check 100 and see if 101 exists, it doesnt so you know the sequence length is 1
# check 4 and see if 3 exists, it does so you know that 4 isnt the start
# Check 200 and see if 199 exists, it doesn't so you start at 200 (length += 1)
# Check 200 and see if 201 exists, it doesnt so you know the sequence length is 1
# Check 1 and see if 0 exists, it doesn't so you start at 1 (length += 1)
# Check 1 and see if 2 exists, it does so you know keep going (length += 1)
# Check 1 and see if 3 exists, it does so you know keep going (length += 1)
# Check 1 and see if 4 exists, it does so you know keep going (length += 1)
# Check 1 and see if 5 exists, it doesn't so you know the sequence is 4
# Check 3 and see if its the start, it isnt so continue
# Check 2 and see if its the start, it isnt so continue
# Time: O(n)    Space: O(n)



from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start
            if(n-1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest