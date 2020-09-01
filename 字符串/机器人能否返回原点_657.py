from typing import *


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic1 = {
            'L': (-1, 0),
            'R': (1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }
        x,y = 0, 0
        for c in moves:
            x, y = x + dic1[c][0], y + dic1[c][1]
        return x == 0 and y == 0


if __name__ == '__main__':
    sol=Solution()
    s='UD'
    print(sol.judgeCircle(s))
