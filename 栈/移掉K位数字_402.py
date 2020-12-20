class Solution:
    """
    要想使得整个数字最小，必须让前面的数字尽量小
    从左往右寻找，每个数字和它左侧数字比较，如果该数字更小，那么去掉前一个数字。
    去除k次。
    """
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain_num = len(num) - k
        for c in num:
            #栈最多弹出k次
            while k and stack and ord(stack[-1]) > ord(c):
                stack.pop()
                k -= 1
            stack.append(c)
        return ''.join(stack[:remain_num]).lstrip('0') or '0'


if __name__ == '__main__':
    sol = Solution()
    num = '0200'
    print(sol.removeKdigits(num, 1))
