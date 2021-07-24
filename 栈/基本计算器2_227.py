from typing import *


class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []
        i = 0
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                op_stack.append(s[i])
            elif s[i] == '*' or s[i] == '/':
                op_stack.append(s[i])
            elif s[i] in '0123456789':
                num = int(s[i])
                i += 1
                while i < len(s) and s[i] in '1234567890':
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
                num_stack.append(num)
                if op_stack and op_stack[-1] in '*/':
                    val1 = num_stack.pop()
                    val2 = num_stack.pop()
                    num_stack.append(self.ope(val2, val1, op_stack[-1]))
                    op_stack.pop()
            i += 1
        if len(op_stack)==0:
            return num_stack[0]
        res = self.ope(num_stack[0], num_stack[1], op_stack[0])
        for i in range(1, len(op_stack)):
            res = self.ope(res, num_stack[i + 1], op_stack[i])
        return res

    def ope(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        return a // b


if __name__ == '__main__':
    sol = Solution()
    s = '33/3*4'
    print(sol.calculate(s))
