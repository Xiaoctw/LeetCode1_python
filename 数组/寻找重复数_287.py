from typing import *
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        数组只读，不可修改
        :param nums:
        :return:
        '''
        beg,end=1,len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            cnt=0
            for val in nums:
                if val<=mid:
                    cnt+=1
            if cnt>mid:
                end=mid-1
            else:
                beg=mid+1
        return beg

if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,0,4,4,4,4,4,4,4]
    sol=Solution()
    print(sol.findDuplicate(arr))
