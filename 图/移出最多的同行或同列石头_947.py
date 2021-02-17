from typing import *


class Solution:
    def __init__(self):
        self.arr = None

    def find(self, i):
        if i != self.arr[i]:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

    def set_union(self, i, j):
        find_i = self.find(i)
        find_j = self.find(j)
        if find_i != find_j:
            self.arr[find_i] = find_j

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        self.arr = [i for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.set_union(i, j)
        return n-len(set(self.find(i) for i in range(n)))

if __name__ == '__main__':
    sol=Solution()
    nums=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(sol.removeStones(nums))