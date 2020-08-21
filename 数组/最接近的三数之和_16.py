from typing import *
import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        tar_val=-sys.maxsize
        for i in range(len(nums)):
            val1=nums[i]
            j,k=i+1,len(nums)-1
            while j<k:
                sum1=val1+nums[k]+nums[j]
                if abs(sum1-target)<abs(tar_val-target):
                    tar_val=sum1
                if sum1>target:
                    k-=1
                else:
                    j+=1
        return tar_val

if __name__ == '__main__':
    sol=Solution()
    nums=[-1,2,1,-4]
    target=1
    print(sol.threeSumClosest(nums,target))

