from typing import *


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.back([], 1, 0, n, k)
        return self.res

    def back(self, list1, val, tem_sum, target, k):
        if tem_sum == target and len(list1) == k:
            self.res.append(list1[:])
            return
        if len(list1) > k or tem_sum > target or val >= 10:
            return
        self.back(list1, val + 1, tem_sum, target, k)
        list1.append(val)
        self.back(list1, val + 1, tem_sum + val, target, k)
        list1.pop()


if __name__ == '__main__':
    sol = Solution()
    k = 1
    n = 9
    print(sol.combinationSum3(k, n))
