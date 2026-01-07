class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)

            return hours <= h

        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2
            if k_works(m):
                r = m
            else:
                l = m + 1

        return l