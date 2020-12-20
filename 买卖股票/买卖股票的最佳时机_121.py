from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0
        for val in prices:
            min_price=min(val,min_price)
            max_profit=max(max_profit,val-min_price)
        return max_profit