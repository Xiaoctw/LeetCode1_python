from typing import List


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        return self.merge(nums,0,len(nums)-1)

    def merge(self,nums,beg,end):
        if beg>=end:
            return 0
        mid=(beg+end)//2
        cnt1=self.merge(nums,beg,mid)
        cnt2=self.merge(nums,mid+1,end)
        beg1, end1, beg2, end2 = beg, mid, mid + 1, end
        cnt=self.partition(nums,beg1,end1,beg2,end2)
        return cnt+cnt1+cnt2

    def partition(self,nums,beg1,end1,beg2,end2):
        i1, i2 = beg1, beg2
        cnt = 0
        while i1 <= end1:
            while i2 <= end2 and nums[i2] < nums[i1]:
                i2 += 1
            cnt += (i2 - beg2)
            i1 += 1
        tem = [0] * (end2 - beg1 + 1)
        i = 0
        i1, i2 = beg1, beg2
        while i1 <= end1 and i2 <= end2:
            if nums[i1] < nums[i2]:
                tem[i] = nums[i1]
                i1 += 1
            else:
                tem[i] = nums[i2]
                i2 += 1
            i += 1
        while i1 <= end1:
            tem[i] = nums[i1]
            i1 += 1
            i += 1
        while i2 <= end2:
            tem[i] = nums[i2]
            i2 += 1
            i += 1
        for i in range(end2 - beg1 + 1):
            nums[i + beg1] = tem[i]
        return cnt


if __name__ == '__main__':
    sol=Solution()
    nums=[10,9,8,7,5,6,4,1,2,3,4,5,6]
    print(sol.reversePairs(nums))
    print(nums)