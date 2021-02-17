from typing import *
from collections import defaultdict


class Solution:
    def __init__(self):
        self.parent = None
        self.edge2val = {}
        self.edge2idx = {}
        self.graph = defaultdict(lambda: [])

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        # while i != self.parent[i]:
        #     i = self.parent[i]
        return self.parent[i]

    def set_union(self, i, j):
        i, j = self.find(i), self.find(j)
        if i != j:
            self.parent[i] = j

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.parent = list(range(n))
        m = len(edges)
        for i, edge in enumerate(edges):
            self.edge2val[(edge[0], edge[1])] = edge[2]
            self.edge2val[(edge[1], edge[0])] = edge[2]
            self.edge2idx[(edge[0], edge[1])] = i
            self.edge2idx[(edge[1], edge[0])] = i
        edges.sort(key=lambda x: x[2])
        set_used = set()
        for _ in range(n - 1):
            idx = 0
            for i in range(m):
                if self.edge2idx[edges[i][0], edges[i][1]] not in set_used and self.find(edges[i][0]) != self.find(
                        edges[i][1]):
                    idx = i
                    break
            self.set_union(edges[idx][0], edges[idx][1])
            # 这里必须是并查集中的边
            self.graph[edges[idx][0]].append(edges[idx][1])
            self.graph[edges[idx][1]].append(edges[idx][0])
            set_used.add(self.edge2idx[edges[idx][0], edges[idx][1]])

        visited = [False] * n
        root_set = set()
        for i in range(n):
            if self.find(i) == i:
                root_set.add(i)
        for i in root_set:
            if not visited[i]:
                self.dfs(i, visited)
        edges1, edges2 = set(), set()
        for i in range(m):
            if i not in set_used:
                self.judge(edges[i][0], edges[i][1], edges1)
        for i in set_used:
            if i not in edges1:
                edges2.add(i)
        return [list(edges2), list(edges1)]

    def judge(self, i, j, edges1):
        edges = []
        i1, j1 = i, j
        while i != j:
            if i != self.parent[i]:
                edges.append((i, self.parent[i]))
            if j != self.parent[j]:
                edges.append((j, self.parent[j]))
            i = self.parent[i]
            j = self.parent[j]
        for edge in edges:
            if self.edge2val[edge[0], edge[1]] == self.edge2val[i1, j1]:
                edges1.add(self.edge2idx[i1, j1])
                edges1.add(self.edge2idx[edge[0], edge[1]])

    def dfs(self, i, visited):
        visited[i] = True
        for j in self.graph[i]:
            if not visited[j]:
                self.parent[j] = i
                self.dfs(j, visited)


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0, 1, 2], [0, 2, 5], [2, 3, 5], [1, 4, 4], [2, 5, 5], [4, 5, 2]]
    print(sol.findCriticalAndPseudoCriticalEdges(n, edges))
