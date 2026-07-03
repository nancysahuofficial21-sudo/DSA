class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        dp=[0]*len(prices)
        dp=prices.copy()
        for i in range(1,len(prices)):
            dp[i]=min(dp[i-1],prices[i])
        for j in range(1,len(prices)):
            maxprofit=max(maxprofit, prices[j]-dp[j])
        return maxprofit