class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        dic1={}
        for c in 'abcdefghiklmjnopqrstuvwxyz':
            dic1[c]=(ord(c)-97)//5,(ord(c)-97)%5
        tem=0,0
        res=[]
        for c in target:
            if c=='z':
                tem1 = dic1[c]
                x, y = tem1[0] - tem[0], tem1[1] - tem[1]
                if y > 0:
                    res.extend(['R' for _ in range(y)])
                else:
                    res.extend(['L' for _ in range(-y)])
                if x > 0:
                    res.extend(['D' for _ in range(x)])
                elif x < 0:
                    res.extend(['U' for _ in range(-x)])
                res.append('!')
                tem = tem1
                continue
            tem1=dic1[c]
            x,y=tem1[0]-tem[0],tem1[1]-tem[1]
            if x>0:
                res.extend(['D' for _ in range(x)])
            elif x<0:
                res.extend(['U' for _ in range(-x)])
            if y>0:
                res.extend(['R' for _ in range(y)])
            else:
                res.extend(['L' for _ in range(-y)])
            res.append('!')
            tem=tem1
        return ''.join(res)

if __name__ == '__main__':
    sol=Solution()
    print(sol.alphabetBoardPath('zdz'))



