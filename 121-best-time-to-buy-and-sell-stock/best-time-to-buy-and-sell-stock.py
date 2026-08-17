class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buystock=prices[0]
        maxprofit=-float('inf')
        currpro=0
        for i in range(1,len(prices)):
            currpro=prices[i]-buystock
            maxprofit=max(maxprofit, currpro)
            buystock=min(buystock, prices[i])
        return maxprofit if maxprofit>0 else 0
        