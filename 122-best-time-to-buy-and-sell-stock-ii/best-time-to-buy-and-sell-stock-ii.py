class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold=prices[0]
        profit=0
        i=1
        while i<len(prices):
            if prices[i]<=prices[i-1]:
                hold=prices[i]
                i+=1
            else:
                while i<len(prices) and prices[i]>prices[i-1]:
                    i+=1
                profit+=prices[i-1]-hold
        return profit