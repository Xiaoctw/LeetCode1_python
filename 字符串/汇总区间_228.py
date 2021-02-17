from typing import *
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)<1:
            return []
        first=0
        res=[]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if first!=i-1:
                    res.append(str(nums[first])+'->'+str(nums[i-1]))
                else:
                    res.append(str(nums[first]))
                first=i
        if first==len(nums)-1:
            res.append(str(nums[first]))
        else:
            res.append(str(nums[first]) + '->' + str(nums[len(nums) - 1]))
        return res

if __name__ == '__main__':
    nums = [0]
    sol=Solution()
    print(sol.summaryRanges(nums))


