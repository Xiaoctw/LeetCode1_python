from typing import *
import sys
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pre=sys.maxsize
        res=[]
        for i in range(len(nums)-2):
            val1=nums[i]
            if val1>0:
                break
            if pre==val1:#去重
                continue
            pre=val1
            j=i+1;k=len(nums)-1
            while j<k:
                if val1+nums[j]+nums[k]==0:
                    res.append([val1,nums[j],nums[k]])
                    #去重
                    while j+1<len(nums) and nums[j+1]==nums[j]:
                        j+=1
                    #去重
                    while k-1>=0 and nums[k-1]==nums[k]:
                        k-=1
                    j+=1
                    k-=1
                elif val1+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return res

if __name__ == '__main__':
    sol=Solution()
    nums=[-1,0,1,2,-1,-4]
    list1=sol.threeSum(nums)
    print(list1)
