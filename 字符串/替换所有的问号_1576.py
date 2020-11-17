import random


class Solution:
    def modifyString(self, s: str) -> str:
        b = list(s)
        list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        # 这里是排除b的长度为1的情况。只有一个？的情况
        for i in range(len(b)):
            if b[i] == '?':
                b[i] = random.choice(list2)
                while (i > 0 and b[i] == b[i - 1]) or (i < len(b) - 1 and b[i] == b[i + 1]):
                    b[i] = random.choice(list2)
        return ''.join(b)


# 这个是入口函数，可直接执行，以后在ide里调试
# 直接打一个main就都出来了
if __name__ == '__main__':
    sol = Solution()  # 定义一个变量
    print(sol.modifyString('?'))
