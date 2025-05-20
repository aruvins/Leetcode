class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelSet = set(['a','e','i','o','u'])
        curVowel = 0
        
        for c in s[:k]:
            if c in vowelSet:
                curVowel += 1

        maxVowel = curVowel

        for i in range(k, len(s)):
            if s[i] in vowelSet:
                curVowel += 1
            if s[i-k] in vowelSet:
                curVowel -= 1

            maxVowel = max(maxVowel, curVowel)

        return maxVowel
