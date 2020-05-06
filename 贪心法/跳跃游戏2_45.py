from typing  import *
class Solution:
    '''
    必须是线性复杂度才能满足需求
    每次找到可以跳到位置的范围
    '''
    def jump(self, nums: List[int]) -> int:
        beg,end=0,0
        ans=0
        while end<len(nums)-1:
            max_pos=-1
            #更新下一跳可以到达的位置
            for i in range(beg,end+1):
                max_pos=max(max_pos,i+nums[i])
            ans+=1
            beg=end+1
            end=max_pos
        return ans



if __name__ == '__main__':
    sol=Solution()
    nums=[2,3,1,1,4]
    print(sol.jump(nums))