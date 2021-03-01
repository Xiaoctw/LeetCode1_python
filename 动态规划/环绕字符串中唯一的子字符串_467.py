from typing import *


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        dp = [0] * 26
        cnt = 1
        dp[ord(p[0])-ord('a')]=1
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i - 1]) == 1 or p[i] == 'a' and p[i - 1] == 'z':
                cnt += 1
            else:
                cnt = 1
            dp[ord(p[i]) - ord('a')] = max(dp[ord(p[i]) - ord('a')], cnt)
        return sum(dp)

if __name__ == '__main__':
    sol=Solution()
    s='zabc'
    print(sol.findSubstringInWraproundString(s))
