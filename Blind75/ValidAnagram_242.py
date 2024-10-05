# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


from collections import defaultdict


class Solution1: #O(nlogn)
    def isAnagram(self, s: str, t: str) -> bool:
        sortedWord1 = sorted(s)
        sortedWord2 = sorted(t)

        if sortedWord1 == sortedWord2:
            return True
        return False

class Solution2: #O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS,  countT= defaultdict(), defaultdict()

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True

