from typing import *
import sys

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        min_val = sys.maxsize
        while lo <= hi:
            mid = (lo + hi) // 2
            min_val = min(min_val, nums[lo], nums[hi], nums[mid])
            if nums[mid] > nums[lo]:
                lo = mid + 1
            elif nums[mid] < nums[lo]:
                hi = mid - 1
            else:  # 处理相等情况，最小值递增，在这里不会漏掉最小值，因为nums[lo]和nums[mid]相等。
                lo += 1
        return min_val


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 2, 2, 0, 1]
    print(sol.findMin(nums))
