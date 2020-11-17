from typing import *
import itertools
import collections
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        if not graph: return -1
        N = len(graph)
        clean = set(range(N)) - set(initial)
        parents = list(range(N))
        size = [1] * N

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if size[rx] < size[ry]:
                    parents[rx] = ry
                    size[ry] += size[rx]
                else:
                    parents[ry] = rx
                    size[rx] += size[ry]

        for u, v in itertools.combinations(clean, 2):
            if graph[u][v]: union(u, v)

        d = collections.defaultdict(set)
        infectedTimes = collections.Counter()
        for u in initial:
            for v in clean:
                if graph[u][v]: d[u].add(find(v))

            for comm in d[u]:
                infectedTimes[comm] += 1

        count = [0] * N
        for u, comms in d.items():
            for comm in comms:
                if infectedTimes[comm] == 1:
                    count[u] += size[comm]

        maxi = max(count)
        return count.index(maxi) if maxi != 0 else min(initial)


if __name__ == '__main__':
    sol = Solution()
    graph =  [[1,1,0,0],[1,1,0,1],[0,0,1,0],[0,1,0,1]]
    initial = [3,0]
    print(sol.minMalwareSpread(graph, initial))
