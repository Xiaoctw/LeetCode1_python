from typing import *
from collections import defaultdict


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        map1 = defaultdict(lambda: -1)
        stack = []
        for i in range(2 * len(nums)):
            idx = i % len(nums)
            while stack and nums[stack[-1]] < nums[idx]:
                map1[stack[-1]] = nums[idx]
                stack.pop()
            stack.append(idx)
        return [map1[i] for i in range(len(nums))]

if __name__ == '__main__':
    nums=[1,2,1]
    sol=Solution()
    print(sol.nextGreaterElements(nums))
