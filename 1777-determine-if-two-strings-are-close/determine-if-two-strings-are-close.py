from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        return (set(word1) == set(word2)) and sorted(freq1.values()) == sorted(freq2.values())