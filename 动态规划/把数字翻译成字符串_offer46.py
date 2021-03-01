class Solution:
    def translateNum(self, num: int) -> int:
        """
        不要首先考虑搜索，动态规划更好用
        :param num:
        :return:
        """
        if num <10:
            return 1
        list1 = []
        while num:
            list1.append(num % 10)
            num = num // 10
        list1 = list1[::-1]
        val1 = 1
        if 10 <= list1[0] * 10 + list1[1] <= 25:
            val2 = 2
        else:
            val2 = 1
        val3 = val2
        for i in range(2, len(list1)):
            if 10 <= list1[i - 1] * 10 + list1[i] <= 25:
                val3 = val1 + val2
            else:
                val3 = val2
            val1 = val2
            val2 = val3
        return val3


if __name__ == '__main__':
    sol = Solution()
    num = 12258
    print(sol.translateNum(num))
