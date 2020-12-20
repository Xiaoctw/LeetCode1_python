from typing import *
from collections import Counter


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dic1 = Counter(senate)
        num_R, num_D = dic1['R'], dic1['D']
        if num_R == 0:
            return 'Dire'
        if num_D == 0:
            return 'Radiant'
        forbid_R, forbid_D = 0, 0
        len_S = num_R + num_D
        forbid_set = set()
        i = 0
        while True:
            if i % len_S in forbid_set:
                i += 1
                continue
            j = i + 1
            while j % len_S in forbid_set or (senate[j % len_S] == senate[i % len_S]):
                j += 1
            forbid_set.add(j % len_S)
            if senate[j % len_S] == 'R':
                forbid_R += 1
            else:
                forbid_D += 1
            if forbid_R == num_R:
                return 'Dire'
            if forbid_D == num_D:
                return 'Radiant'
            i += 1


if __name__ == '__main__':
    sol = Solution()
    s = "RRDRDDRDRRDDDDDRDRDR"
    print(sol.predictPartyVictory(s))
