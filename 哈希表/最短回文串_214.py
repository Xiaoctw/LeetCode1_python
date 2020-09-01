from typing import *


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        base, mod = 113, 10 ** 7 + 9
        val1, val2 = 0, 0
        mul = 1
        best = -1
        for idx in range(len(s)):
            # ord函数返回该字符对应的ascii数值
            val1 = (val1 * base % mod + ord(s[idx])) % mod
            val2 = (val2 + ord(s[idx]) * mul % mod) % mod
            mul = mul * base % mod
            if val2 == val1:
                best = idx
        if best != -1:
            s1 = s[best + 1:]
            return s1[::-1] + s
        return s[::-1] + s


if __name__ == '__main__':
    sol = Solution()
    s = 'abcd'
    print(sol.shortestPalindrome(s))
