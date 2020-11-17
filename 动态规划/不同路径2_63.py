from typing import *


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                    continue
                if i == 1 and j == 1:
                    dp[i][j] = 1
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    sol = Solution()
    obs = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
    print(sol.uniquePathsWithObstacles(obs))
