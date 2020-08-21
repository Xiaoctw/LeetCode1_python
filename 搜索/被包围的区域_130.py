from typing import *


class Solution:
    def __init__(self):
        self.m, self.n = None, None
        self.set1 = set()
        self.dir1 = [-1, 0, 0, 1]
        self.dir2 = [0, 1, -1, 0]
        self.visited = None
        self.flag = True

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        self.m, self.n = len(board), len(board[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        for i in range(1, self.m - 1):
            for j in range(1, self.n - 1):
                self.flag = True
                self.set1 = set()
                if not self.visited[i][j] and board[i][j] == 'O':
                    self.dfs(board, i, j)
                    if self.flag:
                        for x1, y1 in self.set1:
                            board[x1][y1] = 'X'

    def dfs(self, board, i, j):
        self.set1.add((i, j))
        self.visited[i][j] = True
        for k in range(4):
            x1 = i + self.dir1[k]
            y1 = j + self.dir2[k]
            if x1 < 0 or x1 >= self.m or y1 < 0 or y1 >= self.n:
                continue
            if not self.visited[x1][y1] and board[x1][y1] == 'O':
                if x1 == 0 or y1 == 0 or x1 == self.m - 1 or y1 == self.n - 1:
                    self.flag = False
                self.dfs(board, x1, y1)


if __name__ == '__main__':
    sol = Solution()
    list1 = [['X', 'O', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    sol.solve(list1)
    print(list1)
