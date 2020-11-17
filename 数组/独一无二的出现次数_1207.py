from typing import *
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic1 = defaultdict(int)
        for val in arr:
            dic1[val] += 1
        set1 = set()
        print(len(dic1))
        for key in dic1:
            if dic1[key] in set1:
                return False
            set1.add(dic1[key])
        return True

if __name__ == '__main__':
    sol=Solution()
    arr = [1, 2, 2, 1, 1, 3]
    print(sol.uniqueOccurrences(arr))