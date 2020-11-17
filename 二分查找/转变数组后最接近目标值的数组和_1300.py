from typing import *
import bisect


class Solution:
    """
    双重二分搜索
    """

    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        sums = [0]
        for val in arr:
            sums.append(sums[-1] + val)
        lo, hi = 0, arr[-1]
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            tem_sum = self.find_sum(arr, sums, mid)
            if tem_sum >= target:
                hi = mid - 1
            else:
                lo = mid + 1

        if abs(self.find_sum(arr, sums, hi) - target) <= abs(self.find_sum(arr, sums, hi + 1) - target):
            return hi
        return hi + 1

    def find_sum(self, arr, sums, val):
        idx = bisect.bisect_left(arr, val)
        tem_sum = sums[idx] + val * (len(arr) - idx)
        return tem_sum


if __name__ == '__main__':
    sol = Solution()
    arr = [60864, 25176, 27249, 21296, 20204]
    # print(bisect.bisect_left(arr, 0))
    target = 56803
    print(sol.findBestValue(arr, target))
