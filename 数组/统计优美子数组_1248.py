from typing import *
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt=defaultdict(int)
        cnt[0]=1
        odd_num,res=0,0
        for i,val in enumerate(nums):
            if val%2==1:
                odd_num+=1
            cnt[odd_num]+=1
            if odd_num>=k:
                res+=cnt[odd_num-k]
        return res

if __name__ == '__main__':
    sol=Solution()
    nums=[2,2,2,1,2,2,1,2,2,2]
    print(sol.numberOfSubarrays(nums,2))
