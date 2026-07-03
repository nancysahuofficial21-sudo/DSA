from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the lowest price to infinity 
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # 1. Update the lowest buying price seen so far
            if price < min_price:
                min_price = price
            # 2. Else, check if selling today yields a higher profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
