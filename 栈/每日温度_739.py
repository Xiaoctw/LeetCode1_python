from typing import *
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        len1=len(T)
        stack=[]
        ans=[0]*len1
        for i in range(len1):
            if not stack:
                stack.append(i)
            while stack and T[stack[-1]]<T[i]:
                pre_idx=stack.pop()
                ans[pre_idx]=i-pre_idx
            stack.append(i)
        return ans

if __name__ == '__main__':
    sol=Solution()
    tems=[73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(tems))