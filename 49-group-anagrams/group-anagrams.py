class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sortedStr = ''.join(sorted(s))
            anagrams[sortedStr].append(s)

        return list(anagrams.values())
