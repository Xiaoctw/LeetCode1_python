from typing import *


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        回文串从首到尾和从尾部到首部字符串同，字符串表示的数字同样也相等。
        子串问题的一个经典的解决方法为将其转化为一个数字，这里也可以采用同样的方法。
        :param s:
        :return:
        '''
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
