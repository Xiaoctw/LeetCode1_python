from typing import *
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        cnt = 0
        for point in points:
            if point[0] == location[0] and point[1] == location[1]:
                cnt += 1
                continue
            angles.append(math.atan2(location[1] - point[1], location[0] - point[0]))
        angles.sort()
        angles.extend([x + math.pi * 2 for x in angles])
        angle = angle / 180 * math.pi
        l, r = 0, 0
        ret = 0
        while r < len(angles):
            while angles[r] - angles[l] > angle:
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret + cnt

if __name__ == '__main__':
    sol=Solution()
    points = [[2, 1], [2, 2], [3, 3]]
    angle = 90
    location = [1, 1]
    print(sol.visiblePoints(points,angle,location))
