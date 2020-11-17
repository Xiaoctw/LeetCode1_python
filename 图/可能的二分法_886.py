from typing import *
from collections import defaultdict


class Solution:
    def __init__(self):
        self.colors = None
        self.graph = defaultdict(lambda: [])
        self.flag = True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.colors = [0] * (N+1)
        for dislike in dislikes:
            self.graph[dislike[0]].append(dislike[1])
            self.graph[dislike[1]].append(dislike[0])

        for i in range(1,N+1):
            if not self.flag:
                return False
            if self.colors[i]==0:
                self.dfs(i, 1)
        return True

    def dfs(self, i, c):
        if not self.flag:
            return
        self.colors[i] = c
        for j in self.graph[i]:
            if self.colors[j] == c:
                self.flag = False
            elif self.colors[j] == 0:
                self.dfs(j, -c)

if __name__ == '__main__':
    sol=Solution()
    N = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    print(sol.possibleBipartition(N,dislikes))