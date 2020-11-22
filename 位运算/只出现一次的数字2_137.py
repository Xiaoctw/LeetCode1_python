from typing import *
from bitarray import bitarray
import math

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            mask = 1 << i
            cnt = 0
            for num in nums:
                if mask & num:
                    cnt += 1
            if cnt % 3 != 0:
                res |= mask
        return res


if __name__ == '__main__':
    sol = Solution()
    print(bin(-2))
    print(bin(-10))
    print(bitarray(10))
    nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
    print(sol.singleNumber(nums))
