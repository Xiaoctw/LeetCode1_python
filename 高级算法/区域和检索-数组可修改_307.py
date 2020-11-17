from typing import *


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.c = [0] * (self.n + 2)
        self.nums = nums
        for i, val in enumerate(nums):
            self.add_val(i + 1, val)

    def lowbit(self, i):
        return i & (-i)

    def add_val(self, idx, val):
        while idx <= self.n:
            self.c[idx] += val
            idx += self.lowbit(idx)

    def get_sum(self, i):
        tem = 0
        while i > 0:
            tem += self.c[i]
            i -= self.lowbit(i)
        return tem

    def update(self, i: int, val: int) -> None:
        self.add_val(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.get_sum(j + 1) - self.get_sum(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums=[1,3,5]
    arr=NumArray(nums)
    print(arr.sumRange(0,2))
    arr.update(0,4)
    arr.update(1,4)
    print(arr.sumRange(0,2))

