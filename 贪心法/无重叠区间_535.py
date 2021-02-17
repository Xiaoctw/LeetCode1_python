from typing import *


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort()
        cnt = 1
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= right:
                # 可能最右端往前挪了挪
                right = intervals[i][1]
            if intervals[i][0] >= right:
                cnt += 1
                right = intervals[i][1]
        return len(intervals) - cnt


if __name__ == '__main__':
    sol = Solution()
    nums = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
    print(sol.eraseOverlapIntervals(nums))
