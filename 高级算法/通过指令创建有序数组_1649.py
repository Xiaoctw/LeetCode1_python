from typing import *


class TreeArr:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def lowbit(self, i):
        return i & (-i)

    def update(self, i, val):
        while i <= self.n:
            self.c[i] += val
            i += self.lowbit(i)

    def get_sum(self, i):
        res = 0
        while i > 0:
            res += self.c[i]
            i -= self.lowbit(i)
        return res


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = int(10 ** 9 + 7)
        list1 = list(set(instructions))
        list1.sort()
        dic1 = {val: i + 1 for i, val in enumerate(list1)}
        treeArr = TreeArr(len(list1))
        total_num = 0
        res = 0
        for val in instructions:
            idx = dic1[val]
            left = treeArr.get_sum(idx - 1)
            right = total_num - treeArr.get_sum(idx)
            res = (res + min(left, right)) % mod
            total_num += 1
            treeArr.update(idx, 1)
        return res


if __name__ == '__main__':
    instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]
    sol = Solution()
    print(sol.createSortedArray(instructions))
