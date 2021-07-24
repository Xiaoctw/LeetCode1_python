from typing import *


class Solution:
    def waysToChange(self, n: int) -> int:
        # 币值为25，10，5，1
        dp = [0] * (n + 1)
        mod = int(10 ** 9 + 7)
        dp[0] = 1
        for coin in [1, 5, 10, 25]:
            for val in range(1, n + 1):
                if val >= coin:
                    dp[val] += dp[val - coin]
        return dp[-1] % mod


if __name__ == '__main__':
    sol = Solution()
    print(sol.waysToChange(5))
