from typing import *
from collections import deque


class Solution:
    def helper(self, i1, j1, k):
        cnt = 0
        while i1 != 0:
            cnt += i1 % 10
            i1 //= 10
        while j1 != 0:
            cnt += j1 % 10
            j1 //= 10
        return cnt <= k

    def movingCount(self, m: int, n: int, k: int) -> int:
        dir1 = [-1, 0, 0, 1]
        dir2 = [0, -1, 1, 0]
        visited = [[False] * n for _ in range(m)]
        que = deque([])
        if k < 0:
            return 0
        que.append((0, 0))
        visited[0][0] = True
        cnt = 0
        while que:
            node = que.popleft()
            cnt += 1
            for i in range(4):
                i1, j1 = node[0] + dir1[i], node[1] + dir2[i]
                if 0 <= i1 < m and 0 <= j1 < n and self.helper(i1, j1, k) and not visited[i1][j1]:
                    visited[i1][j1] = True
                    que.append((i1, j1))
        return cnt


if __name__ == '__main__':
    sol = Solution()
    m = 2
    n = 3
    k = 1
    print(sol.movingCount(m, n, k))
