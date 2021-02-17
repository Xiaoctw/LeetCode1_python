import math


class Solution:
    def keyboard(self, k: int, n: int) -> int:
        mod = int(1e9 + 7)
        tem = 0
        i = 0
        while n - (k + 1) * i >= 0:
            if i % 2 == 0:
                val = int(self.C(26, i) * self.F(26, n - (k + 1) * i)) % mod
            else:
                val = -(int(self.C(26, i) * self.F(26, n - (k + 1) * i)) % mod)
            i += 1
            tem += val
        while n > 0:
            tem = (tem * n) % mod
            n -= 1
        return tem

    def C(self, n, i):
        if i == 0:
            return 1
        res = 1
        for j in range(1, i + 1):
            res = res * (n / j)
            n -= 1
        return res

    def F(self, n, i):
        return self.C(n + i - 1, i)


if __name__ == '__main__':
    sol = Solution()
    k = 1
    n = 2
    print(sol.keyboard(k=k, n=n))
# print(sol.C(26, 3))
