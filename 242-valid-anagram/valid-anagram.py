from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = Counter(s)
        freqT = Counter(t)

        return freqS == freqT