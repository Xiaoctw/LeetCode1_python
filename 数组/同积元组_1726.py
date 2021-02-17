from typing import *
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnts=defaultdict(lambda :0)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                cnts[nums[i]*nums[j]]+=1
        res=0
        for i in cnts:
            if cnts[i]>1:
                res+=cnts[i]*(cnts[i]-1)*4
        return res

if __name__ == '__main__':
    sol=Solution()
    nums =[1,2,4,5,10]
    print(sol.tupleSameProduct(nums))

