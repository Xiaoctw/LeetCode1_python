from typing import *
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        cnt=1
        i=1
        bound=intervals[0][1]
        while i<len(intervals):
            if intervals[i][1]<=bound:
                i+=1
            else:
                cnt+=1
                bound=intervals[i][1]
                i+=1
        return cnt

if __name__ == '__main__':
    sol=Solution()
    intervals = [[1, 4], [3, 6], [2, 8]]
    arr1=[[1,6],[1,8],[2,5],[2,6]]
    print(sol.removeCoveredIntervals(arr1))
