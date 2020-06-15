from typing import *
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return []
        ###这个队列中保存的是窗口内的元素，保持降序!!!!!!!
        #不止是栈可以采取这种操作
        que=deque()
        res,n=[],len(nums)
        for i in range(k):
            while que and que[-1]<nums[i]:
                que.pop()
            que.append(nums[i])
        res.append(que[0])
        for i in range(n-k):
            if que[0]==nums[i]:
                que.popleft()
            while que and que[-1]<nums[i+k]:
                que.pop()
            que.append(nums[i+k])
            res.append(que[0])
        return res
if __name__ == '__main__':
    sol=Solution()
    nums=[1,3,-1,-3,5,8,8,8,8,8,8,3,6,7,4]
    print(sol.maxSlidingWindow(nums,3))
