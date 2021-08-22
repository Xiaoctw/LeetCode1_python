from typing import *

class Solution:
    def __init__(self):
        self.array=[]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        assert k<=len(nums)
        self.array=nums[:k]
        for i in range(k//2+1,-1,-1):
            self.modify(i,k)
        for i in range(k,len(nums)):
            if nums[i]<self.array[0]:
                continue
            self.array[0]=nums[i]
            self.modify(0,k)
        return self.array[0]


    def modify(self,idx,k):
        left=2*idx+1
        right=2*idx+2
        min_idx=idx
        if left<k and self.array[min_idx]>self.array[left]:
            min_idx=left
        if right<k and self.array[min_idx]>self.array[right]:
            min_idx=right
        if min_idx!=idx:
            self.array[min_idx],self.array[idx]=self.array[idx],self.array[min_idx]
            self.modify(min_idx,k)


if __name__ == '__main__':
    arr=[3,2,3,1,2,4,5,5,6]
    sol=Solution()
    print(sol.findKthLargest(arr,4))
