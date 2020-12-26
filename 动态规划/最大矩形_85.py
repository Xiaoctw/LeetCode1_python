from typing import *


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        num_up = [[0] * n for _ in range(m)]
        for i in range(n):
            if matrix[0][i] == '1':
                num_up[0][i] = 1
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '1':
                    num_up[i][j] = num_up[i - 1][j] + 1
        ans = 0
        for i in range(m):
            pre_zero = -1
            min_up = float('inf')
            for j in range(n):
                if matrix[i][j] == '0':
                    pre_zero = j
                    min_up=float('inf')
                else:
                    min_up = min(min_up, num_up[i][j])
                    ans = max(ans, min_up * (j - pre_zero))
        return ans

if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    sol=Solution()
    print(sol.maximalRectangle(matrix))

