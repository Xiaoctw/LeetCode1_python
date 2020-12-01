from typing import *
import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx1 = bisect.bisect_left(nums, target)
        idx2 = bisect.bisect_right(nums, target)
        if idx1 >= len(nums) or nums[idx1] != target:
            return [-1, -1]
        return [idx1, idx2 - 1]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 9, 9, 9, 10]
    sol = Solution()
    print(sol.searchRange(nums, 4))
