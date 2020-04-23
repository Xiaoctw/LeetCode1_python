from typing import *
class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        从前到后贪心算法
        :param intervals:
        :return:
        '''
        if len(intervals)==0:
            return 0
        intervals.sort()
        pre=0
        cnt=0
        for i in range(1,len(intervals)):
            if intervals[i][0]>=intervals[pre][1]:
                pre=i
            elif intervals[i][1]<=intervals[pre][1]:
                pre=i
                cnt+=1
            else:
                cnt+=1
        return cnt

if __name__ == '__main__':
    sol=Solution()
    arr=[ [1,2],[2,3] ]
    print(sol.eraseOverlapIntervals(arr))