from typing import *
from collections import defaultdict


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n
        for i in range(2 * n):
            # 维持一个单调不升的栈
            # 注意这里是while
            while stack and nums[i % n] > nums[stack[-1] % n]:
                pre = stack.pop()
                res[pre % n] = nums[i % n]
            stack.append(i)
        return res


if __name__ == '__main__':
    nums = [0]
    sol = Solution()
    print(sol.nextGreaterElements(nums))
