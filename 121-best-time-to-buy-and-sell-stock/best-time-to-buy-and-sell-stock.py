class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprofit=0
        for i in prices:
            if i<minprice:
                minprice=i
            maxprofit1=i-minprice
            if maxprofit1 >maxprofit:
                maxprofit=i-minprice
        
        return maxprofit
        