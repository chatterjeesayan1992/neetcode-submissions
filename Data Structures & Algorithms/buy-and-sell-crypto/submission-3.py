class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # max_profit = [0]*len(prices)

        # for i in range(1,len(prices)):
        #     max_profit[i] = max(0,(max_profit[i-1] + (prices[i] - prices[i-1])))
        
        # return max(max_profit)

        l,r = 0, 1
        import sys

        res = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, (prices[r] - prices[l]))
            
            r += 1
        
        return res
            


        