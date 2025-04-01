class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1

        return max(freq, key=freq.get)
        