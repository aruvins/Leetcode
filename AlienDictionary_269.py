# 269. Alien Dictionary
# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# Example 1:

# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"
# Example 2:

# Input:
# [
#   "z",
#   "x"
# ]

# Output: "zx"
# Example 3:

# Input:
# [
#   "z",
#   "x",
#   "z"
# ]

# Output: "" 

# Explanation: The order is invalid, so return "".
# Note:

# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# Solution: 
# 

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:min]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j].add(w2[j])]
                    break
        
        visit = {} #False = visited, True = current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
                
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()   
        return "".join(res)