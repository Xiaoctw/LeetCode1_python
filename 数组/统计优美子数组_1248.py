from typing import *
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt=[0]*(len(nums)+1)
        odd_num=0
        j=0
        cnt[0]=1
        res=0
        while j<len(nums):
            if nums[j]%2==1:
                odd_num+=1
            if odd_num>=k:
                res+=cnt[odd_num-k]
            cnt[odd_num]+=1
            j+=1
        return res

if __name__ == '__main__':
    sol=Solution()
    nums=[2,2,2,1,2,2,1,2,2,2]
    print(sol.numberOfSubarrays(nums,2))
