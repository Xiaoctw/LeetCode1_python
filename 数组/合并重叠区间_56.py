from typing import *
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        intervals.sort(key=lambda x:x[0])
        beg=intervals[0][0]
        end=intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=end:
                end=max(intervals[i][1],end)
            else:
                res.append([beg,end])
                beg=intervals[i][0]
                end=intervals[i][1]
        res.append([beg,end])
        return res


if __name__ == '__main__':
    sol=Solution()
    list1=[[1,4],[2,3]]
    print(sol.merge(list1))
