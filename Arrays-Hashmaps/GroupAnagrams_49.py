# https://leetcode.com/problems/group-anagrams/description/


# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Solution: Hash Map
# We can loop through each word and sort the word by char
# Since the chars in the word is sorted alphabetically any anagrams would be the same word
# We can then add it to a hash map to keep track of the words
# We then create a 2d array/ map from the hashmap and then return it
# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }
# Note: defaultdict is a dict but better error handling
# Note: Sorted() returns a new list while .sort() does not return a new list and sorts the original list
# Time: O(N∗M∗Log(M)) because it takes M*Log(M) to sort and you are looping through every word

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagram_map[sortedWord].append(word)
        
        return list(anagram_map.values())