from typing import *


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        list1 = [0]
        ans = []
        for val in arr:
            list1.append(list1[-1] ^ val)
        for query in queries:
            val1 = list1[query[0]]
            val2 = list1[query[1] + 1]
            ans.append(val1 ^ val2)
        return ans


if __name__ == '__main__':
    arr = [4, 8, 2, 10]
    queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
    sol = Solution()
    print(sol.xorQueries(arr, queries))
