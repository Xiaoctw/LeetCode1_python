from typing import *
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        return self.right(nums, target) - self.left(nums, target) + 1

    def left(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi -= 1
        return lo

    def right(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo += 1
        return hi


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.search(nums, 4))
