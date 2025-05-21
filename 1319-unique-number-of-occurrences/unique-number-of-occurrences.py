from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        occurrencesSet = set()

        for v in freq.values():
            if v in occurrencesSet:
                return False
            occurrencesSet.add(v)

        return True
