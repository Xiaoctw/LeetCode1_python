from typing import *
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _len=len(nums)
        if _len<=0:
            return False
        bnd=_len-1
        for i in range(_len-2,-1,-1):
            if nums[i]+i>=bnd:
                bnd=min(bnd,i)
        return bnd==0




if __name__ == '__main__':
    l=[3,2,1,0,4]
    l1=[2,3,1,1,4]
    print(Solution().canJump(l))
    print(Solution().canJump(l1))
    print(Solution().canJump([1]))


