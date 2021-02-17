from typing import *
from collections import defaultdict


class Solution:
    def __init__(self):
        self.arr = None

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        N = len(dominoes)
        self.arr = list(range(N))
        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                for j in range(i + 1, N):
                    if not visited[j] and ((dominoes[i][0] == dominoes[j][0] and dominoes[j][1] == dominoes[i][1])
                                           or (dominoes[i][1] == dominoes[j][0] and dominoes[j][1] == dominoes[i][0])):
                        self.set_union(i, j)
                        visited[i] = True
                        visited[j] = True
                visited[i]=True
        dic1 = defaultdict(int)
        for i in range(N):
            dic1[self.find(i)] += 1
        res = 0
        for key in dic1:
            res += dic1[key] * (dic1[key] - 1) // 2
        return res

    def find(self, i):
        if self.arr[i] != i:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

    def set_union(self, i, j):
        find_i = self.find(i)
        find_j = self.find(j)
        if find_j != find_i:
            self.arr[find_j] = find_i

if __name__ == '__main__':
    sol=Solution()
    dominoes =[[1,2],[1,2],[1,1],[1,2],[2,2]]
    print(sol.numEquivDominoPairs(dominoes))