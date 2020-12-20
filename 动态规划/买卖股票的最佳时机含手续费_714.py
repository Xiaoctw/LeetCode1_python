from typing import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -prices[0]
        sell = 0
        max_profit = 0
        max_val1 = sell
        max_val2 = buy - fee
        for i in range(1, len(prices)):
            buy = max(buy, max_val1 - prices[i])
            sell = max(sell, max_val2 + prices[i])
            max_val1 = max(sell, max_val1)
            max_val2 = max(buy - fee, max_val2)
            max_profit = max(max_profit, buy, sell)
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(sol.maxProfit(prices, fee))
