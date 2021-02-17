from typing import *


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n
        return [i + 1 for i, num in enumerate(nums) if num <= n]


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDisappearedNumbers(nums))
