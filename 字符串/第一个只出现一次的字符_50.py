class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic={}
        for c in s:
            dic[c]=not c in dic
        for k,v in dic.items():
            if v:
                return k
        return ' '

if __name__ == '__main__':
    dic1={}
    dic1['b']=1
    dic1['a']=2
    dic1['c']=3
    for key in dic1:
        #输出是有序的，按照添加的顺序
        print('{}:{}'.format(key,dic1[key]))