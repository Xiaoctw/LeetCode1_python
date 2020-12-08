class Solution:
    def countPrimes(self, n: int) -> int:
        # 埃氏筛
        isPrime = [True] * (n)
        cnt = 0
        for i in range(2, n):
            if isPrime[i]:
                cnt += 1
                k = 2
                while k * i < n:
                    isPrime[k * i] = False
                    k += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()
    num = 10
    print(sol.countPrimes(num))
