from typing import *
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        mat=[[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                mat[j][i]=matrix[i][j]
        return mat

if __name__ == '__main__':
    sol=Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.transpose(matrix))