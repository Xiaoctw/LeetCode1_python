from typing import *


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    sol = Solution()
    nums = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.maxValue(nums))
