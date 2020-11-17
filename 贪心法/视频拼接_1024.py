from typing import *


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        if clips[0][0]>0:
            return -1
        last = clips[0][1]
        cnt = 1
        j = 0
        while j < len(clips):
            if last >= T:
                return cnt
            max_last = clips[j][1]
            while j < len(clips) and clips[j][0] <= last:
                max_last = max(max_last, clips[j][1])
                j += 1
            if j<len(clips) and clips[j][0]>max_last:
                return -1
            if max_last <= last < T:
                return -1
            last = max_last
            cnt += 1
        if last>=T:
            return cnt
        return -1

if __name__ == '__main__':
    sol = Solution()
    clips=[[8, 10], [17, 39], [18, 19], [8, 16], [13, 35], [33, 39], [11, 19], [18, 35]]
    T=20

    print(sol.videoStitching(clips, T))
