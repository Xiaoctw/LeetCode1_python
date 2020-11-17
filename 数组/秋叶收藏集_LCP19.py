class Solution:
    def minimumOperations(self, leaves: str) -> int:
        sum_r,sum_y=[],[]
        if leaves[0]=='r':
            sum_r.append(1)
            sum_y.append(0)
        else:
            sum_r.append(0)
            sum_y.append(1)
        sub_val=sum_y[0]-sum_r[0]
        res=float('inf')
        for j in range(1,len(leaves)-1):
            if leaves[j]=='r':
                sum_r.append(sum_r[-1]+1)
                sum_y.append(sum_y[-1])
            else:
                sum_r.append(sum_r[-1])
                sum_y.append(sum_y[-1]+1)
            res=min(res,sum_r[j]-sum_y[j]+sub_val)
            sub_val=min(sub_val,sum_y[j]-sum_r[j])
        if leaves[len(leaves)-1]=='y':
            res+=(sum_y[-1]+1)
        else:
            res+=sum_y[-1]
        return res




if __name__ == '__main__':
    sol = Solution()
    leaves = "ryyyyyr"
    print(sol.minimumOperations(leaves))
