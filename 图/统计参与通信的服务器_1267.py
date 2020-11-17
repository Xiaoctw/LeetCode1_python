from typing import *


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0
        r_count, c_count = [0] * r, [0] * c
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    r_count[i] += 1
                    c_count[j] += 1

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (r_count[i] > 1 or c_count[j] > 1):
                    count += 1
        return count


if __name__ == '__main__':
    sol=Solution()
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    print(sol.countServers(grid))
