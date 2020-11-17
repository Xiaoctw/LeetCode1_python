from typing import *


class Solution:
    def __init__(self):
        self.graph = None
        self.dic1 = {}
        self.dic2 = {}
        self.broken_Set = set()
        self.used = None
        self.match = None

    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        for broken_list in broken:
            self.broken_Set.add((broken_list[0], broken_list[1]))
        N = (m * n) // 2 + 1
        self.graph = [[0] * N for _ in range(N)]
        idx1, idx2 = 0, 0
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 0:
                    self.dic1[i, j] = idx1
                    idx1 += 1
                else:
                    self.dic2[i, j] = idx2
                    idx2 += 1
        for i in range(n):
            for j in range(m):
                if (i, j) not in self.broken_Set:
                    self.add(i, j, n, m)

        res = 0
        self.match = [-1] * N  # 标记匹配结果,没有匹配用-1，因为存在下表为0的用户，
        # 因此不能设为0。
        for i in range(N):
            self.used = [0] * N
            if self.find(i):
                res += 1
        return res

    # 这里给出匈牙利算法的步骤
    def find(self, x):
        for j in range(len(self.match)):
            if self.graph[x][j] and not self.used[j]:
                self.used[j] = 1
                if self.match[j] == -1 or self.find(self.match[j]):
                    self.match[j] = x
                    return True
        return False

    def add(self, i, j, n, m):
        dir1 = [0, 1, -1, 0]
        dir2 = [1, 0, 0, -1]
        for k in range(4):
            x, y = i + dir1[k], j + dir2[k]
            if 0 <= x < n and 0 <= y < m and (x, y) not in self.broken_Set:
                if (i + j) % 2 == 0:
                    self.graph[self.dic1[i, j]][self.dic2[x, y]] = 1
                else:
                    self.graph[self.dic1[x, y]][self.dic2[i, j]] = 1


if __name__ == '__main__':
    sol = Solution()
    n = 2
    m = 3
    broken = [[1, 0], [1, 1]]
    print(sol.domino(n, m, broken))
