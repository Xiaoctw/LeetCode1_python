from typing import *
import bisect


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        dp = [0] * len(s)
        for val in g:
            i = bisect.bisect_left(s, val)
            while i < len(s) and (s[i] < val or dp[i]):
                i += 1
            if i < len(s):
                dp[i] = 1
        return sum(dp)


if __name__ == '__main__':
    g = [1, 2]
    s = [1, 2, 3]
    sol = Solution()
    print(sol.findContentChildren(g, s))
