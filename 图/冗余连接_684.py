from typing import *


class Solution:
    def __init__(self):
        self.res = None
        self.arr = None
        # self.num_node = None

    def find(self, x):
        if x != self.arr[x]:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]

    def union_set(self, x, y):
        find_x = self.find(x)
        find_y = self.find(y)
        if find_x == find_y:
            # 这里需要注意，如果发现x和y处于同一个cluster当中，说明这个边是冗余的
            self.res = [x, y]
        else:
            self.arr[find_x] = find_y

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.arr = [i for i in range(n + 1)]
        for edge in edges:
            if self.res:
                return self.res
            self.union_set(edge[0], edge[1])
        return self.res


if __name__ == '__main__':
    sol = Solution()
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(sol.findRedundantConnection(edges))
