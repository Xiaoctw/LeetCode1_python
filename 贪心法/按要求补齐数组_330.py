from typing import *


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, x = 0, 1
        length, index = len(nums), 0

        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                patches += 1
        return patches


if __name__ == '__main__':
    nums = [1, 2, 2]
    n = 5
    sol = Solution()
    print(sol.minPatches(nums, n))
