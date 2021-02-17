from typing import *
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque([])
        res = []
        for i in range(len(nums)):
            if que and i >= k and nums[i - k] == que[0]:
                que.popleft()
            while que and que[-1] < nums[i]:
                que.pop()
            que.append(nums[i])
            if i >= k - 1:
                res.append(que[0])
        return res


if __name__ == '__main__':
    nums = [7, 2, 4]
    k = 2
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))
