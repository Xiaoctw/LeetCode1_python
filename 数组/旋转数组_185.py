from typing import *


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len1 = len(nums)
        k=k%len1
        self.reverse(nums, 0, len1 - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len1 - 1)
        return nums

    def reverse(self, nums, beg, end):
        i, j = beg, end
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    sol = Solution()
    nums = [-1]
    k = 2
    print(sol.rotate(nums, k))
