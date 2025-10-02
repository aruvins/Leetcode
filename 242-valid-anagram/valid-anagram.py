from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        for c in s:
            freq1[c] = freq1.get(c, 0) + 1

        for c in t:
            freq2[c] = freq2.get(c, 0) + 1

        return freq1 == freq2