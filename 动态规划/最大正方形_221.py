from typing import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_val = -1
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_val = max(max_val, dp[i][j])
        return max_val ** 2


if __name__ == '__main__':
    sol = Solution()
    matrix = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    print(sol.maximalSquare(matrix))

    # import numpy as np
    # a=np.array([(0,1),(1,0),(0.5,0.5)])
    # b=np.array([[0,-1],[-1,0],[-0.5,-0.5]])
    # ba_=np.dot(b,a.transpose())
    # u,s,vt=np.linalg.svd(ba_)
    # res=np.dot(u,vt)
    # print(b)
    # print(np.dot(res,a))
