from typing import *


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.c = [0] * (self.n + 2)
        for i, val in enumerate(nums):
            self.update(i + 1, val)

    def lowbit(self, i):
        return i & (-i)

    def update(self, idx, val):
        while idx <= self.n:
            self.c[idx] += val
            idx += self.lowbit(idx)

    def get_sum(self, idx):
        s = 0
        while idx > 0:
            s += self.c[idx]
            idx -= self.lowbit(idx)
        return s

    def sumRange(self, i: int, j: int) -> int:
        return self.get_sum(j + 1) - self.get_sum(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
