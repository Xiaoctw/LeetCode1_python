from typing import *
import bisect
class Solution:
    '''
    双重二分搜索
    '''
    def findBestValue(self, arr: List[int], target: int) -> int:
        sum_arr=[]
        arr.sort()
        tem_sum=0
       # sum_arr.append(0)
        for val in arr:
            tem_sum+=val
            sum_arr.append(tem_sum)
        l,r=0,max(arr)
        #这里搜索的是刚好小于等于target的value值
        ans=-1
        while l<=r:
            mid=(l+r)//2
            #返回的是最后一个小于等于mid的位置
            it=bisect.bisect_left(arr,mid)
            if it==0:
                cur_val=(len(arr)-it)*mid
            else:
                cur_val=sum_arr[it-1]+(len(arr)-it)*mid
            if cur_val<=target:
                ans=mid #这里做一个记录，循环结束后便于找到结果
                l=mid+1
            else:
                r=mid-1
        def check(x):
            return sum(x if num>=x else num for num in arr)
        return ans if abs(check(ans)-target)<=abs(check(ans+1)-target) else ans+1



if __name__ == '__main__':
    sol=Solution()
    arr = [1,3,4,4,4]
    print(bisect.bisect_left(arr,0))
    target=10
    print(sol.findBestValue(arr,target))


