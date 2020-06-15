from types import *
from typing import *
import sys
class Solution:
    '''
    控制一个栈，栈重元素单调增
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        if n==0:
            return 0
        stack=[]
        lefts,rights=[0]*n,[0]*n
        #arr=[-sys.maxsize]+heights+[-sys.maxsize]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                lefts[i]=-1
            else:
                lefts[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                rights[i]=n
            else:
                rights[i]=stack[-1]
            stack.append(i)
        return max([(rights[i]-lefts[i]-1)*heights[i] for i in range(n)])

if __name__ == '__main__':
    sol=Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3]))



