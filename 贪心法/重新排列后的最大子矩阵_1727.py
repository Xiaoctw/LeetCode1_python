from typing import *


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dp1 = []
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if matrix[i][j] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                else:
                    if matrix[i][j] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j] + 1
            dp1.append(sorted(dp[i],reverse=True))
        res = 0
        for i in range(m):
            min_val = float('inf')
            for j in range(n):
                min_val = min(min_val, dp1[i][j])
                res = max(res, min_val * (j + 1))
                if dp1[i][j] == 0:
                    break
        return res

if __name__ == '__main__':
    sol=Solution()
    matrix = [[1,1,0],[1,0,1]]
    print(sol.largestSubmatrix(matrix))
