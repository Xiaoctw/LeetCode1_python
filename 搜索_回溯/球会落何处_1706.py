from typing import *


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [self.dfs(i, 0, m, n, grid) for i in range(n)]
        return res

    def dfs(self, idx, row, m, n, grid):
        if row == m:
            return idx
        if idx == 0 and grid[row][idx] == -1:
            return -1
        if idx == n - 1 and grid[row][idx] == 1:
            return -1
        if idx < n - 1 and grid[row][idx] == 1 and grid[row][idx + 1] == -1:
            return -1
        if idx > 0 and grid[row][idx] == -1 and grid[row][idx - 1] == 1:
            return -1
        if grid[row][idx] == 1:
            return self.dfs(idx + 1, row + 1, m, n, grid)
        else:
            return self.dfs(idx - 1, row + 1, m, n, grid)


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]
    print(sol.findBall(grid))
