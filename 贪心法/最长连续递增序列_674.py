from typing import *


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        max_len = 1
        beg = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                max_len = max(max_len, i - beg + 1)
            else:
                beg = i
        return max_len


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 2, 2, 2, 2]
    print(sol.findLengthOfLCIS(nums))
