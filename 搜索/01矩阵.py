from typing import *
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        dist=[[m+n]*n for _ in range(m)]
        dir1=[-1,0,0,1]
        dir2=[0,1,-1,0]
        q=deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    q.append((i,j))
                    dist[i][j]=0
        while q:
            i,j=q.popleft()
            for k in range(4):
                i1,j1=i+dir1[k],j+dir2[k]
                if 0<=i1<m and 0<=j1<n and dist[i1][j1]==m+n:
                    dist[i1][j1]=dist[i][j]+1
                    q.append((i1,j1))
        return dist





if __name__ == '__main__':
    sol=Solution()
    matrix=[[0 ,0 ,0],
            [0 ,1 ,0],
            [1 ,1, 1]]
    print(sol.updateMatrix(matrix))


