from typing import *
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        注意两次是关键信息，数组中值得大小也是关键信息，按照索引和取负值
        可以找到答案
        :param nums:
        :return:
        '''
        res=[]
        for val in nums:
            idx=abs(val)-1
            if nums[idx]<0:
                res.append(idx+1)
            nums[idx]=-nums[idx]
        return res

if __name__ == '__main__':
    sol=Solution()
    nums=[4,3,2,7,8,2,3,1]
    print(sol.findDuplicates(nums))