from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i = 0
        len1 = len(formula)
        tem_dic = defaultdict(int)
        stack = []
        set1 = set('ABCDEFGHIGKLMNOPQRSTUVWXYZ')
        set2 = set('abcdefghigklmnopqrstuvwxyz')
        set3 = set('0123456789')
        set4 = set()
        while i < len1:
            if formula[i] in set1:
                c = formula[i]
                i += 1
                while i < len1 and formula[i] in set2:
                    c += formula[i]
                    i += 1
                set4.add(c)
                if i < len1 and formula[i] in set3:
                    val = int(formula[i])
                    i += 1
                    while i < len1 and formula[i] in set3:
                        val = val * 10 + int(formula[i])
                        i += 1
                    tem_dic[c] += val
                else:
                    tem_dic[c] += 1
            elif formula[i] == '(':
                stack.append(tem_dic)
                tem_dic = defaultdict(int)
                i += 1
            else:
                i += 1
                if i < len1 and formula[i] in set3:
                    val = int(formula[i])
                    i += 1
                    while i < len1 and formula[i] in set3:
                        val = val * 10 + int(formula[i])
                        i += 1
                    for key in tem_dic:
                        tem_dic[key] = tem_dic[key] * val
                res_dic = stack.pop()
                for key in res_dic:
                    tem_dic[key] = tem_dic[key] + res_dic[key]
        res = []
        list1 = list(set4)
        list1.sort()
       # print(tem_dic)
        for val in list1:
            if tem_dic[val] > 1:
                res.append(val + str(tem_dic[val]))
            else:
                res.append(val)
        return ''.join(res)

if __name__ == '__main__':
    s="(((U42Se42Fe10Mc31Rh49Pu49Sb49)49V39Tm50Zr44Og6)33((W2Ga48Tm14Eu46Mt12)23(RuRnMn11)7(Yb15Lu34Ra19CuTb2)47" \
      "(Md38BhCu48Db15Hf12Ir40)7CdNi21(Db40Zr24Tc27SrBk46Es41DsI37Np9Lu16)46(Zn49Ho19RhClF9Tb30SiCuYb16)15)37(Cr48(Ni31)25" \
      "(La8Ti17Rn6Ce35)36" \
      "(Sg42Ts32Ca)37Tl6Nb47Rh32NdGa18Cm10Pt49(Ar37RuSb30Cm32Rf28B39Re7F36In19Zn50)46)38(Rh19Md23No22PoTl35Pd35Hg)41)50"
    sol=Solution()
    print(sol.countOfAtoms(s))