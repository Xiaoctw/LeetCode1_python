from typing import *
import sys


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = max(nums), sum(nums)
        res = lo  # 先指定一个值，lo还是hi无所谓，但是不要是-1，否则可能出错
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.judge(nums, mid, m):
                hi = mid - 1
                res = mid
            else:
                lo = mid + 1
        return res

    def judge(self, nums, val, m):
        tem_sum = 0
        k = 0
        i = 0
        while i < len(nums):
            tem_sum += nums[i]
            if tem_sum > val:
                k += 1
                tem_sum = 0
            else:
                i += 1
        k += 1
        return k <= m


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    m = 15
    print(sol.splitArray(nums, 1))
