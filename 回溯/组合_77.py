from typing import *


class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        for i in range(1, n + 1):
            self.back([], i, n, k)
        return self.res

    def back(self, list1, val, n, k):
        list1.append(val)
        if len(list1) == k:
            self.res.append(list1[:])
            list1.pop()
            return
        for i in range(val + 1, n + 1):
            self.back(list1, i, n, k)
        list1.pop()
        return


if __name__ == '__main__':
    sol = Solution()
    n = 4
    k = 2
    print(sol.combine(n, k))
