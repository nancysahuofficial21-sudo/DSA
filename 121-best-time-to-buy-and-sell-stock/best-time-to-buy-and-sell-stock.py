class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prc = float('inf')
        max_pro = 0

        for price in prices:
            if price < min_prc:
                min_prc = price

            elif price-min_prc > max_pro :
                max_pro = price - min_prc

        return max_pro