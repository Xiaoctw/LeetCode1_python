from typing import *


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        res = []
        res.append(pairs[0])
        i = 1
        right = pairs[0][1]
        while i < len(pairs):
            while i < len(pairs) and pairs[i][0] <= right:
                i += 1
            if i == len(pairs):
                break
            res.append(pairs[i])
            right = pairs[i][1]
        #  print(res)
        return len(res)


if __name__ == '__main__':
    sol = Solution()
    list1 = [[1, 2], [2, 3], [3, 4]]
    print(sol.findLongestChain(list1))
