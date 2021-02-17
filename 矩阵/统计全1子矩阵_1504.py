from typing import *
import sys


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if len(mat) == 0 or len(mat[0]) == 0:
            return 0
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = mat[i][j]
                elif mat[i][j] != 0:
                    dp[i][j] = dp[i][j - 1] + 1
        for i in range(m):
            for j in range(n):
                val = sys.maxsize
                if dp[i][j] > 0:
                    for k in range(i, -1, -1):
                        val = min(val, dp[k][j])
                        res += val
        return res


if __name__ == '__main__':
    sol = Solution()
    mat = [[1, 0, 1],
           [1, 1, 0],
           [1, 1, 0]]
    print(sol.numSubmat(mat))
