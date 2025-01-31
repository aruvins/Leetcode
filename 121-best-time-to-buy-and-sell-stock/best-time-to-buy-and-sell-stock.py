class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for sell in prices[1:]:
            if sell > buy:
                maxProfit = max(maxProfit, sell - buy)
            else:
                buy = sell

        return maxProfit
        
        
        
        
        
        
        
        
        
        
        
        # maxProfit = 0
        # for buy in range(len(prices)):
        #     for sell in range(buy + 1, len(prices)):
        #         maxProfit = max(maxProfit, prices[sell] - prices[buy])
        # return maxProfit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # profit = 0
        # buy = prices[0]

        # for sell in prices[1:]:
        #     if sell > buy:
        #         profit = max(profit, sell - buy)
        #     else:
        #         buy = sell

        # return profit
