from typing import *


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        list1 = [a, b, c]
        list1.sort()
        a1, b1, c1 = list1[0], list1[1], list1[2]
        max_ans = c1 - a1 - 2
        if c1 - b1 == 1 and b1 - a1 == 1:
            min_ans = 0
        elif c1 - b1 <= 2 or b1 - a1 <= 2:
            min_ans = 1
        else:
            min_ans = 2
        return [min_ans, max_ans]
