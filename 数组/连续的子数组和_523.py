from typing import *
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic1={}
        dic1[0]=-1# 哨兵元素
        sum=0
        for i,val in enumerate(nums):
            sum+=val
            if k!=0:
                k1=sum%k
            else:
                k1=sum
            if k1 in dic1:
                if i-dic1[k1]>1:
                    return True
            else:
                dic1[k1]=i
        return False

if __name__ == '__main__':
    sol=Solution()
    nums=[0,1,0]
    print(sol.checkSubarraySum(nums,0))