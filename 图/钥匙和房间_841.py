from typing import *
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        que = deque([])
        que.append(0)
        visited[0] = True
        cnt = 0
        while que:
            tem = que.popleft()
            cnt += 1
            for j in rooms[tem]:
                if not visited[j]:
                    que.append(j)
                    visited[j] = True
        return cnt == n


if __name__ == '__main__':
    sol = Solution()
    print('first')
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(sol.canVisitAllRooms(rooms))
    print('Hello')
