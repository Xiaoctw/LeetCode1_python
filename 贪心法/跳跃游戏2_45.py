from typing  import *
class Solution:
    '''
    必须是线性复杂度才能满足需求
    '''
    def jump(self, nums: List[int]) -> int:
        _len=len(nums)
        ans=0
        end=0 #记录当前跳数能够到达的最远位置
        max_pos=0
        for i in range(_len-1):
            max_pos=max(max_pos,nums[i]+i)
            if max_pos>=_len-1:
                return ans+1
            if i==end:
                end=max_pos
                ans+=1
        return ans


if __name__ == '__main__':
    sol=Solution()
    nums=[2,3,1,1,4]
    print(sol.jump(nums))