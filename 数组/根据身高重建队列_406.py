from typing import *
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #将所有人到倒序排列
        people.sort(key=lambda x:(-x[0], x[1]))
        ans=[]
        for person in people:
            ans.insert(person[1],person)
        return ans

if __name__ == '__main__':
    people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    sol=Solution()
    print(sol.reconstructQueue(people))