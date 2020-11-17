class Solution:
    def maxDepth(self, s: str) -> int:
        """
        本题使用到了栈，但其实是简单题，没有特别复杂的技巧，
        记录栈的深度即可
        :param s:
        :return:
        """
        stack = []
        max_size = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.pop()
            max_size = max(max_size, len(stack))
        return max_size


if __name__ == '__main__':
    sol = Solution()
    s1 = '(1+(2*3)+((8)/4))+1'
    print(sol.maxDepth(s1))
