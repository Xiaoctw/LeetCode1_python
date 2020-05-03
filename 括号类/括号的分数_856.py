class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == '(':
                # 新创建一层，该层分数暂时是0
                stack.append(0)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                val = val2
                if val1 == 0:
                    val += 1
                else:
                    val += 2 * val1
                stack.append(val)
        return stack.pop()


if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreOfParentheses('()()()'))
