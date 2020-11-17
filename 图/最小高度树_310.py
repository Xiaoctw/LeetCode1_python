from typing import *
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        que = deque([])
        for i in range(n):
            if len(graph[i]) == 1:
                que.append(i)
        visited = [False] * n
        res = []
        while que:
            res = []
            size = len(que)
            for _ in range(size):
                x = que.popleft()
                visited[x] = True
                res.append(x)
                for neighbor in graph[x]:
                    if visited[neighbor]:
                        continue
                    graph[neighbor].remove(x)
                    if len(graph[neighbor]) == 1:
                        que.append(neighbor)
        return res


if __name__ == '__main__':
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    sol = Solution()
    print(sol.findMinHeightTrees(6, edges))
