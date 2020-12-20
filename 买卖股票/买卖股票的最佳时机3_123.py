from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        ans = 0
        min_left = float('inf')
        max_rights = self.helper(prices)
        max_rights.append(0)
        for i in range(len(prices)):
            min_left = min(prices[i], min_left)
            max_profit = max(prices[i] - min_left, max_profit)
            ans = max(ans, max_profit + max_rights[i + 1])
        return ans

    def helper(self, prices):
        max_right = -float('inf')
        max_profit = 0
        max_profits = []
        for i in range(len(prices) - 1, -1, -1):
            max_right = max(max_right, prices[i])
            max_profit = max(max_profit, max_right - prices[i])
            max_profits.append(max_profit)
        return max_profits[::-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [7,6,4,3,1]
    print(sol.maxProfit(nums))
