class Solution:
    """
    康拓展开
    """

    def getPermutation(self, n: int, k: int) -> str:
        chs = [str(i) for i in range(1, 10)]
        factor = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        k -= 1
        ans = ''
        for j in range(n - 1, -1, -1):
            # divmod返回除数和余数
            j, k = divmod(k, factor[j])
            ans += chs.pop(j)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 4
    k = 9
    print(sol.getPermutation(n, k))
