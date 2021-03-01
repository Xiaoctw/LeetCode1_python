from typing import *
from collections import deque, defaultdict


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        que1 = deque([])  # 包括最后一个元素的递增
        que2 = deque([])  # 包括最后一个元素的递减
        j = 0
        max_len = 1
        for i in range(len(nums)):
            while que1 and nums[i] > que1[-1]:
                que1.pop()
            while que2 and nums[i] < que2[-1]:
                que2.pop()
            que1.append(nums[i])
            que2.append(nums[i])
            while que1 and que2 and abs(que2[0] - que1[0]) > limit:
                if nums[j] == que1[0]:
                    que1.popleft()
                if nums[j] == que2[0]:
                    que2.popleft()
                j+=1
            max_len = max(max_len, i - j + 1)
        return max_len


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 2, 2, 2, 4, 4, 2, 2]
    limit = 0
    print(sol.longestSubarray(nums, limit))
