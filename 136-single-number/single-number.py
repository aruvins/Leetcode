from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for i,v in freq.items():
            if v == 1:
                return i