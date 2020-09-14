class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        方法为每次选择较多的字符写入，当且仅当前两个字符
        相等时，选择另外一种字符
        """
        ans = []
        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B
            if writeA:
                ans.append('a')
                A -= 1
            else:
                B -= 1
                ans.append('b')
        return "".join(ans)
