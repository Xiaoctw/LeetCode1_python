from typing import *
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return 0
        m,n=len(grid),len(grid[0])
        visited=[[False]*n for _ in range(m)]
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    cnt+=1
                    self.dfs(i,j,m,n,grid,visited)
        return cnt

    def dfs(self,i,j,m,n,grid,visited):
        que=deque([])
        dir1 = [-1, 0, 0, 1]
        dir2 = [0, 1, -1, 0]
        que.append((i,j))
        visited[i][j] = True
        while que:
            i,j=que.popleft()
            for k in range(4):
                i1,j1=i+dir1[k],j+dir2[k]
                if 0<=i1<m and 0<=j1<n and not visited[i1][j1] and grid[i1][j1]=='1':
                    visited[i1][j1]=True
                    que.append((i1,j1))

if __name__ == '__main__':
    sol=Solution()
    grid=[["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]]
    print(sol.numIslands(grid))
