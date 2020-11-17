from typing import *
import sys


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[-1] * (N + 1) for _ in range(N + 1)]
        for time in times:
            graph[time[0]][time[1]] = time[2]
        max_dist = max(self.Dij(graph, K, N))
        return max_dist if max_dist < sys.maxsize else -1

    def Dij(self, graph, start, N):
        visited = [False] * (N + 1)
        dist = [sys.maxsize] * (N + 1)
        dist[start] = 0
        for _ in range(N):
            min_val = sys.maxsize
            index = -1
            for i in range(1, N + 1):
                if not visited[i] and dist[i] < min_val:
                    min_val = dist[i]
                    index = i
            if -1 == index:
                break
            visited[index] = True
            for i in range(1, N + 1):
                if not visited[i] and graph[index][i] != -1:
                    if dist[i] > (dist[index] + graph[index][i]):
                        dist[i] = dist[index] + graph[index][i]
        return dist[1:]


if __name__ == '__main__':
    sol = Solution()
    times = [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75],
             [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51],
             [3, 1, 36], [2, 3, 59]]
    N = 5
    K = 5
    print(sol.networkDelayTime(times, N, K))
