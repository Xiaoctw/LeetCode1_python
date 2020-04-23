class Solution:
    '''
    巧妙用栈解决问题
    '''
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        stack.append(-1)
        max_len=0
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    #更新最靠后的位置
                    stack.append(i)
                else:
                    max_len=max(max_len,i-stack[-1])
        return max_len