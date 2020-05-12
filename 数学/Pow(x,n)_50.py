class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        ### 这样可以减少循环次数
        cnt, sum = 1, x
        while cnt * 2 <= n:
            sum = sum * sum
            cnt = 2 * cnt
        return self.myPow(x, n - cnt) * sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.myPow(4, 6))
