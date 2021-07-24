from typing import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if not arr or arr[-1] < num:
                arr.append(num)
            else:
                idx = self.search(num, arr)
                arr[idx] = num
        return len(arr)

    def search(self, val, arr):
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (hi - lo) // 2 + lo
            if arr[mid] >= val:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    arr = [1, 5, 6, 7, 8]
    print(sol.lengthOfLIS(nums))
