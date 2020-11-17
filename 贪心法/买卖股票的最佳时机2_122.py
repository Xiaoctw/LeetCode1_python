from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tem_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                tem_profit += (prices[i] - prices[i - 1])
        return tem_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [1, 2, 3, 4, 5]
    print(sol.maxProfit(prices))
