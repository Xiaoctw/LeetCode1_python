from typing import *
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        arr = []
        for _, val in envelopes:
            idx = bisect.bisect_left(arr, val)
            if idx == len(arr):
                arr.append(val)
            else:
                arr[idx] = val
        return len(arr)


if __name__ == '__main__':
    sol = Solution()
    envelopes = [[1, 1], [1, 1], [1, 1]]
    print(sol.maxEnvelopes(envelopes))
