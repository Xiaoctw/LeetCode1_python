class Solution:
    def translateNum(self, num: int) -> int:
        """
        不要首先考虑搜索，动态规划更好用
        :param num:
        :return:
        """
        p, q = 1, 1
        num_str = str(num)
        for i in range(1, len(num_str)):
            p, q = q, p + q if 10 <= int(num_str[i - 1:i + 1]) <= 25 else q
        return q


if __name__ == '__main__':
    sol = Solution()
    num = 25
    print(sol.translateNum(num))
