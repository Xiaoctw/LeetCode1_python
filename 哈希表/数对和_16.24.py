from typing import *
from collections import defaultdict
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        dic=defaultdict(int)
        res=[]
        for val in nums:
            if dic[target-val]>0:
                res.append([target-val,val])
                dic[target-val]-=1
            else:
                dic[val]+=1
        return res

if __name__ == '__main__':
    sol=Solution()
    num=[2,1,8,6,5,7,-1,3,5,5]
    target=7
    print(sol.pairSums(num,target))
