from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        max_rights=[0]*len(height)
        max_rights[-1]=-1
        max_val=height[-1]
        max_idx=len(height)-1
        for i in range(len(height)-2,-1,-1):
            max_rights[i]=max_idx
            if height[i]>max_val:
                max_val=height[i]
                max_idx=i
        res=0
        max_left=0
        for i in range(len(height)-1):
            left = height[i]
            if left<max_left:
                continue
            max_left=max(max_left,left)
            right_idx=max_rights[i]
            while right_idx!=-1:
                res=max((right_idx-i)*min(left,height[right_idx]),res)
                right_idx=max_rights[right_idx]
        return res

if __name__ == '__main__':
    sol=Solution()
    height=[1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))