from typing import *
from collections import defaultdict
class Node:
    def __init__(self,value):
        self.value=value
        self.adj1=None
        self.adj2=None


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic=defaultdict(Node)
        cnt=defaultdict(int)
        for adj in adjacentPairs:
            node1,node2=adj[0],adj[1]
            cnt[node1]+=1
            cnt[node2]+=1
            if node1 not in dic:
                dic[node1]=Node(node1)
            if node2 not in dic:
                dic[node2]=Node(node2)
            if dic[node1].adj1 is None:
                dic[node1].adj1=dic[node2]
            else:
                dic[node1].adj2=dic[node2]
            if dic[node2].adj1 is None:
                dic[node2].adj1=dic[node1]
            else:
                dic[node2].adj2=dic[node1]

        beg=None
        for node in cnt:
            if cnt[node]==1:
                beg=node
                break
        return self.search(dic,beg)

    def search(self,dic,beg):
        res=[]
        set1=set()
        tem=dic[beg]
        while True:
            res.append(tem.value)
            set1.add(tem.value)
            if tem.adj2 is not None and tem.adj2.value not in set1:
                tem=tem.adj2
            elif tem.adj1 is not None and tem.adj1.value not in set1:
                tem=tem.adj1
            else:
                break
        return res

if __name__ == '__main__':
    sol=Solution()
    ajd=[[2,1],[3,4],[3,2]]
    print(sol.restoreArray(ajd))





