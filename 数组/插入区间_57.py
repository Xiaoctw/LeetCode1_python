from typing import *


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res=[]
        i=0
        while i<len(intervals):
            left,right=intervals[i][0],intervals[i][1]
            while i+1<len(intervals) and intervals[i+1][0]<=right:
                i+=1
                right=max(right,intervals[i][1])
            res.append([left,right])
            i+=1
        return res



if __name__ == '__main__':
    sol = Solution()
    intervals = [[1, 5]]
    newInterval = [4, 6]
    print(sol.insert(intervals, newInterval))
