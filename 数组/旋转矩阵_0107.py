from typing import *
import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
        return

if __name__ == '__main__':
        sol=Solution()
        matrix=[[ 5, 1, 9,11],
                 [ 2, 4, 8,10],
                 [13, 3, 6, 7],
                 [15,14,12,16]]
        sol.rotate(matrix)
        print(matrix)