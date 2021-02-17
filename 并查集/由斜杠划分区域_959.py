from typing import *


class Solution:
    def __init__(self):
        self.arr = None

    def find(self, x):
        if self.arr[x] != x:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]

    def set_union(self, i, j):
        find_i = self.find(i)
        find_j = self.find(j)
        if find_j != find_i:
            self.arr[find_j] = find_i

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        self.arr = list(range(4 * n * n))
        for i in range(n):
            for j in range(n):
                idx = i * n + j
                if i < n - 1:
                    bottom = idx + n
                    self.set_union(idx * 4 + 2, bottom * 4)
                if j < n - 1:
                    right = idx + 1
                    self.set_union(idx * 4 + 1, right * 4 + 3)
                if grid[i][j] == '/':
                    self.set_union(idx * 4, idx * 4 + 3)
                    self.set_union(idx * 4 + 1, idx * 4 + 2)
                elif grid[i][j] == '\\':
                    self.set_union(idx * 4, idx * 4 + 1)
                    self.set_union(idx * 4 + 2, idx * 4 + 3)
                else:
                    self.set_union(idx * 4, idx * 4 + 1)
                    self.set_union(idx * 4 + 1, idx * 4 + 2)
                    self.set_union(idx * 4 + 2, idx * 4 + 3)
        roots=set()
        for i in range(4*n*n):
            roots.add(self.find(i))
        return len(roots)

if __name__ == '__main__':
    sol=Solution()
    grid=[
        "\\/",
        "/\\"
    ]
    print(sol.regionsBySlashes(grid))