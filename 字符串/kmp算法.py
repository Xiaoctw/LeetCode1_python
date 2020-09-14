from typing import *


def getNext(substr):
    """
    该函数的核心为构建next数组，该数组表示的是模式串开头有多少个和
    当前位置之前字符匹配
    比如模式串为abcabc
    next数组为：[0,0,0,1,2,3]
    :param substr:
    :return:
    """
    idx, m = 0, len(substr)
    pnext = [0] * m
    i = 1
    while i < m:
        if substr[i] == substr[idx]:
            pnext[i] = idx + 1
            idx += 1
            i += 1
        else:
            if idx != 0:
                idx = pnext[idx - 1]
            else:
                pnext[i] = 0
                i += 1
    return pnext


def kmp(s: str, t: str):
    pnext = getNext(t)
    print(pnext)
    m, n = len(t), len(s)
    i, j = 0, 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = pnext[j - 1]
            else:
                i += 1
    if j == m:
        return i - j
    return -1

if __name__ == '__main__':
    t = 'abac'
    s = 'abdcdabcabcabacababacab'
    print(kmp(s, t))
