from typing import *


class Solution:
    def __init__(self):
        self.res = []
        self.visited = None
        self.graph = None

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.visited = [False] * len(graph)
        self.graph = graph
        self.dfs(len(graph), [], 0)
        return self.res

    def dfs(self, N, path, i):
        if i == N - 1:
            tem_path = path[:]
            tem_path.append(i)
            self.res.append(tem_path)
        self.visited[i] = True
        path.append(i)
        for j in self.graph[i]:
            if not self.visited[j]:
                self.dfs(N, path, j)
        path.pop()
        self.visited[i] = False


if __name__ == '__main__':
    sol = Solution()
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(sol.allPathsSourceTarget(graph))
