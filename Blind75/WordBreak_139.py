# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# Solution 1: Brute Force
# Test every possible combination of string and check if its in dict
# Time: O(n^2)

# Solution 2: Check dict word
# use the word in the dict as the prefix and check if it matches
# Time: O(n*m*n)

# Solution 3: DP
# Input: S ="neetcode", wordDict["neet", "leet", "code"]
# DP[8] = true   //end of word
# DP[7] = false
# DP[6] = DP[5] = false
# DP[4] = true   //end of word
# DP[3] = DP[2] = DP[1] = false
# DP[0] = DP[0 + len(word)] = True //since this is true then you return true
# Since you started from bottom up you know where the words end

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if(i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

