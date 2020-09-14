from typing import *


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 5, 5, 5, 5, 6]
    target = 3
    print(sol.searchInsert(nums, target))
