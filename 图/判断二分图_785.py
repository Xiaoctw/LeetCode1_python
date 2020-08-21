from typing import *
from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph=defaultdict(lambda :[])
        self.group=None
        self.flag=True
        self.visited=None

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        self.graph=graph
        self.visited=[False]*n
        self.group=[-1]*n
        for i in range(n):
            if not self.visited[i]:
                self.dfs(i,0)
        return self.flag

    def dfs(self,node,val):
        if not self.flag:
            return
        self.group[node]=val
        self.visited[node]=True
        if val==0:
            val1=1
        else:
            val1=0
        for node1 in self.graph[node]:
            if self.group[node1]==val:
                self.flag=False
        for node1 in self.graph[node]:
            if not self.visited[node1]:
                self.dfs(node1,val1)


if __name__ == '__main__':
    sol=Solution()
    graph=[[1,2,3], [0,2], [0,1,3], [0,2]]
    print(sol.isBipartite(graph))