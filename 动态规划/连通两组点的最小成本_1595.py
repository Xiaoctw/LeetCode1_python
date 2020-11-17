from typing import *

import sys


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        cost_matrix = [[0] * (1 << n) for _ in range(m)]
        for k in range(m):
            for i in range(1 << n):
                tem_sum = 0
                for j in range(n):
                    if i & (1 << j) > 0:
                        tem_sum += cost[k][j]
                cost_matrix[k][i] = tem_sum
        dp = [cost_matrix[0]]
        for i in range(1, m):
            dp.append([sys.maxsize] * (1 << n))
        for i in range(1, m):
            for k in range(1, (1 << n)):
                for j in range(n):
                    dp[i][k | (1 << j)] = min(dp[i][k | (1 << j)], dp[i - 1][k] + cost_matrix[i][1 << j])
                rest = (1 << n) - 1 - k  # 剩余的物品
                j = rest
                while j >= 1:
                    dp[i][j | k] = min(dp[i][j | k], dp[i - 1][k] + cost_matrix[i][j])
                    j = rest & (j - 1)
        return dp[m - 1][(1 << n) - 1]


if __name__ == '__main__':
    sol = Solution()
    cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
    print(sol.connectTwoGroups(cost))
