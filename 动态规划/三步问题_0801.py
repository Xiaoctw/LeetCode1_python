from typing import *


class Solution:
    def waysToStep(self, n: int) -> int:
        mod = int(10 ** 9 + 7)
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    n = 5
    print(sol.waysToStep(n))
