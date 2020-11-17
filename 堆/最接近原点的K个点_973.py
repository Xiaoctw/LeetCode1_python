from typing import *
import heapq


class Solution:
    """
    通过该题学会使用heapq
    """

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.helper1(points, K, 0, len(points) - 1)
        return points[:K]

    def helper1(self, points, K, lo, hi):
        if lo >= hi:
            return
        idx = self.helper2(points, lo, hi)
        if idx - lo + 1 > K:
            # 这里范围必须逐渐缩小
            self.helper1(points, K, lo, idx - 1)
        else:
            self.helper1(points, K - (idx - lo) - 1, idx + 1, hi)

    def helper2(self, points, lo, hi):
        i = lo - 1
        val = self.dist(points[hi])
        for j in range(lo, hi):
            if self.dist(points[j]) < val:
                i += 1
                points[i], points[j] = points[j], points[i]
        points[i + 1], points[hi] = points[hi], points[i + 1]
        return i + 1

    def dist(self, point):
        return point[0] ** 2 + point[1] ** 2


if __name__ == '__main__':
    points = [[-95, 76], [17, 7], [-55, -58], [53, 20], [-69, -8], [-57, 87], [-2, -42], [-10, -87], [-36, -57],
              [97, -39],
              [97, 49]]
    K = 5
    sol = Solution()
    print(sol.kClosest(points, K))
