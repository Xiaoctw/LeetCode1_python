import time
import itertools
from numpy import *
import matplotlib.pyplot as plt

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        count=0
        pre=-1
        time1=0
        time2=0
        def find_lists(lists,list1,nums,target,index):
            """
            :param lists:
            :param list1:
            :param nums:
            :param target:
            :param index:
            :type lists List[List[int]]
            :return:
            """
            nonlocal pre
            nonlocal time1
            nonlocal time2
            if target<0:
                return
            if  target==0:
                temp=list1[:]
                lists.append(temp)
                if pre!=temp[0]:
                    time2=time.time()
                    pre=temp[0]
                    print(list1)
                    print("执行当前数字消耗时间{}".format(time2-time1))
                    time1=time.time()
            for i in range(index,len(nums)):
                temp=list1[:]
                temp.append(nums[i])
                find_lists(lists,temp,nums,target-nums[i],i)
            return
        time1=time.time()
        lists=[]
        sorted(candidates)
        find_lists(lists,[],candidates,target,0)
        return lists

if __name__ == '__main__':
    candidates=[2,3,6,7]
    candidates1=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    candidates1=list(set(candidates1))
    time_start=time.time()
    num=50
    res=Solution().combinationSum(candidates1,num)
    time_end=time.time()
 #   print(res)
    print("{}个数耗时{}".format(num,time_end-time_start))
