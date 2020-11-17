from typing import *


class TreeArr:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)
        self.arr=[0]*(n+1)

    def lowbit(self, i):
        return i & (-i)

    def update(self, i, val):
        self.arr[i] += val
        while i <= self.n:
            self.c[i] += val
            i += self.lowbit(i)


    def get_sum(self, i):
        tem = 0
        while i > 0:
            tem += self.c[i]
            i -= self.lowbit(i)
        return tem


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        set1 = set()
        for num in nums:
            set1.add(num)
            set1.add(num / 2)
        list1 = list(set1)
        list1.sort()
        treeArr = TreeArr(len(list1))
        dic1 = {val: i + 1 for i, val in enumerate(list1)}
        res = 0
        for val in nums[::-1]:
            idx = dic1[val/2]
            res += treeArr.get_sum(idx - 1)
            treeArr.update(dic1[val], 1)
        return res


if __name__ == '__main__':
    nums = [2,4,3,5,1]
    sol = Solution()
    print(sol.reversePairs(nums))
