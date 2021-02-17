from typing import *
import sys


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                if i == j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(i + dp[i + 1][j], j + dp[i][j - 1])
                    for k in range(i + 1, j):
                        dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1],dp[k + 1][j]))
        return dp[1][n]


if __name__ == '__main__':
    sol = Solution()
    n = 10
    print(sol.getMoneyAmount(n))
