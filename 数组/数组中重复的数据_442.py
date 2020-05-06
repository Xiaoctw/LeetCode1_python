from typing import *
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr=[0]*(len(nums)+1)
        for num in nums:
            arr[num]+=1
        res=[]
        for i in range(1,len(arr)):
            if arr[i]>1:
                res.append(i)
        return res

if __name__ == '__main__':
    sol=Solution()
    nums=[4,3,2,7,8,2,3,1]
    print(sol.findDuplicates(nums))