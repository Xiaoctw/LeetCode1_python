from typing import *


class Solution:
    def __init__(self):
        self.ans = None
        self.num_nodes = None
        self.dp = None
        self.graph = None
        self.visited = None

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        self.ans = [0] * N
        self.num_nodes = [0] * N
        self.dp = [0] * N
        self.visited = [False] * N
        self.graph = [[] for _ in range(N)]
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        self.dfs1(0)
        self.visited = [False] * N
        self.dfs2(0)
        return self.ans

    def dfs1(self, i):
        self.visited[i] = True
        self.num_nodes[i] = 1
        for j in self.graph[i]:
            if not self.visited[j]:
                self.dfs1(j)
                self.dp[i] += (self.dp[j] + self.num_nodes[j])
                self.num_nodes[i] += self.num_nodes[j]

    def dfs2(self, i):
        self.ans[i] = self.dp[i]
        self.visited[i] = True
        for j in self.graph[i]:
            if not self.visited[j]:
                self.dp[i] -= (self.dp[j] + self.num_nodes[j])
                self.num_nodes[i] -= self.num_nodes[j]
                self.dp[j] += (self.dp[i] + self.num_nodes[i])
                self.num_nodes[j] += self.num_nodes[i]
                self.dfs2(j)
                self.num_nodes[j] -= self.num_nodes[i]
                self.dp[j] -= (self.dp[i] + self.num_nodes[i])
                self.num_nodes[i] += self.num_nodes[j]
                self.dp[i] += (self.dp[j] + self.num_nodes[j])


if __name__ == '__main__':
    sol = Solution()
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    N = 6
    print(sol.sumOfDistancesInTree(N, edges))
