from typing import *


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        for i in range(n):
            self.back([], i, n)
        self.res1 = []
        for l in self.res:
            self.res1.append(self.make_str(l, n))
        return self.res1

    def make_str(self, l, n):
        res = []
        for val in l:
            l1 = ['.'] * n
            l1[val] = 'Q'
            res.append("".join(l1))
        return res

    def back(self, list1, val, n):
        list1.append(val)
        if len(list1) == n:
            self.res.append(list1[:])
            list1.pop()
            return
        for i in range(n):
            if self.judge(list1, i):
                self.back(list1, i, n)
        list1.pop()

    def judge(self, list1, val):
        x1, y1 = len(list1), val
        if val in list1:
            return False
        for x2, y2 in enumerate(list1):
            if y1 - y2 == x1 - x2 or y1 - y2 == x2 - x1:
                return False
        return True

if __name__ == '__main__':
    sol=Solution()
    print(sol.solveNQueens(4))
