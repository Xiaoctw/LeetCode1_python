from typing import *
from collections import deque
from collections import defaultdict

class Solution:
    def __init__(self):
        self.visited = None
        self.cnt = 0
        self.map1=None
        self.set_path=None

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.set_path = set()
        self.map1=defaultdict(lambda :[])
        self.visited = [False] * n
        for connection in connections:
            self.set_path.add((connection[0], connection[1]))
            self.map1[connection[0]].append(connection[1])
            self.map1[connection[1]].append(connection[0])
        self.dfs(0,-1)
        return self.cnt

    def dfs(self, x, pre):
        self.visited[x]=True
        if (pre, x) in self.set_path:
            self.cnt += 1
        for y in self.map1[x]:
            if not self.visited[y]:
                self.dfs(y,x,)

if __name__ == '__main__':
    sol=Solution()
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(sol.minReorder(n,connections))


