from typing import *
from collections import defaultdict


class Solution:
    def __init__(self):
        self.dp = defaultdict(lambda: float('inf'))
        self.graph = defaultdict(lambda: [])

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        for flight in flights:
            self.dp[flight[0], flight[1], 1] = flight[2]
            self.dp[flight[0], flight[0], 0] = 0
            self.dp[flight[1], flight[1], 0] = 0
            self.graph[flight[0]].append((flight[1], flight[2]))
        min_val=float('inf')
        for i in range(K+2):
            min_val=min(min_val,self.find(src,dst,i))
        if min_val==float('inf'):
            return -1
        return min_val

    def find(self, a, b, k):
        if k < 0:
            return float('inf')
        if (a, b, k) in self.dp:
            return self.dp[a, b, k]
        min_val = float('inf')
        for c in self.graph[a]:
            min_val = min(min_val, self.find(c[0], b, k - 1) + c[1])
        self.dp[a, b, k] = min_val
        return min_val

if __name__ == '__main__':
    sol=Solution()
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(sol.findCheapestPrice(n,edges,src,dst,k))
