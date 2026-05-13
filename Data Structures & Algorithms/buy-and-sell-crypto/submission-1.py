class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = [0]*len(prices)

        for i in range(1,len(prices)):
            max_profit[i] = max(0,(max_profit[i-1] + (prices[i] - prices[i-1])))
        
        return max(max_profit)

        