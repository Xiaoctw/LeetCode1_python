from typing import *
from collections import defaultdict


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic1 = defaultdict(lambda: float('inf'))
        for i, val in enumerate(arr2):
            dic1[val] = i
        arr1.sort(key=lambda x: (dic1[x], x))
        return arr1


if __name__ == '__main__':
    sol = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(sol.relativeSortArray(arr1, arr2))
