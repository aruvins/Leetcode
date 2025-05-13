class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        maxLen = max(len(word1), len(word2))
        
        for i in range(maxLen):
            res += word1[i: i+1]
            res += word2[i: i+1]

        # if len(word1) > len(word2):
        #     res += word1[minLen:]
        # elif len(word1) < len(word2):
        #     res += word2[minLen:]

        return res