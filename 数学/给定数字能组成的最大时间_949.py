from typing import *
import itertools


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans = -1
        i1, j1, k1, l1 = -1, -1, -1, -1
        # 返回arr中元素的所有排列
        for i, j, k, l in itertools.permutations(arr):
            h = 10 * i + j
            m = 10 * k + l
            if 0 <= h <= 23 and 0 <= m <= 59:
                if 60 * h + m > ans:
                    i1, j1, k1, l1 = i, j, k, l
                    ans = 60 * h + m
        if ans == -1:
            return ''
        return '{}{}:{}{}'.format(i1, j1, k1, l1)


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 3, 4]
    print(set(itertools.permutations(arr)))
    print(sol.largestTimeFromDigits(arr))
