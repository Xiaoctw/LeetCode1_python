from typing import *
from collections import defaultdict


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        window_sum = sum(nums) - x
        r = 0
        l = 0
        tem_sum = 0
        max_len = -1
        if tem_sum == window_sum:
            max_len = 0
        while r < len(nums):
            tem_sum += nums[r]
            while l<=r and tem_sum > window_sum:
                tem_sum=tem_sum-nums[l]
                l+=1
            if tem_sum == window_sum:
                max_len = max(max_len, r - l + 1)
            r += 1
        if max_len==-1:
            return -1
        return len(nums)-max_len

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1]
    x = 3
    print(sol.minOperations(nums, x))
