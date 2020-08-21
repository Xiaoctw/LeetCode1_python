from typing import *
import sys


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0
        tem_sum = 0
        min_len = sys.maxsize
        for j in range(len(nums)):
            tem_sum += nums[j]
            while i <= j and tem_sum >= s:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                tem_sum -= nums[i]
                i += 1
        if min_len < sys.maxsize:
            return min_len
        return 0


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    print(sol.minSubArrayLen(s, nums))
