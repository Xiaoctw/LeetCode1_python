from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        dir1 = [-1, 0, 0, 1]
        dir2 = [0, 1, -1, 0]
        flag = False

        def back(x1, y1, idx):
            nonlocal flag
            if idx >= len(word) or board[x1][y1] != word[idx] or flag:
                return
            if idx == len(word) - 1:
                flag = True
            visited[x1][y1] = True
            for i in range(4):
                x2, y2 = x1 + dir1[i], y1 + dir2[i]
                if 0 <= x2 < m and 0 <= y2 < n and not visited[x2][y2]:
                    back(x2, y2, idx + 1)

            visited[x1][y1] = False

        for i in range(m):
            for j in range(n):
                back(i, j, 0)

        return flag


if __name__ == '__main__':
    sol = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCB'
    print(sol.exist(board, word))
