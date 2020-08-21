from typing import *


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0] * m for _ in range(m)]
        sum1, sum2 = 0, 0
        for i in range(m):
            sum1 += triangle[i][0]
            sum2 += triangle[i][i]
            dp[i][0] = sum1
            dp[i][i] = sum2
        for i in range(2, m):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[m - 1])


if __name__ == '__main__':
    sol = Solution()
    tri = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]]
    print(sol.minimumTotal(tri))
