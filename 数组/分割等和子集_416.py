from typing import *
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tem_set=set()
        tem_sum=0
        for val in nums:
            tem_sum+=val
            set1=set()
            set1.add(val)
            for x in tem_set:
                set1.add(x+val)
                set1.add(x)
            tem_set=set1
        if tem_sum%2!=0:
            return False
        return tem_sum//2 in tem_set


if __name__ == '__main__':
    sol=Solution()
    nums=[1,2,3,5]
    print(sol.canPartition(nums))

