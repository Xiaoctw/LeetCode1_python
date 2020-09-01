from typing import *
from collections import defaultdict, deque
import heapq


class Solution:
    def __init__(self):

        self.graph = defaultdict(lambda: [])
        self.visited = defaultdict(lambda: False)
        self.res = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        本题可能出现这种情况：走着走着走到了死胡同，出不去了。要避免这种情况的发生
        :param tickets:
        :return:
        """
        graph = defaultdict(list)
        stack = []

        def dfs(cur):
            while graph[cur]:
                tem = heapq.heappop(graph[cur])
                dfs(tem)
            stack.append(cur)

        for a, b in tickets:
            graph[a].append(b)
        for key in graph:
            heapq.heapify(graph[key])
        dfs('JFK')
        return stack[::-1]


if __name__ == '__main__':
    sol = Solution()
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(sol.findItinerary(tickets))
