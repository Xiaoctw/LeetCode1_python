from typing import *


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic1 = {}
        for val in arr:
            dic1[val] = self.num_one(val)
        arr.sort(key=lambda x: (dic1[x], x))
        return arr

    def num_one(self, val):
        num = 0
        while val:
            val = val & (val - 1)
            num += 1
        return num


if __name__ == '__main__':
    sol = Solution()
    print(3 & 1)
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(sol.sortByBits(arr))
