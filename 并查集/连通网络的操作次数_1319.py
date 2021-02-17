from typing import *


class Solution:
    def __init__(self):
        self.arr = None

    def find(self, i):
        if i != self.arr[i]:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

    def set_union(self,i,j):
        find_i=self.find(i)
        find_j=self.find(j)
        if find_j!=find_i:
            self.arr[find_j]=find_i



    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        self.arr = list(range(n))
        for connection in connections:
            self.set_union(connection[0],connection[1])
        cnt=sum([i==self.find(i) for i in range(n)])
        return cnt-1

if __name__ == '__main__':
    sol=Solution()
    n = 5
    connections = [[0,1],[0,2],[3,4],[2,3]]
    print(sol.makeConnected(n,connections))
