class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            curProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, curProfit)
            if prices[r] < prices[l]:
                l = r
            r += 1

        return maxProfit
            