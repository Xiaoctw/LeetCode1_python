from typing import *


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        lo, hi = 0, len(s)
        ans = lo
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if self.judge(s, t, mid, cost=maxCost):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    def judge(self, s, t, l, cost):
        tem_sum = 0
        flag = False
        for i in range(l):
            tem_sum += abs(ord(s[i]) - ord(t[i]))
        if tem_sum <= cost:
            flag = True
        for i in range(l, len(s)):
            tem_sum -= abs(ord(s[i - l]) - ord(t[i - l]))
            tem_sum += abs(ord(s[i]) - ord(t[i]))
            if tem_sum <= cost:
                flag = True
        return flag


if __name__ == '__main__':
    sol = Solution()
    s = "abcd"
    t = "acde"
    cost = 0
    print(sol.equalSubstring(s, t, cost))
