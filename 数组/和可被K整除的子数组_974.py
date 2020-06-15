from typing import *
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dic1={}
        '''
        键为整除K余值为多少
        '''
        sum = 0
        dic1[sum%K]=1
        res=0
        for val in A:
            sum+=val
            if sum%K in dic1:
                res+=dic1[sum%K]
                dic1[sum%K]+=1
            else:
                dic1[sum%K]=1
        return res



if __name__ == '__main__':
    sol=Solution()
    nums=[4,5,0,-2,-3,1]
    print(sol.subarraysDivByK(nums,5))



