from typing import *
from collections import defaultdict


class Solution:
    """
    利用染色的方法判断一个图是否是二分图

    """

    def __init__(self):
        self.flag = True
        self.colors = None
        self.graph = None

    def isBipartite(self, graph: List[List[int]]) -> bool:
        num_node = len(graph)
        self.graph = graph
        self.colors = [0] * num_node
        for i in range(num_node):
            if self.colors[i] == 0:
                self.dfs(i, 1)
        return self.flag

    def dfs(self, node, c):
        if not self.flag:
            return
        self.colors[node] = c
        for node1 in self.graph[node]:
            if self.colors[node1] == c:
                self.flag = False
            elif self.colors[node1] == 0:
                self.dfs(node1, -c)


if __name__ == '__main__':
    sol = Solution()
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(sol.isBipartite(graph))
