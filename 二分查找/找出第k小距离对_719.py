from typing import *


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_val = nums[-1] - nums[0]
        min_val = max_val
        for i in range(1, len(nums)):
            min_val = min(min_val, nums[i] - nums[i - 1])
        lo, hi = min_val, max_val
        while lo <= hi:
            mid = (hi + lo) // 2
            cnt = self.helper(nums, mid, k)
            if cnt == k:
                res = mid
                hi = mid - 1
            elif cnt < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi

    def helper(self, nums, val, k):
        cnt = 0
        j = 0
        for i in range(1, len(nums)):
            while j < i and nums[j] + val <= nums[i]:
                j += 1
            cnt += (i - j)
        return cnt


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 1]
    k = 1
    print(sol.smallestDistancePair(nums, k))
