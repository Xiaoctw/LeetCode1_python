from typing import *


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i][0], coordinates[i][1]
            if (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) != 0:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(sol.checkStraightLine(coordinates))
