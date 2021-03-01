from typing import *


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for beg1 in range(m - 1):
            beg2 = 0
            k = 0
            val = matrix[beg1][beg2]
            while beg1 + k < m and beg2 + k < n:
                if matrix[beg1 + k][beg2 + k] != val:
                    return False
                k += 1
        for beg2 in range(n - 1):
            beg1 = 0
            k = 0
            val = matrix[beg1][beg2]
            while beg1 + k < m and beg2 + k < n:
                if matrix[beg1 + k][beg2 + k] != val:
                    return False
                k += 1
        return True


if __name__ == '__main__':
    sol = Solution()
    matrix = [[1, 3, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(sol.isToeplitzMatrix(matrix))
