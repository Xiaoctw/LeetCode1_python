class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        i=0
        k=0
        for i in range(len(S)):
            if S[i] in J:
                k=k+1
        return k

