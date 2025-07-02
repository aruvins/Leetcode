class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for sell in prices[1:]:
            print(buy)
            print('sell', sell)
            if sell > buy:
                maxProfit = max(maxProfit, sell - buy)
            else:
                buy = sell
            

        return maxProfit