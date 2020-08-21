from typing import *
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return self.intersect(nums2,nums1)
        dic1=defaultdict(int)
        for val in nums1:
            dic1[val]+=1
        res=[]
        for val in nums2:
            if dic1[val]>0:
                res.append(val)
                dic1[val]-=1
        return res

if __name__ == '__main__':
    sol=Solution()
    nums1=[1,2,2,1]
    num2=[2,2]
    print(sol.intersect(nums1,num2))
