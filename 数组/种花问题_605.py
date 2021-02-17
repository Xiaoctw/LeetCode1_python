from typing import *
import math


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        len1 = len(flowerbed)
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i == 0 and i == len1 - 1:
                if flowerbed[i] == 0:
                    cnt += 1
            elif i == 0 and i + 1 < len1 and flowerbed[i + 1] == 0:
                cnt += 1
                flowerbed[i] = 1
            elif i == len1 - 1 and i - 1 >= 0 and flowerbed[i - 1] == 0:
                cnt += 1
                flowerbed[i] = 1
            elif i > 0 and flowerbed[i - 1] == 0 and i + 1 < len1 and flowerbed[i + 1] == 0:
                cnt += 1
                flowerbed[i] = 1
        return cnt >= n


if __name__ == '__main__':
    sol = Solution()
    nums = [1,0,0,0,1]
    n = 1
    print(sol.canPlaceFlowers(nums, n))
