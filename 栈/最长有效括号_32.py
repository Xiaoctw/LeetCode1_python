class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        max_len=0
        stack.append((-1,')'))#添加一个哨兵元素，保证栈不为空
        for i,c in enumerate(s):
            if c=='(':
                stack.append((i,'('))
            else:
                if stack[-1][1]=='(':#匹配到了，观察是否能够达到最大长度
                    stack.pop()
                    max_len=max(max_len,i-stack[-1][0])
                else:
                    stack.append((i,c))
        return max_len




if __name__ == '__main__':
    sol=Solution()
    s=')()())'
    print(sol.longestValidParentheses(s))

