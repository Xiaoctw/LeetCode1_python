# Definition for a binary tree node.
from typing import *
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    转化成字符串匹配方法
    利用kmp算法
    '''
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        list1,list2=[],[]
        self.dfs(s,list1)
        self.dfs(t,list2)
        return self.kmp(list1,list2)
    def dfs(self,node,list1:List):
        if node is None:
            return
        list1.append(node.val)
        if node.left:
            self.dfs(node.left,list1)
        else:
            list1.append(-sys.maxsize)
        if node.right:
            self.dfs(node.right,list1)
        else:
            list1.append(sys.maxsize)

    def kmp(self,list1:List,list2:List):
        len1,len2=len(list1),len(list2)
        fail=[-1]*len2
        j=-1
        for i in range(1,len2):
            while j!=-1 and list1[i]!=list1[j+1]:
                j=fail[j]
            if list2[i]==list2[j+1]:
                j+=1
            fail[i]=j
        j=-1
        for i in range(len1):
            while j!=-1 and list1[i]!=list2[j+1]:
                j=fail[j]
            if list1[i]==list2[j+1]:
                j+=1
            if j==len2-1:
                return TreeNode
        return False
