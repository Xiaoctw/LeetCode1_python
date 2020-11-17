from typing import *
from collections import defaultdict


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        found = False

        def find_next(idx_i, idx_j):
            next_i, next_j = None, None
            for i in range(idx_i, 9):
                if next_i is not None:
                    break
                for j in range(9):
                    if i == idx_i and j <= idx_j:
                        continue
                    if board[i][j] == '.':
                        next_i, next_j = i, j
                        break
            return next_i, next_j

        def back(idx_i, idx_j, val):
            nonlocal found
            board[idx_i][idx_j] = val
            row_sets[idx_i].add(val)
            col_sets[idx_j].add(val)
            box_sets[idx_i // 3, idx_j // 3].add(val)
            next_i, next_j = find_next(idx_i, idx_j)
            if next_i is None:
                found = True
                return
            box_next_i, box_next_j = next_i // 3, next_j // 3
            for next_val in range(1, 10):
                next_val = str(next_val)
                if next_val not in row_sets[next_i] and next_val not in col_sets[next_j] and next_val not in box_sets[box_next_i, box_next_j]:
                    back(next_i, next_j, next_val)
            if not found:
                board[idx_i][idx_j] = '.'
                row_sets[idx_i].remove(val)
                col_sets[idx_j].remove(val)
                box_sets[idx_i // 3, idx_j // 3].remove(val)

        row_sets = defaultdict(lambda: set())
        col_sets = defaultdict(lambda: set())
        box_sets = defaultdict(lambda: set())
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    row_sets[i].add(board[i][j])
                    col_sets[j].add(board[i][j])
                    box_i, box_j = i // 3, j // 3
                    box_sets[box_i, box_j].add(board[i][j])
        idx_i, idx_j = find_next(0, -1)
        for val in range(1, 10):
            val = str(val)
            if found:
                break
            if val not in row_sets[idx_i] and val not in col_sets[idx_j] and val not in box_sets[
                idx_i // 3, idx_j // 3]:
                back(idx_i, idx_j, val)


if __name__ == '__main__':
    sol = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol.solveSudoku(board)
    print(board)
