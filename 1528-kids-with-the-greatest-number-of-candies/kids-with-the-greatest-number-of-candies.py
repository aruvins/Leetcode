class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        res = []
        for kid in candies:
            if kid + extraCandies >= maxCandies:
                res.append(True)
            else:
                res.append(False)
        return res
