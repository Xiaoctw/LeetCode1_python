from typing import *
import time
import matplotlib.pyplot as plt

class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(2,n+1):
            for j in  range(i):
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j])
        return dp[n]

class Solution1:
    def integerBreak(self, n: int) -> int:
        if n<4:
            return n-1
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(3,n+1):
            dp[i]=max(2*(i-2),2*dp[i-2],3*(i-3),3*dp[i-3])
        return dp[n]

class Solution2:
    def integerBreak(self,n:int)->int:
        if n<4:
            return n-1
        quotient,remainder=n//3,n%3
        if remainder==0:
            return 3**quotient
        elif remainder==1:
            return 3**(quotient-1)*4
        else:
            return 3**quotient*2



if __name__ == '__main__':
    sol=Solution()
    sol1=Solution1()
    sol2=Solution2()
    xs=list(range(30000,100000,5000))
    times1,times2,times3=[],[],[]
    for num in xs:
        # time1=time.time()
        # sol.integerBreak(num)
        # time2=time.time()
        # times1.append(time2-time1)
        # print(time2-time1)
        time1 = time.time()
        sol1.integerBreak(num)
        time2 = time.time()
        print(time2 - time1)
        times2.append(time2 - time1)
        time1 = time.time()
        sol2.integerBreak(num)
        time2 = time.time()
        print(time2 - time1)
        times3.append(time2 - time1)
    # plt.plot(xs, times1, color='g', label='sol', lw=2, ls='-')
    # plt.scatter(xs, times1, color='m', marker='<')
    plt.plot(xs, times2, color='b', label='sol1', lw=2, ls='--')
    plt.scatter(xs, times2, color='y', marker='^')
    plt.plot(xs, times3, color='r', label='sol2', lw=2, ls='--')
    plt.scatter(xs, times3, color='y', marker='>')
    plt.legend()
    plt.title('no title')
    plt.show()

