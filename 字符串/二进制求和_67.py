from typing import *


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        add = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 and j >= 0:
            val = (int(a[i]) + int(b[j]) + add) % 2
            add = (int(a[i]) + int(b[j]) + add) // 2
            res.append(str(val))
            i -= 1
            j -= 1
        while i >= 0:
            val = (int(a[i]) + add) % 2
            add = (int(a[i]) + add) // 2
            res.append(str(val))
            i -= 1
        while j >= 0:
            val = (int(b[j]) + add) % 2
            add = (int(b[j]) + add) // 2
            res.append(str(val))
            j -= 1
        if add:
            res.append(str(add))
        return ''.join(res[::-1])


if __name__ == '__main__':
    sol = Solution()
    a = '1010'
    b = '1011'
    print(sol.addBinary(a, b))
