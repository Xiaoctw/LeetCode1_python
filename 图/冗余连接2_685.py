from typing import *
from collections import *


class Solution:

    def __init__(self):
        self.findSet = {}

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> [List[int]]:
        n = len(edges)
        indegrees = [0] * (n + 1)
        for edge in edges:
            indegrees[edge[1]] += 1
        list1 = []
        for (i, edge) in enumerate(edges):
            if indegrees[edge[1]] > 1:
                list1.append(i)

        if len(list1) > 0:
            if self.judge_remove_edge(edges, list1[1]):
                return edges[list1[1]]
            return edges[list1[0]]

        self.findSet = {i: i for i in range(1, len(edges) + 1)}
        for edge in edges:
            if self.find(edge[0]) == self.find(edge[1]):
                return edge
            self.union_set(edge[0], edge[1])
        return []

    def judge_remove_edge(self, edges, i):
        self.findSet = {i: i for i in range(1, len(edges) + 1)}
        for j in range(len(edges)):
            if j == i:
                continue
            if self.find(edges[j][0]) == self.find(edges[j][1]):
                return False
            self.union_set(edges[j][0], edges[j][1])
        return True

    def find(self, i):
        while i != self.findSet[i]:
            i = self.findSet[i]
        return i

    def union_set(self, i, j):
        find_i = self.find(i)
        find_j = self.find(j)
        if find_j != find_i:
            self.findSet[find_i] = find_j


if __name__ == '__main__':
    sol = Solution()
    edges = [[1,2], [1,3], [2,3]]
    print(sol.findRedundantDirectedConnection(edges))
