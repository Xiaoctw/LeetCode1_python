from typing import *
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        all, res = [], []
        for building in buildings:
            all.append((building[0], -building[2]))
            all.append((building[1], building[2]))
        all.sort()
        heights = [0]
        last = [0, 0]
        for p in all:
            if p[1] < 0:
                heapq.heappush(heights, p[1])
            else:
                heights.remove(-p[1])
                heapq.heapify(heights)
            max_height = -heights[0]
            if last[1] != max_height:
                last[0] = p[0]
                last[1] = max_height
                res.append(last[:])
        return res

if __name__ == '__main__':
    buildings=[[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]
    sol=Solution()
    print(sol.getSkyline(buildings))
