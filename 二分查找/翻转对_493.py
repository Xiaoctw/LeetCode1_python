from typing import *
import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = []
        res = 0
        for val in nums[::-1]:
            num1 = bisect.bisect_left(arr, val / 2)
            res += num1
            bisect.insort_left(arr, val)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [11, 4, 3, 5, 1]
    print(sol.reversePairs(nums))
