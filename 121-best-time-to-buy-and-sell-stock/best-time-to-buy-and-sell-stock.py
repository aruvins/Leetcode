class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for sell in prices[1:]:
            if buy < sell:
                maxProfit = max(maxProfit, sell - buy)
            else:
                buy = sell

        return maxProfit