# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack=[]
        i=0
        while i<len(S):
            cnt = 0
            while i < len(S) and S[i] == '-':
                cnt += 1
                i += 1
            value=0
            while i<len(S) and  S[i].isdigit():
                value=value*10+int(S[i])
                i+=1
            if not stack:
                stack.append(TreeNode(value))
            else:
                node1=TreeNode(value)
                if cnt==len(stack):
                    stack[-1].left=node1
                else:
                    stack=stack[:cnt]
                    stack[-1].right=node1
                stack.append(node1)
        return stack[0]

if __name__ == '__main__':
    sol=Solution()
    s1='1-2--3--4-5--6--7'
    print(sol.recoverFromPreorder(s1))
