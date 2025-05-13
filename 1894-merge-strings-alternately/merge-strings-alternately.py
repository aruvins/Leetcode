class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        minLen = min(len(word1), len(word2))
        
        for i in range(minLen):
            res += word1[i]
            res += word2[i]

        if len(word1) > len(word2):
            res += word1[minLen:]
        elif len(word1) < len(word2):
            res += word2[minLen:]
            
        return res