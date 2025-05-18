class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        prev = groups[0]

        for i,v in enumerate(groups[1:]):
            if v == prev:
                continue
            res.append(words[i+1])
            prev = v

        return res