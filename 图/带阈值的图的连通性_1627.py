from typing import *
import math


class Solution:
    def __init__(self):
        self.arr = None

    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        self.arr = [i for i in range(n + 1)]
        for k in range(threshold + 1, n // 2 + 1):
            i = 1
            while (i + 1) * k <= n:
                # 进行合并，没必要合并所有的边
                self.set_union(i * k, (i + 1) * k)
                i += 1
        return [self.find(query[0]) == self.find(query[1]) for query in queries]

    def set_union(self, i, j):
        find_i = self.find(i)
        find_j = self.find(j)
        if find_j != find_i:
            self.arr[find_j] = find_i

    def find(self, i):
        if i != self.arr[i]:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]


if __name__ == '__main__':
    sol = Solution()
    n = 5
    threshold = 1
    queries = [[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]]
    print(sol.areConnected(n, threshold, queries))
