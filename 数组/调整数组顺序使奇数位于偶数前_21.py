from typing import *


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = -1
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 3, 6, 2, 1, 5, 2, 6, 2, 5, 7, 8, 7, 7, 10, 3, 2]
    print(sol.exchange(nums))
